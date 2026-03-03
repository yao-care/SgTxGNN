---
layout: default
title: Data Sources Reference
parent: Help
nav_order: 5
description: "Data sources used in SgTxGNN"
permalink: /sources/
---

# Data Sources

SgTxGNN integrates data from multiple authoritative sources to provide comprehensive drug repurposing predictions and evidence.

---

## Primary Sources

### TxGNN Model

**Source**: Harvard Medical School, Zitnik Lab

The core prediction engine, published in *Nature Medicine* (2023).

- [Project Page](https://zitniklab.hms.harvard.edu/projects/TxGNN/)
- [Paper](https://doi.org/10.1038/s41591-023-02233-x)
- [Dataset](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM)

### Singapore HSA

**Source**: Health Sciences Authority, Singapore

Drug registration data for Singapore-approved medications.

- [HSA Website](https://www.hsa.gov.sg/)
- [data.gov.sg](https://data.gov.sg/)

---

## Evidence Sources

### ClinicalTrials.gov

**Source**: U.S. National Library of Medicine

Global registry of clinical trials.

- [Website](https://clinicaltrials.gov/)
- [API Documentation](https://clinicaltrials.gov/data-api/api)

### PubMed

**Source**: U.S. National Library of Medicine

Biomedical literature database.

- [Website](https://pubmed.ncbi.nlm.nih.gov/)
- [API Documentation](https://www.ncbi.nlm.nih.gov/home/develop/api/)

### DrugBank

**Source**: University of Alberta

Comprehensive drug and target database.

- [Website](https://go.drugbank.com/)
- Data used under academic license

---

## Data Processing

### Drug Mapping

1. HSA drug names extracted from registration data
2. Normalized using chemical name standardization
3. Mapped to DrugBank identifiers
4. Successfully mapped: 745 drugs

### Prediction Generation

1. DrugBank IDs matched to TxGNN knowledge graph
2. Knowledge Graph predictions generated
3. Deep Learning predictions generated
4. Results combined and deduplicated

---

## Update Schedule

| Source | Last Updated | Frequency |
|--------|--------------|-----------|
| TxGNN Model | 2023 | As published |
| HSA Data | March 2026 | Quarterly |
| DrugBank | 2025 | Annual |

---

## Licensing

- **TxGNN**: Academic use permitted
- **HSA Data**: Open Government License
- **DrugBank**: Academic license
- **PubMed/ClinicalTrials**: Public domain

---

## Citation

When using SgTxGNN data, please cite:

1. This platform (see [About](/about/) for citation format)
2. Original TxGNN paper (Huang et al., Nature Medicine 2023)
3. Relevant data sources as appropriate
