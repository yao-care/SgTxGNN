---
layout: default
title: Semaglutide
parent: 僅模型預測 (L5)
nav_order: 896
evidence_level: L5
indication_count: 10
---

# Semaglutide
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

# Semaglutide: From Type 2 Diabetes / Weight Management to Focal Stiff Limb Syndrome

## One-Sentence Summary

> Semaglutide is a GLP-1 receptor agonist established for glycaemic control and weight management (original indication data not directly recorded in this evidence pack — see Data Gap DG002).
> The TxGNN model's top prediction is **Focal Stiff Limb Syndrome**, but this prediction is supported by **0 clinical trials** and **0 publications**, and the model's own rationale explicitly states there is no known biological mechanism linking GLP-1 agonism to this autoimmune/neurological disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (Data Gap DG002). Semaglutide is clinically classified as a GLP-1 receptor agonist for type 2 diabetes/weight management — referenced contextually within the rationale notes, but not confirmed by structured data here |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 98.64% (rank 13,288 of full candidate list) |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for semaglutide is not available in this evidence pack (Data Gap DG002). Based on general drug-class knowledge referenced within the pack's own rationale notes, semaglutide acts as a GLP-1 receptor agonist, primarily used to improve glycaemic control and promote weight loss through effects on insulin secretion, gastric emptying, and appetite regulation.

The link between this mechanism and **Focal Stiff Limb Syndrome** is not supported. The evidence pack's own rationale is explicit on this point: stiff limb syndrome (and the related "classic stiff person syndrome," ranked #2 with an identical score) is a CNS hyperexcitability / autoimmune disorder (often anti-GAD65 mediated), and there is **no known biological pathway** connecting it to GLP-1 receptor signalling. The rationale attributes the high TxGNN score to knowledge-graph embedding similarity among rare-disease clusters, not to genuine mechanistic inference.

It is also worth noting that several lower-ranked candidates in this same batch (ranks 5–7: drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy) raise a **directionality concern** — GLP-1 agonist injection sites are a documented *cause* of localized lipoatrophy, not a treatment for it. This suggests the model may in some cases be capturing adverse-effect associations rather than therapeutic ones, which should be kept in mind when interpreting this entire prediction set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

*Note: Among the other 9 predicted indications in this batch, only rank 9 ("pancreatic agenesis") has associated literature (3 publications, evidence level L4). None of these directly support efficacy — one is a preclinical serotonin/GLP-1 mechanistic study, one is a safety/pretreatment-screening review, and one is a nonhuman-primate pancreatic histopathology study. The rationale further notes a mechanistic contradiction: semaglutide's glucose-lowering effect depends on residual functional β-cell mass, which is typically absent in pancreatic agenesis.*

---

## Singapore Market Information

Semaglutide is not currently registered or marketed in Singapore under this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data are recorded as Data Gaps in this pack — DG001 flags TFDA label warnings/contraindications as a Blocking gap for safety evaluation.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Focal Stiff Limb Syndrome) has zero clinical trial or literature support, and the evidence pack's own mechanistic assessment finds no plausible biological link — attributing the high TxGNN score to knowledge-graph embedding artefacts rather than mechanistic signal. Combined with a Blocking data gap on TFDA safety labeling (DG001) and the drug's non-marketed status in Singapore, this candidate cannot proceed past S0.

**To proceed, the following is needed:**
- TFDA/HSA product labeling (warnings, contraindications) to close Blocking gap DG001
- Confirmed mechanism-of-action data from DrugBank to close High-priority gap DG002
- Confirmed original indication history for semaglutide (currently absent from structured data)
- Independent mechanistic or preclinical rationale specifically linking GLP-1 agonism to stiff person/stiff limb syndrome pathophysiology before any further evaluation is warranted
- Re-review of the broader candidate batch to resolve the directionality concern flagged for the lipodystrophy-related predictions (ranks 5–7)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

