---
layout: default
title: Methyl Aminolevulinate
parent: Low Evidence (L5)
nav_order: 660
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methyl Aminolevulinate: predicted new indication Hereditary hemochromatosis (evidence level L5). Approved use: Not recorded in the Singapore license data. Published reviews describ…"
monitor_inn: "methyl aminolevulinate"
predicted_indications: ["hereditary hemochromatosis", "seborrheic keratosis", "acne (disease)", "vulvar inverted follicular keratosis", "psoriasis", "common wart", "drug-induced osteoporosis", "pityriasis lichenoides", "Wilson disease", "iron metabolism disease"]
---

# Methyl Aminolevulinate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Methyl Aminolevulinate: From Topical Photodynamic Therapy to Hereditary Hemochromatosis
{: .text-alpha }

## One-Sentence Summary

Methyl aminolevulinate (Metvix cream) is a topical photosensitizer precursor used in photodynamic therapy (PDT) of skin lesions. The TxGNN model predicts it may be effective for **hereditary hemochromatosis**, but **no clinical trials and no publications** currently support this prediction. It is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore license data. Published reviews describe it as approved for actinic keratosis, basal cell carcinoma and Bowen's disease |
| Predicted New Indication | Hereditary hemochromatosis |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Methyl aminolevulinate is a precursor of the heme-biosynthesis pathway. After topical application it is converted to protoporphyrin IX, which generates reactive oxygen species when activated by red light. This is how it destroys targeted skin tissue in PDT.

The only plausible link to hereditary hemochromatosis is conceptual. Heme biosynthesis uses iron in its final step, so the model may be picking up graph proximity to iron metabolism. Hemochromatosis is a systemic iron-overload disorder, while this product is applied locally to the skin for light-activated treatment. A topical PDT product is unlikely to change systemic iron handling. The high score is probably a knowledge-graph proximity effect rather than a real therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13410P | Metvix 160mg/g Cream (Laboratoires GALDERMA) | Cream (topical) | Not stated in the available license record |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges in the TxGNN knowledge graph, not from label text): photosensitivity disease and photoparoxysmal response. These are consistent with the light-activated nature of the drug.

Please refer to the package insert for the full warnings, contraindications and interaction information. The package insert content has not been obtained yet.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials or publications. The topical, local PDT mechanism does not plausibly address a systemic iron-overload disease. Other predictions in the same candidate list have more support, for example acne (two completed Phase 2 trials, L2) and common warts (case series, L4). If this drug is pursued, they are better candidates for further evaluation than hemochromatosis.

**To proceed, the following is needed:**
- Any mechanistic or preclinical evidence linking methyl aminolevulinate to iron metabolism
- Clarification of route compatibility, since a topical product would be used for a systemic disease
- Mechanism of action data and the package insert warnings and contraindications
- The Singapore approved-indication text, to confirm the original indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

