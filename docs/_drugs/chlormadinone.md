---
layout: default
title: Chlormadinone
parent: Low Evidence (L5)
nav_order: 239
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlormadinone: predicted new indication Antithrombin deficiency type 2 (evidence level L5). Approved use: Not stated in the registration data (the product is a combined oral c…"
monitor_inn: "Chlormadinone"
predicted_indications: ["antithrombin deficiency type 2", "heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "candidiasis", "plasma cell myeloma", "heart neoplasm", "rheumatoid arthritis", "indolent plasma cell myeloma", "gout", "thrombophilia"]
---

# Chlormadinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Chlormadinone: From Contraception (Oral Hormonal) to Antithrombin Deficiency Type 2

## One-Sentence Summary

Chlormadinone is a synthetic progestogen (antigonadotropic and antiandrogenic) that is marketed in Singapore as part of an oral combined contraceptive product.
The TxGNN model predicts it may be effective for **antithrombin deficiency type 2**, but **no clinical trials** and **no supporting publications** exist for this prediction.
The prediction is a computational signal only, and the available evidence points more toward a thrombotic safety concern than a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (the product is a combined oral contraceptive tablet) |
| Predicted New Indication | Antithrombin deficiency type 2 |
| TxGNN Prediction Score | 98.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, chlormadinone is a progestogen with antigonadotropic and antiandrogenic activity. It is used in hormonal contraception, but no established mechanism links it to correcting antithrombin deficiency.

Antithrombin deficiency type 2 is a hereditary coagulation disorder that raises the risk of thrombosis. Hormonal agents are generally a thrombotic concern in this population rather than a treatment. The high score most likely reflects proximity to coagulation-related nodes in the knowledge graph, not a real pharmacological relationship.

The other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Heparin cofactor 2 deficiency | 98.67% | L5 | No plausible pathway; likely graph proximity |
| 3 | Factor 5 excess with spontaneous thrombosis | 98.64% | L5 | Prothrombotic state; not expected to respond to a progestogen |
| 4 | Candidiasis | 98.62% | L5 | Only a 1967 general review; hormonal contraceptives are if anything linked to higher candidiasis risk |
| 5 | Plasma cell myeloma | 97.89% | L5 | No established link |
| 6 | Heart neoplasm | 97.77% | L5 | Only a general 1990 safety review |
| 7 | Rheumatoid arthritis | 97.72% | L5 | Only a 1971 biomarker observation in healthy women |
| 8 | Indolent plasma cell myeloma | 97.68% | L5 | Overlaps with the myeloma signal |
| 9 | Gout | 97.68% | L5 | No established link |
| 10 | Thrombophilia | 97.66% | L4 | Literature concerns safety of progestogen use, not treatment |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For the lead prediction (antithrombin deficiency type 2), currently no related literature is available.

The most relevant publications were found for the related prediction **thrombophilia** (rank 10). They concern the safety of progestogens in women at high thrombotic risk, not therapeutic benefit:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15541404](https://pubmed.ncbi.nlm.nih.gov/15541404/) | 2004 | Cohort (retrospective) | Contraception | Compared women at high risk of venous thromboembolism using antigonadotropic-dose chlormadinone acetate (n=102) with matched women using no hormonal contraception; assesses the venous impact of progestogen-only contraception |
| [25961217](https://pubmed.ncbi.nlm.nih.gov/25961217/) | 2010 | Review | Hormone Molecular Biology and Clinical Investigation | Antigonadotropic progestogens as contraceptive options for women who cannot use the combined pill |
| [15333036](https://pubmed.ncbi.nlm.nih.gov/15333036/) | 2004 | Cohort (cross-sectional) | Journal of Thrombosis and Haemostasis | Assessed the effect of a chlormadinone acetate progestagen-only pill on activated protein C resistance |
| [1199513](https://pubmed.ncbi.nlm.nih.gov/1199513/) | 1975 | Cohort | Zentralblatt fur Gynakologie | Fibrinolytic split products increased during use of several hormonal contraceptives, including a chlormadinone acetate combination |

Other single references found for lower-ranked predictions are general or biomarker papers that do not show efficacy: candidiasis ([5337087](https://pubmed.ncbi.nlm.nih.gov/5337087/), 1967 review), heart neoplasm ([2170823](https://pubmed.ncbi.nlm.nih.gov/2170823/), 1990 review of estrogen and progestogen risks) and rheumatoid arthritis ([4994393](https://pubmed.ncbi.nlm.nih.gov/4994393/), 1971 cohort of autoantibodies in healthy women using oral contraceptives).

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14870P | BELARA film-coated tablet 0.03mg/2mg (Gedeon Richter Plc.) | Film-coated tablet (oral) | Not stated in the registration data |

---

## Safety Considerations

Please refer to the package insert for safety information.

One point from the compiled literature deserves attention: progestogens may influence activated protein C resistance and coagulation markers, which is a thrombotic safety concern for patients with thrombophilia or inherited coagulation disorders. This needs careful evaluation before any use in such populations.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a computational score, with no clinical trials and no publications for antithrombin deficiency type 2. There is no plausible mechanism, and hormonal agents are generally a thrombotic concern in this population. The same applies to the other top-ranked predictions, none of which is supported above L5 (thrombophilia reaches L4, but its literature addresses safety, not efficacy).

**To proceed, the following is needed:**
- The package insert warnings and contraindications for the registered product, which are not available and block safety screening
- Mechanism of action data for chlormadinone
- Evidence of a biological pathway linking chlormadinone to antithrombin or other coagulation-factor function, if one exists
- A thrombosis risk assessment specific to patients with hereditary coagulation disorders
- Review of the thrombophilia literature as a safety question (can chlormadinone be used as a contraceptive in this population) and not as a repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

