"""
Heuristic extraction of EIA and MIA/Vamil list entries from the brochures.

This does NOT invent or transform values; it collects text snippets with page
references so they can be reviewed and curated into structured data.

Outputs:
- data/subsidies/eia_candidates.json
- data/subsidies/mia_candidates.json
Each candidate has: page, block_text, and the first line for quick scanning.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List

import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "subsidies"


CODE_START = re.compile(r"^[A-Z]?[0-9]{3,}")


def extract_blocks(pdf_path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            text = page.extract_text() or ""
            lines = [ln.rstrip() for ln in text.splitlines() if ln.strip()]
            blocks: List[List[str]] = []
            current: List[str] = []
            for ln in lines:
                if CODE_START.match(ln):
                    if current:
                        blocks.append(current)
                    current = [ln]
                else:
                    if current:
                        current.append(ln)
            if current:
                blocks.append(current)

            for block in blocks:
                items.append(
                    {
                        "page": i,
                        "first_line": block[0],
                        "block_text": "\n".join(block),
                    }
                )
    return items


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(payload)} blocks to {path}")


def main() -> None:
    eia_pdf = ROOT / "Brochure-EIA-Energielijst2025.pdf"
    mia_pdf = ROOT / "BrochureMilieulijst2025v3.pdf"

    eia_blocks = extract_blocks(eia_pdf)
    write_json(DATA_DIR / "eia_candidates.json", eia_blocks)

    mia_blocks = extract_blocks(mia_pdf)
    write_json(DATA_DIR / "mia_candidates.json", mia_blocks)


if __name__ == "__main__":
    main()
