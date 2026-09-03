---
layout: default
title: Somapacitan
parent: 僅模型預測 (L5)
nav_order: 917
evidence_level: L5
indication_count: 10
---

# Somapacitan
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

# Somapacitan: From Growth Hormone Deficiency to Allergic Asthma

## One-Sentence Summary

> Somapacitan is a long-acting human growth hormone (GH) analogue; the evidence pack does not document its original approved indication in Singapore, but by drug class it is used for GH replacement therapy.
> The TxGNN model predicts it may be effective for **Allergic Asthma**, but this prediction is currently supported by **zero clinical trials** and **zero publications** — it is a model-only signal at the earliest evaluation stage (S0).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (drug class: GH replacement therapy) |
| Predicted New Indication | Allergic Asthma |
| TxGNN Prediction Score | 95.73% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (`original_moa` is a data gap). Based on the model's own rationale field, Somapacitan is described as a long-acting human GH analogue that acts primarily via the GH receptor/IGF-1 axis.

There is no established biological link between the GH/IGF-1 axis and the Th2/IgE-driven immune pathways that underlie allergic asthma. The high TxGNN score most likely reflects indirect node proximity within the knowledge graph rather than a genuine shared mechanism — the model's own rationale explicitly flags this as a possible false positive.

Given the absence of any clinical trial, literature, or mechanistic pathway connecting these two conditions, this prediction should be treated as hypothesis-generating only, not as a basis for clinical or research prioritization at this time.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

No Singapore market authorization records are available — Somapacitan is currently **not marketed** in Singapore (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: The evidence pack flags a **Blocking** data gap (DG001) — TFDA/HSA label warnings and contraindications are unavailable, which by itself prevents this candidate from advancing past the initial safety screening stage regardless of efficacy evidence.

---

## Other Ranked Predictions (Context)

All 10 candidate indications for Somapacitan carry the same evidence level (L5) and recommendation (Hold), with only one (rank 3, brain small vessel disease with ocular anomalies) returning any literature — and that literature was assessed as keyword mismatches unrelated to GH therapy. Two candidates warrant particular caution rather than optimism:

- **Diabetic nephropathy** (rank 8): published mechanistic evidence suggests GH/IGF-1 axis *activation* may worsen, not improve, diabetic nephropathy — the predicted direction may be mechanistically inverted.
- **Gout** (rank 6): any plausible link is theoretical and would require a purely speculative uricosuric effect, with competing risk from GH-associated insulin resistance.

None of the 10 predictions currently meet the threshold to leave S0.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's model score (L5), with no clinical trials or literature evidence, an implausible-to-contradictory mechanistic rationale, and a blocking gap in safety labeling data. There is no basis to advance this candidate beyond initial screening.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed original approved indication and full MOA data (DG002)
- Any preclinical or mechanistic literature specifically linking GH/IGF-1 signaling to Th2/IgE-mediated allergic asthma pathways
- Continued monitoring for new clinical trial registrations or publications before re-scoring
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

