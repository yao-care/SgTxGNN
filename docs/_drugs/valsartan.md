---
layout: default
title: Valsartan
parent: Medium Evidence (L3-L4)
nav_order: 1054
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Valsartan: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Valsartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "obsolete susceptibility to ischemic stroke"]
---

# Valsartan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials** and only **1 indirect publication** (a preclinical study of a different drug) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, valsartan belongs to the angiotensin II type 1 (AT1) receptor blocker class. Its efficacy in hypertension is established, and it is also known to lower blood pressure and protect the kidney.

Malignant hypertension and its kidney injury are strongly driven by the renin-angiotensin system. Blocking the AT1 receptor is therefore mechanistically on target. The same reasoning applies to the second-ranked prediction, malignant renovascular hypertension, where preclinical work (PMID 11560862) suggests AT1 blockade can prevent lethal malignant hypertension in an animal model.

However, the only paper retrieved for the top prediction (PMID 24368192) studies avosentan, an endothelin antagonist, in rats. It does not test valsartan. The prediction is therefore biologically plausible but not directly supported by valsartan-specific data.

Other predictions in the list are weaker. Chronic pulmonary heart disease (rank 6) has some indirect clinical data, mostly on the sacubitril/valsartan combination in heart failure. Pulmonary hypertension, Braddock syndrome, Prinzmetal angina, and the remaining predictions rest on prediction alone or on off-topic literature.

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

For reference, the only trial linked to any of the top-ranked predictions is for chronic pulmonary heart disease (rank 6), and it is only loosely relevant:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Exercise rehabilitation and vascular function in hypertension; does not directly test valsartan |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical | Pharmacological Research | Avosentan (not valsartan) protected against hypertensive nephropathy in transgenic rats at doses that did not cause fluid retention |

Related indirect evidence for the second-ranked prediction, malignant renovascular hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Preclinical | Circulation | AT1 receptor blockade prevented lethal malignant hypertension in an animal model, linked to reduced kidney inflammation |

## Singapore Market Information

All 20 registrations are valid single-ingredient licences in oral film-coated tablet form. The approved indication text was not available for these licences. Five main authorizations:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11555P | DIOVAN TABLET 80 mg | Film-coated tablet | Not available |
| SIN11554P | DIOVAN TABLET 160 mg | Film-coated tablet | Not available |
| SIN14139P | Valsartan Sandoz film coated tablet 80mg | Film-coated tablet | Not available |
| SIN14140P | Valsartan Sandoz film coated tablet 160mg | Film-coated tablet | Not available |
| SIN12011P | CO-DIOVAN 160/25 TABLET | Film-coated tablet | Not available |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: Conditions linked to valsartan as cautions include angioedema (including hereditary and RAAS-blocker-induced forms), liver disease and liver failure, hepatic encephalopathy, impaired renal function, anuria, renal artery obstruction, hypotensive disorder, diabetes mellitus and diabetic ketoacidosis, potassium deficiency disease, gout, hypercalcemia, hyperparathyroidism, neutropenia and agranulocytosis, systemic lupus erythematosus, pancreatitis, gallbladder disease, and neonatal jaundice. Of particular relevance to the predicted use, renal artery obstruction and impaired renal function are listed, so kidney safety needs careful evaluation.
- **Drug Interactions**: 100 interactions were recorded. The main ones include:
  - **Major**: potassium chloride and potassium bicarbonate (risk of raised potassium).
  - **Moderate**: many insulin products, exenatide, hydrocortisone, eluxadoline, and polyethylene glycol 3350 with electrolytes.

Please also refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high (99.97%), and blocking the renin-angiotensin system is biologically sensible for malignant hypertensive kidney injury. However, no clinical trials exist, and the only retrieved paper tests a different drug in animals. Evidence is limited to L4 (mechanistic and preclinical). Valsartan's kidney-related cautions also require a safety evaluation.

**To proceed, the following is needed:**
- Valsartan-specific preclinical or clinical data in malignant hypertensive nephropathy
- Detailed mechanism of action data
- Package insert warnings and contraindications from the HSA, to enable safety screening
- Approved indication text for the Singapore licences
- A renal safety assessment (renal artery stenosis, impaired renal function, hyperkalaemia risk)
- Consideration of chronic pulmonary heart disease as a secondary research question, since it has the most indirect clinical data (largely from sacubitril/valsartan)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

