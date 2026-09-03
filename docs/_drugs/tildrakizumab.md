---
layout: default
title: Tildrakizumab
parent: 僅模型預測 (L5)
nav_order: 981
evidence_level: L5
indication_count: 10
---

# Tildrakizumab
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

# Tildrakizumab: From Plaque Psoriasis to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Tildrakizumab is an anti-IL-23p19 monoclonal antibody originally approved for plaque psoriasis.
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — and the evidence pack itself flags it as a likely model artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Plaque psoriasis (based on known drug mechanism data; not derived from a Singapore license, as none exists) |
| Predicted New Indication | Severe nonproliferative diabetic retinopathy |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed regulatory-grade mechanism of action (MOA) documentation is not available for this drug. Based on the information present in the evidence pack, tildrakizumab is an anti-IL-23p19 monoclonal antibody that works by inhibiting Th17 pathway activation, and its approved use is for plaque psoriasis.

There is no known biological link between the IL-23/Th17 axis and the pathophysiology of diabetic retinopathy, which is driven by chronic hyperglycemia-induced microvascular damage and VEGF-mediated neovascularization. The same applies to the other diabetes-related conditions in this candidate set (cataract subtypes, drug-induced osteoporosis) — none share a plausible mechanistic pathway with IL-23 inhibition.

Notably, all 10 ranked predictions for this drug cluster tightly around diabetes-associated eye and bone conditions with near-identical, closely-spaced scores (0.986–0.996). This pattern — rather than reflecting 10 independent biological signals — is more consistent with a knowledge-graph embedding artifact, where tildrakizumab's node sits near a cluster of diabetes-comorbidity or psoriasis-comorbidity drug nodes. **The evidence pack's own mechanistic analysis for every one of the top 10 predictions concludes there is no credible biological rationale**, and no clinical trial or literature evidence exists for any of them.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(This applies to all 10 ranked predicted indications, not just the top one.)*

---

## Literature Evidence

Currently no related literature available.

*(This applies to all 10 ranked predicted indications, not just the top one.)*

---

## Singapore Market Information

Tildrakizumab currently has no market authorization in Singapore (0 registrations). No licensing or approved-indication data is available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack; TFDA/HSA label information is flagged as a blocking data gap — see below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the 10 TxGNN-predicted indications for this drug have any clinical trial or literature support, and the evidence pack's own rationale explicitly identifies these as likely embedding-clustering artifacts rather than genuine mechanistic signals. Combined with the absence of MOA and safety/label data, there is no basis to advance any of these candidates beyond S0.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert (warnings, contraindications) — currently a **blocking** gap
- Confirmed drug MOA from DrugBank or primary literature
- Independent biological or clinical evidence (in vitro, preclinical, or trial data) specifically linking IL-23 inhibition to diabetic microvascular or lens pathology, before any of these candidates should be re-scored
- If no such evidence emerges, this candidate cluster should be deprioritized as a likely false-positive artifact rather than re-evaluated repeatedly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

