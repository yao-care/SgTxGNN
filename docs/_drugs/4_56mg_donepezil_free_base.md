---
noindex: true
sitemap: false
layout: default
title: 4 56Mg Donepezil Free Base
parent: Low Evidence (L5)
nav_order: 11
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# 4 56Mg Donepezil Free Base
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

## Donepezil 4.56 mg (Free Base): Data Quality Issues Prevent Repurposing Evaluation
{: .text-alpha }

> **⚠️ Note:** The standard title format `From [Original Indication] to [Predicted New Indication]` cannot be applied because this Evidence Pack contains **no predicted indications**. The root cause is identified below.

---

## One-Sentence Summary

The entry `4.56MG DONEPEZIL FREE BASE` appears to refer to a transdermal patch formulation of donepezil, a reversible acetylcholinesterase inhibitor used for Alzheimer's disease.
However, the TxGNN model generated **no predicted indications** for this entry — most likely due to a drug name normalization failure where the dosage value and formulation descriptor were parsed as part of the INN.

<!-- review:begin sg-lic-20261106-4_56mg_donepezil_free_base-1 -->

> **Review correction (2026-11-06)**: Originally stated: "However, the TxGNN model generated **no predicted indications** for this entry — most likely due to a drug name normalization failure where the dosage value and formulation descriptor were parsed as part of the INN. No Singapore market registrations were found, and a complete repurposing evaluation cannot be produced until the upstream data quality issues are resolved." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 15 registrations for this drug, 15 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-4_56mg_donepezil_free_base-1 -->

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Evidence Pack (donepezil is clinically approved for Alzheimer's disease) |
| Predicted New Indication | None — TxGNN generated zero predictions for this entry |
| TxGNN Prediction Score | N/A |
| Evidence Level | Not applicable |
| Singapore Market Status | Marketed (valid licences: 15 of 15) |
| Number of Registrations | 15 (valid: 15) |
| Recommended Decision | **Hold** |

---

## Why Were No Predictions Generated?

The drug identifier submitted to the pipeline — `4.56MG DONEPEZIL FREE BASE` — mixes three distinct pieces of information: a dosage quantity (`4.56MG`), the INN (`DONEPEZIL`), and a salt/formulation descriptor (`FREE BASE`). This non-standard composite string is the most probable cause of the TxGNN mapping failure: the pipeline was unable to resolve this entry to the correct DrugBank node, and consequently produced no disease predictions.

Interestingly, the query log (ID 2) records a **successful** DrugBank lookup with `result_count: 1`, which suggests the underlying compound was identified at some stage of the pipeline. The predictions were either never requested or were discarded before reaching the output layer. Re-running with the clean INN `Donepezil` (DrugBank: DB00843) should recover predictions.

Donepezil is a well-characterised compound with a known mechanism of action (reversible inhibition of acetylcholinesterase → increased synaptic acetylcholine → improved cholinergic transmission). Its pharmacological profile has been explored in multiple disease contexts beyond Alzheimer's disease (e.g., vascular dementia, Lewy body dementia, and various neuropsychiatric indications), meaning TxGNN would be expected to generate meaningful candidates once the identifier is corrected.

<!-- review:begin sg-lic-20261106-4_56mg_donepezil_free_base-2 -->

> **Review correction (2026-11-06)**: Originally stated: "No HSA registrations were found for the string `4.56MG DONEPEZIL FREE BASE`. This is expected: Singapore product registrations are filed under the INN (`Donepezil`) or specific brand names (e.g., Aricept®, Memac®), not under dosage-qualified strings. A separate query under the correct INN or known brand names is needed to determine actual Singapore market status." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 15 registrations for this drug, 15 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-4_56mg_donepezil_free_base-2 -->

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN13645P | Aricept Evess 5mg orodispersible tablet | TABLET, ORALLY DISINTEGRATING | Valid |
| SIN13646P | Aricept Evess 10mg orodispersible tablet | TABLET, ORALLY DISINTEGRATING | Valid |
| SIN14389P | DOPEZIL TABLETS 10MG | TABLET, FILM COATED | Valid |
| SIN14390P | DOPEZIL TABLETS 5MG | TABLET, FILM COATED | Valid |
| SIN14575P | Aricept Film-coated Tablets 23mg | TABLET, FILM COATED | Valid |

Showing 5 of 15 HSA registrations.

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack cannot support a repurposing evaluation in its current form. The drug name is not a valid INN, no TxGNN predictions were generated, and all safety data fields are unresolved. The underlying compound (donepezil) is well-characterised and evaluation-ready — the obstacle is entirely a data pipeline issue.

**To proceed, the following is needed:**

- **Normalize the drug name:** Strip the dosage (`4.56MG`) and salt descriptor (`FREE BASE`) and resubmit as the bare INN `Donepezil`
- **Re-run the TxGNN prediction pipeline** using the corrected identifier to generate `predicted_indications`
- **Retrieve MOA and safety data** from DrugBank (DB00843) to populate `original_moa`, `key_warnings`, and `contraindications`
- **Re-generate the Evidence Pack** with the corrected drug entry before proceeding to formal evaluation

<!-- review:begin sg-lic-20261106-4_56mg_donepezil_free_base-3 -->

> **Review correction (2026-11-06)**: Originally stated: "**Retrieve MOA and safety data** from DrugBank (DB00843) to populate `original_moa`, `key_warnings`, and `contraindications` / **Re-query Singapore HSA** under `Donepezil` and known brand names to determine actual market status" Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 15 registrations for this drug, 15 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-4_56mg_donepezil_free_base-3 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "No Singapore market registrations were found, and a complete repurposing evaluation cannot be produced until the upstream data quality issue" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "No HSA registrations were found for the string `4.56MG DONEPEZIL FREE BASE`. This is expected: Singapore product registrations are filed und" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "**Re-query Singapore HSA** under `Donepezil` and known brand names to determine actual market status" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

