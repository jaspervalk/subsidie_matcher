#!/usr/bin/env python3
"""
Extract MIA/Vamil Milieulijst 2025 data using Claude's native PDF reading.
This script uses the Anthropic API to read the PDF directly and extract structured data.
"""

import anthropic
import json
import os
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MIARequirement(BaseModel):
    """Technical requirement for a MIA code"""
    name: str
    value: str
    description: Optional[str] = None

class MIACode(BaseModel):
    """Structured MIA/Vamil code entry"""
    code: str = Field(description="MIA code (e.g., A 1100, B 2220, E 5215)")
    title: str = Field(description="Short title/name of the bedrijfsmiddel")
    description: str = Field(description="Full description of what this is for")
    category: str = Field(description="Category letter (A, B, C, D, E, F, G)")
    chapter: str = Field(description="Chapter name and number")
    mia_percentage: Optional[int] = Field(default=None, description="MIA percentage (13, 27, 36, 45)")
    vamil_percentage: Optional[int] = Field(default=75, description="Vamil percentage (usually 75%)")
    requirements: List[MIARequirement] = Field(default_factory=list, description="Technical requirements")
    max_investment: Optional[float] = Field(default=25_000_000, description="Max investment (€25M default)")
    keywords: List[str] = Field(default_factory=list, description="Keywords for matching")
    notes: Optional[str] = Field(default=None, description="Additional notes or toelichting")
    page: int = Field(description="Page number in the PDF")

class MIADatabase(BaseModel):
    """Complete MIA/Vamil database"""
    version: str = "2025"
    source: str = "BrochureMilieulijst2025v3.pdf"
    mia_budget: int = 189_000_000
    vamil_budget: int = 20_000_000
    updated: str = "2024-12-01"
    codes: List[MIACode]


def extract_mia_from_pdf(pdf_path: str, output_path: str):
    """
    Extract MIA/Vamil codes from PDF using Claude.

    Args:
        pdf_path: Path to the MIA PDF file
        output_path: Path to save the extracted JSON data
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # Read PDF file
    with open(pdf_path, "rb") as f:
        pdf_data = f.read()

    print(f"📄 Reading PDF: {pdf_path}")
    print(f"📊 File size: {len(pdf_data) / 1024 / 1024:.2f} MB")

    # Create the extraction prompt
    prompt = """
Je bent een expert in het extraheren van gestructureerde data uit Nederlandse overheidssubsidie documenten.

Lees dit MIA/Vamil Milieulijst 2025 PDF document en extraheer ALLE MIA/Vamil codes met hun details.

Voor elke MIA/Vamil code, extraheer:
1. **code**: De MIA code (bijv. "A 1100", "B 2220", "E 5215")
2. **title**: Korte titel (bijv. "Circulaire woning", "Elektrische vrachtwagen")
3. **description**: Volledige omschrijving ("Bestemd voor: ...")
4. **category**: Categorie letter (A, B, C, D, E, F, G)
5. **chapter**: Hoofdstuk nummer en naam (bijv. "1. Grondstoffen- en watergebruik", "3. Mobiliteit")
6. **mia_percentage**: MIA percentage (13, 27, 36, of 45)
7. **vamil_percentage**: Vamil percentage (meestal 75)
8. **requirements**: Lijst van technische eisen met name, waarde, beschrijving
9. **max_investment**: Maximum investering (standaard €25 miljoen per bedrijfsmiddel)
10. **keywords**: Relevante zoekwoorden
11. **notes**: Extra notities of toelichtingen
12. **page**: Paginanummer in het PDF

BELANGRIJKE INSTRUCTIES:
- Extraheer ALLE codes die beginnen met een letter gevolgd door een nummer (A 1100, B 2220, etc.)
- Let op de verschillende MIA percentages: 13%, 27%, 36%, 45%
- Sommige codes hebben alleen MIA, sommige hebben alleen Vamil, sommige hebben beide
- Voor codes met sub-categorieën (a, b, c), extraheer elke variant als aparte requirement
- Bewaar de Nederlandse tekst zoals deze is
- Let op speciale maximumbedragen per bedrijfsmiddel
- Negeer de algemene toelichting en inhoudsopgave

