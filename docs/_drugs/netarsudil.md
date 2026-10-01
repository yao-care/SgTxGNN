---
layout: default
title: Netarsudil
parent: Medium Evidence (L3-L4)
nav_order: 700
evidence_level: L4
indication_count: 10
---

# Netarsudil
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

# Netarsudil: From Open-Angle Glaucoma and Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Netarsudil is a topical eye drop (marketed in Singapore as Rhopressa and Rocklatan) used to lower eye pressure in open-angle glaucoma and ocular hypertension.
The TxGNN model ranks **primary hereditary glaucoma** as its top predicted new indication, but only **1 loosely related clinical trial** and **no publications** support this specific direction, so evidence is at the model-prediction level.
Netarsudil's evidence in ordinary glaucoma is much stronger (see the Conclusion), but that reflects its existing use, not a new repurposing finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Open-angle glaucoma and ocular hypertension (from the Evidence Pack rationale; the Singapore licence records provide no indication text) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Netarsudil inhibits Rho kinase (ROCK) and the norepinephrine transporter. ROCK inhibition relaxes the trabecular meshwork and increases the eye's main fluid outflow route. It also lowers episcleral venous pressure, and norepinephrine transporter inhibition reduces aqueous humour production. Together these effects lower intraocular pressure (IOP). The Evidence Pack has no separate DrugBank mechanism entry, so this description comes from the pack's repurposing rationale and the literature abstracts.

Hereditary glaucoma is also driven by raised eye pressure, so a drug that improves outflow is a plausible fit. The main weakness is that no trial or publication has tested hereditary or paediatric forms of glaucoma specifically. The one linked trial studies a related but different question (see below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06969586](https://clinicaltrials.gov/study/NCT06969586) | N/A | Enrolling by invitation | 50 | Tests whether topical ROCK inhibitors protect corneal endothelial cells after cataract surgery in patients with glaucoma and Fuchs endothelial corneal dystrophy, versus placebo. Not a hereditary glaucoma efficacy study, so it offers only indirect evidence on ocular tolerability. |

---

## Literature Evidence

Currently no related literature available for primary hereditary glaucoma.

A systematic review of topical netarsudil in childhood glaucoma ([PMID 39749726](https://pubmed.ncbi.nlm.nih.gov/39749726/), *Current Eye Research*, 2025) appears under the broader "glaucoma" prediction. Its findings are not included in the Evidence Pack, so it should be read in full before any conclusion is drawn.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16816P | RHOPRESSA Ophthalmic Solution, 0.02% w/v | Sterile solution | Not stated in the data provided |
| SIN16818P | ROCKLATAN Ophthalmic Solution, 0.02% w/v / 0.005% w/v (netarsudil/latanoprost) | Sterile solution | Not stated in the data provided |

---

## Safety Considerations

- **Known adverse events (from the pack's rationale and literature):**
  - Conjunctival hyperemia
  - Corneal verticillata
  - Punctal changes, including a report of partial stenosis and complete punctal closure ([PMID 36223296](https://pubmed.ncbi.nlm.nih.gov/36223296/))
  - Reticular epithelial corneal edema ([PMID 41438161](https://pubmed.ncbi.nlm.nih.gov/41438161/))
  - Corneal flattening in a 4-year-old child with secondary open-angle glaucoma ([PMID 35702654](https://pubmed.ncbi.nlm.nih.gov/35702654/)), which is relevant to any paediatric or hereditary use

Please refer to the package insert for warnings, contraindications and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (99.50%), but there is no efficacy trial or publication for primary hereditary glaucoma, and paediatric safety and efficacy are not established. The predicted use is plausible on mechanism alone, which is not enough to proceed.

**Context from the other predictions in the Evidence Pack:**

| Predicted Indication | Evidence Level | Decision | Comment |
|------|------|------|------|
| Glaucoma; glaucoma 1, open angle; open angle glaucoma | L1 | Proceed with Guardrails | Multiple completed Phase 3 RCTs (e.g. NCT02674854, NCT02558374, NCT02207621). This is the drug's existing use, so it confirms the labelled indication rather than a new one. |
| Axenfeld anomaly, hydrophthalmos (congenital glaucoma) | L5 | Hold | Plausible IOP-lowering rationale, but surgery is the standard of care and there are no trials or literature. |
| Hypoglycemia, hereditary thrombocytopenia with normal platelets, dense granule disease, macrothrombocytopenia with mitral valve insufficiency | L5 | Hold | No credible mechanistic link. Topical eye dosing gives minimal systemic exposure, and the scores likely reflect graph-proximity artefacts. |

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are currently a blocking data gap
- The labelled indication text for the two Singapore licences
- Detailed mechanism-of-action data from DrugBank
- Full review of the childhood glaucoma systematic review (PMID 39749726), and ideally prospective data in hereditary or paediatric glaucoma
- A paediatric-specific ocular safety plan covering corneal changes and punctal effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

