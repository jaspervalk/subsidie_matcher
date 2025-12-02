"""
Parse EIA and MIA/Vamil brochures into code-based blocks with page and category.

This script does NOT invent values; it slices the brochure text into blocks that
start with a code (e.g., 310000, 211102, B1234) and keeps the following lines
until the next code. Output is meant for human review before use.

Outputs:
- data/subsidies/eia_extracted_blocks.json
- data/subsidies/mia_extracted_blocks.json
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "subsidies"

EIA_CODE_RE = re.compile(r"^([0-9]{6}[A-Z]?|[A-Z][0-9]{5,6})\b")
# MIA/Vamil codes are often 4–6 digits and can have a leading letter.
MIA_CODE_RE = re.compile(r"^([0-9]{4,6}[A-Z]?|[A-Z][0-9]{4,6})\b")

# Category headings to help tag sections (heuristic)
EIA_CATEGORY_HEADINGS = {
    "A.": "A",
    "B.": "B",
    "C.": "C",
    "D.": "D",
    "E.": "E",
    "F.": "F",
}


def detect_category(line: str, current: Optional[str], headings: Dict[str, str]) -> Optional[str]:
    for prefix, cat in headings.items():
        if line.strip().startswith(prefix):
            return cat
    return current


def parse_pdf(pdf_path: Path, headings: Dict[str, str], code_re: re.Pattern[str]) -> List[Dict[str, Any]]:
    blocks: List[Dict[str, Any]] = []
    with pdfplumber.open(pdf_path) as pdf:
        current_block: Optional[Dict[str, Any]] = None
        current_category: Optional[str] = None
        for page_index, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            lines = [ln.rstrip() for ln in text.splitlines() if ln.strip()]
            for ln in lines:
                stripped = ln.strip()
                current_category = detect_category(stripped, current_category, headings)
                m = code_re.match(stripped)
                if m:
                    # start new block
                    if current_block:
                        blocks.append(current_block)
                    code = m.group(1)
                    title = stripped[len(code) :].strip()
                    current_block = {
                        "code": code,
                        "title": title,
                        "lines": [stripped],
                        "page": page_index,
                        "category": current_category,
                    }
                else:
                    if current_block:
                        current_block["lines"].append(stripped)
        if current_block:
            blocks.append(current_block)
    # post-process: join lines
    for b in blocks:
        b["text"] = "\\n".join(b["lines"])
        b.pop("lines", None)
    return blocks


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(payload)} blocks to {path}")


def main() -> None:
    eia_pdf = ROOT / "Brochure-EIA-Energielijst2025.pdf"
    mia_pdf = ROOT / "BrochureMilieulijst2025v3.pdf"

    eia_blocks = parse_pdf(eia_pdf, EIA_CATEGORY_HEADINGS, EIA_CODE_RE)
    write_json(DATA_DIR / "eia_extracted_blocks.json", eia_blocks)

    # MIA headings are less consistent; reuse same detection for now.
    mia_blocks = parse_pdf(mia_pdf, EIA_CATEGORY_HEADINGS, MIA_CODE_RE)
    write_json(DATA_DIR / "mia_extracted_blocks.json", mia_blocks)


if __name__ == "__main__":
    main()
