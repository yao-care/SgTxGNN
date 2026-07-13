---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 522
evidence_level: L5
indication_count: 10
---

# Insulin Lispro
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

# Insulin Lispro: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin lispro is a rapid-acting insulin analog widely used for glycemic control in type 1 and type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**,
with **0 clinical trials** and **0 publications** currently supporting this direction. Evidence support is limited entirely to model prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes Mellitus (Type 1 & Type 2) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Insulin lispro is a rapid-acting analog of human insulin (Lys(B28), Pro(B29) substitution) that binds insulin receptors on target tissues, facilitating glucose uptake in muscle and adipose tissue while suppressing hepatic glucose output. Its altered amino acid sequence at the B-chain terminus reduces self-aggregation, enabling faster absorption compared to regular human insulin.

Autoimmune oophoritis is a rare autoimmune endocrinopathy characterised by lymphocytic infiltration of the ovaries, often co-occurring with other organ-specific autoimmune conditions — most notably type 1 diabetes mellitus, Addison's disease, and autoimmune thyroiditis (autoimmune polyglandular syndromes Type I and II). This comorbidity pattern likely explains the high TxGNN score: the model detects shared "autoimmune endocrine organ destruction" network nodes connecting type 1 diabetes (insulin's primary indication) to oophoritis via polyglandular autoimmune pathways.

However, this is a co-occurrence relationship, not a therapeutic one. Insulin itself exerts no known immunomodulatory activity directed at ovarian tissue. The TxGNN prediction appears to reflect disease network topology rather than a direct mechanism of action. Biological plausibility for insulin lispro as a treatment for autoimmune oophoritis is currently absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Insulin lispro currently has no HSA-registered products in Singapore (0 authorisations on record).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score of 99.78% for autoimmune oophoritis reflects autoimmune disease network co-occurrence with type 1 diabetes rather than any direct mechanistic link between insulin lispro and ovarian autoimmune inflammation. With zero clinical trials, zero supporting literature, no approved Singapore registration, and no established biological rationale, this candidate does not meet the threshold for further development at this time.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for insulin lispro from DrugBank API to confirm or exclude any immunomodulatory properties
- Review of autoimmune polyglandular syndrome literature to assess whether insulin therapy incidentally influences oophoritis progression
- Preclinical evidence establishing biological plausibility of insulin signalling in ovarian autoimmune pathology
- Safety package: full package insert warnings, contraindications, and drug interaction profile (currently unavailable)
- HSA regulatory assessment if future evidence warrants Singapore market entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

