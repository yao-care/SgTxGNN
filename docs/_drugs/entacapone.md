---
layout: default
title: Entacapone
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Entacapone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Entacapone: From Parkinson's Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a selective, reversible catechol-O-methyltransferase (COMT) inhibitor, used as adjunctive therapy alongside levodopa/carbidopa in Parkinson's disease to reduce "wearing-off" motor fluctuations.
The TxGNN model predicts it may be effective for **PLA2G6-Associated Neurodegeneration (PLAN)**, with **no clinical trials** and **no publications** currently directly supporting this direction.
The prediction rests on a mechanistic analogy: PLAN type III presents as early-onset parkinsonism with substantia nigra dopaminergic degeneration — the same dopamine deficit that Entacapone is designed to address.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (adjunct to levodopa/carbidopa) |
| Predicted New Indication | PLA2G6-Associated Neurodegeneration (PLAN) |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Entacapone is a peripheral and central COMT inhibitor. COMT is the enzyme that methylates and inactivates catecholamines, including dopamine and levodopa. By inhibiting COMT, Entacapone prolongs the plasma and brain half-life of levodopa, enhancing dopaminergic neurotransmission. This mechanism is well-established as adjunctive therapy in Parkinson's disease and is the basis for its repurposing rationale here.

PLA2G6-Associated Neurodegeneration (PLAN) is a rare autosomal recessive disorder caused by loss-of-function mutations in the *PLA2G6* gene, which encodes Group VI calcium-independent phospholipase A2. PLAN presents across three clinical subtypes; type III (adult-onset dystonia-parkinsonism) is most relevant here, as it features progressive degeneration of dopaminergic neurons in the substantia nigra — pathologically and clinically overlapping with idiopathic Parkinson's disease.

The mechanistic link is biologically plausible but indirect. Since PLAN type III patients exhibit the same downstream dopamine deficiency as classical PD, Entacapone could theoretically serve as a levodopa-enhancing adjunct in this subtype, extending levodopa efficacy in patients with proven dopaminergic responsiveness. The plausibility is rated moderate: the mechanism is not specific to the upstream PLA2G6 defect, but rather targets the shared symptomatic endpoint of dopamine depletion. No clinical evidence currently substantiates this hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Entacapone is not currently registered in Singapore. No approved licences, product names, or authorisation numbers are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic extrapolation from Parkinson's disease to PLAN type III is scientifically coherent — both conditions share substantia nigra dopaminergic degeneration — but the evidence remains at L4 (theoretical mechanism only), with no clinical trials, no published studies, and no Singapore regulatory footprint to support advancement at this stage.

**To proceed, the following is needed:**
- Confirm dopaminergic deficit in target patients via imaging (DaT-SPECT or [18F]F-DOPA PET) to establish pharmacological target engagement in PLAN type III
- Document levodopa responsiveness in PLAN type III cases as proof-of-concept before adding Entacapone as an adjunct
- Complete safety data review: retrieve Entacapone package insert warnings, contraindications, and drug interactions (DrugBank API + TFDA/EMA label)
- Assess paediatric/young-adult safety profile, given that PLAN type III onset is typically earlier than idiopathic PD
- Evaluate regulatory pathway: Singapore has zero registrations; a compassionate use or named-patient framework would be required for any clinical application
- Consider case report or small case series design as the minimum evidence threshold before escalating to a formal research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

