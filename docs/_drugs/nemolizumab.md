---
layout: default
title: Nemolizumab
parent: Low Evidence (L5)
nav_order: 696
evidence_level: L5
indication_count: 10
---

# Nemolizumab
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

# Nemolizumab: From Anti-IL-31 Receptor A Therapy to Diabetic Cataract

## One-Sentence Summary

Nemolizumab is an anti-IL-31 receptor A antibody that is already marketed in Singapore as an injectable. The TxGNN model predicts it may be effective for **diabetic cataract**, and nine other eye-related conditions follow closely. This prediction currently has **no clinical trials and no publications** behind it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (approved-indication text is empty on both licences) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.55% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the knowledge graph. What is known is that nemolizumab blocks the IL-31 receptor A, which is the signalling pathway for IL-31, a cytokine linked to itch and skin inflammation.

No established link between IL-31 signalling and diabetic lens opacity was found in the supplied data. Cataract in diabetes is driven mainly by high blood sugar, including polyol pathway activity and oxidative stress, which is unrelated to IL-31 blockade. The same is true for the other cataract subtypes that were predicted.

The top nine predictions are all cataract types, and six of them have the identical score of 0.9849. This pattern suggests the score comes from a shared parent disease node in the knowledge graph rather than from biology specific to each subtype. Diabetic retinopathy ranks tenth (score 98.24%). Inflammatory cytokines play a general role in that disease, but no role for IL-31 has been established, and anti-VEGF treatments already exist. **Overall, the prediction is not biologically supported by the data provided.**

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17206P | NEMLUVIO Powder and Solvent for Solution for Injection in Pre-filled Pen 30 mg | Injection, powder, lyophilized, for solution | Not stated in the supplied data |
| SIN17207P | NEMLUVIO Powder and Solvent for Solution for Injection in Pre-filled Syringe 30 mg | Injection, powder, lyophilized, for solution | Not stated in the supplied data |

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score and no trials or publications. There is also no plausible mechanistic link between IL-31 receptor blockade and cataract, and the near-identical scores across cataract subtypes point to a graph artifact.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indications), which is currently missing and blocks safety screening
- Detailed mechanism-of-action data from DrugBank
- Preclinical or mechanistic evidence that IL-31 signalling plays a role in lens or retinal disease
- A check for any published or registered studies on nemolizumab in eye disease

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

