---
layout: default
title: Pertuzumab
parent: 僅模型預測 (L5)
nav_order: 773
evidence_level: L5
indication_count: 10
---

# Pertuzumab
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

# Pertuzumab: From HER2-Positive Breast Cancer to Progesterone-Receptor Positive Breast Cancer

## One-Sentence Summary

Pertuzumab (DrugBank DB06366) is an anti-HER2 monoclonal antibody used in combination regimens (with trastuzumab ± docetaxel) for HER2-positive breast cancer. The TxGNN model predicts a specific benefit in the **progesterone-receptor (PR) positive** subgroup of HER2+ breast cancer, with **10 clinical trials** (including 2 completed Phase 3 RCTs) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HER2-positive breast cancer (per trial/literature context; no formal indication text on file — see Data Gaps) |
| Predicted New Indication | Progesterone-Receptor Positive Breast Cancer |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack. Based on the information available, Pertuzumab is an anti-HER2 monoclonal antibody that inhibits HER2–HER3 heterodimerization, thereby blocking downstream proliferative signaling in HER2-overexpressing tumors.

PR (progesterone receptor) status is not an independent drug target — it is a hormone-receptor biomarker used to sub-classify HER2-positive breast cancer. The TxGNN prediction essentially identifies a **biomarker-defined subgroup confirmation** rather than a mechanistically novel indication: large prospective trial datasets already exist for HER2+/PR+ and HER2+/PR- populations treated with pertuzumab-containing regimens (e.g., PERTAIN, CLEOPATRA/APHINITY-type populations).

Notably, evidence for the closely related "PR-negative breast cancer" prediction (rank 3 in this pack, also L1) is explicitly annotated as representing Pertuzumab's **core existing indication population**, reinforcing that the PR-positive subgroup prediction is a reasonable extension along the same hormone-receptor axis rather than an unrelated disease area.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Double-blind RCT: QL1209 (pertuzumab biosimilar) vs. reference pertuzumab, both + trastuzumab + docetaxel, in HER2+/ER-PR-negative early/locally advanced breast cancer |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | Withdrawn | 0 | Single-arm neoadjuvant weekly paclitaxel response rate study in Nigerian women with breast cancer (no pertuzumab arm; withdrawn) |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | Terminated | 139 | DECRESCENDO: de-escalated adjuvant chemo in HER2+/ER-negative/node-negative early BC after pCR to neoadjuvant chemo + SC pertuzumab/trastuzumab FDC |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | Unknown | 7 | Neoadjuvant aromatase inhibitor + pertuzumab/trastuzumab (chemo-free) in HR+ (ER+/PR+) HER2+ localized breast cancer |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | Active, not recruiting | 128 | TBCRC 023: Lapatinib + trastuzumab ± endocrine therapy, 12 vs. 24 weeks, in HER2-overexpressing breast cancer |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: Atezolizumab vs. placebo added to neoadjuvant AC→paclitaxel + trastuzumab + pertuzumab in early HER2+ breast cancer |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | Active, not recruiting | 398 | BCD-178 (pertuzumab biosimilar) vs. Perjeta as neoadjuvant therapy in HER2+, ER/PR-negative breast cancer |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | Active, not recruiting | 164 | T-DM1 + pertuzumab in the preoperative setting; impact of HER2 heterogeneity on treatment response in early HER2+ BC |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | Completed | 417 | 4-arm neoadjuvant trial of Herceptin/docetaxel/pertuzumab combinations; pathological complete response rate in locally advanced/inflammatory/early HER2+ BC |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | Completed | 1151 | Retrospective multicenter study of HER2-low prevalence, characteristics, and outcomes in metastatic breast cancer patients previously classified HER2-negative |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II: endocrine therapy + trastuzumab/pertuzumab vs. de-escalated chemotherapy in HR+/HER2+ early breast cancer |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | RCT (DECRESCENDO) | Future Oncology | De-escalating chemotherapy in HER2+, ER-negative, node-negative early breast cancer with dual HER2 blockade |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | RCT (Phase 2, PERTAIN) | J Clin Oncol | Trastuzumab + aromatase inhibitor ± pertuzumab in first-line HER2+/HR+ metastatic/locally advanced breast cancer |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guideline | J Clin Oncol | ASCO guideline update: systemic therapy for advanced HER2-positive breast cancer |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | Systematic Review | Int J Mol Sci | Pertuzumab + trastuzumab + docetaxel as adjuvant doublet therapy for HER2-positive breast cancer |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Cohort (long-term follow-up) | Lancet Oncology | NeoSphere 5-year analysis: neoadjuvant pertuzumab + trastuzumab in locally advanced/inflammatory/early-stage HER2+ breast cancer |
| [37723497](https://pubmed.ncbi.nlm.nih.gov/37723497/) | 2023 | Real-world retrospective, subgroup analysis | World J Surg Oncol | PR status is a more decisive factor than ER status in efficacy of adding pertuzumab to neoadjuvant therapy for HER2+/node-positive breast cancer |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase 2 trial | Annals of Oncology | WSG-ADAPT HER2+/HR- final analysis: 12-week neoadjuvant dual HER2 blockade ± weekly paclitaxel |
| [32905036](https://pubmed.ncbi.nlm.nih.gov/32905036/) | 2020 | Literature Review | Cureus | Therapeutic strategies for HER2-positive metastatic breast cancer |
| [40739524](https://pubmed.ncbi.nlm.nih.gov/40739524/) | 2025 | Real-world study | Br J Clin Pharmacol | Real-world treatment patterns among patients with hormone receptor-positive metastatic breast cancer in the USA |

---

## Singapore Market Information

Pertuzumab is currently **not marketed or registered in Singapore** — 0 registrations are on file in the available regulatory dataset.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-HER2 monoclonal antibody; HER2–HER3 dimerization inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base meets L1 criteria — two completed Phase 3 RCTs (NCT04629846, NCT03726879) plus multiple supporting Phase 2 studies and guideline-level literature — but this is best understood as confirmation of a hormone-receptor-defined subgroup of Pertuzumab's existing HER2+ breast cancer use, not a mechanistically novel indication. Drug-level safety and regulatory documentation remain incomplete, and the product is not currently marketed in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent label warnings, contraindications, and precautions (Blocking data gap DG001)
- Formal mechanism-of-action documentation from DrugBank or manufacturer labeling (High-severity data gap DG002)
- Confirmation of Singapore regulatory/registration pathway status, since the drug is currently unmarketed locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

