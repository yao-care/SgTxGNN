---
layout: default
title: Data Downloads
parent: Resources
nav_order: 2
description: "Download SgTxGNN datasets"
permalink: /resources/downloads/
---

# Data Downloads

Download SgTxGNN datasets for research use.

---

## Prediction Data

### Unified Predictions

All drug repurposing predictions with source and model score.

| File | Format | Size | Records |
|------|--------|------|---------|
| [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) | CSV | ~2 MB | One row per drug–disease pair |

**Columns**:
- `drugbank_id`: DrugBank identifier
- `drug_name`: Generic drug name
- `disease_name`: Disease (predicted or known use, see `source`)
- `score`: Model score (0-1); a ranking value, not a probability
- `source`: KG = known use in the knowledge graph; DL = model prediction; KG+DL = known use also scored by DL

### Drug List

List of drug report pages with evidence level and links.

| File | Format | Size | Records |
|------|--------|------|---------|
| [drugs.json]({{ '/data/drugs.json' | relative_url }}) | JSON | ~300 KB | One entry per drug page (count in `total_count`) |

---

## Search Index

Searchable index used by the website and the SMART app: drugs with their top predicted indications, and indications with their drugs.

| File | Format | Size | Entries |
|------|--------|------|---------|
| [search-index.json]({{ '/data/search-index.json' | relative_url }}) | JSON | ~750 KB | Counts in `drug_count` and `indication_count` |

---

## FHIR Resources

FHIR R4 resources are served as static JSON files. MedicationKnowledge files are named by drug (`/fhir/MedicationKnowledge/{drug}.json`) and ClinicalUseDefinition files by drug and predicted indication (`/fhir/ClinicalUseDefinition/{drug}-{disease}.json`):

```bash
# CapabilityStatement
curl https://sgtxgnn.yao.care/fhir/metadata

# MedicationKnowledge
curl https://sgtxgnn.yao.care/fhir/MedicationKnowledge/amlodipine.json

# ClinicalUseDefinition
curl https://sgtxgnn.yao.care/fhir/ClinicalUseDefinition/amlodipine-brain-stem-infarction.json
```

---

## Bulk Download

The git repository does not include the processed data files (`data/processed/`), so cloning it is not enough. The complete dataset is published as a GitHub Release asset of the SgTxGNN repository, currently [data-20261029](https://github.com/yao-care/SgTxGNN/releases/tag/data-20261029) (see all [SgTxGNN releases](https://github.com/yao-care/SgTxGNN/releases)).

Download every `SgTxGNN-data.tar.gz.part-*` file and `SgTxGNN-data.sha256` from the release, then:

```bash
# Verify and extract (creates SgTxGNN/data/)
sha256sum -c SgTxGNN-data.sha256
cat SgTxGNN-data.tar.gz.part-* | tar xzf -

# Processed data is in SgTxGNN/data/processed/
ls SgTxGNN/data/processed/
```

---

## Data Format Details

### CSV Format

- **Encoding**: UTF-8
- **Delimiter**: Comma
- **Quote character**: Double quote
- **Header**: First row

### JSON Format

`drugs.json`:

```json
{
  "generated": "2026-10-17",
  "total_count": 1051,
  "source": "SgTxGNN",
  "drugs": [
    {
      "slug": "abacavir",
      "name": "Abacavir",
      "evidence_level": "L4",
      "indication_count": 10,
      "original_indication": "",
      "predicted_indication": "",
      "txgnn_score": "",
      "url": "/drugs/abacavir/"
    }
  ]
}
```

---

## Usage Terms

### Academic Use

Free for academic and research purposes with citation:

```bibtex
@software{sgtxgnn2026,
  author = {Yao.Care},
  title = {SgTxGNN: Drug Repurposing Predictions for Singapore},
  year = 2026,
  url = {https://sgtxgnn.yao.care}
}
```

### Commercial Use

Contact for commercial licensing.

### Attribution

Please cite both SgTxGNN and the original TxGNN paper when using this data.

---

## Data Updates

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | March 2026 | Initial release |

Subscribe to [GitHub releases](https://github.com/yao-care/SgTxGNN/releases) for update notifications.

---

<div class="disclaimer">
<strong>Research Use Only</strong><br>
This data is provided for research purposes. Predictions have not been clinically validated. See <a href="{{ '/resources/sources/' | relative_url }}">Data Sources</a> for licensing details.
</div>
