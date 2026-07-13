---
layout: default
title: Lurbinectedin
parent: 僅模型預測 (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
---

# Lurbinectedin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lurbinectedin: From Small Cell Lung Cancer to Multiple Endocrine Neoplasia

## One-Sentence Summary

Lurbinectedin (Zepzelca) is an alkylating antineoplastic agent approved by the US FDA in 2020 for adult patients with metastatic small cell lung cancer (SCLC) who have progressed on or after platinum-based chemotherapy; it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Multiple Endocrine Neoplasia (MEN)**, with **0 clinical trials** and **0 publications** currently supporting this direction.
All 10 predicted indications are at evidence level L5 (model prediction only); the prediction list includes multiple veterinary and non-human diseases, suggesting significant knowledge graph overgeneralisation artifacts.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic small cell lung cancer (SCLC) — FDA-approved 2020; no Singapore HSA registration |
| Predicted New Indication | Multiple Endocrine Neoplasia (MEN) |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on published pharmacology literature, Lurbinectedin is a selective inhibitor of oncogenic transcription: it binds covalently to the DNA minor groove, recruits nucleotide excision repair (NER) machinery, and causes stalled RNA Polymerase II (RNA Pol II) complexes to collapse, generating DNA double-strand breaks. This selectively kills tumour cells that depend on high-level transcriptional activity — the core vulnerability exploited in SCLC.

Multiple Endocrine Neoplasia (MEN) is a hereditary tumour syndrome driven by germline mutations in MEN1, RET, or CDKN1B. MEN1-associated tumours (pancreatic neuroendocrine tumours, parathyroid adenomas, pituitary adenomas) exhibit altered transcriptional regulation due to loss of menin, a histone-H3K4 methyltransferase scaffold protein. In theory, RNA Pol II inhibition could disrupt the abnormal transcriptional programmes sustaining these tumours. This indirect mechanistic chain — germline MEN1 loss → transcriptional dysregulation → RNA Pol II dependency — is scientifically plausible but extremely speculative.

The practical gap is large: MEN is a heritable syndrome driven by germline loss-of-function mutations, fundamentally different from the oncogene-driven transcriptional addiction seen in SCLC. The 99.44% TxGNN score almost certainly reflects broad "neoplasm" node connectivity in the knowledge graph rather than direct pharmacological relevance. Without any preclinical, clinical, or literature evidence, the mechanistic link must be rated as very weak indirect association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Lurbinectedin has no Singapore HSA registrations as of the data cutoff (2026-06-22). The drug is marketed internationally under the brand name **Zepzelca** and holds regulatory approval in the United States (FDA, June 2020) and the European Union (EMA, 2023) for metastatic SCLC, but has not entered the Singapore market.

---

## Cytotoxicity

Lurbinectedin is an antineoplastic alkylating agent (trabectedin-class synthetic compound). The following cytotoxicity profile applies:

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — alkylating agent / selective RNA Pol II inhibitor (ecteinascidin/trabectedin class) |
| Myelosuppression Risk | High — dose-limiting toxicity is neutropenia; febrile neutropenia and thrombocytopenia reported in SCLC trials |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential (ANC nadir ~Day 15), liver function tests (ALT, AST, bilirubin), renal function, serum electrolytes |
| Handling Protection | Must follow cytotoxic drug handling and preparation regulations; NIOSH hazardous drug classification applies |

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-drug interaction data were not available in the current Evidence Pack. Given the known severe myelosuppression profile, any off-label use in non-oncology indications (e.g. rheumatoid arthritis, HIV, ALS) would carry disproportionate haematological risk that must be formally assessed before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Every predicted indication in this Evidence Pack is rated L5 with zero supporting clinical or preclinical evidence; moreover, 4 of the top 10 predictions are veterinary or non-human diseases (SIV, feline AIDS, bovine rhinotracheitis, malignant catarrh), which is a clear signal that the TxGNN knowledge graph is producing overgeneralised false-positive outputs for this drug rather than clinically actionable repurposing candidates.

**To proceed, the following is needed:**
- Retrieve the full prescribing information (FDA label / EMA SmPC) to populate safety warnings, contraindications, and drug-drug interactions
- Query DrugBank API for confirmed MOA, targets, and pharmacokinetics (especially blood-brain barrier penetration data, relevant for ALS/Mills syndrome predictions)
- Consider re-running TxGNN with a filtered disease ontology that excludes veterinary-only and non-human disease nodes to improve prediction specificity
- Conduct a targeted preclinical literature search for Lurbinectedin in MEN-associated tumours (pancreatic NETs, parathyroid carcinoma) and in tumours with MEN1 loss-of-function mutations as a biomarker
- Evaluate rheumatoid arthritis (Rank 3) only after confirming that a short-course or pulsed cytotoxic approach is being hypothesised, given that chronic dosing is pharmacologically incompatible with lurbinectedin's toxicity profile
- Apply a formal indication-plausibility filter to exclude non-human disease predictions before presenting results to clinical stakeholders
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

