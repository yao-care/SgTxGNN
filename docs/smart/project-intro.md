---
layout: default
title: Project Introduction
parent: SMART on FHIR
nav_order: 7
description: "SgTxGNN project introduction"
permalink: /smart/project-intro/
---

# Project Introduction

## SgTxGNN: Drug Repurposing Predictions for Singapore

---

## Background

Drug repurposing (also known as drug repositioning) is a strategy for identifying new uses for existing, approved drugs. This approach offers several advantages over traditional drug discovery:

- **Reduced development time**: Existing drugs have known safety profiles
- **Lower costs**: Much of the clinical work has already been done
- **Higher success rates**: Known compounds reduce technical risk

---

## The TxGNN Model

SgTxGNN is built on **TxGNN** (Therapeutic Target Prediction using Graph Neural Networks), developed by Harvard Medical School's Zitnik Lab and published in *Nature Medicine* (2023).

### Key Features

- **Knowledge Graph**: Integrates biomedical knowledge from multiple sources
- **Deep Learning**: Uses graph neural networks for prediction
- **Clinical Focus**: Designed specifically for drug repurposing

### Citation

> Huang, K., Chandak, P., Wang, Q. et al. A foundation model for clinician-centered drug repurposing. *Nat Med* (2023). https://doi.org/10.1038/s41591-023-02233-x

---

## Singapore Adaptation

SgTxGNN adapts TxGNN specifically for Singapore:

### Data Sources

| Source | Description |
|--------|-------------|
| **HSA** | Health Sciences Authority drug registry |
| **DrugBank** | Drug-target relationships |
| **TxGNN KG** | Biomedical knowledge graph |

### Coverage

- **745 drugs** mapped to DrugBank
- **31,543 predictions** generated
- **4,589 diseases** covered

---

## Methodology

### 1. Drug Mapping

Singapore HSA drug data is mapped to international identifiers:

```
HSA Drug Registry → Ingredient Normalisation → DrugBank ID
```

Mapping rate: **73.87%** of HSA ingredients successfully mapped

### 2. Prediction Methods

Two complementary approaches:

| Method | Description | Count |
|--------|-------------|-------|
| **Knowledge Graph (KG)** | Direct relationship queries | 22,136 |
| **Deep Learning (DL)** | Neural network predictions | 29,100 |
| **Unified (KG+DL)** | Dual-validated predictions | 1,217 |

### 3. Evidence Classification

Predictions are classified by evidence level:

| Level | Description |
|-------|-------------|
| **L1** | Multiple Phase 3 RCTs |
| **L2** | Single RCT or Phase 2 trials |
| **L3** | Observational studies |
| **L4** | Preclinical/mechanistic evidence |
| **L5** | Model prediction only |

---

## Use Cases

### For Researchers

- Identify promising drug repurposing candidates
- Prioritise experimental validation studies
- Explore drug-disease relationships

### For Clinicians

- Research potential off-label uses
- Understand drug mechanisms
- Access structured evidence summaries

### For Healthcare Institutions

- Support translational research
- Enable clinical decision support research
- Facilitate EHR integration via SMART on FHIR

---

## Limitations

Important considerations:

1. **Research use only**: Predictions have not been clinically validated
2. **No clinical guidance**: Not intended for treatment decisions
3. **Model uncertainty**: AI predictions may be incorrect
4. **Singapore focus**: Based on HSA-approved medications

---

## Future Directions

Planned enhancements:

- Integration of clinical trial evidence
- Literature-based validation scoring
- Drug interaction analysis
- Periodic model updates

---

## Contact

- **Website**: [sgtxgnn.yao.care](https://sgtxgnn.yao.care)
- **GitHub**: [yao-care/SgTxGNN](https://github.com/yao-care/SgTxGNN)
- **Issues**: [Report bugs or suggest features](https://github.com/yao-care/SgTxGNN/issues)
