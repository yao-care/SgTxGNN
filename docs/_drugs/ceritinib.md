---
layout: default
title: Ceritinib
parent: Low Evidence (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Ceritinib
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ceritinib: From ALK-Positive Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Ceritinib is an oral ALK inhibitor used for ALK-positive non-small cell lung cancer (NSCLC). The TxGNN model predicts it may be effective for **gingival fibromatosis** with a very high score, but **0 clinical trials** and **0 publications** support this specific prediction. It is a model-only signal and should be held.

The original indication comes from the retrieved literature (for example the ASCEND-4 Phase 3 trial), not from the Singapore licence record, whose indication text is blank.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALK-positive NSCLC (inferred from the literature, not stated in the licence record) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. From the supplied analysis, ceritinib is an ALK/IGF-1R/ROS1 kinase inhibitor. Its efficacy in ALK-rearranged NSCLC is well established.

**The data do not support a mechanistic link to gingival fibromatosis.** No ALK-driven pathology is established for this condition. The TxGNN score of 99.86% does not discriminate well, because the other top candidates for this drug all score about 0.998. It should be read as a weak knowledge-graph association rather than a meaningful signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14776P | ZYKADIA CAPSULE 150mg | Capsule | Not stated in the licence record |

The manufacturers listed are Novartis Pharma Stein AG and Sandoz S.R.L. The route of administration is oral.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | ECG/QT interval and respiratory symptoms (from the literature signals below); other parameters per the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned no records.
- **Safety signals in the retrieved literature** (background only, not the label):
  - QT prolongation
  - Hypersensitivity, including a case report with diffuse infiltrative lung disease, pericarditis and pleural effusion
  - Gastrointestinal and other adverse events, discussed in ceritinib management reviews and meta-analyses

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no trials, no literature and no documented mechanistic link. It is supported only by a non-discriminating model score.

Other candidates for ceritinib have some retrieved evidence, but it is indirect:
- **Lung benign neoplasm** has 20 publications, all on ALK-positive NSCLC, which is on-label oncology evidence.
- **Lung germ cell tumor** has one Phase 0/II CNS-penetration study and ALK-related neuroblastoma reports.

None of this shows benefit in the predicted diseases.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications, which are currently a blocking gap for safety screening
- Detailed mechanism of action data (DrugBank)
- Biological evidence that ALK, IGF-1R or ROS1 signalling contributes to gingival fibromatosis
- A check of the disease mapping and a targeted literature search for the predicted disease
- Confirmation of route and formulation suitability, since gingival disease may favour a local route and only an oral capsule is registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

