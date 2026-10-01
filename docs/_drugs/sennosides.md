---
layout: default
title: Sennosides
parent: Low Evidence (L5)
nav_order: 897
evidence_level: L5
indication_count: 10
---

# Sennosides
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

# Sennosides: From Stimulant Laxative to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Sennosides are a stimulant laxative, and the registration records give no approved indication text.
The TxGNN model predicts they may be effective for **hypotrichosis simplex of the scalp** with a very high score, but **no clinical trials and no publications** support this prediction.
It is a model output only, with no identified mechanism, and the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records; classed as a stimulant laxative |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sennosides are anthraquinone glycosides that act on colonic motility and secretion. They act mainly in the gut with minimal systemic absorption.

No plausible link to hair follicle biology has been identified. The high score is a computational prediction, and because the drug's original mechanism is missing, the knowledge-graph path behind it cannot be checked.

The other top predictions are also unsupported. They are hair-related terms (congenital hypotrichosis milia, diffuse alopecia areata, alopecia), glaucoma terms (open-angle and primary hereditary glaucoma, plus duplicate entries), and esophageal varices. Many of these look like related or duplicate ontology entries that share the same graph neighbourhood, so they are probably not independent signals. None has a plausible mechanism or supporting publications. For esophageal varices, laxatives are sometimes used as supportive care in cirrhosis, but that is not treatment of the varices.

## Clinical Trial Evidence

Currently no related clinical trials registered for hypotrichosis simplex of the scalp.

Two trials were matched to the broader term "alopecia" (NCT03082560, a lichen planopilaris assessment-tool study, and NCT05348343, a platelet-rich plasma pilot). Neither tests sennosides or any related laxative, so they provide no support for this repurposing idea.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04731P | SENOKOT TABLET 7.5 mg (Reckitt Benckiser Healthcare (UK) Ltd) | Tablet | Not listed in the record |
| SIN02550P | SENNA TABLET 7.5 mg (Remedica Ltd) | Tablet | Not listed in the record |

Both products are oral tablets. No topical formulation is registered, which would also matter for any scalp indication.

## Safety Considerations

- **Drug Interactions**: No interaction records were found for this drug.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score (L5). No trial or publication tests sennosides for this condition, and there is no plausible mechanism. The registered oral tablets also do not match a scalp indication.

**To proceed, the following is needed:**
- Mechanism of action data, to check the knowledge-graph path behind the prediction
- Package insert warnings and contraindications, which block safety screening
- Any preclinical or clinical evidence linking sennosides to hair follicle biology
- A route-compatibility assessment, since only oral tablets are registered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

