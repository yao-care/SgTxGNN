---
layout: default
title: Olaparib
parent: High Evidence (L1-L2)
nav_order: 735
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Olaparib: predicted new indication Female breast carcinoma (evidence level L1). Approved use: Ovarian cancer"
monitor_inn: "Olaparib"
predicted_indications: ["female breast carcinoma", "gonadal germ cell tumor", "ovarian primitive germ cell tumor", "choriocarcinoma of ovary", "ovarian neoplasm", "ovarian malignant mesothelioma", "malignant non-epithelial tumor of ovary", "ovarian cancer, susceptibility to, 1", "ovarian adenosarcoma", "ovarian Sertoli-Leydig cell tumor"]
---

# Olaparib
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Olaparib: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Olaparib is an oral PARP inhibitor, originally used to treat BRCA-mutated ovarian cancer.
The TxGNN model predicts it may be effective for **female breast carcinoma**,
with **33 clinical trials** and **20 publications** compiled for this prediction, including several Phase 3 randomised trials in BRCA-mutated breast cancer.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (the Singapore licence records contain no approved-indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.09% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Based on known information, olaparib inhibits PARP1/2 and traps PARP on DNA. In tumours with defective homologous recombination repair, such as those carrying BRCA1/2 mutations, this causes synthetic lethality: the cancer cells cannot repair the resulting DNA damage and die.

Ovarian cancer and breast cancer share this BRCA-related biology. In germline BRCA1/2-mutated breast cancer, homologous recombination repair is deficient, which is the same mechanism underlying olaparib's use in BRCA-mutated ovarian cancer. This makes the prediction mechanistically plausible. It is also consistent with the literature, which describes olaparib as approved for germline BRCA-mutated HER2-negative breast cancer.

The benefit is therefore expected mainly in biomarker-selected patients (germline BRCA1/2 or other homologous recombination gene alterations), not in all breast cancer.

## Clinical Trial Evidence

Of the 33 trials compiled, the most relevant are shown below. Many are early-phase combination studies, and the compiled data contains no completed Phase 3 breast cancer registry entry. The Phase 3 breast cancer evidence comes from the publications listed in the next section.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Phase 2 | Completed | 99 | Open-label study of olaparib (AZD2281) in BRCA-mutated breast and ovarian cancer; response rate and response markers |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Phase 2 | Recruiting | 34 | Pembrolizumab and ablative radiotherapy with or without olaparib in metastatic triple-negative or HR+/HER2- breast cancer |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Phase 4 | Completed | 202 | Olaparib in Indian patients with relapsed ovarian cancer and metastatic breast cancer with germline BRCA1/2 mutation (limited direct breast evidence) |
| [NCT02684318](https://clinicaltrials.gov/study/NCT02684318) | Phase 1/2 | Unknown | 100 | Lurbinectedin (PM01183) plus olaparib in advanced solid tumours |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Phase 1 | Completed | 118 | PI3K inhibitor (BKM120 or BYL719) plus olaparib in triple-negative breast cancer or high-grade serous ovarian cancer; safety and dosing |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Phase 1 | Completed | 77 | Olaparib plus carboplatin in refractory or recurrent women's cancers; pharmacokinetic/pharmacodynamic run-in |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Phase 1/2 | Active, not recruiting | 155 | Cediranib plus olaparib in recurrent ovarian or triple-negative breast cancer |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Phase 1 | Completed | 25 | Carboplatin-olaparib followed by olaparib vs capecitabine in BRCA-mutated HER2-negative advanced breast cancer; phase 1 dose finding |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Phase 1 | Completed | 24 | Olaparib with radiation therapy in triple-negative breast cancer |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Phase 1 | Active, not recruiting | 36 | Olaparib plus navitoclax in triple-negative breast cancer and high-grade serous ovarian cancer |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuvant olaparib in BRCA1/2-mutated early breast cancer |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA overall survival results of adjuvant olaparib in high-risk, HER2-negative early breast cancer with germline BRCA1/2 variants |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib in metastatic breast cancer with a germline BRCA mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD final overall survival and tolerability vs physician's-choice chemotherapy |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | Phase 3 follow-up | Eur J Cancer | OlympiAD extended follow-up; median overall survival 19.3 vs 17.1 months in the final analysis (P = 0.513) |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Phase 2 trial | J Clin Oncol | TBCRC 048: olaparib in metastatic breast cancer with somatic BRCA1/2 or other homologous recombination gene mutations |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Phase 2 trial | J Clin Oncol | Olaparib monotherapy in advanced cancers with germline BRCA1/2 mutation, including breast cancer |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Phase 2 (I-SPY2) | Cancer Cell | Durvalumab plus olaparib and paclitaxel increased pathologic complete response rates in HER2-negative breast cancer |
| [32249603](https://pubmed.ncbi.nlm.nih.gov/32249603/) | 2020 | Review | Future Oncol | Olaparib for advanced breast cancer |
| [29867226](https://pubmed.ncbi.nlm.nih.gov/29867226/) | 2018 | Review | Br J Cancer | BRCA1/2 testing and therapeutic implications for breast cancer management |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15662P | LYNPARZA FILM-COATED TABLET 150MG | Film-coated tablet | Not stated in the licence record |
| SIN15663P | LYNPARZA FILM-COATED TABLET 100MG | Film-coated tablet | Not stated in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (PARP inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; haematological parameters (CBC) are generally monitored for this drug class |
| Handling Protection | Please refer to the package insert and local handling regulations |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in the drug interaction query. Major-level interactions in the listed results include:
  - Aprepitant
  - Dexamethasone
  - Clarithromycin

  Moderate-level examples include metformin, bupropion, cimetidine, miconazole, ondansetron, glyburide, repaglinide, rosuvastatin and simvastatin. Prucalopride is rated Minor.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Randomised Phase 3 studies (OlympiA and OlympiAD) support olaparib in germline BRCA-mutated breast cancer, and the mechanism matches its established use in ovarian cancer. Evidence applies mainly to biomarker-selected patients, so use should be restricted to that group. Olaparib is already marketed in Singapore, with two registrations.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website, which are currently missing
- Mechanism of action data, which is currently unavailable
- Confirmation of the approved indication wording on the Singapore licences, since the licence records contain no indication text
- A germline BRCA1/2 testing pathway to select eligible patients
- A monitoring plan for haematological toxicity and for the major drug interactions (aprepitant, dexamethasone, clarithromycin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

