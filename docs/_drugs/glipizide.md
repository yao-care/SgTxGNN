---
layout: default
title: Glipizide
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
---

# Glipizide
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

# Glipizide: From Type 2 Diabetes Mellitus to Opsismodysplasia

## One-Sentence Summary

Glipizide is a second-generation sulfonylurea, clinically established for the management of Type 2 Diabetes Mellitus by stimulating pancreatic beta-cell insulin secretion.
The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare skeletal dysplasia caused by *INPPL1* gene mutations.
Currently, **0 clinical trials** and **0 publications** directly support this repurposing direction, and the biological rationale is weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Glipizide is a second-generation sulfonylurea that acts by blocking ATP-sensitive potassium channels (KATP channels) on pancreatic beta cells, triggering membrane depolarisation and calcium-mediated insulin exocytosis. Its efficacy in lowering blood glucose in Type 2 Diabetes Mellitus is well-proven.

Opsismodysplasia is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *INPPL1* gene (encoding SHIP2), which encodes an inositol phosphatase involved in PI3K/Akt signalling. There is no established direct mechanistic link between KATP channel blockade and skeletal chondrocyte development or *INPPL1* pathway regulation.

The TxGNN prediction likely originates from a distant network association within the phosphorylation signalling pathway subgraph in the knowledge graph, rather than a biologically validated mechanism. Given the fundamental disconnect between Glipizide's mode of action and the pathogenesis of opsismodysplasia, this prediction has very limited biological plausibility and should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Glipizide is currently **not registered** in Singapore. No product authorisations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported solely by a TxGNN model score with no clinical trials, no human literature, and no credible mechanistic pathway connecting Glipizide's KATP-channel-dependent insulin secretion mechanism to the skeletal phenotype of opsismodysplasia (an *INPPL1*-driven PI3K/Akt signalling disorder). The prediction likely reflects a distant graph topology association rather than a therapeutically relevant biological relationship.

**To proceed, the following would be needed:**
- Preclinical evidence (in vitro or animal models) demonstrating any effect of KATP channel modulation or sulphonylureas on *INPPL1*-deficient chondrocytes or skeletal development
- Mechanistic studies clarifying whether SHIP2/INPPL1 activity is functionally coupled to KATP channel signalling in bone tissue
- MOA data from DrugBank to support a formal mechanistic gap analysis
- Singapore/TFDA package insert review to assess safety and contraindications before any investigational use is considered
- Given that Glipizide is not registered in Singapore, a regulatory pathway assessment would also be required prior to any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

