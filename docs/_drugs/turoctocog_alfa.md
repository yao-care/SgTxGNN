---
layout: default
title: Turoctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 1026
evidence_level: L5
indication_count: 10
---

# Turoctocog Alfa
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

# Turoctocog alfa: From Haemophilia A to Primary Release Disorder of Platelets

## One-Sentence Summary

> Turoctocog alfa is a recombinant Factor VIII replacement product, conventionally used to control and prevent bleeding in **Haemophilia A**.
> The TxGNN model predicts it may be effective for **primary release disorder of platelets**,
> but this candidate currently has **0 clinical trials** and **0 publications** supporting it, and the model's own mechanistic rationale flags the biological plausibility as weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Haemophilia A (known drug class fact; not present in Singapore registry data, as the product is not yet marketed) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the registry input (DrugBank query pending — see Data Gap DG002). Based on known information, Turoctocog alfa is a recombinant Factor VIII (FVIII) concentrate that acts on the intrinsic coagulation cascade, replacing deficient clotting factor activity in Haemophilia A. Its efficacy in reducing bleeding episodes in FVIII-deficient patients is well established.

The predicted new indication, primary release disorder of platelets (a platelet storage pool disease), involves a defect in platelet granule content release during activation — a mechanism entirely upstream and independent of the coagulation cascade that FVIII participates in. The Evidence Pack's own mechanistic assessment for this candidate explicitly states that FVIII "does not participate in platelet activation or granule release" and that the high TxGNN score likely reflects **topological similarity between "bleeding tendency" nodes in the knowledge graph rather than genuine biological plausibility**.

Among the ten candidates returned, one indication — **acquired coagulation factor deficiency** (rank 5) — has a materially stronger mechanistic rationale, since acquired FVIII deficiency (e.g., acquired haemophilia A with anti-FVIII antibodies) is a recognized on-label-adjacent use for FVIII replacement. However, this candidate is currently supported by no clinical trials or literature either, and the disease label is too broad to confirm the specific subtype implied. Overall, the top-ranked prediction should be treated as a model-generated hypothesis requiring independent biological validation before any further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Turoctocog alfa currently has **no registrations** in Singapore (`total_licenses: 0`, market status: 未上市 / Not marketed). No authorization records, product names, or approved indication text are available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are currently unavailable — see Data Gap DG001, classified as Blocking for safety pre-screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (primary release disorder of platelets) is supported only by a TxGNN model score (L5, S0) with zero clinical trials or literature, and the mechanistic review itself indicates the biological rationale is weak, likely driven by knowledge-graph topology rather than true pharmacological relevance. The drug is also not currently marketed in Singapore, and safety data (DG001, Blocking) required for even a preliminary S1 safety screen is missing.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain product label warnings/contraindications, e.g., via HSA/TFDA-equivalent label filing
- Resolve DG002 (High): confirm mechanism of action via DrugBank API to properly assess mechanistic linkage
- If pursuing further, prioritize re-evaluation of the mechanistically stronger candidate **acquired coagulation factor deficiency** (rank 5) with a narrower disease definition (e.g., acquired haemophilia A) rather than the current top-ranked candidate
- Clarify rank 8 "flood factor deficiency" — likely an ontology/naming artifact possibly meaning combined Factor V/VIII deficiency — before considering it as a candidate
- Independent biological/preclinical evidence before any clinical evaluation is initiated, given the complete absence of trials or literature across all ten candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

