---
layout: default
title: Zolbetuximab
parent: 僅模型預測 (L5)
nav_order: 1077
evidence_level: L5
indication_count: 10
---

# Zolbetuximab
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

Using no specialized skill here — this is a direct, fully-specified report-writing task; I'll produce the Markdown report per the v5 prompt spec.

# Zolbetuximab: From Gastric/GEJ Adenocarcinoma to Diabetic Cataract

## One-Sentence Summary

> Zolbetuximab is a monoclonal antibody targeting Claudin 18.2 (CLDN18.2), originally developed for CLDN18.2-positive gastric/gastroesophageal junction adenocarcinoma.
> The TxGNN model predicts it may be effective for **Diabetic Cataract**,
> but this direction is currently supported by **0 clinical trials** and **0 publications** — it is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | CLDN18.2-positive gastric/gastroesophageal junction adenocarcinoma (inferred from rationale text; not confirmed via a Singapore-licensed label) |
| Predicted New Indication | Diabetic Cataract |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on the drug's identity, zolbetuximab is understood to be a chimeric IgG1 monoclonal antibody that binds Claudin 18.2 on tumour cell surfaces and triggers antibody-dependent and complement-dependent cytotoxicity (ADCC/CDC); it is used for CLDN18.2-positive gastric and gastroesophageal junction adenocarcinoma.

The proposed link to diabetic cataract rests on the fact that Claudin-family proteins in general do participate in tight-junction formation in lens epithelial cells, which is biologically relevant to cataract pathophysiology. However, the evidence pack itself flags this connection as **highly speculative**: there is no established evidence that the specific CLDN18.2 subtype is expressed in lens or ocular tissue, and no direct literature supports this pathway. This appears to be an indirect association surfaced through shared "claudin family" knowledge-graph nodes rather than a validated biological mechanism.

Notably, the same rationale text raises a mechanistic concern for a related prediction (diabetic retinopathy, rank 10): because zolbetuximab's mode of action is cytotoxic (ADCC/CDC-mediated cell killing) rather than barrier-restorative, applying it to a tissue where the goal would be to *preserve* epithelial integrity could theoretically be counterproductive rather than therapeutic. This same caution reasonably extends to the cataract-related predictions.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Zolbetuximab currently holds no marketing authorization in Singapore (0 registrations). No license or approved-indication data is available to summarize.

## Cytotoxicity

Zolbetuximab is an antineoplastic monoclonal antibody (original indication involves adenocarcinoma; ADCC/CDC-mediated tumour cell killing), so cytotoxicity information is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-Claudin 18.2 monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model prediction (L5) with no supporting clinical trials or literature, no confirmed marketing status in Singapore, and a mechanistic rationale the evidence pack itself describes as highly speculative — including a plausible scenario where the drug's cytotoxic mechanism could work against, rather than for, the proposed indication. Ten of the top predictions for this drug are all cataract/retinopathy-related, at similarly weak evidence levels, suggesting a systematic knowledge-graph artifact around "claudin family ↔ ocular disease" rather than an independently validated signal.

**To proceed, the following is needed:**
- TFDA/regulatory label warnings and contraindications (blocking gap DG001) before any S1 safety review can begin
- Confirmed mechanism of action and original indication sourced directly from DrugBank API (gap DG002)
- Preclinical evidence establishing CLDN18.2 expression/function in lens or ocular tissue
- Any case-level or preclinical data addressing whether ADCC/CDC-mediated cytotoxicity is compatible with an ocular epithelial-preservation goal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

