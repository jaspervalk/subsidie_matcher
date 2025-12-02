# SubsidieMatch - Master Document

**AI-powered subsidie-matching & optimalisatie tool voor Nederlandse MKB**

**Laatste update:** 1 december 2024  
**Status:** Pre-launch / MVP Development  
**Website:** subsidiematch.nl (geregistreerd)

---

## 📋 Inhoudsopgave

1. [Executive Summary](#executive-summary)
2. [Het Probleem](#het-probleem)
3. [De Oplossing](#de-oplossing)
4. [Marktvalidatie](#marktvalidatie)
5. [Concurrentie Analyse](#concurrentie-analyse)
6. [Differentiatie & USPs](#differentiatie--usps)
7. [Technische Architectuur](#technische-architectuur)
8. [Data Bronnen](#data-bronnen)
9. [Product Specificaties](#product-specificaties)
10. [Business Model](#business-model)
11. [Klanten & Distributie](#klanten--distributie)
12. [Go-to-Market Strategie](#go-to-market-strategie)
13. [Development Roadmap](#development-roadmap)
14. [Financiële Projecties](#financiële-projecties)
15. [Team & Resources](#team--resources)

---

## Executive Summary

**SubsidieMatch** is een AI-powered platform dat Nederlandse MKB-bedrijven helpt om maximaal te profiteren van overheidssubsidies (EIA, ISDE, MIA/Vamil) door:

1. **Automatisch offertes te scannen** en alle toepasselijke subsidies te identificeren
2. **Arbitrage-kansen te vinden** door alternatieve equipment keuzes voor te stellen die meer subsidie opleveren
3. **Het proces te versnellen** van weken naar 30 seconden

### Key Metrics (Target Year 1)
- **TAM:** 420.000 MKB bedrijven in Nederland
- **Target:** 100 B2B klanten (installateurs/accountants)
- **Revenue:** €240k ARR (€200/maand × 100 klanten)
- **Value Created:** €5M+ aan gevonden subsidies voor klanten

### The Pitch
> "Stel je voor: Een metaalbedrijf koopt een €80k CNC machine. Zonder ons betalen ze €80k. Met SubsidieMatch: EIA €8k + optimalisatie €2k = €10k besparing. Kost hun X per scan of Y per maand. Wij verdienen via SaaS model aan installateurs die 50+ projecten/jaar doen."

---

## Het Probleem

### Subsidies blijven massaal onbenut

**Onderzoeksgegevens:**
- **80%** van Nederlandse bedrijven komt in aanmerking voor subsidies
- **Slechts 1 op 1.270** MKB-bedrijven ontvangt daadwerkelijk innovatiesubsidies
- **€33M** aan klimaatsubsidies (DUMAVA) bleef onbenut in 2024
- **80%** van €1M cybersecurity subsidie (Mijn Cyberweerbare Zaak) niet opgehaald

**Budgetten 2025:**
- EIA: €431 miljoen
- ISDE: ~€550 miljoen
- MIA/Vamil: €189M + €20M

### Root Causes

1. **Complexiteit**
   - Verschillende regelingen per overheidsniveau
   - Complexe technische eisen (SCOP, energielabels, vermogen specs)
   - Onduidelijke eligibility criteria

2. **Gebrek aan awareness**
   - MKB ondernemers weten niet wat mogelijk is
   - Installateurs hebben geen tijd om uit te zoeken
   - Accountants zijn niet gespecialiseerd in subsidies

3. **Fragmentatie**
   - RVO, provincies, gemeentes hebben elk eigen regelingen
   - Geen centraal overzicht
   - Geen tool die automatisch checkt

4. **Timing issues**
   - EIA moet binnen 3 maanden na opdracht aangevraagd
   - ISDE moet vooraf aangevraagd
   - Te laat = geen subsidie

### De Business Pijn

**Voor installateurs:**
- Klanten vragen: "Krijg ik subsidie?"
- Antwoord nu: "Weet ik niet, zoek het zelf uit"
- Resultaat: Lost sales aan concurrenten die wél helpen

**Voor MKB-bedrijven:**
- Investering van €50k-200k
- €10k-40k subsidie mogelijk
- Te complex om zelf uit te zoeken
- Huren consultant = €2k-5k (vaak meer dan subsidie waard voor kleinere projecten)

**Voor accountants:**
- Klanten vragen advies bij investeringen
- Accountant weet subsidie-landscape niet
- Gemiste kans om waarde toe te voegen

---

## De Oplossing

### SubsidieMatch Platform

Een AI-powered platform dat in **3 stappen** werkt:

#### STAP 1: Upload Offerte
- Klant/installateur upload investeringsofferte (PDF)
- AI extraheert automatisch:
  - Equipment details (merk, model, type)
  - Technische specs (vermogen, SCOP, energielabel)
  - Prijzen (excl. BTW)
  - Bedrijfsgegevens

#### STAP 2: Match & Analyse
- Systeem checkt tegen 3 subsidie-databases:
  - **EIA Energielijst 2025** (129 categorieën)
  - **ISDE Meldcodelijsten** (warmtepompen, isolatie, glas)
  - **MIA/Vamil Milieulijst** (milieuvriendelijke investeringen)
- AI verifieert complexe eligibility eisen
- Berekent exacte subsidiebedragen

#### STAP 3: Optimalisatie & Advies
- **Arbitrage Engine** vergelijkt alternatieven:
  - "Model A: €8k subsidie"
  - "Model B (+€1.5k duurder): €11k subsidie = €1.5k netto voordeel"
- Genereert rapport met:
  - Alle toepasselijke subsidies
  - Exacte bedragen per regeling
  - Optimalisatie-aanbevelingen
  - Links naar RVO aanvraagpagina's
  - Pre-filled formulieren (waar mogelijk)

### Output Voorbeeld

```
📄 OFFERTE ANALYSE
Bedrijf: Metaal BV
Investering: CNC Machine Haas VF-2 + Warmtepomp Daikin

✅ GEVONDEN SUBSIDIES:
├─ EIA Code 220101 (Warmtepomp): €4.200 (40% van €10.500)
├─ EIA Code 310405 (CNC Machine): €8.000 (40% van €20.000)
└─ ISDE Meldcode KA18409: €3.800

💡 OPTIMALISATIE:
Upgrade Daikin Altherma 3H → Altherma 3H HT (+€800)
├─ Reden: Hogere SCOP → Hogere ISDE categorie
├─ Extra subsidie: +€1.200 ISDE
└─ Netto voordeel: €400

📊 TOTAAL:
├─ Zonder optimalisatie: €16.000
├─ Met optimalisatie: €17.200
└─ Extra besparing: €1.200

⏱️ DEADLINE: Aanvraag binnen 87 dagen (EIA deadline)
```

---

## Marktvalidatie

### Primair Onderzoek

**Confirmatiedat het probleem bestaat:**

1. **CBS Data (2024):**
   - 420.000 MKB bedrijven in Nederland (2-250 werknemers)
   - 80% komt in aanmerking, maar 99.9% haalt het niet op

2. **RVO Cijfers:**
   - €33M DUMAVA onbenut (2024)
   - 80% cybersecurity subsidie niet opgehaald
   - EIA budget €431M (2025) wordt historisch niet volledig benut

3. **Interviews met installateurs (Informeel):**
   - "Klanten vragen altijd naar subsidie, maar ik heb geen tijd om uit te zoeken"
   - "Ik mis sales omdat concurrent wel subsidie regelt"
   - "Zou €500/jaar betalen voor tool die dit automatisch doet"

### Marktomvang

**Segmentatie:**

| Segment | Aantal | Gemiddelde investering/jaar | Subsidie potentieel |
|---------|--------|----------------------------|---------------------|
| Productie bedrijven | 60.000 | €100k | €30k (EIA+MIA) |
| Horeca/Retail | 120.000 | €50k | €15k (EIA+ISDE) |
| Transport | 40.000 | €80k | €24k (EIA) |
| Bouw/Installatie | 80.000 | €60k | €18k (EIA+ISDE) |

**Total Addressable Market:**
- 420.000 bedrijven × €20k gemiddelde subsidie = **€8,4 miljard** jaarlijks potentieel
- Huidig gebruik: ~€1 miljard
- **Gap: €7,4 miljard blijft liggen**

**Serviceable Addressable Market:**
- Bedrijven die actief investeren in duurzame middelen: ~100.000
- Via B2B distributie (installateurs/accountants): 5.000 intermediairs
- Elke intermediar heeft 20-200 klanten

**Serviceable Obtainable Market (Year 1):**
- 100 B2B klanten × 50 projecten/jaar = 5.000 scans
- Value created: €5M aan gevonden subsidies
- Revenue: €240k ARR

---

## Concurrentie Analyse

### Bestaande Spelers

#### 1. **SubsidyCloud**
**Type:** Generic subsidie matching platform  
**Focus:** Breed, 3000+ subsidies database  
**Aanpak:** Bedrijfsprofiel matching (sector, grootte, locatie)  
**Business Model:** B2B SaaS  

**Verschil met ons:**
- ❌ Geen offerte-specifieke analyse
- ❌ Geen equipment optimalisatie
- ❌ Generic matching zonder arbitrage
- ✅ Wel grote database (maar wij focussen op 3 belangrijkste)

---

#### 2. **subsidAI**
**Type:** WBSO automation  
**Focus:** R&D tax credits only  
**Aanpak:** Automatiseert WBSO aanvragen  

**Verschil met ons:**
- ❌ Alleen WBSO (niet EIA/ISDE/MIA)
- ❌ Andere markt (R&D vs equipment investeringen)
- ✅ Wel geproven AI approach

---

#### 3. **Subsidie Expertise** (Stan Duinmeijer)
**Type:** 1-persoons consultancy  
**Focus:** Particulieren + kleine zakelijke vastgoed  
**Aanpak:** Handmatige ISDE aanvragen voor woningen  
**Business Model:** 7.5% success fee  
**Capaciteit:** Max 100-200 klanten/jaar  

**Hun markt:**
- Particulieren: Warmtepomp in woning (€8k project, €2.5k subsidie)
- Verhuurders: ISDE voor huurwoningen
- VvE's: Verduurzaming appartementencomplex

**Verschil met ons:**
- ❌ Focus op **woningen** (wij: bedrijven/machines)
- ❌ Alleen **ISDE** (wij: EIA+ISDE+MIA)
- ❌ Handmatig proces (wij: AI, 30 sec)
- ❌ Geen optimalisatie (wij: arbitrage engine)
- ❌ Niet schaalbaar (1 persoon vs onze software)

**Overlap:** Minimaal. Ze doen wel "zakelijk ISDE" voor bedrijfspanden (warmtepomp/isolatie), maar:
- Focus blijft op **gebouw-verduurzaming**
- Wij focussen op **machines/apparatuur/productie-middelen**
- Different subsidies, different market

---

#### 4. **Simpel Subsidie**
**Type:** ISDE service voor installateurs  
**Focus:** Widget/API voor ISDE aanvragen  
**Aanpak:** Installateurs integreren widget, mensen dienen via hun platform aan  
**Business Model:** Per-aanvraag fee  

**Verschil met ons:**
- ❌ Alleen ISDE (niet EIA/MIA)
- ❌ Geen optimalisatie features
- ❌ Human-powered (niet self-service AI)
- ✅ Wel B2B distributie via installateurs (inspiratie!)

---

#### 5. **Traditionele Subsidie Adviseurs**
**Namen:** Leap, Brands Subsidieadvies, Ignite Group, De Subsidie Club  
**Type:** Consultancy firms  
**Focus:** Full-service subsidie advies (EIA, MIA, WBSO, SDE++)  
**Aanpak:** 1-on-1 advies, handmatig proces  
**Business Model:** Success fee 10-15% of fixed project fee €2k-10k  

**Verschil met ons:**
- ❌ Langzaam (weken/maanden vs 30 seconden)
- ❌ Duur (€5k-10k vs €200/maand unlimited)
- ❌ Niet schaalbaar (consultants vs software)
- ✅ Wel diepgaande expertise (inspiratie voor onze AI prompts)

---

### Competitive Matrix

| Feature | SubsidieMatch (Wij) | SubsidyCloud | Subsidie Expertise | Simpel Subsidie | Trad. Adviseurs |
|---------|---------------------|--------------|-------------------|-----------------|-----------------|
| **Offerte Scan** | ✅ AI, 30 sec | ❌ Manual input | ❌ Phone call | ❌ Manual | ❌ Manual |
| **EIA** | ✅ | ✅ | ⚠️ Als backup | ❌ | ✅ |
| **ISDE** | ✅ | ✅ | ✅ Core | ✅ Core | ✅ |
| **MIA/Vamil** | ✅ | ✅ | ❌ | ❌ | ✅ |
| **Optimalisatie** | ✅ Arbitrage | ❌ | ❌ | ❌ | ⚠️ Sometimes |
| **Speed** | 30 sec | Hours | Days | Days | Weeks |
| **Price** | €200/m | €299/m | 7.5% | Per request | 10-15% |
| **Target** | MKB equipment | All businesses | Homeowners | Homeowners | Large projects |
| **Scalability** | ∞ (software) | High | Low (1 person) | Medium | Low (humans) |

---

### Waarom We Winnen

**1. Offerte-Specific vs Profile-Based**
- Concurrenten: "Vertel ons over je bedrijf" → generic matches
- Wij: "Upload je offerte" → specifieke apparatuur met exacte subsidies

**2. Arbitrage/Optimalisatie**
- Concurrenten: "Je kan €8k krijgen"
- Wij: "Je kan €8k krijgen, maar kies model Y voor €2k extra subsidie"

**3. Speed**
- Concurrenten: Dagen/weken
- Wij: 30 seconden

**4. Multi-Scheme**
- Concurrenten: Gefocust op 1-2 regelingen
- Wij: EIA + ISDE + MIA combinaties

**5. B2B Distribution**
- Concurrenten: 1 klant tegelijk (B2C)
- Wij: Installateur = 50 klanten (B2B scale)

**6. Equipment Focus**
- Concurrenten: Breed of particulier
- Wij: MKB equipment investeringen (grotere bedragen)

---

## Differentiatie & USPs

### Unique Selling Propositions

#### 1. **Offerte-Specific Intelligence**
**What:** AI leest werkelijke PDF offertes met specifieke merken, modellen, specs  
**Why it matters:** Exacte subsidie bedragen ipv "mogelijk €5k-10k"  
**Competition:** Niemand doet dit - allen werken met generieke profielen

#### 2. **Arbitrage Engine**
**What:** Vergelijkt alternatieven en stelt wijzigingen voor die meer subsidie opleveren  
**Why it matters:** €2k-5k extra per project door slimme keuzes  
**Competition:** Niemand heeft dit - allen reactief ("dit is mogelijk")

**Voorbeeld:**
```
ZONDER ARBITRAGE:
Daikin Altherma 3H 12kW → ISDE €3.200

MET ARBITRAGE:
Daikin Altherma 3H HT 12kW (+€600) → ISDE €4.400
Netto voordeel: €1.600
```

#### 3. **Multi-Scheme Optimization**
**What:** Checkt EIA + ISDE + MIA tegelijk, vindt beste combinaties  
**Why it matters:** Meeste adviseurs focussen op 1 regeling  
**Competition:** SubsidyCloud heeft database, maar geen optimalisatie

**Voorbeeld:**
```
Investering: €50k CNC machine + €15k warmtepomp

EIA Optie 1: Alles als EIA (40%) = €26k subsidie
EIA Optie 2: CNC als EIA (€20k) + Warmtepomp als ISDE (€4k) = €24k

ONZE TOOL KIEST: Optie 1 (€2k meer)
```

#### 4. **B2B Distribution Model**
**What:** SaaS voor installateurs/accountants die vele klanten hebben  
**Why it matters:** 1 klant = 50-200 projecten/jaar  
**Competition:** Meesten zijn B2C (1 project tegelijk)

#### 5. **30-Second Turnaround**
**What:** Upload → Scan → Result in 30 seconden  
**Why it matters:** Installateur kan ter plekke bij klant resultaat tonen  
**Competition:** Consultants hebben dagen/weken nodig

#### 6. **Equipment/Machine Focus**
**What:** Gespecialiseerd in productie-middelen, niet woningen  
**Why it matters:** Hogere bedragen (€50k-200k vs €10k), andere subsidies  
**Competition:** Subsidie Expertise doet woningen, wij doen bedrijfsmiddelen

---

### Defensible Moat

**Waarom kunnen klanten het niet zelf met ChatGPT?**

#### 1. **Data Moat**
- We bouwen **proprietary subsidie database**:
  - EIA Energielijst 2025 (129 codes, gestructureerd)
  - ISDE Meldcodelijsten (1000+ warmtepomp/isolatie codes)
  - MIA Milieulijst categorieën
  - Equipment specifications database (welke warmtepomp = welke meldcode)
- Updates: EIA 2026 = wij updaten automatisch, zij moeten handmatig
- ChatGPT kent deze specifieke Nederlandse regelingen niet

#### 2. **Compliance & Accuracy Moat**
- Wij **garanderen** correctheid (liability insurance)
- ChatGPT: "Ik denk..." vs Onze tool: "Gegarandeerd €8.200"
- Legal compliance checking (is aanvraag nog op tijd? Zijn alle docs compleet?)

#### 3. **Arbitrage Engine Moat**
- AI die **automatisch** 1000+ alternatieven vergelijkt
- ChatGPT kan 1 offerte analyseren, maar niet systematisch optimaliseren
- Vereist domain expertise in equipment specs + subsidie thresholds

#### 4. **Integration Moat**
- API/Widget in hun CRM systeem
- Batch processing (20 offertes tegelijk)
- Historical tracking ("je hebt dit kwartaal €150k subsidies gevonden")
- ChatGPT = losse sessies, geen persistence

#### 5. **Time Moat**
- Wij: 30 seconden
- Zelf uitzoeken met ChatGPT: 1-2 uur (RVO sites lezen, codes opzoeken, berekenen)
- Voor installateur met 50 projecten = 100 uur/jaar bespaard

#### 6. **Network Effects (Future)**
- Meer gebruikers → Meer edge cases → Betere AI
- Feedback loop: "Deze subsidie werkte wel/niet" → Training data
- Community: "Beste practices" voor subsidie optimalisatie

---

### Why This Is A Real Business

**The Test:**
> "Als je product morgen gratis beschikbaar wordt, zouden klanten het dan nog gebruiken?"

**Antwoord: JA**
- Installateurs willen **tijd besparen** (2 uur → 30 sec)
- Klanten willen **zekerheid** ("garantie dat het klopt")
- Bedrijven willen **optimalisatie** (arbitrage die ze zelf niet vinden)
- Accountants willen **compliance** (deadline tracking, documentatie)

**We verkopen niet "AI offerte scanning" (commodity)**  
**We verkopen "Subsidie Intelligence Platform" (value)**

---

## Technische Architectuur

### Tech Stack (MVP)

#### Backend
- **Framework:** FastAPI (Python 3.11+)
- **LLM:** Claude Sonnet 4.5 via Anthropic API
- **Structured Extraction:** Instructor library + Pydantic v2
- **Database:** PostgreSQL (voor klant data, scan history)
- **File Storage:** S3-compatible (offertes, reports)
- **Cache:** Redis (voor repeated scans)

#### Frontend (Future/Phase 2)
- **Framework:** React + TypeScript
- **UI:** Tailwind CSS
- **State:** React Query
- **Auth:** Clerk/Auth0

#### Infrastructure
- **Hosting:** Railway/Render (MVP), AWS (scale)
- **CDN:** CloudFlare
- **Monitoring:** Sentry (errors) + PostHog (analytics)

### Core Components

#### 1. **Document Processor** (`services/document_processor.py`)
**Input:** PDF offerte  
**Process:**
- Read PDF with Claude's native PDF support (no separate OCR!)
- Extract with Instructor:
  ```python
  client = instructor.from_anthropic(anthropic.Anthropic())
  quote = client.messages.create(
      model="claude-sonnet-4-20250514",
      response_model=Quote,
      messages=[{"role": "user", "content": [...pdf_content...]}]
  )
  ```
**Output:** Structured `Quote` object (Pydantic model)

**Quote Model:**
```python
class Equipment(BaseModel):
    item_type: str  # "warmtepomp", "cnc_machine"
    brand: str
    model: str
    quantity: int
    unit_price: Decimal
    technical_specs: dict  # SCOP, vermogen, energielabel, etc.

class Quote(BaseModel):
    quote_number: str
    date: datetime
    supplier: CompanyInfo
    customer: CompanyInfo
    equipment: list[Equipment]
    total_investment: Decimal
```

#### 2. **Subsidy Matcher** (`services/subsidy_matcher.py`)
**Input:** `Quote` object  
**Process:**
1. **Rule-based pre-filtering:**
   - Keyword matching (warmtepomp → check ISDE)
   - Technical spec filtering (SCOP > 4.0 → eligible)
   - Price thresholds (min €2.500 voor EIA)

2. **LLM verification:**
   - Voor edge cases: Claude verifieert complexe eisen
   - Structured output met `SubsidyMatch` model

3. **Amount calculation:**
   - EIA: `price * 0.40`
   - ISDE: Lookup in meldcode table
   - MIA: Percentage per categorie

**Output:** `SubsidyAnalysis` object

**SubsidyAnalysis Model:**
```python
class SubsidyMatch(BaseModel):
    scheme: str  # "EIA", "ISDE", "MIA"
    code: str  # "220101", "KA18409"
    equipment_matched: str
    eligible: bool
    estimated_amount: Decimal
    percentage: Optional[float]
    requirements: list[str]
    missing_info: list[str]
    confidence: str  # "high", "medium", "low"
    source_url: str

class SubsidyAnalysis(BaseModel):
    quote_summary: str
    matches: list[SubsidyMatch]
    total_potential_savings: Decimal
    recommendations: list[str]  # Arbitrage suggestions
    warnings: list[str]
    deadline: Optional[date]
```

#### 3. **Arbitrage Engine** (`services/arbitrage_engine.py`)
**Input:** `Quote` + `SubsidyAnalysis`  
**Process:**
1. Identify optimization opportunities:
   - Equipment near subsidy thresholds
   - Alternative models with better subsidies
2. Calculate net benefit: `(extra_subsidy - extra_cost)`
3. Rank by ROI

**Example Logic:**
```python
def find_arbitrage_opportunities(equipment: Equipment, current_subsidy: Decimal):
    # Check alternative models
    alternatives = get_equipment_alternatives(equipment.brand, equipment.model)
    
    opportunities = []
    for alt in alternatives:
        alt_subsidy = calculate_subsidy(alt)
        extra_cost = alt.price - equipment.price
        net_benefit = alt_subsidy - current_subsidy - extra_cost
        
        if net_benefit > 500:  # Min €500 net benefit
            opportunities.append({
                "alternative": alt,
                "extra_cost": extra_cost,
                "extra_subsidy": alt_subsidy - current_subsidy,
                "net_benefit": net_benefit
            })
    
    return sorted(opportunities, key=lambda x: x["net_benefit"], reverse=True)
```

#### 4. **Subsidy Database** (`data/subsidies/`)
**Structure:**
```
data/subsidies/
├── eia_2025.json          # EIA Energielijst
├── isde_2025.json         # ISDE meldcodes
├── mia_2025.json          # MIA categorieën
└── equipment_specs.json   # Equipment database (voor arbitrage)
```

**EIA Example:**
```json
{
  "version": "2025",
  "updated": "2025-01-01",
  "categories": [
    {
      "code": "220101",
      "name": "Warmtepomp lucht-water",
      "description": "Elektrische warmtepomp die warmte onttrekt...",
      "requirements": {
        "min_scop": 4.0,
        "min_price": 2500,
        "energy_label": "A++"
      },
      "subsidy_percentage": 0.40,
      "keywords": ["warmtepomp", "heat pump", "lucht-water"]
    }
  ]
}
```

**ISDE Example:**
```json
{
  "version": "2025",
  "warmtepompen": [
    {
      "meldcode": "KA18409",
      "brand": "Daikin",
      "model": "Altherma 3H 16kW",
      "type": "lucht-water",
      "vermogen_kw": 16,
      "scop": 4.65,
      "subsidy_amount": 3800
    }
  ]
}
```

### API Design

#### Endpoints (MVP)

**POST /api/v1/analyze-quote**
```json
// Request
{
  "file": "base64_encoded_pdf",
  "company_info": {
    "name": "Metaal BV",
    "kvk": "12345678"
  }
}

// Response
{
  "scan_id": "scan_abc123",
  "quote_info": {...},
  "subsidies_found": [
    {
      "scheme": "EIA",
      "code": "220101",
      "amount": 4200,
      "confidence": "high"
    }
  ],
  "total_savings": 16000,
  "arbitrage_opportunities": [
    {
      "recommendation": "Upgrade to model X",
      "extra_cost": 800,
      "extra_subsidy": 1200,
      "net_benefit": 400
    }
  ],
  "report_url": "https://subsidiematch.nl/reports/scan_abc123.pdf"
}
```

**GET /api/v1/subsidies**
```json
// Response
{
  "available_schemes": ["EIA", "ISDE", "MIA"],
  "eia_budget_2025": 431000000,
  "isde_budget_2025": 550000000
}
```

### Cost Structure

**Claude API Costs:**
- **Input:** ~1,500-3,000 tokens per 2-5 page PDF
- **Output:** ~500-1,000 tokens per analysis
- **Cost per scan:** ~€0.03-0.10

**With prompt caching (90% discount on repeated system prompts):**
- **Cost per scan:** ~€0.01-0.03

**Target:** <€0.50 per scan (including all infrastructure)

**Budget €100 = 1,000-3,000 analyses**

### Scalability Considerations

**MVP (0-100 scans/day):**
- Single FastAPI instance on Railway
- Claude API direct calls
- PostgreSQL on Railway
- **Cost:** ~€50/month

**Growth (100-1000 scans/day):**
- Multiple FastAPI instances (load balanced)
- Redis cache for repeated equipment lookups
- Prompt caching optimization
- **Cost:** ~€500/month

**Scale (1000+ scans/day):**
- Consider fine-tuned model (cheaper per scan)
- Or open-source LLM (Qwen 2.5 72B on vLLM)
- Distributed processing
- **Cost:** ~€2k/month

---

## Data Bronnen

### Officiële RVO Data

#### 1. **EIA Energielijst 2025**
**URL:** https://www.rvo.nl/sites/default/files/2025-01/Brochure-EIA-Energielijst2025.pdf  
**Format:** PDF (129 pagina's)  
**Inhoud:**
- 129 categorieën energiebesparende bedrijfsmiddelen
- Codes (bijv. 220101 voor warmtepomp lucht-water)
- Technische requirements (SCOP, vermogen, etc.)
- 40% investeringsaftrek voor alles op lijst

**Key Changes 2025:**
- Budget €431M (increased from previous year)
- Nieuwe categorieën: luchtdeuren, fiber laser machines
- Strengere SCOP eisen voor warmtepompen
- Hogere isolatie subsidie caps

**Extractie Plan:**
- PDF → Markdown (met Marker/Docling)
- Parse categorieën met regex/Claude
- Store in JSON database
- Update annually (usually published January)

#### 2. **ISDE Meldcodelijsten**
**URL:** https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten  
**Format:** HTML tables  
**Inhoud:**
- Warmtepompen: 1000+ meldcodes met specifieke modellen
- Isolatiematerialen: Meldcodes per type/dikte
- Glas: HR++/Triple glas codes
- Per meldcode: Merk, model, vermogen, SCOP, subsidiebedrag

**ISDE 2025 Budget:** ~€550M
**Subsidy Ranges:**
- Lucht-water warmtepompen: €2.000-€4.150
- Bodem-water warmtepompen: €4.000-€12.975
- Isolatie: €8-25/m² (depending on type)
- Triple glas: €45-75/m²

**Requirements:**
- Bestaande bouw only (gebouwd voor 1-1-2019)
- Energielabel A++ minimum voor warmtepompen
- Gecertificeerd installateur required

**Extractie Plan:**
- Scrape HTML tables monthly
- Parse met BeautifulSoup
- Map to structured JSON
- Track changes (subsidies wijzigen soms mid-year)

#### 3. **MIA/Vamil Milieulijst**
**URL:** https://www.rvo.nl/subsidies-financiering/mia-vamil  
**Format:** PDF  
**Inhoud:**
- Categorieën milieuvriendelijke bedrijfsmiddelen
- MIA percentages (13%, 27%, 36%, 45%)
- Vamil: 75% willekeurige afschrijving

**Budget 2025:**
- MIA: €189M
- Vamil: €20M

**Categorieën:**
- Circulaire economie
- CO2-reductie
- Energiebesparing (overlap met EIA)
- Elektrische voertuigen
- Waterbesparende systemen

#### 4. **EP-Online API** (Energy Performance)
**URL:** https://www.ep-online.nl  
**Access:** API beschikbaar voor energielabels  
**Use Case:** Verify energielabel van equipment (required for ISDE)

### Data Update Strategie

**Frequency:**
- **EIA:** Annually (January) - manual update
- **ISDE:** Monthly check (budgets can run out mid-year)
- **MIA:** Annually + ad-hoc changes
- **Equipment specs:** Continuous (as manufacturers release new models)

**Notification System:**
- RVO RSS feeds monitoren
- Email alerts bij nieuwe publicaties
- Slack notification naar team bij updates
- Auto-email naar klanten: "EIA 2026 is live, we've updated your scans"

### Proprietary Data (Long-term)

**Equipment Alternatives Database:**
- Voor arbitrage engine
- Maintained by ons team
- Community contributions (power users kunnen suggesties doen)

**Historical Success Rates:**
- Welke subsidies worden goedgekeurd?
- Welke worden vaak afgewezen?
- Gebruik voor "confidence score"

---

## Product Specificaties

### MVP Feature Set (Month 1-2)

**Core Functionality:**
- ✅ PDF upload & parsing
- ✅ Equipment extraction (brand, model, specs)
- ✅ EIA matching & calculation
- ✅ ISDE matching (warmtepompen only voor MVP)
- ✅ Basic arbitrage (1-2 alternatives)
- ✅ PDF report generation
- ✅ Simple web interface (upload + results)

**NOT in MVP:**
- ❌ User accounts/authentication
- ❌ MIA/Vamil (Phase 2)
- ❌ CRM integrations
- ❌ Batch processing
- ❌ Mobile app

### Phase 2 Features (Month 3-4)

**Authentication & Accounts:**
- User registration/login
- Company profiles
- Scan history
- Monthly usage dashboard

**Extended Subsidies:**
- MIA/Vamil support
- Regionale subsidies (provincie, gemeente)
- Combinatie optimalisatie (EIA+ISDE+MIA)

**Enhanced Arbitrage:**
- 5-10 alternative suggestions
- Custom optimization (prioritize: max subsidie vs. min cost)
- "What-if" scenarios

**Reporting:**
- Branded PDF reports (white-label for partners)
- Excel export
- Email delivery

### Phase 3 Features (Month 5-6)

**B2B Features:**
- API access voor CRM integration
- Bulk upload (10-50 offertes tegelijk)
- Team accounts (installateur + medewerkers)
- Dashboard: Total subsidies found this month/quarter

**Integrations:**
- HubSpot/Salesforce apps
- Exact/AFAS accounting software
- Offerte platforms (OfferteStudio, etc.)

**Advanced Intelligence:**
- Deadline tracking & reminders
- Pre-filled aanvraagformulieren (RVO portal integration)
- Success rate predictions
- Compliance checker ("is deze aanvraag compliant?")

### Phase 4 Features (Month 7+)

**Marketplace:**
- Connect bedrijven met installateurs
- Installateur recommendations ("deze installateur kan jouw project met subsidie uitvoeren")

**Financial Integration:**
- Link met banks voor financing
- "Subsidie + lening in 1 package"

**White-label Platform:**
- Grote installateurs kunnen eigen branded versie draaien
- "GeoenergieMatch powered by SubsidieMatch"

---

## Business Model

### Revenue Streams

#### 1. **B2B SaaS (Primary - 80% revenue)**

**Target:** Installateurs, accountants, subsidieadviseurs

**Pricing Tiers:**

| Tier | Price | Scans/month | Features |
|------|-------|-------------|----------|
| **Starter** | €149/month | 20 | Basic matching, PDF reports |
| **Professional** | €299/month | 100 | + Arbitrage, API access, branding |
| **Enterprise** | €999/month | Unlimited | + White-label, dedicated support, CRM integration |

**Unit Economics (Professional tier voorbeeld):**
- Price: €299/month
- COGS: ~€50/month (API costs @ 100 scans)
- Gross margin: 83%
- CAC: €1,000 (assumes 3-month sales cycle)
- Payback: 3.3 months
- LTV (24 month retention): €7,176
- LTV/CAC: 7.2x

#### 2. **Success Fee (Secondary - 20% revenue)**

**Target:** Directe MKB klanten (geen intermediar)

**Model:**
- Upload offerte gratis
- See subsidies found
- Pay 10% van gevonden subsidies als je aanvraagt
- Minimum €99, maximum €2,500 per project
- "No cure, no pay"

**Example:**
- Found subsidy: €8,000
- Fee: €800 (10%)
- Customer keeps: €7,200
- Customer pays: €0 if not approved

**Conversion Funnel:**
- 1000 visitors → 200 uploads (20%) → 100 paid conversions (50%) = €80k revenue

#### 3. **Affiliate/Referrals (Future - 5% revenue)**

**Model:**
- Connect customers met installateurs
- Installateur pays €200-500 per qualified lead
- Win-win: Customer gets subsidie, installateur gets klant

### Pricing Philosophy

**Why €299/month for Professional?**

**Value Delivered:**
- Installateur doet 100 projecten/year = €8.33 per scan
- Finds average €1,000 extra per project via arbitrage
- Total value: €100,000/year extra subsidies found
- Our cost: €3,588/year
- **ROI: 28x**

**Willingness to Pay:**
- Current alternatives:
  - Hire consultant per project: €500-2,000
  - DIY (2 hours per offerte): 100 × 2h × €75/hour = €15,000
- Our pricing = 25% van DIY cost, unlimited scans

**Competitive Positioning:**
- SubsidyCloud: €299/month (similar pricing, validates market)
- Consultants: 10-15% success fee (much higher)
- Our SaaS = predictable cost, unlimited value

### Go-to-Market Economics

**Year 1 Targets:**
- 100 B2B customers (80 Starter, 15 Professional, 5 Enterprise)
- Revenue breakdown:
  - SaaS: €192k (80 × €149 × 12 + 15 × €299 × 12 + 5 × €999 × 12)
  - Success fees: €48k (200 direct conversions × €240 avg)
  - **Total: €240k ARR**

**Cost Structure:**
- COGS: €20k (API costs)
- Team: €120k (2 FTE @ €60k)
- Infrastructure: €6k
- Marketing: €30k
- **Total: €176k**

**EBITDA: €64k (27% margin)**

### Path to Profitability

**Assumption:** 40% MoM growth in customers

| Month | Customers | MRR | ARR | Costs | Profit |
|-------|-----------|-----|-----|-------|--------|
| 1 | 5 | €745 | €8.9k | €14.7k | -€5.8k |
| 3 | 10 | €1.5k | €18k | €14.7k | +€3.3k |
| 6 | 25 | €3.7k | €45k | €14.7k | +€30k/yr |
| 12 | 100 | €15k | €180k | €14.7k | +€165k/yr |

**Break-even: Month 2-3** (assuming 5 beta customers start paying)

---

## Klanten & Distributie

### Target Customer Profiles

#### PERSONA 1: "Dennis de Duurzame Installateur" ⭐ (Primary)

**Demographics:**
- Leeftijd: 35-55 jaar
- Rol: Eigenaar/Directeur installatiebedrijf
- Bedrijfsgrootte: 5-20 medewerkers
- Omzet: €500k-€3M/jaar
- Locatie: Nederland (all provinces)

**Firmographics:**
- Specialisatie: Warmtepompen, zonnepanelen, HVAC
- Projecten: 50-200/jaar
- Gemiddeld projectbedrag: €10k-50k
- Mix: 70% particulier, 30% zakelijk

**Psychographics:**
- Wil groeien maar heeft geen tijd
- Tech-savvy (gebruikt offerte software, email, WhatsApp)
- Wil zich differentiëren van concurrentie
- Cares about klantentevredenheid

**Pain Points:**
1. **Lost sales:** "Klanten vragen subsidie, ik weet het niet, ze gaan naar concurrent"
2. **Time sink:** "Uitzoeken welke subsidie mogelijk is kost 2 uur per project"
3. **Knowledge gap:** "EIA, ISDE, MIA... ik ben installateur, geen subsidie-expert"
4. **Missed opportunities:** "Achteraf blijkt €5k subsidie mogelijk, klant is teleurgesteld"

**Jobs To Be Done:**
- Klanten helpen met subsidie aanvragen
- Meer projecten binnenhalen
- Hogere marges (door subsidie-optimalisatie)
- Minder tijd kwijt aan administratie

**How We Help:**
- 30 seconden scan = instant antwoord voor klant
- Arbitrage suggestions = hogere projectwaarde
- Branded reports = professionele uitstraling
- API integration = naadloos in workflow

**Acquisition Channels:**
- LinkedIn (DM campaigns)
- ISSO netwerken (installatievakbond)
- Vakbeurzen (Installatie, Energie Nederland)
- Google Ads ("subsidie tool installateurs")
- Referrals (installateur → installateur)

---

#### PERSONA 2: "Anna de Adviserende Accountant" (Secondary)

**Demographics:**
- Leeftijd: 30-50 jaar
- Rol: Accountant/Adviseur bij MKB-kantoor
- Klanten: 50-200 MKB bedrijven
- Kantoorgrootte: 10-100 medewerkers

**Firmographics:**
- Type kantoor: MKB accountancy/advieskantoor
- Services: Boekhouding + bedrijfsadvies
- Klanten per accountant: 30-50
- Investeringsadvies: 10-20 klanten/jaar vragen advies

**Psychographics:**
- Wil waarde toevoegen beyond boekhouden
- Conservative (risk-averse, wil zekerheid)
- Wil upsell advisory services
- Trusted advisor van hun klanten

**Pain Points:**
1. **Knowledge gap:** "Klant vraagt of investering subsidie krijgt, ik weet het niet"
2. **Missed upsell:** "Ik zou advisory fee kunnen rekenen voor subsidie advies"
3. **Time constraint:** "Ik heb geen tijd om RVO sites door te worstelen"
4. **Compliance risk:** "Als ik verkeerde advies geef, ben ik liable"

**Jobs To Be Done:**
- Klanten adviseren over investeringen
- Extra diensten verkopen (advisory fee)
- Klanten blij houden (retention)
- Risk mitigation (correcte informatie)

**How We Help:**
- Tool die ze vertrouwen (compliance guaranteed)
- White-label reports (met hun branding)
- Dashboard: "Je hebt €150k subsidies gevonden voor klanten dit kwartaal"
- Upsell angle: "Advisory service powered by SubsidieMatch"

**Acquisition Channels:**
- AccountancyVanmorgen (vakblad)
- NBA bijeenkomsten (Nederlandse Beroepsorganisatie van Accountants)
- Partnerships met Exact/AFAS
- LinkedIn (target "accountant MKB")
- Webinars ("Subsidie advisory als upsell")

---

#### PERSONA 3: "Fatima de Fabrieks Manager" (Tertiary)

**Demographics:**
- Leeftijd: 35-60 jaar
- Rol: Operations Manager / CFO
- Bedrijf: MKB productie/industrie
- Omzet: €5M-50M/jaar

**Firmographics:**
- Sector: Metaalbewerking, food production, etc.
- Investeringen: €100k-€500k/jaar in machines
- Frequency: 2-10 grote investeringen/jaar
- Decision makers: CFO + Operations + Directie

**Psychographics:**
- ROI-focused
- Wants all information before decision
- Risk-averse (grote investeringen)
- Busy (beslist snel als business case klopt)

**Pain Points:**
1. **Complex:** "Welke subsidie past bij CNC machine van €200k?"
2. **Opportunity cost:** "Mis ik €50k subsidie door verkeerde keuze?"
3. **Time sensitive:** "EIA moet binnen 3 maanden aangevraagd"
4. **Expertise:** "Wij zijn geen subsidie experts"

**Jobs To Be Done:**
- CapEx optimaliseren (max rendement uit investeringen)
- Board overtuigen (business case met subsidie is makkelijker)
- Compliance (correcte aanvragen)
- Sustainability goals (duurzame investeringen)

**How We Help:**
- Upload machine offerte → instant subsidie calc
- Arbitrage: "Kies model X voor €10k extra subsidie"
- CFO-friendly reports (ROI, payback period)
- Deadline tracking (no missed opportunities)

**Acquisition Channels:**
- Partnerships met machine leveranciers
- MKB-Nederland (ondernemersvereniging)
- LinkedIn Ads (target CFO/Operations Manager)
- Case studies (B2B content marketing)
- Referrals via accountants

---

### Prioritization

**Phase 1 (Month 1-3): Focus 100% on Installateurs**
- Easiest to acquire (clear pain, immediate value)
- Highest volume (50-200 projects/jaar)
- Best testimonials ("Found €50k subsidies in first month")
- Product-market fit fastest

**Phase 2 (Month 4-6): Add Accountants**
- Longer sales cycle (need case studies from Phase 1)
- Higher scale potential (50-200 clients each)
- Need white-label features (Phase 2 product)

**Phase 3 (Month 7+): Direct to MKB**
- Lowest priority (hardest to reach, lower frequency)
- But highest ACV (€500-2,000 per project)
- Via inbound (content marketing + SEO)

---

### Distribution Strategy

#### Channel 1: Direct Sales (Outbound)

**Tactic:** LinkedIn DM campaigns + cold email

**Target:** 500 installateurs in NL

**Message:**
> "Hoi Dennis, ik zie dat je warmtepompen installeert. Hoeveel van je klanten vragen of ze subsidie kunnen krijgen? Wij hebben een tool die in 30 seconden alle subsidies checkt + optimalisatie tips geeft. €149/maand, 20 scans. Interesse in gratis demo?"

**Conversion Funnel:**
- 500 DMs → 50 replies (10%) → 15 demos (30%) → 5 customers (33%)
- Time to customer: 2-4 weeks

**Effort:** 1 person, 4 hours/week = 125 DMs/week

---

#### Channel 2: Content Marketing (Inbound)

**Tactic:** LinkedIn posts + SEO blog

**Content Themes:**
1. **Case studies:** "Installateur vond €50k subsidies met SubsidieMatch"
2. **Education:** "EIA vs ISDE: Welke past bij jouw project?"
3. **Arbitrage tips:** "3 trucjes die €5k extra subsidie opleveren"
4. **News:** "EIA 2026 changes: Wat betekent dit voor jou?"

**Frequency:** 3x/week LinkedIn, 1x/week blog

**Conversion Funnel:**
- 10,000 impressions → 200 website visits (2%) → 20 signups (10%) → 5 customers (25%)
- Time to customer: 1-3 months

**Effort:** 1 person, 10 hours/week

---

#### Channel 3: Partnerships (Leverage)

**Target Partners:**

**A) Offerte Platforms**
- OfferteStudio, QuoteWizard, etc.
- Integration: "Subsidie Check" button in hun tool
- Revenue share: 20% of subscriptions via them

**B) Installateur Platforms**
- Techniek Nederland (brancheorganisatie)
- ISSO (Installatiesector)
- Deal: Exclusive deal voor hun leden (€119 ipv €149)

**C) Accounting Software**
- Exact, AFAS, Twinfield
- App in their marketplace
- Freemium: Basic tier free, Pro tier paid

**Conversion Funnel:**
- 1 partnership = 100-1,000 potential customers
- Time to customer: 3-6 months (partnership + integration)

**Effort:** 1 person, dedicated partnerships role (Month 4+)

---

#### Channel 4: Events & Community

**Tactics:**
- Sponsor vakbeurzen (Installatie, Energie Nederland)
- Host webinars ("Subsidie masterclass voor installateurs")
- Local MKB meetups (pitch + demo)

**Frequency:** 1 event/month

**Conversion:** 50 attendees → 10 signups → 3 customers

---

### Customer Acquisition Cost (CAC) Targets

| Channel | CAC Target | Time to Customer | Scale Potential |
|---------|------------|------------------|-----------------|
| Direct Sales | €500-1,000 | 2-4 weeks | Medium (limited by manual effort) |
| Content Marketing | €200-500 | 1-3 months | High (scales with content) |
| Partnerships | €100-300 | 3-6 months | Very High (leverage) |
| Events | €300-800 | 1-2 months | Low (limited events) |

**Blended CAC Target Year 1:** €600

---

## Go-to-Market Strategie

### Phase 1: MVP + First 5 Customers (Week 1-8)

**Goal:** Product validation + testimonials

**Week 1-2: Build MVP**
- Implement core features (offerte scan, EIA matching, basic report)
- Test with 10 sample offertes
- Deploy on Railway

**Week 3-4: Beta Recruitment**
- Reach out to 20 installateurs in netwerk (warm introductions)
- Offer: "Gratis beta access, je helpt ons product testen"
- Goal: 5 beta users

**Week 5-8: Beta Period**
- Onboard 5 beta users
- Scan their last 10 offertes (total 50 scans)
- Gather feedback:
  - What subsidies did we miss?
  - Which features are most valuable?
  - Would you pay for this?
- Iterate based on feedback

**Success Metrics:**
- ✅ 5 active beta users
- ✅ 50 scans completed
- ✅ 3+ testimonials ("Found €X subsidies I missed")
- ✅ 80% would pay post-beta

**Output:**
- Case study: "Beta user vond €50k subsidies in 1 week"
- Product improvements list
- Pricing validation

---

### Phase 2: Product-Market Fit (Month 3-4)

**Goal:** 20-30 paying customers

**Tactics:**

**A) Convert Beta → Paid**
- Offer early adopter discount: €99/month (normally €149)
- Lifetime lock-in (price never increases)
- Target: 4/5 convert = 4 customers

**B) Warm Outreach (50 prospects)**
- LinkedIn: Friends-of-friends in installatie sector
- Message: "Remember that subsidie tool I mentioned? Just launched, check out these results [case study link]"
- Target: 10% conversion = 5 customers

**C) Cold Outreach (200 prospects)**
- LinkedIn DMs: 100 installateurs
- Email: 100 accountants
- Offer: "Gratis scan van je laatste 3 offertes - laat zien hoeveel je mist"
- Target: 5% conversion = 10 customers

**D) Content Marketing**
- 3x/week LinkedIn posts (case studies, tips, news)
- Launch website met "Gratis Subsidie Scan" lead magnet
- SEO blog: 2 articles/week
- Target: 50 leads → 10 trials → 3 customers

**E) Partnership Conversations**
- Approach 5 offerte platforms
- Approach 3 installateur verenigingen
- Goal: 1 signed partnership (goes live Month 5)

**Success Metrics:**
- ✅ 25 paying customers (€3,725/month MRR)
- ✅ <€1,000 CAC
- ✅ 1 partnership signed
- ✅ 500 website visitors/month

---

### Phase 3: Scale to 100 Customers (Month 5-12)

**Goal:** €15k MRR (€180k ARR)

**Tactics:**

**A) Double Down on What Works**
- Analyze Month 3-4: Which channel had best CAC/LTV?
- Allocate 60% effort to best channel
- Example: If LinkedIn DMs work best → hire VA for outreach

**B) Launch Partnerships**
- Partnership integration goes live
- Co-marketing: Webinar with partner
- Target: 20 customers via partnerships

**C) Paid Acquisition**
- Google Ads: "EIA subsidie berekenen" keywords
- LinkedIn Ads: Target "installateur" "warmtepomp"
- Budget: €2k/month
- Target: 10 customers via paid

**D) Referral Program**
- Customers get 1 month free for each referral
- Referred customer gets 1 month free
- Target: 20% of new customers via referral

**E) Content at Scale**
- 5x/week LinkedIn
- 1 YouTube video/week
- 1 case study/month
- SEO: Target 2,000 visitors/month

**Success Metrics:**
- ✅ 100 paying customers
- ✅ €15k MRR
- ✅ <€600 blended CAC
- ✅ 20% MoM growth sustained

---

### Phase 4: Enterprise & Scale (Month 13-24)

**Goal:** €50k MRR (€600k ARR)

**Tactics:**

**A) Enterprise Sales**
- Target: Grote installateurs (50-200 medewerkers)
- Offer: White-label, dedicated support, custom integrations
- Pricing: €2k-5k/month
- Target: 10 enterprise customers = €30k MRR

**B) Geographic Expansion**
- Belgium (similar subsidy system)
- Germany (different system, more research needed)

**C) Product Expansion**
- Add regionale subsidies (provincie, gemeente)
- Add financial integration (subsidie + lening)
- Add marketplace (connect bedrijven met installateurs)

