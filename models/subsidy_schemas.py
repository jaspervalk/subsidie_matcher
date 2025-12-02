"""
Pydantic models for SubsidieMatch - EIA, ISDE, and MIA/Vamil subsidy matching.

This module defines the data structures for:
- Equipment from quotes (extracted via Claude)
- Subsidy codes (EIA, ISDE, MIA/Vamil)
- Matching results and calculations
- Arbitrage opportunities
"""

from pydantic import BaseModel, Field, field_validator
from typing import List, Optional, Dict, Any, Literal
from datetime import datetime
from enum import Enum
from decimal import Decimal


# ============================================================================
# ENUMS
# ============================================================================

class SubsidyScheme(str, Enum):
    """Subsidy scheme types"""
    EIA = "EIA"  # Energie-investeringsaftrek
    ISDE = "ISDE"  # Investeringssubsidie Duurzame Energie
    MIA = "MIA"  # Milieu-investeringsaftrek
    VAMIL = "Vamil"  # Willekeurige afschrijving milieu-investeringen


class EquipmentCategory(str, Enum):
    """Equipment categories for matching"""
    WARMTEPOMP = "warmtepomp"
    ISOLATIE = "isolatie"
    GLAS = "glas"
    ZONNEBOILER = "zonneboiler"
    CNC_MACHINE = "cnc_machine"
    LED_VERLICHTING = "led_verlichting"
    KOELING = "koeling"
    VENTILATIE = "ventilatie"
    ELEKTRISCH_VOERTUIG = "elektrisch_voertuig"
    OTHER = "other"


class ISDECategory(str, Enum):
    """ISDE subsidy categories"""
    WARMTEPOMP = "warmtepomp"
    ISOLATIE = "isolatie"
    ISOLATIEMATERIALEN = "isolatiematerialen"  # Alias for isolatie
    GLAS = "glas"
    HOOGRENDEMENTSGLAS = "hoogrendementsglas"  # Alias for glas
    ZONNEBOILER = "zonneboiler"


# ============================================================================
# EQUIPMENT MODELS (Input - from PDF quotes)
# ============================================================================

class Equipment(BaseModel):
    """Equipment extracted from a quote PDF"""

    # Basic info
    description: str = Field(..., description="Equipment description from quote")
    brand: Optional[str] = Field(None, description="Brand/manufacturer")
    model: Optional[str] = Field(None, description="Model number/name")
    quantity: int = Field(1, ge=1, description="Quantity")
    unit_price: float = Field(..., ge=0, description="Unit price in EUR")
    total_price: float = Field(..., ge=0, description="Total price (quantity * unit_price)")

    # Technical specs (extracted where available)
    specs: Dict[str, Any] = Field(default_factory=dict, description="Technical specifications")

    # Categorization (from Claude)
    category: Optional[EquipmentCategory] = Field(None, description="Equipment category")
    keywords: List[str] = Field(default_factory=list, description="Keywords for matching")

    # Metadata
    line_number: Optional[int] = Field(None, description="Line number in quote")
    extracted_text: Optional[str] = Field(None, description="Original text from PDF")

    @field_validator('total_price')
    @classmethod
    def validate_total_price(cls, v, info):
        """Ensure total_price matches quantity * unit_price"""
        if 'quantity' in info.data and 'unit_price' in info.data:
            expected = info.data['quantity'] * info.data['unit_price']
            if abs(v - expected) > 0.01:  # Allow small floating point errors
                return expected
        return v

    class Config:
        json_schema_extra = {
            "example": {
                "description": "Daikin Altherma 3H warmtepomp 16kW",
                "brand": "Daikin",
                "model": "Altherma 3H 16kW",
                "quantity": 1,
                "unit_price": 12000.0,
                "total_price": 12000.0,
                "specs": {
                    "power_kw": 16.0,
                    "type": "lucht-water"
                },
                "category": "warmtepomp",
                "keywords": ["warmtepomp", "daikin", "altherma", "heating"]
            }
        }


