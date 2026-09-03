---
layout: default
title: Pasireotide
parent: 僅模型預測 (L5)
nav_order: 758
evidence_level: L5
indication_count: 10
---

# Pasireotide
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

# Pasireotide: From Cushing's Disease/Acromegaly to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Pasireotide is a multi-receptor somatostatin analog with established use in Cushing's disease and acromegaly. The TxGNN model predicts potential activity in **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**, but this pairing is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own rationale flags the mechanistic link as weak — a pure embedding-similarity signal rather than a validated pharmacological hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cushing's disease / Acromegaly (based on known pharmacology; not present in evidence pack — see DG002) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 96.12% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (data gap DG002, severity High). Based on known pharmacology, pasireotide binds multiple somatostatin receptor subtypes (SSTR1, SSTR2, SSTR3, SSTR5) and is used clinically to suppress ACTH secretion in Cushing's disease and growth hormone/IGF-1 secretion in acromegaly.

NSIAD is a rare congenital disorder caused by constitutively activating mutations of the vasopressin V2 receptor (AVPR2), which produces an antidiuretic phenotype independent of circulating vasopressin levels. As the evidence pack's own repurposing rationale states, pasireotide acts upstream by suppressing hormone secretion (GH, ACTH, etc.) and has no known biological pathway intersecting with a receptor-level constitutive activation defect. The mechanistic link is therefore assessed as weak, and the score should be read as a TxGNN embedding-similarity signal rather than a grounded pharmacological hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Pasireotide currently has no marketing authorization in Singapore (0 registrations).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or literature evidence exists for this drug-disease pair, the mechanistic rationale is explicitly assessed as weak in the source data, and the evidence level (L5) reflects a model-prediction-only signal with no independent corroboration.

**To proceed, the following is needed:**
- HSA/product label data (safety warnings, contraindications — currently blocking, DG001)
- Confirmed mechanism-of-action detail for pasireotide (DG002)
- Preclinical or biological validation connecting somatostatin receptor pathways to AVPR2-driven syndromes before any further stage advancement

**Note:** within this evidence pack, the rank-10 candidate (duodenal obstruction, L4/S1, "Research Question") carries a comparatively stronger — though still indirect — class-effect rationale (analogy to octreotide's use in malignant bowel obstruction) and may warrant separate evaluation if this report set is reviewed further.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

