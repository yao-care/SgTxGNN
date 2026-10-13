---
layout: default
title: Indapamide
parent: Low Evidence (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
---

# Indapamide
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

# Indapamide: From Hypertension to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Indapamide is a thiazide-like diuretic originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **chronic pulmonary heart disease** (cor pulmonale).
There are currently **0 clinical trials** and **no study that tested indapamide in this condition**, so the support is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension and congestive heart failure (the Singapore registration records do not state indication text) |
| Predicted New Indication | Chronic pulmonary heart disease |
| TxGNN Prediction Score | 92.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Indapamide is a thiazide-like diuretic with vasodilating properties. It lowers blood pressure and reduces fluid overload in hypertension and heart failure. Mechanistically, it could ease right-heart volume overload in chronic pulmonary heart disease.

This link is theoretical. The two papers retrieved for this condition are a general review of how hypertension progresses to heart failure and a case report of an overdose. Neither tests indapamide in cor pulmonale. The high TxGNN score most likely reflects network proximity to the drug's existing cardiovascular indications, not disease-specific evidence.

Diuretics in this setting are used only to manage symptomatic fluid retention. They are not disease-modifying. Thiazide-like diuretics can also cause metabolic alkalosis and potassium loss, which may be unhelpful in patients with chronic lung disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC. Heart Failure | General update on how long-standing hypertension leads to heart failure through pressure overload, diastolic dysfunction and left ventricular hypertrophy. It does not address indapamide or cor pulmonale. |
| [19623566](https://pubmed.ncbi.nlm.nih.gov/19623566/) | 2009 | Case report | Pharmacoepidemiology and Drug Safety | An 89-year-old man with COPD overdosed on methyldopa, indapamide and theophylline. He had prolonged hypotension, marked diuresis for 4.5 days and hypokalaemia. This is a toxicity report, not evidence of benefit. |

---

## Singapore Market Information

There are 12 valid registrations, all marketed. Five main ones are listed below. The registration records do not include approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10161P | APO-INDAPAMIDE Tablet 2.5 mg | Film-coated tablet |
| SIN11664P | RINALIX Tablet 2.5 mg | Film-coated tablet |
| SIN16750P | SWILIX SR Tablet 1.5 mg | Film-coated extended-release tablet |
| SIN09074P | NATRILIX SR Tablet 1.5 mg | Film-coated tablet |
| SIN13823P | COVERSYL PLUS Tablet 10 mg/2.5 mg | Film-coated tablet (perindopril combination) |

The remaining registrations are other perindopril-based combinations (NATRIXAM and TRIPLIXAM). All are oral tablets.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver disease, gallbladder disease, potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, hyperparathyroidism, osteitis fibrosa, anuria and gout.
- **Drug Interactions**: 100 interactions were identified, mostly of moderate severity. Examples include:
  - acarbose, metformin, alogliptin and albiglutide (glucose control)
  - hydrocortisone, dexamethasone, betamethasone, triamcinolone and beclomethasone (corticosteroids)
  - amphotericin B
  - omeprazole and rabeprazole
  - bupropion and morphine
  - cholecalciferol and bisacodyl
  - Minor interactions include doxycycline, atropine and hyoscyamine.
- **Signals from the retrieved literature**: Overdose can cause severe hypotension, marked diuresis and hypokalaemia. Indapamide has also been linked to ocular adverse events (choroidal effusion, with angle-closure glaucoma reported as a possible effect). Hypotension from diuresis could be harmful in acute right-heart conditions.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no clinical trials and no literature testing indapamide in chronic pulmonary heart disease. The theoretical benefit is limited to symptomatic volume control, and diuretic-induced electrolyte and acid-base disturbances may be a concern in chronic lung disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator, to complete safety screening
- Detailed mechanism of action data
- Any indapamide-specific clinical data in right-heart failure or cor pulmonale
- A safety plan covering electrolytes, acid-base status and blood pressure in patients with chronic lung disease

**Note:** Among the other predicted indications, **chronic kidney disease** (score 78%) has the strongest supporting literature (L3). This includes perindopril/indapamide data in patients with type 2 diabetes and CKD, and cohort data on thiazide-like diuretics. It may be a better candidate for further research, although indapamide-specific evidence remains limited and efficacy at low eGFR is debated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

