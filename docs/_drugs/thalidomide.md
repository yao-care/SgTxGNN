---
layout: default
title: Thalidomide
parent: 僅模型預測 (L5)
nav_order: 969
evidence_level: L5
indication_count: 10
---

# Thalidomide
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

# Thalidomide: From Multiple Myeloma to Neuroblastoma

> **Note on candidate selection**: This Evidence Pack contains 10 TxGNN-predicted indications for thalidomide. The #1 and #2 ranked candidates by raw TxGNN score (*ganglioneuroblastoma*, *vertebral anomalies/T-cell dysfunction syndrome*) have **zero supporting trials or literature** and are flagged in the model's own rationale as likely knowledge-graph embedding noise rather than genuine signal. This report instead highlights **Neuroblastoma (rank 4)**, the highest-scoring candidate with substantive clinical and mechanistic support. A summary of all 10 candidates is provided at the end for transparency.

## One-Sentence Summary

Thalidomide is a well-established immunomodulatory drug (IMiD) with documented use in multiple myeloma and inflammatory conditions (per literature within this evidence pack), acting through cereblon (CRBN)-mediated protein degradation and anti-angiogenic effects. The TxGNN model predicts activity in **Neuroblastoma**, a pediatric solid tumor, with **3 clinical trials** and **8 relevant publications** — including a completed xenograft efficacy study and two completed Phase 2 trials — supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple Myeloma (established per literature evidence in this pack; no structured TFDA/local registration data available) |
| Predicted New Indication | Neuroblastoma |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails (conditional — see Conclusion) |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data (DrugBank MOA field) is not available in this evidence pack (flagged as data gap DG002). Based on the literature evidence collected, thalidomide is a **cereblon (CRBN) modulator / immunomodulatory drug (IMiD)**: it binds cereblon to redirect the CRL4-CRBN E3 ubiquitin ligase toward degradation of specific transcription factors (e.g., IKZF1/3), and separately exerts **anti-angiogenic activity** by suppressing bFGF/VEGF-driven neovascularization. These two mechanisms together underlie its established efficacy in multiple myeloma and its historical repositioning from a withdrawn sedative into an oncology/immunology agent.

