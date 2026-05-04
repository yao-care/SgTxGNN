---
layout: default
title: Ambroxol Hcl
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 0
---

# Ambroxol Hcl
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

# AMBROXOL HCL: Repurposing Evaluation — Prediction Pipeline Incomplete

## One-Sentence Summary

Ambroxol HCL is a widely used mucolytic agent for respiratory tract disorders, with established safety in clinical practice.
However, the current Evidence Pack contains **no TxGNN predicted indications** for this drug, and it is **not registered** in Singapore's HSA database.
A full repurposing evaluation cannot be completed until critical data gaps are resolved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Respiratory tract disorders (mucolytic / secretolytic agent) |
| Predicted New Indication | No prediction data available |
| TxGNN Prediction Score | Not available |
| Evidence Level | L5 — Prediction pipeline returned no results |
| Singapore Market Status | ✗ Not Registered |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why No Prediction Was Generated

The TxGNN pipeline requires a valid **DrugBank ID** to anchor the drug node within the knowledge graph. For this run, the DrugBank ID for Ambroxol HCL was not successfully mapped (returned `null`), even though the DrugBank query reported a successful response. This ID resolution failure prevents the system from locating the correct knowledge graph node, which in turn blocks both the KG-based and deep-learning prediction steps.

Additionally, the two blocking data gaps below compound the problem:

| Data Gap | Severity | Impact |
|----------|----------|--------|
| TFDA/HSA package insert warnings & contraindications | Blocking | Cannot complete S1 safety screen |
| Mechanism of action (MOA) | High | Cannot perform mechanistic plausibility analysis |

Without resolved data, any indication scores or evidence tables produced would be unreliable and should not be acted upon.

---

## Singapore Market Information

Ambroxol HCL is **not registered** under HSA in Singapore based on current data (0 licences found). No product table can be generated.

> Note: Ambroxol is registered and widely marketed in many Asia-Pacific markets (Taiwan, Japan, Thailand, EU) under brand names such as Mucosolvan, Ambrox, and Lysopain. The absence of an HSA record should be verified against the HSA PRISM database directly before concluding market absence.

---

## Safety Considerations

All safety fields in this Evidence Pack are marked as data gaps. No drug-drug interaction records were found.

> Please refer to the package insert and HSA/DrugBank records directly for safety information before proceeding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline produced no output for Ambroxol HCL due to a failed DrugBank ID mapping, and both safety and MOA data are absent. There is currently no evidence base from which to evaluate a repurposing hypothesis.

**To proceed, the following is needed:**

1. **Resolve DrugBank ID** — Query DrugBank by INN `ambroxol` (not salt form `ambroxol HCl`) and confirm the canonical ID (expected: DB06742). Verify the mapping normalizer handles salt-stripped names.
2. **Obtain MOA data** — Pull pharmacology, mechanism, and target data from DrugBank API once the ID is confirmed.
3. **Source HSA / TFDA package insert** — Download the PDF and parse warnings, contraindications, and approved indications to clear the Blocking data gap (DG001).
4. **Re-run TxGNN prediction pipeline** — With a valid DrugBank ID and complete drug profile, re-execute `run_kg_prediction.py` and the DL model to generate ranked repurposing candidates.
5. **Verify Singapore market status** — Cross-check the HSA PRISM product register directly; the current "not registered" result may reflect a data ingestion gap rather than a true absence.
6. **Re-issue Evidence Pack** — Once the above are complete, generate a v5 Evidence Pack and produce a full evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

