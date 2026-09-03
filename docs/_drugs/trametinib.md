---
layout: default
title: Trametinib
parent: 僅模型預測 (L5)
nav_order: 1000
evidence_level: L5
indication_count: 10
---

# Trametinib
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

# Trametinib: From BRAF-Mutant Melanoma to Choroideremia

## One-Sentence Summary

> Trametinib is a selective MEK1/2 inhibitor, used internationally in combination with dabrafenib for BRAF V600E/K-mutation-positive melanoma; it is not currently registered in Singapore.
> The TxGNN model's top-ranked prediction is **Choroideremia**, a rare inherited retinal degeneration.
> This specific prediction is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags it as a likely false-positive knowledge-graph association.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore (未上市); no local approved indication text available. Per clinical trial data in this evidence pack, trametinib is used with dabrafenib for BRAF V600E/K-mutation-positive melanoma |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for trametinib is flagged as a data gap in this evidence pack (DG002). Based on information available elsewhere in the dataset, trametinib is a selective allosteric inhibitor of MEK1/2, acting on the RAS-RAF-MEK-ERK (MAPK) signalling pathway. It is used clinically in combination with the BRAF inhibitor dabrafenib for BRAF V600E/K-mutation-positive melanoma, and this MAPK-blocking mechanism underlies most of the other candidate indications in this evidence pack (e.g., non-cutaneous, mucosal, acral, and nodular melanoma subtypes).

For the top-ranked prediction, **choroideremia**, this mechanistic logic does not hold. Choroideremia is caused by loss-of-function mutations in the *CHM* gene (Rab escort protein 1), which regulates intracellular vesicle trafficking in photoreceptor and retinal pigment epithelial cells — a pathway with no established connection to MAPK/MEK signalling. The evidence pack's own rationale explicitly states that this high TxGNN score is "極可能為知識圖譜偽陽性關聯" (very likely a knowledge-graph false positive), possibly arising from indirect connections through ophthalmology-related nodes rather than genuine pharmacological relevance.

By contrast, several lower-ranked candidates in this same evidence pack — particularly **malignant melanoma of the mucosa** (rank 6, L2, "Proceed with Guardrails") — are mechanistically consistent with trametinib's known MAPK-inhibiting activity and are backed by dedicated clinical trials and preclinical literature. These represent a more biologically plausible repurposing direction than the top-ranked choroideremia prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Trametinib currently has no registrations in Singapore (0 licenses; market status: 未上市 / Not Marketed). No local product, dosage form, or approved indication text is available.

---

## Cytotoxicity

Trametinib is an antineoplastic agent (MEK inhibitor used in BRAF-mutant melanoma per trial data in this evidence pack), so cytotoxicity information is included below.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (selective MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (choroideremia) has no supporting clinical trials or literature, and the evidence pack's own mechanistic analysis identifies it as a probable knowledge-graph false positive with no plausible link between MEK/MAPK inhibition and CHM-gene-related retinal degeneration.

**To proceed, the following is needed:**
- Independent mechanistic or preclinical validation of any trametinib–retinal pathway interaction, since none currently exists in the dataset
- TFDA/HSA package insert warnings and contraindications (currently a Blocking data gap, DG001) before any safety review can begin
- Confirmed mechanism of action data from DrugBank (currently a data gap, DG002)
- Singapore regulatory registration status, since trametinib is not currently marketed locally

**Note:** This same evidence pack contains a mechanistically stronger candidate — **malignant melanoma of the mucosa** (Evidence Level L2, "Proceed with Guardrails") — supported by a dedicated adjuvant trial (NCT04666272) and preclinical MAPK-pathway literature. If pursuing repurposing for trametinib, this indication warrants separate evaluation rather than the top-ranked choroideremia prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