Neuroblastoma is a highly vascularized pediatric solid tumor in which microvessel density correlates with poor prognosis, making it a mechanistically plausible target for anti-angiogenic therapy. Direct preclinical support exists: thalidomide significantly reduced tumor growth in a neuroblastoma xenograft model (PMID 14612937) and potentiated etoposide-induced apoptosis via NF-κB suppression in a murine model (PMID 29423589). This mechanistic rationale is further reinforced by two completed Phase 2 clinical trials combining thalidomide with chemotherapy (temozolomide, or a 5-drug metronomic regimen) specifically in children with relapsed/refractory neuroblastoma or brain tumors, giving this prediction a foundation stronger than mechanism alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00357500](https://clinicaltrials.gov/study/NCT00357500) | Phase 2 | Completed | 101 | Oral 5-drug anti-angiogenic metronomic regimen (thalidomide + celecoxib + fenofibrate + etoposide + cyclophosphamide) in relapsed/progressive cancer |
| [NCT00098865](https://clinicaltrials.gov/study/NCT00098865) | Phase 2 | Completed | 15 | Thalidomide + temozolomide in relapsed/progressive brain tumors or recurrent neuroblastoma |
| [NCT00049296](https://clinicaltrials.gov/study/NCT00049296) | Phase 1 | Completed | 26 | PK trial of thalidomide + docetaxel, anti-angiogenic therapeutic principle, advanced cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18024879](https://pubmed.ncbi.nlm.nih.gov/18024879/) | 2007 | Case Report | J Clin Oncol | Successful anti-angiogenic therapy for neuroblastoma with thalidomide |
| [14612937](https://pubmed.ncbi.nlm.nih.gov/14612937/) | 2003 | Preclinical/Xenograft | Int J Oncol | Thalidomide is anti-angiogenic in a neuroblastoma xenograft model |
| [29423589](https://pubmed.ncbi.nlm.nih.gov/29423589/) | 2018 | Preclinical | Pediatr Surg Int | Thalidomide potentiates etoposide-induced apoptosis via NF-κB suppression in murine neuroblastoma |
| [15707702](https://pubmed.ncbi.nlm.nih.gov/15707702/) | 2005 | Review | Cancer Treat Rev | Antiangiogenic strategies in neuroblastoma |
| [24123865](https://pubmed.ncbi.nlm.nih.gov/24123865/) | 2014 | Phase 2 Clinical Trial | Pediatr Blood Cancer | Multi-agent oral antiangiogenic (metronomic) regimen in children with recurrent/progressive cancer |
| [23982484](https://pubmed.ncbi.nlm.nih.gov/23982484/) | 2013 | Preclinical | Cancer Immunol Immunother | Lenalidomide overcomes NK-cell suppression by neuroblastoma microenvironment (IL-6/TGFβ1) |
| [12033499](https://pubmed.ncbi.nlm.nih.gov/12033499/) | 2002 | Preclinical | Biol Pharm Bull | Hydroxylated thalidomide metabolites reduce vessel density and tumor/endothelial proliferation |
| [10882863](https://pubmed.ncbi.nlm.nih.gov/10882863/) | 2000 | Review | Eur J Cancer | "Accidental" anti-angiogenic drugs, including thalidomide, as anticancer agents |

---

## Singapore Market Information

Currently no local registrations. Thalidomide is **not marketed** (未上市, 0 authorizations recorded) in this evidence pack.

---

## Cytotoxicity

Thalidomide is an oncology-relevant agent across the majority of predicted indications in this pack (neuroblastoma, AML/MDS, multiple myeloma variants), so this section is included.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunomodulatory drug (IMiD) — not a conventional cytotoxic agent; acts via cereblon-mediated protein degradation and anti-angiogenesis |
| Myelosuppression Risk | Not directly documented in this evidence pack; literature instead highlights **venous thromboembolism (VTE)** as a notable risk when combined with induction regimens (see NCT04106700, apixaban prophylaxis study) and peripheral neuropathy (PMID 31647152) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC, coagulation status/VTE risk assessment, neurological exam for peripheral neuropathy |
| Handling Protection | Teratogenicity requires strict controlled-distribution handling; refer to package insert and applicable REMS-equivalent protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were retrievable in this evidence pack (see data gaps below).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Conditional)**

**Rationale:**
The neuroblastoma candidate itself has L2 evidence (preclinical xenograft efficacy + 2 completed Phase 2 trials) justifying a "Proceed with Guardrails" recommendation. However, this is **blocked at the drug level**: TFDA/local label warnings and contraindications (DG001, severity: Blocking) are missing, which explicitly prevents entry into the S1 safety pre-evaluation stage regardless of indication-level evidence strength.

**To proceed, the following is needed:**
- **DG001 (Blocking)**: Retrieve official label warnings/contraindications (download and parse the package insert PDF from the relevant regulatory authority) — required before any safety pre-evaluation.
- **DG002 (High)**: Query DrugBank API for structured mechanism-of-action data to strengthen the mechanistic-link analysis.
- Route-of-administration and dosage-form compatibility data (currently "pending" for all candidates).
- Given thalidomide's known teratogenicity, a pediatric-population risk/benefit and REMS-equivalent distribution plan specific to neuroblastoma (pediatric indication) before advancing further.

---

## Appendix: Summary of All 10 TxGNN-Predicted Indications

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|------|------|------|------|
| 1 | Ganglioneuroblastoma | 98.96% | L5 | Hold | No trials/literature; likely KG noise |
| 2 | Vertebral anomalies/endocrine/T-cell dysfunction syndrome | 98.95% | L5 | Hold | No evidence; unrelated rare syndrome |
| 3 | Retroperitoneal neoplasm | 98.68% | L4 | Research Question | Only indirect case-report evidence (histiocytic sarcoma, Castleman disease) |
| **4** | **Neuroblastoma** | **98.66%** | **L2** | **Proceed with Guardrails** | **Headlined above** |
| 5 | Brachydactyly-syndactyly syndrome | 94.22% | L5 | Hold | Related to thalidomide's teratogenic *risk* profile, not a treatment target |
| 6 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 93.20% | L5 | Hold | Same as above — teratogenicity signal, not therapeutic |
| 7 | Rheumatoid Arthritis | 92.40% | L3 | Research Question | Older open-label studies (1989–1999); no modern RCT |
| 8 | Myeloid Leukemia (AML/MDS) | 90.54% | L2 | Proceed with Guardrails | Multiple completed Phase 2 trials in MDS/AML |
| 9 | Indolent Plasma Cell Myeloma | 88.46% | L2 | Proceed with Guardrails | Closely related to thalidomide's established myeloma use; strong Phase 2 evidence |
| 10 | Acute Lymphoblastic Leukemia | 74.75% | L4 | Research Question | Evidence largely from lenalidomide (analog), not thalidomide itself |

Candidates 8 and 9 are also reasonable alternative headline choices given comparable evidence strength, and may warrant separate dedicated evaluation reports.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

