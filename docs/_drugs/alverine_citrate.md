---
layout: default
title: Alverine Citrate
parent: 僅模型預測 (L5)
nav_order: 75
evidence_level: L5
indication_count: 0
---

# Alverine Citrate
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

# Alverine Citrate: Preliminary Screening — Insufficient Data for Full Evaluation

## One-Sentence Summary

Alverine Citrate is an antispasmodic smooth muscle relaxant commonly used for irritable bowel syndrome (IBS) and gastrointestinal spasms.
However, the current Evidence Pack contains **no TxGNN-predicted new indications**, **no Singapore regulatory registrations**, and **no mechanism of action data** —
this report serves as a data-gap assessment, and a **Hold** decision is recommended until core data is collected.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not recorded in Singapore regulatory database |
| Predicted New Indication | No predictions available (TxGNN pipeline not completed) |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — Model prediction not yet generated |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Alverine Citrate in this Evidence Pack. Based on known pharmacological literature, Alverine Citrate is a selective smooth muscle relaxant belonging to the antispasmodic class. Its efficacy in gastrointestinal conditions (particularly IBS and intestinal colic) has been established in clinical practice.

Without a completed TxGNN prediction run, no new indication has been identified. The DrugBank query returned one result (query log ID 2), suggesting the compound exists in the DrugBank database — however, the DrugBank ID was not captured in this Evidence Pack. Completing the DrugBank ID lookup would be the critical first step to enable TxGNN graph traversal and generate repurposing candidates.

---

## Singapore Market Information

Alverine Citrate currently has **no registered products** in the Singapore Health Sciences Authority (HSA) database. There are no active licenses, withdrawn entries, or historical registrations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN repurposing pipeline has not been executed for Alverine Citrate, yielding zero predicted indications. Without a DrugBank ID, mechanism of action data, or safety profile, no evidence-based repurposing assessment is possible at this stage.

**To proceed, the following is needed:**

- **[Blocking]** Retrieve the DrugBank ID from the DrugBank API (query log confirms the compound exists — ID capture failed)
- **[Blocking]** Download and parse the package insert (PI) from Singapore HSA or equivalent regional authority to obtain warnings and contraindications
- **[High]** Extract mechanism of action (MOA) from DrugBank once the ID is confirmed
- **[High]** Re-run the TxGNN KG prediction pipeline with the confirmed DrugBank ID to generate repurposing candidates
- **[Medium]** Verify Singapore market status — confirm whether Alverine Citrate is sold under a combination product or under a different INN that may carry its own registration
- **[Medium]** Run ClinicalTrials.gov and PubMed collectors after TxGNN candidates are generated to populate evidence tables
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

