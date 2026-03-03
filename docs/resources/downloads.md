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

All drug repurposing predictions with source and confidence information.

| File | Format | Size | Records |
|------|--------|------|---------|
| [unified_predictions.csv]({{ '/data/unified_predictions.csv' | relative_url }}) | CSV | ~3 MB | 31,543 |

**Columns**:
- `drugbank_id`: DrugBank identifier
- `drug_name`: Generic drug name
- `disease_name`: Predicted indication
- `score`: Confidence score (0-1)
- `source`: Prediction method (KG, DL, KG+DL)

### Drug List

Complete list of analysed drugs with metadata.

| File | Format | Size | Records |
|------|--------|------|---------|
| [drugs.json]({{ '/data/drugs.json' | relative_url }}) | JSON | ~500 KB | 745 |
| [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) | CSV | ~100 KB | 745 |

---

## Search Index

Full searchable index for the website.

| File | Format | Size | Entries |
|------|--------|------|---------|
| [search-index.json]({{ '/data/search-index.json' | relative_url }}) | JSON | ~5 MB | 31,543 |

---

## FHIR Resources

FHIR R4 resources available via API:

```bash
# CapabilityStatement
curl https://sgtxgnn.yao.care/fhir/metadata

# MedicationKnowledge
curl https://sgtxgnn.yao.care/fhir/MedicationKnowledge/DB00945

# ClinicalUseDefinition
curl https://sgtxgnn.yao.care/fhir/ClinicalUseDefinition/DB00945-indication-1
```

---

## Mapping Files

### Drug Mapping

HSA drugs to DrugBank mappings.

| File | Format | Description |
|------|--------|-------------|
| [drug_mapping.csv]({{ '/data/drug_mapping.csv' | relative_url }}) | CSV | HSA → DrugBank |

### Disease Mapping

Disease name normalisation.

| File | Format | Description |
|------|--------|-------------|
| [disease_mapping.csv]({{ '/data/disease_mapping.csv' | relative_url }}) | CSV | Local → Standard |

---

## Bulk Download

Download complete dataset:

```bash
# Clone repository
git clone https://github.com/yao-care/SgTxGNN.git

# Data is in data/processed/
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

```json
{
  "drugs": [
    {
      "drugbank_id": "DB00945",
      "name": "Aspirin",
      "predictions": [...]
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
