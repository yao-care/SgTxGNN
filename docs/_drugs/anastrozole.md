---
layout: default
title: Anastrozole
parent: High Evidence (L1-L2)
nav_order: 100
evidence_level: L1
indication_count: 10
---

# Anastrozole
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

# Anastrozole: From an Unrecorded Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Anastrozole is a non-steroidal aromatase inhibitor marketed in Singapore under 11 registrations, but the record lists no original indication.
The TxGNN model predicts it may be effective for **female breast carcinoma**, which is in fact the drug's established use, so this is effectively an on-label indication rather than true repurposing.
The prediction is supported by **50 clinical trials** (including 3 completed Phase 3 trials) and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all Singapore licence indication fields are empty) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

The structured mechanism-of-action field is not available. The literature in the pack describes anastrozole as a third-generation non-steroidal aromatase inhibitor. It blocks the aromatase (cytochrome P-450) enzyme complex, which carries out the final step of estrogen synthesis in peripheral tissues. In postmenopausal women this lowers circulating estrogen and deprives hormone-receptor-positive breast tumours of estrogen-driven growth.

Breast cancer is the drug's established, marketed use, so the prediction is well supported. The trials and papers below cover the whole disease continuum: prevention (IBIS-II), adjuvant treatment (ATAC), neoadjuvant treatment, and advanced disease. The input record should be corrected to list breast cancer as the original indication.

The other nine predictions for this drug are much weaker. Eight have no trials or literature, or only indirect papers, and all are rated Hold. Examples include neuroblastoma, monocytic leukemia and rhabdomyosarcoma.

---

## Clinical Trial Evidence

The pack lists 50 trials; the 10 most relevant are shown.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | Completed | 9358 | ATAC: anastrozole alone vs tamoxifen alone vs combination as adjuvant therapy in postmenopausal women |
| [NCT00078832](https://clinicaltrials.gov/study/NCT00078832) | Phase 3 | Completed | 3864 | IBIS-II: anastrozole for breast cancer prevention in high-risk postmenopausal women |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | Completed | 1914 | 6 vs 3 years of adjuvant anastrozole after 2–3 years of tamoxifen |
| [NCT02767661](https://clinicaltrials.gov/study/NCT02767661) | Phase 3 | Completed | 263 | Metronomic capecitabine plus aromatase inhibitor vs aromatase inhibitor alone, first-line HR+/HER2- metastatic disease |
| [NCT00688194](https://clinicaltrials.gov/study/NCT00688194) | Phase 3 | Unknown | 396 | Fulvestrant ± lapatinib ± aromatase inhibitor in metastatic disease progressing after aromatase inhibitor therapy |
| [NCT00274469](https://clinicaltrials.gov/study/NCT00274469) | Phase 2 | Completed | 205 | Fulvestrant 500 mg vs anastrozole 1 mg as first-line therapy in advanced HR+ disease |
| [NCT04436744](https://clinicaltrials.gov/study/NCT04436744) | Phase 2 | Completed | 221 | Giredestrant + palbociclib vs anastrozole + palbociclib, neoadjuvant, ER+/HER2- early disease |
| [NCT00629616](https://clinicaltrials.gov/study/NCT00629616) | Phase 2 | Completed | 116 | Neoadjuvant anastrozole vs fulvestrant, with hormone-sensitivity profiling |
| [NCT00186121](https://clinicaltrials.gov/study/NCT00186121) | Phase 2 | Completed | 35 | Anastrozole plus goserelin in premenopausal women with HR+ metastatic disease |
| [NCT01016665](https://clinicaltrials.gov/study/NCT01016665) | N/A | Completed | 71 | Double-blind placebo-controlled study of short-term anastrozole effects on proliferation and progesterone receptor indexes |

---

## Literature Evidence

The pack lists 20 publications; the 10 most relevant are shown.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | RCT | Lancet | IBIS-II long-term results: anastrozole vs placebo for preventing breast cancer (invasive and DCIS) |
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | RCT | Lancet | ATAC after 5 years of adjuvant treatment in 9,366 women: anastrozole significantly prolonged disease-free survival vs tamoxifen (575 vs 651 events) |
| [24716940](https://pubmed.ncbi.nlm.nih.gov/24716940/) | 2014 | Meta-analysis | Asian Pac J Cancer Prev | Fulvestrant 250 mg vs anastrozole 1 mg in advanced breast cancer, comparing efficacy and tolerability |
| [30499075](https://pubmed.ncbi.nlm.nih.gov/30499075/) | 2020 | Meta-analysis | Pathol Oncol Res | Endocrine therapy for DCIS after breast-conserving surgery and radiotherapy; includes 2 trials comparing tamoxifen with anastrozole |
| [34048027](https://pubmed.ncbi.nlm.nih.gov/34048027/) | 2021 | Pharmacogenomic study | Clin Pharmacol Ther | SNP–treatment interaction for anastrozole vs exemestane in 4,465 early-stage patients |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opin Pharmacother | Comparison of anastrozole, letrozole and exemestane in early breast cancer; AIs consistently superior to tamoxifen |
| [16439860](https://pubmed.ncbi.nlm.nih.gov/16439860/) | 2006 | Review | Oncology | Role of anastrozole from advanced disease through early disease and prevention; survival benefit vs megestrol acetate in second-line use |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Review | Rev Assoc Med Bras | Anastrozole in chemoprevention and treatment; notes inter-individual variability in pharmacokinetics |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Review | Expert Opin Drug Saf | Overview of adjuvant use; greater efficacy than tamoxifen in several randomised trials |
| [32632513](https://pubmed.ncbi.nlm.nih.gov/32632513/) | 2020 | Cohort study | Breast Cancer Res Treat | Genetic and clinical predictors of arthralgia during letrozole or anastrozole therapy |

---

## Singapore Market Information

Eleven registrations exist; five are shown. The approved-indication text is empty in every record.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN09433P | ARIMIDEX TABLET 1 mg | Tablet, film coated |
| SIN14627P | ANASTROZOLE SANDOZ FILM COATED TABLET 1MG | Tablet, film coated |
| SIN14796P | AROMATT 1 ANASTROZOLE TABLET 1 MG | Tablet |
| SIN14864P | ANZONAT FILM-COATED TABLET 1 mg | Tablet, film coated |
| SIN15280P | ANEXTROZOLE FILM-COATED TABLET 1 mg | Tablet, film coated |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Endocrine therapy (non-steroidal aromatase inhibitor); not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Bone density and musculoskeletal adverse events |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three completed Phase 3 trials (ATAC, IBIS-II and the 6- vs 3-year duration study) and multiple RCT publications support anastrozole in breast cancer, giving L1 evidence. The blocking gap is the missing Singapore package insert safety data.

**To proceed, the following is needed:**
- Download and parse the package insert (warnings and contraindications) from the HSA website. This is a blocking gap for safety screening.
- Retrieve the mechanism of action from DrugBank.
- Correct the input record so breast cancer is listed as the original, on-label indication.
- Confirm the approved indications for the Singapore licences.
- Apply the guardrails: limit use to hormone-receptor-positive disease and the labelled postmenopausal population, and monitor bone density and musculoskeletal adverse events.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

