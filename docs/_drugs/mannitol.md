---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
---

# Mannitol
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

# Mannitol: From an Undocumented Original Indication to Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)

## One-Sentence Summary

Mannitol's original approved indication is not documented in this evidence pack (a DrugBank record was located, but its indication/MOA text was not captured — flagged as data gap DG002), so no verified "from" indication can be cited here.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, with a prediction score of **99.97%**, but this is currently supported by only **0 clinical trials** and **1 non-specific review article**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — DrugBank record found, but indication/MOA text not extracted (see data gap DG002); no Singapore license records exist to source this from |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Mannitol is not available in this evidence pack. A DrugBank query returned a record (query log #2, `result_status: success`), but the MOA and original-indication text were not extracted, and this is explicitly flagged as a High-severity data gap (DG002) requiring a follow-up DrugBank API lookup. Because this specific dataset does not confirm Mannitol's approved indication, this report does not assert one.

NSIAD is a rare condition caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which produces persistent free-water retention and hyponatremia independent of actual ADH levels. Standard management relies on fluid restriction, urea, or vaptan-class V2-receptor antagonists. Mannitol, as an osmotic diuretic, could theoretically increase free-water excretion — this is the plausible mechanistic bridge that the knowledge graph appears to have captured.

However, the single supporting literature item (PMID 26706473) is a general review on diagnostic pitfalls in hyponatremia evaluation — it does not specifically discuss Mannitol's role in NSIAD, and no NSIAD-specific trials, case series, or mechanistic studies were found. The mechanistic link is therefore a plausible extrapolation rather than a demonstrated therapeutic relationship, consistent with the evidence being graded **L5 (model prediction only, no disease-specific studies)**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | General review of common diagnostic pitfalls in evaluating hyponatremia; does not specifically address Mannitol or its use in NSIAD. |

---

## Singapore Market Information

Mannitol currently has no marketing authorization on record in Singapore (0 registrations). This evidence pack contains no license entries to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/HSA label warnings and contraindications for Mannitol are not yet captured in this evidence pack (Blocking data gap DG001) — this must be resolved before any Stage 1 (S1) safety screening can proceed. No drug-drug interaction data was found (DDI query returned `not_found`, 0 results).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting evidence is a single general review that does not specifically discuss Mannitol in NSIAD, with zero disease-specific trials or case studies, placing this candidate at evidence level L5 (model prediction only). Combined with a Blocking safety data gap (DG001) and Mannitol's non-marketed status in Singapore, there is currently no basis to advance this candidate beyond initial screening.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — resolve DG001 (Blocking)
- DrugBank-sourced mechanism of action detail for Mannitol — resolve DG002 (High)
- At least one study or case report specifically evaluating Mannitol (not diuretics in general) in NSIAD or a closely related SIAD/hyponatremia cohort
- Assessment of an import/special-access pathway, since Mannitol currently holds zero marketing registrations in Singapore

*Note: This evidence pack also contains 9 additional lower-ranked predicted indications (ranks 2–10, TxGNN scores 99.66%–99.88%), all currently rated Hold with L4–L5 evidence. Several (e.g., malignant hyperthermia susceptibility, exercise-induced malignant hyperthermia, King-Denborough syndrome) appear to stem from knowledge-graph confounding via Mannitol's role as an excipient in Dantrolene injection formulations rather than direct pharmacological activity, per the rationale notes in the evidence pack.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

