---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
---

# Olanzapine
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

# Olanzapine: From Schizophrenia to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Olanzapine is an atypical antipsychotic internationally approved for **schizophrenia and bipolar I disorder**. The TxGNN model's top-ranked prediction is **Benign Paroxysmal Torticollis of Infancy**, but this direction currently has **0 clinical trials** and **0 publications** — it is a model-score-only prediction with no supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Schizophrenia, Bipolar I Disorder (internationally established use; drug is not registered in Singapore, so no local approved-indication text is available) |
| Predicted New Indication | Benign Paroxysmal Torticollis of Infancy |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, olanzapine is a thienobenzodiazepine-class atypical antipsychotic that antagonizes D1–D4 dopamine, 5-HT2A/2C serotonin, muscarinic, histamine H1, and α1-adrenergic receptors; its efficacy in schizophrenia and bipolar I disorder is well established.

Benign paroxysmal torticollis of infancy, however, is an episodic vestibular disorder of early childhood believed to sit on the migraine spectrum. There is no known mechanistic link between D2/5-HT2A receptor antagonism and this condition's pathophysiology, and the extrapyramidal side-effect risk of antipsychotics in infants further undermines plausibility.

Taken together, this is the highest-scoring TxGNN output by rank, but it is not accompanied by any mechanistic rationale, clinical trial, or literature support. It should be read as a raw model signal rather than a substantiated repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Olanzapine is not currently registered in Singapore under this evidence pack (0 licenses on file); no product/dosage-form/indication records are available for listing.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Benign Paroxysmal Torticollis of Infancy) has zero clinical trials, zero literature, no plausible mechanistic link, and is explicitly scored L5/S0 — model prediction only, insufficient to advance.
- The drug is not currently marketed in Singapore, and a Blocking data gap (TFDA/HSA label warnings and contraindications) prevents even a preliminary safety assessment.

**To proceed, the following is needed:**
- Official label/package insert data (warnings, contraindications, DDI) to close the Blocking data gap
- Confirmed mechanism-of-action documentation (currently a data gap)
- If pursuing repurposing further, note that other candidates in this same evidence pack — **neurotic depression** and **melancholia** (rank 6–7, Evidence Level L2, "Proceed with Guardrails") — are backed by multiple systematic reviews/network meta-analyses and align with the already-approved olanzapine–fluoxetine combination for treatment-resistant depression; these represent a substantially stronger basis for evaluation than the top TxGNN-ranked candidate above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

