---
layout: default
title: Lisinopril
parent: Low Evidence (L5)
nav_order: 601
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From ACE Inhibitor Therapy to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an ACE inhibitor marketed in Singapore as oral tablets. The TxGNN model predicts it may be useful for **posterolateral myocardial infarction**, but **0 clinical trials** and **0 publications** currently support this specific prediction. The evidence rests on model output and general pharmacology only, and the broader myocardial infarction (MI) class may already be an approved use, so this may not be true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the dataset. Based on general pharmacology, lisinopril is an ACE inhibitor. After an MI, blocking angiotensin II production reduces ventricular remodeling, so the biological link is plausible.

The registration records supplied for Singapore do not include approved indication text, so the relationship to the original indication cannot be assessed from the data. The MI class is also likely already covered by existing labelling or practice. This posterolateral subtype is therefore probably not a genuinely new use. Its score is identical to that of the posteroinferior MI entry (99.90%), which suggests both were inherited from a shared parent node in the knowledge graph rather than from evidence specific to this subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Lisinopril has 13 registrations in Singapore, all oral tablets. The 5 main authorizations are listed below. Approved indication text was not provided in the records.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN12005P | NOPERTEN 5 TABLET 5 mg | Tablet | PT Dexa Medica |
| SIN07870P | LISORIL 10 TABLET 10 mg | Tablet | IPCA Laboratories Ltd |
| SIN11994P | DAPRIL 5 TABLET 5 mg | Tablet | Medochemie Ltd (Central Factory / Factory AZ) |
| SIN07868P | LISORIL 5 TABLET 5 mg | Tablet | IPCA Laboratories Ltd |
| SIN11996P | DAPRIL 20 TABLET 20 mg | Tablet | Medochemie Ltd (Factory AZ) / Medochemie (Far East) Ltd |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but there are no trials or publications for this subtype, so the evidence level is L5. The MI class likely overlaps with an existing indication, so the added value of this prediction is unclear.

**To proceed, the following is needed:**
- The HSA package insert, to confirm the registered indications and obtain warnings and contraindications
- Mechanism of action data from DrugBank
- A check of whether MI is already an approved or guideline-supported use of lisinopril, which would make this a label extension rather than repurposing
- A targeted search for lisinopril or ACE inhibitor studies in MI

**Other predictions worth noting:** Of the ten predicted indications, *chronic pulmonary heart disease* has the strongest evidence (L4). Two older reports appear to study lisinopril directly in this population (PMID 14524095 and 17047621), but their designs and outcomes are unverified. It could be reviewed first if a follow-up candidate is needed. The other predictions have no supporting evidence, and the pulmonary hypertension literature retrieved appears to be a generic hypoxia keyword match rather than lisinopril-related evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

