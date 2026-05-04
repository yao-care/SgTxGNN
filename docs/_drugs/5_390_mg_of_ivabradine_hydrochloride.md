---
layout: default
title: 5 390 Mg Of Ivabradine Hydrochloride
parent: 僅模型預測 (L5)
nav_order: 13
evidence_level: L5
indication_count: 0
---

# 5 390 Mg Of Ivabradine Hydrochloride
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

# Ivabradine: Insufficient Data for Repurposing Evaluation

> ⚠️ **Data Quality Alert**: The `inn` field in this Evidence Pack contains a dosage specification (`"5.390 MG OF IVABRADINE HYDROCHLORIDE)"`) rather than a proper INN. The active ingredient is **Ivabradine**. This malformed input is the root cause of all downstream data gaps in this report.

---

## One-Sentence Summary

Ivabradine is a selective If (funny current) channel inhibitor used in cardiovascular medicine, approved in multiple jurisdictions for stable angina and chronic heart failure with reduced ejection fraction.
This Evidence Pack contains **no TxGNN predicted indications** — the malformed drug name field caused the prediction pipeline to return zero results.
A full repurposing evaluation **cannot be completed** until the input data is corrected and the pipeline is re-run.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available — no Singapore registration data |
| Predicted New Indication | None — TxGNN prediction not generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | N/A — no predictions available |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why This Report Cannot Proceed to Full Evaluation

Two structural problems prevent evaluation:

**Problem 1 — Malformed drug identifier.** The `inn` field contains `"5.390 MG OF IVABRADINE HYDROCHLORIDE)"` — a dosage string with an unmatched parenthesis, not a standard INN. The correct INN is simply `ivabradine`. This caused the TxGNN pipeline's drug lookup to fail, resulting in `predicted_indications: []` and no DrugBank ID resolution.

**Problem 2 — No Singapore market data.** With zero HSA registrations on record, the regulatory context for a repurposing pathway is entirely absent.

**What is known about Ivabradine from published sources:**
Ivabradine selectively inhibits the If current in the sinoatrial node, reducing heart rate without affecting myocardial contractility or conduction — a mechanism distinct from beta-blockers and calcium channel blockers. It is approved in the EU (Procoralan, Servier), the US (Corlanor, Amgen), and several Asia-Pacific markets for stable angina and HFrEF. Its pure chronotropic effect has been studied in conditions ranging from inappropriate sinus tachycardia to POTS (postural orthostatic tachycardia syndrome). Had the pipeline run successfully, these are likely candidate areas TxGNN would have flagged.

---

## Clinical Trial Evidence

Currently no related clinical trials registered in this Evidence Pack.

---

## Literature Evidence

Currently no related literature available in this Evidence Pack.

---

## Singapore Market Information

Ivabradine is currently **not registered** in Singapore (HSA). No product authorisations are on record.

> **Context:** Ivabradine (Coralan/Procoralan) holds regulatory approval in the EU, US, Australia, and several Asian markets. Its absence from Singapore's register most likely reflects a commercial market-access decision by the originator (Servier) rather than a safety or efficacy rejection by HSA.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No TxGNN predictions were generated due to a malformed drug name input, making it impossible to evaluate any repurposing hypothesis. Without predicted indications, there is no candidate to assess.

**To proceed, the following is needed:**

1. **Fix the `inn` field** — Replace `"5.390 MG OF IVABRADINE HYDROCHLORIDE)"` with the correct INN: `"ivabradine"`
2. **Re-run TxGNN pipeline** — Execute KG and DL predictions with the corrected drug name to generate predicted indications
3. **Re-query DrugBank** — Use `ivabradine` to retrieve the DrugBank ID, MOA, safety warnings, and contraindications (DrugBank query log shows `result_count: 1`, so data exists but was not mapped due to the malformed name)
4. **Verify Singapore HSA registration** — Perform a direct search in HSA PRISM using `ivabradine` to confirm whether any products are registered
5. **Re-generate Evidence Pack** — Once the above inputs are corrected, regenerate the full Evidence Pack at version ≥ v5 and re-run this report
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

