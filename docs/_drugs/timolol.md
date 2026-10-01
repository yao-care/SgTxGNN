---
layout: default
title: Timolol
parent: Low Evidence (L5)
nav_order: 982
evidence_level: L5
indication_count: 10
---

# Timolol
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

# Timolol: From Glaucoma (Ophthalmic Use) to Primary Hereditary Glaucoma

## One-Sentence Summary

Timolol is a non-selective beta-blocker marketed in Singapore mainly as eye drops. The Singapore records do not list an approved indication, but its established ophthalmic use is lowering eye pressure in glaucoma. The TxGNN model predicts it may be effective for **primary hereditary glaucoma** with a high score, but this prediction has **no supporting evidence**: the only clinical trial retrieved (**1 trial**) concerns nosebleeds in a different disease, and **0 publications** were found.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (inferred from the ophthalmic products; no indication text in the Singapore records) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. Based on the evidence pack's analysis, timolol is a non-selective beta-blocker that lowers intraocular pressure (IOP) by reducing aqueous humor production. That is plausible for glaucoma in general.

Primary hereditary (congenital) glaucoma is a glaucoma subtype, so the prediction is not a large conceptual jump. However, it is usually managed surgically, and a topical IOP-lowering mechanism has not been shown to be relevant. The high TxGNN score is a model output only and is not backed by clinical data.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02484716](https://clinicaltrials.gov/study/NCT02484716) | Phase 2 | Completed | 58 | Randomized, placebo-controlled test of timolol nasal spray for nosebleeds in Hereditary Hemorrhagic Telangiectasia (HHT). Unrelated to glaucoma; it matches only the word "hereditary" and is likely a keyword-matching artifact. |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11054P | TIMABAK EYEDROPS 0.5% | Solution | Not specified |
| SIN08619P | TIMOPTOL-XE OPHTHALMIC SOLUTION 0.5% | Solution | Not specified |
| SIN04135P | TIMOPTOL OPHTHALMIC SOLUTION 0.5% | Solution | Not specified |
| SIN09709P | TIMOLOL-POS EYE DROPS 0.5% | Solution | Not specified |
| SIN13744P | TIMO-COMOD 0.5% EYE DROPS | Solution | Not specified |

Showing 5 of 20 registrations.

## Safety Considerations

Please refer to the package insert for safety information.

For general context, the evidence pack's analyses of other timolol indications flag caution in asthma, severe COPD, bradycardia and heart block. They also advise monitoring for systemic absorption of the eye drops.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The only retrieved trial is an unrelated HHT nosebleed study, no literature was found, and the evidence level is L5. Congenital glaucoma is mainly treated surgically, so topical timolol has no demonstrated role.

For context, other predictions for this drug are better supported:
- **Angle-closure glaucoma** reached L2 (Proceed with Guardrails), as an adjunct to definitive treatment only.
- **Open-angle glaucoma** reached L1, but this is confirmation of established use rather than new repurposing.

**To proceed, the following is needed:**
- Clinical or observational data on timolol in primary hereditary (congenital) glaucoma
- Approved indication text and safety information from the HSA package inserts
- Mechanism-of-action data from DrugBank
- A confirmed original indication for the record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

