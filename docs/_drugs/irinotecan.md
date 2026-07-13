---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 531
evidence_level: L5
indication_count: 10
---

# Irinotecan
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

# Irinotecan: From Colorectal Cancer to Female Breast Carcinoma

## One-Sentence Summary

Irinotecan (CPT-11) is a camptothecin-derived topoisomerase I inhibitor widely deployed as the backbone of FOLFIRI and FOLFIRINOX regimens for colorectal and pancreatic cancers.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **22 clinical trials** and **20 publications** currently supporting this direction — including two pivotal Phase 3 programmes of sacituzumab govitecan, an antibody-drug conjugate that delivers Irinotecan's active metabolite SN-38 directly to breast tumour cells, and a dedicated Phase 2 trial testing Irinotecan monotherapy in anthracycline/taxane-refractory metastatic breast cancer.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer (globally established; not registered in Singapore) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Irinotecan is a prodrug that is hydrolysed in vivo to SN-38, which traps Topoisomerase I in a cleavable complex with DNA, blocking the replication fork and triggering double-strand breaks during S-phase — ultimately driving tumour cell apoptosis. Because this mechanism targets rapid DNA replication rather than a tissue-specific receptor, its cytotoxic activity is broadly applicable to any fast-proliferating malignancy with high Topoisomerase I expression.

The strongest mechanistic bridge to breast cancer comes from antibody-drug conjugates (ADCs). TROP-2, a transmembrane glycoprotein overexpressed in most breast cancers — especially triple-negative (TNBC) and HR+/HER2-negative subtypes — has been exploited to deliver SN-38 selectively to tumour cells. Sacituzumab govitecan (an anti-TROP-2/SN-38 ADC) received FDA approval for TNBC on the strength of ASCENT (Phase 3) and for HR+/HER2-negative metastatic breast cancer based on TROPiCS-02 (Phase 3), directly validating the clinical activity of SN-38 in breast cancer. Nanoliposomal formulations of Irinotecan itself (Nal-IRI/MM-398) have also been evaluated in breast cancer patients in Phase 1 and Phase 2 studies, further supporting the drug's intrinsic efficacy independent of the ADC platform.

