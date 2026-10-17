---
layout: default
title: Lisinopril
parent: Medium Evidence (L3-L4)
nav_order: 607
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Lisinopril: predicted new indication Posterolateral myocardial infarction (evidence level L4). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Lisinopril"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome"]
---

# Lisinopril
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

# Lisinopril: From Hypertension and Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but this is an anatomical subtype of an indication it already covers, with **0 clinical trials** and **0 publications** specific to this subtype.
The evidence is indirect, based on extrapolation from the parent indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge-graph indication list; no approved indication text is available from the Singapore licences) |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, lisinopril is an angiotensin-converting enzyme (ACE) inhibitor. Its efficacy in hypertension and myocardial infarction is established, and mechanistically it may be applicable to subtypes of myocardial infarction.

Posterolateral myocardial infarction is an anatomical subtype of myocardial infarction, which is already a listed indication for lisinopril. The expected ACE inhibitor benefits after infarction (reduced adverse ventricular remodelling and lower mortality) plausibly apply across subtypes. The prediction is therefore best viewed as an ontology-level duplicate of the existing indication, not a distinct repurposing signal.

The other predicted indications are also mostly weak. Several are further MI subtypes (posteroinferior, septal). The pulmonary hypertension predictions rest on generic renin-angiotensin system rationale. Malignant renovascular hypertension raises a safety concern, because ACE inhibitors carry a risk of acute kidney injury in renal artery stenosis. The one signal that stands apart is **chronic pulmonary heart disease**, supported by two small lisinopril-specific clinical publications (rated L3, "Research Question"), which may merit separate follow-up.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

For reference, the closest related signals among other predicted indications are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17047621](https://pubmed.ncbi.nlm.nih.gov/17047621/) | 2006 | Clinical study (design unconfirmed) | Kardiologiia | Lisinopril 10 mg/day attenuated pulmonary hypertension and improved right ventricular function in heart failure with ischaemic heart disease and COPD (chronic pulmonary heart disease) |
| [14524095](https://pubmed.ncbi.nlm.nih.gov/14524095/) | 2003 | Clinical study (design unconfirmed) | Problemy tuberkuleza i boleznei legkikh | Lisinopril treatment in chronic cor pulmonale (no abstract available) |
| [39018146](https://pubmed.ncbi.nlm.nih.gov/39018146/) | 2024 | Case report | JPMA | ACE inhibitor plus coenzyme Q10 as adjunctive treatment in ventricular septal rupture after late-onset MI (septal MI; not lisinopril-specific) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12005P | NOPERTEN 5 | Tablet | Not stated |
| SIN07870P | LISORIL 10 | Tablet | Not stated |
| SIN11994P | DAPRIL 5 | Tablet | Not stated |
| SIN07868P | LISORIL 5 | Tablet | Not stated |
| SIN11996P | DAPRIL 20 | Tablet | Not stated |

All 13 registrations are valid single-ingredient oral tablets; none has been cancelled.

---

## Safety Considerations

**Contraindications / conditions of concern (from the drug-disease knowledge graph, not label text):**
- Angioedema (including hereditary, acquired, and ACE-inhibitor-induced)
- Kidney disease and liver disease; hepatic encephalopathy
- Pancreatitis and gallbladder disease
- Aortic stenosis and other aortic valve disease
- Hypotensive disorders
- Diabetes mellitus and diabetic ketoacidosis
- Potassium deficiency disease and hyperparathyroidism
- Neutropenia and agranulocytosis
- Systemic lupus erythematosus and connective tissue disease

**Drug Interactions** (100 interactions recorded; main ones listed):
- **Major:** potassium citrate, potassium bicarbonate (risk of hyperkalaemia)
- **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), antidiabetic agents (metformin, alogliptin, saxagliptin, canagliflozin, dapagliflozin, empagliflozin, chlorpropamide), acetylsalicylic acid, morphine, bupropion, dronabinol

A published case report also describes severe hypotension and bradycardia when lisinopril was combined with tizanidine.

Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but posterolateral myocardial infarction is a subtype of an indication lisinopril already covers. There are no trials or literature specific to it, so this is not a new repurposing opportunity. The evidence level is L4, on indirect class extrapolation only.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website, which are required before safety screening can proceed
- Mechanism of action data (for example from DrugBank)
- Confirmation of the approved indication text for Singapore licences, to check whether MI is already covered
- Separate evaluation of **chronic pulmonary heart disease**, the only prediction with lisinopril-specific clinical publications, including confirmation of study design and quality
- Safety review for the renal and hypotension-related predictions (malignant renovascular hypertension, malignant hypertensive renal disease)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

