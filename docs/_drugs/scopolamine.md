---
layout: default
title: Scopolamine
parent: 僅模型預測 (L5)
nav_order: 888
evidence_level: L5
indication_count: 10
---

# Scopolamine
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

# Scopolamine: From [No Local Approved Indication] to Cauda Equina Syndrome

## One-Sentence Summary

> Scopolamine (DrugBank DB00747) is a muscarinic receptor antagonist internationally known for uses such as motion sickness, pre-operative secretion control, and ophthalmic mydriasis/cycloplegia, but it currently holds no marketing registration in Singapore.
> The TxGNN model predicts a possible association with **Cauda Equina Syndrome**, but this direction is currently supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic note flags a potential pharmacological conflict rather than a supportive one.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (market status: 未上市/Not Marketed); no local approved-indication text is available to extract |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% (score 0.9999, model rank 346) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this drug in the evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge, scopolamine is a non-selective muscarinic acetylcholine receptor antagonist, and its established clinical roles (motion sickness, antisialagogue, ophthalmic cycloplegia) all derive from blocking parasympathetic/muscarinic signaling.

For the top-ranked prediction, **Cauda Equina Syndrome**, the model's own repurposing rationale is notably cautious: it states that scopolamine's anticholinergic action could theoretically *worsen* neurogenic urinary retention rather than treat the syndrome, meaning the mechanistic direction may actually run counter to the disease pathology. This is a pure knowledge-graph statistical association (TxGNN score) with no mechanistic, trial, or literature confirmation.

It is worth noting that among the 10 candidates in this evidence pack, indications further down the list — such as **idiopathic uveal effusion syndrome** (rank 9) and **idiopathic panuveitis** (rank 10) — have a more biologically plausible link, since scopolamine eye drops are an established cycloplegic used adjunctively in uveitis to reduce pain and prevent synechiae. However, these also lack any direct supporting trials or literature in this dataset, so they cannot yet be elevated in priority over the top-ranked candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Scopolamine currently has no marketing authorization registered in Singapore (0 licenses on file). No product-level licensing details are available for reporting.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: Local prescribing-label warnings/contraindications (仿單警語/禁忌) are marked as a Blocking data gap in this evidence pack and must be sourced before any safety assessment can proceed.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is an L5, model-prediction-only signal with zero supporting clinical trials or literature. Moreover, the model's own mechanistic rationale suggests the drug's pharmacology may be directionally inconsistent with treating Cauda Equina Syndrome, so there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature
- Local (TFDA/HSA-equivalent) label warnings and contraindications — currently a Blocking data gap
- Independent mechanistic review of the cauda equina syndrome hypothesis, given the internally flagged directional conflict
- If pursuing the alternative ophthalmic-route hypotheses (uveal effusion syndrome, panuveitis), targeted literature search on scopolamine's use as an adjunct cycloplegic in uveitic disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

