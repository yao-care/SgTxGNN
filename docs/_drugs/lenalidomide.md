---
layout: default
title: Lenalidomide
parent: 僅模型預測 (L5)
nav_order: 580
evidence_level: L5
indication_count: 10
---

# Lenalidomide
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

# Lenalidomide: From Multiple Myeloma / MDS(del 5q) to Myeloid Leukemia (AML)

## One-Sentence Summary

Lenalidomide is an oral immunomodulatory imide drug (IMiD) whose internationally established uses include multiple myeloma and transfusion-dependent anemia in low-risk myelodysplastic syndrome (MDS) with a deletion 5q (del(5q)) cytogenetic abnormality (local Singapore license data for these indications is not available in this evidence pack).
The TxGNN model predicts it may also be effective for **Myeloid Leukemia (acute myeloid leukemia, AML)**, with **50 clinical trials** and **20 publications** currently retrieved for this drug–disease pair — though, as detailed below, part of that literature actually documents lenalidomide as a *risk factor* for secondary myeloid leukemia rather than a treatment for it, making this a genuine dual-edged research question rather than a straightforward efficacy signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple myeloma / low-risk MDS with del(5q)-associated anemia (based on internationally known original approved uses; no Singapore/local license record available in this pack) |
| Predicted New Indication | Myeloid Leukemia (Acute Myeloid Leukemia, AML) |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (MOA is flagged as a data gap). Based on known pharmacology, lenalidomide binds cereblon (CRBN), a substrate receptor of the CRL4 E3 ubiquitin ligase complex, and redirects it to ubiquitinate and degrade the transcription factors IKZF1 (Ikaros) and IKZF3 (Aiolos). This produces anti-angiogenic, immunomodulatory, and direct anti-clonal effects that underlie its efficacy in myeloid and lymphoid malignancies, and it is frequently combined with hypomethylating agents such as azacitidine in high-risk MDS/AML regimens.

MDS and AML sit on the same disease continuum — a substantial proportion of MDS cases transform into AML, and both are clonal myeloid bone-marrow disorders sharing overlapping cytogenetic drivers (including 5q abnormalities). This biological continuity is the basis for TxGNN's high prediction score: a drug active in one myeloid clonal disorder is mechanistically plausible in the other, and this is reflected in numerous combination trials (e.g., with azacitidine, cytarabine, or MEC chemotherapy) conducted in relapsed/refractory AML and high-risk MDS/AML populations.

