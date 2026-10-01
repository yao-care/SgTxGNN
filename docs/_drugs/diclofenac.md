---
layout: default
title: Diclofenac
parent: Low Evidence (L5)
nav_order: 323
evidence_level: L5
indication_count: 10
---

# Diclofenac
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

# Diclofenac: From NSAID Pain and Inflammation Therapy to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Diclofenac is a nonsteroidal anti-inflammatory drug (NSAID) that inhibits COX enzymes. The registration data supplied does not list its approved indication, so this report treats it as a pain and inflammation drug.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**, a genetic hair-loss disorder, with a very high score.
There are **0 clinical trials** and **0 publications** for this prediction, so it rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the registration data (NSAID for pain and inflammation) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Diclofenac is a COX-1/COX-2 inhibitor that reduces prostaglandin-mediated inflammation and pain.

Hypotrichosis simplex of the scalp is a genetic hair-follicle disorder, and there is no credible mechanistic link between it and COX inhibition. The high score (0.997) has no supporting trials or literature. It is most likely a graph-propagation artifact, meaning the model has propagated similarity from neighbouring nodes rather than found a real pharmacological connection.

The other top-ranked predictions are also unsupported: several skeletal dysplasias, other hypotrichosis conditions, myosclerosis, diffuse alopecia areata and WHIM syndrome. All are L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

The registration data supplied does not include approved indication text, so that column is omitted. Of the 20 registrations, the 5 below are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN10523P | ULTRAFEN 12.5 SUPPOSITORY 12.5 mg | Suppository | Beximco Pharmaceuticals Ltd |
| SIN09088P | APO-DICLO SR TABLET 75 mg | Film-coated tablet | Apotex Inc |
| SIN09951P | RHEWLIN GEL 1% w/v | Gel | Beacons Pharmaceuticals Pte. Ltd. |
| SIN06145P | APO-DICLO TABLET 50 mg | Enteric-coated tablet | Apotex Inc |
| SIN09672P | CLOFEC TABLET 25 mg | Film-coated tablet | Atlantic Laboratories Corpn Ltd |

Across all registrations, the available routes are oral, topical, injectable, suppository and patch. Route compatibility with the predicted indication has not been assessed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no literature and no plausible mechanism (L5, model-only). The high TxGNN score alone is not enough to justify further work on hair-loss disorders.

**To proceed, the following is needed:**
- Any preclinical or clinical evidence linking prostaglandin/COX inhibition to hair-follicle biology in this condition
- Detailed mechanism of action data (MOA) and package insert warnings and contraindications from HSA
- Route compatibility assessment, since topical delivery would be the most plausible route for a scalp condition

**Note on other predictions:** Among the 10 predicted indications, only **juvenile idiopathic arthritis** (score 99.25%, L3, Proceed with Guardrails) has supporting evidence. This includes small, older diclofenac studies from 1983 and 1988. It is closer to an established symptomatic NSAID use than a true repurposing. It would need pediatric dosing guidance and GI, renal and cardiovascular risk review. It is a much better candidate for follow-up than the top-ranked prediction.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

