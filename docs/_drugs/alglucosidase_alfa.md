---
layout: default
title: Alglucosidase Alfa
parent: Low Evidence (L5)
nav_order: 64
evidence_level: L5
indication_count: 10
---

# Alglucosidase Alfa
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

# Alglucosidase alfa: From Pompe Disease to Adult Polyglucosan Body Disease

## One-Sentence Summary

Alglucosidase alfa is a recombinant enzyme (acid alpha-glucosidase) that breaks down glycogen inside lysosomes, and it is used as enzyme replacement therapy for Pompe disease.
The TxGNN model predicts it may be effective for **Adult Polyglucosan Body Disease (APBD)**, but **0 clinical trials** and **0 publications** support this direction so far.
The prediction rests on model output alone, and the mechanistic link is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pompe disease (acid alpha-glucosidase deficiency), inferred from the drug's known enzyme function. The Singapore registration record contains no indication text. |
| Predicted New Indication | Adult polyglucosan body disease |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, alglucosidase alfa is a lysosomal enzyme replacement product. It supplies acid alpha-glucosidase (GAA) so that glycogen can be degraded inside lysosomes, which is the defect in Pompe disease.

APBD is a different disease. It is caused by deficiency of glycogen branching enzyme (GBE1), which produces poorly branched polyglucosan that builds up mainly in the **cytosol** of neurons and axons. Both conditions are glycogen-storage disorders, which probably explains the high graph score.

The mechanistic link is **weak and indirect** for three reasons:
- The defective enzyme is different (GBE1 versus GAA).
- The accumulation site is different (cytosol versus lysosome).
- The enzyme does not cross the blood-brain barrier efficiently, and APBD is mainly a neurological disease.

No clinical data were provided to offset these concerns.

The other nine predictions in the top 10 are also L5 with a Hold recommendation:
- **Two forms of GSD type IV** (GBE deficiency, congenital neuromuscular and fatal perinatal) share the same enzyme mismatch as APBD.
- **Seven congenital eyelid, ocular or ptosis-related conditions** (such as entropion, ectropion, Horner syndrome and epiblepharon) have no plausible mechanism and look like knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13543P | Myozyme® (Alglucosidase alfa) 50mg Powder for Solution for Infusion (Genzyme Ireland Limited) | Injection, powder, lyophilized, for solution | Not stated in the registration record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the database query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5), with no trials or publications. The biology argues against it: lysosomal GAA replacement is not expected to reach cytosolic polyglucosan, and brain penetration is poor. The package insert safety data is also missing, which blocks the safety screening step.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently a blocking gap
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence that GAA replacement affects polyglucosan accumulation in APBD or GBE1 deficiency, including whether the enzyme can reach cytosolic polyglucosan and neural tissue
- Route compatibility and similarity-to-original assessments, both still pending
- A review of the other nine top predictions. The GSD IV entries share the same mismatch, and the ocular and ptosis-related entries look like artifacts.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

