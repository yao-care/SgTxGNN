---
layout: default
title: Amlodipine
parent: Low Evidence (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a dihydropyridine calcium channel blocker, a widely used blood pressure-lowering drug. The TxGNN model predicts it may help with **brain stem infarction** (score 99.94%), but **no clinical trials and no publications** are linked to this specific prediction. This is a model-only signal (Evidence Level L5), and the stronger clues in this pack point to other stroke-related indications.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (from the pack's rationale text; the HSA licence records have no indication text) |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on the pack's rationale text, amlodipine is a dihydropyridine calcium channel blocker. It lowers blood pressure by relaxing blood vessels and reducing systemic vascular resistance.

Lowering blood pressure is a plausible route to preventing a secondary stroke. However, brain stem infarction is defined by where the infarct sits, not by a distinct treatment target. Nothing in the data shows amlodipine acting differently for this location. The link therefore rests on general pharmacology and the model score alone.

Similarity between the original and predicted indications has not been assessed (marked pending in the pack).

## Clinical Trial Evidence

Currently no related clinical trials registered for brain stem infarction.

The pack does contain trials for related stroke indications. The most relevant is for **intracerebral hemorrhage** (rank 10 candidate, evidence level L2, the strongest in this pack):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: triple-combination blood pressure pill vs placebo to prevent recurrent stroke after intracerebral hemorrhage. Results are not in the pack, and the regimen is understood to include amlodipine (unverified). |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1000 | High-dose ARB alone vs ARB plus calcium channel blocker in elderly Japanese hypertensive patients. Amlodipine as the partner drug is unverified. |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11414 | Treating high-normal blood pressure in type 2 diabetes. Amlodipine is not specified. |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study. Too small to interpret. |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Phase NA | Terminated | 4 | TRIDENT MRI sub-study. Too small to interpret. |

## Literature Evidence

Currently no related literature available for brain stem infarction.

For the intracerebral hemorrhage candidate, the pack lists mostly off-target papers. The two most relevant are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design/rationale | Int J Stroke | TRIDENT rationale: a single-pill combination of blood pressure drugs as secondary prevention after intracerebral hemorrhage. |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with a thalamic hemorrhagic stroke (a safety signal). |

## Singapore Market Information

Showing 5 of 20 registrations. The HSA records provided have no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14529P | AMCAD 5 TABLET 5 mg | Tablet | Not stated in record |
| SIN15498P | AMLOPIN TABLET 5MG | Tablet | Not stated in record |
| SIN13538P | ACTAPIN TABLET 10MG | Tablet | Not stated in record |
| SIN14548P | Tenox tablets 5 mg | Tablet | Not stated in record |
| SIN13537P | ACTAPIN TABLET 5MG | Tablet | Not stated in record |

All registered forms are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were retrieved.

Two signals appear in the pack's evidence review:
- A case report of probable amlodipine-induced angioedema (PMID 19299323).
- For the hypoxia-related pulmonary hypertension prediction (rank 2), the rationale notes that calcium channel blockers may blunt hypoxic pulmonary vasoconstriction and worsen ventilation-perfusion matching in lung disease. This is a potential harm signal.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The brain stem infarction prediction has a very high model score but no linked trials or literature (L5), and the mechanism is only generic blood pressure lowering. The best-supported direction in this pack is intracerebral hemorrhage (L2, driven by TRIDENT), and it is still a combination-regimen signal with no results in the record.

**Other candidates in the pack (for triage):**

| Predicted Indication | Score | Evidence Level | Recommendation |
|------|------|------|------|
| Intracerebral hemorrhage | 99.79% | L2 | Research Question |
| Cerebral artery occlusion | 99.89% | L4 (animal data only) | Research Question |
| Malignant renovascular hypertension | 99.90% | L4 | Research Question |
| MRI defined brain infarct | 99.86% | L4 | Research Question |
| Pulmonary hypertension due to lung disease/hypoxia | 99.91% | L5 (literature is off-target keyword matches) | Hold, possible harm signal |
| Other 4 candidates (including the multifactorial pulmonary hypertension and malignant hypertensive renal disease predictions) | 99.85–99.91% | L5 | Hold |

**To proceed, the following is needed:**
- Retrieve the TRIDENT (NCT02699645) primary results, confirm amlodipine is in the regimen, and check whether the effect can be attributed to it.
- Package insert warnings and contraindications from HSA (currently missing).
- Mechanism of action data from DrugBank.
- Expert review of the pulmonary hypertension links, given the potential harm signal.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

