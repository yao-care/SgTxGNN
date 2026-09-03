---
layout: default
title: Ramucirumab
parent: 僅模型預測 (L5)
nav_order: 842
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: From Anti-Angiogenic Oncology Therapy to Uterine Ligament Adenocarcinoma

## One-Sentence Summary

> Ramucirumab is a VEGFR2-targeting anti-angiogenic monoclonal antibody used in oncology; no confirmed original indication is recorded in the current dataset because the drug is not yet registered in Singapore.
> The TxGNN model predicts potential efficacy for **Uterine Ligament Adenocarcinoma** (top of 10 rare gynecological adenocarcinoma subtypes flagged in this batch),
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — it rests entirely on mechanistic class-effect reasoning.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (drug not registered in Singapore; no license/indication text on file) |
| Predicted New Indication | Uterine Ligament Adenocarcinoma |
| TxGNN Prediction Score | 99.95% (rank 1176 of model output) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Ramucirumab is not available in structured form (`original_moa` = Data Gap). Based on the repurposing rationale evidence provided, Ramucirumab is described as a **VEGFR2 antagonist** — an anti-angiogenic monoclonal antibody that blocks vascular endothelial growth factor receptor 2 signalling.

The mechanistic link to this prediction is a **class-effect argument**: bevacizumab, an anti-VEGF-A antibody with an overlapping anti-angiogenic mechanism, has demonstrated efficacy in metastatic cervical cancer (GOG-240 trial). Since uterine ligament adenocarcinoma and the other candidates listed below are gynecological adenocarcinoma subtypes anatomically and histologically related to cervical/endometrial cancer, the model infers a theoretical basis for VEGFR2 blockade being active in this tissue context. One rationale entry also notes Ramucirumab has approved use in metastatic colorectal cancer, and intestinal-variant cervical mucinous adenocarcinoma shares histological features with colorectal mucinous adenocarcinoma — offering an additional, indirect cross-tumour analogy.

However, **none of these links are subtype-specific**: uterine ligament adenocarcinoma is an extremely rare anatomic site, and there is no direct molecular pathology, preclinical, or clinical evidence that VEGFR2 is a driver in this specific subtype. This prediction should be read as hypothesis-generating only.

---

## Other Predicted Indications (Rank 2–10)

This candidate batch (`TW-DB05578-multi`) flagged 10 related gynecological adenocarcinoma subtypes, all at TxGNN scores >99.9% and all classified L5 / Hold:

| Rank | Disease | Score | Rationale Summary |
|------|---------|-------|---------|
| 2 | Endocervical carcinoma | 99.95% | Same VEGFR2 class-effect argument (bevacizumab precedent); no drug-specific evidence |
| 3 | Adenoid cystic carcinoma of the cervix uteri | 99.95% | Angiogenesis-dependence undefined for this rare histotype |
| 4 | Uterine ligament serous adenocarcinoma | 99.94% | Serous histology often angiogenesis-active, but no site-specific data |
| 5 | Signet ring cell variant cervical mucinous adenocarcinoma | 99.94% | No angiogenesis-specific literature for this rare variant |
| 6 | Cervical adenosquamous carcinoma, glassy cell variant | 99.94% | Aggressive histotype; no VEGFR2 expression/response data |
| 7 | Uterine ligament endometrioid adenocarcinoma | 99.94% | Indirect analogy to endometrial cancer anti-angiogenic studies |
| 8 | Uterine ligament clear cell adenocarcinoma | 99.94% | Weak analogy to ovarian/endometrial clear cell angiogenesis markers |
| 9 | Uterine ligament mucinous adenocarcinoma | 99.94% | General cross-tumour theoretical extension only |
| 10 | Intestinal variant cervical mucinous adenocarcinoma | 99.94% | Histological analogy to CRC (an approved Ramucirumab indication) |

All 10 candidates share the same limitation: extremely rare anatomic subtypes with no drug-specific clinical or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Ramucirumab currently has **0 authorizations** on file and is **not marketed** in Singapore. No license records are available to summarize.

---

## Cytotoxicity

Ramucirumab is an antineoplastic agent (anti-angiogenic monoclonal antibody targeting VEGFR2), so this section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (anti-angiogenic monoclonal antibody, VEGFR2 antagonist) — not conventional cytotoxic chemotherapy |
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
All 10 predicted indications in this batch are supported only by TxGNN model scores (L5) with zero clinical trials and zero literature evidence; the mechanistic link relies on cross-drug class-effect reasoning (bevacizumab precedent) rather than direct data on Ramucirumab in these subtypes. The drug is also not currently registered in Singapore, and core safety/MOA data are flagged as blocking gaps (DG001, DG002).

**To proceed, the following is needed:**
- HSA/package insert data: key warnings, contraindications, and drug-drug interactions (currently blocking — DG001)
- Confirmed mechanism of action and original approved indication(s) from DrugBank (DG002)
- Preclinical or case-level evidence of VEGFR2 expression/angiogenesis-dependence in uterine ligament adenocarcinoma and related rare subtypes
- Any real-world or case-report data on anti-VEGFR2 therapy in these specific rare gynecological histotypes before advancing beyond S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

