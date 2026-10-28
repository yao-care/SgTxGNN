---
layout: default
title: Darunavir
parent: Low Evidence (L5)
nav_order: 305
evidence_level: L5
indication_count: 4
monitor_inn: "Darunavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-28
description: "Darunavir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Darunavir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Darunavir: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Darunavir is an HIV protease inhibitor, and HIV infection and AIDS are its original uses.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary disease.
There are **no clinical trials** and **no publications** that directly study this disease, so the support is model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this report. Darunavir is known as an HIV-1 protease inhibitor, a class of drugs that blocks the enzyme the virus needs to mature into infectious particles.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, so a mechanistic rationale is plausible. However, FIV protease differs structurally from HIV-1 protease, and darunavir's activity against it is not established in the data compiled for this report. The high score is a computational prediction only.

This is also a veterinary condition, so its relevance to human drug repurposing is limited. The other predicted indications are weaker still:

- **Simian immunodeficiency virus infection (score 0.9997)**: Four preclinical macaque studies were found, but they test combination antiretroviral regimens or adjunct agents and do not isolate darunavir's own effect. It is an animal research model, not a human treatment indication. These studies do not directly address feline AIDS.
- **Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter (0.9997)**: No mechanistic link is evident, and the very high score likely reflects TxGNN model (deep learning) artifacts.
- **Obsolete familial combined hyperlipidemia (0.9919)**: HIV protease inhibitors are associated with dyslipidemia, which runs opposite to a therapeutic benefit. The disease term is also obsolete in the ontology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for feline acquired immunodeficiency syndrome.

For the related simian immunodeficiency virus prediction, the following preclinical macaque studies were found. They are indirect evidence only.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Preclinical NHP study | AIDS Res Hum Retroviruses | Comparison of two injectable combination ART regimens in SIV-infected rhesus macaques |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Preclinical NHP study | PLoS Pathog | Highly intensified multidrug ART gave long-term viral suppression and restricted the viral reservoir in a simian AIDS model |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Preclinical NHP study | PLoS One | Suppressive ART plus the HDAC inhibitor SAHA in SIV-infected Chinese rhesus macaques |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Preclinical NHP study | AIDS | Auranofin plus ART restricted the viral reservoir in the monkey AIDS model |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13853P | PREZISTA™ Tablet 75 mg | Film-coated tablet | Not stated in the records |
| SIN13854P | PREZISTA™ Tablet 150 mg | Film-coated tablet | Not stated in the records |
| SIN13855P | PREZISTA™ Tablet 400 mg | Film-coated tablet | Not stated in the records |
| SIN13856P | PREZISTA™ Tablet 600 mg | Film-coated tablet | Not stated in the records |
| SIN14595P | PREZISTA™ Tablet 800 mg | Film-coated tablet | Not stated in the records |

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: The knowledge graph links darunavir to the following conditions as contraindication relations: liver failure, liver disease, cirrhosis of liver, gallbladder disease, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, chronic hepatitis B and C virus infection, hypertriglyceridemia, and hemophilia. These should be checked against the package insert.
- **Drug Interactions**: 100 interactions were found in total. Examples include:
  - **Major**: cisapride
  - **Moderate**: corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic drugs (metformin, pioglitazone, acarbose, alogliptin, saxagliptin, canagliflozin, dapagliflozin, chlorpropamide, acetohexamide, albiglutide), clarithromycin, and aprepitant

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a veterinary disease with no trials or publications, so the evidence level is L5. The related simian model studies do not isolate darunavir's effect and do not directly study feline AIDS. The human equivalent, HIV, is already an original use of this drug.

**To proceed, the following is needed:**
- Data on darunavir's activity against FIV protease (in vitro or in vivo)
- Confirmation that a veterinary indication falls within the scope of this human repurposing programme
- Package insert warnings and contraindications from the HSA, and mechanism of action data
- Mapping of the obsolete hyperlipidemia term to its current ontology term, if that prediction is to be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

