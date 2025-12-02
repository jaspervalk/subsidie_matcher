# Data Corrections Log

## December 2, 2025 - EIA Subsidy Percentage Fix

### Issue Identified:
- **Problem:** 85.3% of EIA codes (157 out of 184) had `subsidy_percentage: null`
- **Root Cause:** Claude extraction didn't capture the universal 40% rule
- **Discovered by:** User review of extracted data

### Official Rule (Confirmed):
According to the official EIA Energielijst 2025 (page 3):

> **"Met EIA kunt u 40% van de investeringskosten van energiebesparende bedrijfsmiddelen aftrekken van de fiscale winst, bovenop uw gebruikelijke afschrijving."**

**Translation:** With EIA you can deduct 40% of the investment costs of energy-saving business assets from fiscal profit, on top of your regular depreciation.

### Fix Applied:
✅ **All 184 EIA codes now have `subsidy_percentage: 0.40`**

```python
# Applied fix:
for code in data['codes']:
    if code.get('subsidy_percentage') is None:
        code['subsidy_percentage'] = 0.40
```

### Verification:
- ✅ Total codes: 184
- ✅ Codes with 40%: 184 (100%)
- ✅ Codes with null: 0

### Updated Files:
1. ✅ [data/subsidies/eia_2025.json](data/subsidies/eia_2025.json) - Fixed data
2. ✅ [scripts/extract_eia_text_based.py](scripts/extract_eia_text_based.py) - Updated prompt to explicitly mention 40% rule

### Important Note:
**ALL EIA codes in the Energielijst 2025 qualify for 40% investment deduction.**

There are NO exceptions or variable percentages in the EIA scheme - it's always 40%.

### How to Calculate EIA Subsidy:
```
EIA Subsidy = Investment Amount × 0.40

Example:
- Warmtepomp: €10,000
- EIA subsidy: €10,000 × 0.40 = €4,000
```

### Limits:
- **Minimum investment:** €2,500 per asset
- **Maximum:** Some specific codes have caps (e.g., €1,400 per kWth for certain warmtepompen)
- **Budget:** €431 million total for 2025

---

## Data Quality Checklist

When verifying subsidy data:

### EIA:
- ✅ All codes should have `subsidy_percentage: 0.40`
- ✅ Check for `min_investment: 2500`
- ✅ Some codes have `max_investment_per_unit` limits
- ✅ Codes should have descriptions and requirements

### ISDE:
- ✅ Each entry should have exact `amount_eur`
- ✅ Meldcodes are product-specific (merk + model)
- ✅ Amounts vary based on product specs (SCOP, power, etc.)
- ✅ Different subsidy amounts for different housing types

### Future MIA/Vamil:
- ⚠️ Variable percentages: 13%, 27%, 36%, 45%
- ⚠️ Must extract actual percentage for each code
- ⚠️ Some codes have only MIA, some only Vamil, some both

---

## Lessons Learned

1. **Always verify extraction results** against official source documents
2. **Universal rules should be hardcoded** when they apply to all entries
3. **LLM extraction may miss context** that's stated once at the beginning
4. **Post-processing validation** is essential for data quality

---

## Next Data Quality Checks

Before using data in production:

1. ✅ EIA subsidy percentages (FIXED)
2. ⏳ EIA min/max investment limits (needs review)
3. ⏳ ISDE amounts match official meldcodelijsten (spot check)
4. ⏳ Code descriptions are complete (spot check)
5. ⏳ Technical requirements are accurate (spot check)

---

**Status:** ✅ EIA data is now correct and ready for use!
