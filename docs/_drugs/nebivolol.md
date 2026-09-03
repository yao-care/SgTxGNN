---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 695
evidence_level: L5
indication_count: 10
---

# Nebivolol
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

# Nebivolol: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Nebivolol is a third-generation, β1-selective adrenergic receptor blocker with nitric oxide-mediated vasodilatory activity, originally used to treat hypertension. The TxGNN model's top-ranked prediction is **Malignant Hypertensive Renal Disease**, but this specific candidate currently has **0 clinical trials** and **0 publications** supporting it — the signal comes from the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (per evidence-pack rationale text; no Singapore license data available — drug not locally marketed) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on information present elsewhere in the evidence pack, Nebivolol is a third-generation β1-selective adrenergic receptor blocker that also promotes nitric-oxide-mediated vasodilation, distinguishing it from older-generation beta-blockers. Its efficacy in essential hypertension is well established as its core pharmacological use.

Malignant hypertensive renal disease is a severe form of hypertension-driven renal vascular injury, so blood pressure control is mechanistically central to its management. In principle, an antihypertensive agent like Nebivolol could contribute to this goal, which is presumably why the model assigned it a high score.

However, this mechanistic plausibility is not backed by any disease-specific evidence: no clinical trials or literature records were retrieved for this drug–disease pair (see below), so the connection remains a model-level inference rather than a validated finding.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.42%), the malignant hypertensive renal disease prediction has no supporting clinical trials or literature (Evidence Level L5, Decision Stage S0) and the drug is not currently marketed in Singapore, so there is no basis to advance this specific candidate at this time.

**To proceed, the following is needed:**
- Disease-specific clinical or preclinical evidence for Nebivolol in malignant hypertensive renal disease
- Structured MOA data (DrugBank API query, currently a Blocking data gap per meta.data_gaps)
- TFDA/local package insert warnings and contraindications (currently a Blocking data gap)
- Singapore regulatory/registration pathway assessment, since the drug is not presently marketed locally

**Note:** Within the same evidence pack, two lower-ranked candidates have materially stronger evidence and may warrant separate evaluation: *chronic pulmonary heart disease* (rank 6, L2, "Proceed with Guardrails," 4 clinical trials including 2 completed Phase 4 trials directly testing Nebivolol, 18 publications) and *Prinzmetal angina* (rank 7, L2, "Proceed with Guardrails," a completed Phase 4 trial directly testing Nebivolol in coronary arterial spasm). These may be more actionable near-term repurposing candidates than the top-ranked prediction covered in this report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

