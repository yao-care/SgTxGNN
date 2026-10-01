---
layout: default
title: Amantadine
parent: Low Evidence (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Amantadine
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

# Amantadine: From Original Indication Not Recorded to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Amantadine is an oral capsule marketed in Singapore as SYMMETREL 100, but the supplied HSA record does not state its approved indication.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis** (score 99.48%),
but **0 clinical trials** and **0 publications** were retrieved, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied HSA record |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.48% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Amantadine's known pharmacology, as noted elsewhere in the evidence pack, includes NMDA-receptor antagonism, dopaminergic modulation and M2 ion channel inhibition.

The only mechanistic link on file is speculative. NMDA-receptor antagonism might protect against excitotoxic or immune-mediated neuronal injury, which is the kind of damage seen in Rasmussen encephalitis. No trial, case report or study in the retrieved data supports this. The relationship to the drug's original indication cannot be assessed because that indication is not recorded.

The high TxGNN score reflects knowledge-graph similarity, not clinical evidence, and it should not be read as evidence of efficacy.

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
| SIN01481P | SYMMETREL 100 CAPSULE 100 mg (Catalent Germany Eberbach GmbH) | Capsule (oral) | Not stated in the supplied record |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interaction data were available in the supplied records.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the TxGNN score alone (L5). No trials or publications were found for Rasmussen subacute encephalitis, no plausible mechanistic support is documented, and the HSA safety and indication information is missing. This is a blocking gap for safety screening.

**To proceed, the following is needed:**
- Download and parse the HSA package insert (approved indication, warnings, contraindications).
- Retrieve the mechanism of action and original indications from DrugBank (DB00915).
- Run a targeted search for amantadine and Rasmussen encephalitis, including case series and preclinical work.
- Consider prioritising other candidates from the same run that have more supporting evidence:
  - Lewy body dementia (rank 7): class-level memantine evidence only.
  - PLA2G6-associated neurodegeneration (rank 4): one related amantadine paper in a different NBIA subtype.
  - Progressive supranuclear palsy-corticobasal syndrome (rank 9): amantadine appears in an atypical parkinsonism management review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

