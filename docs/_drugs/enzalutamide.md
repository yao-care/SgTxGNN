---
layout: default
title: Enzalutamide
parent: Low Evidence (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Enzalutamide
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

# Enzalutamide: From Prostate Cancer to Prostate Cancer/Brain Cancer Susceptibility

## One-Sentence Summary

Enzalutamide is an androgen receptor (AR) antagonist marketed in Singapore as XTANDI, and prostate cancer is its established use.
The TxGNN model's top-ranked prediction is **prostate cancer/brain cancer susceptibility**, but this is a genetic-predisposition concept rather than a treatable disease.
It has **0 clinical trials** and **0 publications** behind it, so it is a model-only signal with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (taken from the evidence rationale; the HSA record has no indication text) |
| Predicted New Indication | Prostate cancer/brain cancer susceptibility |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Enzalutamide is known to be an AR antagonist. The retrieved evidence describes it as inhibiting AR ligand binding, nuclear translocation and DNA binding.

The predicted term is a susceptibility or genetic-predisposition concept, not a disease that a drug can treat. No AR-based mechanism links it to enzalutamide. The 0.997 score comes from the model alone, with no supporting trials or literature. The model most likely picked up its closeness to prostate cancer in the knowledge graph.

Other predictions for this drug are better supported, but most are on-label rather than true repurposing:

- **Prostate neoplasm (rank 9, 98.37%):** Phase 3 RCT evidence exists (ARCHES, PROSPER, PREVAIL, and NCT01949337). This is enzalutamide's established indication, so it confirms on-label use. It would be graded L1 with "Proceed with Guardrails".
- **Male reproductive organ cancer (rank 6, 99.51%):** The evidence is almost entirely prostate cancer. The L1 grade should not be extended to testicular or penile cancers.
- **Benign prostate and reproductive neoplasms (ranks 2, 4, 5, 7, 8, 10):** The trials and papers concern malignant prostate cancer, not benign tumours. Several of these terms have no evidence at all.
- **Brenner tumor (rank 3):** This looks like an ontology-neighbour artifact with no clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14829P | XTANDI™ Soft Capsules 40mg | Capsule, liquid filled (oral) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. The interaction database query returned no records, which does not mean no interactions exist.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is a susceptibility concept with no mechanistic link, trials or literature, so it is a model-only signal (L5). The well-supported findings for this drug concern prostate cancer, which is enzalutamide's established indication.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Confirmation of the approved indication against the HSA label
- A decision on whether to re-rank candidates so that prostate neoplasm (rank 9) is treated as on-label confirmation, and to drop the susceptibility term as a non-treatable concept
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

