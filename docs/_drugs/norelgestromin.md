---
layout: default
title: Norelgestromin
parent: Low Evidence (L5)
nav_order: 720
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "Norelgestromin"
predicted_indications: ["amenorrhea (disease)"]
description: "Norelgestromin: predicted new indication Amenorrhea (disease) (evidence level L5). In Singapore: 1 HSA registration (1 valid)"
---

# Norelgestromin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Norelgestromin: Amenorrhea (disease)
{: .text-alpha }

## One-Sentence Summary

Norelgestromin is a progestin (the active metabolite of norgestimate), delivered in a transdermal contraceptive patch together with ethinyl estradiol.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials and no publications** were found to support this direction.
The prediction is based on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 0.9951 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for norelgestromin and ethinyl estradiol (a combination product containing norelgestromin): "NGMN is the active progestin largely responsible for the progestational activity that occurs in women following application of norelgestromin and ethinyl estradiol transdermal system." ([DailyMed: norelgestromin and ethinyl estradiol prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10fa1458-c8ed-4197-922a-1ba7271d2b02), label version 2026-04-16; accessed 2026-11-19.) Based on known information, norelgestromin is a progestin used in a combined hormonal contraceptive patch with ethinyl estradiol. It supplies exogenous hormonal support to the endometrium, so it may plausibly be applicable to functional amenorrhea or cycle regulation.

There are important caveats. Amenorrhea is also a recognised side effect of hormonal contraceptives, so the direction of effect (treating versus causing it) needs clarification. No studies of norelgestromin itself were retrieved, and the high score (0.9951) is a computational prediction only.

Other predicted indications follow the same pattern of weak support:
- **Acne (98.5%)**: combined hormonal contraceptives lower androgen output and sebum production. Norgestimate-containing products have acne data, but this is class-level, indirect support only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN12423P | EVRA TRANSDERMAL PATCH (6 mg/600 mcg) | PATCH | Valid |

<!-- licenses:end -->

Manufacturer: LTS Lohmann Therapie-Systeme AG. The registration is valid and is a single-ingredient listing.

## Safety Considerations

- **Drug Interactions**: One major interaction was identified, with **sugammadex** (source: DDInter).
- **Knowledge-graph contraindication signals**: These come from the TxGNN knowledge graph, not from label text, and should be verified against the package insert. Associated conditions include:
  - Cardiovascular and metabolic: hypertension, coronary artery disease, thrombophlebitis, diabetes mellitus and diabetic ketoacidosis, hyperglycaemia, hyperlipidaemia (including familial), hypertriglyceridaemia
  - Hepatic, renal and biliary: liver disease, kidney disease, gallbladder disease, pyoureter
  - Neurological and psychiatric: migraine, epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
  - Other: female breast carcinoma, porphyria (including inherited forms), systemic lupus erythematosus (including paediatric), asthma (including intrinsic and allergic), obsolete functional visual loss

Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is supported only by a model score. There are no clinical trials or publications for norelgestromin, the mechanism data is missing, and the direction of effect for amenorrhea is unclear. The knowledge-graph contraindication signals are also extensive.

**To proceed, the following is needed:**
- The package insert from the Health Sciences Authority (HSA), covering approved indications, warnings and contraindications
- Mechanism of action data (for example, from DrugBank)
- A literature and trial search for norelgestromin, norgestimate and combined hormonal contraceptives in amenorrhea, and in acne as a possible alternative lead
- Clarification of whether the prediction means treating or causing amenorrhea
- A route and formulation compatibility assessment, since the available product is a transdermal patch with a fixed dose combination

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: norelgestromin and ethinyl estradiol prescribing information, Zydus Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=10fa1458-c8ed-4197-922a-1ba7271d2b02) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

