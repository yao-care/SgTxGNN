---
layout: default
title: Methodology
parent: Help
nav_order: 1
description: "How SgTxGNN predictions are generated and validated"
permalink: /methodology/
---

# Methodology
{: .fs-9 }

How predictions are generated and validated
{: .fs-6 .fw-300 }

---

## Overview

SgTxGNN uses TxGNN's **deep learning (DL)** model to score drug–disease pairs. Indications and contraindications already recorded for the drug in the TxGNN **knowledge graph (KG)** are removed, so drug pages list only new predicted indications with a score of at least 0.99 (up to 10 per drug).

---

## Prediction Pipeline

### Step 1: Deep Learning Prediction (DL)

The Deep Learning method uses TxGNN's graph neural network model:
- Trained on known drug-disease relationships
- Learns complex patterns in the knowledge graph
- Outputs scores (0.0-1.0) for each drug-disease pair

### Step 2: Known-Use Check (KG)

The TxGNN knowledge graph records **80,127 drug-disease relationships** (indications, off-label uses and contraindications). Indications and contraindications already recorded for a drug are removed from its predictions; they are known uses, not new predictions.

### Step 3: Selection

For each drug, the remaining predictions with a score of at least 0.99 are kept (up to 10), and evidence is collected for each of them.

---

## Evidence Classification

### L1-L5 Evidence Levels

| Level | Definition | Criteria |
|-------|------------|----------|
| **L1** | Multiple Phase 3 RCTs | ≥2 completed Phase 3 trials with positive results |
| **L2** | Single RCT or Phase 2 | 1 RCT or ≥2 Phase 2 trials |
| **L3** | Observational Studies | Cohort or case-control studies |
| **L4** | Preclinical/Mechanistic | In vitro, animal studies, or mechanistic evidence |
| **L5** | Prediction Only | AI prediction without clinical evidence |

### Evidence Sources

Evidence is collected from:
1. **ClinicalTrials.gov** - Clinical trial registry
2. **PubMed** - Biomedical literature
3. **DrugBank** - Drug mechanism and interaction data
4. **Singapore HSA** - Local registration status

---

## Prediction Quality

### Filtering Criteria

Predicted new indications shown on drug pages meet all of these criteria:
- DL score ≥ 0.99
- Not an indication or contraindication already recorded in the knowledge graph
- Drug is registered with Singapore HSA
- Drug has valid DrugBank mapping

---

## Data Processing

### Singapore HSA Data

1. Drug registration data from [data.gov.sg](https://data.gov.sg/)
2. 11,466 registered products processed
3. Active ingredients mapped to DrugBank IDs
4. 745 unique drugs with successful mapping

### TxGNN Integration

1. DrugBank IDs matched to TxGNN knowledge graph
2. Predictions generated for all mapped drugs
3. Results filtered by confidence threshold
4. Known uses removed; predictions with score ≥ 0.99 kept: **{{ site.data.site_stats.indications }} predicted new indications**

---

## Limitations

### Model Limitations

- TxGNN trained on historical data (may miss recent discoveries)
- Some drugs/diseases not in knowledge graph
- Predictions are computational hypotheses, not clinical evidence

### Data Limitations

- HSA data may not include all marketed products
- Some ingredient mappings may be imprecise
- Evidence collection limited to English literature

### Interpretation

- L5 predictions require clinical validation
- High DL scores don't guarantee clinical efficacy
- Always consult healthcare professionals

---

## Reproducibility

### Code & Data

- Source code: [GitHub](https://github.com/yao-care/SgTxGNN)
- TxGNN model: [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM)
- HSA data: [data.gov.sg](https://data.gov.sg/)

### Version Information

| Component | Version |
|-----------|---------|
| TxGNN Model | v1.0 (Nature Medicine 2024) |
| HSA Data | March 2026 |
| SgTxGNN | v1.0.0 |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Predictions are computational hypotheses for research purposes only. Clinical validation is required before any therapeutic application.
</div>
