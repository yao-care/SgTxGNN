---
layout: default
title: Eplerenone
parent: Low Evidence (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Eplerenone
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

# Eplerenone: From Heart Failure and Hypertension to Pulmonary Hypertension (Unclear Multifactorial Mechanism)

## One-Sentence Summary

Eplerenone is a mineralocorticoid receptor (MR) blocker; the Singapore registration records do not state its approved indications, and it is generally used for heart failure and hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension with unclear multifactorial mechanism** with a very high score, but this is a model prediction only, with **0 clinical trials** and **0 publications** for this exact indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA registration records (heart failure and hypertension per general drug knowledge) |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on the analysis, eplerenone blocks the mineralocorticoid receptor, which mediates aldosterone-driven fibrosis, inflammation and vascular remodeling. Blocking it could plausibly reduce pulmonary vascular remodeling and fibrosis, which is the basis of this prediction.

The predicted label is nonspecific ("unclear multifactorial mechanism"), so it is hard to link to a defined patient group. The high score is a knowledge-graph prediction, and no trial or paper was retrieved for this exact indication. The 20 papers retrieved for the related label "pulmonary hypertension owing to lung disease and/or hypoxia" cover generic hypoxia biology (brain aging, cancer, immunity). None evaluates eplerenone or pulmonary hypertension, so they are treated as keyword noise and not as support.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication.

Some indirect evidence exists under a neighbouring prediction, **chronic pulmonary heart disease** (score 95.62%, rank 6):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00232180](https://clinicaltrials.gov/study/NCT00232180) | Phase 3 | Completed | 2743 | Eplerenone vs placebo in NYHA Class II systolic heart failure; left-sided disease, so indirect |
| [NCT01115855](https://clinicaltrials.gov/study/NCT01115855) | Phase 3 | Completed | 221 | Japanese companion trial of eplerenone vs placebo in chronic heart failure; indirect |

## Literature Evidence

Currently no related literature available for the top-ranked indication.

Preclinical papers under **chronic pulmonary heart disease** show a mixed signal:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29499691](https://pubmed.ncbi.nlm.nih.gov/29499691/) | 2018 | Preclinical (animal) | BMC Pulm Med | Eplerenone attenuated pulmonary vascular remodeling, but not right ventricular remodeling, in pulmonary arterial hypertension |
| [24067600](https://pubmed.ncbi.nlm.nih.gov/24067600/) | 2013 | Preclinical (animal) | Int J Cardiol | Eplerenone plus losartan was not effective in experimental right ventricular failure |

## Singapore Market Information

The registration records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN13048P | INSPRA TABLETS 25mg (Viatris Pharmaceuticals LLC) | Tablet, coated |
| SIN13049P | INSPRA TABLETS 50mg (Viatris Pharmaceuticals LLC) | Tablet, coated |
| SIN16941P | EPLERENONE MEVON FILM-COATED TABLETS 25 MG (Pharmathen S.A.) | Tablet, film coated |
| SIN16940P | EPLERENONE MEVON FILM-COATED TABLETS 50 MG (Pharmathen S.A.) | Tablet, film coated |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is L5: a model score with no trials or literature for this exact indication, and a nonspecific disease label. The mixed preclinical signal in the related indication, chronic pulmonary heart disease, is best treated as a research question rather than a basis for a go decision.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indications), which is a blocking gap for safety screening
- Detailed mechanism of action data (MOA) from DrugBank
- A defined pulmonary hypertension subtype and target population, then a targeted search for eplerenone-specific trials and literature
- Human evidence for right-heart or pulmonary vascular endpoints, since current Phase 3 data is limited to left-sided heart failure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

