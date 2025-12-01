import json
from pathlib import Path
from typing import List, Dict, Any
from anthropic import Anthropic
from models.schemas import (
    SubsidyMatchRequest,
    SubsidyMatchResponse,
    SubsidyMatch,
    SubsidyRule,
    MatchScore,
    CompanySize
)


class SubsidyMatcher:
    """Service for matching companies/projects with eligible subsidies"""

    def __init__(self, api_key: str, subsidies_path: str = "data/subsidies"):
        """
        Initialize subsidy matcher

        Args:
            api_key: Anthropic API key
            subsidies_path: Path to subsidies data directory
        """
        self.client = Anthropic(api_key=api_key)
        self.subsidies_path = Path(subsidies_path)
        self.subsidies: List[SubsidyRule] = []
        self._load_subsidies()

    def _load_subsidies(self):
        """Load subsidy rules from JSON files"""
        if not self.subsidies_path.exists():
            self.subsidies_path.mkdir(parents=True, exist_ok=True)
            return

        for json_file in self.subsidies_path.glob("*.json"):
            try:
                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            self.subsidies.append(SubsidyRule(**item))
                    else:
                        self.subsidies.append(SubsidyRule(**data))
            except Exception as e:
                print(f"Error loading {json_file}: {e}")

    async def match_subsidies(
        self,
        request: SubsidyMatchRequest
    ) -> SubsidyMatchResponse:
        """
        Match company and project with eligible subsidies

        Args:
            request: Subsidy match request

        Returns:
            SubsidyMatchResponse with matching subsidies
        """
        matches: List[SubsidyMatch] = []

        for subsidy in self.subsidies:
            match_result = self._evaluate_match(request, subsidy)
            if match_result:
                matches.append(match_result)

        # Sort by match score descending
        matches.sort(key=lambda x: x.match_score.score, reverse=True)

        return SubsidyMatchResponse(
            matches=matches,
            total_matches=len(matches)
        )

    def _evaluate_match(
        self,
        request: SubsidyMatchRequest,
        subsidy: SubsidyRule
    ) -> SubsidyMatch | None:
        """
        Evaluate if a subsidy matches the request

        Args:
            request: Subsidy match request
            subsidy: Subsidy rule to evaluate

        Returns:
            SubsidyMatch if eligible, None otherwise
        """
        score = 0.0
        max_score = 100.0
        reasons = []
        missing_requirements = []
        eligible = True

        # Check company size eligibility (20 points)
        if request.company.size in subsidy.eligible_company_sizes:
            score += 20
            reasons.append(f"Company size ({request.company.size}) is eligible")
        else:
            eligible = False
            missing_requirements.append(
                f"Company size must be one of: {', '.join(subsidy.eligible_company_sizes)}"
            )

        # Check category match (30 points)
        if request.project.category == subsidy.category:
            score += 30
            reasons.append(f"Project category matches ({subsidy.category})")
        else:
            score += 10
            reasons.append("Project category doesn't perfectly match")

        # Check budget constraints (20 points)
        if subsidy.min_budget and request.project.budget < subsidy.min_budget:
            eligible = False
            missing_requirements.append(
                f"Project budget must be at least €{subsidy.min_budget:,.2f}"
            )
        elif subsidy.max_budget and request.project.budget > subsidy.max_budget:
            eligible = False
            missing_requirements.append(
                f"Project budget must not exceed €{subsidy.max_budget:,.2f}"
            )
        else:
            score += 20
            reasons.append("Project budget meets requirements")

        # Check industry eligibility (15 points)
        if subsidy.eligible_industries:
            if request.company.industry in subsidy.eligible_industries:
                score += 15
                reasons.append("Company industry is eligible")
            else:
                score += 5
                reasons.append("Company industry may not be primary target")
        else:
            score += 15
            reasons.append("No industry restrictions")

        # Check region eligibility (15 points)
        if subsidy.regions:
            if any(region.lower() in request.company.location.lower()
                   for region in subsidy.regions):
                score += 15
                reasons.append("Company location is eligible")
            else:
                eligible = False
                missing_requirements.append(
                    f"Company must be located in: {', '.join(subsidy.regions)}"
                )
        else:
            score += 15
            reasons.append("No regional restrictions")

        # Calculate confidence based on data completeness
        confidence = self._calculate_confidence(request)

        match_score = MatchScore(
            score=min(score, max_score),
            confidence=confidence,
            reasons=reasons
        )

        return SubsidyMatch(
            subsidy=subsidy,
            match_score=match_score,
            eligible=eligible,
            missing_requirements=missing_requirements
        )

    def _calculate_confidence(self, request: SubsidyMatchRequest) -> float:
        """
        Calculate confidence level based on data completeness

        Args:
            request: Subsidy match request

        Returns:
            Confidence score between 0 and 1
        """
        total_fields = 0
        filled_fields = 0

        # Check company info completeness
        company_fields = [
            request.company.name,
            request.company.kvk_number,
            request.company.size,
            request.company.industry,
            request.company.location
        ]
        total_fields += len(company_fields)
        filled_fields += sum(1 for f in company_fields if f)

        # Check project info completeness
        project_fields = [
            request.project.title,
            request.project.description,
            request.project.category,
            request.project.budget > 0,
            request.project.duration_months > 0
        ]
        total_fields += len(project_fields)
        filled_fields += sum(1 for f in project_fields if f)

        return filled_fields / total_fields if total_fields > 0 else 0.0

    async def analyze_with_claude(
        self,
        request: SubsidyMatchRequest,
        matches: List[SubsidyMatch]
    ) -> Dict[str, Any]:
        """
        Use Claude to provide additional analysis and recommendations

        Args:
            request: Original match request
            matches: List of subsidy matches

        Returns:
            Dictionary with Claude's analysis
        """
        # Placeholder for Claude-based analysis
        # Would use Claude API to provide deeper insights and recommendations
        return {
            "summary": f"Found {len(matches)} potential subsidies",
            "recommendations": [],
            "next_steps": []
        }
