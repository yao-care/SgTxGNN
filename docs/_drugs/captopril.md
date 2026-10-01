---
layout: default
title: Captopril
parent: Low Evidence (L5)
nav_order: 203
evidence_level: L5
indication_count: 10
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

Captopril is an oral ACE inhibitor marketed in Singapore as tablets, and its indication is generally hypertension. The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**. Support is very thin: **0 clinical trials** and **1 publication** (a diagnostic case report, not a treatment study).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA licence records (captopril is generally used for hypertension) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Captopril acts on the renin-angiotensin-aldosterone system (RAAS), and blocking this system is an established way to lower blood pressure. Its efficacy in hypertension is well established, and mechanistically it may be applicable to renin-driven malignant hypertension with kidney involvement.

The link is plausible, but it is not proven by the evidence retrieved. The only paper found describes captopril renography, a diagnostic test, in a patient with renal cell carcinoma. It does not show that captopril treats this condition. The high TxGNN score likely reflects knowledge-graph proximity between hypertension-related diseases rather than direct clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case report | Clinical Nuclear Medicine | A positive captopril renography (a diagnostic test) turned out to be caused by a large renal cell carcinoma rather than renal artery stenosis. Renin-dependent hypertension resolved after nephrectomy. This is diagnostic, not evidence of therapeutic benefit. |

## Singapore Market Information

Six licences are registered in total; the five below are the main ones. All are oral tablets. The approved indication text is not listed in the records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN08473P | DEXACAP TABLET 12.5 mg | Tablet | PT Dexa Medica |
| SIN10401P | CATOPLIN-25 TABLETS 25 mg | Tablet | Beacons Pharmaceuticals Pte. Ltd. |
| SIN06666P | APO-CAPTO TABLET 25 mg | Tablet | Apotex Inc |
| SIN06665P | APO-CAPTO TABLET 50 mg | Tablet | Apotex Inc |
| SIN06667P | APO-CAPTO TABLET 12.5 mg | Tablet | Apotex Inc |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has model support only (L5), with no registered trials and no therapeutic studies. The single publication is a diagnostic case report. The HSA package insert safety data are also missing, which blocks safety screening.

Other captopril predictions in this Evidence Pack have more support and may be better candidates to pursue first. These are malignant renovascular hypertension (L4), chronic pulmonary heart disease (L3) and chronic renal failure (L3). Even these rest mainly on small hemodynamic, animal or non-randomized studies.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, downloaded and parsed
- Mechanism of action data from DrugBank
- Approved indication text for the Singapore licences
- Any treatment study (clinical or observational) of captopril in malignant hypertensive renal disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

