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

The predicted new indications listed on this site's public drug pages, one row per drug–indication pair, with the TxGNN deep learning (DL) model score. Known uses are excluded on the drug pages, so they are not in these files. The files are rebuilt from the drug pages (noindex and redirect pages excluded).

| Format | File | Size | Description |
|--------|------|------|-------------|
| CSV | [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) | ~250 KB | All predicted drug–indication pairs on the public drug pages |
| JSON | [drugs.json]({{ '/data/drugs.json' | relative_url }}) | ~300 KB | List of drug report pages with evidence level |
| JSON | [drugs-by-level.json]({{ '/data/drugs-by-level.json' | relative_url }}) | ~280 KB | Public drug pages grouped by evidence level (`levels`, with each drug's top-scoring predicted indication), drug and pair counts (`counts`), and the 100 highest-scoring pairs (`high_score`) |
| JSON | [search-index.json]({{ '/data/search-index.json' | relative_url }}) | ~750 KB | Search index used by the site and the SMART app |

---

## Data Schema

### drugs.csv Columns

| Column | Type | Description |
|--------|------|-------------|
| `drugbank_id` | string | DrugBank identifier (e.g., DB01048), from this site's DrugBank ID redirect pages; empty when none |
| `drug_name` | string | Drug name as shown on the drug page |
| `disease_name` | string | Predicted new indication listed on the drug page |
| `score` | float | TxGNN deep learning model score (0–1, 4 decimals); a ranking value, not a probability |
| `source` | string | Always DL (deep learning prediction). Known uses are excluded on the drug pages, so there are no KG or KG+DL rows |

### Example Rows

```csv
drugbank_id,drug_name,disease_name,score,source
DB01048,Abacavir,simian immunodeficiency virus infection,0.9979,DL
DB01048,Abacavir,feline acquired immunodeficiency syndrome,0.9979,DL
DB01048,Abacavir,"neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter",0.9978,DL
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
