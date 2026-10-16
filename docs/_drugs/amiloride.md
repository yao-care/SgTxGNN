---
layout: default
title: Amiloride
parent: Low Evidence (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amiloride: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
---

# Amiloride
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

# Amiloride: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic, originally used for hypertensive disorders, hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no publications** specific to this indication were found, so the prediction currently rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure (the Singapore licence record contains no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, amiloride blocks the epithelial sodium channel (ENaC) in the distal nephron, which reduces sodium reabsorption, spares potassium and lowers blood pressure.

Hypertensive renal disease is driven by sustained high blood pressure damaging the kidney. Because amiloride is already used for hypertension, it is plausible that the same blood-pressure-lowering and sodium-handling effects could be relevant. The high TxGNN score (99.82%) is most likely driven by this overlap with the existing hypertension indication rather than by any direct evidence in malignant hypertensive renal disease.

**Other predicted indications (for context):**

| Predicted Indication | TxGNN Score | Evidence Level | Assessment |
|------|------|------|------|
| Malignant renovascular hypertension | 99.82% | L4 | Mechanistically coherent (acts downstream of aldosterone), but the only paper found is a general review on mineralocorticoid hypertension |
| Pulmonary hypertension (multifactorial, or owing to lung disease/hypoxia) | 99.81% | L5 / L4 | Preclinical papers link ASIC1 and ENaC to hypoxic pulmonary hypertension; no human data, and most retrieved papers were off-topic |
| Braddock syndrome | 99.75% | L5 | Prediction only |
| Chronic pulmonary heart disease | 99.68% | L4 | Indirect evidence from heart failure studies |
| Acute pulmonary heart disease | 98.40% | L5 | Prediction only; diuretic action is not a plausible acute therapy |
| Primary hereditary glaucoma / open-angle glaucoma | 92.06% / 87.41% | L5 | Theoretical ocular ion-transport rationale only |
| Chronic renal failure syndrome | 85.53% | L4 | Indirect; significant hyperkalaemia caveat; a narrow lithium-related niche may merit separate review |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For the second-ranked prediction (malignant renovascular hypertension), the only publication retrieved was a general review:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | J Hypertens Suppl | Overview of how to investigate mineralocorticoid-driven hypertension; diagnostic in nature, not a treatment study |

Selected publications for other predicted indications that are most relevant to amiloride:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/) | 1987 | RCT (double-blind crossover, 14 patients) | Lancet | Captopril alone vs frusemide plus amiloride in mild heart failure; 4 patients on captopril alone deteriorated |
| [1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/) | 1991 | Clinical study (double-blind crossover, 11 patients) | Cardiovasc Drugs Ther | Amiloride improved haemodynamics in chronic heart failure patients on digoxin and diuretics |
| [25398716](https://pubmed.ncbi.nlm.nih.gov/25398716/) | 2015 | Review (preclinical) | Exp Physiol | Smooth muscle ASIC1 implicated in hypoxic pulmonary hypertension |
| [3987787](https://pubmed.ncbi.nlm.nih.gov/3987787/) | 1985 | Clinical study | Eur J Clin Pharmacol | Limits on amiloride use in early renal failure; potassium excretion reduced |
| [3428342](https://pubmed.ncbi.nlm.nih.gov/3428342/) | 1987 | Pharmacokinetic study | Eur J Clin Pharmacol | Renal impairment reduces amiloride clearance and prolongs its half-life |
| [8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/) | 1996 | Case report | Am J Med Sci | Severe hyperkalaemia in an elderly patient with heart failure on trimethoprim-sulfamethoxazole (safety signal) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06538P | AA-AMILZIDE TABLET (Apotex Inc) | Tablet | Not stated in the licence record |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not package insert text):** kidney disease, anuria, diabetic nephropathy, liver disease, hepatic coma/encephalopathy, potassium deficiency disease, diabetes mellitus, diabetic ketoacidosis, acidosis disorders (including acquired lactic acidosis), gout, hyperparathyroidism, systemic lupus erythematosus, pancreatitis, gallbladder disease, pyoureter and neonatal jaundice.
- **Drug Interactions:** 100 interactions were identified. Those listed include moderate-level interactions with metformin, corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin), exenatide, bupropion, dronabinol, and laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose). Minor interactions include doxycycline, amoxicillin and cimetidine.
- **Clinical caution from the literature:** Hyperkalaemia is the key concern, especially when kidney function is reduced (see PMIDs 3987787, 3428342, 8615380).

Please refer to the package insert for the official warnings, as these were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant hypertensive renal disease is supported only by the model score, with no trials or publications. Amiloride is already marketed in Singapore, but safety in kidney disease (hyperkalaemia risk, plus kidney disease listed among its contraindications) is a particular concern for a kidney-focused indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), which is a blocking gap for safety screening
- Detailed mechanism of action data (for example from DrugBank)
- Targeted literature search for amiloride in malignant or hypertensive nephropathy, and for the better-supported alternatives (pulmonary hypertension via ASIC1/ENaC, lithium-related nephrogenic diabetes insipidus)
- A hyperkalaemia and renal function monitoring plan for any study in patients with reduced kidney function
- Review of the approved indication text for licence SIN06538P, which is blank in the current record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

