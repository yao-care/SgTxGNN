#!/usr/bin/env python3
"""Generate news monitoring keywords from prediction results.

Creates a keywords.json file for news monitoring based on:
1. Drug names from repurposing candidates
2. Disease/indication names
3. Synonyms from synonyms.json

Usage:
    uv run python scripts/generate_news_keywords.py

Output:
    data/news/keywords.json
"""

import json
from pathlib import Path
from collections import defaultdict

import pandas as pd


def load_synonyms(synonyms_path: Path) -> dict:
    """Load synonyms from JSON file."""
    if not synonyms_path.exists():
        return {"indication_synonyms": {}, "drug_synonyms": {}}

    with open(synonyms_path, "r", encoding="utf-8") as f:
        return json.load(f)


def extract_keywords_from_candidates(candidates_path: Path) -> tuple[set, set]:
    """Extract unique drugs and indications from candidates.

    Returns:
        Tuple of (drug_names, indication_names)
    """
    if not candidates_path.exists():
        print(f"Warning: {candidates_path} not found")
        return set(), set()

    df = pd.read_csv(candidates_path)

    # Extract unique drug names (ingredients)
    drugs = set()
    if "ingredient" in df.columns:
        drugs = set(df["ingredient"].dropna().unique())

    # Extract unique indications
    indications = set()
    if "potential_indication" in df.columns:
        indications = set(df["potential_indication"].dropna().unique())

    return drugs, indications


def generate_drug_patterns(drugs: set, synonyms: dict) -> list[dict]:
    """Generate keyword patterns for drugs.

    Args:
        drugs: Set of drug names
        synonyms: Synonym dictionary

    Returns:
        List of keyword pattern dictionaries
    """
    drug_synonyms = synonyms.get("drug_synonyms", {})
    patterns = []

    for drug in sorted(drugs):
        drug_lower = drug.lower()

        # Get synonyms for this drug
        drug_syns = drug_synonyms.get(drug_lower, [])

        # Create pattern with drug name and synonyms
        all_terms = [drug] + drug_syns

        pattern = {
            "category": "drug",
            "primary_term": drug,
            "search_terms": all_terms,
            "exclude_terms": ["stock", "shares", "market", "investor"],
        }
        patterns.append(pattern)

    return patterns


def generate_indication_patterns(indications: set, synonyms: dict) -> list[dict]:
    """Generate keyword patterns for indications.

    Args:
        indications: Set of indication names
        synonyms: Synonym dictionary

    Returns:
        List of keyword pattern dictionaries
    """
    indication_synonyms = synonyms.get("indication_synonyms", {})
    patterns = []

    for indication in sorted(indications):
        indication_lower = indication.lower()

        # Get synonyms for this indication
        ind_syns = indication_synonyms.get(indication_lower, [])

        # Create pattern
        all_terms = [indication] + ind_syns

        pattern = {
            "category": "indication",
            "primary_term": indication,
            "search_terms": all_terms,
            "exclude_terms": [],
        }
        patterns.append(pattern)

    return patterns


def generate_combination_patterns(
    drugs: set, indications: set, synonyms: dict, top_n: int = 100
) -> list[dict]:
    """Generate drug-indication combination patterns.

    Focuses on high-interest combinations for news monitoring.

    Args:
        drugs: Set of drug names
        indications: Set of indication names
        synonyms: Synonym dictionary
        top_n: Number of top combinations to include

    Returns:
        List of combination pattern dictionaries
    """
    drug_synonyms = synonyms.get("drug_synonyms", {})
    indication_synonyms = synonyms.get("indication_synonyms", {})

    # Priority indications (common in news)
    priority_indications = {
        "cancer",
        "diabetes",
        "alzheimer",
        "parkinson",
        "heart disease",
        "stroke",
        "covid",
        "obesity",
        "depression",
        "asthma",
    }

    patterns = []

    # Generate patterns for priority indication combinations
    for indication in indications:
        ind_lower = indication.lower()

        # Check if this is a priority indication
        is_priority = any(p in ind_lower for p in priority_indications)
        if not is_priority:
            continue

        ind_syns = indication_synonyms.get(ind_lower, [])

        for drug in drugs:
            drug_lower = drug.lower()
            drug_syns = drug_synonyms.get(drug_lower, [])

            pattern = {
                "category": "drug_indication",
                "drug": drug,
                "indication": indication,
                "search_terms": {
                    "drug_terms": [drug] + drug_syns[:2],
                    "indication_terms": [indication] + ind_syns[:2],
                },
                "query_template": '("{drug_term}") AND ("{indication_term}")',
            }
            patterns.append(pattern)

            if len(patterns) >= top_n:
                break

        if len(patterns) >= top_n:
            break

    return patterns


