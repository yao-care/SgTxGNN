---
layout: default
title: Acetazolamide
parent: Low Evidence (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Acetazolamide
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

# Acetazolamide: From Carbonic Anhydrase Inhibitor Therapy to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Acetazolamide is an oral carbonic anhydrase inhibitor, marketed in Singapore as 250 mg tablets, and the registration records provided do not state an approved indication.
The TxGNN model's top prediction is **exercise-induced malignant hyperthermia**, and no clinical trials or publications support it.
Among the top 10 predictions, the only one with registered trials is **cardiomyopathy** (rank 7), with **3 trials in heart failure populations** and **11 publications** that are mostly case reports and reviews.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records |
| Predicted New Indication | Exercise-induced malignant hyperthermia (rank 1) |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

For comparison, the best-supported candidate is cardiomyopathy: score 99.83%, evidence level L4, and a "Research Question" recommendation. It is the only prediction in the top 10 that reached screening stage S1.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on general pharmacology, acetazolamide inhibits carbonic anhydrase and reduces proximal tubular sodium and bicarbonate reabsorption. This produces natriuresis and a diuretic effect. It has also been used in some channelopathies.

**Rank 1 (exercise-induced malignant hyperthermia):** No mechanistic link can be established from the data provided. The very high score is not backed by any trial or publication. Nothing supports carbonic anhydrase inhibition as relevant to malignant hyperthermia, so this looks like a model-only signal.

**Best-supported candidate (cardiomyopathy):** The link is plausible but indirect. Acetazolamide can improve the diuretic response in volume-overloaded heart failure, which is a downstream syndrome of cardiomyopathy. The registered trials enroll acute or decompensated heart failure patients, not cardiomyopathy-specific populations. The other signals are weak:
- Rabbit ischaemia-reperfusion data are preclinical.
- Case reports on periodic paralysis with cardiomyopathy do not transfer to a general cardiomyopathy population.

Several other top-10 predictions look like knowledge-graph artifacts or carry safety concerns:
- Hypertrophic cardiomyopathy due to intensive athletic training is a physiological adaptation, not a disease needing treatment.
- Cirrhotic cardiomyopathy runs into the known caution of hyperammonaemia and encephalopathy in cirrhosis.
- Intestinal obstruction and myopathic intestinal pseudo-obstruction raise a harm signal, because acetazolamide-induced adynamic ileus has been reported.

## Clinical Trial Evidence

Rank 1 (exercise-induced malignant hyperthermia): currently no related clinical trials registered.

Trials for the best-supported candidate, cardiomyopathy (rank 7):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06166654](https://clinicaltrials.gov/study/NCT06166654) | Phase 4 | Recruiting | 939 | Double-blind RCT in acute heart failure with volume overload. It compares a loop diuretic plus metolazone or acetazolamide against a loop diuretic alone. No results yet. |
| [NCT05802849](https://clinicaltrials.gov/study/NCT05802849) | Phase 4 | Recruiting | 400 | Oral acetazolamide for decompensated heart failure. It tests the drug directly, but the population is indirect to cardiomyopathy. No results yet. |
| [NCT06092437](https://clinicaltrials.gov/study/NCT06092437) | N/A | Recruiting | 466 | TAILOR-AHF tests a urine-sodium-guided diuretic algorithm in acute heart failure. It tests a strategy, not acetazolamide specifically. |

## Literature Evidence

Rank 1: currently no related literature available.

Publications for cardiomyopathy (rank 7). No randomized trial is among them.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | Update on heart failure management and the 2023 ESC guideline changes. It is general context, not acetazolamide-specific. |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Review of new cardiovascular drugs in 2022, including mavacamten for obstructive hypertrophic cardiomyopathy. It is not acetazolamide-specific. |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case report | J Cardiol Cases | Acetazolamide was used to treat hypochloremia in an advanced heart failure patient who also had hypertrophic cardiomyopathy. Urinary electrolyte monitoring was emphasized. |
| [22426904](https://pubmed.ncbi.nlm.nih.gov/22426904/) | 2012 | Preclinical (animal) | Saudi Med J | Effects of acetazolamide on ischaemia-reperfused isolated rabbit hearts. It is preclinical and not transferable to patients. |
| [29123889](https://pubmed.ncbi.nlm.nih.gov/29123889/) | 2017 | Case report (adverse event) | Acute Med Surg | Non-cardiogenic pulmonary oedema after intravenous acetazolamide in a patient with dilated cardiomyopathy. |
| [23571262](https://pubmed.ncbi.nlm.nih.gov/23571262/) | 2014 | Case report | Indian J Ophthalmol | Topical dorzolamide plus oral acetazolamide for cystoid macular oedema in Danon disease. |
| [7324871](https://pubmed.ncbi.nlm.nih.gov/7324871/) | 1981 | Case series | Acta Neurol Scand | Heart muscle disease in familial hypokalaemic periodic paralysis. The patient developed exercise angina while on acetazolamide 750–1000 mg daily. |
| [742352](https://pubmed.ncbi.nlm.nih.gov/742352/) | 1978 | Case report | Acta Neurol Scand | Cardiological findings in nine family members with hypokalaemic periodic paralysis. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16860P | GP-Acetazolamide Tablet 250 mg | Tablet | GPAX Pharmaceuticals Private Ltd |
| SIN01140P | AA Pharma Acetazolamide Tablet 250 mg | Tablet | Apotex Inc |

Both registrations are oral tablets. No approved indication text is recorded in the data provided.

## Safety Considerations

Package insert warnings and contraindications for the Singapore products were not available, so please refer to the package insert for safety information. No drug interactions were found in the queried data.

Safety signals from the retrieved literature and model rationale:
- **Adynamic (paralytic) ileus:** reported with acetazolamide, which is relevant to the gut-motility predictions.
- **Non-cardiogenic pulmonary oedema:** reported after intravenous acetazolamide in a patient with dilated cardiomyopathy.
- **Cirrhosis:** reduced renal ammonia excretion may cause hyperammonaemia and encephalopathy.
- **Obstructive hypertrophic cardiomyopathy:** diuretics need caution because of preload sensitivity.
- **Electrolytes:** hypochloraemia and hyponatraemia need monitoring during diuretic therapy, as the heart failure case report shows.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, exercise-induced malignant hyperthermia, has no trials, no literature and no plausible mechanism. Most other top-10 predictions are also model-only, and some raise safety concerns. Cardiomyopathy is the only candidate worth a research question, but its trials are still recruiting, without results, in heart failure rather than cardiomyopathy populations.

**To proceed, the following is needed:**
- The Singapore package insert (HSA) for warnings, contraindications and the approved indication.
- Mechanism of action data from DrugBank.
- Results from NCT05802849 and NCT06166654, to judge whether the diuretic benefit in heart failure is real.
- A cardiomyopathy-specific evidence review, if the research question is pursued. It should separate obstructive hypertrophic cardiomyopathy from other types, given the preload-sensitivity concern.
- Deprioritizing intestinal obstruction, myopathic intestinal pseudo-obstruction and cirrhotic cardiomyopathy unless the safety signals are resolved.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

