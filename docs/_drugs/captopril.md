---
layout: default
title: Captopril
parent: Low Evidence (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Captopril: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, hypertensive disorder, diabetic nephropathy"
monitor_inn: "Captopril"
predicted_indications: ["malignant hypertensive renal disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "chronic pulmonary heart disease", "intracerebral hemorrhage", "chronic renal failure syndrome"]
---

# Captopril
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

# Captopril: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is an ACE inhibitor originally used for hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but there are currently **0 registered clinical trials** and only **1 publication** (a diagnostic case report), so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, captopril is an ACE inhibitor. It lowers angiotensin II-mediated vasoconstriction and aldosterone release. Its efficacy in hypertension and diabetic nephropathy is established.

Malignant hypertension with renal involvement is a severe, often renin-driven form of high blood pressure. Mechanistically, blocking the renin-angiotensin system is therefore plausible for this condition.

However, the only publication retrieved is a case report of captopril renography (a diagnostic test) in a patient whose hypertension was caused by a renal cell carcinoma. It shows no therapeutic benefit. The high score is a model prediction, not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | Positive captopril renography (a diagnostic test indicating renin-dependent hypertension) was caused by a large renal cell carcinoma, not renal artery stenosis. Hypertension resolved after nephrectomy. This is a diagnostic use, not treatment evidence. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08473P | DEXACAP TABLET 12.5 mg | Tablet | Not recorded |
| SIN10401P | CATOPLIN-25 TABLETS 25 mg | Tablet | Not recorded |
| SIN06666P | APO-CAPTO TABLET 25 mg | Tablet | Not recorded |
| SIN06665P | APO-CAPTO TABLET 50 mg | Tablet | Not recorded |
| SIN06667P | APO-CAPTO TABLET 12.5 mg | Tablet | Not recorded |

A sixth licence (SIN08474P, DEXACAP TABLET 25 mg) is also valid. All six are single-ingredient oral tablets.

## Safety Considerations

- **Contraindications / disease associations (from the knowledge graph, not label text)**: kidney disease, liver disease, pancreatitis, gallbladder disease, angioedema (including hereditary and ACE-inhibitor-related forms), systemic lupus erythematosus, diabetes and diabetic ketoacidosis, potassium deficiency, neutropenia and agranulocytosis, aortic stenosis, hypotension, hyperparathyroidism, hepatic encephalopathy, and connective tissue and bone disease.
- **Drug Interactions**: 100 interactions were found. Most of the listed ones are Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), antidiabetic drugs (metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, exenatide, chlorpropamide, acetohexamide), morphine, bupropion, acetylsalicylic acid, and dronabinol. Antacids (aluminium hydroxide, calcium carbonate) are Minor.
- **Clinical concern for this indication**: ACE inhibitors can reduce kidney function in patients with bilateral renal artery stenosis or a solitary kidney, which matters in severe renovascular and renal hypertension.

Package insert warnings were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a high model score and a plausible mechanism. No trials are registered, and the only publication is a diagnostic case report. Evidence for therapeutic benefit is currently absent.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Detailed mechanism of action data
- Clinical evidence of captopril treatment in malignant hypertension with renal involvement
- A renal safety plan: monitoring creatinine and potassium, and excluding bilateral renal artery stenosis

## Other Predicted Indications Worth Noting

Of the other predicted indications, two are rated more promising than the top-ranked one:

| Predicted Indication | Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|
| Chronic renal failure syndrome | 81.33% | L2 | Proceed with Guardrails | One randomized trial of captopril to mitigate chronic renal failure after hematopoietic stem cell transplantation ([PMID 18029109](https://pubmed.ncbi.nlm.nih.gov/18029109/)). The trial phase and results should be verified, and broader support comes from class-effect data for other ACE inhibitors. |
| Chronic pulmonary heart disease | 97.08% | L3 | Research Question | Several small, older haemodynamic studies in COPD with pulmonary hypertension (1986-1989) gave mixed results, for example [PMID 3530649](https://pubmed.ncbi.nlm.nih.gov/3530649/) and [PMID 3050941](https://pubmed.ncbi.nlm.nih.gov/3050941/), the latter showing no pulmonary benefit. |
| Malignant renovascular hypertension | 99.28% | L4 | Research Question | Mechanistically relevant, but literature is mostly reviews and diagnostic case reports. |

The remaining predictions (pulmonary hypertension subtypes, Braddock syndrome, rare syndromes, brain small vessel disease, intracerebral hemorrhage) have only model prediction or preclinical evidence and are on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

