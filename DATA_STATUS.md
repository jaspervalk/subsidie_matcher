# Subsidy Data Status

**Last Updated:** December 2, 2025

## 📊 Data Collection Overview

| Subsidy Scheme | Status | Entries | Quality | Source | Last Updated |
|----------------|--------|---------|---------|--------|--------------|
| **ISDE** | ✅ Complete | ~7,500 | ⭐⭐⭐⭐⭐ | Excel (Nov 2025) | Dec 2, 2025 |
| **EIA** | 🔄 Extracting | ~129 expected | Pending | PDF (Jan 2025) | In progress |
| **MIA/Vamil** | ⏳ Pending | ~200 expected | Pending | PDF (Dec 2024) | Not started |

---

## ✅ **ISDE - COMPLETE**

### Files:
- ✅ [data/subsidies/isde_warmtepompen.json](data/subsidies/isde_warmtepompen.json) - **2,965 heat pumps**
- ✅ [data/subsidies/isde_isolatiematerialen.json](data/subsidies/isde_isolatiematerialen.json) - **~2,300 insulation materials**
- ✅ [data/subsidies/isde_hoogrendementsglas.json](data/subsidies/isde_hoogrendementsglas.json) - **~1,800 glass products**
- ✅ [data/subsidies/isde_zonneboilers.json](data/subsidies/isde_zonneboilers.json) - **~450 solar boilers**

### Source Data:
- Official RVO Excel files from November 2025
- [Meldcodelijsten](https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten)

### Data Structure:
```json
{
  "scheme": "ISDE",
  "category": "warmtepomp",
  "meldcode": "KA01205",
  "manufacturer": "Alpha Innotec",
  "model": "SWC 172K3",
  "amount_eur": 5775.0,
  "attributes": {
    "power_kw": 19.0,
    "refrigerant": "R410A",
    "gwp": 2088.0,
    "type": "Grond-Water"
  }
}
```

### Coverage:
- ✅ Heat pumps (Lucht-Water, Grond-Water, Water-Water, Warmtepompboilers)
- ✅ Insulation materials (all types)
- ✅ High-performance glass (HR++ and Triple)
- ✅ Solar boilers

### Update Frequency:
- **Monthly** - Check RVO website for updates
- Next update: January 2025

---

## 🔄 **EIA - IN PROGRESS**

### Target File:
- ⏳ [data/subsidies/eia_2025.json](data/subsidies/eia_2025.json) - **Extracting now**

### Source Data:
- Official RVO PDF: [Brochure-EIA-Energielijst2025.pdf](https://english.rvo.nl/sites/default/files/2025-01/Brochure-EIA-Energielijst2025.pdf)
- Downloaded: ✅ `ruwe_data/Brochure-EIA-Energielijst2025.pdf`
- File size: 1.26 MB (84 pages)

### Expected Coverage:
- ~129 EIA codes across categories A-G
- Major categories:
  - **A**: Energieprestatieverbetering bedrijfsgebouwen
  - Verwarmen (warmtepompen, ketels)
  - Koelen/vriezen (koelinstallaties)
  - Verlichting (LED, efficiënte verlichting)
  - CNC machines
  - Motors and drives
  - And more...

### Budget:
- **€431 million** for 2025
- 40% investment deduction
- Minimum investment: €2,500 per asset

### Extraction Method:
- Text extraction from PDF using pdfplumber
- Structured extraction with Claude API in 10-page chunks
- **ETA:** 3-5 minutes (currently running)

### Update Frequency:
- **Annually** (January)
- Next update: January 2026

---

## ⏳ **MIA/Vamil - PENDING**

### Target File:
- ⏳ [data/subsidies/mia_vamil_2025.json](data/subsidies/mia_vamil_2025.json) - **Not started**

### Source Data:
- Official RVO PDF: [RVO-Brochure-Milieulijst2025.pdf](https://www.rvo.nl/sites/default/files/2024-12/RVO-Brochure-Milieulijst%202025.pdf)
- Downloaded: ✅ `ruwe_data/BrochureMilieulijst2025v3.pdf`
- File size: 3.3 MB

### Expected Coverage:
- ~200 MIA/Vamil codes
- 5 main chapters:
  1. Grondstoffen- en watergebruik
  2. Voedselvoorziening en landbouwproductie
  3. Mobiliteit (electric vehicles, etc.)
  4. Klimaat en lucht
  5. Gebouwde omgeving en klimaatadaptatie

### MIA Percentages:
- 13%, 27%, 36%, or 45% investment deduction
- Vamil: 75% accelerated depreciation
- Max investment: €25 million per asset (new limit 2025)

### Budgets:
- **MIA:** €189 million
- **Vamil:** €20 million

### Extraction Method:
- Same as EIA (text-based extraction with Claude)
- **ETA:** Will run after EIA completes

### Update Frequency:
- **Annually** (December)
- Next update: December 2025

---

## 📋 **Next Steps**

### Immediate:
1. ⏳ Wait for EIA extraction to complete (~3-5 minutes)
2. ✅ Verify EIA data quality
3. 🔄 Run MIA/Vamil extraction (~5-10 minutes)
4. ✅ Verify MIA data quality

### Then:
1. 📊 Design unified database schema for all subsidies
2. 🔧 Implement core features:
   - PDF quote parser with Claude
   - Subsidy matcher engine
   - Basic arbitrage engine
3. 🧪 Test with sample quotes

---

## 🔄 **Data Update Process**

### ISDE (Monthly):
```bash
# Download latest meldcodelijsten from RVO
# Run parse_isde.py script
python scripts/parse_isde.py
```

### EIA (Annually - January):
```bash
# Download latest PDF from RVO
# Run extraction script
export ANTHROPIC_API_KEY="your_key"
python scripts/extract_eia_text_based.py
```

### MIA/Vamil (Annually - December):
```bash
# Download latest PDF from RVO
# Run extraction script
export ANTHROPIC_API_KEY="your_key"
python scripts/extract_mia_with_claude.py  # Or text-based variant
```

---

## 📚 **Data Sources**

All data comes from official RVO (Rijksdienst voor Ondernemend Nederland) sources:

- **ISDE**: https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten
- **EIA**: https://www.rvo.nl/subsidies-financiering/eia/energielijst
- **MIA/Vamil**: https://www.rvo.nl/subsidies-financiering/mia-vamil/milieulijst

---

## ⚠️ **Important Notes**

1. **API Costs**: Each PDF extraction costs ~€0.10-0.30 (one-time)
2. **Rate Limits**: Claude API has rate limits - if extraction fails, wait and retry
3. **Data Accuracy**: Always spot-check extracted data against official RVO sources
4. **Legal**: This is for informational purposes - always verify with RVO before applying
5. **Caching**: PDF extraction uses prompt caching when possible to reduce costs

---

## 🎯 **Data Completeness for MVP**

For the MVP, we need **minimum**:
- ✅ **ISDE Warmtepompen** (most common use case)
- 🔄 **EIA codes for warmtepompen** (complementary)
- ⏳ **Top 20-30 EIA codes** (most requested equipment)

**Nice to have** for MVP:
- EIA full database
- MIA/Vamil database
- ISDE all categories

**Can add later:**
- Regional subsidies (provincie, gemeente)
- Historical subsidy data
- Success rate tracking
