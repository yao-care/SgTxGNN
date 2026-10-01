---
layout: default
title: Valbenazine
parent: Low Evidence (L5)
nav_order: 1040
evidence_level: L5
indication_count: 10
---

# Valbenazine
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

# Valbenazine: From Tardive Dyskinesia to Psychogenic Movement Disorders

## One-Sentence Summary

Valbenazine is an oral VMAT2 inhibitor used for tardive dyskinesia, an indication not recorded in the Singapore licence text but described in the supporting literature. The TxGNN model predicts it may be effective for **psychogenic movement disorders** with a very high score, but **no clinical trials and no publications** currently support this specific prediction. It is best treated as a model-only signal, probably an artifact of the knowledge graph.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tardive dyskinesia (inferred from the literature; the licence indication text is blank) |
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Based on the supporting literature, valbenazine is a selective VMAT2 inhibitor. It reduces presynaptic dopamine packaging and release, which is the basis for its use in hyperkinetic movement disorders such as tardive dyskinesia.

The model's prediction most likely reflects general similarity between movement disorders in the knowledge graph. Psychogenic (functional) movement disorders are not primarily driven by dopamine excess, so suppressing dopamine release has a weak biological rationale here. A high score with no trials or literature, and a rank of 3123 among all predictions, suggests a knowledge-graph neighbourhood artifact rather than a real therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16198P | REMLEAS HARD CAPSULES 40 MG | Capsule, gelatin coated (oral) | — (not listed in the record) |

Manufacturer: Patheon France S.A.S.

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no trials, no literature and a weak mechanistic rationale. Evidence is at L5 (model prediction only), so there is nothing to justify moving forward for psychogenic movement disorders.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence linking VMAT2 inhibition to functional movement disorders
- The Singapore package insert (warnings, contraindications and the approved indication text)
- Mechanism-of-action data for the drug record

**Other predictions for this drug (outside the scope of this report):**
- **Chronic tic disorder** is the most credible genuine repurposing direction (L3). It has a plausible VMAT2 rationale, a terminated pediatric Phase 2 rollover study (n=6) and real-world reports, but no randomized evidence.
- **Drug-induced dyskinesia (tardive dyskinesia)** is the marketed use, with Phase 3 RCT support (L1). It is not true repurposing, and its guardrails are confirming label status in Singapore and monitoring for depression, suicidality, somnolence, QT effects and CYP2D6/3A4 interactions.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

