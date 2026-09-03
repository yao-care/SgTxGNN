---
layout: default
title: Tafluprost
parent: 僅模型預測 (L5)
nav_order: 940
evidence_level: L5
indication_count: 10
---

# Tafluprost
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

# Tafluprost: From Glaucoma to Primary Hereditary Glaucoma

## One-Sentence Summary

Tafluprost is a prostaglandin F2α analogue used to lower intraocular pressure. The TxGNN model's top prediction — **primary hereditary glaucoma** — is essentially a within-class extension of its known glaucoma indication, but this candidate currently has **zero clinical trials and zero literature entries** directly attached to it in the evidence pack. A secondary signal on **vascular disease** is supported by 2 trials and 10 publications, but that evidence is safety/mechanistic in nature, not therapeutic support for a new indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in registry data (drug is not marketed in Singapore) |
| Predicted New Indication | Primary hereditary glaucoma |
| TxGNN Prediction Score | 98.62% |
| Evidence Level | L4 (mechanism-only; no direct trials or literature attached to this candidate) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack (marked as a data gap). Based on known pharmacology, however, tafluprost is a selective **FP receptor (prostaglandin F2α) agonist** that lowers intraocular pressure primarily by increasing uveoscleral outflow — this is well established as the mechanism underlying the entire prostaglandin analogue drug class (same family as latanoprost, travoprost, bimatoprost), which is first-line therapy for open-angle glaucoma and ocular hypertension.

The predicted indication, "primary hereditary glaucoma," sits within the same disease family as tafluprost's established use in glaucoma/ocular hypertension. This is not a cross-mechanism repurposing hypothesis but rather a **subtype extension** — the model is essentially recognizing that a drug already used to treat glaucoma should also work on a genetically-defined glaucoma subtype, which is mechanistically expected rather than novel.

Despite this plausibility, the evidence pack shows **no clinical trials or literature specifically retrieved for this candidate** (trials_count = 0, literature_count = 0). The high TxGNN score reflects strong network-level similarity between "glaucoma" and "primary hereditary glaucoma" as disease nodes, not independent clinical validation for the hereditary subtype specifically.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Tafluprost has no registered licenses in Singapore (`total_licenses: 0`, `market_status: 未上市`). No product table is available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: `key_warnings`, `contraindications`, and DDI data are all flagged as data gaps or not found in the evidence pack — TFDA label warnings/contraindications are listed as a Blocking data gap that must be resolved before any S1 safety assessment can proceed.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate (primary hereditary glaucoma) is mechanistically plausible as a within-class extension of tafluprost's known glaucoma pharmacology, but it currently has no direct clinical trial or literature support — this is a model-score-only prediction (L4, not the L5 assigned score would suggest but effectively unsupported at the indication level). Separately, the "vascular disease" candidate (rank 9) has real evidence (2 trials, 10 publications), but that evidence documents tafluprost's **vascular side effects** (corneal vascular changes, hyperemia, systemic blood pressure elevation) — this is a safety signal, not efficacy support, and argues against rather than for repurposing toward vascular disease.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/original-market label warnings and contraindications) — currently Blocking for any safety review
- Resolve DG002 (confirmed MOA from DrugBank) to properly ground the mechanistic rationale
- Targeted literature/trial search specifically on "hereditary glaucoma" + prostaglandin analogues, since the current evidence pack returned none despite the high model score
- Given zero direct evidence for the top candidate, this should remain a research question (S0/S1) rather than move toward development planning
- If pursuing the vascular-disease signal, reframe as a pharmacovigilance/safety monitoring topic rather than a repurposing indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

