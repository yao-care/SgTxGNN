---
layout: default
title: Sotalol
parent: Low Evidence (L5)
nav_order: 932
evidence_level: L5
indication_count: 10
---

# Sotalol
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

# Sotalol: From Atrial Fibrillation to Sick Sinus Syndrome 2, Autosomal Dominant

## One-Sentence Summary

Sotalol is a class III antiarrhythmic drug with beta-blocking activity, originally used to treat atrial fibrillation.
The TxGNN model's top-ranked prediction is **sick sinus syndrome 2, autosomal dominant**, but **no clinical trials and no publications** support this prediction. Sotalol is also contraindicated in sick sinus syndrome, so the prediction is unlikely to reflect real therapeutic benefit.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the licence entries list no approved indication text; this is taken from the knowledge-graph indication data) |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, sotalol is a class III antiarrhythmic and beta-blocker. It blocks the hERG (IKr) potassium channel, prolongs repolarisation, and slows sinus rate and atrioventricular conduction. Its efficacy in atrial fibrillation rhythm control is established.

The predicted link to sick sinus syndrome is probably an artefact of the model. Both conditions involve cardiac rhythm, which probably explains the high score. Pharmacologically, however, slowing the sinus rate and AV conduction is likely to worsen sinus node dysfunction (bradycardia, sinus arrest). Sick sinus syndrome is a known contraindication for sotalol unless a pacemaker is in place. The prediction therefore most likely reflects a safety signal rather than a therapeutic opportunity.

Other predictions in the top 10 are also weak. These include Wildervanck syndrome, sarcoglycanopathy, manic bipolar disorder, ABri amyloidosis and nephrogenic syndrome of inappropriate antidiuresis. None has supporting trials or any plausible mechanistic link. The one candidate with some indirect evidence is **stroke disorder** (rank 4, evidence level L4). That link runs only through atrial fibrillation and is not independent of the original indication.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (sick sinus syndrome 2, autosomal dominant).

For reference, the only trial found among the top 10 predictions is listed below. It relates to the rank 4 prediction, stroke disorder, and is only indirectly relevant.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00007605](https://clinicaltrials.gov/study/NCT00007605) | Phase 3 | Completed | 706 | CSP #399: amiodarone and sotalol for maintaining sinus rhythm in atrial fibrillation. It targets AF rhythm control, not stroke prevention. |

## Literature Evidence

No publications are available for the top-ranked prediction.

For reference, the most relevant publications found for the rank 4 prediction (stroke disorder) are listed below. They concern atrial fibrillation management and do not show a direct stroke-prevention effect of sotalol.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Cohort | Circ Arrhythm Electrophysiol | Retrospective comparison of dronedarone and sotalol for maintaining sinus rhythm in antiarrhythmic-drug-naive veterans with AF |
| [1281807](https://pubmed.ncbi.nlm.nih.gov/1281807/) | 1992 | Clinical study | Int J Cardiol | Sotalol suppressed ventricular arrhythmias in 50-60% of treatment attempts in complex ventricular ectopy |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Review of acute-onset AF; AF raises the risk of stroke and heart failure |
| [9358515](https://pubmed.ncbi.nlm.nih.gov/9358515/) | 1997 | Review | Pacing Clin Electrophysiol | Complications of AF; warfarin reduces stroke risk |
| [38011245](https://pubmed.ncbi.nlm.nih.gov/38011245/) | 2023 | Review | Circulation | Contemporary AF management in hypertrophic cardiomyopathy |
| [37777295](https://pubmed.ncbi.nlm.nih.gov/37777295/) | 2023 | Guideline review | Am J Cardiol | Guideline recommendations on antiarrhythmic drug selection in AF |
| [29954667](https://pubmed.ncbi.nlm.nih.gov/29954667/) | 2019 | Clinical study | Int J Cardiol | Efficacy and adverse effects of sotalol in adults with congenital heart disease |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13311P | SotaHexal 80mg Tablet | Film-coated tablet | Not stated in the data |
| SIN09139P | APO-SOTALOL TABLET 160 mg | Tablet | Not stated in the data |

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease edges, not package insert text):** long QT syndrome (including familial), torsades de pointes, sick sinus syndrome (including familial), atrioventricular block, asthma and other bronchial disease, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, hypotension, impaired renal function, and anaphylaxis.
- **Drug Interactions:** 100 interactions were identified. Major-level ones include:
  - epinephrine
  - clarithromycin
  - picosulfuric acid
  - polyethylene glycol (3350 with electrolytes)

  Many others are moderate, including famotidine, cimetidine, loperamide, bupropion, morphine, atropine, canagliflozin and dapagliflozin.
- **QT-prolongation risk with antipsychotics:** The literature shows beta-blockade can augment the torsadogenic action of risperidone. This is relevant to the mania prediction.

Please refer to the package insert for other safety information, including key warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical or literature support (L5, model prediction only). Sotalol's pharmacology is likely to worsen sick sinus syndrome, and the condition is a recognised contraindication. None of the other top-10 predictions has direct supporting evidence. Stroke is the only one with indirect evidence, and it depends on the existing atrial fibrillation indication.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indications), as the licence entries list no indication text
- Mechanism of action data from DrugBank
- A review of whether the prediction reflects a model artefact from the contraindication relationship
- For stroke, direct outcome evidence showing a benefit beyond AF rhythm control and anticoagulation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