class Quote(BaseModel):
    """A quote/offerte containing multiple equipment items"""

    # Quote metadata
    quote_number: Optional[str] = Field(None, description="Quote number from PDF")
    date: Optional[datetime] = Field(None, description="Quote date")
    customer_name: Optional[str] = Field(None, description="Customer name")
    supplier_name: Optional[str] = Field(None, description="Supplier/installer name")

    # Equipment list
    equipment: List[Equipment] = Field(..., description="List of equipment items")

    # Totals
    subtotal: float = Field(..., ge=0, description="Subtotal excluding VAT")
    vat_amount: Optional[float] = Field(None, ge=0, description="VAT amount")
    total_including_vat: Optional[float] = Field(None, ge=0, description="Total including VAT")

    # Processing metadata
    uploaded_at: datetime = Field(default_factory=datetime.now, description="Upload timestamp")
    processed_at: Optional[datetime] = Field(None, description="Processing timestamp")

    class Config:
        json_schema_extra = {
            "example": {
                "quote_number": "OFF-2025-001",
                "date": "2025-01-15",
                "customer_name": "Jan Jansen BV",
                "supplier_name": "Installatiebedrijf De Boer",
                "equipment": [],
                "subtotal": 12000.0,
                "vat_amount": 2520.0,
                "total_including_vat": 14520.0
            }
        }


# ============================================================================
# SUBSIDY CODE MODELS (Database schemas)
# ============================================================================

class EIACode(BaseModel):
    """EIA (Energie-investeringsaftrek) code"""

    code: str = Field(..., description="EIA code (e.g., 211102)")
    title: str = Field(..., description="Code title")
    description: Optional[str] = Field(None, description="Detailed description")
    category: Optional[str] = Field(None, description="Category letter")
    chapter: Optional[str] = Field(None, description="Chapter name")
    subsidy_percentage: float = Field(0.40, description="Subsidy percentage (always 0.40)")
    min_investment: float = Field(2500.0, description="Minimum investment in EUR")
    max_investment_per_unit: Optional[float] = Field(None, description="Max investment per unit")
    page: Optional[int] = Field(None, description="Page number in source PDF")

    class Config:
        json_schema_extra = {
            "example": {
                "code": "211102",
                "title": "Warmtepompboiler",
                "description": "Bestemd voor het nuttig aanwenden van omgevingswarmte...",
                "category": "A",
                "chapter": "Verwarmen",
                "subsidy_percentage": 0.40,
                "min_investment": 2500.0,
                "page": 20
            }
        }


class ISDEMeldcode(BaseModel):
    """ISDE meldcode for specific product"""

    scheme: Literal["ISDE"] = "ISDE"
    category: ISDECategory = Field(..., description="ISDE category")
    meldcode: str = Field(..., description="Unique meldcode")
    manufacturer: Optional[str] = Field(None, description="Manufacturer name (merk)")
    model: Optional[str] = Field(None, description="Model name/number")

    # Amount fields - warmtepomp uses amount_eur, isolatie/glas use amounts dict
    amount_eur: Optional[float] = Field(None, ge=0, description="Fixed subsidy amount in EUR (warmtepomp)")
    amounts: Optional[Dict[str, Optional[float]]] = Field(None, description="Subsidy amounts by housing type (isolatie/glas)")

    # Source metadata
    source: Optional[Dict[str, str]] = Field(None, description="Source file info")

    # Technical attributes (varies by category)
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Technical attributes")

    class Config:
        json_schema_extra = {
            "example": {
                "scheme": "ISDE",
                "category": "warmtepomp",
                "meldcode": "KA01205",
                "manufacturer": "Alpha Innotec",
                "model": "SWC 172K3",
                "amount_eur": 5775.0,
                "attributes": {
                    "power_kw": 19.0,
                    "refrigerant": "R410A",
                    "type": "Grond-Water"
                }
            }
        }


class MIAVamilCode(BaseModel):
    """MIA/Vamil code"""

    code: str = Field(..., description="MIA/Vamil code (e.g., F 1200)")
    title: str = Field(..., description="Code title")
    description: str = Field(..., description="Detailed description")
    category: str = Field(..., description="Category letter")
    chapter: str = Field(..., description="Chapter name")

    # MIA and Vamil percentages
    mia_percentage: Optional[int] = Field(None, description="MIA percentage (13, 27, 36, or 45)")
    vamil_percentage: Optional[int] = Field(None, description="Vamil percentage (usually 75)")

    page: Optional[int] = Field(None, description="Page number in source PDF")

    class Config:
        json_schema_extra = {
            "example": {
                "code": "F 1200",
                "title": "Nieuwe en innovatieve grondstofbesparende productieapparatuur",
                "description": "Zie paragraaf 2b...",
                "category": "F",
                "chapter": "1. Grondstoffen- en watergebruik",
                "mia_percentage": 45,
                "vamil_percentage": 75,
                "page": 24
            }
        }


