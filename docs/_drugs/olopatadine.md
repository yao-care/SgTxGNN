---
layout: default
title: Olopatadine
parent: 僅模型預測 (L5)
nav_order: 730
evidence_level: L5
indication_count: 10
---

# Olopatadine
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

# Olopatadine: From Allergic Conjunctivitis to Rosacea Conjunctivitis

## One-Sentence Summary

Olopatadine is a well-known H1-antihistamine / mast cell stabilizer eye drop, publicly documented as being used for allergic conjunctivitis (formal indication text is not available in the current dataset). The TxGNN model predicts it may be effective for **Rosacea Conjunctivitis**, but this direction currently has **0 clinical trials** and **0 publications** supporting it — the prediction score is high, but it stands entirely on the model itself.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured data (drug not marketed in Singapore); publicly known as an H1-antihistamine/mast cell stabilizer used for allergic conditions (e.g., allergic conjunctivitis) |
| Predicted New Indication | Rosacea Conjunctivitis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for olopatadine is not available in this dataset (data gap). Based on publicly known pharmacology, olopatadine is an H1-antihistamine and mast cell stabilizer whose action targets IgE-mediated allergic reactions — this is consistent with its known clinical use in allergic conjunctivitis/rhinitis.

Rosacea conjunctivitis, however, is pathologically distinct: it is primarily driven by meibomian gland dysfunction and chronic vascular inflammation rather than an IgE-mediated hypersensitivity response. The evidence pack's own mechanistic assessment for this candidate explicitly flags this as a **weak** mechanistic link, since olopatadine's antihistamine action does not directly address the vascular/glandular inflammatory pathway thought to drive rosacea conjunctivitis.

The high TxGNN score (99.41%) reflects a strong signal in the knowledge-graph embedding space, but this is a pure model-based prediction (rank 7282) with no corroborating clinical trials or literature — placing it at Evidence Level L5. Several lower-ranked candidates in this batch (e.g., punctate epithelial keratoconjunctivitis, blepharoconjunctivitis) at least have some allergy-related literature context, which the top-ranked rosacea conjunctivitis candidate lacks entirely.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies solely on the TxGNN model score with no clinical trial or literature support, and the pack's own mechanistic analysis rates the drug–indication link as weak (rosacea conjunctivitis is not primarily an IgE-mediated condition). This is insufficient evidence to advance beyond model prediction (L5/S0).

**To proceed, the following is needed:**
- TFDA/HSA label data (warnings, contraindications) — currently a **Blocking** data gap (DG001), required before any S1 safety screening
- Confirmed mechanism of action from DrugBank — currently a **High**-severity data gap (DG002)
- Targeted preclinical or mechanistic studies linking histamine/mast cell pathways to rosacea conjunctivitis pathophysiology
- Consideration of re-prioritizing toward candidates with existing literature signal (e.g., blepharoconjunctivitis, punctate epithelial keratoconjunctivitis, parasitic conjunctivitis), which at least offer indirect allergy-related evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

