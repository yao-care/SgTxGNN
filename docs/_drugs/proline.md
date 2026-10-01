---
layout: default
title: Proline
parent: Low Evidence (L5)
nav_order: 822
evidence_level: L5
indication_count: 10
---

# Proline
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

# Proline: From Parenteral Amino Acid Nutrition to Congenital Prothrombin Deficiency

## One-Sentence Summary

Proline is an amino acid supplied in intravenous amino acid infusion products marketed in Singapore. The registration data does not state an approved indication, so its original use is inferred from the product types.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency** (score 98.9%), but **0 clinical trials** and **0 publications** support this prediction.
No plausible mechanism is evident, so the prediction is treated as a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in registration data (inferred: parenteral amino acid nutrition, based on product types such as Aminoven, Nephrosteril and Aminoplasmal) |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, proline is a proteinogenic amino acid, a nutritional component of intravenous amino acid infusions. Its role as a nutrient is established, but the mechanism cannot be cross-checked against the model score.

Mechanistically, the link to congenital prothrombin deficiency (factor II deficiency) is weak. This condition is a single-protein synthesis defect, and amino acid supplementation would not be expected to correct it. The high score (rank 11,253 in the model's ranking) is therefore best read as a statistical association in the knowledge graph, not a supported therapeutic rationale.

Among the other top-10 predictions, only **dyspepsia** (score 91.7%) has indirect supporting literature. Several metabolomic studies report altered arginine/proline metabolism in functional dyspepsia, but these are biomarker associations, not evidence that proline treats the condition. The one dyspepsia trial (NCT05876845) tests a pre-/pro-/post-biotic supplement, where "pro" means probiotic, so it does not test proline.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Registration data lists 19 licences in total. The five main ones are below. Approved indication text is not recorded for these products.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution | Fresenius Kabi Austria GmbH (Graz) |
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection | Fresenius Kabi Austria GmbH |
| SIN11829P | AMINOVEN SOLUTION FOR INFUSION 10% | Injection | Fresenius Kabi Austria GmbH |
| SIN06299P | NEPHROSTERIL FOR INTRAVENOUS INFUSION | Injection | Fresenius Kabi Austria GmbH |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection | B Braun Melsungen AG |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction rests on the model score alone, with no trials, no literature and no plausible mechanism. The evidence level is L5. Proline's role as a nutritional amino acid does not suggest correction of a congenital coagulation factor deficiency.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening), plus the approved indication text for the registered products
- Mechanism of action data for proline (for example from DrugBank), to allow a mechanistic cross-check of the score
- A review of the "obsolete vitamin D deficiency" mapping (rank 2), which should be redirected to a current vitamin D deficiency term
- Consideration of dyspepsia as a lower-priority research question (L4), starting with a targeted literature review of proline metabolism in functional dyspepsia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

