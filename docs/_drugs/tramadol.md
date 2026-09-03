---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 999
evidence_level: L5
indication_count: 10
---

# Tramadol
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

# Tramadol: From Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

> Tramadol is an opioid/SNRI analgesic used for pain management.
> The TxGNN model assigns a very high score to **Acromesomelic Dysplasia, Hunter-Thompson Type**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** —
> the model's own rationale flags this as a likely graph-proximity artefact rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pain management (opioid/SNRI analgesic) — no Singapore registration record available |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data for tramadol is not available in this evidence pack. Based on general pharmacological knowledge, tramadol is a centrally-acting opioid (weak μ-opioid receptor agonist) combined with serotonin-norepinephrine reuptake inhibition (SNRI), and its efficacy in moderate-to-moderately-severe pain is well established.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare genetic skeletal dysplasia (associated with *GDF5* mutations) causing severe limb shortening and joint abnormalities. There is **no disease-modifying mechanistic link** between tramadol and this condition — at most, tramadol could offer symptomatic relief for chronic musculoskeletal pain that may accompany the disorder, not treatment of the underlying skeletal defect.

Notably, the model-generated rationale for this candidate explicitly states that the high TxGNN score likely arises from **knowledge-graph node proximity bias** (tramadol clustering near "skeletal/pain" nodes) rather than a specific, biologically meaningful association. This same pattern of "high score, no mechanistic specificity" repeats across the top 6 ranked candidates in this pack (all rare skeletal/connective-tissue dysplasias), suggesting a systematic bias rather than independent repurposing signals. The only candidate with any literature support is rank 7 (juvenile idiopathic arthritis, L4), and even there the cited publications do not study tramadol directly.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tramadol is currently **not marketed** in Singapore per this evidence pack (`market_status: 未上市`, 0 registrations). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: This evidence pack has flagged the absence of TFDA/HSA label warnings and contraindications as a **Blocking** data gap — see Conclusion below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no supporting clinical trials or literature, no established mechanistic link to the target disease, and the model's own rationale attributes the high score to a likely knowledge-graph bias artefact rather than a genuine repurposing signal. Combined with the absence of MOA data and the drug's unmarketed status in Singapore, there is insufficient basis to advance beyond S0.

**To proceed, the following is needed:**
- Tramadol's confirmed mechanism of action (query DrugBank API — DG002)
- TFDA/HSA label warnings and contraindications, required before any S1 safety screening (DG001, Blocking)
- Disease-specific evidence (preclinical or case-level) linking tramadol to acromesomelic dysplasia or related skeletal dysplasias, beyond generic analgesic use
- Reassessment of whether rank 1–6 candidates (all rare skeletal dysplasias with identical "no mechanistic link" rationale) represent a systematic KG bias that should be filtered before further evaluation
- If pursuing rank 7 (juvenile idiopathic arthritis, L4) instead, tramadol-specific pediatric pain-management literature, since current citations do not study tramadol directly
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

