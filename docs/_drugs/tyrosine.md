---
layout: default
title: Tyrosine
parent: 僅模型預測 (L5)
nav_order: 1027
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine: From No Approved Indication to Cauda Equina Syndrome

## One-Sentence Summary

Tyrosine is an endogenous amino acid with no approved therapeutic indication and no marketing registration in Singapore; it is more commonly used as a nutritional supplement. The TxGNN model's top-ranked prediction associates it with **Cauda Equina Syndrome**, but this is supported only by a single, mechanistically unrelated case report — **0 clinical trials** and only **1 tangential publication** currently exist for this pairing, and our assessment is that this is very likely an algorithmic false positive.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No approved indication on record — Tyrosine is not registered as a therapeutic product in Singapore |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Tyrosine is not available in this evidence pack. Tyrosine is a naturally occurring, non-essential amino acid that serves as the biochemical precursor to catecholamines (dopamine, norepinephrine, epinephrine) and thyroid hormones (T3/T4). It has no approved indication and no marketing authorization in Singapore, and is more typically encountered as a dietary/nutritional supplement rather than a regulated drug product.

The TxGNN model's top-ranked association — cauda equina syndrome — is not supported by any identifiable mechanistic pathway. The only literature retrieved for this pairing is a 2006 case report describing clear cell sarcoma originating from a spinal (S1) nerve root, a soft-tissue tumour pathology entirely unrelated to tyrosine metabolism, catecholamine synthesis, or thyroid hormone physiology. No clinical trials exist for this indication pair.

Our assessment, consistent with the evidence pack's own `repurposing_rationale`, is that this is very likely an algorithmic false-positive association driven by embedding similarity rather than a genuine pharmacological signal, and it should not be treated as a credible repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case Report | Neurosurgical Focus | Describes a clear cell sarcoma originating from the S1 nerve root, previously misdiagnosed as psammomatous melanotic schwannoma. Concerns tumour pathology/histogenesis, not tyrosine pharmacology — no direct relevance to a tyrosine-based intervention. |

---

## Singapore Market Information

Tyrosine currently has no marketing authorization records in Singapore (0 registered licenses; market status: Not Marketed).

---

## Safety Considerations

No formulation-specific safety data (warnings, contraindications, or drug-drug interactions) is available for Tyrosine in this evidence pack, and it has no marketed drug product in Singapore from which such labeling could be derived. Please refer to general amino-acid supplement safety literature and any product-specific labeling if a specific commercial formulation is being considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication (cauda equina syndrome) has no mechanistic plausibility and is supported only by a single, topic-unrelated case report; evidence level is L5 (model prediction only). This does not meet the threshold to proceed to further evaluation.
- A blocking data gap exists (DG001 — no HSA/TFDA-equivalent labeling data), which independently prevents any Stage 1 safety assessment even if a plausible indication were identified.

**Additional context from the full candidate set:**
All 10 TxGNN-predicted indications for Tyrosine in this evidence pack (including hyperthyroidism, angle-closure glaucoma, POTS, neovascular glaucoma, and thyroid hormone resistance) were independently reviewed and **all received a Hold recommendation**. Several of the higher-scoring candidates (hyperthyroidism, POTS, neovascular glaucoma) are confounded by name collisions between "tyrosine" (the amino acid) and unrelated **tyrosine kinase inhibitor (TKI)** drugs in the underlying trial/literature corpus, and in at least one case (POTS) the retrieved mechanistic evidence points in the *opposite* pharmacological direction (a tyrosine hydroxylase *inhibitor*, not tyrosine supplementation, showed benefit). No candidate in the set reached L3 or better evidence.

**To proceed, the following would be needed:**
- Resolution of DG001 (regulatory labeling/safety data) and DG002 (verified MOA), sourced from DrugBank/regulatory filings rather than inference
- A re-run of literature/trial retrieval with explicit disambiguation between "tyrosine" (amino acid) and "tyrosine kinase inhibitor" drug classes, given the demonstrated confounding across multiple candidates
- If any specific indication is to be pursued further, a standalone mechanistic hypothesis with target-specific supporting evidence — none of the current 10 candidates meet this bar
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

