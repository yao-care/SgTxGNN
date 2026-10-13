---
layout: default
title: Finasteride
parent: Low Evidence (L5)
nav_order: 431
evidence_level: L5
indication_count: 10
---

# Finasteride
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

# Finasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, finasteride is a type II 5-alpha-reductase inhibitor that lowers dihydrotestosterone (DHT). Its efficacy in BPH is established, and DHT suppression is also the basis for its use in androgen-driven hair conditions.

The mechanistic link to the predicted indication is weak. Ambras syndrome is a congenital generalised hypertrichosis caused by genomic rearrangements affecting regulation of the TRPS1 gene. It is not primarily androgen-driven, so DHT suppression is not expected to address its underlying cause. The very high TxGNN score reflects a model output, not supporting experimental or clinical data.

For context, the second-ranked prediction, hypertrichosis (score 99.99%), is also only indirectly plausible. Hypertrichosis is by definition non-androgen-dependent excess hair growth, while finasteride acts on androgen-dependent hair growth. The lower-ranked predictions (for example prostate calculus, a possible BPH-mediated indirect link) have similarly limited direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for Ambras type hypertrichosis universalis congenita.

For the closely related predicted indication of general hypertrichosis, four publications were retrieved. None provides direct evidence for finasteride in that condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de dermatologie et de venereologie | Hypertrichosis is non-androgen-dependent, unlike hirsutism. Causes in adults include drugs, metabolic, nutritional and paraneoplastic factors |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Overview of new treatments for androgenetic alopecia and hirsutism |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Finasteride for male pattern hair loss; laser hair removal for hypertrichosis and hirsutism |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods | Der Hautarzt | TrichoScan digital hair analysis tool, not a treatment study |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15733P | FINAREX FILM-COATED TABLET 5MG | Film-coated tablet | Not specified |
| SIN16530P | FINAPECIA 1 FILM COATED TABLET 1 MG | Film-coated tablet | Not specified |
| SIN09921P | PROPECIA TABLET 1 mg | Film-coated tablet | Not specified |
| SIN14865P | STERCIA FILM-COATED TABLET 1MG | Film-coated tablet | Not specified |
| SIN07513P | PROSCAR TABLET 5 mg | Film-coated tablet | Not specified |

Ten single-ingredient oral licences are valid in total; none are cancelled.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text)**: liver disease and gallbladder disease.
- **Drug Interactions**: The interaction query returned 100 records. The examples listed (such as calcitriol, doxycycline, famotidine, acetylsalicylic acid, bupropion, omeprazole, metformin and morphine) have no severity level assigned, so their clinical significance is unclassified.
- **Pregnancy**: The model's rationale notes that finasteride carries a teratogenic risk in pregnancy, which is relevant to any use in congenital or neonatal conditions.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials or publications, and the mechanism is weak because Ambras syndrome is not primarily androgen-driven. Finasteride is already well established in Singapore for its original indication, but that does not support the new one.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently missing, which blocks safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Preclinical or mechanistic evidence linking DHT suppression to TRPS1-related hypertrichosis
- Any case reports or early-phase studies of finasteride in congenital hypertrichosis
- Review of the pregnancy and teratogenicity risk for the intended patient population
- Consideration of other predictions with more plausible links, such as prostate calculus (BPH-mediated)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