**D) Team Expansion**
- Hire 2 sales reps
- Hire 1 customer success manager
- Hire 1 data analyst (subsidie data maintenance)

---

### Marketing Budget Allocation

**Month 1-3: €3k total**
- Team time: €2k (sweat equity)
- Tools: €500 (website, email, CRM)
- Ads: €500 (test small campaigns)

**Month 4-6: €10k total**
- Team: €5k
- Ads: €3k
- Events: €1k
- Tools: €1k

**Month 7-12: €30k total**
- Team: €15k (hire marketing person)
- Ads: €10k
- Events/Partnerships: €3k
- Tools: €2k

---

### Key Metrics Dashboard

**North Star Metric:** MRR (Monthly Recurring Revenue)

**Leading Indicators:**
- Website visitors/month
- Leads generated (free scans)
- Demos booked
- Trial signups

**Lagging Indicators:**
- Paying customers
- MRR
- Churn rate
- Net Revenue Retention

**Customer Health:**
- Scans per customer/month (engagement)
- Subsidies found per scan (value delivered)
- NPS score

**Target Metrics (Month 12):**
- 100 customers
- €15k MRR
- 2,000 website visitors/month
- 5% churn/month
- NPS: 50+

---

## Development Roadmap

### Month 1-2: MVP Development

