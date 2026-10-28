---
layout: default
title: Maraviroc
parent: Low Evidence (L5)
nav_order: 636
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Maraviroc: predicted new indication Multiple endocrine neoplasia (evidence level L5). Approved use: Not available in the registration data"
monitor_inn: "Maraviroc"
predicted_indications: ["multiple endocrine neoplasia", "acne (disease)", "primary cutaneous T-cell lymphoma", "pediatric systemic lupus erythematosus", "primary cutaneous T-cell non-Hodgkin lymphoma", "primary cutaneous B-cell lymphoma", "candidiasis", "complement component 4a deficiency", "cytomegalovirus infection", "HER2 positive breast carcinoma"]
---

# Maraviroc
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

## Maraviroc: From an Unspecified Original Indication to Multiple Endocrine Neoplasia
{: .text-alpha }

## One-Sentence Summary

Maraviroc is a CCR5 antagonist marketed in Singapore as an oral film-coated tablet. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia** with a very high score, but **no clinical trials and no publications** currently support this prediction, so it remains a purely computational signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the registration data |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 0.9982 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. What is known is that maraviroc is a CCR5 antagonist, a drug that blocks a chemokine receptor involved in immune-cell trafficking.

No CCR5-related mechanism linking maraviroc to multiple endocrine neoplasia syndromes (such as MEN1 or RET-driven endocrine tumours) is evident. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis only.

**Other predicted indications (for context):** All of the following are also at Hold, except the last, which is classed as a research question:
- Acne, pediatric systemic lupus erythematosus, primary cutaneous B-cell lymphoma and complement component 4a deficiency: model predictions with no trials or literature.
- Primary cutaneous T-cell lymphoma and T-cell non-Hodgkin lymphoma: a plausible but indirect chemokine-trafficking rationale. The only citation is a 2023 review of ACKR1, an atypical chemokine receptor, which does not test maraviroc.
- Candidiasis and cytomegalovirus infection: the cited papers concern HIV populations and do not show a therapeutic effect of maraviroc.
- **HER2-positive breast carcinoma (research question):** this is the most mechanistically coherent link. A 2020 preclinical study reported that autocrine CCL5 mediates trastuzumab resistance via ERK pathway activation, suggesting CCR5 blockade could potentially reverse resistance. The evidence is preclinical and indirect, with no clinical trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (multiple endocrine neoplasia), currently no related literature is available.

For reference, the most mechanistically relevant item among the other predicted indications:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32404410](https://pubmed.ncbi.nlm.nih.gov/32404410/) | 2020 | Preclinical/Mechanistic | Molecular Cancer Therapeutics | Autocrine CCL5 drives trastuzumab resistance through ERK pathway activation in HER2-positive breast cancer (predicted indication rank 10) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13640P | Celsentri Film-Coated Tablet 150mg | Tablet, film coated | Not available |

Manufacturer: Pfizer Manufacturing Deutschland GmbH. Route: oral.

## Safety Considerations

- **Contraindication signals (knowledge graph, not label text):** The TxGNN knowledge graph links maraviroc to the following conditions, among others:
  - Liver conditions: liver disease, drug-induced liver injury, chronic hepatitis B and hepatitis C virus infection.
  - Kidney conditions: kidney disease, chronic kidney disease, end-stage renal failure.
  - Cardiovascular conditions: coronary artery disease, myocardial infarction, myocardial ischemia, coronary thrombosis.
  - Orthostatic conditions: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy.
  - Other: gallbladder disease, hemoglobinopathy, pyoureter, infectious disease.

  These come from knowledge graph edges and need confirmation against the official label.
- **Drug Interactions:** 93 interactions were identified. Examples:
  - **Major:** clarithromycin.
  - **Moderate:** aprepitant, dexamethasone, cimetidine, cobicistat, miconazole, clotrimazole, rolapitant, eliglustat, naltrexone, deferasirox, promethazine, among others.

  Many of these likely relate to CYP3A-mediated metabolism, though the data do not state the mechanism.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for multiple endocrine neoplasia rests on a very high model score alone (Evidence Level L5). There are no trials or publications, and no plausible mechanistic link. Among the other predicted indications, only HER2-positive breast carcinoma has a coherent but preclinical rationale, and it is best treated as a research question rather than a clinical recommendation.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications, approved indication), which is currently a blocking gap for safety screening
- Mechanism of action data, to support mechanistic-link analysis
- Any biological evidence connecting CCR5 signalling to multiple endocrine neoplasia, or a decision to move to a better-supported candidate such as HER2-positive breast cancer (with preclinical validation of CCL5-CCR5 blockade)
- Review of the major and moderate drug interactions and the knowledge-graph contraindication signals (liver, kidney, cardiovascular) before any use in a new patient population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

