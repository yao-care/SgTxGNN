---
layout: default
title: Risdiplam
parent: 僅模型預測 (L5)
nav_order: 865
evidence_level: L5
indication_count: 10
---

# Risdiplam
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

# Risdiplam: From Spinal Muscular Atrophy to Acne

## One-Sentence Summary

> Risdiplam is an SMN2 pre-mRNA splicing modulator, developed to treat spinal muscular atrophy (SMA) by increasing functional SMN protein levels.
> The TxGNN model's top-ranked prediction is **Acne (disease)**, with a prediction score of **99.45%**,
> but **no clinical trials or published literature currently support this direction**, and the model's own mechanistic rationale explicitly states there is no known biological link between the drug and this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal Muscular Atrophy (SMA) — inferred from mechanistic description in evidence pack; not confirmed by formal regulatory labeling (MOA is a documented Data Gap, DG002) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature for any of the top 10 candidates) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the regulatory dataset (Data Gap DG002). Based on the mechanistic annotations embedded in this evidence pack, Risdiplam acts as an SMN2 pre-mRNA splicing modulator, increasing production of functional SMN protein — a mechanism specific to the neuromuscular pathology of SMA.

Unlike typical repurposing candidates in this system, the evidence pack's own rationale text explicitly concludes that **no plausible biological pathway connects SMN2 splicing modulation to acne pathophysiology** (sebaceous gland inflammation, androgen signaling, *Cutibacterium acnes* colonization). The same pattern repeats across all ten ranked candidates: drug-induced osteoporosis, plasma zinc elevation, common wart, and a cluster of five melanoma-related terms (metastatic melanoma, non-cutaneous melanoma, epithelioid cell melanoma, eyelid melanoma) — none of which share a documented mechanistic overlap with SMN2 splicing regulation.

The recurring melanoma cluster is particularly notable: the rationale for these entries flags it as a likely **knowledge-graph embedding artifact** — diseases positioned close together in TxGNN's latent space due to topological proximity rather than genuine pharmacological relevance. This is a useful signal that the high TxGNN scores here (96–99%) reflect graph-structural similarity rather than validated drug-disease biology, and should not be interpreted as repurposing evidence without independent mechanistic or clinical corroboration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Risdiplam currently has no marketing authorization registered in Singapore (0 licenses on file). No dosage form or approved-indication data is available for local review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Key warnings, contraindications, and drug interaction data are all recorded as Data Gaps in this evidence pack — DG001, marked Blocking severity, since it prevents any S1 safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten TxGNN-predicted indications for Risdiplam are supported only by model scores (Evidence Level L5), with zero clinical trials or literature identified, and the mechanistic rationale itself indicates no credible biological pathway for the top candidate (acne) or several others (melanoma subtypes appear to be a graph-embedding artifact rather than a genuine signal). Combined with the Blocking-severity safety data gap (TFDA/HSA label warnings and contraindications unavailable), this candidate cannot advance past the initial screening stage.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (resolves DG002)
- Official prescribing information / package insert with warnings and contraindications (resolves DG001, currently Blocking)
- Independent mechanistic or preclinical evidence connecting SMN2 splicing modulation to any candidate indication before pursuing S1 review
- If pursued further, re-rank candidates after filtering out likely embedding-artifact clusters (e.g., the five melanoma-subtype entries)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