**Sprint 1 (Week 1-2): Core Infrastructure**
- [ ] Project setup (FastAPI, PostgreSQL, Railway)
- [ ] Claude API integration + Instructor setup
- [ ] Pydantic models (Quote, Equipment, SubsidyMatch)
- [ ] PDF parsing with Claude
- [ ] Basic EIA database (top 20 codes)

**Sprint 2 (Week 3-4): Matching Engine**
- [ ] EIA matching logic (rule-based + LLM verification)
- [ ] Subsidy calculation
- [ ] ISDE warmtepomp matching (top 50 meldcodes)
- [ ] Basic arbitrage (1-2 alternatives)

**Sprint 3 (Week 5-6): Output & Interface**
- [ ] PDF report generation
- [ ] Simple web UI (upload + results page)
- [ ] Deploy to Railway
- [ ] Cost monitoring

**Sprint 4 (Week 7-8): Testing & Polish**
- [ ] Test with 10 real offertes
- [ ] Fix edge cases
- [ ] Add confidence scores
- [ ] Beta user onboarding docs

**Deliverable:** Working MVP that can scan offertes and find EIA + basic ISDE

---

### Month 3-4: Product-Market Fit Features

**Sprint 5 (Week 9-10): User Accounts**
- [ ] Authentication (email + password)
- [ ] Company profiles
- [ ] Scan history
- [ ] Usage dashboard

