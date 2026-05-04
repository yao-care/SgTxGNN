---
layout: default
title: 9 12Mg Donepezil Free Base
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 0
---

# 9 12Mg Donepezil Free Base
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

# Donepezil (9.12mg Free Base): Evaluation Blocked — Data Entry Issue and Missing Predictions

## One-Sentence Summary

The entry "9.12MG DONEPEZIL FREE BASE" appears to encode a dosage specification within the drug name field rather than a clean INN, preventing proper DrugBank matching and TxGNN prediction.
**No repurposing predictions were returned** for this entry, and the drug shows **zero Singapore registrations** under this name — making a full repurposing evaluation impossible at this stage.
Resolving the naming issue and re-running the pipeline is required before any clinical assessment can proceed.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — original indications array is empty |
| Predicted New Indication | None — no TxGNN predictions returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (no predictions, no supporting studies available) |
| Singapore Market Status | ✗ Not marketed (under this entry name) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Root Cause Analysis

> ⚠️ **This report cannot follow the standard format because the Evidence Pack contains no predicted indications.** The sections below explain why and what needs to be resolved.

### Drug Name Format Problem

The INN field contains `9.12MG DONEPEZIL FREE BASE` — this is a **formulation specification string**, not an International Nonproprietary Name. The correct INN is simply **donepezil**.

The embedded dosage ("9.12mg") represents the free base equivalent of donepezil hydrochloride 10mg — a pharmaceutical equivalence note that belongs in a dosage field, not the drug name field.

This format mismatch explains two downstream failures:

| Failure | Cause |
|---------|-------|
| `drugbank_id: null` | DrugBank lookup could not match the full string to donepezil |
| `predicted_indications: []` | TxGNN received no valid drug node to generate predictions |
| Singapore registrations: 0 | Regulatory lookup found no match for this non-standard name |

### What Is Known About Donepezil

Although the Evidence Pack contains no original indication data (empty array), donepezil is a widely recognised acetylcholinesterase inhibitor approved for **Alzheimer's disease** (mild to severe dementia). It is marketed globally under the brand name Aricept (DrugBank: DB00843). Donepezil hydrochloride is registered in Singapore under multiple product licences. None of this information can be confirmed from the current Evidence Pack and would need to be reloaded after the naming issue is corrected.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(All safety fields returned [Data Gap]. DDI query returned no results under the current non-standard name.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pipeline produced no usable output because the INN field encodes a dosage specification rather than a clean drug name, blocking DrugBank ID resolution, TxGNN prediction, regulatory lookup, and evidence collection simultaneously. There is nothing to evaluate clinically until the upstream data entry is corrected.

**To proceed, the following is required:**

1. **Fix the drug name entry** — replace `9.12MG DONEPEZIL FREE BASE` with the INN `donepezil` in the source data; move dosage information to the appropriate dosage/formulation field
2. **Confirm the DrugBank ID** — donepezil maps to DB00843; verify and populate `drugbank_id`
3. **Re-run the full TxGNN pipeline** — with a clean INN, predictions and evidence collection should proceed normally
4. **Retrieve MOA data** (Data Gap DG002) — query the DrugBank API for mechanism of action after the ID is confirmed
5. **Retrieve Singapore regulatory data** — re-run the regulatory lookup for `donepezil` to identify all registered products
6. **Retrieve safety data** (Data Gap DG001) — download and parse the approved package insert for warnings and contraindications
7. **Generate a new Evidence Pack** — once all upstream issues are resolved, re-generate and resubmit for evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

