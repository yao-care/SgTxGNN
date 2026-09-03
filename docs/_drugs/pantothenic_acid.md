---
layout: default
title: Pantothenic Acid
parent: 僅模型預測 (L5)
nav_order: 754
evidence_level: L5
indication_count: 10
---

# Pantothenic Acid
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

# Pantothenic Acid: From No Established Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

Pantothenic acid (Vitamin B5, DrugBank DB01783) has no formally recorded original indication in this evidence pack and is not currently marketed in Singapore. The TxGNN model's top prediction is **Congenital Prothrombin Deficiency**, but this pairing is currently supported only by **1 loosely related clinical trial** and **no disease-specific literature** — the evidence pack itself flags this as a topological artifact of the knowledge graph rather than a mechanistically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text on file; drug is not marketed in Singapore |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, pantothenic acid is a water-soluble B-vitamin and the essential precursor of coenzyme A (CoA), and its physiological role is well established in fatty-acid and energy metabolism.

The proposed new indication, congenital prothrombin deficiency, is a genetic disorder affecting Factor II (prothrombin) synthesis in the coagulation cascade. There is no established biochemical pathway connecting CoA/pantothenate metabolism to prothrombin gene expression or hepatic synthesis of coagulation factors.

The evidence pack's own mechanistic assessment is explicit on this point: the high TxGNN score is attributed to **knowledge-graph topological similarity** between disease nodes rather than any known biological mechanism. The single associated clinical trial (a dietary-supplement study in hypertensive patients) does not investigate coagulation factor deficiency at all. Taken together, this prediction should be treated as a hypothesis-generation signal only, not as evidence of therapeutic plausibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | NA | Completed | 25 | Cross-over RCT testing a multi-ingredient dietary supplement (L-arginine, Pycnogenol, vitamin K2, alpha-lipoic acid, B-vitamins) on endothelial function in hypertension/hyperhomocysteinemia. Not a study of congenital prothrombin deficiency — flagged as **relevance grade C (mismatch)** in the source data. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Pantothenic acid has no current marketing authorizations on file in Singapore (0 licenses).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence pack shows no mechanistic pathway linking pantothenate metabolism to prothrombin synthesis, and the only associated clinical trial is unrelated to the proposed indication. With no disease-specific literature and evidence level at L5, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for pantothenic acid (currently a data gap — DG002)
- Regulatory safety labeling / warnings and contraindications (currently a data gap — DG001, blocking)
- Preclinical or biochemical evidence for any link between CoA metabolism and coagulation factor II synthesis
- Disease-specific clinical or case-level evidence in congenital prothrombin deficiency populations

**Additional note:** Within this same evidence pack, rank 4 (**folic acid deficiency anemia**) reached a materially stronger evidence position — Evidence Level L3, decision stage S1 ("Research Question"), supported by 4 clinical trials and 4 publications, including a direct trial comparing natural vs. synthetic B-complex vitamins. If prioritizing among this drug's candidates, that indication warrants review ahead of the top-ranked but mechanistically unsupported prediction above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