**Sprint 6 (Week 11-12): Extended Database**
- [ ] Full ISDE meldcodelijsten (all 1000+ codes)
- [ ] Full EIA Energielijst (all 129 categories)
- [ ] Equipment specs database (for arbitrage)

**Sprint 7 (Week 13-14): Enhanced Reports**
- [ ] Branded PDF reports (logo upload)
- [ ] Excel export
- [ ] Email delivery
- [ ] Deadline calculator

**Sprint 8 (Week 15-16): Analytics & Optimization**
- [ ] Scan analytics (which subsidies found most)
- [ ] A/B test report formats
- [ ] Prompt optimization (reduce costs)
- [ ] Performance monitoring (Sentry)

**Deliverable:** Production-ready product with accounts, full database, professional reports

---

### Month 5-6: B2B Features

**Sprint 9 (Week 17-18): API**
- [ ] REST API with authentication
- [ ] API documentation (Swagger)
- [ ] Rate limiting
- [ ] Webhooks (scan completed)

**Sprint 10 (Week 19-20): Team Features**
- [ ] Team accounts (multiple users per company)
- [ ] Role-based access (admin, user)
- [ ] Bulk upload (10-50 offertes at once)
- [ ] Shared scan history

**Sprint 11 (Week 21-22): MIA/Vamil**
- [ ] MIA Milieulijst database
- [ ] MIA matching logic
- [ ] Vamil calculations
- [ ] Combined optimization (EIA+ISDE+MIA)

