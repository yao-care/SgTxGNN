---
layout: default
title: Amantadine Hcl
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 0
---

# Amantadine Hcl
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

# Amantadine HCl: Repurposing Evaluation — Insufficient Data to Proceed

---

## One-Sentence Summary

Amantadine HCl is a well-known antiviral and antiparkinsonian agent used clinically for influenza A prophylaxis and Parkinson's disease management. However, this Evidence Pack contains **no predicted repurposing indications** from TxGNN, and key data items — including the mechanism of action, Singapore market registration, and safety warnings — are all unresolved gaps. **A meaningful repurposing evaluation cannot be completed until these gaps are addressed.**

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in this Evidence Pack |
| Predicted New Indication | None — TxGNN predictions not available |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction unavailable; no supporting studies retrievable) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

This section cannot be completed as written because the Evidence Pack contains **no predicted indication** (`predicted_indications: []`). There is therefore no mechanistic link to evaluate between a source and target disease.

From publicly available pharmacological knowledge, Amantadine HCl is understood to act as an NMDA receptor antagonist and dopamine-releasing agent. It has established use in influenza A prophylaxis and Parkinson's disease. These mechanisms have led researchers to investigate it in conditions such as fatigue syndromes, traumatic brain injury, and multiple sclerosis — but **none of these directions is reflected in this Evidence Pack**, and none can be formally evaluated here without TxGNN predictions and supporting evidence data.

Until a complete Evidence Pack with `predicted_indications` is generated, mechanistic reasoning for repurposing cannot be substantiated.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature is available in this Evidence Pack.

---

## Singapore Market Information

Amantadine HCl holds **zero active product licences** in Singapore. The drug is classified as **not marketed**.

There are no registration records to display.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields in this Evidence Pack — including key warnings, contraindications, and drug–drug interactions — returned no data. The DDI query status is `not_found` with zero interactions recorded. The TFDA package insert has not been parsed (Data Gap DG001, severity: Blocking).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This Evidence Pack is structurally incomplete: there are no predicted indications, no regulatory registrations, no safety data, and no mechanistic information. Proceeding to any repurposing evaluation stage is not possible in this state.

**To proceed, the following is needed:**

- **[DG001 — Blocking]** Obtain and parse the package insert (仿單) from the TFDA website to extract warnings and contraindications. Without this, the safety screening step (S1) cannot begin.
- **[DG002 — High]** Retrieve the mechanism of action via the DrugBank API using the DrugBank ID. The ID field is currently `null` — a successful DrugBank query was logged (Query ID 2, status: success), but the result was not written back into the pack.
- **Re-run TxGNN prediction pipeline** — the `predicted_indications` array is empty, which means either the drug was not matched to a DrugBank node or the pipeline did not execute. Confirm DrugBank ID resolution and rerun repurposing scoring.
- **Confirm INN standardisation** — the drug is listed as `AMANTADINE HCL` (salt form). Verify that the mapping pipeline is correctly resolving this to the base INN `amantadine` before querying DrugBank and TxGNN.
- Once predictions are available, re-generate a full Evidence Pack and re-evaluate using the standard L1–L5 evidence framework.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

