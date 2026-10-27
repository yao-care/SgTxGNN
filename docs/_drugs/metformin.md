---
layout: default
title: Metformin
parent: Low Evidence (L5)
nav_order: 655
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metformin: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy", "homozygous familial hypercholesterolemia"]
---

# Metformin
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

## Metformin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome
{: .text-alpha }

## One-Sentence Summary

Metformin is an oral antidiabetic drug originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (taken from the knowledge-graph indication records; the Singapore licence records contain no indication text) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, metformin is an established oral antidiabetic agent whose efficacy in type 2 diabetes is well documented. The data compiled for this report, however, do not support a mechanistic link to focal stiff limb syndrome.

Focal stiff limb syndrome belongs to the stiff-person spectrum, which is an autoimmune/neurological group of disorders. The related classic stiff person syndrome involves anti-GAD antibodies and impaired GABAergic signalling. No established metformin pathway to these conditions is evident. The association may partly reflect the co-occurrence of autoimmune diabetes with these disorders in the model's data, rather than a therapeutic rationale.

The same limitation applies to the other top-ranked predictions. The second-ranked prediction, classic stiff person syndrome, has an almost identical score (99.45%). It has no trials or literature either. Opsismodysplasia, thiamine-responsive dysfunction syndrome and several localized lipodystrophies also rank highly, but none has supporting clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for focal stiff limb syndrome.

Among the lower-ranked predictions, the only evidence was indirect:

- **Pancreatic agenesis (rank 8):** The retrieved publications are mostly general reviews of diabetes, pancreatic cancer or type 3c diabetes, plus a metformin hepatotoxicity case report. None addresses pancreatic agenesis. Insulin replacement is the standard therapy, and metformin's insulin-sensitizing action would not be expected to compensate for absent beta cells.
- **Homozygous familial hypercholesterolemia (rank 10):** One in vitro study ([PMID 3377878](https://pubmed.ncbi.nlm.nih.gov/3377878/), 1988, *Atherosclerosis*) reported that metformin decreased cholesterol metabolism in cultured human fibroblasts. This is preclinical and not clinical evidence. The other publication ([PMID 37160786](https://pubmed.ncbi.nlm.nih.gov/37160786/), 2023, *Acta Diabetologica*) concerns GLP-1 analogue therapy in rare genetic diseases and does not establish metformin efficacy.

## Singapore Market Information

Metformin has 20 valid single-ingredient registrations in Singapore. Approved indication text is not recorded in the licence data. The five main authorizations are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN04249P | Glucophage Tablet 500 mg | Film-coated tablet | Merck Sante SAS / Merck S.L. / PT Merck Tbk |
| SIN06988P | Glucophage Tablet 850 mg | Film-coated tablet | Merck Sante SAS / Merck S.L. / PT Merck Tbk |
| SIN13249P | Glucophage XR 500 mg Extended Release Tablet | Extended-release tablet | Merck Sante sas (Semoy) / Merck Healthcare KGaA |
| SIN07530P | Glycomet Tablet 500 mg | Tablet | USV Private Limited |
| SIN16257P | Adimet XR Tablet 500 mg | Film-coated extended-release tablet | Centaur Pharmaceuticals Private Limited |

All products are oral tablets (immediate-release, film-coated or extended-release).

## Safety Considerations

**Contraindication signals from the knowledge graph (not label text):**
The knowledge graph links metformin to contraindication with several conditions, including:
- Liver failure and liver disease
- Kidney disease
- Congestive heart failure
- Pancreatitis and gallbladder disease
- Pituitary hormone deficiencies (including hypopituitarism and Sheehan syndrome)
- Adrenocortical insufficiency
- Pyoureter and thymus gland disease

These have not been confirmed against the package insert and should be verified.

**Drug Interactions:**
The interaction search returned 100 records. The following are the major-level interactions among those listed:
- **Acetazolamide** (Major)
- **Ethanol** (Major)

Moderate interactions include dolutegravir, abemaciclib, ranitidine, nifedipine, ibuprofen, ketorolac, hydrochlorothiazide, ethinylestradiol, hydrocortisone, and sympathomimetics such as epinephrine, salbutamol, formoterol, pseudoephedrine and phenylephrine.

Please refer to the package insert for key warnings and formal contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no clinical trials or literature for focal stiff limb syndrome, and no plausible mechanistic link is supported. The condition is autoimmune and neurological, so benefit from an insulin-sensitizing antidiabetic drug is unlikely without new evidence.

**To proceed, the following is needed:**
- Mechanism of action data for metformin, to allow a proper mechanistic analysis
- Package insert warnings and contraindications from the Singapore regulator (HSA), needed for safety screening
- Preclinical or clinical evidence linking metformin to stiff-person-spectrum disorders
- Review of the knowledge-graph contraindication signals against the label, particularly renal, hepatic and cardiac conditions
- Consideration of other high-scoring candidates only if direct supporting evidence emerges (none was found for the top ten predictions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

