---
layout: default
title: Adapalene
parent: Low Evidence (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Adapalene
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

# Adapalene: From Acne Vulgaris to Elevated Plasma Zinc

## One-Sentence Summary

Adapalene is a topical retinoid marketed in Singapore in acne products (Differin, Epiduo). The TxGNN model predicts it may be effective for **elevated plasma zinc**, but the score is a graph-based signal only, with **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne vulgaris (the HSA registration text is empty; inferred from the products and the evidence pack) |
| Predicted New Indication | Zinc, elevated plasma |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Adapalene is a topical retinoid that acts as an RAR-beta/gamma agonist. It normalizes follicular keratinization and reduces inflammation, which is why it works in acne.

No plausible mechanistic link to zinc homeostasis has been identified. Elevated plasma zinc is a systemic metabolic finding, while adapalene is applied to the skin, with minimal systemic exposure. The very high TxGNN score (0.995) comes from patterns in the knowledge graph and is not supported by any trial or publication, so it should be treated as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN11116P | DIFFERIN CREAM 0.1% | Cream |
| SIN08957P | DIFFERIN GEL 0.1% | Gel |
| SIN15460P | EPIDUO FORTE GEL 0.3%/2.5% | Gel |
| SIN13789P | EPIDUO GEL 0.1%/2.5% | Gel |

The registration data does not include approved indication text.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism. It is L5 (model prediction only). Adapalene is applied topically, so a systemic effect on plasma zinc is unlikely.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications) to complete safety screening
- Mechanism-of-action data from DrugBank
- A biologically plausible mechanism linking retinoid signalling to zinc regulation, and any preclinical or clinical data
- Consideration of lower-ranked predictions such as seborrheic dermatitis (rank 8). It has a plausible sebaceous and anti-inflammatory rationale, but the retrieved evidence concerns acne vulgaris, not seborrheic dermatitis.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

