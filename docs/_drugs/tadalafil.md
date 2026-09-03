---
layout: default
title: Tadalafil
parent: 僅模型預測 (L5)
nav_order: 938
evidence_level: L5
indication_count: 10
---

# Tadalafil
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

# Tadalafil: From Unregistered Indication to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tadalafil is a PDE5 inhibitor whose approved uses (based on general pharmacological knowledge embedded in this evidence pack) rely on inhibiting cGMP degradation to relax vascular and smooth muscle. The TxGNN model's top-ranked prediction for this drug is **Ambras type hypertrichosis universalis congenita**, a rare congenital hair-overgrowth syndrome — but this pairing is supported by **zero clinical trials and zero publications**, and the model's own rationale states it is a pure statistical artifact with no known mechanistic basis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no market authorization or approved indication text on record in Singapore |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed drug-level mechanism-of-action data is flagged as a data gap in this pack. However, mechanistic context recoverable from the evidence pack's rationale fields indicates Tadalafil is a PDE5 inhibitor: it blocks degradation of cGMP, producing vascular and smooth muscle relaxation, with known clinical relevance to the corpus cavernosum and pulmonary vasculature (the same rationale text notes Tadalafil is already used in WHO Group 1 pulmonary arterial hypertension).

Ambras type hypertrichosis universalis congenita is a congenital, genetically-driven disorder of excessive hair growth. There is no established biological pathway connecting PDE5/cGMP signaling to the genetic regulation of hair follicle overgrowth in this condition. The evidence pack's own mechanistic assessment for this prediction states explicitly that the association is "purely a statistical relationship derived from the TxGNN knowledge graph, without any mechanistic or clinical basis."

In other words, despite a very high model confidence score (99.98%), this particular top-ranked prediction should not be interpreted as a credible repurposing signal — a high TxGNN score reflects graph-embedding similarity, not biological plausibility, and here the two diverge substantially.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Safety Considerations

Please refer to the package insert for safety information. Note: official label warnings and contraindications for this drug have not yet been obtained and are currently a blocking data gap for any formal safety evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Ambras type hypertrichosis universalis congenita) has no clinical trial or literature support, and the model's own rationale confirms it lacks mechanistic plausibility — this is a statistical artifact, not a repurposing signal. The drug is also not currently marketed in Singapore (0 registrations), and blocking safety data (official label warnings/contraindications) is unavailable, preventing entry into a formal safety review (S1).

**To proceed, the following is needed:**
- Obtain official label warnings and contraindications from HSA (or equivalent regulatory source) to close the blocking data gap before any safety-stage evaluation
- Obtain a verified, sourced mechanism-of-action reference for Tadalafil to close the mechanism data gap
- If this candidate pack is revisited, evaluate rank 7 (kyphoscoliotic heart disease, L4/S1, "Research Question") separately — it is the only candidate in this pack with a biologically coherent link to Tadalafil's known pulmonary vasodilatory activity, though evidence remains preclinical/theoretical
- Treat the migraine-related candidates (ranks 8–9) as safety signals rather than efficacy leads — available literature associates Tadalafil with *inducing* migraine aura, not treating it
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

