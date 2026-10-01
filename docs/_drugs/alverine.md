---
layout: default
title: Alverine
parent: Low Evidence (L5)
nav_order: 74
evidence_level: L5
indication_count: 10
---

# Alverine
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

# Alverine: From Smooth-Muscle Antispasmodic Use to Dysthymic Disorder

## One-Sentence Summary

Alverine is an oral smooth-muscle antispasmodic, and its registered indication text is not included in the Singapore data supplied.
The TxGNN model predicts it may be effective for **Dysthymic Disorder** (chronic low-grade depression), but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model-only prediction that should be held pending further evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (alverine is generally described as a smooth-muscle antispasmodic) |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the supplied dataset. Alverine is generally described as an antispasmodic that acts on smooth muscle, with reported 5-HT1A receptor antagonist activity. This background pharmacology is not confirmed by the supplied data.

The link to dysthymic disorder is speculative. If the serotonergic activity is real, it could plausibly relate to chronic depressive symptoms, because the serotonin system is implicated in mood regulation. However, the original use (gut smooth-muscle spasm) and dysthymic disorder are different disease areas, and no data bridge them.

The TxGNN score of 99.83% reflects proximity in a knowledge graph, not clinical proof. Several other top-ranked predictions for alverine are also psychiatric or neurological (neurotic disorder, anxiety disorder, neurotic depression, melancholia, migraine). This suggests the model is picking up a serotonergic-type signal. That pattern is consistent, but it is not independent verification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*For context, the closest signal across all predictions is under **anxiety disorder** (rank 3). A 2014 mouse study ([PMID 25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/), *European Journal of Pharmacology*) reported anxiolytic-like effects of alverine citrate in experimental anxiety models. This is preclinical and does not apply directly to dysthymic disorder.*

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17214P | ALMET CAPSULES (XL Laboratories Private Limited) | Capsule, liquid filled (oral) | Not listed in the supplied data |
| SIN16773P | ALVERSIME SOFT CAPSULES (Phil Inter Pharma Co., Ltd.) | Capsule (oral) | Not listed in the supplied data |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the supplied query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dysthymic disorder prediction rests on a knowledge-graph score alone. There are no trials, no literature, and no confirmed mechanism in the supplied data (Evidence Level L5). Safety data are also unavailable, so the candidate cannot move beyond the initial screening stage.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (from the HSA website), which currently block safety screening
- Verified mechanism of action data (for example, from DrugBank) to test the serotonergic rationale
- Human clinical evidence in chronic depressive disorders. A targeted literature search is a reasonable first step.
- Consideration of prioritizing **anxiety disorder** over dysthymic disorder for follow-up, since it is the only prediction with any direct (preclinical) support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

