"""Singapore HSA (Health Sciences Authority) collector.

Fetches drug registration data from Singapore HSA via data.gov.sg API.
"""

import json
from pathlib import Path
from typing import Any

import httpx

from .base import BaseCollector, CollectorResult


class SGHSACollector(BaseCollector):
    """Collector for Singapore HSA drug registration data.

    Uses the data.gov.sg API to search for registered drugs.
    API: https://data.gov.sg/datasets/d_767279312753558cbf19d48344577084

    Provides:
    - Drug registration status
    - Active ingredients
    - Dosage form
    - Manufacturer information
    - ATC classification
    - License holder
    """

    source_name = "sghsa"
    API_URL = "https://data.gov.sg/api/action/datastore_search"
    RESOURCE_ID = "d_767279312753558cbf19d48344577084"

    def __init__(
        self,
        cache_dir: str | Path | None = None,
        max_results: int = 50,
    ):
        """Initialize the Singapore HSA collector.

        Args:
            cache_dir: Directory for caching fetched data
            max_results: Maximum number of results per query
        """
        base_dir = Path(__file__).parent.parent.parent.parent / "data"

        if cache_dir is None:
            self.cache_dir = base_dir / "external" / "sghsa_cache"
        else:
            self.cache_dir = Path(cache_dir)

        self.max_results = max_results
        self._local_data: list[dict] | None = None
        self._local_data_path = base_dir / "raw" / "sg_hsa_drugs.json"

    def _load_local_data(self) -> list[dict]:
        """Load local HSA drug data if available."""
        if self._local_data is not None:
            return self._local_data

        self._local_data = []
        if self._local_data_path.exists():
            with open(self._local_data_path, "r", encoding="utf-8") as f:
                self._local_data = json.load(f)

        return self._local_data

    def _search_local(self, drug: str) -> list[dict]:
        """Search for drug in local data.

        Args:
            drug: Drug name or ingredient to search

        Returns:
            List of matching drug records
        """
        data = self._load_local_data()
        drug_lower = drug.lower()
        results = []

        for record in data:
            # Search in product name
            product_name = record.get("product_name", "").lower()
            # Search in active ingredients
            ingredients = record.get("active_ingredients", "").lower()

            if drug_lower in product_name or drug_lower in ingredients:
                results.append(record)

        return results[: self.max_results]

    def _search_api(self, drug: str) -> list[dict]:
        """Search for drug via data.gov.sg API.

        Args:
            drug: Drug name or ingredient to search

        Returns:
            List of matching drug records
        """
        params = {
            "resource_id": self.RESOURCE_ID,
            "q": drug,
            "limit": self.max_results,
        }

        try:
            with httpx.Client(timeout=30.0) as client:
                response = client.get(self.API_URL, params=params)
                response.raise_for_status()
                data = response.json()

                if data.get("success"):
                    return data.get("result", {}).get("records", [])
                return []

        except httpx.HTTPError as e:
            print(f"Error fetching HSA data: {e}")
            return []

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        """Search for HSA registration data for a drug.

        Args:
            drug: Drug name (product name or ingredient)
            disease: Ignored for HSA lookup (no indication data available)

        Returns:
            CollectorResult with HSA registration data
        """
        query = {"drug": drug, "disease": disease}

        # First try local data
        results = self._search_local(drug)

        # If no local results, try API
        if not results:
            results = self._search_api(drug)

        if not results:
            return self._make_result(
                query=query,
                data={
                    "found": False,
                    "count": 0,
                    "records": [],
                    "message": f"No HSA registration found for '{drug}'",
                },
                success=True,
            )

        # Parse and normalize results
        parsed_results = []
        for record in results:
            parsed = self._parse_record(record)
            parsed_results.append(parsed)

        return self._make_result(
            query=query,
            data={
                "found": True,
                "count": len(parsed_results),
                "records": parsed_results,
                "source": "Singapore HSA (data.gov.sg)",
            },
            success=True,
        )

    def _parse_record(self, record: dict) -> dict:
        """Parse and normalize an HSA record.

        Args:
            record: Raw HSA record

        Returns:
            Normalized record dictionary
        """
        return {
            "license_no": record.get("licence_no", ""),
            "product_name": record.get("product_name", ""),
            "active_ingredients": record.get("active_ingredients", ""),
            "strength": record.get("strength", ""),
            "dosage_form": record.get("dosage_form", ""),
            "route_of_administration": record.get("route_of_administration", ""),
            "atc_code": record.get("atc_code", ""),
            "manufacturer": record.get("manufacturer", ""),
            "country_of_manufacturer": record.get("country_of_manufacturer", ""),
            "license_holder": record.get("license_holder", ""),
            "forensic_classification": record.get("forensic_classification", ""),
            "approval_date": record.get("approval_d", ""),
            "registry": "Singapore HSA",
            "url": f"https://eservice.hsa.gov.sg/prism/common/enquirepublic/SearchDRBProduct.do?action=load",
        }

    def get_by_license(self, license_no: str) -> dict | None:
        """Get drug record by HSA license number.

        Args:
            license_no: HSA license number (e.g., "SIN00001P")

        Returns:
            Drug record or None if not found
        """
        data = self._load_local_data()

        for record in data:
            if record.get("licence_no") == license_no:
                return self._parse_record(record)

        return None

    def get_by_atc(self, atc_code: str) -> list[dict]:
        """Get all drugs with a specific ATC code.

        Args:
            atc_code: ATC code or prefix (e.g., "C09" for RAAS drugs)

        Returns:
            List of matching drug records
        """
        data = self._load_local_data()
        atc_upper = atc_code.upper()
        results = []

        for record in data:
            record_atc = record.get("atc_code", "").upper()
            if record_atc.startswith(atc_upper):
                results.append(self._parse_record(record))

        return results

    def get_statistics(self) -> dict:
        """Get statistics about HSA drug data.

        Returns:
            Dictionary with data statistics
        """
        data = self._load_local_data()

        if not data:
            return {"error": "No local data available"}

        # Count by ATC category
        atc_counts = {}
        for record in data:
            atc = record.get("atc_code", "")
            if atc and isinstance(atc, str) and len(atc) > 0:
                category = atc[0]
                atc_counts[category] = atc_counts.get(category, 0) + 1

        # Count by forensic classification
        forensic_counts = {}
        for record in data:
            fc = record.get("forensic_classification", "Unknown")
            forensic_counts[fc] = forensic_counts.get(fc, 0) + 1

        return {
            "total_products": len(data),
            "by_atc_category": atc_counts,
            "by_forensic_classification": forensic_counts,
            "source": "Singapore HSA (data.gov.sg)",
        }
