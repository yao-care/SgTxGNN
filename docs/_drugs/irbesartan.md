---
layout: default
title: Irbesartan
parent: Low Evidence (L5)
nav_order: 547
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Irbesartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, hypertensive disorder, diabetic nephropathy"
monitor_inn: "Irbesartan"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "chronic pulmonary heart disease", "obsolete susceptibility to ischemic stroke"]
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker, originally used to treat hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials** and **no publications** currently support this specific prediction (evidence level L5, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (the registration records contain no approved indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, irbesartan belongs to the angiotensin II type 1 (AT1) receptor blocker class. Its efficacy in hypertension and diabetic nephropathy is established, and mechanistically, blocking the renin-angiotensin system may be applicable to hypertensive kidney injury.

The predicted indication is closely related to the approved ones: both involve high blood pressure damaging the kidney. The high TxGNN score (0.993) most likely reflects this closeness in the knowledge graph rather than independent evidence. In addition, malignant hypertension is an acute emergency usually managed with parenteral agents, so an oral ARB is unlikely to be a primary therapy.

Other predictions from the same model run were also reviewed. They do not have stronger support:
- **Malignant renovascular hypertension** (score 99.31%): mechanistically coherent, but there are no trials or literature. Bilateral renal artery stenosis is a known safety concern for ARBs.
- **Pulmonary hypertension owing to lung disease and/or hypoxia** (score 99.25%): the most developed evidence (L4), but all of it is preclinical, from cell and animal models of hypoxic stress.
- **Chronic pulmonary heart disease** (score 96.53%): literature is mostly about heart failure with preserved ejection fraction and is only indirectly relevant.
- Other predictions (pulmonary hypertension of unclear mechanism, Braddock syndrome, Prinzmetal angina, two ultra-rare genetic disorders, and an obsolete stroke-susceptibility term) have no trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

For reference, the closest indirect evidence comes from the rank 4 prediction (pulmonary hypertension owing to lung disease and/or hypoxia). It is almost entirely preclinical:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30356256](https://pubmed.ncbi.nlm.nih.gov/30356256/) | 2018 | Preclinical | PLoS One | Irbesartan protected cardiomyocytes under hypoxic stress |
| [34626328](https://pubmed.ncbi.nlm.nih.gov/34626328/) | 2022 | Preclinical | Sleep Breath | Irbesartan reduced sleep-apnea-induced cardiac apoptosis |
| [34147903](https://pubmed.ncbi.nlm.nih.gov/34147903/) | 2021 | Preclinical | Biomed Pharmacother | Irbesartan ameliorated chronic mountain sickness in rats via cholesterol metabolism |
| [34286497](https://pubmed.ncbi.nlm.nih.gov/34286497/) | 2021 | Preclinical | Eur Rev Med Pharmacol Sci | Irbesartan improved oxidative stress in high-altitude pulmonary hypertension in rats via intestinal flora |
| [17142340](https://pubmed.ncbi.nlm.nih.gov/17142340/) | 2007 | Preclinical | Am J Physiol Heart Circ Physiol | Irbesartan inhibited hypoxia-stimulated coronary angiogenesis in neonatal rats |
| [35288835](https://pubmed.ncbi.nlm.nih.gov/35288835/) | 2022 | Review | Inflammopharmacology | Pleiotropic effects of AT1 receptor antagonists in cardiac ischaemia-induced hypoxia |
| [18949104](https://pubmed.ncbi.nlm.nih.gov/18949104/) | 2008 | RCT (pilot) | Can Respir J | Exercise training and irbesartan on blood pressure and heart rate variability in COPD patients (blood pressure endpoint, indirect) |

## Singapore Market Information

All 20 registrations are valid single-ingredient products (oral tablets). Approved indication text is not recorded for any of them. Five main authorizations are listed:

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10861P | APROVEL Film-Coated Tablet 150 mg | Film-coated tablet | Not recorded |
| SIN10862P | APROVEL Film-Coated Tablet 300 mg | Film-coated tablet | Not recorded |
| SIN11646P | COAPROVEL Film-Coated Tablet 150/12.5 mg | Film-coated tablet | Not recorded |
| SIN14137P | Tensiber Film Coated Tablet 150mg | Film-coated tablet | Not recorded |
| SIN16193P | IRBETAS 150 Film Coated Tablet 150 mg | Film-coated tablet | Not recorded |

## Safety Considerations

- **Disease-level cautions from the knowledge graph** (not package insert text): irbesartan is linked to contraindication or caution signals for angioedema (including RAAS-blocker-induced and hereditary forms), pancreatitis, systemic lupus erythematosus, renal artery obstruction, anuria, hypotensive disorder, diabetes mellitus and diabetic ketoacidosis, gout and hyperuricaemia, hyperparathyroidism, hypercalcaemia, hepatic encephalopathy, and muscle disorders including rhabdomyolysis. Renal artery obstruction is particularly relevant to the renovascular predictions.
- **Drug Interactions**: 100 interactions were found. Two are classed as **Major**: potassium citrate and potassium bicarbonate (risk of hyperkalaemia). Many are Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, acetylsalicylic acid, morphine, bupropion, aprepitant and dronabinol.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials or literature support irbesartan in malignant hypertensive renal disease, and the condition is an acute emergency normally treated with parenteral agents. The strongest related signal (hypoxia-associated pulmonary hypertension) is preclinical only and is better treated as a research question.

**To proceed, the following is needed:**
- Literature and trial searches specific to ARBs in malignant hypertension and hypertensive nephrosclerosis
- Mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA, and the approved indication text for the Singapore registrations
- A clinical rationale for an oral ARB in an acute, emergency setting
- Safety assessment for renal artery stenosis, hyperkalaemia and acute kidney injury risk
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

