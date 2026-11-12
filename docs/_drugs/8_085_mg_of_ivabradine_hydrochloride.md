---
noindex: true
sitemap: false
layout: default
title: 8 085 Mg Of Ivabradine Hydrochloride
parent: Low Evidence (L5)
nav_order: 17
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# 8 085 Mg Of Ivabradine Hydrochloride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Ivabradine: Evaluation Report — Insufficient Data for Repurposing Assessment
{: .text-alpha }

---

## One-Sentence Summary

The Evidence Pack submitted contains a malformed drug entry ("8.085 MG OF IVABRADINE HYDROCHLORIDE)"), which appears to be a dosage descriptor incorrectly captured as an INN — the actual active ingredient is **ivabradine** (a selective funny current Ih inhibitor used in heart failure and stable angina).
No TxGNN-predicted indications were returned for this entry.
As a result, **a full repurposing evaluation cannot be completed**; the data gaps below must be resolved before assessment can proceed.

<!-- review:begin sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-1 -->

> **Review correction (2026-11-06)**: Originally stated: "No TxGNN-predicted indications were returned for this entry, and Singapore regulatory registration records are absent." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 8 registrations for this drug, 8 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in this Evidence Pack |
| Predicted New Indication | None returned by TxGNN |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — and none present) |
| Singapore Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
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

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN13408P | CORALAN Tablet 5mg | TABLET, FILM COATED | Valid |
| SIN13409P | CORALAN Tablet 7.5 mg | TABLET, FILM COATED | Valid |
| SIN16726P | BRAVACOR FILM-COATED TABLETS 5MG | TABLET, FILM COATED | Valid |
| SIN16727P | BRAVACOR FILM-COATED TABLETS 7.5MG | TABLET, FILM COATED | Valid |
| SIN17056P | ABRAD FILM COATED TABLET 7.5 MG | TABLET, FILM COATED | Valid |

Showing 5 of 8 HSA registrations.

<!-- licenses:end -->

> Based on international data, ivabradine is marketed globally as **Procoralan** (Servier) and **Corlanor** (Amgen/US).

<!-- review:begin sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-2 -->

> **Review correction (2026-11-06)**: Originally stated: "No registered products found for this entry." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 8 registrations for this drug, 8 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-2 -->

<!-- review:begin sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-3 -->

> **Review correction (2026-11-06)**: Originally stated: "> Based on international data, ivabradine is marketed globally as **Procoralan** (Servier) and **Corlanor** (Amgen/US). If ivabradine is correctly identified and re-queried, Singapore HSA registration records should be searched under the INN `ivabradine` or brand name `Procoralan`." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 8 registrations for this drug, 8 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-3 -->

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
- **Re-query DDI database** with `ivabradine` to retrieve interaction data
- Once all above are resolved, resubmit a corrected Evidence Pack for a complete L1–L5 repurposing evaluation

<!-- review:begin sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-4 -->

> **Review correction (2026-11-06)**: Originally stated: "**Re-query DrugBank** with `ivabradine` to retrieve `drugbank_id`, `original_moa`, and toxicity data / **Re-query Singapore HSA** with the corrected drug name to populate `taiwan_regulatory` fields" Removed: leftover template text about Taiwan's TFDA, which does not apply to this Singapore page. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-8_085_mg_of_ivabradine_hydrochloride-4 -->

---

> ⚠️ **Data Quality Note:** This report was generated from an Evidence Pack with a Blocking data gap (DG001) and a High-severity gap (DG002). The drug INN field contains a dosage descriptor rather than a valid drug name, rendering all downstream predictions and safety lookups invalid. No clinical or regulatory conclusions should be drawn from this report.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and Singapore regulatory registration records are absent" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "No registered products found for this entry" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "If ivabradine is correctly identified and re-queried, Singapore HSA registration records should be searched under the INN `ivabradine` or br" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "**Re-query Singapore HSA** with the corrected drug name to populate `taiwan_regulatory` fields" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

