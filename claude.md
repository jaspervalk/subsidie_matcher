# SubsidieMatch - Claude Context File

**DO NOT USE EMOJIS IN COMMUNICATION WITH THE USER**

## Project Overview

SubsidieMatch is an AI-powered subsidie-matching platform for Dutch SMEs (MKB). It scans PDF quotes and automatically identifies applicable subsidies (EIA, ISDE, MIA/Vamil), calculates amounts, and suggests arbitrage opportunities to maximize subsidy returns.

**Status**: MVP Development - Database & Schema Complete (Dec 2, 2025)
**Tech Stack**: FastAPI + Claude Sonnet 4.5 + Instructor + Pydantic v2
**Database**: JSON files (in-memory, 32ms load time, <1ms searches)
**Target**: 100 B2B customers (installers/accountants) by Year 1
**Revenue Model**: B2B SaaS (149-999 EUR/month)

---

## Core Value Proposition

**Problem**: 80% of Dutch SMEs qualify for subsidies but only 0.08% actually receive them due to complexity and lack of awareness.

**Solution**:
1. Upload PDF quote (offerte)
2. AI extracts equipment details automatically
3. Match against subsidy databases (EIA, ISDE, MIA/Vamil)
4. Calculate exact subsidy amounts
5. Suggest alternative equipment for higher subsidies (arbitrage)
6. Generate report in 30 seconds

**Key Differentiator**: Arbitrage engine that finds equipment alternatives with better subsidy outcomes.

---

## Technical Architecture

### Tech Stack
- **Backend**: FastAPI (Python 3.11+)
- **LLM**: Claude Sonnet 4.5 via Anthropic API
- **Structured Extraction**: Instructor library + Pydantic v2
- **Database**: JSON files with in-memory indexes (7,372 entries, 32ms load, <1ms search)
- **File Storage**: Local JSON files (MVP), S3 later
- **Deployment**: Railway/Render (MVP), AWS (scale)
- **PostgreSQL**: Not needed for MVP (will add for user accounts in Phase 2)

### Project Structure
```
subsidie_matcher/
├── data/
│   └── subsidies/          # Subsidy databases (JSON)
│       ├── eia_2025.json           # 184 EIA codes
│       ├── isde_warmtepompen.json  # 2,965 heat pumps
│       ├── isde_isolatiematerialen.json
│       ├── isde_hoogrendementsglas.json
│       ├── isde_zonneboilers.json
│       └── mia_vamil_2025.json     # MIA/Vamil codes
├── ruwe_data/              # Raw PDFs and Excel files
├── scripts/                # Data extraction scripts
│   ├── extract_eia_text_based.py      # EIA extraction (COMPLETE)
│   ├── extract_mia_text_based.py      # MIA extraction (COMPLETE)
│   └── test_api_key.py                # API key validation
├── services/               # Core business logic
│   ├── subsidy_database.py            # In-memory database (COMPLETE)
│   └── subsidy_matcher.py             # Matching engine (TODO)
├── models/                 # Pydantic schemas
│   └── subsidy_schemas.py             # Complete models (COMPLETE)
└── tests/
    └── test_database.py               # Database tests (ALL PASSING)
```

---

## Data Sources & Status

### Current Data (December 2, 2025)

| Scheme | Status | Entries | Source | Quality |
|--------|--------|---------|--------|---------|
| **EIA** | COMPLETE | 184 codes | PDF extraction | 5/5 stars |
| **ISDE** | COMPLETE | 7,500 entries | Excel parsing | 5/5 stars |
| **MIA/Vamil** | IN PROGRESS | ~200 expected | PDF extraction | Pending |

### EIA (Energie-investeringsaftrek)
- **All codes have 40% investment deduction** (fixed on Dec 2)
- Minimum investment: 2,500 EUR per asset
- Budget: 431 million EUR (2025)
- Covers: Warmtepompen, CNC machines, LED, cooling, ventilation, etc.
- File: `data/subsidies/eia_2025.json`

### ISDE (Investeringssubsidie Duurzame Energie)
- Product-specific subsidies with exact amounts
- Categories: Warmtepompen, Isolatie, Hoogrendementsglas, Zonneboilers
- Budget: 550 million EUR (2025)
- Updated monthly by RVO
- Files: `data/subsidies/isde_*.json`

