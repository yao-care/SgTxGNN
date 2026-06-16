---
layout: default
title: Granisetron
parent: 僅模型預測 (L5)
nav_order: 437
evidence_level: L5
indication_count: 10
---

# Granisetron
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

# Granisetron: From Chemotherapy-Induced Nausea and Vomiting to Manic Bipolar Affective Disorder

## One-Sentence Summary

Granisetron is a selective 5-HT₃ (serotonin type 3) receptor antagonist primarily used to prevent nausea and vomiting induced by chemotherapy, radiotherapy, and postoperative settings.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction rests entirely on model inference from the knowledge graph.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prevention of nausea and vomiting caused by chemotherapy, radiotherapy, and surgery |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.62% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Registered |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Granisetron is a highly selective antagonist of the 5-HT₃ receptor — a ligand-gated ion channel that mediates fast excitatory serotonergic transmission. It exerts its antiemetic effect by blocking 5-HT₃ receptors on peripheral vagal nerve terminals in the gut and centrally in the chemoreceptor trigger zone of the area postrema, suppressing the vomiting cascade triggered by serotonin release during cytotoxic chemotherapy.

The theoretical basis for a role in bipolar mania stems from the known involvement of the serotonin system in mood regulation. 5-HT₃ receptors are expressed at relatively high density in limbic structures — including the hippocampus, amygdala, and prefrontal cortex — that govern emotional processing. Antagonising these receptors could, in principle, dampen aberrant serotonergic excitation in circuits implicated in manic episodes. The Evidence Pack rates this mechanistic link as **weak to moderate**: while the anatomical substrate exists, the precise role of 5-HT₃ receptors in bipolar mania remains speculative, and established mood stabilisers (lithium, valproate, atypical antipsychotics) operate through fundamentally different pathways.

Without any published clinical or preclinical data to anchor this prediction, this signal should be treated as a hypothesis-generating observation only. The high TxGNN score is likely driven by the drug's broad serotonergic footprint in the knowledge graph rather than by direct disease-mechanism evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Granisetron is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product authorisation has been identified in this dataset.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All evidence for this indication is at Level L5 — TxGNN model prediction only, with zero supporting clinical trials or publications. The mechanistic connection between 5-HT₃ antagonism and bipolar mania is theoretical and rated weak to moderate, and granisetron is not currently registered in Singapore, creating an additional regulatory barrier before any clinical use could be considered.

**To proceed, the following is needed:**
- Retrieve full MOA data from DrugBank (DB00889) to complete mechanistic analysis
- Conduct a broader literature search covering the entire 5-HT₃ antagonist class (ondansetron, tropisetron) in bipolar disorder and mania to assess class-level evidence
- Identify and review preclinical (animal model) studies examining 5-HT₃ blockade in manic-like behavioural paradigms
- Obtain TFDA / HSA package insert to assess key warnings, contraindications, and QTc prolongation risk (relevant for psychiatric co-prescribing)
- Evaluate Singapore HSA regulatory pathway and feasibility of new indication registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

