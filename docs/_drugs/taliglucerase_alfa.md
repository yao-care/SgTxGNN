---
layout: default
title: Taliglucerase Alfa
parent: Low Evidence (L5)
nav_order: 953
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Taliglucerase Alfa: predicted new indication Hurler syndrome (evidence level L5). Approved use: Gaucher disease"
monitor_inn: "Taliglucerase alfa"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "lysosomal storage disease with skeletal involvement", "Wolman disease with hypolipoproteinemia and acanthocytosis", "Wolman disease", "proximal myopathy with extrapyramidal signs", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant"]
---

# Taliglucerase Alfa
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

# Taliglucerase alfa: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Taliglucerase alfa is an enzyme replacement therapy originally used to treat Gaucher disease.
The TxGNN model predicts it may be effective for **Hurler syndrome**, but there are currently **0 clinical trials** and **0 publications** supporting this specific direction. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, taliglucerase alfa is a plant-cell-expressed recombinant glucocerebrosidase (beta-glucosidase) that targets macrophage mannose receptors. Its efficacy in Gaucher disease, a lysosomal storage disorder, has been established.

Hurler syndrome (MPS I) is also a lysosomal storage disease, but it is caused by a deficiency of alpha-L-iduronidase, leading to accumulation of glycosaminoglycans. The missing enzyme and the accumulated substrate both differ from those in Gaucher disease, so glucocerebrosidase replacement would not be expected to address the underlying defect.

The high TxGNN score (0.995) most likely reflects shared lysosomal storage disease associations in the knowledge graph rather than a validated therapeutic link. The same is true for the other top-ranked predictions: Scheie syndrome (an attenuated form of MPS I), cholesteryl ester storage disease and Wolman disease (both lysosomal acid lipase deficiencies, for which sebelipase alfa is the specific therapy). Several other predictions, such as benign neoplasm of adrenal gland, proximal myopathy with extrapyramidal signs, and a STAT5B-related growth hormone insensitivity syndrome, have no plausible mechanistic connection and appear to be knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly evaluates taliglucerase alfa in Hurler syndrome. The only publications retrieved relate to a broader category ("lysosomal storage disease with skeletal involvement", rank 6) and concern the approved Gaucher indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41096096](https://pubmed.ncbi.nlm.nih.gov/41096096/) | 2025 | Cohort (real-world, 10-year follow-up) | Journal of Clinical Medicine | Long-term efficacy and safety of taliglucerase alfa in treatment-naïve and previously treated type 1 Gaucher disease patients in Albania |
| [22916340](https://pubmed.ncbi.nlm.nih.gov/22916340/) | 2012 | Review | Drugs of Today | Overview of taliglucerase alfa in Gaucher disease, a disorder caused by glucocerebrosidase (GBA) deficiency and glucocerebroside accumulation |

These papers support the drug in its approved indication only. They do not provide evidence for Hurler syndrome.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16770P | ELELYSO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 200 UNITS/ VIAL | Injection, powder, lyophilized, for solution | Not stated in the registration data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. The enzyme and the substrate differ between Gaucher disease and Hurler syndrome, and no trials or literature support use in this condition. Other lysosomal disorders in the prediction list have their own targeted enzyme therapies.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA website
- Preclinical or mechanistic evidence that glucocerebrosidase replacement can affect glycosaminoglycan accumulation in MPS I
- Clear definition of the target disease entity for any broader categories (e.g., "lysosomal storage disease with skeletal involvement")
- Evaluation of whether other predicted indications have any plausible biological rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