def main():
    print("=" * 60)
    print("Generating News Keywords - SgTxGNN")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / "data"
    news_dir = data_dir / "news"

    # Ensure output directory exists
    news_dir.mkdir(parents=True, exist_ok=True)

    # Load synonyms
    print("1. Loading synonyms...")
    synonyms_path = news_dir / "synonyms.json"
    synonyms = load_synonyms(synonyms_path)
    print(f"   Loaded {len(synonyms.get('drug_synonyms', {}))} drug synonym entries")
    print(
        f"   Loaded {len(synonyms.get('indication_synonyms', {}))} indication synonym entries"
    )

    # Extract from candidates
    print("2. Extracting from repurposing candidates...")
    candidates_path = data_dir / "processed" / "repurposing_candidates.csv"
    drugs, indications = extract_keywords_from_candidates(candidates_path)
    print(f"   Found {len(drugs)} unique drugs")
    print(f"   Found {len(indications)} unique indications")

    # Add indications from synonyms.json (common health terms)
    print("   Adding common health terms from synonyms...")
    for ind_name in synonyms.get("indication_synonyms", {}).keys():
        indications.add(ind_name)
    print(f"   Total indications after adding synonyms: {len(indications)}")

    # Generate patterns
    print("3. Generating keyword patterns...")

    drug_patterns = generate_drug_patterns(drugs, synonyms)
    print(f"   Generated {len(drug_patterns)} drug patterns")

    indication_patterns = generate_indication_patterns(indications, synonyms)
    print(f"   Generated {len(indication_patterns)} indication patterns")

    combination_patterns = generate_combination_patterns(drugs, indications, synonyms)
    print(f"   Generated {len(combination_patterns)} combination patterns")

    # Build output structure
    keywords = {
        "description": "News monitoring keywords for SgTxGNN drug repurposing",
        "generated": pd.Timestamp.now().isoformat(),
        "statistics": {
            "total_drugs": len(drugs),
            "total_indications": len(indications),
            "drug_patterns": len(drug_patterns),
            "indication_patterns": len(indication_patterns),
            "combination_patterns": len(combination_patterns),
        },
        "news_sources": [
            {
                "name": "CNA Health",
                "url": "https://www.channelnewsasia.com/singapore/health",
                "region": "SG",
            },
            {
                "name": "Straits Times Health",
                "url": "https://www.straitstimes.com/singapore/health",
                "region": "SG",
            },
            {
                "name": "Today Health",
                "url": "https://www.todayonline.com/singapore/health",
                "region": "SG",
            },
            {
                "name": "Medical News Today",
                "url": "https://www.medicalnewstoday.com/",
                "region": "global",
            },
            {
                "name": "Reuters Health",
                "url": "https://www.reuters.com/business/healthcare-pharmaceuticals/",
                "region": "global",
            },
        ],
        "patterns": {
            "drugs": drug_patterns[:100],  # Limit for manageability
            "indications": indication_patterns,  # Include all for news matching
            "combinations": combination_patterns,
        },
        "global_exclude_terms": [
            "stock price",
            "shares",
            "investor",
            "quarterly earnings",
            "IPO",
            "merger",
            "acquisition",
        ],
    }

    # Write output
    output_path = news_dir / "keywords.json"
    print(f"4. Writing to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(keywords, f, indent=2, ensure_ascii=False)

    print()
    print("=" * 60)
    print("News Keywords Generation Complete!")
    print("=" * 60)
    print(f"  Drug patterns: {len(drug_patterns[:50])}")
    print(f"  Indication patterns: {len(indication_patterns[:50])}")
    print(f"  Combination patterns: {len(combination_patterns)}")
    print(f"  Output: {output_path}")


if __name__ == "__main__":
    main()
