---
layout: default
title: Leucine
parent: Low Evidence (L5)
nav_order: 590
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Leucine: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not stated in the registration records"
monitor_inn: "Leucine"
predicted_indications: ["congenital prothrombin deficiency", "gastroparesis (disease)", "acne (disease)", "bone Paget disease", "obsolete vitamin D deficiency", "postmenopausal osteoporosis", "sclerosing cholangitis", "pregnancy associated osteoporosis", "albinism-deafness syndrome", "Worth syndrome"]
---

# Leucine
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

## Leucine: From Parenteral Nutrition Amino Acid to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Leucine is an essential amino acid used as a component of parenteral nutrition and amino acid infusion products in Singapore.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
The prediction is purely computational, and its mechanistic basis is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (all 19 licences list no approved indication text); the products are amino acid infusion and parenteral nutrition formulations |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 98.999% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 19 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, leucine is a branched-chain essential amino acid, mainly supplied as part of amino acid infusions and combined parenteral nutrition products. Its role is nutritional support.

Congenital prothrombin deficiency is a monogenic disorder caused by variants in the F2 gene. We found no identifiable mechanistic link between leucine and prothrombin (Factor II) synthesis, and leucine supplementation is not expected to correct a genetic defect in this clotting factor. The high TxGNN score therefore looks like a computational artefact rather than a biologically grounded signal.

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital prothrombin deficiency.

## Literature Evidence

Currently no related literature available for congenital prothrombin deficiency.

### Other Predicted Indications Reviewed

The other top-ranked predictions were also reviewed. None shows convincing evidence of benefit.

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Gastroparesis | 98.85% | L5 | No supporting data; amino acids would more likely slow gastric emptying |
| Acne | 98.42% | L4 | Likely the opposite direction: leucine activates mTORC1, which is implicated in acne. The one matching trial (NCT07277075) studies a different protein (LRG1) and matches by name only |
| Bone Paget disease | 98.00% | L5 | Literature concerns SQSTM1 mutations, not leucine therapy |
| Obsolete vitamin D deficiency | 97.67% | L5 | No data; the disease term is obsolete |
| Postmenopausal osteoporosis | 97.42% | L4 | Most plausible but still indirect (see below) |
| Sclerosing cholangitis | 97.18% | L5 | Incidental literature; a leucine-containing peptide causes cholangitis in rats |
| Pregnancy associated osteoporosis | 96.57% | L5 | Only an animal study of the leucine metabolite HMB |
| Albinism-deafness syndrome | 96.43% | L5 | No data |
| Worth syndrome | 96.33% | L5 | No data |

**Postmenopausal osteoporosis** is the most plausible secondary lead. Its related trial is [NCT01757340](https://clinicaltrials.gov/study/NCT01757340), a completed, non-phased study with 43 obese postmenopausal women. It tested calorie restriction with leucine supplementation and measured insulin sensitivity, muscle mass and function, and bone mineral density. It did not enrol patients with diagnosed osteoporosis. The literature consists mainly of metabolomic associations and preclinical studies. These show that amino acid profiles are linked to low bone density but not that leucine treats it. This direction is worth treating as a research question only.

## Singapore Market Information

Leucine is registered in Singapore as a single-ingredient component of 19 valid licences. All are infusion or emulsion products, and none has approved indication text on record. Five main licences:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution | Not stated |
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection | Not stated |
| SIN06299P | NEPHROSTERIL FOR INTRAVENOUS INFUSION | Injection | Not stated |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection | Not stated |
| SIN14286P | SmofKabiven Emulsion for Infusion | Injection, emulsion | Not stated |

## Safety Considerations

- **Disease associations flagged by the knowledge graph (not label text)**: Leucine is linked to contraindication edges for several conditions. These include kidney disease (chronic kidney disease, end-stage renal failure, chronic renal failure syndrome), nephrolithiasis and nephrocalcinosis, hypercalcemia and sarcoidosis, heart disease and cardiovascular disease, ventricular fibrillation, digitalis poisoning, phenylketonuria and other phenylalanine metabolism disorders, and acute urate nephropathy. These are model-derived signals and need to be verified against the product labels.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, congenital prothrombin deficiency, is a monogenic clotting factor disorder with no mechanistic link to leucine and no trials or literature. The other predictions are also unsupported, and some may point in the opposite direction, such as acne. Postmenopausal osteoporosis is the only direction with partial, indirect support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, so that safety screening can begin
- Mechanism of action data for leucine (for example from DrugBank)
- For osteoporosis as a secondary lead, a focused review or trial in patients with diagnosed osteoporosis, with bone endpoints
- A renal and metabolic safety assessment for the target populations, given the knowledge graph signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

