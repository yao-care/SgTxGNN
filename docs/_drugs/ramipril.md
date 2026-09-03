---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 841
evidence_level: L5
indication_count: 10
---

# Ramipril
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

# Ramipril: From Unspecified Indication to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Ramipril's original indication is not documented in the current evidence pack (the drug is not marketed in Singapore and no license records exist). The TxGNN model predicts a possible new indication for **Pulmonary Hypertension with Unclear Multifactorial Mechanism**, but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only signal at this stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license/indication data in evidence pack |
| Predicted New Indication | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only, no clinical or literature support) |
| Singapore Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the repurposing rationale embedded in the evidence pack, Ramipril is understood to be an **ACE inhibitor** acting on the renin-angiotensin-aldosterone system (RAAS), which regulates vascular tone and blood pressure. The top-ranked prediction links this RAAS-modulating mechanism to pulmonary hypertension, but the evidence pack itself explicitly notes this connection is inferred purely from graph co-occurrence patterns in TxGNN, without any specific pathophysiological explanation for why RAAS inhibition would address a multifactorial, unclear-mechanism form of pulmonary hypertension.

No clinical trials, ICTRP registrations, or PubMed literature were retrieved for this specific candidate, so there is no external evidence to corroborate or refute the mechanistic link. It is worth noting that among the 10 candidates in this evidence pack, later-ranked indications — particularly **cerebral artery occlusion** (rank 10, L3 evidence with a completed Phase 2 human trial and a Ramipril-specific comparative cerebral blood flow study) — carry substantially stronger supporting evidence than this top-ranked candidate. The high TxGNN score for pulmonary hypertension should therefore be interpreted as a graph-embedding signal rather than a validated pharmacological hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No marketing authorization records found. Ramipril's `market_status` is recorded as **未上市 (Not marketed)** with **0 total licenses**, so no product/dosage form/indication data is available for Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not available in the current evidence pack; TFDA label warnings/contraindications are flagged as a **Blocking** data gap, DG001, preventing initial safety screening.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (pulmonary hypertension with unclear multifactorial mechanism) has an L5 evidence level — a high TxGNN score with zero supporting clinical trials or literature. Combined with a Blocking data gap on safety labeling (DG001) and a High-severity gap on mechanism of action (DG002), there is insufficient basis to advance this candidate beyond the hypothesis stage.

**To proceed, the following is needed:**
- TFDA/regulatory label (warnings, contraindications) to complete the S1 safety pre-screen (DG001)
- DrugBank-sourced mechanism of action data to assess mechanistic plausibility (DG002)
- Targeted literature/clinical trial search specific to Ramipril and pulmonary hypertension (current literature results were generic hypoxia-biology papers, not drug-specific)
- Consider re-evaluating **cerebral artery occlusion** (rank 10) as a higher-priority candidate, given its existing Phase 2 human trial and Ramipril-specific comparative pharmacology data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