However, this mechanistic link is genuinely double-edged and must be treated as the central research question rather than a simple positive signal. The same CRBN-mediated mechanism that gives lenalidomide anti-clonal activity has also been directly implicated in *promoting* clonal evolution: PMID 35512188 (Blood, 2022) reports that lenalidomide is associated with development of TP53-mutated therapy-related myeloid neoplasms, and a Japanese post-marketing surveillance study (NCT02921815) was specifically designed to track transformation from del(5q) MDS to AML in patients on Revlimid. Any further development of lenalidomide for AML would need to explicitly reconcile this therapeutic-potential-versus-leukemogenic-risk duality, likely through TP53/cytogenetic-status-stratified trial design.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | Completed | 41 | MEC chemotherapy (mitoxantrone/etoposide/cytarabine) + lenalidomide in relapsed/refractory AML; direct disease-specific evidence. |
| [NCT02921815](https://clinicaltrials.gov/study/NCT02921815) | N/A | Completed | 84 | Japanese post-marketing surveillance tracking transformation of del(5q) MDS to AML in patients on Revlimid — a safety/monitoring study, not an efficacy trial. |
| [NCT00867308](https://clinicaltrials.gov/study/NCT00867308) | Phase 2 | Terminated | 32 | High-dose lenalidomide in MDS and AML with trilineage dysplasia; terminated early, limiting evidence strength. |
| [NCT01442714](https://clinicaltrials.gov/study/NCT01442714) | Phase 2 | Terminated | 33 | Azacitidine + lenalidomide in elderly, previously treated AML/high-risk MDS (VIREL2 trial); terminated early. |
| [NCT00885508](https://clinicaltrials.gov/study/NCT00885508) | Phase 2 | Unknown | 85 | Escalating-dose chemotherapy + lenalidomide in intermediate-2/high-risk MDS and AML with del(5q); completion status unconfirmed. |
| [NCT00179621](https://clinicaltrials.gov/study/NCT00179621) | Phase 3 | Completed | 205 | Randomized, double-blind, placebo-controlled trial of lenalidomide doses in RBC transfusion-dependent del(5q) MDS — the pivotal MDS-004 trial; disease label here is a mismatch (this is the established MDS indication, not AML). |
| [NCT01038635](https://clinicaltrials.gov/study/NCT01038635) | Phase 1/2 | Completed | 94 | Azacitidine + lenalidomide combination dose-finding and efficacy study in high-risk MDS and AML. |
| [NCT01522976](https://clinicaltrials.gov/study/NCT01522976) | Phase 2 | Active, not recruiting | 282 | Randomized Phase 2/3 comparing azacitidine ± lenalidomide or vorinostat in higher-risk MDS and CMML. |
| [NCT01556477](https://clinicaltrials.gov/study/NCT01556477) | Phase 2 | Unknown | 72 | Randomized open-label study of azacitidine alone vs. + lenalidomide in high-risk myeloid disease (MDS/AML) with del(5q) karyotype. |
| [NCT02905552](https://clinicaltrials.gov/study/NCT02905552) | N/A | Unknown | 320 | Case-control study of infection risk factors in MDS (background epidemiology, not a treatment trial). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | Meta-analysis | Hematology (Amsterdam) | Systematic review/meta-analysis of efficacy and adverse events of azacitidine + lenalidomide in AML, MDS, and CMML. |
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | Systematic Review/Meta-analysis | Cancer Management and Research | Efficacy and safety of lenalidomide for AML treatment; notes that benefit in AML (versus del(5q) MDS) remains controversial. |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | American Journal of Hematology | 2023 update on MDS diagnosis, risk stratification, and management, including transformation risk to AML. |
| [24656536](https://pubmed.ncbi.nlm.nih.gov/24656536/) | 2014 | Review | Lancet | Comprehensive review of MDS pathophysiology and progression to AML in about one-third of cases. |
| [35320468](https://pubmed.ncbi.nlm.nih.gov/35320468/) | 2022 | Review | Current Treatment Options in Oncology | New approaches to MDS treatment, covering risk-stratified therapeutic strategies. |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | Cohort (safety signal) | Blood | Lenalidomide identified as promoting development of TP53-mutated therapy-related myeloid neoplasms — key safety caveat for this indication. |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Phase 1/2 Cohort | Leukemia | Reviews rationale and early trial data for combining azacitidine and lenalidomide in MDS/AML. |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Cohort | Haematologica | Azacitidine + lenalidomide + donor lymphocyte infusion for post-transplant relapse of MDS/AML/CMML (Azalena trial). |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Cohort | Bone Marrow Transplantation | Safety and tolerability of lenalidomide maintenance in post-transplant AML and high-risk MDS. |
| [37874917](https://pubmed.ncbi.nlm.nih.gov/37874917/) | 2023 | Review | Blood | Clinical decision-making framework for MDS treatment across risk categories. |

---

## Singapore Market Information

Lenalidomide currently has **no registered product license in Singapore** (0 registrations; market status: not marketed) according to this evidence pack. No dosage form, brand name, or approved indication text is available to summarize in this section.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — immunomodulatory imide drug (IMiD), a CRBN/E3 ubiquitin ligase modulator; not a conventional cytotoxic chemotherapy agent |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are the most common dose-limiting toxicities across MDS/AML/MM combination regimens seen in the trials above |
| Emetogenicity Classification | Low — oral IMiD with minimal emetogenic potential compared with classic cytotoxic chemotherapy |
| Monitoring Items | Complete blood count with differential (frequent monitoring, especially during early treatment cycles), renal function (dose adjustment needed with renal impairment), pregnancy status (teratogenicity risk), and thromboembolism risk assessment |
| Handling Protection | Special precautions required — lenalidomide is a thalidomide analogue with teratogenic potential and is typically distributed under restricted-access safety programs; institutional hazardous-drug handling precautions should still be followed even though it is an oral (non-infusional) agent |

---

## Safety Considerations

Please refer to the package insert for safety information. No specific key warnings, contraindications, or drug–drug interaction data were available in this evidence pack (the DDI query returned no matches, and warning/contraindication fields were marked as data gaps).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is a genuine Phase 2 signal for lenalidomide combined with chemotherapy in relapsed/refractory AML (NCT03118466, completed, n=41), and a broader body of trials supports its use in combination regimens for high-risk MDS/AML. However, the same mechanistic pathway (CRBN-mediated) that provides anti-clonal activity is separately documented to promote TP53-mutated therapy-related myeloid neoplasms (PMID 35512188), and a dedicated post-marketing surveillance study exists specifically to monitor MDS-to-AML transformation risk on this drug (NCT02921815). This dual-edged mechanism means the evidence base cannot yet support a straightforward "proceed" decision — it must first be resolved as a defined research question.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) documentation from DrugBank or the manufacturer
- TFDA/HSA package insert data for warnings, contraindications, and drug interactions (currently all data gaps)
- A biomarker-stratified analysis (e.g., by TP53 mutation status and cytogenetic risk group) distinguishing patients likely to benefit from lenalidomide-based AML therapy from those at elevated risk of lenalidomide-associated secondary/therapy-related myeloid neoplasm
- Confirmation of Singapore/regional regulatory pathway feasibility, given the drug currently has zero local registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

