---
layout: default
title: Piracetam
parent: Low Evidence (L5)
nav_order: 789
evidence_level: L5
indication_count: 10
---

# Piracetam
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

# Piracetam: From an Unrecorded Original Indication to Osteoarthritis

## One-Sentence Summary

Piracetam is a marketed drug in Singapore, but the registration records do not state its approved indication.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **0 clinical trials** and **0 publications** currently support this direction.
The prediction rests on knowledge-graph link prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore license records |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.45% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for piracetam, and none of the five Singapore licenses list an approved indication. No mechanistic link to osteoarthritis is documented. The high score (0.985) reflects only the model's knowledge-graph association, not any biological rationale.

Because the original indication is unknown here, the similarity between the original and new indication cannot be assessed. Route compatibility is also unassessed. Piracetam is available as an injection, capsules and film-coated tablets, but the route needed for osteoarthritis has not been defined.

The prediction should be treated as a hypothesis-generating signal only. The closest neighbouring predictions are no stronger: "osteoarthritis susceptibility" is a genetic phenotype rather than a treatable condition, and it is likely an artifact of the osteoarthritis link.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16054P | Cetam Injection 200mg/ml | Injection |
| SIN08477P | Neurocetam Capsule 400 mg | Capsule |
| SIN10738P | Racetam Capsule 400 mg (Orange/white) | Capsule |
| SIN10602P | Cetam Capsule 400 mg | Capsule |
| SIN06408P | Cebrotonin Tablet 800 mg | Tablet, film coated |

The approved indication text is blank in all five records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The osteoarthritis prediction has a high model score but no trials, no literature and no documented mechanism (evidence level L5). Missing safety and indication data also block progression to safety screening.

Other top-ranked predictions are no stronger. Rheumatoid arthritis and hepatic porphyria have only indirect evidence, and all of it concerns levetiracetam, a structural analog, rather than piracetam. The remaining candidates have no evidence and are probably graph-neighbourhood artifacts.

**To proceed, the following is needed:**
- Singapore package insert (warnings and contraindications), downloaded from the HSA website
- Piracetam's approved indications and mechanism of action (for example, from the DrugBank API)
- A literature search for piracetam-specific studies in osteoarthritis, including preclinical work
- A mechanistic rationale linking piracetam to osteoarthritis pathology
- Route and dosage-form compatibility assessment for osteoarthritis

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

