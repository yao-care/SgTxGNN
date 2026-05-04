---
layout: default
title: Abacavir Sulfate 702 762 Mg Eqv Abacavir
parent: 僅模型預測 (L5)
nav_order: 21
evidence_level: L5
indication_count: 0
---

# Abacavir Sulfate 702 762 Mg Eqv Abacavir
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

# Abacavir Sulfate: Drug Repurposing Evaluation — Insufficient Data for TxGNN Prediction

---

## One-Sentence Summary

Abacavir Sulfate is a nucleoside reverse transcriptase inhibitor (NRTI) widely used in HIV-1 combination antiretroviral therapy worldwide, though it currently has no Singapore HSA registration in this dataset.
The TxGNN model was **unable to generate any repurposing predictions** for this drug in the current pipeline run — most likely due to an unresolved DrugBank ID and a malformed drug name string containing dosage information.
This report documents the root causes of pipeline failure and recommends specific remediation steps before re-evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in current dataset |
| Predicted New Indication | No predictions generated |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 — model prediction stage not reached |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

No repurposing predictions were generated in this pipeline run, so a mechanism-to-indication rationale cannot be completed at this stage.

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmaceutical knowledge, Abacavir Sulfate is a nucleoside reverse transcriptase inhibitor (NRTI). After intracellular phosphorylation to carbovir triphosphate, it competitively inhibits HIV-1 reverse transcriptase and acts as a chain terminator during viral DNA synthesis. Its efficacy in HIV-1 infection is well-established; its known expected DrugBank entry is DB01048.

The TxGNN pipeline failure most likely has three compounding causes: (1) the `inn` field contains a full dispensing string — `"ABACAVIR SULFATE 702.762 MG EQV. ABACAVIR"` — rather than a clean INN, causing the name normalizer to fail to match against the DrugBank vocabulary; (2) the `drugbank_id` field is `null`, which prevents the knowledge graph from locating the node for this drug; and (3) the `original_indications` array is empty, removing a fallback signal for disease context. All three issues must be resolved before the prediction step can proceed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered — no repurposing indication was predicted for this drug in the current pipeline run.

---

## Literature Evidence

Currently no related literature available — no repurposing indication was predicted for this drug in the current pipeline run.

---

## Singapore Market Information

Abacavir Sulfate is currently **not registered** with Singapore's Health Sciences Authority (HSA) under this drug entry. No active licenses were found in the regulatory dataset.

> **Note:** Abacavir-containing combination products (e.g., Ziagen®, Kivexa®/Epzicom®) may be registered under separate HSA entries. A targeted HSA registry search using the brand name and/or the active ingredient "abacavir" is recommended to confirm actual market presence before concluding the drug is unavailable in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Known class-level alert (not from Evidence Pack):** Abacavir carries a Black Box Warning for hypersensitivity reactions associated with the HLA-B\*57:01 allele, and for lactic acidosis/severe hepatomegaly with steatosis. HLA-B\*57:01 screening is mandatory before initiation. This information should be formally captured via TFDA/HSA package insert retrieval to close Data Gap DG001.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction pipeline did not reach the scoring stage due to a malformed drug name string and a missing DrugBank ID, making it impossible to evaluate any repurposing hypothesis at this time. No safety screening has been completed either, as all warning/contraindication fields remain unresolved.

**To proceed, the following is needed:**

- **Fix drug name normalisation** — Strip dosage information from the `inn` field; use clean INN `"abacavir"` as the query string
- **Resolve DrugBank ID** — Query DrugBank API for `"abacavir"`; expected result: `DB01048`
- **Populate `original_indications`** — After DrugBank resolution, extract approved indications (HIV-1 infection) to provide disease context for the pipeline
- **Obtain MOA data** — Retrieve mechanism of action from DrugBank after ID resolution (closes DG002)
- **Retrieve Singapore/HSA package insert** — Search HSA registry for Ziagen® or Kivexa® to obtain warnings and contraindications (closes DG001)
- **Re-run TxGNN prediction pipeline** — After all above remediation steps, re-run to generate ranked repurposing candidates
- **Confirm Singapore market presence** — Perform a targeted HSA registry search by ingredient name before concluding "Not marketed"
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

