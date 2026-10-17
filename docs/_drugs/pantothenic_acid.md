---
layout: default
title: Pantothenic Acid
parent: Low Evidence (L5)
nav_order: 762
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pantothenic Acid: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Ascorbic acid deficiency, scurvy"
monitor_inn: "Pantothenic acid"
predicted_indications: ["congenital prothrombin deficiency", "ochronosis disorder", "glycerol metabolism disease", "folic acid deficiency anemia", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "urinary tract infection (disease)", "gonococcal urethritis", "Ureaplasma urethritis", "Keshan disease"]
---

# Pantothenic Acid
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

# Pantothenic Acid: From Ascorbic Acid Deficiency / Scurvy to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (vitamin B5) is a vitamin used for nutritional deficiency states, and in the knowledge graph it is linked to ascorbic acid deficiency and scurvy.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, with a very high score. However, there are **0 clinical trials** and **0 publications** supporting this prediction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ascorbic acid deficiency, scurvy (from the knowledge graph; no approved indication text is available in the Singapore licence record) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pantothenic acid is a vitamin and a precursor of coenzyme A, which participates broadly in lipid and energy metabolism. It is supplied in Singapore as part of a multivitamin injection.

For the top-ranked prediction, the connection is weak. Congenital prothrombin deficiency is a genetic coagulation factor disorder (F2 gene), and pantothenic acid has no known role in prothrombin synthesis or function. The high TxGNN score is a model output only and is not backed by any trial or publication. The original indications (vitamin deficiency states) are nutritional, while the predicted one is a genetic bleeding disorder, so the two do not share an obvious pathway.

Among the other predictions in the list, some have a more plausible, though still limited, rationale:

- **Folic acid deficiency anemia (score 99.60%, L4):** B-vitamin deficiencies often co-occur, and historical animal work links pantothenic acid and folic acid deficiencies to anemia and granulocytopenia. Folate repletion remains the standard treatment, and no human trial supports pantothenic acid for this condition.
- **Uterine inflammatory disease (score 99.14%, L4):** A 2026 mouse study reports that pantothenic acid alleviates vagotomy-induced endometrial injury. This is a single preclinical model and is hypothesis-generating only.

The remaining predictions (ochronosis, glycerol metabolism disease, xanthogranulomatous pyelonephritis, urinary tract infection, gonococcal urethritis, Ureaplasma urethritis, Keshan disease) have no supportive evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital prothrombin deficiency, or for any of the other top-10 predicted indications.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

For reference, literature retrieved for lower-ranked predictions is summarised below. None of it supports the top prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41223999](https://pubmed.ncbi.nlm.nih.gov/41223999/) | 2026 | Preclinical (mouse) | Mucosal Immunology | Pantothenic acid alleviated vagotomy-induced endometrial injury (uterine inflammatory disease) |
| [21021037](https://pubmed.ncbi.nlm.nih.gov/21021037/) | 1946 | Historical report | Nutrition Reviews | Anemia and granulocytopenia in relation to pantothenic acid and folic acid deficiencies (folic acid deficiency anemia) |
| [21929634](https://pubmed.ncbi.nlm.nih.gov/21929634/) | 2011 | Review | Maternal & Child Nutrition | Fortified foods for pregnant and lactating women and their effect on nutritional status (folic acid deficiency anemia) |
| [3724048](https://pubmed.ncbi.nlm.nih.gov/3724048/) | 1986 | Review | Laboratory Animal Science | Nutritional deficiency anemias in nonhuman primates, including pantothenic acid and folic acid (folic acid deficiency anemia) |
| [20505214](https://pubmed.ncbi.nlm.nih.gov/20505214/) | 2010 | Observational metabolomics | Science Translational Medicine | Plasma metabolic signatures of exercise; pantothenate appears only as one detected metabolite (glycerol metabolism disease) |
| [22380686](https://pubmed.ncbi.nlm.nih.gov/22380686/) | 2012 | Preclinical metabolomics | Journal of Proteome Research | Liver metabolomics in aged rats; not a pantothenic acid treatment study (glycerol metabolism disease) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11975P | CERNEVIT FOR INJECTION | Injection, powder, for solution | Not stated in the available record |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, sickle cell anemia, hereditary persistence of fetal hemoglobin, primary hyperoxaluria, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease. These come from model-graph contraindication edges and should be verified against the product label.

Please refer to the package insert for other safety information, including warnings and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, congenital prothrombin deficiency, rests on a model score alone. There are no trials or publications, and pantothenic acid has no known role in prothrombin biology. The Singapore product is a multivitamin injection, and the available safety data are incomplete.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the registered product (currently missing and blocking safety screening)
- Mechanism of action data for pantothenic acid
- A defined biological hypothesis linking coenzyme A metabolism to prothrombin synthesis, if this prediction is to be pursued at all
- Consideration of folic acid deficiency anemia and uterine inflammatory disease as better-supported research questions (L4), starting with human observational data or well-designed preclinical work
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