**Sprint 12 (Week 23-24): Integrations Prep**
- [ ] Zapier integration
- [ ] HubSpot app (beta)
- [ ] CSV import/export
- [ ] Partnership dashboard

**Deliverable:** Full B2B platform with API, teams, and all subsidy types

---

### Month 7-12: Scale & Enterprise

**Features:**
- White-label platform
- Advanced arbitrage (10+ alternatives)
- Pre-filled RVO forms
- Success rate predictions
- Regional subsidies
- Mobile app (React Native)
- CRM integrations (Salesforce, HubSpot)
- Accounting software plugins (Exact, AFAS)

---

### Technical Debt & Maintenance

**Ongoing Tasks:**
- Monthly ISDE data updates
- Annual EIA updates (January)
- Security audits (quarterly)
- Performance optimization (as traffic grows)
- Bug fixes & edge cases
- Customer feedback implementation

---

## Financiële Projecties

### Year 1 Projections

**Assumptions:**
- Start: Month 1 with 5 beta users (free)
- Growth: 40% MoM in customers (conservative)
- Churn: 5% per month
- Pricing: €149/month average (mix of tiers)

| Month | New Customers | Total Customers | MRR | ARR | Costs | Monthly Profit |
|-------|---------------|-----------------|-----|-----|-------|----------------|
| 1 | 5 | 5 | €0 | €0 | €5k | -€5k |
| 2 | 3 | 7 | €447 | €5.4k | €5k | -€4.6k |
| 3 | 5 | 11 | €1.1k | €13k | €8k | -€6.9k |
| 6 | 12 | 30 | €4.5k | €54k | €10k | -€5.5k |
| 9 | 20 | 60 | €8.9k | €107k | €12k | -€3.1k |
| 12 | 30 | 100 | €14.9k | €179k | €15k | -€0.1k |

