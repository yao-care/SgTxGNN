---
layout: default
title: Gemeprost
parent: Low Evidence (L5)
nav_order: 469
evidence_level: L5
indication_count: 10
---

# Gemeprost
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

# Gemeprost: From Obstetric Use (Pregnancy Termination) to Atypical Coarctation of Aorta

## One-Sentence Summary

Gemeprost is a prostaglandin E1 (PGE1) analogue given as a vaginal pessary, and the literature in the Evidence Pack describes it for cervical preparation and early pregnancy termination.
The TxGNN model predicts it may be effective for **atypical coarctation of aorta**, but **0 clinical trials** and **0 publications** support this prediction, so it is most likely a knowledge-graph artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. The literature describes obstetric use (cervical preparation, termination of early pregnancy). |
| Predicted New Indication | Atypical coarctation of aorta |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, gemeprost is a PGE1 analogue (a uterotonic that promotes cervical ripening), and its efficacy in obstetric use is documented. There is no evident mechanistic route to atypical coarctation of aorta.

Atypical coarctation of aorta is a congenital structural vascular anomaly. A uterine-acting prostaglandin pessary would not be expected to correct a structural defect of this kind. The high TxGNN score (98th-plus percentile, but rank 6,254 overall) most likely reflects graph connectivity rather than real pharmacology.

The other top-ranked predictions show the same pattern:

- Several are congenital structural defects (aortic malformation, esophageal malformation), with no evidence found.
- Amenorrhea appears in the literature only as gestational age in abortion studies, not as a disease being treated.
- For vascular indications, the available literature points to harm rather than benefit (see Safety Considerations).

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
| SIN02475P | CERVAGEM VAGINAL PESSARY 1 mg (Ono Pharmaceutical Co Ltd) | Suppository | Not stated in the registration record |

---

## Safety Considerations

- **Cardiovascular signals in the literature**: Case reports describe acute myocardial infarction, coronary vasospasm, cardiogenic shock and stroke after gemeprost or related PGE analogues (PMIDs 18185889, 10904996, 10826591, 11187221, 20224253). These signals argue against any vascular use.
- **Pulmonary artery effects**: In vitro work shows EP3-receptor agonists contract human pulmonary artery (PMID 7834185). This is unfavorable for any pulmonary vascular indication.

Please refer to the package insert for formal warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or literature, and no plausible mechanism for treating a congenital aortic anomaly. The related vascular literature shows safety concerns rather than benefit.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A plausible mechanistic rationale and any preclinical evidence for the predicted indication
- Consideration of higher-ranked predictions only if they show real supporting evidence; none of the other top-10 predictions currently do
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

