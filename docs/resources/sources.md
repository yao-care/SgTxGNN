---
layout: default
title: Data Sources
parent: Resources
nav_order: 1
description: "Data sources used in SgTxGNN"
permalink: /resources/sources/
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

**Coverage**:
- 17,080 diseases
- 7,957 drugs
- 80,000+ drug-disease relationships

### Singapore HSA

**Source**: Health Sciences Authority, Singapore

Drug registration data for Singapore-approved medications.

- [HSA Website](https://www.hsa.gov.sg/)
- [data.gov.sg](https://data.gov.sg/)

**Coverage**:
- 11,466 registered drugs
- 745 drugs mapped to DrugBank

---

## Evidence Sources

### ClinicalTrials.gov

**Source**: U.S. National Library of Medicine

Global registry of clinical trials.

- [Website](https://clinicaltrials.gov/)
- [API Documentation](https://clinicaltrials.gov/data-api/api)

**Usage**: Evidence collection for drug-disease pairs

### PubMed

**Source**: U.S. National Library of Medicine

Biomedical literature database.

- [Website](https://pubmed.ncbi.nlm.nih.gov/)
- [API Documentation](https://www.ncbi.nlm.nih.gov/home/develop/api/)

**Usage**: Literature evidence for repurposing candidates

### DrugBank

**Source**: University of Alberta

Comprehensive drug and target database.

- [Website](https://go.drugbank.com/)
- Data used under academic license

**Coverage**:
- Drug identifiers and mappings
- Drug-target interactions
- Drug-drug interactions

---

## Safety Data Sources

### DDInter

**Source**: Shanghai University

Drug-drug interaction database.

- [Website](http://ddinter.scbdd.com/)

**Coverage**: 240,000+ interaction pairs

### SIDER

**Source**: EMBL

Side effect database.

- [Website](http://sideeffects.embl.de/)

---

## Data Processing

### Drug Mapping

1. HSA drug names extracted from registration data
2. Normalised using chemical name standardisation
3. Mapped to DrugBank identifiers
4. Successfully mapped: **745 drugs** (73.87% of unique ingredients)

### Prediction Generation

1. DrugBank IDs matched to TxGNN knowledge graph
2. Knowledge Graph predictions generated: **22,136**
3. Deep Learning predictions generated: **29,100**
4. Results unified and deduplicated: **31,543**

---

## Update Schedule

| Source | Last Updated | Frequency |
|--------|--------------|-----------|
| TxGNN Model | 2023 | As published |
| HSA Data | March 2026 | Quarterly |
| DrugBank | 2025 | Annual |
| DDInter | 2025 | Annual |

---

## Licensing

| Source | License |
|--------|---------|
| **TxGNN** | Academic use permitted |
| **HSA Data** | Open Government License |
| **DrugBank** | Academic license |
| **PubMed/ClinicalTrials** | Public domain |
| **DDInter** | Academic use |

---

## Data Quality

### Validation Steps

1. **Drug name verification**: Cross-referenced with multiple sources
2. **ID mapping validation**: Verified against DrugBank
3. **Prediction deduplication**: Removed duplicate entries
4. **Evidence verification**: Checked source availability

### Known Limitations

- Not all HSA drugs have DrugBank mappings
- Some generic names have multiple variants
- TxGNN model trained on Western drug databases
- Evidence collection may miss recent publications

---

## Contact

For data-related questions:
- [GitHub Issues](https://github.com/yao-care/SgTxGNN/issues)
