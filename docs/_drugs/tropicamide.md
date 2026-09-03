---
layout: default
title: Tropicamide
parent: 僅模型預測 (L5)
nav_order: 1022
evidence_level: L5
indication_count: 10
---

# Tropicamide
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

# Tropicamide: From Ophthalmic Mydriatic Use to Cauda Equina Syndrome

## One-Sentence Summary

> Tropicamide is an anticholinergic agent conventionally used topically as an ophthalmic mydriatic/cycloplegic agent to dilate the pupil for eye examinations.
> The TxGNN model's top prediction suggests possible relevance to **Cauda Equina Syndrome**,
> but this is supported by **0 clinical trials** and **0 publications**, and the model's own rationale flags it as a likely false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; drug class is known as ophthalmic mydriatic/cycloplegic (no formal indication text on file) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap). Based on known pharmacological classification, Tropicamide is an anticholinergic (antimuscarinic, M-receptor antagonist) agent, almost exclusively used as a topical ophthalmic solution for short-acting pupil dilation and cycloplegia during eye exams.

The top-ranked prediction, Cauda Equina Syndrome, is a compressive neurosurgical emergency (nerve root compression from disc herniation, tumor, or trauma) requiring urgent surgical decompression. There is **no mechanistic pathway** by which an antimuscarinic agent would treat this condition. The evidence pack's own rationale explicitly notes this is likely a **false positive**, probably arising from the model's proximity to neighboring "bladder dysfunction" nodes in the knowledge graph rather than a genuine therapeutic signal.

Among the 10 candidates in this evidence pack, only rank 2 (neurogenic bladder) and rank 3 (irritable bowel syndrome) have directionally plausible mechanisms, since antimuscarinics are an established drug class for both conditions — but no pharmacokinetic data exists to support that a topical ophthalmic agent like Tropicamide could reach therapeutic systemic concentrations safely. Rank 8 (primary hereditary glaucoma) is mechanistically **contradictory**: Tropicamide-induced pupil dilation narrows the anterior chamber angle and is a known contraindication in angle-closure glaucoma, making this prediction a safety flag rather than a therapeutic lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tropicamide currently has no marketed product registration in Singapore (0 licenses on file); no product/dosage form/indication data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: local regulatory label warnings and contraindications for Tropicamide are currently unavailable — this is flagged as a **Blocking** data gap (DG001) and must be resolved before any safety pre-screening (S1) can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (cauda equina syndrome) lacks any plausible mechanistic basis and is explicitly flagged by the evidence pack as a likely knowledge-graph artifact/false positive. There are zero clinical trials or publications supporting any of the 10 predicted indications, the drug is not currently marketed in Singapore, and mandatory safety data (label warnings/contraindications) is blocked by a data gap — evidence is insufficient at every level to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain HSA/TFDA package insert warnings and contraindications
- Resolve DG002 (High): obtain mechanism of action data via DrugBank API to properly assess mechanistic plausibility
- If pursuing rank 2 (neurogenic bladder) or rank 3 (IBS) as more mechanistically plausible candidates, obtain pharmacokinetic/systemic absorption data, since Tropicamide currently has no systemic (non-ophthalmic) formulation or dosing precedent
- Re-run TxGNN scoring review to distinguish genuine signal from graph-proximity artifacts, particularly for rank 1 and rank 8, which show contradictory or implausible mechanistic links
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

