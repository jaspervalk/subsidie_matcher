# Data Extraction Scripts

This folder contains scripts to extract subsidy data from official RVO PDF and Excel files.

## 📋 Overview

We extract data from three main subsidy schemes:

1. **EIA (Energie-investeringsaftrek)** - Energy Investment Deduction
2. **ISDE (Investeringssubsidie Duurzame Energie)** - Investment Subsidy for Sustainable Energy
3. **MIA/Vamil** - Environmental Investment Deduction

## 🚀 Quick Start

### 1. Setup API Key

First, add your Anthropic API key to `.env` file in the project root:

```bash
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxx
```

Get your API key from: https://console.anthropic.com/

### 2. Test API Key

```bash
python scripts/test_api_key.py
```

### 3. Run Extractions

```bash
# Extract EIA data (takes ~30-60 seconds)
python scripts/extract_eia_with_claude.py

# Extract MIA/Vamil data (takes ~60-90 seconds)
python scripts/extract_mia_with_claude.py

# ISDE data is already extracted (from Excel files)
# No need to run extraction for ISDE
```

## 📁 Input Files (in `ruwe_data/`)

| File | Source | Status |
|------|--------|--------|
| `Brochure-EIA-Energielijst2025.pdf` | [RVO EIA](https://english.rvo.nl/sites/default/files/2025-01/Brochure-EIA-Energielijst2025.pdf) | ✅ Downloaded |
| `BrochureMilieulijst2025v3.pdf` | [RVO MIA/Vamil](https://www.rvo.nl/sites/default/files/2024-12/RVO-Brochure-Milieulijst%202025.pdf) | ✅ Downloaded |
| `Meldcodelijst Warmtepompen - November 2025.xlsx` | [RVO ISDE](https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten/warmtepompen) | ✅ Downloaded |
| `Meldcodelijst Isolatiematerialen - November 2025.xlsx` | [RVO ISDE](https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten) | ✅ Downloaded |
| `Meldcodelijst Hoogrendementsglas - November 2025.xlsx` | [RVO ISDE](https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten) | ✅ Downloaded |
| `Meldcodelijst Zonneboilers - November 2025.xlsx` | [RVO ISDE](https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten) | ✅ Downloaded |

## 📊 Output Files (in `data/subsidies/`)

| File | Description | Status |
|------|-------------|--------|
| `eia_2025.json` | EIA codes with requirements | ⏳ Run script |
| `mia_vamil_2025.json` | MIA/Vamil codes | ⏳ Run script |
| `isde_warmtepompen.json` | ISDE heat pumps (2,965 entries) | ✅ Extracted |
| `isde_isolatiematerialen.json` | ISDE insulation materials | ✅ Extracted |
| `isde_hoogrendementsglas.json` | ISDE high-performance glass | ✅ Extracted |
| `isde_zonneboilers.json` | ISDE solar boilers | ✅ Extracted |

## 🔧 Extraction Methods

### EIA & MIA (Claude API)

These scripts use Claude's native PDF reading capability to extract structured data:

- **Model**: `claude-sonnet-4-20250514`
- **Method**: Direct PDF upload to API
- **Output**: Structured JSON with Pydantic validation
- **Accuracy**: High (Claude understands complex Dutch technical documents)
- **Cost**: ~€0.15-0.30 per PDF (one-time extraction)

### ISDE (Excel Parsing)

Already extracted using `parse_isde.py`:

- **Method**: Direct Excel reading with `openpyxl`
- **Output**: Clean JSON files
- **Status**: ✅ Complete (2,965+ entries)

## 📈 Data Quality

| Scheme | Status | Entries | Quality |
|--------|--------|---------|---------|
| **ISDE** | ✅ Complete | ~7,500 | ⭐⭐⭐⭐⭐ |
| **EIA** | ⏳ Pending | ~129 expected | N/A |
| **MIA** | ⏳ Pending | ~200 expected | N/A |

## 🔄 Update Frequency

- **EIA**: Annually (January) - Manual update required
- **ISDE**: Monthly - Check RVO website for new meldcodelijsten
- **MIA/Vamil**: Annually (December) - Manual update required

## 📝 Script Details

### `extract_eia_with_claude.py`

Extracts all EIA codes from the Energielijst 2025 PDF.

**Output structure:**
```json
{
  "version": "2025",
  "budget": 431000000,
  "codes": [
    {
      "code": "211102",
      "title": "Warmtepompboiler",
      "description": "...",
      "category": "A",
      "requirements": [
        {"name": "COP", "value": "≥ 3.0", "description": "..."}
      ],
      "subsidy_percentage": 0.40,
      "keywords": ["warmtepomp", "boiler"],
      "page": 20
    }
  ]
}
```

### `extract_mia_with_claude.py`

Extracts all MIA/Vamil codes from the Milieulijst 2025 PDF.

**Output structure:**
```json
{
  "version": "2025",
  "mia_budget": 189000000,
  "vamil_budget": 20000000,
  "codes": [
    {
      "code": "A 1100",
      "title": "Circulaire woning",
      "description": "...",
      "mia_percentage": 36,
      "vamil_percentage": 75,
      "chapter": "1. Grondstoffen- en watergebruik",
      "page": 15
    }
  ]
}
```

### `parse_isde.py`

Already run - extracts ISDE data from Excel files.

**Output**: Separate JSON files per category (warmtepompen, isolatie, glas, zonneboilers)

## 🐛 Troubleshooting

### API Key Issues

```bash
# Test your API key
python scripts/test_api_key.py
```

If test fails:
1. Check `.env` file has correct key
2. Verify key starts with `sk-ant-`
3. Check you have API credits at console.anthropic.com

### Extraction Fails

If extraction fails, check:
1. PDF files exist in `ruwe_data/`
2. Output directory `data/subsidies/` exists
3. Check `_debug.txt` files for raw Claude output

### JSON Parsing Errors

If you get JSON errors:
1. Check `*_debug.txt` files to see raw output
2. Claude may have added explanation text around JSON
3. Run script again (sometimes temporary API issues)

## 💡 Tips

1. **Run extractions once** - Results are saved and don't need re-running unless data changes
2. **Check debug files** - If extraction fails, check the `_debug.txt` file
3. **Verify output** - Always spot-check a few entries to ensure accuracy
4. **Update annually** - EIA and MIA lists update yearly, ISDE updates monthly

## 📞 Support

If you encounter issues:
1. Check the debug output files
2. Verify your PDF files match the official RVO versions
3. Test your API key with `test_api_key.py`
4. Check the script output for specific error messages
