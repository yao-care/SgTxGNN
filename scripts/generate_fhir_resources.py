#!/usr/bin/env python3
"""Generate FHIR R4 resources from unified prediction results.

Usage:
    uv run python scripts/generate_fhir_resources.py

Prerequisites:
    Run both run_kg_prediction.py and run_dl_prediction.py first,
    then merge them into unified_predictions.csv

Output:
    docs/fhir/metadata
    docs/fhir/MedicationKnowledge/*.json
    docs/fhir/ClinicalUseDefinition/*.json
"""

import json
from pathlib import Path
from datetime import datetime

import pandas as pd


# Singapore-specific configuration
BASE_URL = "https://sgtxgnn.yao.care"

JURISDICTION = {
    "coding": [{
        "system": "urn:iso:std:iso:3166",
        "code": "SG",
        "display": "Singapore"
    }]
}

# Evidence level mapping based on prediction source
EVIDENCE_LEVELS = {
    "KG+DL": "L4",  # Both methods agree - higher confidence
    "DL": "L5",     # Deep learning only
    "KG": "L5",     # Knowledge graph only
}


def generate_capability_statement() -> dict:
    """Generate CapabilityStatement (metadata)."""
    return {
        "resourceType": "CapabilityStatement",
        "id": "sgtxgnn-fhir-server",
        "url": f"{BASE_URL}/fhir/metadata",
        "version": "1.0.0",
        "name": "SgTxGNNFHIRServer",
        "title": "Singapore TxGNN FHIR Server",
        "status": "active",
        "experimental": True,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "publisher": "Yao.Care - SgTxGNN Project",
        "description": "FHIR R4 API for Singapore drug repurposing predictions based on TxGNN knowledge graph",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {
                    "type": "MedicationKnowledge",
                    "profile": "http://hl7.org/fhir/StructureDefinition/MedicationKnowledge",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "code", "type": "token"},
                        {"name": "status", "type": "token"}
                    ]
                },
                {
                    "type": "ClinicalUseDefinition",
                    "profile": "http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition",
                    "interaction": [{"code": "read"}, {"code": "search-type"}],
                    "searchParam": [
                        {"name": "type", "type": "token"},
                        {"name": "subject", "type": "reference"}
                    ]
                }
            ]
        }]
    }


def generate_medication_knowledge(
    drug_name: str,
    drugbank_id: str,
    brand_name: str,
    license_id: str
) -> dict:
    """Generate MedicationKnowledge resource."""
    slug = drugbank_id.lower()
    return {
        "resourceType": "MedicationKnowledge",
        "id": slug,
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/MedicationKnowledge"]
        },
        "status": "active",
        "code": {
            "coding": [
                {
                    "system": "https://go.drugbank.com/drugs",
                    "code": drugbank_id,
                    "display": drug_name
                }
            ],
            "text": drug_name
        },
        "synonym": [brand_name] if brand_name != drug_name else [],
        "intendedJurisdiction": [JURISDICTION],
        "regulatory": [{
            "regulatoryAuthority": {
                "display": "Singapore Health Sciences Authority (HSA)"
            },
            "identifier": [{
                "system": f"{BASE_URL}/hsa-license",
                "value": license_id
            }]
        }],
        "extension": [{
            "url": f"{BASE_URL}/fhir/StructureDefinition/prediction-source",
            "valueString": "TxGNN Knowledge Graph"
        }]
    }


def generate_clinical_use_definition(
    drug_name: str,
    drugbank_id: str,
    indication: str,
    source: str,
    score: float | None = None
) -> dict:
    """Generate ClinicalUseDefinition resource."""
    drug_slug = drugbank_id.lower()
    # Create safe indication slug (limit length, remove special chars)
    indication_slug = "".join(c if c.isalnum() or c == "-" else "-" for c in indication.lower())[:50]
    indication_slug = indication_slug.strip("-")
    resource_id = f"{drug_slug}-{indication_slug}"

    # Determine evidence level based on source
    evidence_level = EVIDENCE_LEVELS.get(source, "L5")

    # Build extensions
    extensions = [
        {
            "url": f"{BASE_URL}/fhir/StructureDefinition/evidence-level",
            "valueCode": evidence_level
        },
        {
            "url": f"{BASE_URL}/fhir/StructureDefinition/prediction-source",
            "valueString": source
        }
    ]

    # Add score if available
    if score is not None and not pd.isna(score):
        extensions.append({
            "url": f"{BASE_URL}/fhir/StructureDefinition/txgnn-score",
            "valueDecimal": round(float(score), 6)
        })

    return {
        "resourceType": "ClinicalUseDefinition",
        "id": resource_id,
        "meta": {
            "profile": ["http://hl7.org/fhir/StructureDefinition/ClinicalUseDefinition"]
        },
        "type": "indication",
        "status": {
            "coding": [{
                "system": "http://hl7.org/fhir/publication-status",
                "code": "draft",
                "display": "Draft"
            }]
        },
        "subject": [{"reference": f"MedicationKnowledge/{drug_slug}"}],
        "indication": {
            "diseaseSymptomProcedure": {
                "concept": {
                    "text": indication
                }
            }
        },
        "extension": extensions,
        "warning": {
            "description": {
                "text": "This is a computational prediction for research purposes only. Not validated for clinical use. Always consult healthcare professionals."
            }
        }
    }


