---
layout: default
title: Labetalol
parent: Low Evidence (L5)
nav_order: 571
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Labetalol: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "Labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "chronic pulmonary heart disease", "primary hereditary glaucoma", "open-angle glaucoma", "atrial flutter (disease)", "ocular tuberculosis"]
---

# Labetalol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha-1 and non-selective beta-blocker, originally used to treat hypertension and hypertensive disorders.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are **no registered clinical trials** and only **1 publication** (an unrelated case report) behind this prediction, so the prediction currently rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, labetalol blocks both alpha-1 and beta receptors. This lowers vascular resistance and heart rate, and beta-blockade also reduces renin release. It is already used for hypertension and hypertensive emergencies.

Malignant renovascular hypertension is a severe form of high blood pressure driven by renal artery disease and activation of the renin system. Mechanistically, lowering blood pressure and renin release could help. However, this is a close extension of the existing hypertension indication rather than a true new use.

The very high score likely reflects the model's closeness to the approved hypertension indication. The one linked publication is a 1981 case report on hallucinogenic drug-induced vasculitis with malignant hypertension. Labetalol was used there only for initial blood pressure control, so it does not demonstrate efficacy in renovascular hypertension.

Other predictions in the same ranking are weaker:
- **Malignant hypertensive renal disease** (score 99.08%): a plausible extension of the hypertension indication, but with no trials or literature.
- **Pulmonary hypertension** (two entries, about 99.08%): mechanistically doubtful. Beta-blockade is not a pulmonary hypertension strategy and may be harmful.
- **Open-angle glaucoma** (score 63.5%): the only other prediction with a plausible direct signal. A 1981 rabbit and small human study reported an eye-pressure-lowering effect of labetalol (PMID 6914126). This is a reasonable research question (evidence level L4) but is not ready for clinical advancement.

## Clinical Trial Evidence

Currently no clinical trials are registered for malignant renovascular hypertension.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case report | Med J Aust | Malignant hypertension in a young man after hallucinogen use, with renal vessel arteritis. Steroids resolved the arteritis. Minoxidil and labetalol were used for initial blood pressure control. Not specific evidence for labetalol in renovascular hypertension. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02281P | TRANDATE INJECTION 100 mg/20 ml | Injection | Not stated in the available record |
| SIN05162P | TRANTALOL TABLET 100 mg | Tablet | Not stated in the available record |

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these are model-derived associations, not package insert text):
- Liver and biliary: liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease, pancreatitis
- Cardiovascular and respiratory: atrioventricular block, hypotensive disorder, pulmonary emphysema, bronchial disease
- Metabolic and renal: diabetes mellitus, diabetic ketoacidosis, kidney disease, anuria, gout, hyperuricemia, potassium deficiency, hypercalcemia, hyperparathyroidism
- Other: systemic lupus erythematosus, anxiety and neurotic disorders, intraoperative floppy iris syndrome

**Drug Interactions:** The interaction screen returned 100 records; the first 20 are shown.
- **Major:** epinephrine, dolasetron
- **Moderate (examples):** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), anticholinergics (atropine, hyoscyamine, dicyclomine, methscopolamine), morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, calcium salts
- **Minor:** acetylsalicylic acid, magnesium oxide

Please refer to the package insert for full safety information. Label warnings and contraindications have not yet been obtained.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (evidence level L5). There are no registered trials, and the single publication does not test labetalol for this condition. The indication is also largely an extension of labetalol's existing hypertension use, so it adds little as a repurposing opportunity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- Approved indication text for the two Singapore licences
- Targeted literature search for labetalol in renovascular and malignant hypertension
- If a new-use direction is wanted, consider open-angle glaucoma as a separate research question, since it has the only direct signal (early, small-scale data)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

