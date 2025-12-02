#!/usr/bin/env python3
"""
Extract MIA/Vamil Milieulijst 2025 data using text extraction from PDF first.
This avoids the 200k token limit by extracting text first with pdfplumber.
"""

import anthropic
import json
import os
from pathlib import Path
import pdfplumber
from dotenv import load_dotenv

load_dotenv()


def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF using pdfplumber"""
    print(f"📄 Extracting text from PDF...")

    text_content = []
    with pdfplumber.open(pdf_path) as pdf:
        total_pages = len(pdf.pages)
        print(f"   Total pages: {total_pages}")

        # Start from page 15 (where actual codes begin, 0-indexed = 14)
        for page_num in range(14, total_pages):
            page = pdf.pages[page_num]
            text = page.extract_text()
            if text:
                text_content.append(f"\n=== PAGE {page_num + 1} ===\n{text}")

            if (page_num + 1) % 10 == 0:
                print(f"   Processed {page_num + 1}/{total_pages} pages...")

    full_text = "\n".join(text_content)
    print(f"✅ Extracted {len(full_text)} characters")
    print(f"   Estimated tokens: ~{len(full_text) // 4}")

    return full_text


def structure_mia_data(text: str, output_path: str):
    """Use Claude to structure the extracted text into JSON"""
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # Always process in chunks for better reliability
    print(f"\n📦 Processing text in chunks...")

    # Split by page markers
    pages = text.split("=== PAGE")

    all_codes = []
    chunk_size = 10  # Process 10 pages at a time

    for i in range(0, len(pages), chunk_size):
        chunk_pages = pages[i:i+chunk_size]
        chunk_text = "=== PAGE".join(chunk_pages)

        if len(chunk_text.strip()) < 100:  # Skip empty chunks
            continue

        chunk_num = i//chunk_size + 1
        total_chunks = (len(pages) + chunk_size - 1) // chunk_size
        print(f"\n📄 Chunk {chunk_num}/{total_chunks} (pages ~{i+15} to ~{min(i+chunk_size+14, len(pages)+14)})...")

        codes = process_text_chunk(client, chunk_text, i+15)
        if codes:
            all_codes.extend(codes)
            print(f"   ✅ Found {len(codes)} codes")
        else:
            print(f"   ⚠️  No codes found in this chunk")

    print(f"\n✅ Total codes extracted: {len(all_codes)}")

    # Save results
    database = {
        "version": "2025",
        "source": "BrochureMilieulijst2025v3.pdf",
        "mia_budget": 189_000_000,
        "vamil_budget": 20_000_000,
        "updated": "2024-12-01",
        "codes": all_codes
    }

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(database, f, ensure_ascii=False, indent=2)

    print(f"\n💾 Saved to: {output_path}")
    print(f"📊 Total MIA/Vamil codes: {len(all_codes)}")

    # Show MIA percentage distribution
    mia_percentages = {}
    for code in all_codes:
        pct = code.get('mia_percentage')
        if pct:
            mia_percentages[pct] = mia_percentages.get(pct, 0) + 1

    if mia_percentages:
        print(f"\n📊 MIA percentage distribution:")
        for pct, count in sorted(mia_percentages.items()):
            print(f"   {pct}%: {count} codes")

    return database


def process_text_chunk(client, text_chunk: str, start_page: int):
    """Process a chunk of text with Claude"""

    prompt = f"""
Je krijgt tekst uit de MIA/Vamil Milieulijst 2025 PDF.

Extraheer ALLE MIA/Vamil codes en return als VALID JSON array.

Schema per code:
{{
  "code": "A 1100",
  "title": "Circulaire woning",
  "description": "Bestemd voor...",
  "category": "A",
  "chapter": "1. Grondstoffen- en watergebruik",
  "mia_percentage": 36,
  "vamil_percentage": 75,
  "page": 20
}}

HOOFDSTUKKEN:
1. Grondstoffen- en watergebruik
2. Voedselvoorziening en landbouwproductie
3. Mobiliteit
4. Klimaat en lucht
5. Gebouwde omgeving en klimaatadaptatie

MIA percentages: 13, 27, 36, of 45
Vamil percentage: meestal 75

BELANGRIJK:
- Extraheer codes met LETTER + SPATIE + NUMMER (A 1100, B 2220, E 5215, etc.)
- Extraheer het JUISTE MIA percentage voor elke code (staat vaak als "MIA: 36%" of "13/27/36/45")
- Vamil is meestal 75%, maar check of het expliciet vermeld staat
- Return ALLEEN valid JSON array, geen tekst eromheen
- Gebruik double quotes, geen single quotes
- Escape special characters in strings

TEKST:
{text_chunk[:50000]}
"""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=8000,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response_text = message.content[0].text.strip()

        # Try to find and extract JSON
        start_idx = response_text.find('[')
        end_idx = response_text.rfind(']') + 1

        if start_idx >= 0 and end_idx > start_idx:
            json_str = response_text[start_idx:end_idx]

            # Try to parse
            try:
                codes = json.loads(json_str)
                return codes if isinstance(codes, list) else []
            except json.JSONDecodeError as je:
                print(f"   ⚠️  JSON parse error: {str(je)[:100]}")
                # Try to fix common issues
                json_str = json_str.replace("'", '"')  # Replace single quotes
                json_str = json_str.replace('\n', ' ')  # Remove newlines
                try:
                    codes = json.loads(json_str)
                    return codes if isinstance(codes, list) else []
                except:
                    print(f"   ⚠️  Could not fix JSON")
                    return []
        else:
            print(f"   ⚠️  No JSON array found in response")
            return []

    except Exception as e:
        print(f"   ❌ Error: {str(e)[:200]}")
        return []


def main():
    """Main execution"""
    project_root = Path(__file__).parent.parent
    pdf_path = project_root / "ruwe_data" / "BrochureMilieulijst2025v3.pdf"
    output_path = project_root / "data" / "subsidies" / "mia_vamil_2025.json"

    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}")
        return

    # Step 1: Extract text
    text = extract_text_from_pdf(str(pdf_path))

    # Step 2: Structure with Claude
    database = structure_mia_data(text, str(output_path))

    if database and database['codes']:
        print(f"\n✅ MIA/Vamil extraction completed successfully!")
        print(f"📋 Sample: {database['codes'][0]['code']} - {database['codes'][0]['title']}")
        if database['codes'][0].get('mia_percentage'):
            print(f"   MIA: {database['codes'][0]['mia_percentage']}%")
    else:
        print("\n❌ Extraction failed or no codes found.")


if __name__ == "__main__":
    main()