# ============================================================================
# MATCH RESULT MODELS (Output)
# ============================================================================

class SubsidyCalculation(BaseModel):
    """Calculated subsidy amount"""

    scheme: SubsidyScheme = Field(..., description="Subsidy scheme")
    code: str = Field(..., description="Subsidy code/meldcode")
    title: str = Field(..., description="Subsidy title")

    # Calculation details
    investment_amount: float = Field(..., ge=0, description="Investment amount used for calculation")
    subsidy_amount: float = Field(..., ge=0, description="Calculated subsidy amount in EUR")
    percentage: Optional[float] = Field(None, description="Percentage used (if applicable)")

    # Rules applied
    rules_applied: List[str] = Field(default_factory=list, description="Calculation rules applied")
    warnings: List[str] = Field(default_factory=list, description="Warnings or limitations")

    class Config:
        json_schema_extra = {
            "example": {
                "scheme": "EIA",
                "code": "211102",
                "title": "Warmtepompboiler",
                "investment_amount": 12000.0,
                "subsidy_amount": 4800.0,
                "percentage": 0.40,
                "rules_applied": ["40% investment deduction"],
                "warnings": []
            }
        }


class EquipmentMatch(BaseModel):
    """Match result for a single equipment item"""

    equipment: Equipment = Field(..., description="The equipment item")

    # All matching subsidies
    eia_matches: List[SubsidyCalculation] = Field(default_factory=list, description="EIA matches")
    isde_matches: List[SubsidyCalculation] = Field(default_factory=list, description="ISDE matches")
    mia_matches: List[SubsidyCalculation] = Field(default_factory=list, description="MIA matches")
    vamil_matches: List[SubsidyCalculation] = Field(default_factory=list, description="Vamil matches")

    # Best combination
    best_combination: List[SubsidyCalculation] = Field(default_factory=list, description="Best subsidy combination")
    total_subsidy: float = Field(0.0, ge=0, description="Total subsidy amount")
    subsidy_percentage_of_cost: float = Field(0.0, ge=0, le=100, description="Subsidy as % of cost")

    # Match quality
    confidence: float = Field(..., ge=0, le=1, description="Match confidence (0-1)")
    match_notes: List[str] = Field(default_factory=list, description="Match notes and explanations")

    class Config:
        json_schema_extra = {
            "example": {
                "equipment": {},
                "eia_matches": [],
                "isde_matches": [],
                "best_combination": [],
                "total_subsidy": 8600.0,
                "subsidy_percentage_of_cost": 71.67,
                "confidence": 0.95,
                "match_notes": ["Exact ISDE model match", "EIA code matches category"]
            }
        }


class ArbitrageOpportunity(BaseModel):
    """Alternative equipment with better subsidy outcome"""

    original_equipment: Equipment = Field(..., description="Original equipment from quote")
    alternative_equipment: Dict[str, Any] = Field(..., description="Alternative equipment details")

    # Cost comparison
    original_cost: float = Field(..., ge=0, description="Original equipment cost")
    alternative_cost: float = Field(..., ge=0, description="Alternative equipment cost")
    cost_delta: float = Field(..., description="Cost difference (alternative - original)")

    # Subsidy comparison
    original_subsidy: float = Field(..., ge=0, description="Original subsidy amount")
    alternative_subsidy: float = Field(..., ge=0, description="Alternative subsidy amount")
    subsidy_delta: float = Field(..., description="Subsidy difference (alternative - original)")

    # Net benefit
    net_benefit: float = Field(..., description="Net benefit (subsidy_delta - cost_delta)")
    roi_improvement: float = Field(..., description="ROI improvement in %")

    # Explanation
    recommendation: str = Field(..., description="Recommendation text")
    details: List[str] = Field(default_factory=list, description="Detailed explanation")

    class Config:
        json_schema_extra = {
            "example": {
                "original_equipment": {},
                "alternative_equipment": {
                    "brand": "Daikin",
                    "model": "Altherma 3H 18kW"
                },
                "original_cost": 12000.0,
                "alternative_cost": 13500.0,
                "cost_delta": 1500.0,
                "original_subsidy": 8600.0,
                "alternative_subsidy": 9600.0,
                "subsidy_delta": 1000.0,
                "net_benefit": -500.0,
                "roi_improvement": -4.17,
                "recommendation": "Upgrade not recommended - net cost increases",
                "details": []
            }
        }


