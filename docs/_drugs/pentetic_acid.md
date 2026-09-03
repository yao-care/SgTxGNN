---
layout: default
title: Pentetic Acid
parent: 僅模型預測 (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
---

# Pentetic Acid
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

# Pentetic Acid (DTPA): From Radionuclide/Heavy Metal Decorporation to Thrombocytopenic Purpura

## One-Sentence Summary

Pentetic acid (DTPA, DrugBank DB14007) is a metal-chelating agent used clinically for radionuclide/heavy-metal decorporation and as a chelating scaffold in diagnostic contrast agents. The TxGNN model predicts it may be effective for **Thrombocytopenic Purpura**, but this direction is currently supported by only **1 clinical trial** (of doubtful relevance) and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; no approved indication text on file (drug not marketed, original indication data unavailable) |
| Predicted New Indication | Thrombocytopenic Purpura |
| TxGNN Prediction Score | 97.25% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on the evidence pack's own repurposing rationale, pentetic acid (DTPA) is a metal chelator used clinically for radionuclide/heavy-metal body decontamination and as the chelating backbone of imaging contrast agents (e.g., Gd-DTPA, 99mTc-DTPA). No established pharmacological link exists between this chelation-based mechanism and the immune/hematologic pathways that drive thrombocytopenic purpura.

The evidence pack explicitly flags this gap: the TxGNN score is high, but "缺乏機轉支持" (mechanistic support is lacking). The only associated clinical trial (NCT03784898) is not a treatment study of pentetic acid in ITP — it is a blood-sample collection study in multiple sclerosis patients who developed immune thrombocytopenic purpura *after* treatment with a different drug (LEMTRADA/alemtuzumab), and is graded relevance "C" (unrelated). There is no supporting literature for this indication.

Given the absence of a plausible mechanistic bridge and the absence of directly relevant clinical or literature evidence, this prediction should be treated as a model-driven signal only, not a substantiated repurposing hypothesis at this stage.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03784898](https://clinicaltrials.gov/study/NCT03784898) | Phase 4 | Completed | 13 | Blood-sample collection in relapsing MS patients who developed ITP after LEMTRADA (alemtuzumab) treatment, for future DNA/SNP biomarker analysis. Not a pentetic acid treatment study; relevance graded "C" (unrelated to pentetic acid or ITP treatment). |

## Literature Evidence

Currently no related literature available

## Singapore Market Information

Not currently registered or marketed in Singapore (0 authorizations on file).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (97.25%), there is no direct mechanistic, clinical, or literature evidence linking pentetic acid's chelation activity to thrombocytopenic purpura — the single associated trial is unrelated to pentetic acid treatment, and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (currently a Blocking data gap; required before any safety pre-screening)
- Verified mechanism of action data from DrugBank (currently a High-severity data gap)
- Preclinical or mechanistic evidence directly connecting DTPA chelation to platelet/immune pathways relevant to ITP
- Drug-drug interaction data (current DDI query returned no results)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

