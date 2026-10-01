---
layout: default
title: Aminacrine
parent: Low Evidence (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
---

# Aminacrine
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

# Aminacrine: From Topical Antiseptic to Paratyphoid Fever

## One-Sentence Summary

Aminacrine is registered in Singapore only as a topical gel (MEDIJEL GEL), and the registration record does not state an approved indication. Background knowledge suggests it is an acridine antiseptic, but this is not confirmed by the input data.
The TxGNN model predicts it may be effective for **paratyphoid fever**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record (generally known as a topical antiseptic, unverified) |
| Predicted New Indication | Paratyphoid fever |
| TxGNN Prediction Score | 98.26% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Aminacrine is generally known as a topical acridine antiseptic, but this comes from background knowledge and not from the supplied data. Acridine compounds are also known DNA intercalators, which is likewise unverified here.

Paratyphoid fever is a systemic *Salmonella* infection. A topical antiseptic gel is unlikely to reach the infection site at therapeutic levels, and no mechanistic link is supported. The high score (98.26%) most likely reflects the knowledge-graph structure rather than a pharmacological rationale.

The other top-ranked predictions are also model output only, with no trials or literature:
- **Plausible if Aminacrine is a topical antimicrobial:** sinusitis, chronic ethmoidal sinusitis, apical periodontitis, periapical granuloma and suppurative periapical periodontitis. The last two share an identical score of 95.12%, which suggests a shared graph neighborhood rather than independent signals.
- **Weak fit:** chronic rhinosinusitis, which is mainly inflammatory.
- **Not credible:** epiglottitis, an airway-threatening infection that needs systemic antibiotics; diffuse scleroderma, likely a knowledge-graph artifact; and paranasal sinus neoplasm, where the only rationale is theoretical DNA intercalation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04748P | MEDIJEL GEL (DDD LTD) | Gel | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials, no literature and no mechanism data. The only registered product is a topical gel, which is a poor route match for a systemic infection like paratyphoid fever.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- The approved indication of the registered product
- Route-compatibility assessment (topical gel versus the route needed for the predicted indication)
- Any preclinical or clinical evidence for the predicted indication. Local-infection candidates such as sinusitis or apical periodontitis may be more worth reviewing than paratyphoid fever.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

