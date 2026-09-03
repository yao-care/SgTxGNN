---
layout: default
title: Vedolizumab
parent: 僅模型預測 (L5)
nav_order: 1048
evidence_level: L5
indication_count: 10
---

# Vedolizumab
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

# Vedolizumab: From Inflammatory Bowel Disease to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

> Vedolizumab is a gut-selective α4β7 integrin inhibitor used internationally for inflammatory bowel disease (Crohn's disease and ulcerative colitis).
> The TxGNN model predicts it may be effective for **Severe Nonproliferative Diabetic Retinopathy**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications**, with no identifiable mechanistic pathway connecting the drug to this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not marketed in Singapore; internationally approved for inflammatory bowel disease (Crohn's disease / ulcerative colitis), per gut-selective α4β7 integrin inhibition described in supporting literature |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 94.51% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available directly from DrugBank in this evidence pack. However, literature contained elsewhere in this pack describes vedolizumab as a humanized monoclonal antibody that binds α4β7 integrin, blocking lymphocyte binding to MAdCAM-1 — a mechanism specific to gut lymphocyte trafficking, used to treat Crohn's disease and ulcerative colitis.

This gut-restricted mechanism has no established connection to the pathways implicated in diabetic retinopathy (chiefly VEGF-driven retinal microvascular damage and local inflammation). The evidence pack's own rationale annotation states explicitly: *"TxGNN assigned a high score (0.945) but no identifiable mechanistic link exists. α4β7 integrin blockade is gut-specific, with no known intersection with diabetic retinopathy's vascular/inflammatory pathways."*

In short, this candidate reflects a case where a high computational similarity score from TxGNN is **not** corroborated by biological plausibility or any real-world evidence. It should be treated as a hypothesis-generation signal only, not a repurposing lead ready for further evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Vedolizumab is not currently marketed in Singapore (market status: 未上市 / Not Marketed; total registrations: 0). No local authorization records exist to report.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: HSA/manufacturer label warnings, contraindications, and drug-interaction data were not retrievable at time of this report — see remediation items below.)*

---

## Additional Predicted Indications (Screened, Not Recommended)

This evidence pack scored the drug against 10 candidate indications. All received a **Hold** recommendation. Two are worth flagging specifically:

| Rank | Disease | TxGNN Score | Evidence Level | Note |
|------|---------|------------|-----------------|------|
| 2 | Dermatitis | 93.6% | L4 | **Evidence points opposite the hypothesis** — multiple case reports/series (PMID 39606602, 35199379, 35659138, 33208632, 30677821) describe vedolizumab **inducing** atopic, psoriasiform, granulomatous, and acneiform dermatitis as an adverse reaction, not treating it. This is a safety signal, not efficacy evidence. |
| 9 | Bronchitis | 91.0% | L4 | Supporting literature is a safety analysis of respiratory tract infection rates in vedolizumab trials (PMID 29788248), not a treatment-efficacy study. |

The remaining 7 candidates (severe nonproliferative diabetic retinopathy, neonatal dermatomyositis, acne keloid, acrodermatitis chronica atrophicans, familial hydroa vacciniforme, childhood ILD with connective tissue disease, amyopathic dermatomyositis, drug-induced osteoporosis) have **zero clinical trials and zero literature** support.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
None of the 10 TxGNN-predicted indications for vedolizumab in this evidence pack are supported by credible clinical or mechanistic evidence. The top-ranked candidate (diabetic retinopathy) has no trials, no literature, and no plausible mechanistic link. The candidate with the most literature (dermatitis) is actually a documented **adverse-effect signal**, not a treatment lead — pursuing it as a repurposing indication would be inappropriate.

**To proceed, the following is needed:**
- Retrieve TFDA/HSA package insert warnings and contraindications (currently a **Blocking** data gap preventing any S1 safety evaluation)
- Obtain confirmed mechanism-of-action data from DrugBank API (currently missing)
- If diabetic retinopathy is to be pursued further, generate a preclinical/mechanistic rationale (e.g., any α4β7 or MAdCAM-1 expression in retinal vasculature) before allocating further evaluation resources
- Treat the dermatitis signal as a pharmacovigilance flag for existing vedolizumab-treated IBD patients, not a repurposing opportunity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

