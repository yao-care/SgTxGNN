---
layout: default
title: Quetiapine
parent: Low Evidence (L5)
nav_order: 836
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Antipsychotic Therapy to Retinal Dystrophy

## One-Sentence Summary

Quetiapine is a marketed antipsychotic. The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, but there is **no clinical trial** and **no study of quetiapine in this condition** to support the prediction. The 14 retrieved publications are general ophthalmology articles that do not mention quetiapine, so this is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the HSA records supplied (quetiapine is an antipsychotic) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Quetiapine is an atypical antipsychotic that acts mainly on D2 and 5-HT2A receptors, and it has an established role in psychiatric disorders.

Nothing in this pharmacology links it to inherited retinal degeneration. The high score (0.996) comes from graph-based similarity in the TxGNN knowledge graph, not from biological or clinical evidence. Many other candidates score almost as high, with TxGNN ranks around 5,900 to 7,600, so the score alone does not separate a real signal from noise. Of the ten predicted indications for quetiapine, only trichotillomania has any drug-specific literature, and that is limited to case reports and narrative reviews.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of these publications studies quetiapine. They are background articles on ocular and orbital conditions retrieved by disease keywords, so they do not support the prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Seminars in Ultrasound, CT, and MR | Overview of orbital infections, most commonly secondary to sinusitis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Systematic approach to evaluating diplopia |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klinische Monatsblätter für Augenheilkunde | Congenital ptosis and its association with refractive errors |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens size, shape and position |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Documenta Ophthalmologica | Wagner-Stickler syndrome complex: vitreoretinal degeneration with extraocular features |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging of pediatric ocular pathologies |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Therapeutic Advances in Ophthalmology | Eye involvement in inherited metabolic disorders |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case report | American Journal of Ophthalmology | Two patients with unilateral cryptophthalmia |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case report | Journal of Neuro-Ophthalmology | Congenital trochlear-oculomotor synkinesis in a 6-year-old boy |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case report | Optometry and Vision Science | Synergistic divergence in congenital fibrosis of the extraocular muscles |

## Singapore Market Information

Quetiapine has 20 registrations in Singapore. The approved indication text is not included in the records supplied. The first five are listed below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16689P | SAQUIN SR Prolonged-Release Tablets 50mg | Tablet, extended release |
| SIN14823P | ALVOQUEL Film Coated Tablets 25mg | Tablet, film coated |
| SIN13838P | Quetiapine Sandoz 25 mg Tablets | Tablet, film coated |
| SIN13769P | Ketipinor Tablet 200 mg | Tablet, film coated |
| SIN14342P | APO-QUETIAPINE Tablet 25mg | Tablet, film coated |

All registered forms are oral.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. There are no clinical trials, no quetiapine-specific literature, and no plausible mechanistic link between a D2/5-HT2A antagonist and inherited retinal degeneration. The evidence level is L5.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications, to allow safety screening
- Mechanism of action data from DrugBank
- A testable biological hypothesis linking quetiapine to retinal pathways, with preclinical support
- Drug-specific literature on quetiapine in retinal dystrophy. If none exists, the candidate should be deprioritised in favour of better-supported predictions for this drug, such as trichotillomania.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

