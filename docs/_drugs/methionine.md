---
layout: default
title: Methionine
parent: Low Evidence (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
monitor_inn: "Methionine"
predicted_indications: ["acne (disease)", "severe nonproliferative diabetic retinopathy", "craniostenosis cataract", "mature cataract", "immature cataract", "diabetes mellitus type 2 associated cataract", "cortical cataract", "tetanic cataract", "nuclear senile cataract", "diabetic cataract"]
last_modified_at: 2026-10-23
description: "Methionine: predicted new indication Acne (disease) (evidence level L5). Approved use: Not stated in the licence records"
---

# Methionine
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

## Methionine: From Parenteral Nutrition Amino Acid Component to Acne
{: .text-alpha }

## One-Sentence Summary

Methionine is an essential amino acid, and in Singapore it is registered as an ingredient of parenteral nutrition and amino acid infusion products. The TxGNN model predicts it may be useful for **acne (disease)**, but there are **0 clinical trials** and only **2 publications** that touch the topic, neither of which tests methionine as a treatment. The prediction should be treated as a hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (all 19 licences have empty indication text); registered as an amino acid component of infusion and parenteral nutrition products |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 19 of 19) |
| Number of Registrations | 19 (valid: 19) |
| Recommended Decision | Hold |

*Evidence level note:* the data compiled for this report assigned L4 to acne, but neither cited paper directly studies methionine for acne (one is a gene mutation case report, the other describes a side effect of isotretinoin). Under the evidence ceiling rule this is therefore L5.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Methionine is a sulfur-containing essential amino acid that takes part in protein synthesis and in the methionine/homocysteine one-carbon metabolic cycle. In Singapore it is used as one component of amino acid solutions for intravenous nutrition.

The link to acne is weak. One retrieved paper is a case report of an MTHFR mutation in a neonate with encephalopathy, hair loss and neonatal acne; it concerns the homocysteine/methionine cycle but not acne treatment. The other reports raised plasma homocysteine in patients taking isotretinoin for cystic acne, which describes a drug side effect on one-carbon metabolism and not a therapeutic role for methionine. Supplementing methionine could even raise homocysteine, which is a potential concern. The very high TxGNN score is therefore not backed by clinical data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort | Int J Dermatol | Plasma homocysteine was elevated in patients receiving isotretinoin for cystic acne; this is a drug side-effect observation and does not test methionine as a treatment |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case report | BMJ Case Reports | Novel MTHFR mutation in a neonate with encephalopathy, hair loss, marfanoid features and neonatal acne; not related to methionine therapy for acne |

## Singapore Market Information

All 19 licences are valid single-ingredient entries; the licence records contain no approved indication text. The five below are examples.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16337P | AMINOVEN SOLUTION FOR INFUSION 15% | Infusion, solution | Not stated in licence record |
| SIN11682P | AMINOVEN SOLUTION FOR INFUSION 5% | Injection | Not stated in licence record |
| SIN06299P | NEPHROSTERIL FOR INTRAVENOUS INFUSION | Injection | Not stated in licence record |
| SIN08352P | AMINOPLASMAL-15% INFUSION | Injection | Not stated in licence record |
| SIN14286P | SmofKabiven Emulsion for Infusion | Injection, emulsion | Not stated in licence record |

All registered forms are injectable or infusion products (plus one sterile peritoneal dialysis solution); no oral or topical methionine product is listed, so route compatibility for acne has not been assessed.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** the TxGNN knowledge graph links methionine to contraindication relations with, among others, kidney disease (including chronic and end-stage renal failure), nephrolithiasis, hypertension, heart disease and cardiovascular disease, diabetes mellitus and diabetic ketoacidosis, hyperlipidemia, hypercalcemia, phenylketonuria and other phenylalanine metabolism disorders, sarcoidosis, digitalis poisoning and ventricular fibrillation. These need verification against the product labels.
- **Drug Interactions** (5 recorded):
  - Activated charcoal: Moderate
  - Ephedrine, pseudoephedrine, mexiletine, flecainide: Minor
- **Other concern:** methionine is converted to homocysteine, and raised homocysteine is a possible vascular risk, so safety and direction of effect must be clarified before any use for acne.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no clinical trial exists and neither retrieved paper tests methionine for acne. The mechanistic link is unsupported and may even point the wrong way because of homocysteine. Evidence is at L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA)
- Mechanism of action data for methionine
- Preclinical or clinical evidence that methionine, rather than its metabolites, affects acne
- Homocysteine safety assessment and clarification of a suitable (non-parenteral) route
- Review of the other lower-ranked predictions: diabetic cataract has the most relevant mechanistic literature (methionine sulfoxide reductase in lens cells), but it is preclinical, concerns the endogenous repair enzyme rather than methionine supplementation, and has no clinical trials; it is best treated as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

