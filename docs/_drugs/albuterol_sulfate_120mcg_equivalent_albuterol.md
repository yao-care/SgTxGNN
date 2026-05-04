---
layout: default
title: Albuterol Sulfate 120Mcg Equivalent Albuterol
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 0
---

# Albuterol Sulfate 120Mcg Equivalent Albuterol
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

# Albuterol Sulfate: From Bronchospasm/Asthma to [No Prediction Available]

## One-Sentence Summary

Albuterol Sulfate (also known as Salbutamol) is a short-acting beta-2 adrenergic agonist classically used for the relief of bronchospasm in conditions such as asthma and COPD.
However, the TxGNN model returned **no predicted new indications** for this entry, likely due to the non-standard drug name format ("ALBUTEROL SULFATE 120MCG EQUIVALENT ALBUTEROL") causing a mapping failure.
As a result, this report documents the data gaps and recommends remediation before proceeding.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not specified in Evidence Pack (general knowledge: bronchospasm, asthma, COPD) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A (no prediction output) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN prediction was generated for this drug entry. The most likely cause is a **drug name normalisation failure**: the query string `"ALBUTEROL SULFATE 120MCG EQUIVALENT ALBUTEROL"` embeds a dosage strength and the phrase "EQUIVALENT", which is atypical for an International Nonproprietary Name (INN). Standard drug-mapping pipelines would expect the clean INN `albuterol` or `salbutamol` as input.

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on general pharmacological knowledge, Albuterol is a selective beta-2 adrenoceptor agonist that relaxes bronchial smooth muscle, producing bronchodilation. This mechanism has established efficacy in reversible obstructive airway disease and mechanistically could be explored in areas such as preterm labour (tocolysis) or hyperkalaemia — but these cannot be surfaced without a valid TxGNN run.

A re-query using the cleaned INN `albuterol` (DrugBank: DB01001) is required before any mechanistic repurposing analysis can proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — TxGNN prediction output is absent; no target indication has been identified to search against.

---

## Literature Evidence

Currently no related literature available — without a predicted indication, a directed literature search cannot be scoped.

---

## Singapore Market Information

This drug is currently **not registered** in Singapore. No licence records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both key warnings and contraindication fields returned `[Data Gap]` in this Evidence Pack, and the DDI query returned zero results. This is inconsistent with Albuterol's known safety profile (e.g., tachycardia, hypokalaemia with high doses, interactions with beta-blockers and MAOIs), further suggesting the drug name failed to match correctly in the data pipeline.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Evidence Pack is non-actionable in its current state — the drug name format is non-standard, no DrugBank ID was resolved, no TxGNN predictions were produced, and all safety fields are empty. Proceeding to repurposing evaluation without correcting these upstream issues would yield unreliable results.

**To proceed, the following is needed:**

- **[Critical] Fix drug name input**: Replace `"ALBUTEROL SULFATE 120MCG EQUIVALENT ALBUTEROL"` with the clean INN `albuterol` (or `salbutamol`) and re-run the full pipeline
- **[Critical] Resolve DrugBank ID**: Expected mapping is `DB01001` (Salbutamol); confirm via DrugBank API and populate `drugbank_id`
- **[Blocking — DG001] Retrieve safety data**: Download the package insert PDF and extract warnings/contraindications
- **[High — DG002] Populate MOA**: Query DrugBank API for mechanism of action using the corrected drug ID
- **[Follow-up] Re-run TxGNN prediction**: Once name normalisation is corrected, re-execute KG and DL prediction pipelines to obtain valid repurposing candidates
- **[Follow-up] Check Singapore registration status**: Query HSA (Health Sciences Authority) directly — it is possible albuterol inhalers are registered under a different brand name or strength descriptor that was not matched
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

