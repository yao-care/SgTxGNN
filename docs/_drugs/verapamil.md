---
layout: default
title: Verapamil
parent: Low Evidence (L5)
nav_order: 1053
evidence_level: L5
indication_count: 10
---

# Verapamil
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

# Verapamil: From a Calcium Channel Blocker to Bundle Branch Block (Obsolete Ontology Term)

## One-Sentence Summary

Verapamil is a calcium channel blocker marketed in Singapore as an extended-release tablet, but the registration record does not state its approved indication.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but there are **0 clinical trials** and **0 publications** for this prediction (evidence level L5, model prediction only).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data |
| Predicted New Indication | Obsolete bundle branch block |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Verapamil is an L-type calcium channel blocker. It slows atrioventricular (AV) nodal conduction and lowers vascular resistance.

The mechanistic fit with this prediction is doubtful. Slowing AV nodal conduction can worsen conduction disease, so a conduction-block indication is unlikely and raises a safety concern. The disease term is also flagged as obsolete in the ontology, so the high score may be a mapping artifact rather than a real therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00344P | ISOPTIN SR TABLET 240 mg | Tablet, film coated (oral) | Not stated in registration data |

Manufacturer: Famar Anonymous Industrial Single Member Company of Pharmaceuticals and Cosmetics.

## Safety Considerations

- **Mechanistic concern**: Verapamil slows AV nodal conduction and can worsen conduction disease, which directly conflicts with a conduction-block indication.
- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no trials or literature. The target term is obsolete, and the drug's electrophysiological effect argues against benefit and for possible harm.

**To proceed, the following is needed:**
- Retrieval of the HSA package insert (warnings, contraindications, approved indication), which currently blocks safety screening
- Mechanism of action data from DrugBank
- Review of whether the "obsolete bundle branch block" term maps to a current disease entry

**Other candidates worth noting (outside the primary prediction):**
- **Arrhythmogenic right ventricular cardiomyopathy** (score 98.40%, L4, Research Question): the retrieved literature covers verapamil-sensitive and idiopathic ventricular tachycardia, mostly reviews and case reports. It is indirect evidence and needs a cautious safety assessment because of negative inotropy.
- **Periodic paralysis with transient compartment-like syndrome** (score 99.08%, L5, Research Question): a hypothesis based on calcium channel (CACNA1S) biology, for expert review only.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

