#!/usr/bin/env python3
"""
Extract EIA Energielijst 2025 data using Claude's native PDF reading.
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

class EIARequirement(BaseModel):
    """Technical requirement for an EIA code"""
    name: str
    value: str
    description: Optional[str] = None

class EIACode(BaseModel):
    """Structured EIA code entry"""
    code: str = Field(description="EIA code (e.g., 211102, 310000)")
    title: str = Field(description="Short title/name of the bedrijfsmiddel")
    description: str = Field(description="Full description of what this is for")
    category: str = Field(description="Category letter (A, B, C, D, E, F, G)")
    chapter: str = Field(description="Chapter name (e.g., 'Verwarmen', 'Koelen/vriezen')")
    requirements: List[EIARequirement] = Field(default_factory=list, description="Technical requirements")
    subsidy_percentage: Optional[float] = Field(default=0.40, description="Subsidy percentage (usually 40%)")
    min_investment: Optional[float] = Field(default=2500.0, description="Minimum investment amount")
    max_investment: Optional[float] = Field(default=None, description="Maximum investment amount per unit")
    keywords: List[str] = Field(default_factory=list, description="Keywords for matching")
    notes: Optional[str] = Field(default=None, description="Additional notes or toelichting")
    page: int = Field(description="Page number in the PDF")

class EIADatabase(BaseModel):
    """Complete EIA database"""
    version: str = "2025"
    source: str = "Brochure-EIA-Energielijst2025.pdf"
    budget: int = 431_000_000
    updated: str = "2025-01-01"
    codes: List[EIACode]


def extract_eia_from_pdf(pdf_path: str, output_path: str, start_page: int = 1, end_page: Optional[int] = None):
    """
    Extract EIA codes from PDF using Claude.

    Args:
        pdf_path: Path to the EIA PDF file
        output_path: Path to save the extracted JSON data
        start_page: Starting page number (1-indexed)
        end_page: Ending page number (None = all pages)
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

Lees dit EIA Energielijst 2025 PDF document en extraheer ALLE EIA codes met hun details.

Voor elke EIA code, extraheer:
1. **code**: De EIA code (bijv. 211102, 310000, 220101)
2. **title**: Korte titel (bijv. "Warmtepompboiler", "Warmtepomp (luchtgerelateerd)")
3. **description**: Volledige omschrijving ("Bestemd voor: ...")
4. **category**: Categorie letter (A, B, C, D, E, F, G)
5. **chapter**: Hoofdstuk naam (bijv. "Verwarmen", "Koelen/vriezen", "Verlichting")
6. **requirements**: Lijst van technische eisen met name, waarde, beschrijving
   - Bijvoorbeeld: {"name": "SCOP", "value": "≥ 4.6", "description": "..."}
   - Bijvoorbeeld: {"name": "COP", "value": "≥ 3.0", "description": "..."}
   - Bijvoorbeeld: {"name": "vermogen", "value": "≤70kW", "description": "..."}
7. **subsidy_percentage**: Percentage (meestal 0.40 = 40%)
8. **min_investment**: Minimum investering (meestal €2.500)
9. **max_investment**: Maximum investering per eenheid (indien vermeld)
10. **keywords**: Relevante zoekwoorden (bijv. ["warmtepomp", "lucht-water", "SCOP"])
11. **notes**: Extra notities of toelichtingen
12. **page**: Paginanummer in het PDF

BELANGRIJKE INSTRUCTIES:
- Extraheer ALLE codes die beginnen met cijfers (210000, 211102, 220101, etc.)
- Negeer hoofdstuk-titels zonder codes
- Let op speciale notaties: [W] = wijziging, [GEWIJZIGD] = gewijzigd, [NIEUW] = nieuw
- Extraheer ALLE technische eisen nauwkeurig (SCOP, COP, vermogen, energielabel, etc.)
- Voor codes met sub-categorieën (a, b, c, d), extraheer elke variant als aparte requirement
- Bewaar de Nederlandse tekst zoals deze is
- Als een maximum investeringsbedrag wordt genoemd (bijv. "€ 1.400 per kWth"), voeg dit toe

Begin met pagina's vanaf ongeveer pagina 18 waar de eigenlijke codes beginnen.
Sla inhoudsopgave en algemene informatie over.

Return het resultaat als een JSON array van EIA code objecten.
"""

    print("🤖 Calling Claude API to extract EIA codes...")
    print("⏳ This may take 30-60 seconds for the full PDF...")

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
    # Look for JSON array in the response
    try:
        # Try to find JSON in the response
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']') + 1

        if start_idx >= 0 and end_idx > start_idx:
            json_str = response_text[start_idx:end_idx]
            codes_data = json.loads(json_str)

            print(f"✅ Successfully parsed {len(codes_data)} EIA codes")

            # Create the database object
            database = EIADatabase(codes=codes_data)

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
            print(f"   Budget: €{database.budget:,}")
            print(f"   Total codes: {len(database.codes)}")

            # Show sample
            if database.codes:
                print("\n📋 Sample entry:")
                sample = database.codes[0]
                print(f"   Code: {sample.code}")
                print(f"   Title: {sample.title}")
                print(f"   Category: {sample.category}")
                print(f"   Requirements: {len(sample.requirements)}")

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
    pdf_path = project_root / "ruwe_data" / "Brochure-EIA-Energielijst2025.pdf"
    output_path = project_root / "data" / "subsidies" / "eia_2025.json"

    # Check if PDF exists
    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return

    # Extract data
    database = extract_eia_from_pdf(
        pdf_path=str(pdf_path),
        output_path=str(output_path)
    )

    if database:
        print("\n✅ EIA extraction completed successfully!")
        print(f"📊 Extracted {len(database.codes)} codes")
    else:
        print("\n❌ EIA extraction failed. Check debug output.")


if __name__ == "__main__":
    main()
