---
layout: default
title: Methyldopa
parent: Medium Evidence (L3-L4)
nav_order: 662
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Methyldopa: predicted new indication Malignant renovascular hypertension (evidence level L4). Approved use: Hypertension / hypertensive disorder"
---

# Methyldopa
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Methyldopa: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Methyldopa is a long-established antihypertensive, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but there are **no registered clinical trials** and only **1 indirect publication** supporting this prediction, so the evidence is model prediction with very weak support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension / hypertensive disorder (the Singapore licence has no approved indication text recorded) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 96.63% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Methyldopa is a well-known antihypertensive that is generally understood to act centrally through its metabolite alpha-methylnorepinephrine, an alpha-2 adrenergic agonist that reduces sympathetic outflow. Its efficacy in ordinary hypertension is established, and mechanistically it may be applicable to severe secondary hypertension.

Malignant renovascular hypertension is a severe form of high blood pressure linked to kidney blood-flow problems. The high TxGNN score most likely reflects its closeness to the approved hypertension indication in the knowledge graph rather than direct proof of benefit.

The only publication retrieved (PMID 22147655) discusses factors that affect the aldosterone/renin ratio, which is a diagnostic screening issue. It does not show that methyldopa treats this condition. The evidence is therefore indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review | Hormone and Metabolic Research | Discusses factors affecting the aldosterone/renin ratio in primary aldosteronism screening, including how malignant or renovascular hypertension and antihypertensive drugs can cause false negatives. It does not show therapeutic benefit. |

### Other Predicted Indications (for context)

| Rank | Predicted Indication | Score | Evidence Level | Note |
|---|---|---|---|---|
| 2 | Malignant hypertensive renal disease | 96.63% | L5 | No trials or literature; prediction only |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 96.30% | L4 | Two 1970s rat studies suggest reduced hypoxia-induced pulmonary vascular changes; preclinical only |
| 6 | Chronic pulmonary heart disease | 85.03% | L3 | A small 1988 study (25 patients, methyldopa 750 mg/day vs placebo) in hypoxic cor pulmonale gave inconclusive overall haemodynamic results |

The remaining predictions (pulmonary hypertension with unclear mechanism, Braddock syndrome, temporomandibular joint ankylosis, polydipsia, atrial flutter, cholangiocarcinoma susceptibility) have no supporting evidence. Of the candidates, chronic pulmonary heart disease has the most direct human data, but it is small, dated and of uncertain design.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03618P | AA PHARMA METHYLDOPA TABLET 250 mg (Apotex Inc) | Film-coated tablet (oral) | Not recorded |

## Safety Considerations

**Contraindications suggested by the knowledge graph** (these come from graph associations, not package insert text):
- Liver conditions: liver failure, liver disease, cirrhosis, hepatic coma, hepatic encephalopathy
- Kidney and heart conditions: kidney disease, anuria, congestive heart failure
- Autoimmune and blood conditions: systemic lupus erythematosus, autoimmune hemolytic anemia, fetal erythroblastosis
- Porphyria (inherited porphyria and related porphyrin metabolism disorders)
- Metabolic and endocrine conditions: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperparathyroidism, hypercalcemia, gout, hyperuricemia
- Others: pancreatitis, gallbladder disease, neonatal jaundice, and psychiatric conditions (anxiety disorder, neurotic disorder, dysthymic disorder)

**Drug Interactions**: The interaction query returned 100 records. Those shown are mostly of Moderate severity:
- Corticosteroids: hydrocortisone, prednisolone, prednisone, dexamethasone, betamethasone, triamcinolone, budesonide
- Sympathomimetics: epinephrine, ephedrine
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
- Others: iron, naltrexone, dronabinol, nabilone
- Minor: sulfonylureas (chlorpropamide, glimepiride, tolazamide)

**Additional note**: A case report (PMID 19623566) describes prolonged, severe hypotension after a methyldopa overdose in an elderly patient. This warrants caution in patients with cardiopulmonary compromise.

The package insert warnings are not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication of malignant renovascular hypertension is supported only by a high model score and one indirect diagnostic review, with no clinical trials. Methyldopa is already marketed for hypertension, but nothing here demonstrates benefit in this specific severe condition.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational evidence specific to malignant renovascular hypertension, and a comparison against current standard treatments
- A safety review of the liver, kidney and heart contraindications, since these are common in patients with severe secondary hypertension
- If a different direction is preferred, a deeper look at chronic pulmonary heart disease, which has the most direct (though old and small) human data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

