---
layout: default
title: Amylmetacresol
parent: Low Evidence (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Amylmetacresol
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

# Amylmetacresol: From Throat Antiseptic Lozenge to Cauda Equina Syndrome

## One-Sentence Summary

Amylmetacresol is an antiseptic ingredient in a throat lozenge marketed in Singapore, and no formal original indication is recorded in the registration data.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction (evidence level L5), so the recommendation is to hold.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data (product type: throat lozenge) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, amylmetacresol is a topical antiseptic used in throat lozenges. Its use in sore throat is not documented in the supplied data, and no mechanistic link to cauda equina syndrome can be established.

Cauda equina syndrome is a compressive neurological emergency, and a topical throat antiseptic has no known relevance to it. The high score (0.9999) is a knowledge-graph prediction only. Systemic exposure from lozenge use is also minimal, which weakens plausibility further.

The other top-ranked predictions show the same pattern:
- Seven of the top ten are ocular conditions (ciliary body disease, panuveitis, iris disease, infectious anterior uveitis, uveitis, ciliary body cancer, benign neoplasm of ciliary body). They appear to share a graph neighborhood rather than reflect a pharmacological rationale.
- Rank 2, "obsolete neurogenic bladder", is flagged obsolete in the ontology, so it may reflect a stale node.
- The only loosely arguable rationale is antiseptic activity for infectious anterior uveitis. No ocular antimicrobial data are available, and intraocular delivery of a lozenge antiseptic is not plausible.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08806P | STREPSILS MAX PLUS LOZENGES | Lozenge | Not recorded in the registration data |

Manufacturer: Reckitt Benckiser Healthcare International Limited; Reckitt Benckiser Healthcare Manufacturing (Thailand) Ltd.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score. There are no trials or literature, no mechanism of action data, and no plausible mechanistic link for cauda equina syndrome or for any of the other top-ten predictions.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- The original approved indication for the Singapore registration
- Any published preclinical or clinical evidence linking amylmetacresol to the predicted condition
- Confirmation that the predicted disease terms are current in the ontology, since one is flagged obsolete
- A route-of-administration feasibility assessment, since a lozenge is not an obvious fit for the predicted conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