**Year 1 Summary:**
- Ending ARR: €179k
- Total Revenue: €90k (avg across 12 months)
- Total Costs: €108k
- Net: -€18k (investment year)
- Ending MRR: €14.9k (growing 40% MoM)

---

### Year 2 Projections

**Assumptions:**
- Start: 100 customers @ €14.9k MRR
- Growth: 20% MoM (slower but sustainable)
- Churn: 3% (improved retention)
- Price increase: €169/month average (more enterprise)

| Quarter | Customers | MRR | ARR | Costs/Quarter | Quarterly Profit |
|---------|-----------|-----|-----|---------------|------------------|
| Q1 | 150 | €25k | €304k | €50k | -€5k |
| Q2 | 225 | €38k | €456k | €60k | +€54k |
| Q3 | 340 | €57k | €689k | €75k | +€96k |
| Q4 | 500 | €85k | €1.0M | €100k | +€155k |

**Year 2 Summary:**
- Ending ARR: €1.02M
- Total Revenue: €590k
- Total Costs: €285k
- Net Profit: €305k (51% margin)
- Ending MRR: €85k

---

### Year 3 Projections

**Assumptions:**
- Focus on enterprise (higher ACV)
- Geographic expansion (Belgium)
- Product expansion (regional subsidies)

**Conservative:**
- Ending ARR: €2.5M
- 1,000 customers
- Net Profit: €1M (40% margin)

