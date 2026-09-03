---
layout: default
title: Salicylic Acid
parent: 僅模型預測 (L5)
nav_order: 886
evidence_level: L5
indication_count: 10
---

# Salicylic Acid
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

# Salicylic Acid: From Topical Dermatological Use to Papillary Conjunctivitis (Predicted)

## One-Sentence Summary

Salicylic acid is a long-established topical keratolytic/anti-inflammatory agent; no formal original indication is on file in this evidence pack because the drug is not currently marketed in Singapore.
The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**, but this prediction is currently supported by **0 clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license record on file |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, salicylic acid is a keratolytic agent with mild local anti-inflammatory activity, commonly used topically for dermatological conditions such as acne, warts, calluses, and psoriasis. However, no original indication is formally recorded here, and the drug has no active market authorization in Singapore.

The TxGNN rationale for the top-ranked candidate notes that salicylic acid's keratolytic and local anti-inflammatory properties could theoretically extend to allergic/inflammatory conjunctival surface reactions such as papillary conjunctivitis. This is described explicitly as an indirect, mechanism-only association — there is no ophthalmic formulation, dosing, or safety data to support ocular use, so the link should be treated as a pure computational prediction rather than a clinically grounded hypothesis.

It is also worth noting that most of the remaining top-10 predictions (e.g., various skeletal/craniofacial dysplasia syndromes) were flagged by the model's own rationale as likely knowledge-graph noise, with no plausible mechanistic connection to salicylic acid. Only rank 5 (rosacea conjunctivitis) and rank 10 (spondyloarthropathy susceptibility) carry comparable theoretical plausibility to the top candidate — and like it, both lack any clinical or literature evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

No Singapore (HSA) market authorizations are on file for this drug — Salicylic acid is currently **not marketed** in Singapore under this evidence pack (0 licenses registered).

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-drug interaction data are currently unavailable and flagged as a Blocking data gap — this must be resolved before any safety evaluation can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence level is L5 — a model prediction only, with no clinical trials, no literature, and no ophthalmic formulation or safety data. Combined with the drug's non-marketed status in Singapore and blocking gaps in warning/contraindication data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (Blocking gap — required before any S1 safety screening)
- Mechanism of action data via DrugBank API (High-priority gap — needed for mechanistic plausibility assessment)
- Preclinical or in vitro evidence for anti-inflammatory activity on conjunctival/ocular tissue
- Ophthalmic formulation and route-compatibility data (topical keratolytic formulations are not equivalent to ocular-safe formulations)
- Any real-world or case-report evidence linking salicylic acid (not aspirin) to ocular surface inflammatory conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

