---
layout: default
title: Idarucizumab
parent: Low Evidence (L5)
nav_order: 513
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: From Dabigatran Reversal to Hemoglobinopathy

## One-Sentence Summary

Idarucizumab is an antidote antibody fragment that neutralizes the anticoagulant dabigatran. The TxGNN model predicts it may be effective for **hemoglobinopathy**, but **no clinical trials and no publications** support this prediction. The signal comes from the knowledge graph alone, and the mechanism gives no plausible reason for it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. Known use is reversal of dabigatran's anticoagulant effect |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 95.66% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. The available description is that idarucizumab is a humanized Fab fragment that binds dabigatran with high affinity and neutralizes its anticoagulant effect. It acts on one specific drug, not on a biological pathway.

**The prediction is not mechanistically reasonable.** Idarucizumab has no known action on hemoglobin structure, red cell production, or red cell function. Hemoglobinopathies are inherited disorders of the red cell, so a drug-specific antidote has nothing to act on. The high score (0.957) is a graph-based signal only. It is further weakened because the source record lists no original indications and no mechanism of action.

The other top-ranked predictions show the same pattern. They include rheumatoid arthritis, beta-thalassemia, pyruvate kinase deficiency, bronchitis, and gout. All have no trials, and all lack a plausible mechanistic link. This suggests the predictions are artifacts of knowledge graph connectivity rather than real repurposing signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

For the other predictions, the only publication retrieved is a 2019 case report (PMID [31381100](https://pubmed.ncbi.nlm.nih.gov/31381100/)), listed under gout. It describes reversal of dabigatran in a patient with acute kidney injury, which is the drug's approved use. It does not test idarucizumab as a treatment for gout, and it is not evidence for repurposing.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15083P | PRAXBIND SOLUTION FOR INJECTION/INFUSION 50 MG/ML | Injection, solution | Boehringer Ingelheim Pharma GmbH & Co KG, Biberach |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph model score, with no trials, no relevant publications, and no plausible mechanism. Idarucizumab is a single-target antidote and cannot plausibly act on red cell disorders. It should not advance to safety screening.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for any safety screening)
- Mechanism of action data from DrugBank
- Expert review to confirm whether any of the ten predictions merits follow-up. On current information, none does.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

