---
layout: default
title: Lixisenatide
parent: 僅模型預測 (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Lixisenatide
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

# Lixisenatide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Lixisenatide is a glucagon-like peptide-1 (GLP-1) receptor agonist used in the treatment of type 2 diabetes mellitus, acting by stimulating insulin secretion in a glucose-dependent manner.
The TxGNN model predicts it may be effective for **Opsismodysplasia**, a rare congenital skeletal dysplasia caused by INPPL1 gene loss-of-function mutations.
Currently, **no clinical trials** and **no publications** support this specific repurposing direction — this prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (GLP-1 receptor agonist class) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.56% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on information embedded in the evidence pack, Lixisenatide is a GLP-1 receptor agonist that increases insulin secretion in a glucose-dependent manner, suppresses inappropriate glucagon secretion, and delays gastric emptying. Its efficacy in type 2 diabetes has been established in multiple large-scale clinical trials.

Opsismodysplasia is an ultra-rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in INPPL1, the gene encoding SHIP2 phosphatase. SHIP2 modulates PI3K/Akt signaling, a pathway involved in bone morphogenesis and chondrocyte differentiation. GLP-1 receptor agonists can indirectly influence PI3K/Akt via cAMP/PKA signaling, and modest evidence suggests GLP-1 may have a minor positive effect on bone mineral density in the context of metabolic disease.

However, the mechanistic link is considered extremely weak. Opsismodysplasia is a congenital structural disorder of skeletal morphogenesis arising from a permanent enzymatic deficiency — a fundamentally different problem from the metabolic dysregulation that GLP-1 receptor agonists address. The PI3K/Akt overlap is highly indirect, and no clinical or preclinical evidence links any GLP-1 receptor agonist to this condition. This prediction most likely reflects shared pathway nodes in the TxGNN knowledge graph rather than a therapeutically actionable relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Lixisenatide is not currently registered or marketed in Singapore. No product authorization records exist in the Singapore Health Sciences Authority (HSA) database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model-only prediction (L5 evidence) with no supporting clinical trials or literature for opsismodysplasia. The mechanistic distance between GLP-1 receptor agonism and this congenital skeletal morphological disorder is too large to justify resource allocation at this stage.

**To proceed, the following is needed:**
- Preclinical mechanistic studies in INPPL1-deficient cell lines or animal models to determine whether GLP-1 receptor activation has any measurable effect on SHIP2-regulated bone morphogenesis
- Full retrieval of lixisenatide's detailed MOA from DrugBank API (currently a data gap)
- Safety data and package insert review from EMA or FDA product information (TFDA registration data unavailable)
- Review of GLP-1 receptor agonist class effects on bone and connective tissue in rare skeletal disease literature before assigning a research priority score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

