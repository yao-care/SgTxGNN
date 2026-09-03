---
layout: default
title: Tucatinib
parent: 僅模型預測 (L5)
nav_order: 1025
evidence_level: L5
indication_count: 10
---

# Tucatinib
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

# Tucatinib: From HER2-Positive Breast Cancer to Migraine Disorder

## One-Sentence Summary

Tucatinib is a HER2 tyrosine kinase inhibitor used in the treatment of HER2-positive breast cancer.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with a prediction score of **98.62%**,
but **no clinical trials or published literature** currently support this specific drug-disease pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (based on known drug class; not formally recorded in the Singapore regulatory dataset as this drug is unmarketed) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Tucatinib is not available in this evidence pack. Based on known information, Tucatinib is a small-molecule HER2 tyrosine kinase inhibitor, approved for HER2-positive breast cancer, and works by blocking HER2 receptor signalling to suppress tumour cell proliferation.

There is no known mechanistic link between HER2 signalling and migraine pathophysiology, which is primarily driven by the trigeminovascular system and CGRP pathway. The evidence pack's own rationale for this candidate states explicitly that the high TxGNN score reflects **knowledge-graph topological similarity**, not biological plausibility, and that biological support is lacking.

This pattern repeats across nearly all of the top 10 predicted indications for this drug (migraine variants, multiple endocrine neoplasia, nephrogenic syndrome of inappropriate antidiuresis, pulmonary hypertension, homozygous familial hypercholesterolemia, kyphoscoliotic heart disease, Prinzmetal angina, rheumatoid arthritis) — each rationale independently notes the absence of a credible mechanistic connection to HER2 inhibition. This is a case where the TxGNN score is high, but the supporting evidence and mechanistic rationale are weak across the board.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tucatinib is not currently marketed in Singapore, and no registration records (SIN numbers) are available in the evidence pack.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (HER2 tyrosine kinase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (migraine disorder) has no clinical trial or literature support, and the evidence pack's own mechanistic analysis assesses the TxGNN score as a knowledge-graph topological artifact rather than a biologically grounded signal. None of the top 10 predicted indications for this drug reach an evidence level above L4, and even the L4 candidates (multiple endocrine neoplasia, migraine susceptibility, rheumatoid arthritis) are supported only by tangentially related trials or reviews that do not mention Tucatinib specifically.

**To proceed, the following is needed:**
- TFDA/local regulatory safety labeling (package insert warnings and contraindications) — currently a blocking data gap
- Confirmed mechanism of action data from DrugBank or primary literature
- Drug-specific preclinical or clinical evidence connecting HER2 inhibition to any of the predicted indications before advancing beyond S0
- If pursuing further, re-review the rheumatoid arthritis (rank 10) and MEN (rank 2) candidates first, as they are the only ones with any associated literature/trials, even though relevance is currently graded low (C) or non-specific
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

