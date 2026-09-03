---
layout: default
title: Perindopril
parent: 僅模型預測 (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
---

# Perindopril
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

# Perindopril: From Hypertension (ACE Inhibitor Class) to Malignant Renovascular Hypertension

## One-Sentence Summary

Perindopril is an ACE inhibitor; a confirmed original approved indication is not present in this evidence pack (registration and MOA fields are marked as data gaps). The TxGNN model predicts potential efficacy for **Malignant Renovascular Hypertension**, but this is currently supported by **0 clinical trials** and **0 publications** — it is a pure model prediction with a mechanistically double-edged risk profile (ACE inhibitors are the standard antihypertensive class for renovascular hypertension, yet are contraindicated in bilateral renal artery stenosis).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no registered license or `original_indications` entry in this dataset; drug class (ACE inhibitor) is typically used for hypertension, but this is not confirmed by registry data |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature identified) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this candidate (flagged as a High-severity data gap — DG002). Based on known pharmacological class information, Perindopril is an ACE inhibitor, and this class is a well-established treatment for hypertension broadly, including certain renovascular hypertension presentations, by suppressing angiotensin II formation and reducing afterload.

However, the relationship between ACE inhibitor pharmacology and malignant renovascular hypertension is bidirectional: the same mechanism that lowers blood pressure in renin-dependent hypertension can precipitate acute renal failure in patients with bilateral (or solitary-kidney unilateral) renal artery stenosis, since glomerular filtration in the affected kidney(s) depends on angiotensin II-mediated efferent arteriolar constriction. This means the mechanistic link is real but carries an inherent contraindication risk that must be actively ruled out before any use in this population, and it is not, by itself, evidence of therapeutic benefit.

No clinical trial or literature evidence in this evidence pack directly evaluates Perindopril in malignant renovascular hypertension — the prediction rests entirely on TxGNN's knowledge-graph inference.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

No registration records found in this dataset — Perindopril has 0 licenses on record and a market status of "Not Marketed."

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This is a Blocking-severity data gap — DG001. Key warnings, contraindications, and drug interaction data were not found in this evidence pack and should be retrieved from the official label before any safety assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (malignant renovascular hypertension) has zero supporting clinical trials or literature, and the underlying mechanism carries a known contraindication risk (bilateral renal artery stenosis) rather than a clean therapeutic rationale. Core drug-level data — original indication, MOA, and label safety information — are all missing from this evidence pack, so this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- Confirmed original indication and registration status (via HSA/official label lookup)
- DrugBank MOA data (DG002)
- Official label warnings and contraindications (DG001, Blocking)
- Formal evaluation of renal artery stenosis status as an exclusion criterion if this indication is pursued further

**Additional context:** All 10 TxGNN-predicted indications for Perindopril in this evidence pack (ranks 1–10, covering renovascular/pulmonary hypertension variants, rare genetic syndromes, cor pulmonale, polydipsia, and TMJ ankylosis) received a "Hold" recommendation — the associated literature hits were largely keyword-level mismatches (e.g., hypoxia biology, congenital ocular anomalies) rather than substantive clinical evidence for Perindopril in those conditions.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

