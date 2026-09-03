---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
---

# Sacituzumab Govitecan
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

# Sacituzumab Govitecan: From Breast Cancer to Drug-Induced Osteoporosis

## One-Sentence Summary

> Sacituzumab govitecan is a Trop-2-targeted antibody-drug conjugate (ADC) carrying the cytotoxic payload SN-38, known clinically for treating triple-negative and HR+/HER2- breast cancer.
> The TxGNN model's top prediction is **Drug-Induced Osteoporosis**, but this is supported by **0 clinical trials** and **0 publications** — the model's own rationale flags this as likely prediction noise rather than a genuine mechanistic signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in Singapore registration data (drug not marketed here). Known globally for triple-negative breast cancer and HR+/HER2- breast cancer (per model's mechanistic rationale) |
| Predicted New Indication | Drug-Induced Osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (flagged as a High-severity data gap). Based on the model's own annotations, sacituzumab govitecan is a Trop-2-targeted ADC whose cytotoxic warhead, SN-38 (a topoisomerase I inhibitor), is the active metabolite of irinotecan. It is used for cytotoxic killing of breast cancer cells, not for modulating bone metabolism.

There is no established or plausible mechanistic link between Trop-2/SN-38 pharmacology and osteoclast/osteoblast regulation. The model's own rationale explicitly states this high score likely reflects an indirect graph artifact — a shared "breast cancer → bone metastasis → osteoporosis" co-morbidity path in the knowledge graph — rather than a true pharmacological signal.

This pattern repeats across the other 9 top-ranked predictions for this drug (diabetic retinopathy, several forms of cataract), none of which have any mechanistic, preclinical, or clinical support. Given that sacituzumab govitecan carries significant systemic cytotoxicity (myelosuppression, diarrhea) via its SN-38 payload, repurposing toward chronic, non-life-threatening degenerative conditions (cataract, retinopathy) is also clinically implausible from a risk-benefit standpoint.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

This drug is not currently registered/marketed in Singapore (0 licenses on file).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Antibody-drug conjugate (ADC) delivering the cytotoxic payload SN-38 (topoisomerase I inhibitor) |
| Myelosuppression Risk | High (SN-38 is the active metabolite of irinotecan; class effect includes significant neutropenia) |
| Emetogenicity Classification | Moderate (SN-38-associated nausea and diarrhea are well-documented class effects) |
| Monitoring Items | CBC with differential, hepatic and renal function, GI symptoms (severe diarrhea) |
| Handling Protection | Standard cytotoxic drug handling precautions apply despite antibody-targeted delivery |

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/HSA label warnings and contraindications are currently unavailable (Blocking data gap DG001) — this must be resolved before any safety pre-screening (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (drug-induced osteoporosis) and all 9 other top candidates for this drug are L5 (model-prediction-only) with zero supporting clinical trials or literature, and the model's own mechanistic rationale identifies most as likely graph artifacts rather than genuine signals. Combined with a Blocking safety data gap (no TFDA/HSA label data available), this candidate cannot advance past initial screening.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — resolves Blocking gap DG001
- Confirmed mechanism of action data from DrugBank — resolves High-severity gap DG002
- Independent mechanistic or preclinical evidence linking Trop-2/SN-38 pharmacology to bone metabolism, specifically for the top-ranked indication
- Re-evaluation of whether this candidate's high TxGNN scores across unrelated disease clusters (bone, retina, lens) indicate a graph-embedding artifact requiring model-side review, rather than pursuing further evidence collection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