def main():
    print("=" * 60)
    print("Generating FHIR R4 Resources - SgTxGNN")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent
    fhir_dir = base_dir / "docs" / "fhir"

    # Create directories
    (fhir_dir / "MedicationKnowledge").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "ClinicalUseDefinition").mkdir(parents=True, exist_ok=True)
    (fhir_dir / "Bundle").mkdir(parents=True, exist_ok=True)

    # 1. Generate CapabilityStatement
    print("1. Generating CapabilityStatement...")
    metadata = generate_capability_statement()
    with open(fhir_dir / "metadata", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
    print("   Created: docs/fhir/metadata")

    # 2. Load unified prediction results
    print("2. Loading unified prediction results...")
    candidates_path = base_dir / "data" / "processed" / "unified_predictions.csv"

    # Fallback to KG-only predictions if unified not available
    if not candidates_path.exists():
        candidates_path = base_dir / "data" / "processed" / "repurposing_candidates.csv"
        print(f"   Warning: unified_predictions.csv not found, using KG predictions only")

    if not candidates_path.exists():
        print(f"   Error: Not found: {candidates_path}")
        print("   Please run run_kg_prediction.py first")
        return

    candidates = pd.read_csv(candidates_path)
    print(f"   Loaded {len(candidates)} predictions")

    # Show source distribution if available
    if "source" in candidates.columns:
        source_counts = candidates["source"].value_counts()
        for src, cnt in source_counts.items():
            print(f"     - {src}: {cnt:,}")

    # 3. Generate MedicationKnowledge resources
    print("3. Generating MedicationKnowledge resources...")

    # Get unique drugs with their info
    drug_info = candidates.groupby("drugbank_id").first().reset_index()
    drug_count = 0

    for _, row in drug_info.iterrows():
        drugbank_id = row["drugbank_id"]
        if pd.isna(drugbank_id) or not drugbank_id:
            continue

        # Handle different column names from KG vs unified predictions
        drug_name = row.get("drug_name", row.get("ingredient", drugbank_id))
        brand_name = row.get("brand_name", drug_name)
        license_id = row.get("license_id", "")

        resource = generate_medication_knowledge(
            drug_name=drug_name,
            drugbank_id=drugbank_id,
            brand_name=brand_name if pd.notna(brand_name) else drug_name,
            license_id=license_id if pd.notna(license_id) else ""
        )

        slug = drugbank_id.lower()
        filepath = fhir_dir / "MedicationKnowledge" / f"{slug}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        drug_count += 1

    print(f"   Created {drug_count} MedicationKnowledge resources")

    # 4. Generate ClinicalUseDefinition resources
    print("4. Generating ClinicalUseDefinition resources...")
    cud_count = 0
    seen_pairs = set()
    source_counts = {"KG": 0, "DL": 0, "KG+DL": 0}

    for _, row in candidates.iterrows():
        drugbank_id = row.get("drugbank_id", "")
        # Handle different column names
        indication = row.get("disease_name", row.get("potential_indication", ""))
        source = row.get("source", "KG")
        score = row.get("score", None)

        if not drugbank_id or not indication or pd.isna(drugbank_id) or pd.isna(indication):
            continue

        # Avoid duplicates
        pair_key = (drugbank_id, indication)
        if pair_key in seen_pairs:
            continue
        seen_pairs.add(pair_key)

        drug_name = row.get("drug_name", row.get("ingredient", drugbank_id))
        resource = generate_clinical_use_definition(
            drug_name=drug_name,
            drugbank_id=drugbank_id,
            indication=indication,
            source=source,
            score=score
        )

        drug_slug = drugbank_id.lower()
        indication_slug = "".join(c if c.isalnum() or c == "-" else "-" for c in indication.lower())[:50]
        indication_slug = indication_slug.strip("-")
        filename = f"{drug_slug}-{indication_slug}.json"

        filepath = fhir_dir / "ClinicalUseDefinition" / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(resource, f, indent=2, ensure_ascii=False)
        cud_count += 1

        # Track source distribution
        if source in source_counts:
            source_counts[source] += 1

    print(f"   Created {cud_count} ClinicalUseDefinition resources")
    if any(source_counts.values()):
        print(f"     - KG+DL (dual validated): {source_counts.get('KG+DL', 0):,}")
        print(f"     - DL only: {source_counts.get('DL', 0):,}")
        print(f"     - KG only: {source_counts.get('KG', 0):,}")

    # 5. Generate summary Bundle
    print("5. Generating summary Bundle...")
    bundle = {
        "resourceType": "Bundle",
        "id": "sgtxgnn-summary",
        "type": "collection",
        "timestamp": datetime.now().isoformat(),
        "total": drug_count + cud_count,
        "link": [
            {"relation": "self", "url": f"{BASE_URL}/fhir/Bundle/sgtxgnn-summary"}
        ],
        "entry": [
            {"fullUrl": f"{BASE_URL}/fhir/metadata", "resource": metadata}
        ]
    }

    with open(fhir_dir / "Bundle" / "summary.json", "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)
    print("   Created: docs/fhir/Bundle/summary.json")

    print()
    print("=" * 60)
    print("FHIR Resource Generation Complete!")
    print("=" * 60)
    print(f"  MedicationKnowledge: {drug_count}")
    print(f"  ClinicalUseDefinition: {cud_count}")
    print(f"  Output directory: {fhir_dir}")
    print()
    print("Note: These predictions are for research only.")
    print("      Not validated for clinical use.")


if __name__ == "__main__":
    main()
