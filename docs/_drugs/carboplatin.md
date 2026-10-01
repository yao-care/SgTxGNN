---
layout: default
title: Carboplatin
parent: Low Evidence (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Carboplatin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Carboplatin: From Platinum Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based chemotherapy drug that is currently marketed in Singapore under 3 registrations. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with a score of 99.86%. This direction is currently backed by **50 clinical trials** and **20 publications**, including several completed Phase 3 trials, but the payload contains no outcome data for them.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 (3 completed Phase 3 trials are listed; carboplatin is not the sole tested variable in all of them, and no results are in the payload) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacology, carboplatin is a platinum agent that forms DNA crosslinks and damages the DNA of dividing tumour cells.

Tumours with homologous recombination deficiency, such as BRCA1/2-associated or triple-negative breast cancer (TNBC), are generally more sensitive to DNA-damaging agents. This explains why many of the retrieved trials focus on TNBC and BRCA-mutated disease. The list also includes HER2-positive regimens in which carboplatin is combined with a taxane and trastuzumab, with or without pertuzumab.

Several trials use carboplatin only as the chemotherapy backbone while testing another agent, so they support use of the regimen rather than carboplatin's own contribution. Direct evidence comes from trials that make carboplatin the tested variable, such as carboplatin versus docetaxel and paclitaxel with or without carboplatin. Published results for these trials should be reviewed before drawing conclusions.

## Clinical Trial Evidence

The table lists the 10 most relevant of the 50 retrieved trials. Trials where carboplatin is the tested variable are listed first, followed by supporting trials where it is part of the regimen.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Carboplatin vs docetaxel in metastatic or recurrent ER-/PR-/HER2- breast cancer. No results in the payload. |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Neoadjuvant weekly paclitaxel vs paclitaxel plus carboplatin in large operable or locally advanced TNBC. |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: compares two dose-dense, dose-intensified neoadjuvant regimens (ETC vs PM(Cb)) in high-risk early breast cancer. |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel and trastuzumab with or without carboplatin as first-line therapy for HER2-amplified advanced breast cancer. |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Neoadjuvant TCHP (docetaxel, carboplatin, trastuzumab, pertuzumab) with or without estrogen deprivation in HR+/HER2+ breast cancer. |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | Completed | 148 | Randomized pilot: carboplatin vs docetaxel in metastatic breast cancer with a genetic (BRCA) background. |
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | Completed | 154 | NACATRINE: neoadjuvant carboplatin in TNBC. |
| [NCT00479674](https://clinicaltrials.gov/study/NCT00479674) | Phase 2 | Completed | 41 | Abraxane, carboplatin and bevacizumab in metastatic TNBC. |
| [NCT00232505](https://clinicaltrials.gov/study/NCT00232505) | Phase 2 | Completed | 112 | Cetuximab alone or with carboplatin in ER-/PR-/HER2-non-overexpressing metastatic breast cancer. |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | TARMAC: epirubicin and cyclophosphamide followed by docetaxel and carboplatin in Nigerian women with TNBC. The primary endpoint is pathological complete response. |

## Literature Evidence

The table lists 10 of the 20 retrieved publications. Randomized trials and meta-analyses are listed first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase 3 RCT | Eur J Cancer | BROCADE3: final overall survival results for veliparib added to carboplatin and paclitaxel in BRCA-mutated, HER2-negative advanced breast cancer. |
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief: camrelizumab vs placebo plus a platinum-containing neoadjuvant regimen in early or locally advanced TNBC. |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT (Phase 2b) | Nat Commun | Compares ARX788 plus pyrotinib with standard TCbHP (docetaxel, carboplatin, trastuzumab, pertuzumab) in HER2-positive breast cancer. |
| [40817986](https://pubmed.ncbi.nlm.nih.gov/40817986/) | 2025 | Randomized Phase 2 | Breast Cancer Res Treat | Single-agent carboplatin vs carboplatin plus everolimus in advanced TNBC. |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Adding carboplatin or bevacizumab improved pathological complete remission rates in neoadjuvant TNBC treatment. |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase 2 trial | Breast Cancer Res | Carboplatin plus bevacizumab in breast cancer brain metastases. |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Early-phase trial | Breast Cancer Res Treat | Carboplatin, gemcitabine and mifepristone in advanced breast and recurrent epithelial ovarian cancer. |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Accumulating evidence for synergy, efficacy and safety of paclitaxel-carboplatin in advanced breast cancer. |
| [9516604](https://pubmed.ncbi.nlm.nih.gov/9516604/) | 1998 | Phase 2 trial | Oncology | Paclitaxel plus carboplatin as first-line chemotherapy in 66 patients with advanced breast cancer. |
| [35837812](https://pubmed.ncbi.nlm.nih.gov/35837812/) | 2023 | Retrospective | Cancer Med | Carboplatin dose, anaemia and pathological complete response in 294 patients treated with neoadjuvant TCHP. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16203P | KEMOCARB Concentrate for Solution for Infusion 10 mg/ml | Infusion, solution concentrate | Fresenius Kabi Oncology Ltd. |
| SIN02301P | DBL Carboplatin Injection 10 mg/ml | Injection | Hospira Australia Pty Ltd |
| SIN10356P | CARBOTINOL Injection 50 mg/5 ml | Injection | Korea United Pharmaceutical Inc |

All three products are injectable. The approved indication text was not available for these registrations.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (platinum class) |
| Myelosuppression Risk | High. Thrombocytopenia and neutropenia are typically dose-limiting, and anaemia is common (see PMID 35837812 for carboplatin-related grade 3/4 anaemia in TCHP). |
| Emetogenicity Classification | Moderate (higher at higher doses) |
| Monitoring Items | CBC with differential, renal function, liver function, electrolytes |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries reflect general class knowledge, because DrugBank toxicity data and package insert warnings were not available in the payload. Please refer to the package insert warnings and precautions.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The breast cancer indication has the strongest evidence among the predicted indications. Three completed Phase 3 trials and several randomized studies involve carboplatin-containing regimens, with the clearest signal in TNBC and BRCA-associated disease. However, several of these trials use carboplatin only as a backbone, and no outcome data is in the payload, so efficacy and subgroup benefit are not yet confirmed.

**To proceed, the following is needed:**
- The published results of NCT00532727, NCT03168880 and NCT02125344, to establish carboplatin's own contribution.
- Subgroup evidence by BRCA and TNBC status.
- The HSA package insert warnings, contraindications and approved indication text (currently missing, and blocking safety screening).
- Detailed mechanism of action data from DrugBank.
- A safety monitoring plan covering myelosuppression, anaemia and emesis.

Other predicted indications are weaker. Germ cell tumour and endometrial mixed adenocarcinoma have moderate evidence and are best treated as research questions. The remaining mucinous and rare-histology predictions rest mainly on the model score and should stay on Hold.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

