---
layout: default
title: Terazosin
parent: 僅模型預測 (L5)
nav_order: 955
evidence_level: L5
indication_count: 10
---

# Terazosin
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

# Terazosin: From Benign Prostatic Hyperplasia to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

> Terazosin is a selective alpha-1 adrenergic receptor antagonist traditionally used to treat benign prostatic hyperplasia (BPH) and hypertension.
> The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**,
> but this ranking currently has **no clinical trials and no supporting literature** — it is a pure model-generated signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia (BPH) / hypertension *(inferred from evidence-pack rationale text; no formal regulatory indication text available)* |
| Predicted New Indication | Hypotrichosis Simplex of the Scalp |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on information embedded in the evidence pack's rationale notes, Terazosin is a selective alpha-1 adrenergic receptor antagonist, clinically established for BPH and hypertension through peripheral vasodilation and smooth-muscle relaxation.

There is no known mechanistic pathway connecting alpha-1 receptor blockade to hair follicle growth stimulation. The evidence pack itself explicitly states this connection is unsupported: *"血管擴張作用與毛囊生長刺激機轉尚無已知關聯"* (the vasodilatory effect has no established link to hair follicle growth stimulation). This ranking is a pure TxGNN statistical output (score 99.97%, rank 784) with zero corroborating clinical trials or literature.

Notably, other lower-ranked predictions in this same batch — **Raynaud disease** (rank 7, L3, two clinical studies directly testing terazosin on vasospasm) and **migraine disorder** (rank 5, L3, two clinical studies from the 1990s) — have meaningfully stronger mechanistic and empirical support, since alpha-1 blockade has a direct, plausible link to vascular tone disorders. These may warrant separate evaluation ahead of the top-ranked hair-loss indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Terazosin is **not currently marketed** in Singapore (0 registrations on file). No license or approved-indication data is available for this drug in the Singapore regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA warning/contraindication data collection is flagged as a **Blocking** data gap — required before any safety-stage evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (hypotrichosis simplex of the scalp) is supported only by a TxGNN statistical score, with no clinical trials, no literature, and no established mechanistic pathway — evidence level L5. Combined with a Blocking data gap on TFDA safety information, this candidate cannot advance past initial screening.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently a Blocking gap
- Confirmed mechanism of action data via DrugBank API
- Any preclinical or case-level evidence linking alpha-1 blockade to hair follicle biology
- Consider re-prioritizing evaluation toward Raynaud disease and migraine prophylaxis, which carry stronger mechanistic rationale (L3) and existing human clinical data, despite lower TxGNN scores
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

