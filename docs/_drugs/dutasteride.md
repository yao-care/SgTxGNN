---
layout: default
title: Dutasteride
parent: Low Evidence (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Dutasteride
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

# Dutasteride: From a 5-Alpha Reductase Inhibitor (Original Indication Not Listed) to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Dutasteride is a 5-alpha reductase inhibitor that lowers dihydrotestosterone (DHT), and its registered indication text is blank in the Singapore records provided.
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **0 clinical trials** and **0 publications** support this prediction. It rests on the model score alone, and the mechanistic link is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated (all approved indication fields in the Singapore registration records are blank) |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank in this dataset. The candidate-level analysis notes that dutasteride inhibits 5-alpha reductase types 1 and 2, which lowers DHT. That mechanism is relevant to androgen-driven hair conditions.

The link to the predicted indication is weak. Ambras syndrome is a congenital condition caused by chromosomal rearrangements affecting *TRPS1* regulation, and it is not driven by androgens. Blocking DHT has no established rationale for it. The high score most likely reflects hair-phenotype proximity in the knowledge graph rather than a therapeutic rationale.

Other top-ranked predictions show the same pattern:
- **Hair-related conditions** (hypertrichosis, hair shaft abnormality, hypotrichosis simplex, congenital hypotrichosis milia, trichomegaly): these are mostly genetic, non-androgen-mediated disorders, and there is no supporting evidence for any of them.
- **Diffuse alopecia areata (rank 8)**: this is the only prediction with any indirect signal (Evidence Level L4, "Research Question"). The one retrieved item is a review of androgenetic alopecia in women, a different alopecia type. Alopecia areata is autoimmune, so the mechanism does not transfer directly.
- **Unrelated developmental or neurological conditions** (Dandy-Walker syndrome, migraine with brainstem aura, odontal/periodontal malformation): no plausible mechanism. The 20 periodontitis papers retrieved for the periodontal malformation prediction never mention dutasteride, so they are a keyword match and not evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

The table lists 5 of the 10 registrations. The other 5 were not provided in the Evidence Pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16448P | DUTABIT 0.5 SOFT CAPSULES 0.5MG | Capsule, liquid filled | Not stated in registration record |
| SIN15882P | RAFUSTER SOFT CAPSULES 0.5 MG | Capsule, liquid filled | Not stated in registration record |
| SIN15563P | INTASTERIDE SOFT CAPSULE 0.5MG | Capsule, liquid filled | Not stated in registration record |
| SIN16476P | ARIPSA SOFT CAPSULES 0.5MG | Capsule, liquid filled | Not stated in registration record |
| SIN15590P | DUTASVITAE SOFT CAPSULE 0.5MG | Capsule, liquid filled | Not stated in registration record |

All listed products are oral formulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but no clinical trials or literature support it. The mechanism (DHT suppression) does not fit a congenital, non-androgen-dependent condition. Safety and indication data from the Singapore package inserts are also missing.

**To proceed, the following is needed:**
- HSA package insert warnings, contraindications and approved indications (currently blocking any safety screening)
- Mechanism of action data from DrugBank to support mechanistic-link analysis
- Genetic and mechanistic review of Ambras syndrome (*TRPS1*-related) to test whether any androgen-pathway role exists
- Evaluation of diffuse alopecia areata (rank 8) as a separate research question, with differential diagnosis and immune-mediated pathways reviewed first
- Route compatibility and similarity-to-original assessments, which are still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

