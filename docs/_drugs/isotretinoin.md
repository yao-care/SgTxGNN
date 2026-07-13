---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 540
evidence_level: L5
indication_count: 10
---

# Isotretinoin
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

# Isotretinoin: From Severe Acne to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin (13-cis-retinoic acid) is a synthetic vitamin A analogue with well-established clinical use in the treatment of severe nodular/cystic acne.
The TxGNN model predicts it may have potential therapeutic relevance in **Malignant Renovascular Hypertension**, a life-threatening hypertensive emergency with severe renal vascular involvement.
However, **no clinical trials and no relevant publications** currently exist to support this specific repurposing direction — this prediction rests entirely on computational modelling.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Severe nodular/cystic acne (no Singapore registration data available) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Isotretinoin is a synthetic retinoid that modulates gene expression by binding to retinoic acid receptors (RAR-α, RAR-β) and retinoid X receptors (RXRs). Its best-established clinical role is in severe nodular acne, where it drastically reduces sebaceous gland activity, normalises follicular epithelial differentiation, and suppresses local inflammation. Once absorbed, 13-cis-retinoic acid undergoes partial isomerisation to all-trans retinoic acid (ATRA) in vivo, sharing mechanistic overlap with this more extensively studied compound. Detailed MOA data was not retrievable from DrugBank in the current evidence cycle and remains an outstanding data gap.

The mechanistic rationale for malignant renovascular hypertension centres on RAR-β signalling in renal vascular biology. Preclinical data show that ATRA can inhibit TGF-β–driven renal fibrosis, attenuate mesangial and vascular smooth muscle cell proliferation, and exert protective effects in hypertensive nephrosclerosis models. Malignant renovascular hypertension is pathologically defined by fibrinoid necrosis and hyperplastic arteriosclerosis of intrarenal vessels — processes theoretically amenable to RAR-mediated suppression of fibrogenic and proliferative pathways.

That said, this connection has never been tested in humans, and several cautions apply. The TxGNN rank-1 and rank-2 predictions (malignant renovascular hypertension and malignant hypertensive renal disease) share an identical score of 0.9901, suggesting these may represent overlapping or redundant disease nodes in the knowledge graph rather than two independently validated targets. The high score most likely reflects the structural topology of hypertension/vascular disease clusters within the graph rather than mechanism-specific signal. Until preclinical studies in relevant animal models are conducted, the prediction must be treated as hypothesis-generating only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Isotretinoin in malignant renovascular hypertension.

---

## Literature Evidence

Currently no related literature available for Isotretinoin in malignant renovascular hypertension.

---

## Singapore Market Information

Isotretinoin currently has no registered products in Singapore (0 licences on record). Singapore prescribers rely on unregistered product access pathways (e.g., Special Access Route) for current dermatological and oncological indications.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Package insert warnings and contraindications for Isotretinoin (including teratogenicity, psychiatric effects, and hepatotoxicity) were not retrieved in this evidence cycle. Obtaining and parsing the full prescribing information is classified as a **Blocking** data gap (DG001) and must be resolved before any Safety Stage 1 (S1) evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high at 99.01%, but this reflects computational modelling based on knowledge-graph topology rather than empirical evidence; no clinical trials and no publications exist linking Isotretinoin to malignant renovascular hypertension, placing this candidate squarely at L5 — the lowest evidence tier. With zero Singapore registrations and unresolved safety data gaps, this candidate cannot advance to formal evaluation at this stage.

**To proceed, the following is needed:**

- **Resolve safety data gap (Blocking):** Retrieve and parse Isotretinoin package insert (any jurisdiction) to extract teratogenicity risk, psychiatric warnings, hepatotoxicity/lipid monitoring requirements, and contraindications
- **Retrieve MOA data (High priority):** Query DrugBank API for DB00982 to confirm RAR subtype specificity, ATRA isomerisation ratio, and known pharmacological targets
- **Clarify knowledge-graph ambiguity:** Determine whether "malignant renovascular hypertension" (rank 1) and "malignant hypertensive renal disease" (rank 2) are distinct disease concepts in TxGNN or ontological duplicates — if duplicates, the effective prediction rank falls significantly
- **Commission targeted preclinical literature review:** Systematic search for ATRA/Isotretinoin in animal models of malignant hypertension, renovascular hypertension, or hypertensive nephrosclerosis
- **Note a more promising direction in the same evidence pack:** The rank-6 indication **Chronic Pulmonary Heart Disease** has a completed Phase 2 clinical trial (NCT00000621, FORTE study) evaluating retinoids in emphysema, and carries an L3 evidence level with a "Research Question" recommendation — this may warrant prioritisation over the rank-1 prediction for immediate follow-up

> *This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

