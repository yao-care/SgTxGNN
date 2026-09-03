---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 786
evidence_level: L5
indication_count: 10
---

# Pioglitazone
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

# Pioglitazone: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

> Pioglitazone is a thiazolidinedione (TZD) insulin sensitizer, historically used to treat **Type 2 Diabetes Mellitus** by activating PPAR-γ.
> The TxGNN model's top-ranked prediction is **Opsismodysplasia**, a rare INPPL1-related skeletal dysplasia,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, and the model's own rationale notes no known biological link to the PPAR-γ pathway.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 Diabetes Mellitus *(inferred from drug class described throughout the evidence pack — thiazolidinedione / PPAR-γ agonist insulin sensitizer; not separately recorded as a structured field)* |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Pioglitazone is not available in this evidence pack (flagged as a High-severity data gap). Based on the contextual information present across the evidence pack, Pioglitazone is a thiazolidinedione that activates PPAR-γ, improving insulin sensitivity and adipocyte differentiation — a mechanism well established for type 2 diabetes.

However, for the top-ranked candidate, Opsismodysplasia, the model's own repurposing rationale explicitly states there is **no known biological connection** between the PPAR-γ pathway and this disease's underlying pathology (INPPL1 gene mutation causing skeletal dysplasia). The rationale describes this prediction as arising purely from TxGNN graph-similarity inference, without a mechanistic basis.

By contrast, several lower-ranked candidates in this evidence pack — such as the lipodystrophy-spectrum diseases (ranks 5–8) — have a more plausible mechanistic rationale, since PPAR-γ is a key regulator of adipocyte differentiation and TZDs have some off-label precedent in lipodystrophy syndromes. None of these, including the top-ranked candidate, are currently supported by any clinical trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Pioglitazone currently has **no market registrations in Singapore** (0 licenses on file; market status: Not Marketed). No product-level authorization data is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are currently unavailable — retrieval of TFDA/HSA package insert warnings is flagged as a Blocking data gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication, Opsismodysplasia, has an Evidence Level of L5 (model prediction only) with zero clinical trials or literature, and the mechanistic rationale itself acknowledges no plausible biological link to Pioglitazone's PPAR-γ mechanism. Combined with the drug's unmarketed status in Singapore and a Blocking gap in safety data, this candidate does not currently meet the bar for further evaluation.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve TFDA/HSA package insert warnings and contraindications before any S1 safety review
- Resolve DG002 (High): confirm Pioglitazone's mechanism of action via DrugBank API
- If pursuing repurposing further, prioritize re-screening lower-ranked candidates with stronger mechanistic plausibility (e.g., lipodystrophy-spectrum diseases, ranks 5–8) rather than the top-ranked but mechanistically unsupported candidate
- Note: literature retrieved for rank 9 (pancreatic agenesis) was reviewed and found to be keyword-matched false positives (general T2DM/TZD reviews, not disease-specific) — do not treat as supporting evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

