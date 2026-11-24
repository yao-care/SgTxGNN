---
layout: default
title: Empagliflozin
parent: Low Evidence (L5)
nav_order: 371
evidence_level: L5
indication_count: 3
monitor_inn: "Empagliflozin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
last_modified_at: 2026-11-20
description: "Empagliflozin: predicted new indication Classic stiff person syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
---

# Empagliflozin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Empagliflozin: From Type 2 Diabetes Mellitus to Classic Stiff Person Syndrome
{: .text-alpha }

## One-Sentence Summary

Empagliflozin was originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (relation recorded in the knowledge graph; no approved indication text is available in the local licence records) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 10 of 10) |
| Number of Registrations | 10 (valid: 10) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for empagliflozin: "Empagliflozin is an inhibitor of SGLT2, the predominant transporter responsible for reabsorption of glucose from the glomerular filtrate back into the circulation. By inhibiting SGLT2, empagliflozin reduces renal reabsorption of filtered glucose and lowers the renal threshold for glucose, and thereby increases urinary glucose excretion." ([DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565), label version 2026-11-10; accessed 2026-11-19.) Empagliflozin is generally known as an SGLT2 inhibitor used in type 2 diabetes, but this was not supplied, so no mechanistic link can be drawn from the available data.

Stiff person syndrome is an autoimmune disorder of GABA- and glycine-mediated inhibitory neurotransmission, usually associated with anti-GAD65 antibodies. No plausible pathway connecting SGLT2 inhibition to this process is evident. The high score is a computational prediction and is not corroborated by any trial or publication.

Two other predictions are similar in nature:
- **Focal stiff limb syndrome** (score 0.9906): it has the same score as classic stiff person syndrome. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- **Opsismodysplasia** (score 0.9903): a rare skeletal dysplasia caused by INPPL1 (SHIP2) loss of function. A theoretical link via insulin/PI3K signalling exists, but it is speculative, and the paediatric skeletal setting raises additional safety questions.

All three are at evidence level L5 with no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14686P | JARDIANCE FILM-COATED TABLETS 10MG | TABLET, FILM COATED | Valid |
| SIN14687P | JARDIANCE FILM-COATED TABLET 25MG | TABLET, FILM COATED | Valid |
| SIN17547P | EMPAZOX 25 Empagliflozin Film Coated Tablets 25 mg | TABLET, FILM COATED | Valid |
| SIN17548P | EMPAZOX 10 Empagliflozin Film Coated Tablets 10 mg | TABLET, FILM COATED | Valid |
| SIN15061P | JARDIANCE DUO FILM COATED TABLET 12.5MG/1000MG | TABLET, FILM COATED | Valid |

Showing 5 of 10 HSA registrations.

<!-- licenses:end -->

All are oral film-coated tablets. Some of these products are combination products (names such as Jardiance Duo and Glyxambi indicate combinations), so their licences do not describe the single-ingredient drug's approval on their own.

<!-- review:begin sg-lic-20261106-empagliflozin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "Eight valid registrations are on record in total; the table shows the first five. All are oral film-coated tablets." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The Quick Overview and the table under Singapore Market Information show the current number of HSA registrations. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-empagliflozin-1 -->

## Safety Considerations

### Drug Interactions
The interaction query returned 100 records; the most notable moderate-level examples include:
- Phenylephrine, pseudoephedrine, epinephrine
- Acebutolol, nifedipine, fosinopril
- Furosemide, acetazolamide
- Formoterol, salbutamol
- Hydrocortisone, ethinylestradiol
- Ethanol

Topical hydrocortisone and topical alclometasone are listed as minor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or publications for classic stiff person syndrome, no mechanism data, and no plausible biological link. This is evidence level L5.

**To proceed, the following is needed:**
- Mechanism of action data for empagliflozin, and a plausible rationale linking it to stiff person syndrome
- Preclinical or case-level evidence in stiff person syndrome or related autoimmune neurological conditions
- Package insert warnings and contraindications from HSA (currently a blocking gap for safety screening)
- Review of the interaction profile in the context of the target population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Eight valid registrations are on record in total; the table shows the first five" | Corrected (revised 2026-11-24; earlier version kept in the record) | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Jardiance (empagliflozin) prescribing information, Boehringer Ingelheim Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=faf3dd6a-9cd0-39c2-0d2e-232cb3f67565) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

