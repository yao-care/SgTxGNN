---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 1005
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

> Travoprost is a prostaglandin (PGF2α) analogue used to lower intraocular pressure in glaucoma and ocular hypertension.
> The TxGNN model's top prediction is **Visceral Calciphylaxis**, with a raw score of **99.9998%**,
> but this candidate is currently supported by **0 clinical trials** and **0 publications**, and the evidence pack's own mechanistic analysis flags it as likely model noise.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glaucoma / Ocular Hypertension (inferred from trial/literature context in the evidence pack; no structured field available) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

The structured `original_moa` field is marked as a data gap, but the evidence pack's own rationale text describes Travoprost's mechanism: it is a PGF2α prostaglandin analogue that activates FP receptors to increase uveoscleral outflow, thereby lowering intraocular pressure — the standard mechanism underlying its established use in glaucoma and ocular hypertension.

Visceral calciphylaxis is a vascular calcification / microthrombotic disorder affecting internal organ vasculature. The evidence pack explicitly states there is **no known mechanistic link** between local FP-receptor-mediated ocular pressure reduction and the calcification/microthrombosis pathophysiology of calciphylaxis, and characterizes this prediction as likely arising from embedding-level semantic similarity around the term "vascular" rather than a genuine pharmacological signal.

No clinical trials or literature currently exist for this specific drug-disease pair. Combined with the explicit noise-flag in the model's own rationale, this candidate does not currently meet the bar for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/HSA label warnings and contraindications data (DG001, blocking gap) have not yet been retrieved, which prevents any formal safety assessment for this or other candidates involving this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (visceral calciphylaxis) has zero clinical trial or literature support, and the evidence pack's own mechanistic analysis identifies it as probable model noise rather than a genuine signal. Combined with the drug not being marketed in Singapore (0 registrations) and a blocking gap in label safety data, there is no basis to proceed.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — currently blocking (DG001)
- Verified mechanism-of-action reference for Travoprost (DG002)
- Independent, non-embedding-based validation of any mechanistic link to calcification/vascular pathophysiology before further evaluation

**Note for portfolio triage:** Among this drug's 10 ranked candidates, only **"vascular disease"** (rank 5) has any supporting evidence — a Phase 4 trial (NCT00308945) directly measuring travoprost's effect on retinal vascular diameter and choroidal blood flow, reaching evidence level L4 and stage S1 ("Research Question"). However, this evidence reflects a *local ocular* pharmacological effect, not treatment of systemic vascular disease, and should not be conflated with efficacy for that broad indication. If this drug is to be pursued further for repurposing, rank 5 — not rank 1 — is the more defensible starting point.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

