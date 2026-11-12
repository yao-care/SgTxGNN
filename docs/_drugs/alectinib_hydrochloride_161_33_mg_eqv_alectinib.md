---
noindex: true
sitemap: false
layout: default
title: Alectinib Hydrochloride 161 33 Mg Eqv Alectinib
parent: Low Evidence (L5)
nav_order: 56
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Alectinib Hydrochloride 161 33 Mg Eqv Alectinib
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

## Alectinib: Evaluation Halted — Insufficient Evidence Pack Data
{: .text-alpha }

## One-Sentence Summary

Alectinib hydrochloride is a second-generation ALK (Anaplastic Lymphoma Kinase) tyrosine kinase inhibitor, internationally approved for ALK-positive non-small cell lung cancer (NSCLC).
The current Evidence Pack contains **no TxGNN-predicted repurposing indications**, **critical data gaps in MOA and safety**, making a standard repurposing evaluation impossible at this stage.
This report documents the gap findings and outlines the remediation steps required before a full evaluation can proceed.

<!-- review:begin sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The current Evidence Pack contains **no TxGNN-predicted repurposing indications**, **zero Singapore regulatory registrations**, and **critical data gaps in MOA and safety**, making a standard repurposing evaluation impossible at this stage." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 1 registration for this drug, 1 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ALK-positive NSCLC (identified from INN) |
| Predicted New Indication | Not available — `predicted_indications` array is empty |
| TxGNN Prediction Score | Not available |
| Evidence Level | Not assessable |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | **Hold** |

---

## Why No Prediction Is Available

The TxGNN pipeline was run against the drug string `"ALECTINIB HYDROCHLORIDE 161.33 MG EQV. ALECTINIB"`. The DrugBank query returned a match (`result_count: 1`), but no `drugbank_id` was populated in the output, and `predicted_indications` remains empty. This typically occurs when the pipeline cannot resolve the compound's canonical identity — likely because the input string contains a dosage quantity rather than a clean INN.

Alectinib is a highly selective, CNS-penetrant ALK inhibitor with a well-characterized pharmacological profile. Its potential for repurposing into other ALK-driven malignancies (e.g., ALK-positive anaplastic large cell lymphoma, inflammatory myofibroblastic tumor) is biologically plausible. However, without a valid TxGNN output, no formal prediction can be evaluated or scored.

Detailed mechanism of action data was not returned in the Evidence Pack (Data Gap DG002). Based on publicly available pharmacology, alectinib inhibits ALK and RET kinases, preventing downstream RAS/MAPK and PI3K/AKT signalling that drives tumour proliferation and survival.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15220P | ALECENSA HARD CAPSULE 150MG | CAPSULE | Valid |

<!-- licenses:end -->

> **Note:** Alectinib (Alecensa®) has regulatory approval in the US (FDA, 2015/2017), EU (EMA), and Japan (PMDA).

<!-- review:begin sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Alectinib is not currently registered with Singapore's HSA. No license records are available in the regulatory database extract." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 1 registration for this drug, 1 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-2 -->

<!-- review:begin sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-3 -->

> **Review correction (2026-11-06)**: Originally stated: "> **Note:** Alectinib (Alecensa®) has regulatory approval in the US (FDA, 2015/2017), EU (EMA), and Japan (PMDA). HSA Singapore approval status should be independently verified via the HSA PRISM portal before concluding "not registered."" Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 1 registration for this drug, 1 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-3 -->

---

## Cytotoxicity

Alectinib meets the antineoplastic classification criteria (cancer indication, targeted kinase inhibitor class).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — ALK/RET tyrosine kinase inhibitor (not a conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate; anaemia is the most common haematological adverse effect |
| Emetogenicity Classification | Low |
| Monitoring Items | LFTs (AST, ALT, bilirubin), CBC, creatine phosphokinase (CPK), serum creatinine, ECG (QTc) |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Both key warnings and contraindications are listed as Data Gap (DG001 — Blocking severity). No DDI interactions were found in the query log. Safety evaluation cannot proceed until the package insert is retrieved and parsed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is structurally incomplete — no TxGNN predictions, two blocking data gaps (DG001, DG002) prevent any component of the standard evaluation from being completed. Proceeding to a repurposing decision without these inputs would be speculative.

<!-- review:begin sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-4 -->

> **Review correction (2026-11-06)**: Originally stated: "The Evidence Pack is structurally incomplete — no TxGNN predictions, no Singapore regulatory records, and two blocking data gaps (DG001, DG002) prevent any component of the standard evaluation from being completed." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 1 registration for this drug, 1 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-4 -->

**To proceed, the following is needed:**

- **Resolve DrugBank mapping** — re-run the pipeline with the clean INN `"alectinib"` (without dose quantity) to obtain a valid `drugbank_id` and trigger TxGNN prediction output
- **Retrieve package insert** (DG001 — Blocking) — download and parse the approved SmPC/PI from FDA.gov, EMA, or PMDA to populate warnings and contraindications
- **Populate MOA data** (DG002 — High) — query DrugBank API with the resolved ID to obtain mechanism of action, targets, and pharmacodynamic class
- **Re-run TxGNN pipeline** with corrected input string and confirm `predicted_indications` is populated before re-initiating this evaluation

<!-- review:begin sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-5 -->

> **Review correction (2026-11-06)**: Originally stated: "**Populate MOA data** (DG002 — High) — query DrugBank API with the resolved ID to obtain mechanism of action, targets, and pharmacodynamic class / **Verify Singapore HSA registration** — cross-check HSA PRISM portal directly; the pipeline returned zero records but international approval is documented" Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 1 registration for this drug, 1 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-alectinib_hydrochloride_161_33_mg_eqv_alectinib-5 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "**zero Singapore regulatory registrations**, and" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "Alectinib is not currently registered with Singapore's HSA. No license records are available in the regulatory database extract" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "HSA Singapore approval status should be independently verified via the HSA PRISM portal before concluding "not registered."" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "no Singapore regulatory records, and" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "**Verify Singapore HSA registration** — cross-check HSA PRISM portal directly; the pipeline returned zero records but international approval" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