### MIA/Vamil (Milieu-investeringsaftrek)
- Variable percentages: 13%, 27%, 36%, or 45%
- Vamil: 75% accelerated depreciation
- Budget: MIA 189M EUR, Vamil 20M EUR
- File: `data/subsidies/mia_vamil_2025.json` (extracting)

---

## Core Features to Implement

### 1. PDF Quote Parser
- Read PDF quotes using Claude's native PDF support
- Extract equipment details: brand, model, specs, price
- Output: Structured Quote object (Pydantic)
- See: `SubsidieMatch.md` lines 483-515 for Quote model

### 2. Subsidy Matcher Engine
- Match equipment against EIA codes (keyword + spec matching)
- Match warmtepompen against ISDE meldcodes (exact model matching)
- Match other equipment against ISDE categories
- Calculate subsidy amounts:
  - EIA: investment * 0.40
  - ISDE: lookup exact amount from database
  - MIA: investment * mia_percentage
- Output: SubsidyAnalysis object with all matches

### 3. Arbitrage Engine
- Compare alternative equipment models
- Find equipment with higher subsidy-to-cost ratio
- Example: "Upgrade to model X (+800 EUR) for +1,200 EUR subsidy = +400 EUR net benefit"
- Rank alternatives by net benefit

---

## Key Business Rules

### EIA Rules
- All codes: 40% investment deduction
- Minimum: 2,500 EUR per asset
- Maximum: Some codes have per-unit caps (e.g., 1,400 EUR per kWth for certain warmtepompen)
- Must apply within 3 months of investment

### ISDE Rules
- Product-specific (must match exact meldcode)
- Only for existing buildings (built before 2019)
- Requires certified installer
- Must apply before installation

### Combination Rules
- EIA + ISDE: Can combine for same equipment
- EIA + MIA: Must choose one OR split costs
- Example: Warmtepomp can get both EIA (40% of price) AND ISDE (fixed amount)

---

## Important Data Quality Notes

### Known Issues & Fixes
1. **EIA subsidy_percentage**: Originally extracted as null, fixed to 0.40 for all codes (Dec 2, 2025)
2. **Extraction method**: Large PDFs require text-based extraction (pdfplumber) then Claude structuring to avoid 200k token limit

### Validation Checklist
- All EIA codes must have `subsidy_percentage: 0.40`
- ISDE entries must have exact `amount_eur`
- MIA codes must have `mia_percentage` (13, 27, 36, or 45)
- Check code descriptions are complete
- Verify technical requirements are accurate

---

## Development Priorities

### MVP Must-Have (Week 1-2)
1. PDF upload & parsing
2. Equipment extraction (brand, model, specs)
3. EIA matching & calculation
4. ISDE warmtepomp matching (primary use case)
5. Basic arbitrage (1-2 alternatives)
6. PDF report generation
7. Simple web interface

### Phase 2 (Week 3-4)
- User accounts/authentication
- MIA/Vamil support
- Extended arbitrage (5-10 alternatives)
- Branded reports

### Phase 3 (Week 5-6)
- API for CRM integration
- Bulk upload
- Dashboard analytics

---

## Target Customers

### Primary: Installateurs (Installers)
- 50-200 projects/year
- Pain: Customers ask about subsidies, they don't know
- Value: 30-second answer, win more sales
- Pricing: 149-299 EUR/month

### Secondary: Accountants
- 30-50 clients asking investment advice
- Pain: Don't know subsidy landscape
- Value: Advisory upsell opportunity
- Pricing: 299-999 EUR/month

### Tertiary: Direct MKB
- Large investments (100k-500k EUR)
- Pain: Complex to figure out subsidies
- Value: Maximize subsidy returns
- Pricing: 10% success fee OR one-time scan fee

---

## Communication Guidelines

**IMPORTANT**:
- DO NOT use emojis in responses
- Be concise and professional
- Focus on facts and technical accuracy
- Provide direct, objective guidance
- Disagree when necessary rather than false agreement

---

## Common Commands

### Extract Subsidy Data
```bash
# EIA extraction
python scripts/extract_eia_text_based.py

# MIA extraction
python scripts/extract_mia_text_based.py

# ISDE already extracted (Excel files)
```

### Test API Key
```bash
python scripts/test_api_key.py
```

### Verify Data
```bash
python -c "import json; data=json.load(open('data/subsidies/eia_2025.json')); print(f'EIA codes: {len(data[\"codes\"])}')"
```

---

## File References

