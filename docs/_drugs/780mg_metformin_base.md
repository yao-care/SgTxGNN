---
noindex: true
sitemap: false
layout: default
title: 780Mg Metformin Base
parent: Low Evidence (L5)
nav_order: 15
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# 780Mg Metformin Base
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

## 780MG METFORMIN BASE): Insufficient Data Quality to Complete Drug Repurposing Assessment
{: .text-alpha }

> ⚠️ **Notice**: This report cannot be completed in standard format due to severe data quality issues with the input data. The following is an analysis of data gaps and recommended actions.

---

## One-Sentence Summary

The drug field (INN) in this Evidence Pack contains a non-standard string `"780MG METFORMIN BASE)"`, which appears to result from a parsing error where dosage specifications were inadvertently mixed into the drug name field, rather than representing a correct international nonproprietary name.
Due to failed drug identification, the system was unable to retrieve any TxGNN predicted indications, or safety data. **At present, drug repurposing assessment cannot be executed**.

<!-- review:begin sg-lic-20261106-780mg_metformin_base-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Due to failed drug identification, the system was unable to retrieve any TxGNN predicted indications, Singapore market availability data, or safety data." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 65 registrations for this drug, 65 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-780mg_metformin_base-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Input Drug Name (Raw) | `780MG METFORMIN BASE)` ← suspected parsing error |
| Presumed Correct Drug | Metformin (Metformin HCl, biguanide antidiabetic) |
| Predicted New Indications | None (predicted_indications array is empty) |
| TxGNN Prediction Score | No data |
| Evidence Level | L5 (model prediction data missing) |
| Singapore Market Status | Marketed (valid licences: 65 of 65) |
| Number of Registrations | 65 (valid: 65) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Due to the empty `predicted_indications` array, mechanistic relevance analysis cannot be performed in this section.

Should the drug be confirmed as **Metformin**, its mechanism of action (AMPK activation, hepatic gluconeogenesis inhibition) possesses a rich research foundation in the drug repurposing field (cancer, PCOS, NAFLD, neurodegenerative disease, etc.), and **would merit evaluation**. However, until the drug identification issue is resolved, no prediction interpretation should be undertaken.

---

## Clinical Trial Evidence

No relevant clinical trial data are currently available (predicted_indications is empty, precluding queries).

---

## Literature Evidence

No relevant literature data are currently available (predicted_indications is empty, precluding queries).

<!-- review:begin sg-lic-20261106-780mg_metformin_base-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The present query retrieved no Singapore approval records (total_licenses: 0)." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 65 registrations for this drug, 65 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-780mg_metformin_base-2 -->

<!-- review:begin sg-lic-20261106-780mg_metformin_base-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Should drug identification be confirmed as Metformin, re-querying is warranted—Metformin is widely marketed in Singapore and would be expected to have multiple HSA approval records." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 65 registrations for this drug, 65 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-780mg_metformin_base-3 -->

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN04249P | GLUCOPHAGE TABLET 500 mg | TABLET, FILM COATED | Valid |
| SIN04272P | METFORMIN TABLET 500 mg | TABLET | Valid |
| SIN04674P | METFORMIN TABLET 500 mg | TABLET, FILM COATED | Valid |
| SIN04812P | DIABETMIN TABLET 500 mg | TABLET, FILM COATED | Valid |
| SIN06937P | GLYFORMIN 500 TABLET 500 mg | TABLET, FILM COATED | Valid |

Showing 5 of 65 HSA registrations.

<!-- licenses:end -->

---

## Safety Considerations

Please consult product labeling warnings and contraindications. Safety data queries failed to return results, possibly due to failed drug identification.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The drug identification field (INN) contains a malformed string, resulting in complete failure of DrugBank mapping, TxGNN prediction, and safety assessment. Without data correction, this case presents no evaluable prediction evidence.

<!-- review:begin sg-lic-20261106-780mg_metformin_base-4 -->

> **Review correction (2026-11-06)**: Originally stated: "The drug identification field (INN) contains a malformed string, resulting in complete failure of DrugBank mapping, TxGNN prediction, Singapore market availability query, and safety assessment." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 65 registrations for this drug, 65 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-780mg_metformin_base-4 -->

**To proceed, the following is needed:**

1. **Resolve drug identification issue (Blocking)**
   - Confirm correct INN: if Metformin, input should be `metformin` (lowercase, no parentheses, no dosage specifications)
   - Re-trigger Evidence Pack generation workflow

2. **Supplement DrugBank ID (High)**
   - Metformin DrugBank ID is `DB00331`
   - Supplementation enables retrieval of complete MOA, drug classification, and safety data

3. **Re-execute TxGNN prediction**
   - Upon confirmation of drug identification, regenerate `predicted_indications`

<!-- review:begin sg-lic-20261106-780mg_metformin_base-5 -->

> **Review correction (2026-11-06)**: Originally stated: "**Supplement Singapore HSA data (High)** / Metformin should have market records in Singapore; re-query to confirm" Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 65 registrations for this drug, 65 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-780mg_metformin_base-5 -->

5. **Supplement product labeling safety data (Blocking)**
   - Per DG001 remediation measures: download product labeling PDF for parsing of warnings and contraindications

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Singapore market availability data" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "The present query retrieved no Singapore approval records (total_licenses: 0)" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "Should drug identification be confirmed as Metformin, re-querying is warranted—Metformin is widely marketed in Singapore and would be expect" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "Singapore market availability query" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "4. **Supplement Singapore HSA data (High)** - Metformin should have market records in Singapore; re-query to confirm" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

