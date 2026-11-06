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

The predicted new indications listed on this site's public drug pages, with the TxGNN deep learning model score. Known uses are excluded on the drug pages, so they are not in this file.

| File | Format | Size | Records |
|------|--------|------|---------|
| [drugs.csv]({{ '/data/drugs.csv' | relative_url }}) | CSV | ~250 KB | One row per drug–indication pair |

**Columns**:
- `drugbank_id`: DrugBank identifier, from this site's DrugBank ID redirect pages; empty when none
- `drug_name`: Drug name as shown on the drug page
- `disease_name`: Predicted new indication listed on the drug page
- `score`: TxGNN model score (0–1); a ranking value, not a probability
- `source`: always DL (deep learning prediction); there are no KG or KG+DL rows

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

`drugs.json` lists the public drug report pages, one entry per page (count in `total_count`).

| Field | Description |
|-------|-------------|
| `slug` | URL name of the drug page (`/drugs/<slug>/`) |
| `name` | Drug name |
| `evidence_level` | Evidence level shown at the top of the drug page (L1–L5) |
| `indication_count` | Number of predicted indications on the drug page |
| `original_indication` | Approved indication, filled only when the drug page front matter has one; currently empty (`""`) for every drug |
| `predicted_indication` | Currently empty (`""`) for every drug. It used to be extracted automatically from the page text, but most extracted values were table headings, so it has been left empty since 2026-11-06. The field is kept so existing code does not break |
| `txgnn_score` | Currently empty (`""`) for every drug, for the same reason |
| `url` | Drug page URL |

For predicted indications and their model scores, see each drug page or [search-index.json]({{ '/data/search-index.json' | relative_url }}).

Example (excerpt of the generated file):

```json
{
  "generated": "2026-11-06",
  "total_count": {{ site.data.drug_stats.total_drugs }},
  "source": "SgTxGNN",
  "drugs": [
    {
      "slug": "abacavir",
      "name": "Abacavir",
      "evidence_level": "L5",
      "indication_count": 3,
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
