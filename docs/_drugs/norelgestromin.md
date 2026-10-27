---
layout: default
title: Norelgestromin
parent: Low Evidence (L5)
nav_order: 720
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Norelgestromin: predicted new indication Amenorrhea (evidence level L5). Approved use: Not stated in the Singapore registration data (the approved indicatio…"
monitor_inn: "Norelgestromin"
predicted_indications: ["amenorrhea (disease)", "acne (disease)", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia", "fat necrosis of breast", "breast abscess", "lactation disease", "primary ovarian failure"]
---

# Norelgestromin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Norelgestromin: From Hormonal Contraception to Amenorrhea
{: .text-alpha }

## One-Sentence Summary

Norelgestromin is a progestin (the active metabolite of norgestimate), delivered in a transdermal contraceptive patch together with ethinyl estradiol.
The TxGNN model predicts it may be effective for **amenorrhea**, but **no clinical trials and no publications** were found to support this direction.
The prediction is based on computation alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data (the approved indication text is blank) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, norelgestromin is a progestin used in a combined hormonal contraceptive patch with ethinyl estradiol. It supplies exogenous hormonal support to the endometrium, so it may plausibly be applicable to functional amenorrhea or cycle regulation.

There are important caveats. Amenorrhea is also a recognised side effect of hormonal contraceptives, so the direction of effect (treating versus causing it) needs clarification. No studies of norelgestromin itself were retrieved, and the high score (0.995) is a computational prediction only.

Other predicted indications follow the same pattern of weak support:
- **Acne (98.5%)**: combined hormonal contraceptives lower androgen output and sebum production. Norgestimate-containing products have acne data, but this is class-level, indirect support only.
- **Benign breast conditions** (fibrocystic disease, apocrine adenosis, blunt duct adenosis, benign mammary dysplasia): the link is speculative and likely reflects knowledge-graph proximity.
- **Primary ovarian failure (95.1%)**: hormone replacement is the standard of care, but contraceptive patch doses are not designed for replacement therapy.
- **Fat necrosis of breast, breast abscess, lactation disease**: no plausible therapeutic link. These are likely graph artefacts, and the lactation link suggests an adverse effect rather than a benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12423P | EVRA TRANSDERMAL PATCH (6 mg/600 mcg) | Patch | Not stated |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

