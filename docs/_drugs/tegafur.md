---
layout: default
title: Tegafur
parent: High Evidence (L1-L2)
nav_order: 949
evidence_level: L1
indication_count: 10
---

# Tegafur
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

# Tegafur: From Oral Fluoropyrimidine Chemotherapy to Colonic Neoplasm

## One-Sentence Summary

Tegafur is an oral prodrug of 5-fluorouracil (5-FU), marketed in Singapore in UFT and TS-ONE capsules; the registration records supplied do not state an approved indication.
The TxGNN model predicts it may be effective for **Colonic Neoplasm**, with **30 clinical trials** and **20 publications** currently supporting this direction.
This is closer to an established use of tegafur-containing regimens than to true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Colonic neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the source record. The evidence review gives the following mechanism. Tegafur is converted mainly by hepatic CYP2A6 into 5-FU, which inhibits thymidylate synthase and DNA/RNA synthesis in tumour cells. In UFT, uracil competitively inhibits the DPD enzyme and raises 5-FU exposure. In S-1, gimeracil (a DPD inhibitor) and oteracil (which reduces gut toxicity) are added.

Fluoropyrimidines are an established backbone of colorectal cancer chemotherapy, so the very high model score matches the clinical evidence. Tegafur-containing regimens such as UFT/LV (tegafur-uracil plus leucovorin) and S-1 have been tested in colon and colorectal cancer in many trials. A 2015 phase III report describes UFT/LV as a widely used standard adjuvant chemotherapy for colon cancer in Japan.

Because of this, regional on-label status should be confirmed before treating this as a new indication.

## Clinical Trial Evidence

Of the 30 trials retrieved, the 10 most relevant are listed below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | Completed | 1608 | Oral UFT + leucovorin vs 5-FU + leucovorin in resected stage II/III colon cancer |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | Completed | 1535 | UFT + leucovorin vs S-1 as adjuvant treatment for stage III colon cancer, with gene-expression predictive factors |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | Completed | 2025 | Adjuvant UFT vs observation after curative resection of stage II colon cancer |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | Completed | 900 | Postoperative UFT vs surgery alone in Dukes C colorectal cancer (NSAS-CC); relapse-free and overall survival |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | Completed | 161 | S-1 vs capecitabine as first-line therapy in metastatic colorectal cancer (SALTO); safety evaluation |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | Unknown | 1191 | SOX (S-1 + oxaliplatin) vs XELOX (capecitabine + oxaliplatin) as adjuvant chemotherapy for stage III colorectal cancer |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | Unknown | 340 | Postoperative UFT+LV, UFT+LV/UFT and UFT+LV+PSK/UFT+PSK in stage III colorectal cancer; disease-free and overall survival |
| [NCT00497107](https://clinicaltrials.gov/study/NCT00497107) | Phase 3 | Unknown | 300 | UFT/LV vs UFT/LV + PSK after curative surgery in stage IIIa/IIIb colorectal cancer; primary endpoint 3-year disease-free survival |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Phase 3 | Unknown | 380 | UFT + PSK vs UFT + LV as adjuvant therapy in stage IIB/III colorectal cancer |
| [NCT05266300](https://clinicaltrials.gov/study/NCT05266300) | N/A | Completed | 722 | DPYD genotyping before fluoropyrimidine treatment (5-FU, capecitabine, tegafur); supports the safety guardrail, not an efficacy trial |

## Literature Evidence

Of the 20 publications retrieved, the 10 most relevant are listed below. Findings are summarised from the abstracts available.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 design: phase III superiority trial of SOX vs UFT/LV as adjuvant chemotherapy in high-risk stage III colon cancer |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT (5-year update) | ESMO Open | SOX was not superior to UFT/LV for disease-free survival in high-risk stage III colon cancer; reports final overall survival and stage subgroups |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | Randomized trial | J Clin Oncol | NSABP C-06: oral UFT + leucovorin compared with intravenous 5-FU + leucovorin in stage II/III colon carcinoma; endpoints disease-free and overall survival |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT | Ann Oncol | JFMC33-0502: phase III trial of treatment duration for UFT/LV adjuvant chemotherapy in stage IIB/III colon cancer |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | Adjuvant immunochemotherapy (OK-432) and chemotherapy with oral pyrimidines (carmofur, UFT) in colorectal cancer |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | Prospective controlled trial | Int J Clin Oncol | JFMC46-1201 final analysis: UFT/LV adjuvant treatment in high-risk stage II colon cancer; updated 5-year overall survival |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | Prospective observational study | BMC Cancer | JFMC46-1201: UFT/LV vs surgery alone in high-risk stage II colon cancer, using propensity score matching |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | Cohort study and meta-analysis | Medicine | Taiwan national cohort comparing UFT with 5-FU as adjuvant chemotherapy in stage II/III colon cancer; disease-free and overall survival |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT as postoperative adjuvant chemotherapy for solid tumours, including clinical evidence and mechanism of action |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Guideline/Consensus | Clin Colorectal Cancer | Asian consensus adapting international guidelines for metastatic colorectal cancer |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN03692P | UFT CAPSULE | Capsule | Taiho Pharmaceutical Co Ltd |
| SIN13672P | TS-ONE Capsule 20 | Capsule | Taiho Pharmaceutical Co., Ltd. (Tokushima Plant) |
| SIN13673P | TS-ONE Capsule 25 | Capsule | Taiho Pharmaceutical Co., Ltd. (Tokushima Plant) |

The approved indication text is not included in the registration records provided. All registered products are oral capsules.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (oral fluoropyrimidine, 5-FU prodrug) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Renal function (dose adjustment); DPYD genotype or DPD activity before treatment; INR if co-administered with warfarin; haematological parameters (a case report describes UFT-induced haemolytic anaemia) |
| Handling Protection | Follow local cytotoxic drug handling regulations |

## Safety Considerations

Package insert warnings, contraindications and drug interaction data are not available in the current record.

The evidence review identified these guardrails:
- **DPD deficiency**: DPYD genotyping or DPD screening before treatment. A completed implementation study (NCT05266300, n=722) supports this approach.
- **Drug interactions**: monitor for interactions, especially with warfarin.
- **Renal function**: dose according to renal function.
- **Adverse events**: a case report describes haemolytic anaemia during UFT therapy for metastatic colon cancer (PMID 11320674).

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least five completed phase 3 trials, plus a large body of adjuvant and metastatic colorectal data, support tegafur-containing regimens in colon cancer, which meets the L1 criterion. Safety screening cannot be completed yet because the package insert data is missing, so safeguards are required.

The other nine predicted indications are all Hold. Seven are benign lesions or non-specific terms, with no trials or only indirect case reports. The rectosigmoid junction neoplasm falls within the colorectal cancer spectrum, but site-specific data are lacking.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking for safety screening)
- The approved indications for UFT and TS-ONE in Singapore, to confirm whether colon cancer is already on-label
- Detailed mechanism-of-action data from DrugBank
- A DPYD/DPD screening protocol, renal dosing guidance and a warfarin interaction monitoring plan
- Status updates for trials listed as Unknown, and relevance grading for the six trials still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

