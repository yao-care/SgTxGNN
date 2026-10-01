---
layout: default
title: Doravirine
parent: Low Evidence (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Doravirine
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

# Doravirine: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used against HIV-1 infection.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome (FIV)**, a veterinary indication.
There are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from drug class; the Singapore registration data do not state an indication) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Doravirine is known to be an HIV-1 NNRTI, so mechanistically it acts by blocking viral reverse transcriptase.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, which is the likely reason the model links the two. The high score (0.999) is probably driven by proximity between lentivirus and HIV nodes in the knowledge graph rather than by real antiviral activity. FIV reverse transcriptase is generally insensitive to NNRTIs, which weakens the mechanistic case. FIV is also an animal disease, not a human clinical target.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15869P | PIFELTRO FILM-COATED TABLET 100MG | Film-coated tablet |
| SIN15909P | DELSTRIGO FILM COATED TABLET 100MG/300MG/300MG | Film-coated tablet |

## Safety Considerations

- **Drug Interactions**: No interaction records were found in the queried source.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or literature support, and the mechanistic rationale is weak because FIV reverse transcriptase is generally insensitive to NNRTIs. It is also a veterinary indication and likely a graph-proximity artifact.

**To proceed, the following is needed:**
- In vitro data showing doravirine activity against FIV reverse transcriptase
- A decision on whether a veterinary indication is within scope
- The mechanism of action from DrugBank and the HSA package insert (warnings and contraindications)

**Note on other predictions in this pack:** The "congenital human immunodeficiency virus" prediction (rank 5) has Phase 3 RCT support (NCT02275780, NCT02397096) in adult HIV-1. This is essentially the on-label disease family, not true repurposing. Congenital, perinatal, or pediatric use is not established, so it would need its own evaluation with dedicated pediatric and pregnancy PK/safety data.

*This report is for research reference only and does not constitute medical advice. Predicted candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