HOOFDSTUKKEN:
1. Grondstoffen- en watergebruik
2. Voedselvoorziening en landbouwproductie
3. Mobiliteit
4. Klimaat en lucht
5. Gebouwde omgeving en klimaatadaptatie

Begin met extraheren vanaf ongeveer pagina 15 waar de eigenlijke codes beginnen.

Return het resultaat als een JSON array van MIA code objecten.
"""

    print("🤖 Calling Claude API to extract MIA/Vamil codes...")
    print("⏳ This may take 60-90 seconds for the full PDF...")

    # Encode PDF to base64
    import base64
    pdf_base64 = base64.standard_b64encode(pdf_data).decode("utf-8")

    # Call Claude API with PDF
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,  # Large output needed
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
                        }
                    },
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )

    # Extract the response
    response_text = message.content[0].text

    print("✅ Received response from Claude")
    print(f"📝 Response length: {len(response_text)} characters")

    # Parse the JSON response
    try:
        # Try to find JSON in the response
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']') + 1

        if start_idx >= 0 and end_idx > start_idx:
            json_str = response_text[start_idx:end_idx]
            codes_data = json.loads(json_str)

            print(f"✅ Successfully parsed {len(codes_data)} MIA/Vamil codes")

            # Create the database object
            database = MIADatabase(codes=codes_data)

            # Save to file
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(database.model_dump(), f, ensure_ascii=False, indent=2)

            print(f"💾 Saved to: {output_path}")
            print(f"✅ Total codes extracted: {len(database.codes)}")

            # Print summary
            print("\n📊 SUMMARY:")
            print(f"   Version: {database.version}")
            print(f"   MIA Budget: €{database.mia_budget:,}")
            print(f"   Vamil Budget: €{database.vamil_budget:,}")
            print(f"   Total codes: {len(database.codes)}")

            # Count by MIA percentage
            mia_percentages = {}
            for code in database.codes:
                pct = code.mia_percentage
                mia_percentages[pct] = mia_percentages.get(pct, 0) + 1

            print("\n   MIA percentage distribution:")
            for pct, count in sorted(mia_percentages.items()):
                print(f"      {pct}%: {count} codes")

            # Show sample
            if database.codes:
                print("\n📋 Sample entry:")
                sample = database.codes[0]
                print(f"   Code: {sample.code}")
                print(f"   Title: {sample.title}")
                print(f"   MIA: {sample.mia_percentage}%")
                print(f"   Chapter: {sample.chapter}")

            return database

        else:
            print("❌ Could not find JSON array in response")
            print("Response preview:", response_text[:500])

            # Save raw response for debugging
            debug_file = output_path.replace('.json', '_debug.txt')
            with open(debug_file, 'w', encoding='utf-8') as f:
                f.write(response_text)
            print(f"💾 Saved debug output to: {debug_file}")

            return None

    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        print("Response preview:", response_text[:500])

        # Save raw response for debugging
        debug_file = output_path.replace('.json', '_debug.txt')
        with open(debug_file, 'w', encoding='utf-8') as f:
            f.write(response_text)
        print(f"💾 Saved debug output to: {debug_file}")

        return None


def main():
    """Main execution"""
    # Paths
    project_root = Path(__file__).parent.parent
    pdf_path = project_root / "ruwe_data" / "BrochureMilieulijst2025v3.pdf"
    output_path = project_root / "data" / "subsidies" / "mia_vamil_2025.json"

    # Check if PDF exists
    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return

    # Extract data
    database = extract_mia_from_pdf(
        pdf_path=str(pdf_path),
        output_path=str(output_path)
    )

    if database:
        print("\n✅ MIA/Vamil extraction completed successfully!")
        print(f"📊 Extracted {len(database.codes)} codes")
    else:
        print("\n❌ MIA/Vamil extraction failed. Check debug output.")


if __name__ == "__main__":
    main()
