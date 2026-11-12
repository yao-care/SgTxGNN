---
noindex: true
sitemap: false
layout: default
title: 84 Anhydrous Anidulafungin 122Mg Eqv Anidulafungin
parent: Low Evidence (L5)
nav_order: 16
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# 84 Anhydrous Anidulafungin 122Mg Eqv Anidulafungin
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

## Anidulafungin: Insufficient Data for Repurposing Evaluation
{: .text-alpha }

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal agent known for treating invasive candidiasis and candidaemia. The current Evidence Pack contains **no TxGNN predicted indications** and extensive data gaps across regulatory, safety, and mechanistic categories. Evaluation cannot proceed until foundational data is retrieved.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available in current data (anidulafungin is clinically used for invasive candidiasis / candidaemia) |
| Predicted New Indication | None — `predicted_indications` array is empty |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only; no actual study evidence retrieved) |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No predicted indications are available in this Evidence Pack, so a repurposing rationale cannot be constructed at this time.

What is known from published pharmacology: anidulafungin inhibits β-1,3-D-glucan synthase, an enzyme essential for fungal cell wall biosynthesis. This mechanism is highly specific to fungi and has no established parallel in mammalian cell biology, which makes broad oncological or inflammatory repurposing hypotheses less intuitive compared to, for example, kinase inhibitors or immunomodulators.

The drug name recorded in the pack — *"84% ANHYDROUS ANIDULAFUNGIN 122MG EQV. ANIDULAFUNGIN"* — appears to be a raw-material or bulk-ingredient specification rather than a finished product INN entry. This may have caused the TxGNN pipeline to fail drug-name normalisation, resulting in zero prediction output. Resolving the name to the standard INN **anidulafungin** (DrugBank: DB04834) before re-running the pipeline is the most likely fix.

---

## Clinical Trial Evidence

Currently no related clinical trials were retrieved for a predicted indication, as `predicted_indications` is empty.

---

## Literature Evidence

Currently no related literature is available for a predicted indication.

<!-- review:begin sg-lic-20261106-84_anhydrous_anidulafungin_122mg_eqv_anidulafungin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Anidulafungin holds no product registrations in Singapore at the time of this report." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 3 registrations for this drug, 3 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-84_anhydrous_anidulafungin_122mg_eqv_anidulafungin-1 -->

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN13585P | Eraxis 100mg For Injection | INJECTION, POWDER, LYOPHILIZED, FOR SOLUTION | Valid |
| SIN16106P | ANIDACCORD 100 POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100 MG | INJECTION, POWDER, FOR SOLUTION | Valid |
| SIN17508P | ANICURA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | INJECTION, POWDER, LYOPHILIZED, FOR SOLUTION | Valid |

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the package insert for safety information. All safety fields in this Evidence Pack are marked as data gaps:

- Key warnings: not retrieved
- Contraindications: not retrieved
- Drug-drug interactions: query returned no results

The DrugBank query did return one result (`result_count: 1`), but the data was not propagated into the pack. Re-running the DrugBank extraction step should recover MOA, warning, and interaction data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN pipeline returned zero predicted indications, most likely because the non-standard drug name string failed INN normalisation. Without a valid prediction, no repurposing evaluation can proceed.

**To proceed, the following is needed:**

1. **Resolve the drug name** — Map *"84% ANHYDROUS ANIDULAFUNGIN 122MG EQV. ANIDULAFUNGIN"* to the standard INN `anidulafungin` (DrugBank ID: DB04834) and re-run the TxGNN pipeline.
2. **Retrieve MOA data** — Pull mechanistic data from DrugBank (query already returned 1 result; extraction step needs to be re-executed).
3. **Retrieve safety data** — Download the Singapore HSA or reference-market package insert PDF and parse key warnings and contraindications (Data Gap DG001).
4. **Re-run the full evidence pipeline** — Once a valid predicted indication is available, re-collect ClinicalTrials.gov and PubMed evidence for that indication pair.

<!-- review:begin sg-lic-20261106-84_anhydrous_anidulafungin_122mg_eqv_anidulafungin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "**Re-run the full evidence pipeline** — Once a valid predicted indication is available, re-collect ClinicalTrials.gov and PubMed evidence for that indication pair. / **Confirm Singapore registration intent** — Since anidulafungin is currently unregistered in Singapore, confirm whether the repurposing study requires a new NDA or is intended for compassionate / named-patient use." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 3 registrations for this drug, 3 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-84_anhydrous_anidulafungin_122mg_eqv_anidulafungin-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Anidulafungin holds no product registrations in Singapore at the time of this report" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "5. **Confirm Singapore registration intent** — Since anidulafungin is currently unregistered in Singapore, confirm whether the repurposing s" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

