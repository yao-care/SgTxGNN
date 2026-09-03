---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 951
evidence_level: L5
indication_count: 10
---

# Temozolomide
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

Using the report template above (no coding/debugging involved — this is direct content generation per the detailed prompt spec), here is the evaluation report.

# Temozolomide: From Malignant Glioma to Adult Astrocytic Tumour

## One-Sentence Summary

Temozolomide is an oral alkylating (imidazotetrazine) chemotherapy agent whose established use is in malignant glioma (glioblastoma / anaplastic astrocytoma), though this is not currently recorded in Singapore's structured regulatory data.
The TxGNN model's top-ranked prediction for this drug is **Adult Astrocytic Tumour**, which is substantially the same disease space as its known clinical use — this prediction is best read as a **model self-validation** rather than a genuinely novel repurposing signal.
It is supported by **2 clinical trials** (including one completed Phase 3 RCT) and **20 publications**, several of which are landmark practice-changing RCTs (e.g., Stupp 2005 NEJM).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Malignant glioma (glioblastoma multiforme / anaplastic astrocytoma) — not recorded in Singapore regulatory data; inferred from literature evidence in this pack |
| Predicted New Indication | Adult Astrocytic Tumour |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Structured mechanism-of-action data is not available for this drug record. However, the evidence pack's own rationale and literature confirm that temozolomide is an oral alkylating agent that induces DNA damage via O6-methylguanine methylation, triggering apoptosis in tumour cells — this is the established mechanism underlying its use as standard-of-care chemotherapy for adult astrocytic tumours, including glioblastoma.

Because "adult astrocytic tumour" is essentially the same disease category as temozolomide's well-documented existing use (the Stupp protocol — concurrent chemoradiotherapy followed by adjuvant temozolomide — has been the international standard of care for newly diagnosed glioblastoma since 2005), this TxGNN prediction functions as a **positive-control / self-consistency check** rather than a novel repurposing hypothesis. The mechanistic link is direct and well-established, and the strength of the evidence (two Phase 3 RCTs among the supporting literature, dozens of confirmatory publications) reflects existing clinical practice rather than an unproven new use.

Given this, the practical value of this evaluation lies less in "is this a viable new indication" and more in verifying that TxGNN correctly reproduces known drug-disease relationships, and in flagging the handful of related but genuinely more speculative predictions found lower in the ranked list (see "Other Candidate Indications" below).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | Completed | 500 | Randomized comparison of temozolomide alone vs. procarbazine/lomustine/vincristine (PCV) in recurrent WHO grade III/IV astrocytic tumours; core efficacy evidence for TMZ monotherapy in recurrent disease. |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | Completed | 26 | Dose-finding study of XL184 (cabozantinib) combined with temozolomide and radiotherapy in newly diagnosed glioblastoma; primarily a safety/PK study, not a TMZ efficacy trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | NEJM | Landmark EORTC/NCIC trial establishing that radiotherapy plus concomitant and adjuvant temozolomide improves survival vs. radiotherapy alone in newly diagnosed glioblastoma — basis of the "Stupp protocol" standard of care. |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | EF-14 trial: adding Tumor-Treating Fields to maintenance temozolomide significantly improved survival vs. temozolomide alone in glioblastoma. |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 Phase 3: lomustine-temozolomide combination superior to temozolomide alone in newly diagnosed, MGMT-methylated glioblastoma. |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | RCT | JAMA Oncology | Randomized trial of adding veliparib to temozolomide in MGMT-methylated glioblastoma. |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncology | NOA-08 trial: temozolomide chemotherapy alone vs. radiotherapy alone in elderly patients with malignant astrocytoma — supports TMZ as a reasonable alternative in this population. |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | NEJM | Randomized trial adding bevacizumab to standard temozolomide/radiotherapy in newly diagnosed glioblastoma; no overall survival benefit shown. |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT (Phase II/III) | J Clin Oncol | NRG Oncology BN007: dual immune checkpoint blockade added to standard temozolomide-based regimen in MGMT-unmethylated newly diagnosed glioblastoma. |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | Comprehensive review of glioblastoma and other primary adult brain malignancies, covering temozolomide-based standard therapy. |
| [41345097](https://pubmed.ncbi.nlm.nih.gov/41345097/) | 2025 | Phase Ib/II | Nature Communications | GEINO 1602 trial: glasdegib (hedgehog pathway inhibitor) combined with temozolomide and radiotherapy in newly diagnosed glioblastoma. |
| [31828428](https://pubmed.ncbi.nlm.nih.gov/31828428/) | 2020 | Cohort | J Cancer Res Clin Oncol | Tumour-Treating Fields combined with lomustine and temozolomide in newly diagnosed MGMT-methylated glioblastoma. |

---

## Singapore Market Information

No registrations are currently on record for this drug in Singapore (0 licenses; market status: **Not Marketed**). This is flagged in the evidence pack as a blocking data gap (TFDA/HSA package insert warnings and contraindications could not be retrieved), which limits the initial safety screen for this candidate.

---

## Cytotoxicity

Temozolomide is a conventional cytotoxic chemotherapy agent (alkylating agent, imidazotetrazine class), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, imidazotetrazine class) |
| Myelosuppression Risk | Moderate — primarily neutropenia and thrombocytopenia; literature in this pack notes generally lower myelotoxicity than PCV regimens, but dose-limiting thrombocytopenia is documented, and pharmacogenomic factors have been studied specifically for this risk |
| Emetogenicity Classification | Moderate (standard classification for oral alkylating agents; specific grading not itemized in this evidence pack) |
| Monitoring Items | CBC with differential (baseline and periodically through each cycle, e.g., day 22/29), liver function tests, renal function |
| Handling Protection | Yes — standard cytotoxic drug handling and disposal precautions required |

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack — this is logged as a **Blocking** data gap requiring TFDA/HSA package insert retrieval before proceeding further.)

