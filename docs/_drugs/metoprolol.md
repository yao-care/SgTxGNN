---
layout: default
title: Metoprolol
parent: Low Evidence (L5)
nav_order: 668
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metoprolol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension, acute coronary syndrome, myocardial infarction"
monitor_inn: "Metoprolol"
predicted_indications: ["malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "posteroinferior myocardial infarction", "posterolateral myocardial infarction", "septal myocardial infarction", "chronic pulmonary heart disease", "trichotillomania"]
---

# Metoprolol
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

# Metoprolol: From Hypertension and Myocardial Infarction to Malignant Renovascular Hypertension

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker originally used for hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but this top-ranked prediction has **no clinical trials** and **1 publication**, which does not address the indication (it concerns diagnosing pheochromocytoma).
The prediction mostly reflects closeness to the already-approved hypertension indication, so it is not a true repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, acute coronary syndrome, myocardial infarction (the Singapore licences list no approved indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known pharmacology, metoprolol is a beta-1 selective adrenergic blocker. It lowers heart rate and blood pressure and reduces renin release, which is plausible in renovascular hypertension.

Renovascular hypertension is a form of hypertension, which is already an approved use of metoprolol. The high score probably reflects proximity to that approved indication in the knowledge graph rather than a new therapeutic opportunity. Malignant hypertension is also usually managed acutely with titratable intravenous agents, not oral metoprolol.

Other predictions follow a similar pattern:
- **Malignant hypertensive renal disease** is a subtype of hypertension, with no trials or literature.
- **Posteroinferior, posterolateral and septal myocardial infarction** are anatomical subtypes of the approved myocardial infarction indication. Only older or indirect studies were found.
- **Pulmonary hypertension (multifactorial, or due to lung disease/hypoxia)** has no mechanistic support. Beta-blockade is not an established therapy and could be harmful if right ventricular function depends on adrenergic drive.
- **Chronic pulmonary heart disease** is the only prediction with substantive trial and literature activity, and it is covered below.
- **Braddock syndrome and trichotillomania** have no evidence and no mechanistic rationale.

---

## Clinical Trial Evidence

For the top-ranked prediction (malignant renovascular hypertension), currently no related clinical trials are registered.

The only prediction with registered trials is chronic pulmonary heart disease (rank 9). Those trials mostly test metoprolol in COPD or heart failure rather than pulmonary heart disease itself:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Not yet recruiting | 311 | Metoprolol in heart failure with reduced ejection fraction and COPD; compares doses, with all-cause death and rehospitalisation as endpoints |
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Terminated | 532 | BLOCK-COPD: metoprolol vs placebo for preventing COPD exacerbations; informs respiratory safety, but early termination limits conclusions |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | CAMERA: carvedilol vs metoprolol respiratory effects in heart failure; no data |
| [NCT05096884](https://clinicaltrials.gov/study/NCT05096884) | Early Phase 1 | Terminated | 14 | Post-COVID exertional dyspnoea and tachycardia; different condition and too small to inform |

---

## Literature Evidence

For malignant renovascular hypertension, the single linked paper does not test metoprolol in this condition:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | Diagnostic study | Medicine | Chromogranin A as a diagnostic marker for pheochromocytoma in the differential diagnosis of hypertension; no evidence for this indication |

Selected literature for the other predictions (indirect evidence only):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction (REDUCE-AMI); off-target for pulmonary heart disease |
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | BICS: bisoprolol in COPD patients at high risk of exacerbation; notes metoprolol did not reduce exacerbations and increased hospitalised exacerbations |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Randomised crossover | J Am Coll Cardiol | Respiratory and haemodynamic effects of switching between beta-1 selective and nonselective beta-blockers in heart failure with COPD |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in older patients with heart failure, COPD, diabetes and renal failure |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohort | Eur J Heart Fail | Danish cohort on beta-blocker use in heart failure with COPD |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Taiwan database study of carvedilol, bisoprolol and metoprolol in coexistent heart failure and COPD |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Clinical study | Heart Vessels | Metoprolol appeared safe in coronary artery disease patients with COPD |
| [8737105](https://pubmed.ncbi.nlm.nih.gov/8737105/) | 1996 | Randomised, double-blind | Eur Heart J | MEXIS: metoprolol vs xamoterol on left ventricular function in heart failure after myocardial infarction |
| [6401230](https://pubmed.ncbi.nlm.nih.gov/6401230/) | 1983 | Clinical physiology study | Circulation | Acute effects of nitroglycerin, nifedipine and metoprolol on regional left ventricular function in one-vessel coronary disease |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00440P | APO-METOPROLOL TABLET 100 mg (Apotex Inc) | Tablet | Not stated in the data compiled |
| SIN00445P | APO-METOPROLOL TABLET 50 mg (Apotex Inc) | Tablet | Not stated in the data compiled |
| SIN01331P | DENEX TABLET 100 mg (Medochemie Ltd) | Tablet | Not stated in the data compiled |

All three licences are valid single-ingredient oral tablets.

---

## Safety Considerations

- **Contraindications (from knowledge-graph drug–disease edges, not label text)**: anxiety and neurotic disorders, dysthymic disorder, pancreatitis, liver disease (including hepatic coma and encephalopathy), gallbladder disease, systemic lupus erythematosus, potassium deficiency, psoriasis and parapsoriasis, diabetes mellitus and diabetic ketoacidosis, hyperuricaemia and gout, hypotensive disorders, hyperparathyroidism and osteitis fibrosa, hypercalcaemia and nephrocalcinosis, phosphorus metabolism disease, neonatal jaundice, anuria, myasthenia gravis and neuromuscular junction disease, and pheochromocytoma. These should be verified against the package insert.
- **Drug Interactions**: 100 interactions were identified; the 20 reviewed are mostly Moderate. Notable examples include epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, glycopyrronium), bupropion, morphine, cimetidine, SGLT2 inhibitors (canagliflozin, dapagliflozin), chlorpropamide, lorcaserin and calcium salts. Minor interactions include acetylsalicylic acid and magnesium oxide.
- **Respiratory safety**: In BLOCK-COPD, metoprolol did not reduce COPD exacerbations and was associated with more exacerbations requiring hospitalisation. This matters for the lung-disease-related predictions.
- **Package insert data**: Warnings and contraindications from the HSA package insert have not been obtained. Please refer to the package insert for label safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top predictions (malignant renovascular hypertension, malignant hypertensive renal disease and the myocardial infarction subtypes) are subtypes of indications metoprolol already has, so they are not real repurposing opportunities. The linked evidence is absent or off-topic (L5).
- The only prediction with a research signal is chronic pulmonary heart disease (L3, "Research Question"), but the evidence concerns heart failure with COPD, not cor pulmonale. BLOCK-COPD also raised a respiratory safety concern.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data
- Approved indication text for the Singapore licences
- For pulmonary heart disease, direct clinical evidence in cor pulmonale and a review of the BLOCK-COPD safety findings
- For malignant renovascular hypertension, a clinical judgement on whether oral metoprolol has any role beyond its approved hypertension use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

