---
layout: default
title: Methodology
parent: Help
nav_order: 4
description: "How SgTxGNN predictions are generated and validated"
permalink: /methodology/
---

# Methodology
{: .fs-9 }

How predictions are generated and validated
{: .fs-6 .fw-300 }

---

## Overview

SgTxGNN uses a dual-method approach combining **Knowledge Graph (KG)** predictions and **Deep Learning (DL)** predictions to identify drug repurposing candidates. Predictions validated by both methods (KG+DL) have higher confidence.

---

## Prediction Pipeline

### Step 1: Knowledge Graph Prediction (KG)

The Knowledge Graph method uses TxGNN's biomedical knowledge graph containing:
- **17,080 biomedical entities** (drugs, diseases, genes, proteins)
- **80,127 drug-disease relationships**
- **Biological pathway connections**

KG predictions identify drugs that share biological pathways or targets with diseases.

### Step 2: Deep Learning Prediction (DL)

The Deep Learning method uses TxGNN's graph neural network model:
- Trained on known drug-disease relationships
- Learns complex patterns in the knowledge graph
- Outputs confidence scores (0.0-1.0) for each drug-disease pair

### Step 3: Dual Validation (KG+DL)

Predictions that appear in **both** KG and DL results are marked as "KG+DL" with higher confidence:
- **1,217 dual-validated predictions** in SgTxGNN
- These predictions have convergent evidence from two independent methods

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

### Confidence Scores

DL predictions include confidence scores:
- **>0.99**: Very high confidence
- **0.95-0.99**: High confidence
- **0.90-0.95**: Moderate confidence
- **0.50-0.90**: Lower confidence (still above threshold)

### Filtering Criteria

All predictions meet these minimum criteria:
- DL score ≥ 0.50 (above random chance)
- Drug is registered with Singapore HSA
- Drug has valid DrugBank mapping

---

## Data Processing

### Singapore HSA Data

1. Drug registration data from [data.gov.sg](https://data.gov.sg/)
2. 5,485 registered products processed
3. Active ingredients mapped to DrugBank IDs
4. 745 unique drugs with successful mapping

### TxGNN Integration

1. DrugBank IDs matched to TxGNN knowledge graph
2. Predictions generated for all mapped drugs
3. Results filtered by confidence threshold
4. Final dataset: **31,543 predictions**

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
| TxGNN Model | v1.0 (Nature Medicine 2023) |
| HSA Data | March 2026 |
| SgTxGNN | v1.0.0 |

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
Predictions are computational hypotheses for research purposes only. Clinical validation is required before any therapeutic application.
</div>
