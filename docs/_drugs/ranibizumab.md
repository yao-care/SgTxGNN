---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 843
evidence_level: L5
indication_count: 10
---

# Ranibizumab
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

# Ranibizumab: From Neovascular Age-Related Macular Degeneration to Severe Nonproliferative Diabetic Retinopathy

## One-Sentence Summary

Ranibizumab is an anti-VEGF monoclonal antibody fragment, best known for treating neovascular (wet) age-related macular degeneration and related retinal vascular disorders. The TxGNN model predicts it may be effective for **severe nonproliferative diabetic retinopathy (NPDR)**, with **6 clinical trials** (including multiple completed Phase 3 RCTs) and **19 publications** currently supporting this direction — this is one of the strongest-evidenced candidates in this batch, ranking well ahead of several lower-confidence cataract-related predictions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Neovascular (wet) age-related macular degeneration and related retinal vascular disease *(based on general drug knowledge — not present in the Singapore regulatory data provided)* |
| Predicted New Indication | Severe Nonproliferative Diabetic Retinopathy |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action data is currently a data gap (DG002). However, the evidence pack's repurposing rationale confirms that ranibizumab is a recombinant humanized monoclonal antibody Fab fragment that binds and neutralizes VEGF-A. Intravitreal injection suppresses retinal neovascularization and vascular permeability — the core pathological drivers of VEGF-mediated retinal disease.

Diabetic retinopathy and age-related macular degeneration share the same downstream pathophysiology: chronic retinal ischemia upregulates VEGF, which drives both neovascularization and vascular leakage. Severe NPDR represents a pre-proliferative, high-risk stage where VEGF is already elevated, making anti-VEGF suppression mechanistically well-matched even before frank proliferative disease develops.

This is not a purely speculative prediction — the evidence pack notes that anti-VEGF agents including ranibizumab already carry regulatory approval for diabetic retinopathy/diabetic macular edema in multiple jurisdictions (including the US), and pivotal trials such as DRCR.net Protocol I and the PANORAMA trial (NCT02634333) directly demonstrate that ranibizumab reduces progression to vision-threatening complications in high-risk NPDR. The recently reported Pavilion trial (2025) further supports sustained anti-VEGF delivery specifically in NPDR without macular edema.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | Completed | 691 | DRCR Protocol I: intravitreal ranibizumab ± laser superior to laser alone for diabetic macular edema and DR progression |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | Completed | 399 | PANORAMA trial: anti-VEGF therapy reduces risk of vision-threatening complications in high-risk NPDR |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | Completed | 25 | Intravitreal ranibizumab reduced microaneurysm turnover and non-perfused retinal area in NPDR with DME |
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | Active, not recruiting | 174 | Port Delivery System with ranibizumab (PDS) evaluated vs comparator arm in DR without center-involved DME |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | Unknown | 118 | Intravitreous ranibizumab vs sham injection for prevention of progression in high-risk DR |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | Unknown | 1000 | Real-world observational study of anti-VEGF therapy across AMD/PDR/DME/CNV; low DR-specificity (Grade C relevance) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion trial: Port Delivery System with ranibizumab vs monitoring reduces progression risk in NPDR without macular edema |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | Systematic Review/Meta-analysis | Health Technol Assess | Anti-VEGF vs laser photocoagulation for DR: systematic review and economic analysis |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | Systematic Review/Meta-analysis | Health Technol Assess | Anti-VEGF vs laser photocoagulation for DR: systematic review and meta-analysis |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | Meta-analysis (Phase III trials) | Ophthalmology Retina | Baseline DR severity affects time to DME resolution with ranibizumab |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | RCT (post-hoc) | Ophthalmic Surg Lasers Imaging Retina | RIDE/RISE post-hoc analysis characterizing DR progression in untreated fellow eyes |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT (post-hoc) | Clin Ophthalmol | RIDE/RISE post-hoc: predictors of early DR regression with ranibizumab |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT (post-hoc) | Retina | DRCR.net Protocol I 5-year report: DR severity changes with ranibizumab for DME |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT (secondary analysis) | JAMA Ophthalmology | 2-year DR change comparing aflibercept, bevacizumab, and ranibizumab |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Ranibizumab's role in revolutionizing anti-VEGF treatment of DR |
| [31669065](https://pubmed.ncbi.nlm.nih.gov/31669065/) | 2019 | Review | J Diabetes Complications | Advances in DR treatment; VEGF-A upregulation identified as key pathological driver |

---

## Singapore Market Information

Ranibizumab currently has **no marketing authorization registered in Singapore** (0 licenses recorded). This is an important gating factor — before any repurposing pathway can proceed locally, a fresh registration or import route would need to be established.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug-interaction data for ranibizumab are not currently available in this evidence pack (flagged as a blocking data gap — DG001: TFDA/HSA label warnings and contraindications not yet retrieved).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The severe NPDR prediction is backed by L1-level evidence — multiple completed Phase 3 RCTs (DRCR Protocol I, PANORAMA/NCT02634333) plus a 2025 RCT (Pavilion) and two recent systematic reviews/HTA analyses — and is mechanistically coherent with ranibizumab's established anti-VEGF activity. However, the drug is not currently marketed in Singapore and safety/label data remain an unresolved blocking gap, so guardrails are required before any local development decision.

**To proceed, the following is needed:**
- Retrieve TFDA/HSA-equivalent package insert warnings and contraindications (DG001, blocking)
- Confirm formal MOA documentation via DrugBank API (DG002)
- Establish Singapore registration/import pathway, since 0 local licenses currently exist
- Confirm drug-drug interaction profile (DDI query currently returned no results)

*Note: Lower-ranked candidates in this evidence pack (ranks 2–10, mostly cataract-related indications) were evaluated but show weak or contradictory mechanistic support (evidence levels L4–L5, largely "Hold") and are not recommended for further action at this time.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

