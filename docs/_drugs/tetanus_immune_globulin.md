---
layout: default
title: Tetanus Immune Globulin
parent: 僅模型預測 (L5)
nav_order: 965
evidence_level: L5
indication_count: 10
---

# Tetanus Immune Globulin
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

# Tetanus Immune Globulin: From Tetanus Prophylaxis to Diabetic Cataract

## One-Sentence Summary

Tetanus Immune Globulin (TIG) is a polyclonal antibody preparation used for passive immunization against tetanus toxin (tetanospasmin). The TxGNN model's top-ranked prediction is **Diabetic Cataract**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own generated rationale explicitly states there is no known mechanistic link — this is a model-score-only signal, not a validated biological hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tetanus prophylaxis / treatment (passive immunization) — not documented in Singapore regulatory data, as this product is not marketed locally |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.61% (absolute score high, but ranks only 13,474th among all candidate diseases — low relative differentiation) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Tetanus Immune Globulin is not available. Based on general pharmacological knowledge, TIG is a polyclonal antibody product that neutralizes circulating tetanus toxin; it is administered for post-exposure prophylaxis after injury or as adjunctive treatment for active tetanus infection. It has no established role in ocular or metabolic pathways.

The model's own repurposing rationale for the top prediction states there is "no known association" between TIG's toxin-neutralizing mechanism and the lens protein glycation/oxidation pathways implicated in diabetic cataract. In other words, this candidate is a pure knowledge-graph embedding signal without any accompanying mechanistic support.

More concerning, 8 of the top 10 predicted indications are cataract subtypes or staging terms (e.g., diabetic cataract, tetanic cataract, cortical cataract, senile cataract, mature/immature cataract), and the rationale for rank 2 ("tetanic cataract") explicitly flags a likely **data artifact**: lexical confusion between the drug name "tetanus" and the historical disease term "tetanic" (a hypocalcemia-related cataract unrelated to tetanus toxin). This raises meaningful concern that the entire cataract-prediction cluster for this drug may be driven by textual/embedding similarity rather than genuine biological signal, and should not be taken at face value without independent mechanistic or preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Tetanus Immune Globulin currently has no marketing authorization in Singapore (0 registrations). No license records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA/regulatory warning and contraindication data for this product is currently a blocking data gap (DG001), which prevents a formal S1 safety evaluation from being conducted.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (diabetic cataract) has no supporting clinical trials, no literature, and no mechanistic plausibility per the model's own rationale. Combined with strong evidence that at least one nearby prediction (tetanic cataract) may reflect a name-similarity artifact rather than a real signal, and the fact that this drug is not currently marketed in Singapore, there is insufficient basis to advance this candidate beyond S0.

**To proceed, the following is needed:**
- TFDA/regulatory warnings and contraindication data (blocking gap DG001) to enable a formal safety evaluation
- Mechanism of action (MOA) detail from DrugBank or other authoritative source (gap DG002)
- Independent mechanistic or preclinical investigation into any plausible TIG–cataract pathway, given the model provides none
- A review to rule out embedding/name-similarity artifacts across the full predicted-indication list before further evidence collection is invested
- Assessment of registration feasibility in Singapore, since the product is currently not marketed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