class QuoteAnalysis(BaseModel):
    """Complete analysis of a quote with subsidy matching"""

    # Input
    quote: Quote = Field(..., description="The analyzed quote")

    # Equipment matches
    equipment_matches: List[EquipmentMatch] = Field(..., description="Match results per equipment")

    # Totals
    total_investment: float = Field(..., ge=0, description="Total investment amount")
    total_subsidies: float = Field(..., ge=0, description="Total subsidy amount")
    net_cost_after_subsidies: float = Field(..., ge=0, description="Net cost after subsidies")
    subsidy_coverage_percentage: float = Field(..., ge=0, le=100, description="Subsidies as % of investment")

    # Breakdown by scheme
    eia_total: float = Field(0.0, ge=0, description="Total EIA subsidies")
    isde_total: float = Field(0.0, ge=0, description="Total ISDE subsidies")
    mia_total: float = Field(0.0, ge=0, description="Total MIA subsidies")
    vamil_total: float = Field(0.0, ge=0, description="Total Vamil subsidies")

    # Arbitrage opportunities
    arbitrage_opportunities: List[ArbitrageOpportunity] = Field(
        default_factory=list,
        description="Alternative equipment suggestions"
    )

    # Metadata
    analysis_timestamp: datetime = Field(default_factory=datetime.now, description="Analysis timestamp")
    processing_time_seconds: Optional[float] = Field(None, description="Processing time")

    # Summary
    summary: str = Field(..., description="Human-readable summary")
    recommendations: List[str] = Field(default_factory=list, description="Action recommendations")

    class Config:
        json_schema_extra = {
            "example": {
                "quote": {},
                "equipment_matches": [],
                "total_investment": 24500.0,
                "total_subsidies": 22200.0,
                "net_cost_after_subsidies": 2300.0,
                "subsidy_coverage_percentage": 90.61,
                "eia_total": 9800.0,
                "isde_total": 12400.0,
                "summary": "Found subsidies covering 90.6% of investment cost",
                "recommendations": ["Apply for EIA within 3 months", "Apply for ISDE before installation"]
            }
        }


# ============================================================================
# API REQUEST/RESPONSE MODELS
# ============================================================================

class QuoteUploadRequest(BaseModel):
    """Request to analyze a quote PDF"""

    # Will be handled as file upload in FastAPI, but including for documentation
    pdf_base64: Optional[str] = Field(None, description="PDF file as base64 string")

    # Optional parameters
    customer_email: Optional[str] = Field(None, description="Customer email for report")
    include_arbitrage: bool = Field(True, description="Include arbitrage analysis")
    max_arbitrage_options: int = Field(5, ge=1, le=10, description="Max arbitrage options per item")


class QuoteAnalysisResponse(BaseModel):
    """Response from quote analysis API"""

    success: bool = Field(..., description="Whether analysis succeeded")
    analysis: Optional[QuoteAnalysis] = Field(None, description="Analysis results")
    error: Optional[str] = Field(None, description="Error message if failed")

    # Processing info
    processing_time_ms: float = Field(..., description="Processing time in milliseconds")
    api_calls_made: int = Field(..., description="Number of API calls to Claude")
    cost_eur: Optional[float] = Field(None, description="Estimated cost in EUR")


class HealthCheckResponse(BaseModel):
    """Health check response"""

    status: str = Field(..., description="Service status")
    version: str = Field(..., description="API version")
    database_loaded: bool = Field(..., description="Whether subsidy database is loaded")
    database_stats: Dict[str, int] = Field(..., description="Database entry counts")
    timestamp: datetime = Field(default_factory=datetime.now, description="Check timestamp")