---

## Other Candidate Indications from TxGNN (Same Drug)

For context, temozolomide's evidence pack contains 10 ranked predicted indications, all within the astrocytic/glial tumour family. Several are anatomically or age-specific variants with materially weaker evidence, including two flagged for **suspected ontology mapping mismatch**:

| Rank | Disease | Score | Evidence Level | Decision | Note |
|------|---------|-------|-----------------|----------|------|
| 2 | Cauda equina neoplasm | 99.30% | L4 | Hold | Mostly myxopapillary ependymoma; different histology from TMZ's core target |
| 3 | Childhood cerebral astrocytoma | 97.49% | L2 | Research Question | Multiple pediatric Phase 1/2 trials, no Phase 3 confirmation |
| 4 | Cerebellar astrocytoma | 97.44% | L3 | Research Question | Anatomic subtype, extrapolated evidence |
| 5 | Subependymal giant cell astrocytoma (SEGA) | 97.43% | L4 | Hold | **Likely ontology mismatch** — SEGA is TSC1/2-mTOR driven; standard treatment is mTOR inhibitors, not alkylating agents |
| 6 | Diencephalic astrocytomas | 97.35% | L5 | Hold | Model score only; sole supporting literature concerns BRAF-targeted therapy, not TMZ |
| 7 | Astrocytic tumor (general) | 97.25% | L2 | Proceed with Guardrails | Broad category, strong evidence volume but needs grade-specific stratification |
| 8 | High grade astrocytic tumor | 97.17% | L1 | Proceed with Guardrails | Effectively restates glioblastoma — strongest evidence tier |
| 9 | Low grade astrocytic tumor | 96.48% | L2 | Research Question | EORTC 22033-26033 RCT shows comparable-to-RT efficacy, no clear OS benefit |
| 10 | Brain astrocytoma (general) | 96.31% | L1 | Proceed with Guardrails | Broad category covering established GBM standard of care |

Ranks 5 and 6 in particular should not be advanced without manual disease-ontology review, as the supporting evidence does not match the predicted disease's actual standard of care.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The top prediction (adult astrocytic tumour) is backed by strong, largely pre-existing clinical evidence (including a completed Phase 3 RCT and multiple landmark trials), but it substantially overlaps with temozolomide's already-established use rather than representing a novel repurposing opportunity — guardrails are warranted mainly around regulatory/safety documentation gaps, not efficacy.

**To proceed, the following is needed:**
- Singapore/HSA package insert data (warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Structured mechanism-of-action confirmation via DrugBank API (DG002)
- Clarification of Singapore market status, given 0 registered licenses despite temozolomide being an internationally established therapy
- Manual disease-ontology review for lower-ranked predictions (SEGA, diencephalic astrocytoma) before any further action on those specific indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

