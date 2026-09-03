---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 952
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: From ST-Elevation Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

> Tenecteplase is a fibrin-specific thrombolytic (tPA variant) whose established use is emergency clot lysis in ST-elevation myocardial infarction (STEMI).
> The TxGNN model's top-ranked prediction, **Posterolateral Myocardial Infarction**, scores **99.87%**,
> but this candidate has **0 clinical trials** and **0 publications** in the evidence pack — it is mechanistically identical to the drug's known use rather than a genuinely new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ST-elevation myocardial infarction (STEMI) — coronary thrombolysis (inferred from mechanistic rationale; not captured in structured Singapore registration data, as this product is not currently marketed there) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is not available (flagged as a High-severity data gap, DG002). Based on the clinical pharmacology description available in the evidence pack, Tenecteplase is a genetically engineered variant of tissue plasminogen activator (tPA) with high fibrin specificity, resistance to plasminogen activator inhibitor-1, and a longer half-life allowing single-bolus dosing. Its core approved use is thrombolysis of the occluding coronary thrombus in STEMI.

"Posterolateral myocardial infarction" is not a distinct disease with a separate pathophysiology — it is the same acute coronary thrombotic event, classified by the anatomical territory of the infarct (posterolateral wall) rather than by mechanism. TxGNN's knowledge graph appears to treat these anatomical subtypes as separate disease nodes, so the model is essentially re-discovering the drug's own approved indication under a different ontology label, rather than proposing a genuine new therapeutic use.

Mechanistically the link is sound — fibrinolysis works identically regardless of which coronary territory is infarcted — but because this is not a novel indication, no dedicated trials or subtype-specific literature exist to substantiate it as a distinct repurposing opportunity. Reviewers should treat this top-ranked result as a **taxonomy artifact** rather than a new-use signal. Within this evidence pack, rank 5 ("coronary stenosis," adjunctive intracoronary use during primary PCI) presents a more genuine and better-evidenced repurposing candidate, supported by a completed Phase 2 RCT (NCT00604695, n=40) and corroborating literature (e.g., PMID 31870492).

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Tenecteplase currently has **no registration records** in the Singapore regulatory dataset (0 licenses; market status: Not Marketed). No approved local product/indication text is available for extraction.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** The absence of safety data here is itself a significant finding — key warnings, contraindications, and drug-drug interaction data are all marked as data gaps (DG001, Blocking severity). Tenecteplase carries substantial bleeding/hemorrhage risk as a thrombolytic; a formal safety evaluation cannot proceed without TFDA/manufacturer label data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked candidate is not a genuinely new indication but an anatomical subtype of the drug's existing approved use (STEMI), with zero supporting trials or literature at that granularity.
- A Blocking-severity safety data gap (DG001 — no TFDA warnings/contraindications available) prevents even an initial (S1) safety assessment, which is mandatory before any repurposing candidate can advance regardless of mechanistic plausibility.

**To proceed, the following is needed:**
- Retrieve TFDA/manufacturer label data (warnings, contraindications, DDI) to resolve DG001 before any S1 safety evaluation can be completed.
- Retrieve confirmed DrugBank MOA data to resolve DG002 and support formal mechanistic-linkage scoring.
- Re-scope the repurposing question away from anatomical MI subtypes (ranks 1–3) toward genuinely distinct, evidence-backed candidates — most notably **rank 5 (coronary stenosis / adjunctive intracoronary use in primary PCI)**, which has an actual completed Phase 2 RCT and multiple supporting publications, and warrants a dedicated S2-stage review.
- Disregard ranks 6–10 (chromosomal/hematologic conditions) as likely graph-embedding noise with no plausible mechanistic link and no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

