---
layout: default
title: Cetrorelix
parent: Low Evidence (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Cetrorelix
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

# Cetrorelix: From Controlled Ovarian Stimulation to Hypertrichosis

## One-Sentence Summary

Cetrorelix is a GnRH receptor antagonist, marketed in Singapore as an injection (CETROTIDE), and its formulation is designed for use in ovarian stimulation.
The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** support this prediction.
The prediction rests on the model score alone, and the mechanistic review found no plausible link.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. Cetrorelix is generally used to prevent premature LH surges in controlled ovarian stimulation (general knowledge, not from the record). |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack. Cetrorelix is a GnRH receptor antagonist. It blocks pituitary GnRH receptors and suppresses LH and FSH, which lowers downstream sex steroids.

Hypertrichosis is mostly a genetic or drug-induced hair follicle disorder, and it is not driven by gonadotropin signalling. No plausible mechanistic link between GnRH antagonism and hypertrichosis was identified. The high score (99.98%, model rank 679) most likely reflects proximity in the knowledge graph rather than a real pharmacological relationship.

The other top predictions show the same pattern. Several are hair phenotypes (Ambras syndrome, isolated hair shaft abnormality, familial trichomegaly). Others are congenital malformations (Dandy-Walker-type syndrome, odontal/periodontal malformation syndrome) or a neonatal condition (persistent fetal circulation). None has a plausible link, and none has supporting studies.

The more biologically plausible prediction in this set is **central precocious puberty** (rank 10, score 99.29%). It is listed in the source as "centra precocious puberty 1", which looks like a typo and should be checked against the source ontology. GnRH antagonism directly targets that disease mechanism. However, GnRH agonists are the standard of care, and the available cetrorelix formulation is short-acting. No trials or literature were retrieved for it either.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

The only literature in the pack was retrieved for the periodontal malformation prediction (rank 3). Those papers cover periodontitis in general and do not involve cetrorelix or GnRH antagonism, so they are retrieval noise and were not counted as evidence.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11345P | CETROTIDE INJECTION 0.25 mg | Injection | Not listed in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no trials or literature and no plausible mechanistic link between GnRH antagonism and hypertrichosis. Safety data is also missing, so the candidate cannot advance to safety screening.

**To proceed, the following is needed:**
- The package insert from the HSA website (warnings and contraindications), which is currently blocking safety screening
- Mechanism of action data from DrugBank
- The approved indication text for SIN11345P
- A targeted literature search on GnRH antagonists in central precocious puberty, and verification of the disease name in the source ontology, since that is the most plausible prediction in this set
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

