---
layout: default
title: Safinamide
parent: 僅模型預測 (L5)
nav_order: 883
evidence_level: L5
indication_count: 10
---

# Safinamide
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

# Safinamide: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Safinamide is a selective, reversible MAO-B inhibitor with additional sodium/calcium channel-mediated glutamate-release inhibition, originally developed as an adjunct treatment for Parkinson's disease.
> The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**,
> but currently **no clinical trials** and **no published literature** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's Disease (adjunct therapy) — inferred from known pharmacological classification; no structured Singapore label data available |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacological classification, Safinamide is a selective MAO-B inhibitor that also inhibits voltage-gated sodium/calcium channels and reduces excessive glutamate release. Its efficacy as an adjunct therapy in Parkinson's disease has been established, and mechanistically its anti-excitotoxic properties could theoretically extend to conditions involving neuronal hyperexcitability.

However, Rasmussen subacute encephalitis is primarily driven by an autoimmune/neuroinflammatory process rather than dopaminergic deficiency or glutamate-mediated excitotoxicity alone. The knowledge-graph-derived rationale itself flags this link as indirect at best, with no direct mechanistic pathway connecting MAO-B inhibition to the underlying autoimmune inflammation of Rasmussen encephalitis.

It is worth noting that other candidates further down the prediction list — such as **paralysis agitans, juvenile, of Hunt** (rank 6) and **Lewy body dementia** (rank 7) — show substantially stronger mechanistic coherence with Safinamide's known dopaminergic/MAO-B pathway, since both involve parkinsonian and dopaminergic neurodegeneration. These may warrant closer review even though they were not the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Safinamide currently holds no product registrations in Singapore (0 licenses on file); no marketing authorization data is available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Rasmussen subacute encephalitis) is supported only by a model score with no corroborating clinical trials or literature, and the proposed mechanistic link (MAO-B/anti-excitotoxic activity vs. autoimmune encephalitis) is weak. This falls squarely into evidence level L5 with no path to a near-term Go decision.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank or primary literature (currently a Blocking data gap)
- TFDA/HSA label warnings and contraindications to complete the S1 safety screen (currently a Blocking data gap)
- Targeted literature/preclinical search on Safinamide in autoimmune or inflammatory CNS conditions
- Re-evaluation of higher-mechanistic-plausibility candidates further down the ranked list (e.g., juvenile parkinsonism, Lewy body dementia) before committing resources to the top-ranked but mechanistically weaker prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

