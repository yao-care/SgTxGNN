---
layout: default
title: Tremelimumab
parent: 僅模型預測 (L5)
nav_order: 1007
evidence_level: L5
indication_count: 10
---

# Tremelimumab
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

# Tremelimumab: From Oncology (Immune Checkpoint Inhibitor) to Cataract-Related Conditions

## One-Sentence Summary

Tremelimumab is an anti-CTLA-4 monoclonal antibody (immune checkpoint inhibitor) originally developed for oncology use.
The TxGNN model predicts potential effectiveness for **diabetic cataract** and several related cataract subtypes,
but **zero clinical trials** and **zero publications** currently support this direction — the prediction is model-output only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no licensed indications on record) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Tremelimumab is an anti-CTLA-4 monoclonal antibody (immune checkpoint inhibitor) used in oncology, typically in combination with durvalumab for tumors such as hepatocellular carcinoma and non-small cell lung cancer. Its mechanism works by blocking CTLA-4 to sustain T-cell activation and enhance anti-tumor immune response.

There is no known biological link between this mechanism and cataract pathology, which primarily involves lens protein denaturation, oxidative damage, or metabolic/developmental processes. Furthermore, checkpoint inhibitors are well documented to cause immune-related adverse events (irAEs), including ocular inflammation such as uveitis and scleritis — an effect that could plausibly *worsen* rather than improve eye conditions like cataract. This mechanistic mismatch, combined with the complete absence of supporting clinical or literature evidence across all 10 predicted indications, suggests this prediction likely reflects knowledge-graph noise rather than a biologically plausible repurposing opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

This drug currently has no registered market authorizations in Singapore (未上市, 0 licenses on record).

## Safety Considerations

Please refer to the package insert for safety information.

*Note: This evidence pack flags a Blocking data gap — TFDA-equivalent label warnings/contraindications are not yet available, which prevents completion of even a preliminary (S1) safety assessment.*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications (diabetic cataract and 9 related cataract/retinopathy conditions) are supported only by TxGNN model scores with zero clinical trials and zero literature evidence (Evidence Level L5). The proposed mechanism (CTLA-4 blockade/T-cell activation) has no established biological connection to cataract pathology, and checkpoint inhibitors carry a known risk of inducing ocular inflammation — a safety signal that runs counter to the proposed benefit.

**To proceed, the following is needed:**
- Mechanistic or preclinical studies establishing a plausible biological link between CTLA-4 inhibition and cataract/lens pathology
- TFDA/regulatory-equivalent label data (warnings, contraindications) to complete baseline safety assessment (currently a Blocking data gap)
- DrugBank-sourced original MOA and indication data to support comparative analysis
- Independent confirmation that this is not a knowledge-graph artifact, given the pattern of uniformly high scores across biologically unrelated cataract subtypes with no differentiating evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

