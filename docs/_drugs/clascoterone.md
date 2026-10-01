---
layout: default
title: Clascoterone
parent: Low Evidence (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Clascoterone
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

# Clascoterone: From Acne to Candidiasis

## One-Sentence Summary

Clascoterone is a topical androgen receptor inhibitor, marketed in Singapore as Winlevi Cream 1% and known as an acne treatment.
The TxGNN model predicts it may be effective for **candidiasis**,
but **no clinical trials and no publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne (the Singapore registration record does not state an indication) |
| Predicted New Indication | Candidiasis |
| TxGNN Prediction Score | 94.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Clascoterone is a topical androgen receptor inhibitor that acts on the pilosebaceous unit, and its efficacy in acne is the basis for its marketing.

Androgen receptor inhibition has no known antifungal activity. No mechanistic link between clascoterone and *Candida* infection could be established. The high TxGNN score (94.82%) is most likely an artifact of the knowledge graph rather than a real pharmacological signal. Oral candidiasis, a subtype of the same disease, is also predicted (86.71%) and likely shares the same artifact.

The other top-10 predictions are migraine-related conditions, leprosy, atrophoderma vermiculata, adrenal gland hyperfunction and others. All are also L5 with no trials or literature. Among them, skin conditions such as atrophoderma vermiculata are biologically closest to clascoterone's tissue target, but they remain speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17072P | Winlevi Cream 1% w/w | Cream | Not stated in the registration record |

Manufacturer: Cosmo S.p.A. Route: topical only.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found.

As a topical agent, clascoterone has minimal systemic exposure. It may suppress the HPA axis at high exposure, so its use for systemic conditions would need careful safety review.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The candidate has only a model prediction (L5), with no trials, no literature and no plausible antifungal mechanism. The prediction is likely a knowledge-graph artifact.

**To proceed, the following is needed:**
- Mechanism of action data (from DrugBank) and any evidence of antifungal activity, for example in vitro susceptibility of *Candida* species
- The HSA package insert, to complete warnings and contraindications (a blocking gap for safety screening)
- Confirmation of the approved indication text for SIN17072P
- Route compatibility assessment for any proposed use (the product is a topical cream only)
- Any published or registered studies of clascoterone in candidiasis or other candidate indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

