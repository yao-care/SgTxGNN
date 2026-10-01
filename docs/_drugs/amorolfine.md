---
layout: default
title: Amorolfine
parent: Low Evidence (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Amorolfine
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

# Amorolfine: From Fungal Nail Infection to Drug-Induced Osteoporosis

## One-Sentence Summary

Amorolfine is a topical antifungal, sold in Singapore as a 5% nail lacquer. The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **0 clinical trials** and **0 publications** supporting this. It rests on a model score alone, with no known biological link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registry text. The products are antifungal nail lacquers, so fungal nail infection is the likely use. |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not well supported. Amorolfine is a topical morpholine antifungal. It inhibits fungal sterol Δ14-reductase and Δ7-Δ8 isomerase, which blocks ergosterol synthesis. The DrugBank mechanism field is not populated, so this description comes from the analysis notes rather than a structured source. No bone-metabolism pathway is documented for the drug.

Fungal nail infection and drug-induced osteoporosis are unrelated conditions. Topical use also implies minimal systemic exposure, so a systemic bone effect is unlikely. The very high score (0.99998) most likely reflects knowledge-graph topology rather than a biological rationale.

The other nine top-ranked predictions have the same problem. They include retroperitoneal disease, lumbar spinal stenosis, sacrum chordoma and abdominal ectopic pregnancy. All are L5 with no trials or literature, and none has a plausible mechanistic link to a topical antifungal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07506P | LOCERYL NAIL LACQUER 5% (Laboratoires Galderma) | Solution | Not listed in the registry extract |
| SIN14604P | AMOROLFINE NAIL LACQUER 5% W/V (Chanelle Medical Unlimited Company) | Solution | Not listed in the registry extract |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials, no literature and no supported mechanism. The drug is topical-only with minimal systemic exposure, and the predicted condition is systemic and unrelated to its known pharmacology.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, currently a blocking gap for safety screening
- Structured mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking sterol-synthesis inhibition to bone metabolism
- Evidence that a non-topical route or a systemic exposure level relevant to the predicted indication is feasible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

