---
layout: default
title: Racecadotril
parent: 僅模型預測 (L5)
nav_order: 838
evidence_level: L5
indication_count: 10
---

# Racecadotril
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

# Racecadotril: From Acute Diarrhea to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Racecadotril is an enkephalinase inhibitor clinically used to treat acute diarrhea. The TxGNN model predicts potential efficacy for **polyclonal hyperviscosity syndrome**, but this signal is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute diarrhea (based on drug's known pharmacological classification; no Singapore regulatory filing available) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 97.72% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for racecadotril in DrugBank. Based on known pharmacological information, racecadotril is an enkephalinase (neutral endopeptidase) inhibitor that reduces intestinal hypersecretion; its established clinical use and mechanism are confined to the gastrointestinal tract (acute diarrhea).

The evidence pack's own mechanistic analysis for this candidate explicitly states that **no biological or pharmacological link** has been identified between enkephalinase inhibition and polyclonal hyperviscosity syndrome, a plasma-protein/blood-viscosity disorder. The prediction arises purely from TxGNN knowledge-graph embedding similarity, not from any shared target, pathway, or clinical observation.

This pattern is not isolated: all 10 top-ranked candidates for racecadotril (scores clustering 94–98%) — including monoclonal gammopathy, congenital analbuminemia, septicemic plague, and acute cystitis — are rated L5 with zero clinical trials, zero literature, and explicit statements of no mechanistic plausibility. This suggests the current candidate list for this drug is exploratory-only and not yet actionable.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Racecadotril has no marketing authorization in Singapore (0 registrations). No license or approved-indication data is available to compare against the predicted new indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication has no clinical trial or literature support, and the evidence pack itself flags an absence of mechanistic plausibility. Combined with L5 evidence level and no Singapore market presence, this candidate does not currently meet the threshold for further evaluation.

**To proceed, the following is needed:**
- Confirmed original MOA and approved indication for racecadotril (currently a High-severity data gap, DG002)
- TFDA/HSA package insert warnings and contraindications (currently a Blocking data gap, DG001) — required before any S1 safety screening can proceed
- Independent mechanistic or preclinical evidence linking enkephalinase inhibition to hyperviscosity/hematological pathophysiology, if this candidate is to be reconsidered
- Re-screening of the full candidate list for signals with at least L3 evidence, since all current top-10 predictions are L5-only
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

