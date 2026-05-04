---
layout: default
title: 8 085 Mg Of Ivabradine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
---

# 8 085 Mg Of Ivabradine Hydrochloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **0** 個
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

# Ivabradine: Evaluation Report — Insufficient Data for Repurposing Assessment

---

## One-Sentence Summary

The Evidence Pack submitted contains a malformed drug entry ("8.085 MG OF IVABRADINE HYDROCHLORIDE)"), which appears to be a dosage descriptor incorrectly captured as an INN — the actual active ingredient is **ivabradine** (a selective funny current Ih inhibitor used in heart failure and stable angina).
No TxGNN-predicted indications were returned for this entry, and Singapore regulatory registration records are absent.
As a result, **a full repurposing evaluation cannot be completed**; the data gaps below must be resolved before assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none present) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why This Report Cannot Be Completed

The Evidence Pack contains a critical data quality issue at the drug identification stage:

**Problem — Malformed INN field:**
The `drug.inn` field contains `"8.085 MG OF IVABRADINE HYDROCHLORIDE)"` — a dosage strength descriptor, not an INN. This string is the declared content of one Procoralan/Corlentor film-coated tablet (8.085 mg ivabradine hydrochloride = 7.5 mg ivabradine base). The upstream data pipeline appears to have concatenated the dosage line into the ingredient name field during parsing.

**Downstream consequences:**
- The DDI query returned no results (the malformed string matched no known drug)
- DrugBank returned 1 result (likely a partial fuzzy match), but no `drugbank_id` was stored
- No original indications were extracted
- No predicted indications were generated — `predicted_indications` is an empty array
- All safety fields are `[Data Gap]`

Because `predicted_indications` is empty, the sections for **Why is This Prediction Reasonable**, **Clinical Trial Evidence**, **Literature Evidence**, **Cytotoxicity**, and **Conclusion and Next Steps** cannot be populated with evidence-based content.

---

## Singapore Market Information

No registered products found for this entry.

> Based on international data, ivabradine is marketed globally as **Procoralan** (Servier) and **Corlanor** (Amgen/US). If ivabradine is correctly identified and re-queried, Singapore HSA registration records should be searched under the INN `ivabradine` or brand name `Procoralan`.

---

## Safety Considerations

> Please refer to the package insert for safety information. No safety data was retrievable for this malformed drug entry.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug entry is structurally invalid — the INN field contains a dosage string rather than a drug name, which has propagated as a data error through every downstream pipeline stage, resulting in zero predicted indications and zero safety data.

**To proceed, the following is needed:**

- **Fix the data pipeline** — identify the upstream parsing step that merged dosage text into the INN field, and correct the record so that `drug.inn = "ivabradine"` (or `"ivabradine hydrochloride"`)
- **Re-run TxGNN prediction** against the corrected INN to obtain `predicted_indications`
- **Re-query DrugBank** with `ivabradine` to retrieve `drugbank_id`, `original_moa`, and toxicity data
- **Re-query Singapore HSA** with the corrected drug name to populate `taiwan_regulatory` fields
- **Re-query DDI database** with `ivabradine` to retrieve interaction data
- Once all above are resolved, resubmit a corrected Evidence Pack for a complete L1–L5 repurposing evaluation

---

> ⚠️ **Data Quality Note:** This report was generated from an Evidence Pack with a Blocking data gap (DG001) and a High-severity gap (DG002). The drug INN field contains a dosage descriptor rather than a valid drug name, rendering all downstream predictions and safety lookups invalid. No clinical or regulatory conclusions should be drawn from this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

