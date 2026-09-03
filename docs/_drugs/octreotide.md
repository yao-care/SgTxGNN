---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
---

# Octreotide
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

# Octreotide: From Neuroendocrine Hormone-Hypersecretion Syndromes to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

Octreotide is a somatostatin analog whose known mechanism suppresses GH/IGF-1, glucagon, gastrin, and VIP secretion along the gastro-entero-pancreatic-pituitary axis — used clinically for neuroendocrine hormone-hypersecretion conditions such as acromegaly and carcinoid syndrome. The TxGNN model's top-ranked prediction for this drug is **Vulvar Inverted Follicular Keratosis**, but this is supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic review flags it as a likely knowledge-graph embedding artifact rather than a pharmacologically plausible lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (drug not marketed locally); internationally used for neuroendocrine hormone-hypersecretion syndromes (e.g., acromegaly, carcinoid syndrome), consistent with its somatostatin-analog mechanism |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Octreotide is not available as a structured field in this evidence pack, but the underlying rationale text confirms it acts as a somatostatin analog, binding somatostatin receptors (SSTR1–5) to inhibit growth hormone/IGF-1, glucagon, gastrin, and vasoactive intestinal peptide (VIP) secretion — the basis for its established use in neuroendocrine hormone-hypersecretion states.

Vulvar inverted follicular keratosis is a benign, localized epidermal/follicular keratinocyte proliferative lesion. There is no established relationship between somatostatin receptor signaling and follicular keratinization pathology, and the original indication (systemic neuroendocrine hormone excess) shares neither organ system nor pathophysiology with the predicted one (localized benign skin lesion).

Per the evidence pack's own repurposing rationale, this high TxGNN score most likely reflects proximity of the "keratosis" disease node to other skin/keratinization-related nodes within the knowledge graph embedding space, rather than genuine pharmacological plausibility. No mechanistic pathway currently supports applying Octreotide to this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Octreotide is not currently registered or marketed in Singapore under this evidence pack (0 licenses on record); no HSA authorization data is available for review.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction carries a high TxGNN score but zero clinical or literature support (L5), and the model's own mechanistic assessment identifies it as a probable false-positive driven by embedding proximity rather than a biologically grounded hypothesis linking somatostatin signaling to follicular keratosis.

**To proceed, the following is needed:**
- Formal MOA and DrugBank mechanism data (DG002) to properly assess pathway plausibility
- Preclinical or case-level evidence connecting SSTR signaling to keratinocyte/follicular proliferation
- Singapore/HSA regulatory and safety data (DG001), given the drug is not currently marketed locally
- Note: other candidates in this batch — Addison disease and adrenocortical insufficiency (both L4, with limited diagnostic-use literature) and primary hypereosinophilic syndrome (flagged as a Research Question with a plausible SSTR-mediated rationale but no supporting data) — carry marginally stronger, though still preliminary, evidence and may warrant separate, focused evaluation rather than this top-ranked candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

