---
layout: default
title: Uracil
parent: Low Evidence (L5)
nav_order: 1033
evidence_level: L5
indication_count: 10
---

# Uracil
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

# Uracil: From Oral Fluoropyrimidine Combination (UFT) to Colonic Neoplasm

## One-Sentence Summary

Uracil is the DPD-inhibiting component of the oral anticancer combination tegafur-uracil (UFT), which is registered in Singapore as UFT Capsule. The TxGNN model predicts it may be effective for **Colonic Neoplasm**. Of **50 registered clinical trials** and **20 publications** retrieved, only **one trial** (NCT00378716, a Phase 3 trial of UFT/LV) and a handful of publications test a uracil-containing regimen directly. The rest are fluoropyrimidine class evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. The registered product (UFT Capsule, tegafur-uracil) is an oral fluoropyrimidine anticancer combination. |
| Predicted New Indication | Colonic neoplasm |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L1 (the Phase 3 evidence applies to the UFT combination, not uracil alone) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for uracil was not retrieved from DrugBank. The mechanism below comes from the evidence review. In UFT, tegafur is a prodrug of 5-fluorouracil (5-FU). Uracil is added in excess to compete with 5-FU for the enzyme dihydropyrimidine dehydrogenase (DPD), which normally breaks 5-FU down. This keeps 5-FU exposure higher and longer from an oral dose.

Colon cancer is a core indication for fluoropyrimidine chemotherapy, and UFT has been developed as adjuvant treatment after tumour resection in several solid tumours, including colon/rectal cancer. This makes the prediction mechanistically plausible. The uracil-specific evidence applies to the UFT combination only. Uracil on its own is not an anticancer treatment, so any repurposing assessment should be restricted to the tegafur-uracil formulation.

---

## Clinical Trial Evidence

