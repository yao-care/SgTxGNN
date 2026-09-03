---
layout: default
title: Triptorelin
parent: 僅模型預測 (L5)
nav_order: 1021
evidence_level: L5
indication_count: 10
---

# Triptorelin
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

# Triptorelin: From Undocumented Original Indication to Hypertrichosis

## One-Sentence Summary

Triptorelin is a synthetic GnRH (gonadotropin-releasing hormone) agonist; its original approved indication is not documented in the current evidence pack. The TxGNN model's top-ranked prediction is **hypertrichosis (disease)**, but this signal is currently supported by **zero clinical trials** and **zero publications**, and the accompanying mechanistic review flags it as a likely false-positive association.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — original indication data was not provided in the evidence pack (data gap DG001/DG002) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for triptorelin is not available in this evidence pack. Based on the mechanistic notes accompanying the predictions, triptorelin is understood to be a **GnRH agonist** that suppresses gonadal steroid production — a class-level fact confirmed across multiple rationale entries in this dataset (e.g., its established use in precocious puberty, rank 7–8 below).

For the top-ranked prediction, hypertrichosis, the model's own rationale states there is **no clear mechanistic link**: GnRH-agonist-driven suppression of gonadal steroids could plausibly affect *androgen-dependent* hair growth (hirsutism), but hypertrichosis is predominantly **non-androgen-dependent** excessive hair growth. The rationale explicitly notes an absence of supporting evidence for this specific association.

By contrast, several lower-ranked predictions in this pack — familial male-limited precocious puberty (rank 7) and precocious puberty (rank 8) — are strongly supported by dozens of completed Phase 3 trials and publications, consistent with triptorelin's well-known real-world use as a GnRH agonist in pediatric endocrinology. This suggests the TxGNN ranking for hypertrichosis (rank 129 by model score) does not align with the evidentiary strength seen elsewhere in the same drug's prediction set, reinforcing the "Hold" classification for this specific candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Triptorelin currently has **no marketing authorization records** in the Singapore regulatory dataset provided (`market_status: 未上市 / Not Marketed`, `total_licenses: 0`). No license table can be generated from the available data.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as Blocking data gap DG001 — TFDA/local label warnings and contraindications required before any safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (hypertrichosis) has no clinical trial or literature support, and the model's own mechanistic rationale flags it as a likely false-positive association given the mismatch between GnRH-agonist pharmacology and non-androgen-dependent hair growth pathology. Evidence level is L5 (prediction only).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/local package insert warnings and contraindications before any safety pre-assessment (S1) can begin
- Resolve DG002 (High): confirm triptorelin's mechanism of action and original approved indication(s) via DrugBank or product label
- If pursuing repurposing signals for this drug, consider re-scoring/re-ranking candidates by evidence density rather than raw TxGNN score alone — rank 7 (familial male-limited precocious puberty) and rank 8 (precocious puberty) show substantially stronger clinical trial and literature support and warrant separate evaluation
- No action recommended on the hypertrichosis candidate specifically until independent mechanistic or preclinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

