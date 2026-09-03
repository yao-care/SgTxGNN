---
layout: default
title: Vildagliptin
parent: 僅模型預測 (L5)
nav_order: 1057
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

Using no additional skill — this is a direct report-generation task fully specified by the prompt template; proceeding straight to the deliverable.

# Vildagliptin: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

> Vildagliptin is a DPP-4 inhibitor originally developed to treat type 2 diabetes mellitus by prolonging endogenous incretin (GLP-1/GIP) activity to enhance glucose-dependent insulin secretion.
> The TxGNN model's top-ranked prediction is **Focal Stiff Limb Syndrome**, but this association is backed by **zero clinical trials** and **zero publications**,
> and the accompanying mechanistic review flags it as a likely knowledge-graph artifact rather than a genuine pharmacological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus (DPP-4 inhibitor class; not present in the Singapore registry dataset) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Vildagliptin inhibits dipeptidyl peptidase-4 (DPP-4), which prevents the rapid degradation of the incretin hormones GLP-1 and GIP. By keeping incretin levels elevated after meals, it enhances glucose-dependent insulin secretion from residual pancreatic β-cells and suppresses inappropriate glucagon release — the basis for its approved use in type 2 diabetes.

Focal Stiff Limb Syndrome, however, sits on the stiff-person syndrome spectrum: an autoimmune neurological disorder driven by anti-GAD65 antibodies that impair GABAergic inhibitory neurotransmission. There is no overlap between this pathway and the incretin/insulin-secretion axis targeted by vildagliptin.

The evidence pack's own mechanistic assessment concludes this prediction has **no plausible pharmacological basis**. GAD65 is a shared knowledge-graph node — it is both a pancreatic β-cell autoantigen (linked to diabetes) and the enzyme that synthesizes GABA (linked to stiff-person syndrome). The model's prediction most likely reflects this shared-node co-occurrence rather than any causal or therapeutic relationship. Given the complete absence of clinical trials or literature, this candidate should be treated as a probable false positive rather than a genuine repurposing hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Vildagliptin is currently **not marketed** in Singapore under this evidence pack (0 registrations recorded), so no authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data for vildagliptin were not available in this evidence pack — HSA label data acquisition remains a blocking gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score, this candidate has L5 evidence (model prediction only), no supporting trials or literature, and the drug's own mechanistic profile does not plausibly connect to the predicted disease's autoimmune/GABAergic pathology. The signal is most consistent with a knowledge-graph artifact via the shared GAD65 node rather than a real therapeutic opportunity.

**To proceed, the following is needed:**
- Confirmed vildagliptin MOA and HSA/regulatory label data (contraindications, warnings, DDI) — currently blocking (DG001, DG002)
- Any preclinical or case-level evidence directly testing DPP-4 inhibition in GABAergic/autoimmune neurological disease, if this hypothesis is to be pursued further
- Independent note: within this same evidence pack, **Type 1 Diabetes Mellitus** (rank 10, TxGNN score 99.37%, evidence level **L2**, stage **S2 – Research Question**) is supported by multiple T1DM-specific trials (including a completed Phase 3 Ramadan-fasting study and a double-blind RCT combining rapamycin + vildagliptin) and mechanistically coherent literature on glucagon counter-regulation. That candidate — not Focal Stiff Limb Syndrome — is the one warranting active follow-up evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

