from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum


class CompanySize(str, Enum):
    """Company size categories"""
    MICRO = "micro"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class SubsidyCategory(str, Enum):
    """Subsidy categories"""
    INNOVATION = "innovation"
    SUSTAINABILITY = "sustainability"
    INTERNATIONALIZATION = "internationalization"
    DIGITALIZATION = "digitalization"
    TRAINING = "training"
    OTHER = "other"


class CompanyInfo(BaseModel):
    """Company information for subsidy matching"""
    name: str = Field(..., description="Company name")
    kvk_number: Optional[str] = Field(None, description="KVK registration number")
    size: CompanySize = Field(..., description="Company size")
    industry: str = Field(..., description="Industry sector")
    employees: int = Field(..., ge=0, description="Number of employees")
    annual_revenue: Optional[float] = Field(None, ge=0, description="Annual revenue in EUR")
    location: str = Field(..., description="Company location (city or province)")


class ProjectInfo(BaseModel):
    """Project information for subsidy matching"""
    title: str = Field(..., description="Project title")
    description: str = Field(..., description="Project description")
    category: SubsidyCategory = Field(..., description="Project category")
    budget: float = Field(..., ge=0, description="Project budget in EUR")
    start_date: Optional[datetime] = Field(None, description="Planned start date")
    duration_months: int = Field(..., ge=1, description="Project duration in months")


class SubsidyMatchRequest(BaseModel):
    """Request for subsidy matching"""
    company: CompanyInfo
    project: ProjectInfo
    additional_info: Optional[Dict[str, Any]] = Field(None, description="Additional information")


class SubsidyRule(BaseModel):
    """Subsidy rule definition"""
    id: str = Field(..., description="Unique subsidy identifier")
    name: str = Field(..., description="Subsidy name")
    description: str = Field(..., description="Subsidy description")
    category: SubsidyCategory
    provider: str = Field(..., description="Subsidy provider organization")
    min_budget: Optional[float] = Field(None, description="Minimum project budget")
    max_budget: Optional[float] = Field(None, description="Maximum project budget")
    eligible_company_sizes: List[CompanySize] = Field(..., description="Eligible company sizes")
    eligible_industries: Optional[List[str]] = Field(None, description="Eligible industries")
    regions: Optional[List[str]] = Field(None, description="Eligible regions")
    requirements: List[str] = Field(..., description="Eligibility requirements")
    url: Optional[str] = Field(None, description="More information URL")


class MatchScore(BaseModel):
    """Match score for a subsidy"""
    score: float = Field(..., ge=0, le=100, description="Match score (0-100)")
    confidence: float = Field(..., ge=0, le=1, description="Confidence level (0-1)")
    reasons: List[str] = Field(..., description="Reasons for the score")


class SubsidyMatch(BaseModel):
    """Subsidy match result"""
    subsidy: SubsidyRule
    match_score: MatchScore
    eligible: bool = Field(..., description="Whether company is eligible")
    missing_requirements: List[str] = Field(default_factory=list, description="Missing requirements")


class SubsidyMatchResponse(BaseModel):
    """Response from subsidy matching"""
    matches: List[SubsidyMatch] = Field(..., description="Matching subsidies")
    total_matches: int = Field(..., description="Total number of matches")
    analysis_timestamp: datetime = Field(default_factory=datetime.now, description="Analysis timestamp")


class DocumentAnalysisRequest(BaseModel):
    """Request for document analysis"""
    document_text: str = Field(..., description="Document text to analyze")
    analysis_type: str = Field(default="general", description="Type of analysis to perform")


class DocumentAnalysisResponse(BaseModel):
    """Response from document analysis"""
    extracted_info: Dict[str, Any] = Field(..., description="Extracted information")
    company_info: Optional[CompanyInfo] = Field(None, description="Extracted company information")
    project_info: Optional[ProjectInfo] = Field(None, description="Extracted project information")
    confidence: float = Field(..., ge=0, le=1, description="Extraction confidence")


class HealthCheckResponse(BaseModel):
    """Health check response"""
    status: str
    service: str
    version: str
