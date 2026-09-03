---
layout: default
title: Ursodeoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 1036
evidence_level: L5
indication_count: 10
---

# Ursodeoxycholic Acid
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

# Ursodeoxycholic Acid: From Original Indication (Not Documented) to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

> Ursodeoxycholic acid (UDCA, DrugBank DB01586) has no original indication or mechanism-of-action data available in the current evidence pack.
> The TxGNN model predicts it may be effective for **Homozygous Familial Hypercholesterolemia**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it is a pure computational prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not documented in evidence pack (data gap) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia |
| TxGNN Prediction Score | 99.86% (rank 2,616 of all candidates) |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for ursodeoxycholic acid in this evidence pack (flagged as a High-severity data gap, DG002). No original indication is documented either — `drug.original_indications` is empty and no Singapore license records exist to infer an approved indication from.

Without MOA and original-indication data, it is not possible to construct an evidence-based mechanistic rationale linking UDCA's known pharmacology to lipid-lowering activity in homozygous familial hypercholesterolemia. The TxGNN score (99.86%) reflects a graph-based structural similarity signal only, not a validated pharmacological hypothesis. This gap must be closed (via DrugBank MOA lookup) before any mechanistic justification can be written with confidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Ursodeoxycholic acid is currently **not marketed** in Singapore, and no HSA registration records are present in the evidence pack (`total_licenses: 0`). No authorization table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA warnings and contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any S1 safety pre-screen can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (homozygous familial hypercholesterolemia) has a high TxGNN score but zero supporting clinical trials or literature (Evidence Level L5), the drug's MOA and original indication are undocumented, safety/regulatory data is a blocking gap, and the drug has no market presence in Singapore. There is currently insufficient evidence to advance this candidate.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001, blocking — required before S1 safety pre-screen)
- Mechanism of action data via DrugBank API (DG002)
- Original indication documentation (currently absent from both `drug.original_indications` and Singapore license records)
- Preclinical or clinical evidence specifically linking UDCA to homozygous familial hypercholesterolemia
- Confirmation of Singapore market/registration pathway status

*Secondary note: rank 7 (diabetic nephropathy, TxGNN score 96.7%) has 7 supporting preclinical publications on UDCA's endoplasmic-reticulum-stress and oxidative-stress mechanisms in diabetic kidney injury — this candidate has materially stronger literature support than the top-ranked prediction and may warrant a separate evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

