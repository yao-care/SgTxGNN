---
layout: default
title: Furosemide
parent: Low Evidence (L5)
nav_order: 459
evidence_level: L5
indication_count: 10
---

# Furosemide
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

# Furosemide: From Hypertension and Congestive Heart Failure to Malignant Renovascular Hypertension

## One-Sentence Summary

Furosemide is a loop diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but currently there are **0 clinical trials** and only **9 loosely related publications** (none directly testing this use), so this prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, congestive heart failure (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, furosemide is a loop diuretic that lowers blood pressure and body fluid volume, and its efficacy in hypertension and heart failure is established. Mechanistically, it may help in volume-dependent forms of hypertension.

However, the fit is weak for this specific disease. Malignant renovascular hypertension is driven mainly by activation of the renin-angiotensin system, and loop diuretics can further stimulate renin release. The high TxGNN score is likely driven by the drug's original hypertension indication rather than by disease-specific evidence.

The retrieved literature mostly describes furosemide as a diagnostic stimulus (the "furosemide test" for plasma renin activity) in secondary hypertension work-ups, not as a treatment for this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below tests furosemide as a treatment for malignant renovascular hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [659766](https://pubmed.ncbi.nlm.nih.gov/659766/) | 1978 | Review | J Am Geriatr Soc | Serum uric acid and renin activity in 96 patients with various types of hypertension; both were higher in malignant than essential hypertension |
| [397653](https://pubmed.ncbi.nlm.nih.gov/397653/) | 1979 | Review | Trans Am Assoc Genito-Urinary Surg | Evaluation of secondary hypertension; furosemide used to stimulate renin release as a diagnostic test |
| [15080378](https://pubmed.ncbi.nlm.nih.gov/15080378/) | 2004 | Cohort | Hypertens Res | Prospective study of 1,020 patients on the prevalence of secondary hypertension; furosemide plus upright test used in screening |
| [2944248](https://pubmed.ncbi.nlm.nih.gov/2944248/) | 1986 | Cohort | Tohoku J Exp Med | Changes in active and inactive renin after captopril or furosemide in hypertensive patients, including renovascular hypertension |
| [1199811](https://pubmed.ncbi.nlm.nih.gov/1199811/) | 1975 | Review | Acta Med Scand | Intravenous diazoxide in severe hypertension (not furosemide) |
| [30401909](https://pubmed.ncbi.nlm.nih.gov/30401909/) | 2019 | Registry study | Hypertens Res | Predictors of confirmatory tests for primary hyperaldosteronism (SHRIMP study) |
| [844016](https://pubmed.ncbi.nlm.nih.gov/844016/) | 1977 | Case report | Can Med Assoc J | Pheochromocytoma case in which a furosemide screening test for renovascular hypertension was used |
| [6389735](https://pubmed.ncbi.nlm.nih.gov/6389735/) | 1984 | Methods | J Lab Clin Med | New radioimmunoassay for plasma renin |
| [10624394](https://pubmed.ncbi.nlm.nih.gov/10624394/) | 1999 | Overview | Med Pregl | Overview of nuclear medicine diagnostics |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00199P | LASIX TABLET 40 mg | Tablet | Not stated in the compiled data |
| SIN14074P | RASITOL TABLET 40MG | Tablet | Not stated in the compiled data |
| SIN15131P | FUROSEMIDE FRESENIUS KABI SOLUTION FOR INJECTION 20MG/2ML | Injection, solution | Not stated in the compiled data |
| SIN00239P | DIRINE INJECTION 20 mg/2 ml | Injection | Not stated in the compiled data |
| SIN16712P | FUSETIC SOLUTION FOR INJECTION 20MG/2ML | Injection, solution | Not stated in the compiled data |

Ten valid single-ingredient licences are registered in total (tablet and injectable forms); the five above are shown.

## Safety Considerations

- **Contraindications (from knowledge-graph disease associations, not label text)**: orthostatic hypotension and other hypotensive disorders, anuria, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, gout and hyperuricaemia, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disorders, myocardial infarction and coronary thrombosis, systemic lupus erythematosus, hearing and auditory system disorders, pancreatitis, benign prostatic hyperplasia and bladder neck obstruction, hemoglobinopathy, multiple system atrophy, and postural orthostatic tachycardia syndrome.
- **Drug Interactions**: 100 interactions were found in total. The first 20 retrieved include one major interaction (dolasetron) and mostly moderate ones, such as antidiabetic agents (acarbose, alogliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide, albiglutide, dulaglutide), corticosteroids (hydrocortisone, betamethasone, beclomethasone), amphotericin B, proton pump inhibitors (rabeprazole, dexlansoprazole), bisacodyl, and dronabinol. Minor interactions include doxycycline and acetylsalicylic acid.
- Package insert warnings were not available in the compiled data. Please refer to the package insert for full safety information.
- In this specific indication, a theoretical concern is that renin stimulation by furosemide may worsen renin-driven hypertension.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score only (L5): no trials, and no literature showing furosemide treating this condition. The mechanism is also questionable because loop diuretics can increase renin release in a renin-driven disease.

**To proceed, the following is needed:**
- Mechanism of action data and package insert warnings and contraindications
- Evidence that furosemide helps (or at least does not harm) in renin-dependent malignant renovascular hypertension, such as clinical studies or mechanistic data
- A safety assessment covering renin stimulation, volume depletion and electrolyte disturbance

**Other predicted indications in the data:** Among other predicted indications, chronic kidney disease has the strongest evidence. It is rated L2 with a recommendation of Proceed with Guardrails, supported by a completed Phase 4 trial of loop diuretics for blood pressure control in CKD stages 3-4 (n=40). Acute pulmonary heart disease and chronic renal failure syndrome have limited evidence and are classed as research questions. These may be better candidates than the top-ranked prediction, though most of this use is symptomatic volume management and overlaps with the existing indications.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