Only the first row directly tests a uracil-containing regimen. The others are fluoropyrimidine-backbone trials in colorectal cancer and show disease and class relevance only.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1608 | **Uracil/tegafur + leucovorin vs 5-FU + leucovorin** in resected stage II/III colon cancer |
| [NCT01228734](https://clinicaltrials.gov/study/NCT01228734) | Phase 3 | Completed | 553 | Cetuximab + FOLFOX-4 vs FOLFOX-4 in first-line RAS wild-type metastatic colorectal cancer (5-FU backbone, no uracil) |
| [NCT04607421](https://clinicaltrials.gov/study/NCT04607421) | Phase 3 | Active, not recruiting | 831 | Encorafenib + cetuximab ± chemotherapy in BRAF V600E-mutant metastatic colorectal cancer (no uracil) |
| [NCT00209625](https://clinicaltrials.gov/study/NCT00209625) | Phase 1/2 | Completed | 23 | Irinotecan + 5-FU + leucovorin in advanced colorectal cancer; dose-finding and efficacy |
| [NCT00039611](https://clinicaltrials.gov/study/NCT00039611) | Not applicable | Completed | Not reported | FOLFOX4 in untreated advanced colorectal cancer (backbone relevance only) |
| [NCT00227747](https://clinicaltrials.gov/study/NCT00227747) | Phase 3 | Completed | 598 | Preoperative chemoradiation with capecitabine ± oxaliplatin in resectable rectal carcinoma |
| [NCT02376452](https://clinicaltrials.gov/study/NCT02376452) | Phase 2 | Unknown | 100 | Raltitrexed + irinotecan vs FOLFIRI as second-line therapy in advanced colorectal cancer |
| [NCT02861300](https://clinicaltrials.gov/study/NCT02861300) | Phase 1/2 | Completed | 50 | CB-839 + capecitabine in fluoropyrimidine-resistant PIK3CA-mutant colorectal cancer |
| [NCT00952029](https://clinicaltrials.gov/study/NCT00952029) | Phase 2/3 | Completed | 492 | FOLFIRI + bevacizumab, with or without bevacizumab maintenance, in metastatic colorectal cancer |
| [NCT04269369](https://clinicaltrials.gov/study/NCT04269369) | Phase 4 | Unknown | 250 | Pre-emptive DPYD genotyping and phenotyping to reduce 5-FU/capecitabine toxicity (relevant to the DPD safety guardrail) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06: oral UFT + leucovorin vs IV 5-FU + leucovorin after surgery for stage II/III colon cancer, comparing disease-free and overall survival |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02: S-1 + oxaliplatin vs UFT/LV as adjuvant therapy in high-risk stage III colon cancer (UFT/LV was the comparator) |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 5-year follow-up: S-1 + oxaliplatin was **not superior** to UFT/LV for disease-free survival |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | Adjuvant immunochemotherapy (OK-432) combined with oral pyrimidines, including UFT, in colorectal cancer |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohort + meta-analysis | Medicine | Taiwan national insurance database (2000–2015) and meta-analysis comparing UFT with 5-FU as adjuvant therapy in stage II/III colon cancer |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective controlled study | Int J Clin Oncol | JFMC46-1201 final analysis: UFT/LV in high-risk stage II colon cancer, with 5-year overall survival and risk-factor analysis |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Prospective observational | BMC Cancer | JFMC46-1201 interim: 3-year disease-free survival was significantly higher with UFT/LV than surgery alone (propensity-matched) |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT as postoperative adjuvant chemotherapy for solid tumours (lung, stomach, colon/rectum, breast): clinical evidence and mechanism |
| [26722024](https://pubmed.ncbi.nlm.nih.gov/26722024/) | 2016 | Review | Anticancer Res | TAS-102 as an emerging oral fluoropyrimidine; discusses DPD-inhibiting approaches such as UFT |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case report | Cancer Chemother Pharmacol | Haemolytic anaemia in a patient receiving UFT for metastatic colon cancer |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03692P | UFT CAPSULE (Taiho Pharmaceutical Co Ltd) | Capsule (oral) | Not stated in the registration record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine class). The cytotoxic effect comes from tegafur/5-FU, and uracil acts as the DPD modulator. |
| Myelosuppression Risk | Not quantified in the available data; please refer to the package insert warnings and precautions. Haemolytic anaemia has been reported with UFT. |
| Emetogenicity Classification | Generally low for oral fluoropyrimidines; confirm against the package insert |
| Monitoring Items | CBC (with differential), liver and renal function; DPYD variant screening before treatment |
| Handling Protection | Follow institutional cytotoxic drug handling procedures; refer to the package insert |

---

## Safety Considerations

Formal warnings, contraindications and interaction data were not available for this report. Please refer to the package insert for safety information. The evidence review points to these risks:

- **DPD deficiency**: screen for DPYD variants, because reduced DPD activity increases fluoropyrimidine toxicity.
- **Haemolytic anaemia**: reported in a patient receiving UFT for metastatic colon cancer.
- **Hepatotoxicity**: monitor liver function during treatment.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Large Phase 3 and prospective studies support the UFT combination in colon cancer (NSABP C-06 and ACTS-CC 02, plus the completed 1,608-patient UFT/LV trial NCT00378716).
- Uracil has no standalone evidence, and most of the other registered trials only support the fluoropyrimidine class.
- The recommendation should be limited to the tegafur-uracil formulation.

**To proceed, the following is needed:**
- The HSA package insert, including approved indication, warnings and contraindications for SIN03692P
- Confirmation of whether UFT (with or without leucovorin) holds a colon cancer indication in Singapore
- A DPYD screening plan and monitoring protocol for haemolytic anaemia and hepatotoxicity
- DrugBank mechanism-of-action data to complete the mechanistic analysis

The same UFT rationale applies to the second-ranked prediction, gastric carcinoma, which has only a Phase 2 UFT maintenance study (NCT02903498) and is classed as a research question. The remaining predictions, such as benign lesions and non-specific terms, are rated Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

