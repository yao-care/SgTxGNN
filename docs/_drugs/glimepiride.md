---
layout: default
title: Glimepiride
parent: Low Evidence (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
---

# Glimepiride
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

# Glimepiride: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a sulfonylurea oral antidiabetic, used for type 2 diabetes. The Singapore licence records supplied do not state an approved indication.
The TxGNN model predicts it may be effective for **focal stiff limb syndrome**, but **no clinical trials and no publications** support this, and no plausible mechanism was identified.
The high score most likely reflects the drug's proximity to diabetes and GAD-autoimmunity in the knowledge graph, not a pharmacological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (not stated in the Singapore licence records) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Glimepiride is a sulfonylurea that blocks the SUR1/Kir6.2 K-ATP channel on pancreatic beta cells and stimulates insulin secretion. Its efficacy in type 2 diabetes is established.

Focal stiff limb syndrome is a rare neuroimmune condition, typically GAD65-associated or paraneoplastic, in the same spectrum as stiff person syndrome. Glimepiride's K-ATP channel blockade has no known role in it.

The likely explanation is graph proximity. Anti-GAD65 autoimmunity often co-occurs with type 1 diabetes, so the knowledge graph places these conditions close to diabetes drugs. This is a statistical association, not a therapeutic rationale. Classic stiff person syndrome received the identical score (99.75%) and has the same weakness.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10459P | AMARYL 2.0 TABLETS 2 mg | Tablet |
| SIN10460P | AMARYL 1.0 TABLETS 1 mg | Tablet |
| SIN10462P | AMARYL 3.0 TABLETS 3 mg | Tablet |
| SIN13674P | DIALOSA TABLET 3MG | Tablet |
| SIN13675P | DIALOSA TABLET 2MG | Tablet |

All products are oral tablets. Approved indication text is not recorded in the licence data received.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (L5). There are no trials or publications, and no pharmacological link between K-ATP channel blockade and stiff-limb neuroimmune disease. Glimepiride's hypoglycaemia risk adds to the concern for a non-diabetic population.

**To proceed, the following is needed:**
- A targeted literature search (glimepiride or sulfonylureas in stiff person spectrum disorders) to confirm there is no signal
- Package insert warnings and contraindications from HSA
- Detailed mechanism of action data, if any mechanism is proposed
- Consider redirecting effort to the same drug's type 1 diabetes prediction (rank 10, L3). It has a T1DM adolescent RCT (PMID 12663616) and preclinical BB-rat data, though it is a diabetes-subtype extension rather than a distinct repurposing signal.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

