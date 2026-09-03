---
layout: default
title: Methylthioninium
parent: 僅模型預測 (L5)
nav_order: 659
evidence_level: L5
indication_count: 10
---

# Methylthioninium
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

# Methylthioninium: From Unspecified Original Indication to Irritable Bowel Syndrome

## One-Sentence Summary

Methylthioninium (methylene blue, DrugBank DB08167) has no original indication or approved product on file in this dataset, and it is not currently marketed in Singapore. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome**, but this candidate is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no approved indication on file; drug is unmarketed in Singapore) |
| Predicted New Indication | Irritable Bowel Syndrome |
| TxGNN Prediction Score | 90.43% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Methylthioninium in this dataset. No original indication or marketed product is on file either, so no direct comparison can be drawn between a prior approved use and the predicted new use of Irritable Bowel Syndrome.

Per the model's own rationale, there is no established pharmacological pathway connecting Methylthioninium to irritable bowel syndrome — no gut-motility, visceral-hypersensitivity, or gut-microbiome mechanism is cited. The high TxGNN score is not accompanied by any supporting mechanistic hypothesis, clinical trial, or literature evidence, which places this specific candidate at the lowest confidence tier (L5, model prediction only).

It is worth noting that other candidates generated for this drug carry somewhat stronger rationale — notably dysthymic disorder (rank 2), where methylene blue's known reversible MAO-inhibitory and redox activity offers a plausible (if still unproven) mechanistic link. That candidate reached decision stage S1 ("Research Question"), one step ahead of the irritable bowel syndrome candidate reviewed here, which remains at S0.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Methylthioninium has no registered products in Singapore in this dataset (0 licenses on file; market status: not marketed).

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Regulatory label warnings/contraindications for this drug (TFDA/HSA-equivalent labeling) are a flagged data gap in this evidence pack (blocking severity) — this must be resolved before any safety pre-screen can proceed.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Irritable Bowel Syndrome candidate has the highest TxGNN score in this set but no clinical, literature, or mechanistic support, and the drug itself is unmarketed in Singapore with no safety labeling on file — insufficient basis to advance past model-prediction stage.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for Methylthioninium (currently a data gap)
- Official product labeling / safety warnings and contraindications (blocking data gap — required before any S1 safety pre-screen)
- A testable mechanistic hypothesis linking methylene blue's known pharmacology to IBS pathophysiology
- Consider reprioritizing evaluation toward the dysthymic disorder candidate (rank 2), which already has a stated mechanistic rationale and reached decision stage S1
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

