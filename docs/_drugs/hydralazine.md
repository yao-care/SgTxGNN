---
layout: default
title: Hydralazine
parent: Low Evidence (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydralazine: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder / hypertension"
monitor_inn: "Hydralazine"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "ocular tuberculosis", "congenital temporomandibular joint ankylosis", "polydipsia", "obsolete superimposed infection"]
---

# Hydralazine
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

# Hydralazine: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Hydralazine is a direct-acting vasodilator, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model prediction alone. It is also essentially an extension of the original hypertension indication rather than true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (the Singapore licence records contain no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 96.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, hydralazine is a direct-acting arteriolar vasodilator that lowers systemic vascular resistance and blood pressure. It is already used in hypertension and hypertensive emergencies.

Malignant hypertensive renal disease is kidney injury caused by severely elevated blood pressure. Lowering blood pressure through arteriolar vasodilation is therefore mechanistically plausible. However, this is largely a narrower form of the original indication, not a distinct new therapeutic area. The high TxGNN score probably reflects this closeness to hypertension. No trials or literature were found to confirm benefit specifically in the renal setting.

**Other predictions reviewed (all Hold unless noted):**

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Malignant renovascular hypertension | 96.86% | L5 | One paper on the aldosterone/renin ratio (diagnostic methodology), not evidence of efficacy |
| 3 | Pulmonary hypertension owing to lung disease and/or hypoxia | 96.70% | L4 | Mostly tumour-hypoxia and preclinical papers; one Cochrane review in infants with hypoxemic respiratory failure |
| 4 | Pulmonary hypertension, unclear multifactorial mechanism | 96.70% | L5 | No evidence |
| 5 | Braddock syndrome | 95.77% | L5 | No mechanistic link, no evidence |
| 6 | Chronic pulmonary heart disease | 88.29% | L3 | Haemodynamic studies in heart failure and COPD with cor pulmonale; flagged as a research question |

Ranks 7–10 (ocular tuberculosis, congenital temporomandibular joint ankylosis, polydipsia, obsolete superimposed infection) have moderate scores (57–59%) and no supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top-ranked prediction (malignant hypertensive renal disease). The closest supporting studies are for **chronic pulmonary heart disease** (rank 6), shown below for context only:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [825327](https://pubmed.ncbi.nlm.nih.gov/825327/) | 1976 | Cohort | Circulation | Oral hydralazine in 10 patients with refractory heart failure lowered systemic vascular resistance by 42% |
| [7225252](https://pubmed.ncbi.nlm.nih.gov/7225252/) | 1981 | Cohort | Br Heart J | Hydralazine and isosorbide dinitrate, alone and combined, in chronic heart failure at rest and on upright exercise |
| [6780233](https://pubmed.ncbi.nlm.nih.gov/6780233/) | 1981 | Cohort | Circulation | The combination improved haemodynamics but caused postural hypotension and tachycardia |
| [23450605](https://pubmed.ncbi.nlm.nih.gov/23450605/) | 2013 | Cohort / systematic review | Cochrane Database Syst Rev | Hydralazine in infants with persistent hypoxemic respiratory failure and pulmonary hypertension |
| [6692695](https://pubmed.ncbi.nlm.nih.gov/6692695/) | 1984 | Study | Chest | Haemodynamic effects of hydralazine in advanced COPD with cor pulmonale; pulmonary arterial pressure increased after intravenous dosing |
| [3053182](https://pubmed.ncbi.nlm.nih.gov/3053182/) | 1988 | Review | Eur Heart J | Long-term vasodilator trials in pulmonary hypertension due to lung disease gave inconsistent results, with sometimes major side effects |
| [36994251](https://pubmed.ncbi.nlm.nih.gov/36994251/) | 2023 | Case report | Cureus | Hydralazine-induced vasculitis, a rare serious adverse effect |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00211P | APO-Hydralazine Tablet 10 mg | Tablet | Not stated in the data |
| SIN00210P | APO-Hydralazine Tablet 25 mg | Tablet, film coated | Not stated in the data |
| SIN01148P | APO-Hydralazine Tablet 50 mg | Tablet, film coated | Not stated in the data |
| SIN01086P | Hydralazine Tablets 10 mg (Beacons Pharmaceuticals) | Tablet, film coated | Not stated in the data |
| SIN01089P | Hydralazine Tablet 50 mg (Beacons Pharmaceuticals) | Tablet, film coated | Not stated in the data |

All five licences are valid single-ingredient oral products.

---

## Safety Considerations

**Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links hydralazine to the following contraindicated conditions. These need verification against the package insert.
- **Cardiovascular:** coronary artery disease, hypertrophic cardiomyopathy, stroke, cerebrovascular disorder, hypotensive disorder
- **Renal / metabolic:** kidney disease, anuria, diabetes mellitus, diabetic ketoacidosis, gout, hyperuricemia, hypercalcemia, hyperparathyroidism, nephrocalcinosis, potassium deficiency
- **Autoimmune:** systemic lupus erythematosus (including paediatric)
- **Hepatic / GI:** hepatic coma and encephalopathy, pancreatitis, peptic ulcer disease
- **Neuropsychiatric:** epilepsy, anxiety and neurotic disorders, dysthymic disorder
- **Other:** slow acetylator status, neonatal jaundice

Kidney disease and systemic lupus erythematosus are especially relevant here, because the proposed indication is a renal condition.

**Drug Interactions:** The interaction database returned 100 entries. Most of those listed are Moderate severity:
- Corticosteroids: hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, budesonide, triamcinolone
- SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
- Statins: rosuvastatin, simvastatin
- Others: bupropion, morphine, aspirin, metronidazole, dronabinol, sapropterin
- Alosetron is Minor.

**Literature safety signals:** postural hypotension and tachycardia (with isosorbide dinitrate), and hydralazine-induced vasculitis.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (96.86%), but it is prediction-only (L5), with no trials or relevant literature. The indication largely overlaps with hydralazine's existing hypertension use, so it adds little as repurposing. Among the other predictions, chronic pulmonary heart disease has the most indirect support (L3), but the studies address heart failure and COPD haemodynamics rather than the predicted disease, and some show unfavourable effects.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Clinical or observational evidence of hydralazine in malignant hypertensive nephropathy
- A decision on whether this counts as a new indication or as a refinement of the existing hypertension label
- Safety review against the contraindication list, especially kidney disease and lupus
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

