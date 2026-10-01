---
layout: default
title: Perindopril
parent: Low Evidence (L5)
nav_order: 771
evidence_level: L5
indication_count: 10
---

# Perindopril
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

# Perindopril: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Perindopril is an ACE inhibitor marketed in Singapore, mainly in combination products with amlodipine or indapamide, so its original use is presumably hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
**No clinical trials** and **no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (inferred from drug class and product names; the registration records list no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on class knowledge, perindopril is an ACE inhibitor. It blocks the renin-angiotensin-aldosterone system (RAAS), which lowers blood pressure.

Renovascular hypertension is driven by RAAS activation, because reduced kidney blood flow triggers renin release. RAAS blockade is therefore biologically plausible here. The high score (0.998) is a model output, not clinical evidence.

There is also a safety concern. ACE inhibitors can precipitate acute renal failure in patients with bilateral renal artery stenosis or a solitary functioning kidney. These are the patients this indication targets, so a dedicated safety review is needed before any further step.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Registration records show 20 licenses. The main ones are listed below. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15400P | COSYREL Film-Coated Tablet 10 mg/5 mg | Tablet, film coated |
| SIN13826P | COVERAM Tablet 5 mg/5 mg | Tablet |
| SIN13633P | COVERSYL PLUS Tablet 5 mg/1.25 mg | Tablet, film coated |
| SIN15399P | COSYREL Film-Coated Tablet 5 mg/10 mg | Tablet, film coated |
| SIN15726P | AMLESSA Tablets 8 mg/10 mg | Tablet |

All listed forms are oral.

## Safety Considerations

Please refer to the package insert for safety information.

One class-level caution applies to this prediction: ACE inhibitors can precipitate acute renal failure in bilateral renal artery stenosis or a solitary functioning kidney.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and no relevant literature, and the evidence level is L5. The target population also carries a known renal safety risk with ACE inhibitors, and the package insert safety data has not been obtained.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking for safety screening)
- Mechanism of action data confirmed from DrugBank
- A dedicated safety review of ACE inhibitor use in renal artery stenosis and solitary kidney
- A targeted search for trials and literature on ACE inhibitors in renovascular hypertension
- Approved-indication text for the Singapore licenses, to confirm the original indication

Results are for research reference only and do not constitute medical advice. Repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

