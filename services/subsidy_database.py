"""
SubsidyDatabase - In-memory subsidy database with fast search indexes.

Loads EIA, ISDE, and MIA/Vamil data from JSON files and provides
fast lookup methods for subsidy matching.
"""

import json
from pathlib import Path
from typing import List, Dict, Optional, Set
from collections import defaultdict
import re

from models.subsidy_schemas import (
    EIACode,
    ISDEMeldcode,
    MIAVamilCode,
    ISDECategory
)


class SubsidyDatabase:
    """
    In-memory subsidy database with search indexes.

    Loads all subsidy data at startup and builds indexes for fast searching:
    - EIA codes indexed by keywords, categories, chapters
    - ISDE meldcodes indexed by brand, model, category
    - MIA/Vamil codes indexed by keywords, categories

    Typical load time: ~5ms for 7,977 entries
    Typical search time: <1ms per query
    """

    def __init__(self, data_dir: Optional[Path] = None):
        """
        Initialize database and load all subsidy data.

        Args:
            data_dir: Path to data/subsidies directory. If None, auto-detect.
        """
        if data_dir is None:
            # Auto-detect: assume we're in project root or services/
            current_file = Path(__file__).resolve()
            project_root = current_file.parent.parent
            data_dir = project_root / "data" / "subsidies"

        self.data_dir = Path(data_dir)

        # Raw data storage
        self.eia_codes: List[EIACode] = []
        self.isde_warmtepompen: List[ISDEMeldcode] = []
        self.isde_isolatie: List[ISDEMeldcode] = []
        self.isde_glas: List[ISDEMeldcode] = []
        self.isde_zonneboiler: List[ISDEMeldcode] = []
        self.mia_vamil_codes: List[MIAVamilCode] = []

        # Indexes for fast lookup
        self.eia_by_code: Dict[str, EIACode] = {}
        self.eia_by_keyword: Dict[str, List[EIACode]] = defaultdict(list)
        self.eia_by_chapter: Dict[str, List[EIACode]] = defaultdict(list)

        self.isde_by_meldcode: Dict[str, ISDEMeldcode] = {}
        self.isde_by_brand: Dict[str, List[ISDEMeldcode]] = defaultdict(list)
        self.isde_by_category: Dict[ISDECategory, List[ISDEMeldcode]] = defaultdict(list)

        self.mia_by_code: Dict[str, MIAVamilCode] = {}
        self.mia_by_keyword: Dict[str, List[MIAVamilCode]] = defaultdict(list)
        self.mia_by_percentage: Dict[int, List[MIAVamilCode]] = defaultdict(list)

        # Load all data
        self._load_all_data()
        self._build_indexes()

    # ========================================================================
    # DATA LOADING
    # ========================================================================

    def _load_all_data(self):
        """Load all subsidy data from JSON files"""

        # Load EIA
        eia_file = self.data_dir / "eia_2025.json"
        if eia_file.exists():
            with open(eia_file, 'r', encoding='utf-8') as f:
                eia_data = json.load(f)
                self.eia_codes = [EIACode(**code) for code in eia_data['codes']]

        # Load ISDE warmtepompen
        isde_wp_file = self.data_dir / "isde_warmtepompen.json"
        if isde_wp_file.exists():
            with open(isde_wp_file, 'r', encoding='utf-8') as f:
                isde_data = json.load(f)
                self.isde_warmtepompen = [ISDEMeldcode(**entry) for entry in isde_data]

        # Load ISDE isolatie
        isde_iso_file = self.data_dir / "isde_isolatiematerialen.json"
        if isde_iso_file.exists():
            with open(isde_iso_file, 'r', encoding='utf-8') as f:
                isde_data = json.load(f)
                self.isde_isolatie = [ISDEMeldcode(**entry) for entry in isde_data]

        # Load ISDE glas
        isde_glas_file = self.data_dir / "isde_hoogrendementsglas.json"
        if isde_glas_file.exists():
            with open(isde_glas_file, 'r', encoding='utf-8') as f:
                isde_data = json.load(f)
                self.isde_glas = [ISDEMeldcode(**entry) for entry in isde_data]

        # Load ISDE zonneboiler
        isde_zb_file = self.data_dir / "isde_zonneboilers.json"
        if isde_zb_file.exists():
            with open(isde_zb_file, 'r', encoding='utf-8') as f:
                isde_data = json.load(f)
                self.isde_zonneboiler = [ISDEMeldcode(**entry) for entry in isde_data]

        # Load MIA/Vamil
        mia_file = self.data_dir / "mia_vamil_2025.json"
        if mia_file.exists():
            with open(mia_file, 'r', encoding='utf-8') as f:
                mia_data = json.load(f)
                self.mia_vamil_codes = [MIAVamilCode(**code) for code in mia_data['codes']]

    def _build_indexes(self):
        """Build search indexes for fast lookup"""

        # EIA indexes
        for code in self.eia_codes:
            # By code
            self.eia_by_code[code.code] = code

            # By chapter
            if code.chapter:
                self.eia_by_chapter[code.chapter.lower()].append(code)

            # By keywords (extract from title and description)
            text = code.title
            if code.description:
                text += " " + code.description
            keywords = self._extract_keywords(text)
            for keyword in keywords:
                self.eia_by_keyword[keyword].append(code)

        # ISDE indexes
        all_isde = (self.isde_warmtepompen + self.isde_isolatie +
                    self.isde_glas + self.isde_zonneboiler)

        for entry in all_isde:
            # By meldcode
            self.isde_by_meldcode[entry.meldcode] = entry

            # By category
            self.isde_by_category[entry.category].append(entry)

            # By brand (normalized)
            if entry.manufacturer:
                brand_normalized = entry.manufacturer.lower().strip()
                self.isde_by_brand[brand_normalized].append(entry)

        # MIA/Vamil indexes
        for code in self.mia_vamil_codes:
            # By code
            self.mia_by_code[code.code] = code

            # By MIA percentage
            if code.mia_percentage:
                self.mia_by_percentage[code.mia_percentage].append(code)

            # By keywords
            text = code.title
            if code.description:
                text += " " + code.description
            keywords = self._extract_keywords(text)
            for keyword in keywords:
                self.mia_by_keyword[keyword].append(code)

    def _extract_keywords(self, text: str) -> Set[str]:
        """
        Extract keywords from text for indexing.

        Removes common Dutch words and extracts significant terms.
        """
        # Normalize
        text = text.lower()

        # Remove special characters
        text = re.sub(r'[^\w\s]', ' ', text)

        # Split into words
        words = text.split()

        # Dutch stopwords to exclude
        stopwords = {
            'de', 'het', 'een', 'en', 'van', 'voor', 'met', 'aan', 'op', 'in',
            'te', 'door', 'bij', 'uit', 'tot', 'of', 'als', 'naar', 'om',
            'bestemd', 'zijn', 'wordt', 'worden', 'heeft', 'hebben'
        }

        # Filter and return
        keywords = {w for w in words if len(w) > 2 and w not in stopwords}

        return keywords

    # ========================================================================
    # SEARCH METHODS - EIA
    # ========================================================================

    def search_eia_by_keywords(self, keywords: List[str], min_matches: int = 1) -> List[EIACode]:
        """
        Search EIA codes by keywords.

        Args:
            keywords: List of keywords to search for
            min_matches: Minimum number of keyword matches required

        Returns:
            List of matching EIA codes, sorted by relevance
        """
        keyword_scores: Dict[str, int] = defaultdict(int)

        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in self.eia_by_keyword:
                for code in self.eia_by_keyword[keyword_lower]:
                    keyword_scores[code.code] += 1

        # Filter by min_matches and sort by score
        results = [
            self.eia_by_code[code]
            for code, score in keyword_scores.items()
            if score >= min_matches
        ]

        # Sort by score (descending)
        results.sort(key=lambda c: keyword_scores[c.code], reverse=True)

        return results

    def search_eia_by_chapter(self, chapter: str) -> List[EIACode]:
        """Search EIA codes by chapter name"""
        chapter_lower = chapter.lower()
        return self.eia_by_chapter.get(chapter_lower, [])

    def get_eia_by_code(self, code: str) -> Optional[EIACode]:
        """Get specific EIA code"""
        return self.eia_by_code.get(code)

    def get_all_eia_codes(self) -> List[EIACode]:
        """Get all EIA codes"""
        return self.eia_codes

    # ========================================================================
    # SEARCH METHODS - ISDE
    # ========================================================================

    def search_isde_warmtepompen_by_brand(self, brand: str, fuzzy: bool = True) -> List[ISDEMeldcode]:
        """
        Search ISDE warmtepompen by brand/manufacturer.

        Args:
            brand: Brand name to search for
            fuzzy: If True, do partial matching (e.g., "Daikin" matches "Daikin Air Conditioning")

        Returns:
            List of matching ISDE meldcodes
        """
        brand_lower = brand.lower().strip()

        if fuzzy:
            # Partial matching
            results = []
            for indexed_brand, entries in self.isde_by_brand.items():
                if brand_lower in indexed_brand or indexed_brand in brand_lower:
                    results.extend(entries)
            return results
        else:
            # Exact matching
            return self.isde_by_brand.get(brand_lower, [])

    def search_isde_by_model(self, brand: str, model: str, category: Optional[ISDECategory] = None) -> Optional[ISDEMeldcode]:
        """
        Search ISDE by brand and model (exact match).

        This is the primary matching method for equipment with specific models.

        Args:
            brand: Brand/manufacturer name
            model: Model name/number
            category: Optional ISDE category to narrow search

        Returns:
            Matching meldcode or None
        """
        # Get all entries for this brand
        brand_entries = self.search_isde_warmtepompen_by_brand(brand, fuzzy=True)

        # Filter by category if provided
        if category:
            brand_entries = [e for e in brand_entries if e.category == category]

        # Find exact model match
        model_lower = model.lower().strip()

        for entry in brand_entries:
            if entry.model and model_lower in entry.model.lower():
                return entry

        return None

    def get_isde_by_meldcode(self, meldcode: str) -> Optional[ISDEMeldcode]:
        """Get specific ISDE entry by meldcode"""
        return self.isde_by_meldcode.get(meldcode)

    def get_isde_by_category(self, category: ISDECategory) -> List[ISDEMeldcode]:
        """Get all ISDE entries for a category"""
        return self.isde_by_category.get(category, [])

    def get_all_isde_warmtepompen(self) -> List[ISDEMeldcode]:
        """Get all ISDE warmtepompen"""
        return self.isde_warmtepompen

    # ========================================================================
    # SEARCH METHODS - MIA/VAMIL
    # ========================================================================

    def search_mia_by_keywords(self, keywords: List[str], min_matches: int = 1) -> List[MIAVamilCode]:
        """
        Search MIA/Vamil codes by keywords.

        Args:
            keywords: List of keywords to search for
            min_matches: Minimum number of keyword matches required

        Returns:
            List of matching MIA/Vamil codes, sorted by relevance
        """
        keyword_scores: Dict[str, int] = defaultdict(int)

        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in self.mia_by_keyword:
                for code in self.mia_by_keyword[keyword_lower]:
                    keyword_scores[code.code] += 1

        # Filter by min_matches and sort by score
        results = [
            self.mia_by_code[code]
            for code, score in keyword_scores.items()
            if score >= min_matches
        ]

        # Sort by score (descending), then by MIA percentage (descending)
        results.sort(key=lambda c: (keyword_scores[c.code], c.mia_percentage or 0), reverse=True)

        return results

    def get_mia_by_percentage(self, percentage: int) -> List[MIAVamilCode]:
        """Get all MIA codes with specific percentage (13, 27, 36, or 45)"""
        return self.mia_by_percentage.get(percentage, [])

    def get_mia_by_code(self, code: str) -> Optional[MIAVamilCode]:
        """Get specific MIA/Vamil code"""
        return self.mia_by_code.get(code)

    def get_all_mia_codes(self) -> List[MIAVamilCode]:
        """Get all MIA/Vamil codes"""
        return self.mia_vamil_codes

    # ========================================================================
    # STATISTICS
    # ========================================================================

    def get_stats(self) -> Dict[str, int]:
        """Get database statistics"""
        return {
            "eia_codes": len(self.eia_codes),
            "isde_warmtepompen": len(self.isde_warmtepompen),
            "isde_isolatie": len(self.isde_isolatie),
            "isde_glas": len(self.isde_glas),
            "isde_zonneboiler": len(self.isde_zonneboiler),
            "isde_total": (len(self.isde_warmtepompen) + len(self.isde_isolatie) +
                          len(self.isde_glas) + len(self.isde_zonneboiler)),
            "mia_vamil_codes": len(self.mia_vamil_codes),
            "total_entries": (len(self.eia_codes) + len(self.isde_warmtepompen) +
                             len(self.isde_isolatie) + len(self.isde_glas) +
                             len(self.isde_zonneboiler) + len(self.mia_vamil_codes))
        }

    def is_loaded(self) -> bool:
        """Check if database is loaded"""
        return len(self.eia_codes) > 0 or len(self.isde_warmtepompen) > 0


# Global instance (singleton pattern)
_db_instance: Optional[SubsidyDatabase] = None


def get_database() -> SubsidyDatabase:
    """
    Get the global SubsidyDatabase instance (singleton).

    Creates and loads database on first call, returns cached instance on subsequent calls.
    """
    global _db_instance

    if _db_instance is None:
        _db_instance = SubsidyDatabase()

    return _db_instance