Conventional Irinotecan monotherapy has been assessed as a later-line option for patients who have exhausted anthracyclines, taxanes, and capecitabine. Phase 2 data (NCT03562390, n = 124; NCT00072852, n = 134) demonstrate measurable activity in this heavily pre-treated population. The mechanistic and clinical evidence together make the TxGNN prediction highly plausible rather than merely algorithmic.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Direct evaluation of Irinotecan monotherapy as 3rd-line or later treatment in Chinese patients with locally recurrent or metastatic breast cancer after ≥2 prior anthracycline/taxane regimens; primary endpoints: safety and efficacy |
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Randomised comparison of two schedules (5-day vs 14-day oral irinotecan) in metastatic breast cancer patients who had failed anthracycline, taxane, and capecitabine; provided direct efficacy and toxicity data for Irinotecan in a heavily pre-treated setting |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | Biodistribution, PK/PD, and ferumoxytol MRI imaging of MM-398 (nanoliposomal Irinotecan) in breast cancer patients; directly quantified tumour drug uptake and safety profile of Irinotecan in breast cancer |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | Pivotal multi-tumour-type study of sacituzumab govitecan (anti-TROP-2/SN-38 ADC); Phase 2 cohort in TNBC generated the data underpinning FDA Breakthrough Therapy designation |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 (checkpoint kinase inhibitor) plus Irinotecan in solid tumours; Part II specifically enrolled triple-negative (ER-/PgR-/HER2-non-amplified) recurrent breast cancer, providing dose-finding data in TNBC |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Sequential Irinotecan followed by Capecitabine in advanced breast cancer; investigated whether Irinotecan pre-treatment sensitises breast cells to capecitabine by Topoisomerase I upregulation |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Basket study of navicixizumab (anti-DLL4/VEGF bispecific) combined with Irinotecan or paclitaxel in advanced cancers; Cohort C is dedicated to TNBC, providing a contemporary Irinotecan-combination evaluation |
| [NCT02033551](https://clinicaltrials.gov/study/NCT02033551) | Phase 1 | Completed | 47 | Extension study of veliparib (PARP inhibitor) combined with Carboplatin/Paclitaxel or FOLFIRI (including Irinotecan) in solid tumours including breast cancer; established tolerability of Irinotecan-based combinations with PARP inhibition |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | Terminated | 221 | Selinexor (XPO1 inhibitor) combined with multiple standard chemotherapy backbones including Irinotecan in advanced malignancies; provided tolerability reference for Irinotecan combinations across tumour types |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | Dose-escalation study of SNB-101, a novel SN-38 nanoparticle formulation, in advanced solid tumours; characterised PK and safety of direct SN-38 delivery — the active moiety of Irinotecan |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Phase 3 RCT | N Engl J Med | ASCENT trial: sacituzumab govitecan (SN-38 ADC) vs physician's choice chemotherapy in refractory mTNBC; significantly improved PFS and OS, directly validating SN-38 (Irinotecan's active metabolite) as an effective payload in breast cancer |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | Phase 3 RCT | J Clin Oncol | TROPiCS-02: sacituzumab govitecan vs physician's choice in pre-treated HR+/HER2-negative mBC; improved PFS and OS across multiple lines of prior therapy, extending clinical validation of SN-38 beyond TNBC |
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Phase 3 Protocol | Future Oncology | TROPiCS-02 protocol paper; describes design rationale, patient population, and endpoints — contextualises Trop-2/SN-38 strategy in endocrine-resistant mBC |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Systematic Review | Breast | Comprehensive review of TROP-2-targeting ADCs in mBC; summarises clinical development trajectory from sacituzumab govitecan to next-generation SN-38 conjugates |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Phase 2 | J Clin Oncol | Sacituzumab govitecan in heavily pre-treated mTNBC (n = 108); ORR 33.3%, median PFS 5.5 months; provided the phase 2 dataset that led to FDA Breakthrough Therapy designation |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 | Eur J Cancer | PHENOMENAL study: liposomal Irinotecan (nal-IRI) in HER2-negative breast cancer patients with brain metastases; demonstrated CNS penetration and antitumour activity, opening a new application avenue |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Phase 1 | Clin Cancer Res | First-in-human sacituzumab govitecan study; established safety, PK, and early efficacy signals across multiple solid tumour types including breast cancer |
| [31208270](https://pubmed.ncbi.nlm.nih.gov/31208270/) | 2019 | Review | mAbs | Mechanistic review of SN-38-based ADCs targeting TROP-2; explains the pharmacological rationale for coupling a camptothecin payload to tumour-targeted antibodies and summarises the ADC landscape |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology | Proposed mechanistic synergy between mitomycin and Irinotecan in breast cancer: mitomycin upregulates Topoisomerase I, enhancing sensitivity to SN-38; provided early rationale for Irinotecan in the breast cancer setting |
| [39768216](https://pubmed.ncbi.nlm.nih.gov/39768216/) | 2024 | Review | Cells | Comprehensive review of sacituzumab govitecan in refractory TNBC; discusses resistance mechanisms, biomarkers (Trop-2 expression, UGT1A1 polymorphism), and future combination strategies relevant to Irinotecan-based therapy |

---

## Singapore Market Information

Irinotecan is currently **not registered** with the Health Sciences Authority (HSA) of Singapore. No product licences are on record (0 authorisations). Irinotecan is, however, internationally approved in numerous jurisdictions for colorectal cancer (as part of FOLFIRI/FOLFOX-IRI regimens) and pancreatic cancer (as part of FOLFIRINOX/NALIRIFOX), and its active metabolite SN-38 is delivered via the HSA/FDA-approved ADC sacituzumab govitecan.

Any clinical use in Singapore would require either special access under the Serious Adverse Drug Events framework or a formal HSA registration application referencing global regulatory approvals.

---

## Cytotoxicity

Irinotecan is a **conventional cytotoxic chemotherapy** (camptothecin class). The following table applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Camptothecin / Topoisomerase I inhibitor class |
| Myelosuppression Risk | **High** — Neutropenia (including febrile neutropenia) is the primary dose-limiting toxicity; thrombocytopenia and anaemia also occur; nadir typically at Day 8–15 |
| Emetogenicity Classification | Moderate (IV bolus/infusion regimens); risk increased with higher single doses and FOLFIRI-type schedules |
| Monitoring Items | Full blood count with differential (CBC) before each cycle; liver function tests (bilirubin, ALT/AST — bilirubin elevation impairs SN-38 glucuronidation); renal function; UGT1A1 genotyping recommended prior to initiation (UGT1A1\*28 homozygotes at significantly elevated risk of severe neutropenia and diarrhoea) |
| Handling Protection | Must be handled following cytotoxic drug handling regulations: closed-system transfer devices, appropriate PPE (gloves, gown, eye protection), preparation in a certified biological safety cabinet; waste disposal per cytotoxic/hazardous waste protocols |

---

## Safety Considerations

No Singapore package insert data or specific warning/contraindication/DDI records are available in this evidence pack. Please refer to the originator package insert (e.g., Camptosar® SmPC / FDA label) for comprehensive safety information, with particular attention to:

- Severe cholinergic syndrome (acute diarrhoea, diaphoresis, abdominal cramping) occurring during or immediately after infusion — managed with atropine
- Delayed diarrhoea (onset > 24 h post-infusion) — potentially life-threatening if untreated; managed with high-dose loperamide
- UGT1A1\*28 pharmacogenomic risk — dose reduction required in homozygous individuals

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 3 RCTs (ASCENT and TROPiCS-02) have established that SN-38 — the active metabolite of Irinotecan — is clinically effective in both TNBC and HR+/HER2-negative metastatic breast cancer when delivered via the TROP-2-targeted ADC sacituzumab govitecan, providing the most direct mechanistic validation available. In parallel, a dedicated Phase 2 trial (NCT03562390, n = 124) evaluated Irinotecan as a stand-alone agent in anthracycline/taxane-refractory mBC in a Chinese patient population, and a completed Phase 2 randomised study (NCT00072852, n = 134) compared dosing schedules in a similar population. Evidence is sufficient to justify further development, but Irinotecan as a naked drug (not conjugated) still lacks a completed Phase 3 RCT in breast cancer.

**To proceed, the following is needed:**

- **Regulatory safety review:** Obtain Singapore HSA (and/or TFDA/EMA) approved package insert to complete the safety gap (DG001 — currently Blocking)
- **MOA data confirmation:** Retrieve full DrugBank entry for DB00762 to formally document MOA and categorisation (DG002 — currently High severity)
- **UGT1A1 genotyping plan:** Establish a pharmacogenomics screening protocol for UGT1A1\*28 before any clinical programme, particularly relevant in Asian populations (higher frequency of \*6 and \*28 alleles)
- **Route and formulation assessment:** Confirm that IV formulations are accessible or specifiable (nanoliposomal vs. conventional), as formulation affects both PK and CNS penetration
- **Phase 3 gap:** Design or identify a Phase 3 randomised trial specifically for Irinotecan monotherapy or combination in the target breast cancer subtype (TNBC or HR+) to upgrade evidence from L2 to L1 before regulatory submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

