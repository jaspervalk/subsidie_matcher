#!/usr/bin/env python3
"""
Extract EIA Energielijst 2025 data using Claude with extended thinking.
Uses a smarter approach that processes the PDF efficiently.
"""

import anthropic
import json
import os
from pathlib import Path
from typing import List
import base64
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def extract_eia_smart(pdf_path: str, output_path: str):
    """
    Extract EIA codes using extended thinking model for better accuracy.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # Read PDF file
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    pdf_base64 = base64.standard_b64encode(pdf_data).decode("utf-8")

    print(f"📄 Reading PDF: {pdf_path}")
    print(f"📊 File size: {len(pdf_data) / 1024 / 1024:.2f} MB")

    # Simpler prompt focused on structured extraction
    prompt = """
Extraheer ALLE EIA codes uit dit PDF document en return ze als een JSON array.

Voor elke code, geef terug:
{
  "code": "211102",
  "title": "Warmtepompboiler",
  "description": "Volledige beschrijving...",
  "category": "A",
  "chapter": "Verwarmen",
  "requirements": [
    {"name": "COP", "value": "≥ 3.0"}
  ],
  "subsidy_percentage": 0.40,
  "min_investment": 2500,
  "max_investment_per_unit": null,
  "keywords": ["warmtepomp", "boiler", "tapwater"],
  "page": 20
}

Extraheer ALLE codes die beginnen met cijfers (210000, 211102, etc.).
Begin vanaf pagina 18. Negeer inhoudsopgave.
Return ALLEEN de JSON array, geen extra tekst.
"""

    print("🤖 Calling Claude API with extended thinking...")
    print("⏳ This may take 60-120 seconds...")

    try:
        # Use extended thinking model for complex extraction
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=16000,
            thinking={
                "type": "enabled",
                "budget_tokens": 10000
            },
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "document",
                            "source": {
                                "type": "base64",
                                "media_type": "application/pdf",
                                "data": pdf_base64
                            },
                            "cache_control": {"type": "ephemeral"}
                        },
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        )

        # Extract response (skip thinking blocks)
        response_text = ""
        for block in message.content:
            if block.type == "text":
                response_text += block.text

        print("✅ Received response from Claude")
        print(f"📝 Response length: {len(response_text)} characters")

        # Parse JSON
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']') + 1

        if start_idx >= 0 and end_idx > start_idx:
            json_str = response_text[start_idx:end_idx]
            codes_data = json.loads(json_str)

            print(f"✅ Successfully parsed {len(codes_data)} EIA codes")

            # Create output structure
            database = {
                "version": "2025",
                "source": "Brochure-EIA-Energielijst2025.pdf",
                "budget": 431_000_000,
                "updated": "2025-01-01",
                "codes": codes_data
            }

            # Save to file
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(database, f, ensure_ascii=False, indent=2)

            print(f"💾 Saved to: {output_path}")
            print(f"\n📊 SUMMARY:")
            print(f"   Total codes: {len(codes_data)}")
            print(f"   Budget: €{database['budget']:,}")

            # Show sample
            if codes_data:
                print(f"\n📋 Sample: {codes_data[0]['code']} - {codes_data[0]['title']}")

            return database

        else:
            print("❌ Could not find JSON in response")
            debug_file = output_path.replace('.json', '_debug.txt')
            with open(debug_file, 'w', encoding='utf-8') as f:
                f.write(response_text)
            print(f"💾 Debug output: {debug_file}")
            return None

    except anthropic.BadRequestError as e:
        print(f"❌ API Error: {e}")
        print("\nℹ️  PDF might be too large. Trying alternative approach...")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


def main():
    """Main execution"""
    project_root = Path(__file__).parent.parent
    pdf_path = project_root / "ruwe_data" / "Brochure-EIA-Energielijst2025.pdf"
    output_path = project_root / "data" / "subsidies" / "eia_2025.json"

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return

    database = extract_eia_smart(str(pdf_path), str(output_path))

    if database:
        print("\n✅ EIA extraction completed!")
    else:
        print("\n❌ Extraction failed. Check debug output.")


if __name__ == "__main__":
    main()
