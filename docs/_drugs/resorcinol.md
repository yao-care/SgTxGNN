---
layout: default
title: Resorcinol
parent: 僅模型預測 (L5)
nav_order: 853
evidence_level: L5
indication_count: 10
---

# Resorcinol
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

# Resorcinol: From Topical Keratolytic Use to Acne Keloid

## One-Sentence Summary

Resorcinol is a traditional topical keratolytic and antibacterial agent, historically used for acne and minor dermatological lesions, though no formal indication record exists for this market. The TxGNN model predicts it may be effective for **Acne Keloid**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on file (drug not registered/marketed locally); historically used as a topical keratolytic/antiseptic agent |
| Predicted New Indication | Acne Keloid |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, Resorcinol is a topical keratolytic and mild antibacterial agent traditionally used for acne and other minor dermatological lesions, acting by softening and dissolving the outer layer of keratin.

Acne keloid (acne keloidalis nuchae) shares a pathological overlap with acne in terms of keratin hyperplasia and follicular inflammation, which gives some superficial biological plausibility to this prediction. However, this connection is inferential rather than confirmed — there is no direct study linking Resorcinol to this specific condition.

It is worth noting that the same TxGNN run also surfaced several other high-scoring candidates (e.g., rheumatoid vasculitis, ankylosing spondylitis, hypermobility of coccyx) for which the reviewer explicitly flagged the mechanistic link as weak or likely a knowledge-graph artifact. This context suggests the model's high scores in this batch should be interpreted cautiously, and acne keloid — while the most plausible of the group — still lacks any confirmatory evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Resorcinol is currently **not registered or marketed** in Singapore. No license records are available for this product.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key regulatory warnings and contraindications for this product have not yet been retrieved — this is flagged as a blocking data gap for safety review.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests solely on a TxGNN model score (L5, no clinical trials or literature), and the drug is not currently registered in this market. Combined with missing mechanism-of-action and safety/label data, there is insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- Local regulatory warnings and contraindications (TFDA label PDF) — currently blocking
- Confirmed mechanism of action (DrugBank API query)
- Preclinical or case-level evidence specifically linking Resorcinol to acne keloid
- Assessment of local market entry pathway, since the drug is not currently registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

