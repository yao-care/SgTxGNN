---
layout: default
title: Dorzolamide
parent: High Evidence (L1-L2)
nav_order: 344
evidence_level: L2
indication_count: 10
---

# Dorzolamide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Dorzolamide: From Glaucoma / Ocular Hypertension to Primary Hereditary Glaucoma

## One-Sentence Summary

Dorzolamide is a topical carbonic anhydrase inhibitor eye drop used to lower intraocular pressure (IOP) in glaucoma, and it is also available in fixed combinations with timolol.
The TxGNN model predicts it may be effective for **primary hereditary glaucoma**, with **1 clinical trial** and **0 publications** currently supporting this direction.
The one trial studies paediatric glaucoma, so the prediction is best read as an extension within the glaucoma family, not a new disease area.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / ocular hypertension (the Singapore licence records carry no indication text; this is inferred from the evidence pack's mechanism notes) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, dorzolamide is a carbonic anhydrase inhibitor. It acts on carbonic anhydrase II in the ciliary body, reducing aqueous humour production and lowering IOP. Its efficacy in open-angle glaucoma and ocular hypertension is well established, and mechanistically it may be applicable to hereditary glaucoma.

Primary hereditary glaucoma is also a disease of raised eye pressure, so an IOP-lowering drop is a plausible fit. The ontology node overlaps with the approved glaucoma indication, which likely explains the very high score.

The registered trial (NCT01527682) enrols children whose glaucoma was refractory to surgery. Children may differ from adults in systemic absorption, acidosis risk and response, so adult glaucoma data cannot simply be carried over.

Other predictions in the list are weaker:
- Open-angle glaucoma appears twice as separate ontology nodes. It is the on-label benchmark, supported by many Phase 3/4 trials, and should not be counted as a novel repurposing finding.
- The hair-loss, heart failure, pulmonary heart disease and respiratory failure predictions have no plausible mechanism and no therapeutic evidence. They are probably graph artefacts and should be held.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | Completed | 37 | Assesses the IOP-lowering effect and safety of latanoprost and dorzolamide in primary paediatric glaucoma refractory to surgery. Enrolment target was reduced during the study. No results are provided in the record. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN08880P | Trusopt Ophthalmic Solution 2% | Solution |
| SIN14985P | Zolichek Eye Drops Solution 2% | Solution, sterile |
| SIN14556P | Dorzolamide and Timolol Stada Eye Drops 20mg/5mg | Solution, sterile |
| SIN15435P | Cosopt-S Ophthalmic Solution | Solution, sterile |
| SIN14984P | Zolichek-T Eye Drops Solution | Solution, sterile |

---

## Safety Considerations

Please refer to the package insert for safety information.

Consideration for this prediction: the target population is paediatric. Systemic absorption and acidosis with carbonic anhydrase inhibitors should be reviewed before any use in children.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Only one completed Phase 2 trial supports this prediction. It has no published results and no supporting literature, and it studies paediatric glaucoma, which may not match "primary hereditary glaucoma". The safety data gap (package insert warnings and contraindications) is a blocking item.

**To proceed, the following is needed:**
- The HSA package insert, with warnings, contraindications and approved indication text
- Published results of NCT01527682, and confirmation of whether its population is congenital or hereditary glaucoma
- Paediatric safety review (systemic absorption, acidosis)
- Mechanism of action data from DrugBank
- Merging of the duplicate open-angle glaucoma ontology nodes and treating them as on-label benchmarks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

