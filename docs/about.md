---
layout: default
title: About
parent: Help
nav_order: 3
description: "SgTxGNN is a drug repurposing prediction platform based on Harvard's TxGNN model, integrating clinical trials, literature, and other evidence sources for 745 Singapore HSA-approved medications."
permalink: /about/
---

# About This Project

<div class="key-takeaway">
Accelerating drug repurposing evidence validation with AI — from prediction to evidence at a glance.
</div>

---

## Project Background

<p class="key-answer" data-question="What is SgTxGNN?">
<strong>SgTxGNN</strong> is a drug repurposing research platform based on Harvard's TxGNN model published in <em>Nature Medicine</em>. Unlike other prediction tools, this platform not only provides AI prediction scores but also integrates clinical evidence from ClinicalTrials.gov, PubMed, and other sources, enabling researchers to quickly assess prediction credibility.
</p>

---

## Team

| Item | Information |
|------|-------------|
| Project Maintainer | Yao.Care |
| Model Basis | Harvard TxGNN (Zitnik Lab) |
| Last Updated | March 2026 |

### Academic Foundation

This project's AI prediction model is based on:

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## What is Drug Repurposing?

<p class="key-answer" data-question="What is drug repurposing?">
<strong>Drug Repurposing</strong> is discovering new therapeutic uses for existing drugs. Compared to developing new drugs (10-15 years, $1-2 billion), drug repurposing takes only 3-5 years and $100-300 million, with existing human safety data and lower failure risk.
</p>

| Comparison | New Drug Development | Drug Repurposing |
|------------|---------------------|------------------|
| Development Time | 10-15 years | 3-5 years |
| Development Cost | $1-2 billion | $100-300 million |
| Safety Data | Must establish new | Existing human data |
| Failure Risk | Very high (>90%) | Lower |

<div class="key-takeaway">
The advantage of drug repurposing: drug safety, pharmacokinetics, and manufacturing processes are already validated, allowing direct entry into clinical efficacy trials.
</div>

---

## What is TxGNN?

<p class="key-answer" data-question="What is TxGNN?">
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> is a deep learning model developed by Harvard Medical School's Zitnik Lab team, published in <em>Nature Medicine</em>. It is the first foundation model designed for clinician-centered drug repurposing.
</p>

<blockquote class="expert-quote">
"TxGNN integrates a knowledge graph of 17,080 biomedical entities, using graph neural networks to learn complex relationships between nodes and predict drug efficacy for rare diseases."
<cite>— Huang et al., Nature Medicine (2023)</cite>
</blockquote>

### Technical Features

1. **Knowledge Graph**: Integrates 17,080 nodes including drugs, diseases, genes, and proteins
2. **Graph Neural Network**: Learns complex relationships between nodes
3. **Prediction Capability**: Predicts which diseases a drug might be effective for

---

## Data Sources

<p class="key-answer" data-question="What are SgTxGNN's data sources?">
This platform integrates multiple authoritative public data sources including AI predictions, clinical trials, academic literature, drug information, Singapore market information, and drug interaction data.
</p>

| Data Type | Source | Description |
|-----------|--------|-------------|
| AI Prediction | [TxGNN](https://zitniklab.hms.harvard.edu/projects/TxGNN/) | Harvard knowledge graph prediction model |
| Clinical Trials | [ClinicalTrials.gov](https://clinicaltrials.gov/) | Global clinical trial registry |
| Academic Literature | [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Biomedical literature database |
| Drug Information | [DrugBank](https://go.drugbank.com/) | Drug and target database |
| Singapore Market | [HSA](https://www.hsa.gov.sg/) | Health Sciences Authority |

---

## Project Scale

| Item | Count |
|------|-------|
| Drug Reports | 745 |
| Repurposing Candidates | 31,543 |
| Diseases Covered | 4,589 |
| Dual Validated (KG+DL) | 1,217 |

---

## How to Cite

If you use data from this platform, please use the following format:

### APA Format

```
Yao.Care. (2026). SgTxGNN: Drug Repurposing Validation Reports for Singapore HSA Drugs (v1.0.0). https://sgtxgnn.yao.care/
```

### Citing the Original Model

If using TxGNN prediction results, please also cite the original paper:

```bibtex
@article{huang2023txgnn,
  title={A foundation model for clinician-centered drug repurposing},
  author={Huang, Kexin and others},
  journal={Nature Medicine},
  year={2023},
  doi={10.1038/s41591-023-02233-x}
}
```

---

## Contact & Feedback

For questions or suggestions, please contact us through:

- **GitHub Issues**: [https://github.com/yao-care/SgTxGNN/issues](https://github.com/yao-care/SgTxGNN/issues)
- **Project Homepage**: [https://sgtxgnn.yao.care/](https://sgtxgnn.yao.care/)

---

<div class="disclaimer">
<strong>Disclaimer</strong><br>
This report is for academic research purposes only and <strong>does not constitute medical advice</strong>. Please follow physician instructions for medication use. Any drug repurposing decisions require complete clinical validation and regulatory approval.
<br><br>
<small>Last Review: 2026-03-03 | Reviewer: SgTxGNN Research Team</small>
</div>
