---
layout: default
title: Testosterone Propionate
parent: 僅模型預測 (L5)
nav_order: 963
evidence_level: L5
indication_count: 10
---

# Testosterone Propionate
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

# Testosterone Propionate: From No Recorded Indication to Urethral Obstruction Sequence

## One-Sentence Summary

Testosterone propionate has no approved indication on record in this evidence pack — the drug is not currently marketed in Singapore. The TxGNN model predicts a possible association with **Urethral Obstruction Sequence** (score 93.26%), but this prediction is currently supported by **zero clinical trials and zero publications**, placing it at the lowest evidence tier (model output only).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore registration on file, and `original_indications` is empty in the evidence pack |
| Predicted New Indication | Urethral Obstruction Sequence |
| TxGNN Prediction Score | 93.26% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (`original_moa` is a data gap). Without confirmed MOA or an on-file original indication, there is no established pharmacological basis to connect testosterone propionate to urethral obstruction sequence.

Urethral obstruction sequence is a congenital, structural condition (similar in presentation to Potter sequence) arising from prenatal urinary tract obstruction. The candidate's own rationale notes there is **no known direct therapeutic mechanism** linking androgen therapy to this condition, and the prediction is driven purely by the knowledge-graph embedding, with no clinical trial or literature signal to corroborate it. For context, other candidates further down this drug's prediction list have marginally more supporting material — e.g., testicular regression syndrome (rank 3, one older case-series PMID 6775612) and freemartinism (rank 5, three animal-behavior studies) — but none of these reach clinical relevance either. This suggests the overall repurposing evidence base for testosterone propionate in this candidate set is very weak across the board.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The underlying data pack flags TFDA/HSA warnings and contraindications as a **Blocking**-severity gap (DG001) — this alone is sufficient to prevent any S1 safety evaluation for this candidate, independent of the efficacy evidence gap above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score (93.26%) is high, but it is unsupported by any clinical trials or literature (Evidence Level L5), and no mechanistic rationale connects testosterone propionate to urethral obstruction sequence. Combined with a Blocking-severity safety data gap, this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA/HSA package insert with full warnings and contraindications (DG001 — Blocking)
- Confirmed mechanism of action from DrugBank (DG002 — High)
- Identification of testosterone propionate's actual approved indication(s), since none are currently on record
- Any preclinical or mechanistic evidence specifically linking androgen therapy to urethral obstruction pathophysiology, given the current rationale explicitly states no known direct mechanism exists
- Re-screening of lower-ranked candidates in this set (e.g., testicular regression syndrome) once the above data gaps are closed, as they may offer a marginally stronger — though still weak — starting point
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

