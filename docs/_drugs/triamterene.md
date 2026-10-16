---
layout: default
title: Triamterene
parent: Low Evidence (L5)
nav_order: 1021
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Triamterene: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension and congestive heart failure"
---

# Triamterene
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

# Triamterene: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Triamterene is a potassium-sparing diuretic originally used for hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this specific prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the Singapore licence has no indication text recorded) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, triamterene blocks the epithelial sodium channel (ENaC) in the distal nephron. This reduces sodium and water retention while sparing potassium, and it lowers blood pressure and fluid volume.

Malignant hypertensive renal disease is kidney damage caused by severe, uncontrolled hypertension. Blood pressure and volume control could plausibly help, which is the link behind the model's prediction. However, this is largely a restatement of the original hypertension indication rather than a genuinely new use. The prediction is not backed by any trial or publication in the data compiled for this report.

Other predictions with the same type of reasoning (malignant renovascular hypertension) share the same limits. Some other high-scoring predictions, such as pulmonary hypertension, Braddock syndrome, and acute pulmonary heart disease, have no clear mechanistic basis and likely reflect network proximity in the knowledge graph.

Among the other predictions, the better-supported ones are:
- **Potassium deficiency disease** (evidence level L4): this fits triamterene's established role in preventing diuretic-induced hypokalaemia. The literature consists of reviews and case reports, including Liddle's syndrome cases treated with triamterene. It is an established adjunctive use rather than a novel repurposing.
- **Chronic pulmonary heart disease** (evidence level L4): only indirect evidence from general chronic heart failure studies using diuretic combinations.

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The knowledge graph links triamterene to the following conditions, which should be treated as cautions:
  - Kidney and urinary: kidney disease, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, pyoureter
  - Liver and biliary: liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis
  - Metabolic: diabetes mellitus (type 1 and type 2), diabetic ketoacidosis, gout, hyperuricaemia, hypercalcaemia, hyperparathyroidism, phosphorus metabolism disease, acidosis, lactic acidosis
  - Other: systemic lupus erythematosus, folic acid deficiency anaemia, neonatal jaundice
- **Drug Interactions**: 100 interactions were identified. Examples include:
  - **Major**: potassium citrate (risk of hyperkalaemia)
  - **Moderate**: metformin, bupropion, morphine, canagliflozin, dapagliflozin, dronabinol, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), plus some bowel-preparation agents and laxatives (bisacodyl, picosulfuric acid, polyethylene glycol)
  - **Minor**: famotidine, ranitidine, cimetidine, doxycycline, minocycline
- **Prediction-specific concerns**: Hyperkalaemia and renal function risks are particularly relevant in renal impairment and renovascular disease, especially when combined with RAAS-active drugs. Use in pregnancy is generally avoided unless clearly needed.

Please refer to the package insert for full warnings, as label-based warnings were not available in the data compiled for this report.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06552P | APO-TRIAZIDE TABLET (Apotex Inc) | Tablet (oral) | Not recorded |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant hypertensive renal disease has no supporting trials or literature (L5). It is also mostly an extension of triamterene's existing hypertension use. Safety concerns in renal impairment, notably hyperkalaemia, add further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website, as these are currently missing and block safety screening
- Detailed mechanism of action data (for example, from DrugBank)
- Clinical or observational evidence of benefit in hypertensive renal disease, beyond blood pressure control
- A renal and potassium monitoring plan for patients with impaired kidney function
- If a more evidence-based direction is preferred, a focused review of **potassium deficiency disease** (L4), which is the best-supported alternative among the predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

