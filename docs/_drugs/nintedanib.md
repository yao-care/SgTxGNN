---
layout: default
title: Nintedanib
parent: 僅模型預測 (L5)
nav_order: 707
evidence_level: L5
indication_count: 10
---

# Nintedanib
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

# Nintedanib: From Idiopathic Pulmonary Fibrosis to Dermatofibrosarcoma Protuberans

## One-Sentence Summary

Nintedanib is a triple angiokinase inhibitor (VEGFR/FGFR/PDGFR) originally developed and approved internationally for idiopathic pulmonary fibrosis (IPF) and other progressive fibrosing interstitial lung diseases.
The TxGNN model predicts it may be effective for **Dermatofibrosarcoma Protuberans (DFSP)**, a PDGFR-β-driven skin sarcoma,
but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests on mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis / progressive fibrosing ILD (based on general drug knowledge; not present in the supplied evidence pack) |
| Predicted New Indication | Dermatofibrosarcoma protuberans |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack for Nintedanib. Based on known information, Nintedanib is a small-molecule tyrosine kinase inhibitor targeting VEGFR, FGFR, and PDGFR, and its efficacy in fibrosing lung disease has been established through this anti-fibrotic/anti-angiogenic activity.

DFSP is a dermal sarcoma driven in the majority of cases by the COL1A1-PDGFB fusion gene, which causes constitutive activation of PDGFR-β signaling. Since Nintedanib has documented PDGFR inhibitory activity, the mechanistic rationale parallels that of imatinib, a PDGFR inhibitor already approved for DFSP. This gives the prediction a plausible biological basis, even though it is not yet supported by any trial or literature evidence in this dataset.

It should be noted that this mechanistic link is inferred from Nintedanib's known kinase-inhibition profile rather than from confirmed MOA data specific to this evidence pack — the MOA field itself is flagged as a data gap (DG002, High severity) and should be verified against a primary source (e.g., DrugBank API) before further evaluation.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Nintedanib is currently not registered/marketed in Singapore (0 authorizations on file), so no local product information is available.

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: DG001 — TFDA/local label warnings and contraindications — is flagged as a Blocking data gap and must be resolved before this candidate can proceed to a safety initial assessment (S1).)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by TxGNN's model score and a plausible but unverified mechanistic argument (PDGFR-β inhibition), with zero clinical trials and zero publications identified (Evidence Level L5). No local regulatory or safety data exists for this drug, so no actionable next step beyond evidence-gathering is currently warranted.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA/local label warnings and contraindications
- Resolve DG002 (High): confirm Nintedanib's mechanism of action via DrugBank or another primary source
- Targeted literature/trial search specifically for Nintedanib in PDGFR-driven sarcomas (DFSP, fibrosarcoma) to move beyond pure mechanistic inference
- Preclinical or case-level evidence before this candidate can be reconsidered for a higher decision stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

