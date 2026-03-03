---
layout: default
title: Downloads
nav_order: 12
description: "Download SgTxGNN drug repurposing prediction data"
permalink: /downloads/
---

# Downloads
{: .fs-9 }

Download prediction data in various formats
{: .fs-6 .fw-300 }

---

## Available Datasets

### Unified Predictions

Complete dataset of all drug repurposing predictions combining KG and DL methods.

| Format | File | Size | Description |
|--------|------|------|-------------|
| CSV | [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) | ~2 MB | All predictions in CSV format |
| JSON | [drugs.json]({{ '/data/drugs.json' | relative_url }}) | ~50 KB | Drug list with metadata |
| JSON | [drugs-by-level.json]({{ '/data/drugs-by-level.json' | relative_url }}) | ~100 KB | Predictions organized by evidence level |
| JSON | [search-index.json]({{ '/data/search-index.json' | relative_url }}) | ~3 MB | Full search index |

---

## Data Schema

### drugs.csv Columns

| Column | Type | Description |
|--------|------|-------------|
| `drugbank_id` | string | DrugBank identifier (e.g., DB00945) |
| `drug_name` | string | Drug generic name |
| `disease_name` | string | Predicted indication |
| `score` | float | DL confidence score (0.5-1.0, null for KG-only) |
| `source` | string | Prediction source (KG, DL, or KG+DL) |

### Example Rows

```csv
drugbank_id,drug_name,disease_name,score,source
DB00945,Acetylsalicylic acid,myocardial infarction,0.948889,KG+DL
DB01076,Atorvastatin,cerebrovascular disorder,0.923456,DL
DB00829,Diazepam,alcohol withdrawal,null,KG
```

---

## API Access

### FHIR R4 API

SgTxGNN provides a FHIR R4-compliant API for programmatic access:

- **Base URL**: `https://sgtxgnn.yao.care/fhir/`
- **Capability Statement**: [/fhir/metadata]({{ '/fhir/metadata' | relative_url }})

#### Available Resources

| Resource | Endpoint | Count |
|----------|----------|-------|
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}` | 745 |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}` | 31,543 |

#### Example Request

```bash
curl https://sgtxgnn.yao.care/fhir/MedicationKnowledge/db00945
```

---

## Terms of Use

- **Academic Use**: Free for academic and research purposes
- **Commercial Use**: Please contact us for licensing
- **Attribution**: Please cite this project when using the data

### Citation

```
Yao.Care. (2026). SgTxGNN: Drug Repurposing Predictions for Singapore HSA Drugs.
https://sgtxgnn.yao.care/
```

---

## Data Updates

| Dataset | Last Updated | Update Frequency |
|---------|--------------|------------------|
| HSA Drug Data | March 2026 | As needed |
| TxGNN Predictions | March 2026 | Model version updates |
| Evidence Collection | - | Future feature |

---

## Source Code

The complete source code for SgTxGNN is available on GitHub:

- **Repository**: [github.com/yao-care/SgTxGNN](https://github.com/yao-care/SgTxGNN)
- **License**: MIT

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Downloaded data is for research purposes only and does not constitute medical advice.
</div>
