---
layout: default
title: Valbenazine
parent: 僅模型預測 (L5)
nav_order: 1040
evidence_level: L5
indication_count: 10
---

# Valbenazine
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

# Valbenazine: From Tardive Dyskinesia to Psychogenic Movement Disorders

## One-Sentence Summary

Valbenazine is a selective VMAT2 inhibitor whose established use (per literature evidence in this pack) is tardive dyskinesia and Huntington's chorea; it is not currently registered in Singapore.
The TxGNN model's top-ranked prediction is **Psychogenic Movement Disorders**, but this specific candidate has **0 clinical trials** and **0 publications** supporting it, and the model's own mechanistic rationale flags it as biologically implausible.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore. Per literature evidence, valbenazine is approved internationally for Tardive Dyskinesia (and Huntington's chorea) |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.82% (rank 3123 overall) |
| Evidence Level | L5 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed formal MOA data for Valbenazine is a data gap. Based on literature within this evidence pack, valbenazine is a selective vesicular monoamine transporter 2 (VMAT2) inhibitor: it downregulates presynaptic packaging and release of dopamine into the neuronal synapse, an action effective in hyperkinetic movement disorders such as tardive dyskinesia and Huntington's chorea (PMID 32454050, 28578484).

Psychogenic (functional) movement disorders, however, are not driven by excess presynaptic dopamine vesicle release — their pathophysiology is understood to be functional/central rather than a dopaminergic packaging defect. The evidence pack's own rationale explicitly notes this: *"功能性（心因性）運動障礙病理機轉非多巴胺囊泡釋放異常，與 VMAT2 抑制作用機轉關聯薄弱"*. Combined with the complete absence of clinical trials or publications for this specific pairing, this appears to be a high TxGNN score without corresponding biological plausibility — a likely false-positive prediction rather than a genuine repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Valbenazine is not currently registered in Singapore (market status: 未上市). No license records are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score, this specific indication (Psychogenic Movement Disorders) has no supporting clinical trials or literature, and the mechanistic rationale itself identifies a poor biological fit. This does not meet the bar to advance past preliminary screening.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent label warnings and contraindications (currently a **Blocking** data gap — required before any S1 safety assessment)
- Formal DrugBank MOA confirmation (currently a **High**-severity data gap)
- Reconsider prioritization: within this same evidence pack, **Chronic Tic Disorder / Tourette syndrome** (rank 5, one Phase 2 trial + 12 publications) and **Drug-Induced Dyskinesia / Tardive Dyskinesia** (rank 10, multiple completed Phase 2–4 RCTs including pivotal KINECT trials) have substantially stronger evidence bases and warrant separate evaluation as more viable candidates than the top-ranked psychogenic movement disorders prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

