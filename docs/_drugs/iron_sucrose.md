---
layout: default
title: Iron Sucrose
parent: 僅模型預測 (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
---

# Iron Sucrose
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

# Iron Sucrose: From Iron Deficiency Anaemia to Primary Hyperoxaluria

## One-Sentence Summary

Iron sucrose is an intravenous iron complex formulation primarily used to treat iron deficiency anaemia (IDA) in patients with chronic kidney disease (CKD) on dialysis, where oral iron is inadequate or not tolerated.
The TxGNN model predicts it may be effective for **Primary Hyperoxaluria**, a rare inherited metabolic disorder caused by excessive oxalate synthesis leading to progressive renal damage.
However, there are currently **no clinical trials** and **no publications** directly supporting this repurposing direction, placing this prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Iron deficiency anaemia (IDA) in chronic kidney disease patients on dialysis |
| Predicted New Indication | Primary Hyperoxaluria |
| TxGNN Prediction Score | 98.82% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for iron sucrose. Based on known pharmacological information, iron sucrose is a composite nanoparticle composed of polynuclear ferric oxyhydroxide stabilised in a sucrose matrix. Following intravenous administration, the iron is released from the sucrose complex and taken up by the reticuloendothelial system, where it is incorporated into haemoglobin and ferritin stores. Its established clinical role is strictly the correction of iron deficiency anaemia, particularly in haemodialysis patients who cannot absorb sufficient iron orally.

Primary hyperoxaluria is caused by loss-of-function mutations in the AGXT, GRHPR, or HOGA1 genes, resulting in overproduction of oxalate and its deposition in the kidneys and other organs. There is no established mechanistic pathway by which iron sucrose could inhibit oxalate biosynthesis or accelerate oxalate clearance. Theoretically, iron participates in mitochondrial enzyme function (IDH, aconitase) and can interact with glyoxalate metabolic intermediates in the TCA cycle, but this connection is highly indirect and speculative with no experimental or clinical support.

The TxGNN model's high prediction score (0.9882) most likely reflects topological similarities in metabolic networks within the knowledge graph rather than a genuine therapeutic signal. The prediction is considered an artefact of network proximity rather than a clinically actionable repurposing opportunity. Among all ten TxGNN-predicted indications in this evidence pack, **hyperparathyroidism (rank 8)** shows the most mechanistically plausible link via the iron deficiency → FGF23 → phosphate homeostasis → parathyroid axis, with supporting literature, and may warrant closer attention in a dedicated evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Iron sucrose is not currently registered with Singapore's Health Sciences Authority (HSA) and holds no active product licences in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for primary hyperoxaluria is evidence level L5 — model prediction only, with no supporting clinical trials, no published literature, and no established mechanistic link between iron sucrose and oxalate metabolism. The high model score most likely reflects knowledge graph topology rather than a genuine therapeutic opportunity, and proceeding without any biological or clinical foundation would not be a responsible use of research resources.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for iron sucrose from DrugBank or published pharmacology resources
- Preclinical (in vitro or animal) evidence demonstrating any measurable effect on oxalate synthesis, glyoxalate metabolism, or oxalate excretion
- Identification of a biologically plausible pathway connecting iron metabolism to primary hyperoxaluria disease biology
- Singapore HSA product licence documentation and approved indication text
- Safety profile documentation (package insert warnings, contraindications, and drug interaction data) before any safety evaluation can proceed

> **Note for researchers:** Among the top-10 TxGNN predictions in this pack, **hyperparathyroidism (rank 8, score 98.62%, evidence level L4)** shows a mechanistically grounded indirect pathway (iron repletion → FGF23 suppression → reduced phosphate reabsorption → secondary hyperparathyroidism improvement) and has associated literature including RCTs on sucroferric oxyhydroxide, a related compound sharing the ferric oxyhydroxide core. A separate dedicated evaluation for that indication may yield a more actionable outcome.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

