---
layout: default
title: Isotretinoin
parent: Low Evidence (L5)
nav_order: 553
evidence_level: L5
indication_count: 10
---

# Isotretinoin
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

# Isotretinoin: From an Unrecorded Original Indication to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is an oral retinoid capsule marketed in Singapore, but the supplied licence records do not state its approved indication.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**.
Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (all licence records have empty indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isotretinoin belongs to the retinoid class and is marketed as oral capsules in Singapore. Its original indication is not recorded in the supplied data, so the link between the original and new indications cannot be assessed.

The score of 99.01% is high, but it is identical to that of the second-ranked prediction, malignant hypertensive renal disease. This suggests both come from the same neighbourhood of the knowledge graph rather than from independent signals. No trial, publication or mechanism supports a link between isotretinoin and malignant renovascular hypertension, so the prediction should be treated as a hypothesis only.

Other predictions have somewhat more context:
- **Chronic pulmonary heart disease** (score 88.70%, Evidence Level L4) has one completed Phase 2 retinoid trial in emphysema, an upstream lung disease. It is only indirect evidence.
- **Pulmonary hypertension due to lung disease and/or hypoxia** (score 98.89%) has 20 retrieved publications. They appear to be generic "hypoxia" keyword matches, and none concern isotretinoin or pulmonary hypertension.
- The remaining candidates have no supporting evidence. Several are poorly defined targets, such as "susceptibility to" terms and an ontology term flagged as obsolete.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

For context, one trial was found for a lower-ranked prediction, chronic pulmonary heart disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000621](https://clinicaltrials.gov/study/NCT00000621) | Phase 2 | Completed | Not reported | Feasibility of retinoic acid in emphysema (FORTE). It tested retinoids in an upstream lung disease, not cor pulmonale. No outcome data were provided, and the agent may not be isotretinoin itself. |

---

## Literature Evidence

Currently no related literature available for malignant renovascular hypertension.

---

## Singapore Market Information

Eight registrations are on record; the five below are the main ones supplied.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13051P | ACNOTIN 20 | Capsule | Not stated in the record |
| SIN14628P | ORATANE CAPSULE 5 mg | Capsule | Not stated in the record |
| SIN11781P | ORATANE CAPSULE 20 mg | Capsule | Not stated in the record |
| SIN13333P | ACNOTIN 10 | Capsule | Not stated in the record |
| SIN11782P | ORATANE CAPSULE 10 mg | Capsule | Not stated in the record |

All products are oral (capsule, including liquid-filled capsule).

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (Evidence Level L5). There are no trials or literature for this indication, the mechanism of action is not available, and the original indication is not documented. Safety screening cannot start without the package insert.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently blocking safety screening
- Mechanism of action data, for example from the DrugBank API
- The approved indication text for the Singapore licences
- A targeted search for trials and literature on isotretinoin or retinoids in renovascular or malignant hypertension
- A route-compatibility assessment, which is still pending
- Optionally, verification that the FORTE trial agent is isotretinoin and a review of its results, if chronic pulmonary heart disease is pursued as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

