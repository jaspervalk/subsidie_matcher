"""
Extract raw tables from the EIA and MIA/Vamil brochures without transforming values.

This is intentionally lossless/raw so values can be verified against the PDFs.
Outputs:
- data/subsidies/eia_tables_raw.json
- data/subsidies/mia_tables_raw.json
Each entry includes page number and the unmodified table cells.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

import pdfplumber

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "subsidies"


def extract_tables(pdf_path: Path) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            tables = page.extract_tables()
            if not tables:
                continue
            items.append(
                {
                    "page": i,
                    "tables": tables,
                }
            )
    return items


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(payload)} page tables to {path}")


def main() -> None:
    eia_pdf = ROOT / "Brochure-EIA-Energielijst2025.pdf"
    mia_pdf = ROOT / "BrochureMilieulijst2025v3.pdf"

    eia_tables = extract_tables(eia_pdf)
    write_json(DATA_DIR / "eia_tables_raw.json", eia_tables)

    mia_tables = extract_tables(mia_pdf)
    write_json(DATA_DIR / "mia_tables_raw.json", mia_tables)


if __name__ == "__main__":
    main()
