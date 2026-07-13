---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 519
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting recombinant basal insulin analog, widely used as the standard of care for glycaemic management in diabetes mellitus (Types 1 and 2).
The TxGNN model predicts it may be effective for **Autoimmune Oophoritis**,
with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction rests entirely on knowledge graph topology, placing it at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes Mellitus (Types 1 & 2) |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on established pharmacology, Insulin glargine is a long-acting recombinant human insulin analog that binds insulin receptors (INSR) and, with weaker affinity, IGF-1 receptors (IGF-1R). It provides a steady, peakless 24-hour basal insulin supply primarily to regulate hepatic glucose output and peripheral glucose uptake in patients with diabetes mellitus.

Autoimmune oophoritis is a T-cell–mediated autoimmune disease in which immune cells attack and destroy ovarian granulosa cells, ultimately leading to premature ovarian insufficiency. The TxGNN model likely identified this prediction through shared pathway nodes in the knowledge graph: INSR is physiologically expressed in ovarian granulosa cells and plays a role in steroidogenesis, meaning insulin signalling and ovarian biology are not entirely disconnected at a molecular level.

However, the connection is indirect. Insulin glargine's primary pharmacological action — lowering blood glucose — has no established relationship to the T-cell–driven inflammatory cascade responsible for autoimmune oophoritis. There is currently no clinical, animal-model, or in-vitro evidence supporting the use of insulin glargine as a therapeutic agent for ovarian autoimmune disease. The high TxGNN score most likely reflects the density of INSR/IGF-1R pathway connections in the knowledge graph rather than a clinically exploitable treatment mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Insulin glargine currently holds **no active product registrations** with the Health Sciences Authority (HSA) of Singapore. The drug is not marketed in Singapore as of the data cutoff date (2026-04-04). Any future clinical or research use in Singapore would require prior regulatory assessment and market authorisation.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN prediction score (99.88%), Insulin glargine's predicted indication in autoimmune oophoritis is supported by zero clinical trials and zero published studies (Evidence Level L5). The mechanistic link is speculative — driven by shared INSR pathway nodes in the knowledge graph — and there is no therapeutic rationale to justify clinical investigation at this stage. Additionally, the drug is not registered in Singapore, creating a compounding regulatory barrier.

> ⚠️ **Additional note from this Evidence Pack:** Among the 10 predicted indications reviewed, **rank 7 (drug-induced localized lipodystrophy)** carries a specific safety flag — insulin glargine injection is itself a well-documented *cause* of injection-site lipodystrophy, representing a reverse safety concern rather than a treatment opportunity. This should be prominently flagged if the knowledge graph is used for downstream decision-making.
>
> Conversely, **rank 6 (pancreatic agenesis, Evidence Level L3)** represents the most clinically coherent prediction in this pack: neonates born without a pancreas require life-long exogenous insulin, and insulin glargine as a basal insulin is mechanistically appropriate. This candidate may warrant a separate, focused evaluation report.

**To proceed with the autoimmune oophoritis indication, the following is needed:**

- Mechanistic studies examining whether insulin/IGF-1R signalling modulates ovarian granulosa cell survival or autoimmune infiltration in vitro or in animal models
- Preclinical proof-of-concept data in an autoimmune oophoritis model (e.g., neonatal thymectomy murine model)
- Full MOA characterisation for Insulin glargine (currently unavailable — remediation via DrugBank API)
- Package insert safety review (currently unavailable — remediation via HSA/manufacturer documentation)
- Regulatory pathway consultation for Singapore market entry (HSA), given zero existing registrations
- Re-evaluation of evidence level: advancement from L5 to at least L4 is required before any clinical hypothesis can be formally considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

