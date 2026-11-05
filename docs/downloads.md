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

Candidate table combining deep learning (DL) predictions with known uses from the knowledge graph (KG). Rows with source KG are known uses, not predictions.

| Format | File | Size | Description |
|--------|------|------|-------------|
| CSV | [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) | ~2 MB | All drug–disease pairs (predictions and known uses) |
| JSON | [drugs.json]({{ '/data/drugs.json' | relative_url }}) | ~300 KB | List of drug report pages with evidence level |
| JSON | [drugs-by-level.json]({{ '/data/drugs-by-level.json' | relative_url }}) | ~40 KB | Row counts by source (KG / DL / KG+DL) and the top-scoring pairs |
| JSON | [search-index.json]({{ '/data/search-index.json' | relative_url }}) | ~750 KB | Search index used by the site and the SMART app |

---

## Data Schema

### drugs.csv Columns

| Column | Type | Description |
|--------|------|-------------|
| `drugbank_id` | string | DrugBank identifier (e.g., DB00945) |
| `drug_name` | string | Drug generic name |
| `disease_name` | string | Disease (predicted or known use, see `source`) |
| `score` | float | DL model score (0.5-1.0, empty for KG-only rows); a ranking value, not a probability |
| `source` | string | KG = known use in the knowledge graph; DL = model prediction; KG+DL = known use also scored by DL |

### Example Rows

```csv
drugbank_id,drug_name,disease_name,score,source
DB00005,ETANERCEPT,ankylosing spondylitis,,KG
DB00829,Diazepam,alcohol withdrawal,0.999200403690338,KG+DL
DB00945,Acetylsalicylic acid,migraine with brainstem aura,0.999371349811554,DL
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
| MedicationKnowledge | `/fhir/MedicationKnowledge/{id}.json` | {{ site.static_files | where_exp: 'f', 'f.path contains "/fhir/MedicationKnowledge/"' | size }} |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/{id}.json` | {{ site.static_files | where_exp: 'f', 'f.path contains "/fhir/ClinicalUseDefinition/"' | size }} |

#### Example Request

```bash
curl https://sgtxgnn.yao.care/fhir/MedicationKnowledge/amlodipine.json
```

Resources are static files named by drug slug; search queries are not supported. See the [FHIR API page]({{ '/smart/fhir-api/' | relative_url }}).

---

## Terms of Use

- **Academic Use**: Free for academic and research purposes
- **Commercial Use**: Please contact us for licensing
- **Attribution**: Please cite this project when using the data

### Citation

```
yao.care. (2026). SgTxGNN: Drug Repurposing Predictions for Singapore HSA Drugs.
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