### Key Documentation
- **Master Plan**: `SubsidieMatch.md` (full business plan, 1970 lines)
- **Data Status**: `DATA_STATUS.md` (current data completeness)
- **Extraction Summary**: `EXTRACTION_SUMMARY.md` (what we have)
- **Data Corrections**: `DATA_CORRECTIONS.md` (fixes applied)
- **Scripts README**: `scripts/README.md` (how to run extractions)

### Code Structure
- **Models**: `models/schemas.py` (Pydantic models)
- **Services**: `services/subsidy_matcher.py` (matching logic)
- **Tests**: `tests/test_main.py`

---

## Environment Setup

### Required Environment Variables
```
ANTHROPIC_API_KEY=sk-ant-...
```

### Virtual Environment
```bash
source venv/bin/activate
```

### Dependencies
See `requirements.txt`:
- anthropic>=0.40.0
- instructor>=1.8.0
- fastapi>=0.115.0
- pydantic>=2.10.0
- pandas>=2.2.0
- openpyxl>=3.1.2
- pdfplumber>=0.11.0

---

## Budget & Costs

### Data Extraction (One-time)
- EIA: ~0.10 EUR (7 chunks)
- MIA: ~0.15 EUR (~10 chunks)
- ISDE: 0 EUR (Excel parsing)
- **Total**: ~0.25 EUR per year

### MVP Operation Costs
- Claude API: ~0.03-0.10 EUR per quote scan
- With prompt caching: ~0.01-0.03 EUR per scan
- Target: <0.50 EUR per scan including infrastructure

---

## Quick Context for Claude

When you (Claude) start a new session:

1. **Project**: AI subsidy matcher for Dutch SMEs
2. **Current Phase**: MVP development - Database & Schema Complete
3. **Data Status**: ALL COMPLETE (EIA + ISDE + MIA/Vamil)
4. **Infrastructure Status**: COMPLETE (Database, Schemas, Tests all passing)
5. **Next Step**: Implement subsidy matcher engine
6. **Style**: No emojis, concise, technical, objective

**The user's goal**: Build a working MVP that can scan quotes and find subsidies in 30 seconds, targeting Dutch installers and accountants.

---

## Current Development Status (December 2, 2025)

### COMPLETED

**Phase 1: Data Extraction (COMPLETE)**
- EIA 2025: 184 codes extracted and verified
- ISDE 2025: 6,895 meldcodes across 4 categories
- MIA/Vamil 2025: 293 codes extracted
- All data quality verified and corrected

**Phase 2: Database & Schema (COMPLETE)**
- Pydantic models for all entities ([models/subsidy_schemas.py](models/subsidy_schemas.py))
- In-memory database with search indexes ([services/subsidy_database.py](services/subsidy_database.py))
- Performance: 32ms load time, <1ms search time
- All tests passing ([tests/test_database.py](tests/test_database.py))

### IN PROGRESS

**Phase 3: Core Features (NEXT)**
1. Subsidy Matcher Engine - Match equipment to subsidies
2. PDF Quote Parser - Extract equipment from quotes using Claude
3. Arbitrage Engine - Find better subsidy opportunities

### File Status

- [models/subsidy_schemas.py](models/subsidy_schemas.py) - COMPLETE (479 lines)
- [services/subsidy_database.py](services/subsidy_database.py) - COMPLETE (365 lines)
- [tests/test_database.py](tests/test_database.py) - COMPLETE (all tests passing)
- services/subsidy_matcher.py - TODO (next task)

---

## Version Info

**Last Updated**: December 2, 2025 - 20:00
**Current Status**: Database & schema implementation complete, ready for matcher engine
**Next Milestone**: Implement subsidy matcher engine with test cases

---

## Quick Reference: Subsidy Amounts

### Example Calculations

**Warmtepomp (12,000 EUR)**
- EIA: 12,000 * 0.40 = 4,800 EUR
- ISDE: ~3,800 EUR (fixed, depends on model)
- Total: ~8,600 EUR

**CNC Machine (85,000 EUR)**
- EIA: 85,000 * 0.40 = 34,000 EUR
- Total: 34,000 EUR

**Isolatie (200m2 at 20 EUR/m2 = 4,000 EUR)**
- ISDE: 200 * 20 EUR/m2 = 4,000 EUR
- Total: 4,000 EUR

---

**END OF CLAUDE CONTEXT FILE**
