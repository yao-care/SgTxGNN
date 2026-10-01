---
layout: default
title: Spironolactone
parent: Low Evidence (L5)
nav_order: 925
evidence_level: L5
indication_count: 10
---

# Spironolactone
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

# Spironolactone: From Heart Failure, Hypertension and Edema to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is an aldosterone receptor antagonist with anti-androgen activity, used mainly for heart failure, hypertension and edema.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but **0 clinical trials** and **0 publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Heart failure, hypertension and edema (taken from a retrieved publication; the Singapore HSA registry entries contain no indication text) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the database. Spironolactone is known to block the androgen receptor, and it also blocks the aldosterone (mineralocorticoid) receptor. The high score probably reflects that the drug sits close to other hair-loss conditions in the knowledge graph.

The fit is doubtful. Hypotrichosis simplex is a rare genetic hair disorder (for example, CDSN, APCDD1 and SNRPE variants) and is not known to be driven by androgens. An anti-androgen mechanism therefore has no clear target in this disease. The prediction looks like a graph-proximity artifact rather than a mechanism-based signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16709P | SPIRIDON TABLETS 100MG | Tablet | Not stated in registry data |
| SIN02168P | SPIROLON 100 TABLET 100 mg | Film-coated tablet | Not stated in registry data |
| SIN02222P | ALDACTONE TABLET 25 mg | Tablet | Not stated in registry data |
| SIN16711P | SPIRIDON TABLETS 25MG | Tablet | Not stated in registry data |
| SIN16710P | SPIRIDON TABLETS 50MG | Tablet | Not stated in registry data |

Only 5 of the 7 registrations are listed here. All listed products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). The disease is a rare genetic hair disorder with no known androgen-driven mechanism, so the mechanistic fit is doubtful.

Among the other predictions for this drug, **alopecia** (female pattern hair loss) has the strongest support. It has a completed Phase 2 trial against topical minoxidil (NCT00175617, n=40), several systematic reviews, and an L2 / "Proceed with Guardrails" rating. That prediction is a better candidate to pursue.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently a blocking gap)
- Mechanism of action data from DrugBank
- Any genetic or mechanistic evidence linking androgen or mineralocorticoid signaling to hypotrichosis simplex
- Any case reports or preclinical studies in this condition

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

