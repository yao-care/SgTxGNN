---
layout: default
title: Albuterol Base
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 0
---

# Albuterol Base
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

# ALBUTEROL BASE: Repurposing Evaluation — No Predictions Available

## One-Sentence Summary

ALBUTEROL BASE is the free-base form of albuterol (salbutamol), a well-known short-acting beta-2 adrenergic agonist, but it is not currently registered under this name in the target regulatory jurisdiction.
The TxGNN model returned **no predicted new indications** for this entry, and no supporting clinical trials or literature were retrieved from the evidence pipeline.
This evaluation cannot advance beyond a preliminary assessment due to incomplete input data and the absence of predictions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (no regulatory registrations found) |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | — (No predictions; insufficient input data) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No TxGNN predictions were generated for this entry, so a mechanistic rationale for a new indication cannot be provided at this time.

Based on general pharmacological knowledge, albuterol (salbutamol) is a selective short-acting beta-2 adrenergic receptor agonist, most widely recognised for relieving bronchospasm in asthma and COPD. The designation **"BASE"** refers to the free-base chemical form rather than the more commonly registered salt form (albuterol sulfate). This naming difference is the most likely explanation for zero regulatory matches — the substance is marketed globally under the INN **salbutamol** or as **albuterol sulfate**, not as "albuterol base."

The absence of predictions is likely a **pipeline input problem rather than a genuine data gap** for the molecule itself: the drug identifier did not resolve to a TxGNN knowledge graph node, preventing the model from generating any candidates. Once the identifier is corrected, a meaningful repurposing analysis should be feasible given albuterol's well-characterised pharmacology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No regulatory registrations were found for **ALBUTEROL BASE** in the HSA database.

> **Naming note:** Albuterol is registered globally under two alternative names — **salbutamol** (WHO International Nonproprietary Name, used in Singapore, UK, Australia) and **albuterol sulfate** (US convention). A repeat search using either of these names is strongly recommended before concluding that the molecule is absent from the Singapore market.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline returned no results for ALBUTEROL BASE, and all critical drug-level inputs — original indications, mechanism of action, and regulatory records — are absent; a repurposing evaluation cannot be meaningfully completed from the current evidence pack.

**To proceed, the following is needed:**

- **Correct the drug identifier**: Re-query using `salbutamol` or `albuterol sulfate` to match HSA regulatory records and the TxGNN knowledge graph node
- **Re-run the TxGNN pipeline** with the corrected identifier to generate repurposing candidates
- **Extract DrugBank data**: The query log confirms a successful DrugBank hit (1 result) — populate MOA, original indications, and DrugBank ID from that result
- **Retrieve safety data**: Download and parse the HSA-approved package insert to populate key warnings and contraindications (currently blocking per DG001)
- **Re-issue the evidence pack** after the above corrections and regenerate this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

