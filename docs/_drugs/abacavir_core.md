---
layout: default
title: Abacavir Core
parent: 僅模型預測 (L5)
nav_order: 20
evidence_level: L5
indication_count: 0
---

# Abacavir Core
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

# Abacavir: HIV Antiretroviral — No Repurposing Predictions Available

## One-Sentence Summary

Abacavir is a nucleoside reverse transcriptase inhibitor (NRTI) used as part of combination antiretroviral therapy for HIV-1 infection.
The TxGNN model returned **no predicted new indications** for this drug entry, and the drug currently has **no registered products in Singapore**, making a full repurposing evaluation impossible at this stage.
The primary cause is a missing DrugBank ID and an unresolved drug identity flag ("CORE"), which prevented the prediction engine from completing a knowledge graph lookup.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (combination antiretroviral therapy) |
| Predicted New Indication | None — no TxGNN predictions returned |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions available |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Evaluation Cannot Proceed

The TxGNN pipeline returned an empty `predicted_indications` list for this entry. Based on the query log and metadata, three compounding issues likely caused the failure:

**1. Unresolved drug identity ("CORE" label)**
The drug is recorded as *"ABACAVIR (CORE)"*, suggesting it was extracted as a core active ingredient from a fixed-dose combination product (e.g., Epzicom or Triumeq) rather than mapped as a standalone monotherapy entity. This label mismatch may have caused the normalisation step to fail drug node lookup in the knowledge graph.

**2. Missing DrugBank ID**
Without a confirmed DrugBank ID, the knowledge graph cannot locate the drug node, and no disease–drug edges can be scored by TxGNN. The DrugBank query returned a result (`result_count: 1`), but the ID was not propagated into the evidence pack — this is a pipeline data-linkage issue that needs to be resolved upstream.

**3. Missing mechanism of action data**
With no MOA available, the model loses a key feature for inferring mechanistic similarity to candidate diseases, further reducing prediction confidence to below the output threshold.

From background knowledge, Abacavir's mechanism — intracellular phosphorylation to carbovir triphosphate, which competitively inhibits HIV-1 reverse transcriptase and acts as a chain terminator — has been explored in repurposing literature for other RNA viruses. However, **no model-generated scores or evidence links are present in this evidence pack** to support a structured evaluation of any new indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note not captured in this evidence pack**: Abacavir carries a well-known black-box warning for potentially fatal hypersensitivity reactions (HSR) associated with the HLA-B\*5701 allele. Pre-treatment genetic screening is mandatory in routine clinical practice. This information must be retrieved from the HSA-approved package insert before any further evaluation or clinical consideration proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model returned zero predictions for this entry due to a broken drug identity chain — the "(CORE)" label and missing DrugBank ID prevented any disease–drug scoring from completing. There is no prediction output to evaluate, and the drug is not registered in Singapore.

**To proceed, the following is needed:**

- **Resolve drug identity**: Confirm whether "ABACAVIR (CORE)" refers to the monotherapy (Ziagen) or a fixed-dose combination component, and align the entry name accordingly
- **Link DrugBank ID**: The DrugBank query returned one result — retrieve and populate the confirmed ID (expected: DB01048) so the prediction pipeline can complete the knowledge graph lookup
- **Re-run TxGNN prediction**: After correcting the drug entry, re-run the full prediction pipeline to generate `predicted_indications`
- **Retrieve Singapore/HSA package insert**: Populate safety warnings, contraindications, and MOA data from the HSA-registered product label
- **Confirm HLA-B\*5701 screening requirement**: Any repurposing evaluation must account for this mandatory safety screen as a key guardrail for any future indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

