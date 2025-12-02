"""
Parse ISDE meldcode Excel files into normalized JSON for matching.

Outputs JSON files under data/subsidies:
- isde_warmtepompen.json
- isde_zonneboilers.json
- isde_isolatiematerialen.json
- isde_hoogrendementsglas.json
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data" / "subsidies"


def _parse_eur(value: Any) -> Optional[float]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    s = str(value)
    if not s.strip():
        return None
    # Remove currency symbols and thousand separators, normalize decimal comma.
    cleaned = re.sub(r"[€\\s]", "", s)
    cleaned = cleaned.replace(".", "")  # dots are thousands in NL notation here
    cleaned = cleaned.replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def _parse_number(value: Any) -> Optional[float]:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return None
    s = str(value).strip()
    if not s:
        return None
    s = s.replace(",", ".")
    # Drop non-numeric (except dot, minus).
    s = re.sub(r"[^0-9.-]", "", s)
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _write_json(filename: str, rows: List[Dict[str, Any]]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / filename
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(rows)} items to {out_path}")


def parse_warmtepompen() -> None:
    xls_path = ROOT / "Meldcodelijst Warmtepompen - November 2025.xlsx"
    df = pd.read_excel(xls_path, sheet_name="Meldcodes")

    rows: List[Dict[str, Any]] = []
    for _, r in df.iterrows():
        item = {
            "scheme": "ISDE",
            "category": "warmtepomp",
            "meldcode": str(r["MELDCODE"]).strip(),
            "manufacturer": str(r["Fabrikant / Merknaam"]).strip(),
            "model": str(r["Model"]).strip(),
            "amount_eur": _parse_eur(r["Subsidiebedrag"]),
            "source": {"file": xls_path.name, "sheet": "Meldcodes"},
            "attributes": {
                "power_kw": _parse_number(r["Vermogen (KW)"]),
                "refrigerant": str(r["NAAM_KOUDEMIDDEL"]).strip(),
                "gwp": _parse_number(r["GWP"]),
                "type": str(r["Categorie"]).strip(),
            },
        }
        rows.append(item)

    _write_json("isde_warmtepompen.json", rows)


def parse_zonneboilers() -> None:
    xls_path = ROOT / "Meldcodelijst Zonneboilers - November 2025.xlsx"
    df = pd.read_excel(xls_path, sheet_name="Meldcodes")

    rows: List[Dict[str, Any]] = []
    for _, r in df.iterrows():
        item = {
            "scheme": "ISDE",
            "category": "zonneboiler",
            "meldcode": str(r["MELDCODE"]).strip(),
            "manufacturer": str(r["Fabrikant / Merknaam"]).strip(),
            "model": str(r["Model"]).strip(),
            "amount_eur": _parse_eur(r["Subsidiebedrag"]),
            "source": {"file": xls_path.name, "sheet": "Meldcodes"},
            "attributes": {
                "jaarproductie_kwh": _parse_number(r["Jaarproductie (KWh)"]),
                "oppervlakte": str(r["Oppervlakte"]).strip(),
            },
        }
        rows.append(item)

    _write_json("isde_zonneboilers.json", rows)


def parse_isolatie() -> None:
    xls_path = ROOT / "Meldcodelijst Isolatiematerialen - November 2025.xlsx"
    df = pd.read_excel(xls_path, sheet_name="Meldcodes")

    rows: List[Dict[str, Any]] = []
    for _, r in df.iterrows():
        item = {
            "scheme": "ISDE",
            "category": "isolatie",
            "meldcode": str(r["MELDCODE"]).strip(),
            "manufacturer": str(r["Fabrikant / Merknaam"]).strip(),
            "model": str(r["Model"]).strip(),
            "source": {"file": xls_path.name, "sheet": "Meldcodes"},
            "attributes": {
                "materiaal": str(r["NAAM_MATERIAAL"]).strip(),
                "min_rd": _parse_number(r["MIN_WAARDE_RD"]),
                "min_dikte_mm": _parse_number(r["MIN_DIKTE_MM"]),
                "biobased_bonus": str(r["BioBased Bonus"]).strip(),
                "category_detail": str(r["Categorie"]).strip(),
                "woning_type": str(r["Woning Type"]).strip(),
            },
            "amounts": {
                "enkel": _parse_eur(r["Subsidiebedrag bij een enkele maatregel"]),
                "meerdere": _parse_eur(
                    r["Subsidiebedrag bij meerdere maateregelen"]
                ),
            },
        }
        rows.append(item)

    _write_json("isde_isolatiematerialen.json", rows)


def parse_glas() -> None:
    xls_path = ROOT / "Meldcodelijst Hoogrendementsglas - November 2025.xlsx"
    df = pd.read_excel(xls_path, sheet_name="Meldcodes")

    rows: List[Dict[str, Any]] = []
    for _, r in df.iterrows():
        item = {
            "scheme": "ISDE",
            "category": "hoogrendementsglas",
            "meldcode": str(r["MELDCODE"]).strip(),
            "manufacturer": str(r["Fabrikant / Merknaam"]).strip(),
            "model": str(r["Model"]).strip(),
            "source": {"file": xls_path.name, "sheet": "Meldcodes"},
            "attributes": {
                "max_u": _parse_number(r["MAX_WAARDE_U"]),
                "category_detail": str(r["Categorie"]).strip(),
                "woning_type": str(r["Woning Type"]).strip(),
            },
            "amounts": {
                "enkel": _parse_eur(r["Subsidiebedrag bij een enkele maatregel"]),
                "meerdere": _parse_eur(
                    r["Subsidiebedrag bij meerdere maateregelen"]
                ),
                "monument": _parse_eur(r["Subsidiebedrag Monumentale woning"]),
            },
        }
        rows.append(item)

    _write_json("isde_hoogrendementsglas.json", rows)


def main() -> None:
    parse_warmtepompen()
    parse_zonneboilers()
    parse_isolatie()
    parse_glas()


if __name__ == "__main__":
    main()
