---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 575
evidence_level: L5
indication_count: 10
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Latanoprost: From Glaucoma / Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

> Latanoprost is a prostaglandin F2α (FP) receptor agonist widely used to lower intraocular pressure in glaucoma and ocular hypertension. The TxGNN model predicts it may also be effective for **primary hereditary glaucoma**, a genetically-driven subtype of glaucoma, with **1 completed Phase 2 clinical trial** directly supporting this direction. Notably, this predicted indication overlaps substantially with latanoprost's already-established real-world use, rather than representing an entirely novel therapeutic hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Latanoprost is not currently marketed in Singapore, so no local registry text exists); it is internationally recognized as a glaucoma / ocular hypertension therapy |
| Predicted New Indication | Primary Hereditary Glaucoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a structured DrugBank mechanism-of-action record is not available for Latanoprost (data gap DG002). Based on the mechanistic rationale associated with this prediction, Latanoprost acts as a **prostaglandin F2α (FP) receptor agonist**, lowering intraocular pressure by increasing aqueous humor outflow through the uveoscleral pathway. This is the standard, well-established mechanism underlying its established use in glaucoma management.

Primary hereditary glaucoma (including primary congenital/infantile glaucoma) shares the same core pathophysiology as the glaucoma spectrum the drug is already used for: impaired aqueous humor outflow leading to elevated intraocular pressure. Because the underlying pressure-lowering mechanism is disease-subtype agnostic, it is mechanistically plausible that Latanoprost would also lower intraocular pressure in patients with hereditary forms of glaucoma, particularly those refractory to surgical intervention.

It is worth being transparent about the nature of this "prediction": rather than being a novel repurposing hypothesis, primary hereditary glaucoma is a clinical subtype within the same disease family the drug is already used to treat. The single supporting trial identified in this evidence pack directly reflects this — it tests Latanoprost combined with a carbonic anhydrase inhibitor (dorzolamide) specifically in a pediatric/hereditary glaucoma population refractory to surgery, rather than exploring an unrelated organ system or disease mechanism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assessed the ocular hypotensive effect and safety of latanoprost combined with dorzolamide in patients with primary pediatric glaucoma refractory to prior surgical procedures |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Latanoprost is **not currently marketed in Singapore** according to this evidence pack — there are 0 registered licenses and no authorization records to list.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug-interaction data are currently unavailable — see data gap DG001, which flags TFDA/HSA label warnings and contraindications as a blocking item for safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (n=37) directly tests Latanoprost in a hereditary/pediatric glaucoma population, and the underlying FP receptor mechanism is well established and directly transferable across glaucoma subtypes — this is a mechanistically low-risk, evidence-supported prediction. However, the drug currently has no Singapore market presence, and formal safety/labeling data are unavailable, so guardrails are required before any local development or use pathway is pursued.

**To proceed, the following is needed:**
- TFDA/HSA product label — warnings, precautions, and contraindications (data gap DG001, currently blocking safety pre-assessment)
- Formal DrugBank/structured mechanism-of-action record (data gap DG002)
- Additional trials or literature specific to hereditary glaucoma subtypes (currently only 1 supporting trial, no literature)
- Assessment of local registration pathway, given Latanoprost is not currently marketed in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

