---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2 Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 monoclonal antibody approved for multiple sclerosis, acting by depleting CD20-positive B lymphocytes. The TxGNN model predicts it may be effective for **HER2 Positive Breast Carcinoma**, but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a pure model-score prediction with no corroborating evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Sclerosis (based on known anti-CD20 mechanism; not confirmed in local registration data) |
| Predicted New Indication | HER2 Positive Breast Carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack (original MOA is a data gap). Based on known public information, Ocrelizumab is an anti-CD20 monoclonal antibody that depletes CD20-positive B lymphocytes, and its efficacy in multiple sclerosis is well established.

However, there is no known mechanistic pathway connecting CD20-mediated B-cell depletion to HER2-driven breast cancer signaling. The evidence pack's own rationale explicitly flags this: the high TxGNN score (99.89%) is likely an **embedding-space false positive**, arising from clustering of breast-cancer-related disease nodes in the model's latent space rather than genuine biological relevance.

This pattern is not isolated to the top candidate — all 10 ranked predictions in this pack (breast cancer subtypes, benign oral/pharyngeal neoplasms, neuroblastoma, schwannoma) share the same profile: high TxGNN scores, no clinical trials, and either no literature or literature that is topically mismatched (see Literature Evidence below). This suggests a systematic scoring artifact for this drug rather than a credible signal for any single indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for HER2 Positive Breast Carcinoma.

*Note: A literature search returned 19 hits for a related lower-ranked candidate ("breast tumor luminal A or B," rank 4), but all retrieved articles concern general B-cell biology, B-cell lymphoma, or hepatitis B vaccination — none address Ocrelizumab in breast cancer. This is assessed as keyword mismatch noise (matching on "B"/"B cell"), not supporting evidence.*

---

## Singapore Market Information

Ocrelizumab currently has no marketing authorization on record in this dataset (0 registrations, market status: not marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA-equivalent label warnings/contraindications are a flagged Blocking data gap (DG001) — this prevents a full safety pre-assessment (S1 stage) for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or valid literature evidence supports Ocrelizumab for HER2 positive breast carcinoma, and no plausible mechanistic link exists between anti-CD20 B-cell depletion and HER2/neu-driven tumor signaling. The high TxGNN score is most likely an embedding-space artifact rather than a genuine repurposing signal, and this pattern is consistent across all 10 ranked candidates for this drug.

**To proceed, the following is needed:**
- Local regulatory package insert (warnings/contraindications) — currently a Blocking data gap (DG001)
- Confirmed mechanism-of-action documentation from DrugBank or equivalent (DG002)
- Any preclinical or mechanistic rationale specifically linking CD20+ B-cell depletion to HER2-pathway biology, before this candidate can be reconsidered
- If no such rationale emerges, formally deprioritize this candidate rather than carry it forward
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

