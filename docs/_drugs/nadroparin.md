---
layout: default
title: Nadroparin
parent: 僅模型預測 (L5)
nav_order: 686
evidence_level: L5
indication_count: 10
---

# Nadroparin
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

# Nadroparin: From Anticoagulant Therapy to Ten Candidate Indications — A Signal Triage Report

## One-Sentence Summary

> Nadroparin is a low molecular weight heparin (LMWH) whose established pharmacology is anticoagulation via antithrombin-mediated inhibition of Factor Xa/IIa (per literature retrieved in this pack; DrugBank original-indication data itself is a Data Gap). TxGNN surfaced **10 candidate indications**, but triage shows the **highest-scoring** candidates (platelet-secretion and bleeding disorders) are **mechanistically contraindicated false positives**, while the only two candidates with real clinical evidence — **thrombophilia** and **pulmonary embolism** — are essentially confirmations of nadroparin's existing anticoagulant use rather than genuinely novel repurposing. **No candidate in this batch qualifies as a validated, novel new indication.**

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — `original_indications` is empty and `original_moa` is a Data Gap in this pack |
| Top-Ranked TxGNN Prediction | Primary release disorder of platelets (rank 1 by score) |
| TxGNN Prediction Score (rank 1) | 98.15% |
| Evidence Level (rank 1) | L5 (model prediction only, no studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision (rank 1) | **Hold** — flagged as mechanistically contraindicated |

**Important caveat:** The template's rank-1 candidate is *not* a usable headline recommendation — its own rationale states nadroparin's anticoagulant effect would likely *worsen* this bleeding disorder, and TxGNN's high score is attributed to knowledge-graph proximity noise. The table below shows the full portfolio so the two evidence-backed candidates aren't hidden behind this artifact.

### Candidate Portfolio (all 10 predictions)

| Rank | Disease | Score | Evidence Level | Stage | Recommendation | Note |
|------|---------|-------|------|-------|------|------|
| 1 | Primary release disorder of platelets | 98.15% | L5 | S0 | Hold | Bleeding disorder — mechanistically opposite to anticoagulation |
| 2 | Glanzmann thrombasthenia | 98.14% | L5 | S0 | Hold | Bleeding disorder — same conflict |
| 3 | Pseudo-von Willebrand disease | 97.56% | L5 | S0 | Hold | Bleeding disorder — same conflict |
| 4 | Thrombophilia | 97.28% | L1 | S3 | Proceed with Guardrails | Real trials/literature, but existing anticoagulant use, not novel |
| 5 | Antithrombin deficiency type 2 | 97.16% | L5 | S1 | Research Question | Plausible but AT-dependent mechanism may blunt efficacy; no evidence |
| 6 | Factor 5 excess with spontaneous thrombosis | 97.03% | L5 | S1 | Research Question | Plausible, zero evidence |
| 7 | Heparin cofactor 2 deficiency | 96.99% | L5 | S1 | Research Question | Plausible, zero evidence |
| 8 | Pulmonary embolism | 96.98% | L1 | S3 | Proceed with Guardrails | Strong evidence, but core existing indication, not novel |
| 9 | Amenorrhea | 96.54% | L5 | S0 | Hold | No plausible mechanistic link; likely graph noise |
| 10 | Hemoglobinopathy | 96.04% | L4 | S1 | Research Question | 1 case report only (thalassemia stroke risk) |

---

## Why Is This Prediction Reasonable?

Detailed mechanism-of-action data for nadroparin is not available in this evidence pack (Data Gap DG002). Based on literature retrieved as supporting evidence for rank 4/8 (PMID 9108990, 31030749), nadroparin is a low molecular weight heparin that activates antithrombin to inhibit Factor Xa (and to a lesser extent Factor IIa/thrombin), the standard mechanism for preventing and treating venous thromboembolism.

This single mechanism explains the entire shape of the TxGNN output: candidates cluster into two opposing groups. The **first group** (ranks 1, 2, 3, 9) consists of hemorrhagic/platelet-function disorders where impaired clotting is the pathology — anticoagulation would plausibly *worsen* these conditions, making them mechanistically contraindicated rather than promising. The **second group** (ranks 4–8, 10) consists of hypercoagulable/prothrombotic states, where nadroparin's known anti-Xa activity is directly on-mechanism.

Within the second group, however, thrombophilia and pulmonary embolism are not truly "new" indications — LMWH is already standard-of-care thromboprophylaxis/treatment for both. The genuinely novel sub-mechanisms (antithrombin deficiency type 2, heparin cofactor II deficiency, Factor V–related thrombosis, hemoglobinopathy-associated hypercoagulability) are plausible extensions but carry no clinical trial or substantive literature support in this pack.

---

## Clinical Trial Evidence

### Thrombophilia (Rank 4, L1/S3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01019655](https://clinicaltrials.gov/study/NCT01019655) | Phase 3 | Unknown | 300 | LMWH efficacy in pregnant women with thrombophilia — direct disease match |
| [NCT04373707](https://clinicaltrials.gov/study/NCT04373707) | Phase 4 | Completed | 1000 | Weight-adjusted prophylactic LMWH dosing vs. fixed dose to prevent VTE in COVID-19 |
| [NCT06494878](https://clinicaltrials.gov/study/NCT06494878) | Phase 3 | Not yet recruiting | 8805 | Postpartum aspirin vs. LMWH for VTE prevention |
| [NCT02987946](https://clinicaltrials.gov/study/NCT02987946) | N/A | Completed | 280 | Anticoagulation optimization in neurosurgical patients at VTE risk |
| [NCT03005444](https://clinicaltrials.gov/study/NCT03005444) | N/A | Unknown | 254 | Anticoagulation in decompensated cirrhosis (hypercoagulable state) |

### Pulmonary Embolism (Rank 8, L1/S3)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00796692](https://clinicaltrials.gov/study/NCT00796692) | Phase 4 | Completed | 274 | Nadroparin vs. unfractionated heparin, initial PE treatment — direct drug/disease match |
| [NCT00951574](https://clinicaltrials.gov/study/NCT00951574) | Phase 3 | Completed | 1166 | Nadroparin for VTE prevention in chemotherapy patients (placebo-controlled) |
| [NCT01828697](https://clinicaltrials.gov/study/NCT01828697) | Phase 4 | Completed | 1110 | Two LMWH dose regimens for recurrent VTE prevention in pregnancy |
| [NCT04373707](https://clinicaltrials.gov/study/NCT04373707) | Phase 4 | Completed | 1000 | Weight-adjusted LMWH prophylaxis in COVID-19 |
| [NCT04536272](https://clinicaltrials.gov/study/NCT04536272) | Phase 3 | Completed | 330 | Reduced anticoagulation targets during ECLS |
| [NCT00843492](https://clinicaltrials.gov/study/NCT00843492) | Phase 3 | Completed | 1351 | Fondaparinux vs. nadroparin for VTE prevention in leg immobilization |
| [NCT01431456](https://clinicaltrials.gov/study/NCT01431456) | Phase 3 | Completed | 148 | Dabigatran/rivaroxaban vs. nadroparin after knee arthroplasty |
| [NCT01542723](https://clinicaltrials.gov/study/NCT01542723) | N/A | Completed | 1500 | Thromboprophylaxis after knee arthroscopy |
| [NCT01727427](https://clinicaltrials.gov/study/NCT01727427) | N/A | Completed | 695 | Treatment of unsuspected PE in cancer patients |
| [NCT00312013](https://clinicaltrials.gov/study/NCT00312013) | Phase 3 | Completed | 503 | Nadroparin effect on survival/progression in advanced lung, pancreatic, prostate cancer |

**All other candidates (ranks 1, 2, 3, 5, 6, 7, 9, 10): Currently no related clinical trials registered.**

---

## Literature Evidence

### Thrombophilia (Rank 4)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38233773](https://pubmed.ncbi.nlm.nih.gov/38233773/) | 2024 | RCT | BMC Pregnancy and Childbirth | Meta-analysis: LMWH for preeclampsia prevention in high-risk pregnancy without thrombophilia |
| [20229677](https://pubmed.ncbi.nlm.nih.gov/20229677/) | 2010 | RCT | Srpski arhiv za celokupno lekarstvo | Nadroparin vs. unfractionated heparin for VTE in pregnancy/puerperium |
| [24995856](https://pubmed.ncbi.nlm.nih.gov/24995856/) | 2014 | RCT (Cochrane) | Cochrane Database Syst Rev | Aspirin and/or heparin for recurrent miscarriage with/without inherited thrombophilia |
| [28478442](https://pubmed.ncbi.nlm.nih.gov/28478442/) | 2017 | Cohort | Acta Haematologica | LMWH prophylaxis and hypercoagulable changes in thrombophilic pregnancy |
| [23262970](https://pubmed.ncbi.nlm.nih.gov/23262970/) | 2014 | Review | Clin Appl Thromb Hemost | Nadroparin outcomes across thrombophilia mutation subtypes |
| [30660948](https://pubmed.ncbi.nlm.nih.gov/30660948/) | 2019 | Review | Thrombosis Research | Anti-Xa monitoring of heparins in antithrombin-deficient patients |

### Pulmonary Embolism (Rank 8)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9108990](https://pubmed.ncbi.nlm.nih.gov/9108990/) | 1997 | Review | Drugs & Aging | Foundational review of nadroparin pharmacology and clinical use in thromboembolic disease |
| [31030749](https://pubmed.ncbi.nlm.nih.gov/31030749/) | 2019 | Review | Prog Mol Biol Transl Sci | Overview of all approved LMWHs including nadroparin |
| [32639644](https://pubmed.ncbi.nlm.nih.gov/32639644/) | 2020 | Retrospective cohort | J Clin Pharmacol | LMWH/fondaparinux effects on liver function in PE patients |
| [20015933](https://pubmed.ncbi.nlm.nih.gov/20015933/) | 2011 | Cohort | J Oncol Pharm Pract | Low-dose nadroparin in PE with brain metastases (2 cases) |
| [12037712](https://pubmed.ncbi.nlm.nih.gov/12037712/) | 2002 | Cohort | Spinal Cord | Primary VTE/PE prevention in acute spinal cord injury |
| [18388030](https://pubmed.ncbi.nlm.nih.gov/18388030/) | 2008 | Retrospective | Angiology | DVT patients and progression to PE |

### Hemoglobinopathy (Rank 10)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20063543](https://pubmed.ncbi.nlm.nih.gov/20063543/) | 2008 | Case Report | Hematol Oncol Stem Cell Ther | Recurrent cerebral stroke in a thalassemic patient — sole evidence for this candidate |

**Remaining candidates (ranks 1, 2, 3, 5, 6, 7, 9): Currently no related literature available.**

---

## Singapore Market Information

No Singapore registration records are available for nadroparin. `taiwan_regulatory.licenses` is empty and `market_status` is **Not Marketed** with **0** total registrations.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and DDI data are all unavailable in this pack — DG001 flags TFDA label warnings as a **Blocking** gap that must be resolved before any safety evaluation can proceed.)

---

## Conclusion and Next Steps

**Decision: Hold** (as a repurposing opportunity for a genuinely new indication)

**Rationale:**
- The highest-TxGNN-score candidates (ranks 1, 2, 3, 9) are mechanistically contraindicated bleeding disorders and should be excluded outright, not advanced.
- The two candidates with real clinical evidence (thrombophilia, pulmonary embolism, both L1/S3) are not novel — they fall within nadroparin's known anticoagulant use — so they don't represent a repurposing "win," only confirmation of existing pharmacology.
- The remaining candidates (antithrombin deficiency type 2, Factor V excess, heparin cofactor II deficiency, hemoglobinopathy) are mechanistically plausible but have essentially no clinical evidence (L4–L5, S1) to support advancing them.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001, Blocking) — required before any S1 safety screening
- Confirmed mechanism-of-action data from DrugBank (DG002, High)
- If pursuing the antithrombin/heparin-cofactor-II/Factor V subtype candidates as genuine research questions: dedicated preclinical or observational studies, since none currently exist
- Re-run TxGNN signal triage with explicit exclusion rules for known contraindicated mechanism classes (bleeding disorders) to reduce false-positive burden in future batches
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