**Optimistic:**
- Ending ARR: €5M
- 1,500 customers (more enterprise)
- Net Profit: €2M (40% margin)

---

### Unit Economics (Mature State)

**Per Customer (Professional tier):**
- ARPU: €299/month
- COGS: €50/month (API + infrastructure)
- Gross Margin: 83%
- CAC: €600
- Payback Period: 2.4 months
- LTV (24 months): €7,176
- LTV/CAC: 12x

**At Scale (1,000 customers):**
- ARR: €3.6M
- Gross Profit: €3M (83% margin)
- Operating Costs: €1.5M (team, marketing, overhead)
- EBITDA: €1.5M (42% margin)

---

### Funding Requirements

**Bootstrap Scenario (Recommended):**
- Month 1-6: €18k founder investment (for costs before revenue positive)
- Month 7+: Self-funded from revenue
- No external funding needed

**Why Bootstrap:**
- ✅ Low capital requirements (software, not hardware)
- ✅ Fast to revenue (SaaS, not long sales cycles)
- ✅ High margins (83% gross margin)
- ✅ Retain control (no dilution)

**Accelerated Scenario (Optional):**
- Raise €200k seed round (Month 6)
- Use for: Hire sales team (3 people), aggressive marketing (€50k/month)
- Goal: Accelerate to €1M ARR by Month 18 (instead of Month 24)
- Dilution: 15-20%

---

## Team & Resources

### Current Team

**Founder 1: [Jasper]**
- Role: CEO / Lead Developer
- Background: AI Engineering, Data Science, Healthcare Tech
- Responsibilities:
  - Product development (MVP)
  - Technical architecture
  - Claude API integration
  - Customer interviews

**Founder 2: [TBD - if applicable]**
- Role: [To be defined]
- Background: [TBD]
- Responsibilities: [TBD]

---

### Hiring Roadmap

**Month 3-6:**
- No hires (founders do everything)

**Month 7-9: First Hire**
- **Role:** Sales/Customer Success
- **Salary:** €3k-4k/month
- **Responsibilities:**
  - Outbound sales (LinkedIn, email)
  - Customer onboarding
  - Feedback collection
  - Basic support

**Month 10-12: Second Hire**
- **Role:** Marketing/Content
- **Salary:** €3k-4k/month
- **Responsibilities:**
  - Content creation (LinkedIn, blog)
  - SEO optimization
  - Partnership management
  - Lead generation

**Year 2:**
- Sales Rep #2 (Month 15)
- Developer #2 (Month 18) - for enterprise features
- Data Analyst (Month 20) - for subsidy database maintenance
- Customer Success Manager (Month 22)

---

### Advisory Board (Aspirational)

**Ideal Advisors:**
1. **Subsidy Expert** - Former RVO employee, knows all regelingen
2. **B2B SaaS Founder** - Built successful SaaS to €5M+ ARR
3. **Installatie Sector Insider** - Connected in installatiewereld
4. **Legal/Compliance** - Helps with liability, terms of service

**Compensation:** 0.5-1% equity, advisory shares

---

### Tools & Infrastructure

**Development:**
- GitHub (code)
- Linear (project management)
- Figma (design)
- Cursor/Claude (AI coding assistant)

**Production:**
- Railway/Render (hosting)
- PostgreSQL (database)
- Redis (cache)
- CloudFlare (CDN)
- Anthropic API (Claude)

**Business:**
- Notion (docs, wiki)
- Slack (communication)
- HubSpot (CRM)
- Stripe (payments)
- PostHog (analytics)
- Sentry (error monitoring)

**Cost:** ~€500/month for all tools (MVP), ~€2k/month at scale

---

## Risk Analysis & Mitigation

### Top Risks

#### 1. **Subsidy Regelingen Veranderen**
**Risk:** RVO verandert EIA/ISDE rules drastically  
**Likelihood:** Medium (regelingen wijzigen jaarlijks)  
**Impact:** High (entire database moet opnieuw)  
**Mitigation:**
- Monitor RVO announcements closely
- Build flexible data structure (easy to update)
- Communicate changes to customers proactively
- "We update automatically when EIA 2026 launches"

---

#### 2. **AI Hallucinations (Incorrect Subsidies)**
**Risk:** Claude geeft verkeerde subsidy informatie  
**Likelihood:** Low-Medium (LLMs kunnen hallucineren)  
**Impact:** Very High (liability, customer trust)  
**Mitigation:**
- Rule-based checks before LLM (sanity checks)
- Confidence scores (high/medium/low)
- Disclaimer: "Always verify with RVO before applying"
- Insurance: Professional liability insurance (€2k/year)
- Human review for edge cases (low confidence)

---

#### 3. **Customer Doesn't Want to Pay**
**Risk:** Installateurs willen gratis trial, maar niet betalen  
**Likelihood:** Medium (SaaS churn is real)  
**Impact:** Medium (affects revenue growth)  
**Mitigation:**
- Strong value demonstration (show €50k found in trial)
- Success-based alternative (10% fee model)
- Lock-in: Annual contract with discount
- Reduce friction: Easy onboarding, instant value

---

#### 4. **Competitor Copies Us**
**Risk:** Subsidie Expertise of SubsidyCloud adds our features  
**Likelihood:** High (if we succeed)  
**Impact:** Medium (market share competition)  
**Mitigation:**
- Speed: Get to 100 customers fast (network effects)
- Data moat: Best subsidy database (continuously improved)
- Brand: Be the "known name" for subsidie matching
- Features: Always 6 months ahead (arbitrage, integrations)

---

#### 5. **Claude API Costs Too High**
**Risk:** Usage grows, API costs eat margins  
**Likelihood:** Medium (as we scale)  
**Impact:** Medium (margin compression)  
**Mitigation:**
- Prompt caching (90% discount on repeated calls)
- Batch processing (amortize system prompts)
- Plan B: Fine-tuned model (cheaper per request)
- Plan C: Open-source LLM (Qwen 2.5, self-hosted)
- Pricing: Build cost increases into pricing (€299 → €399 if needed)

---

#### 6. **Regulatory/Legal Issues**
**Risk:** Providing "financial advice" zonder licentie?  
**Likelihood:** Low (we don't give advice, just info)  
**Impact:** High (fines, shutdown)  
**Mitigation:**
- Disclaimer: "For informational purposes only, verify with RVO"
- Legal review: Terms of Service by lawyer (€2k)
- Insurance: Professional liability (€2k/year)
- Position as "tool" not "adviseur"

---

## Next Steps

### Immediate Actions (This Week)

- [x] Register subsidiematch.nl domain ✅
- [ ] Set up project repository on GitHub
- [ ] Start MVP development (Sprint 1)
- [ ] Create list of 50 potential beta users (installateurs in network)
- [ ] Draft beta outreach message

### Week 2-4 Actions

- [ ] Complete MVP core features
- [ ] Test with 10 sample offertes
- [ ] Reach out to 20 beta candidates
- [ ] Schedule 5 beta user onboarding calls

### Month 2 Actions

- [ ] Onboard 5 beta users
- [ ] Scan 50 offertes (10 per user)
- [ ] Collect testimonials
- [ ] Write first case study
- [ ] Set up LinkedIn content calendar

### Month 3 Actions

- [ ] Convert beta → paid (target 3-4 customers)
- [ ] Launch paid product (€149/month)
- [ ] Start cold outreach (100 prospects)
- [ ] Launch website with lead magnet
- [ ] Reach out to 5 potential partners

---

## Success Metrics

### Month 3 Goals
- ✅ 5 paying customers
- ✅ €745 MRR
- ✅ 3+ testimonials
- ✅ <€1,000 CAC
- ✅ Product works reliably (80%+ accuracy)

### Month 6 Goals
- ✅ 25 paying customers
- ✅ €3,725 MRR
- ✅ 1 partnership signed
- ✅ 500 website visitors/month
- ✅ <€800 CAC

### Month 12 Goals
- ✅ 100 paying customers
- ✅ €14,900 MRR
- ✅ 2,000 website visitors/month
- ✅ <€600 blended CAC
- ✅ Break-even or profitable

### Year 2 Goals
- ✅ 500 customers
- ✅ €85k MRR (€1M ARR)
- ✅ 40%+ net margin
- ✅ Expand to Belgium

---

## Appendix

### Resources

**Official Data Sources:**
- RVO EIA: https://www.rvo.nl/subsidies-financiering/eia
- RVO ISDE: https://www.rvo.nl/subsidies-financiering/isde
- RVO MIA/Vamil: https://www.rvo.nl/subsidies-financiering/mia-vamil
- RVO Open Data: https://www.rvo.nl/onderwerpen/open-data

**Industry Organizations:**
- Techniek Nederland: https://www.technieknederland.nl
- ISSO: https://www.isso.nl
- MKB-Nederland: https://www.mkb.nl

**Competitors:**
- SubsidyCloud: https://subsidycloud.nl
- Simpel Subsidie: https://simpelsubsidie.nl
- Subsidie Expertise: https://subsidie-expertise.nl

**Technical:**
- Anthropic Claude API: https://docs.anthropic.com
- Instructor Library: https://github.com/jxnl/instructor
- FastAPI: https://fastapi.tiangolo.com

---

### Contact

**Email:** info@subsidiematch.nl  
**Website:** https://subsidiematch.nl  
**LinkedIn:** [To be created]  
**Phone:** [To be added]

---

**Document Version:** 1.0  
**Last Updated:** December 1, 2024  
**Next Review:** January 1, 2025 (after EIA 2026 release)

---

## Changelog

**v1.0 (Dec 1, 2024):**
- Initial comprehensive documentation
- Market research completed
- Competitive analysis finalized
- Technical architecture defined
- Go-to-market strategy documented
- Financial projections modeled

**Future Updates:**
- v1.1: After beta period (add learnings)
- v1.2: After first 25 customers (refine ICP)
- v2.0: Year 2 strategy (after €1M ARR)