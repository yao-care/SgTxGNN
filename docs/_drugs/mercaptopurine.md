---
layout: default
title: Mercaptopurine
parent: Low Evidence (L5)
nav_order: 645
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine is an oral purine antimetabolite, long used as a backbone of maintenance chemotherapy for acute lymphoblastic leukemia (ALL).
The TxGNN model predicts it may be effective for **myeloid leukemia** (score 99.94%).
The evidence pack retrieved **29 registered trials** and **20 publications** for this indication, but most trials are combination regimens in which mercaptopurine's role is not confirmed, so the support is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence record. Established use is ALL maintenance therapy (per the ALL entries in this evidence pack) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 (as assigned in the evidence pack; combination-regimen evidence, not single-agent) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on general pharmacology, mercaptopurine is a purine antimetabolite. It is converted by HGPRT into thioguanine nucleotides, which are incorporated into DNA/RNA and inhibit de novo purine synthesis. This is cytotoxic to rapidly dividing cells, including myeloid blasts.

Its efficacy in lymphoid leukemia (ALL) is well established. Myeloid and lymphoid leukemias are both proliferative blood cancers, so an antimetabolite mechanism could plausibly apply. Mercaptopurine also already appears in several myeloid regimens:
- **Acute promyelocytic leukemia (APL):** ATRA + methotrexate + mercaptopurine maintenance (AIDA-type protocols).
- **AML:** older induction regimens with mercaptopurine, cytarabine and daunorubicin, mostly from Japanese groups.

Two cautions apply. First, this is combination-regimen evidence, and trial titles are often truncated, so mercaptopurine arms need verification. Second, outside APL maintenance its role is unproven. A randomized trial (PMID 10497848) found no benefit from adding etoposide to a mercaptopurine-containing AML induction regimen.

The pack also ranks ALL (rank 10) and precursor lymphoblastic leukemia/lymphoma (rank 9) as predictions. These are established uses, not new repurposing.

---

## Clinical Trial Evidence

The 10 most relevant of the 29 retrieved trials are shown, prioritizing those that explicitly name mercaptopurine or 6-MP/methotrexate maintenance.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Randomized APL trial (tretinoin + chemotherapy ± arsenic trioxide), then maintenance with intermittent tretinoin vs tretinoin + mercaptopurine + methotrexate. Most direct randomized signal |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Two doses of gemtuzumab vs two-year ATRA + chemotherapy maintenance in intermediate/high-risk APL. Maintenance chemotherapy is classically 6-MP + MTX (needs verification) |
| [NCT00599937](https://clinicaltrials.gov/study/NCT00599937) | Phase 3 | Completed | 576 | Timing of chemotherapy with or after ATRA and the role of maintenance therapy in APL |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Unknown | 750 | ATRA + idarubicin with intensive consolidation, then randomized maintenance by minimal residual disease in APL. Mercaptopurine role plausible but unverified |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | Not applicable | Unknown | 1068 | AIDA protocol testing intermittent ATRA vs standard methotrexate + 6-mercaptopurine maintenance in APL |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | Not reported | AIDA regimen in APL with ATRA + methotrexate + mercaptopurine maintenance and salvage |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA2005 risk-adapted APL protocol with low-dose methotrexate + mercaptopurine maintenance |
| [NCT00180128](https://clinicaltrials.gov/study/NCT00180128) | Phase 4 | Unknown | 80 | AIDA2000 risk-adapted APL therapy with two years of 6-MP, methotrexate and ATRA maintenance |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | Venetoclax + 6-mercaptopurine in relapsed/refractory AML (ApoAML) |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | Hydroxyurea + valproic acid, or 6-MP + valproic acid, in AML/high-risk MDS patients unfit for standard therapy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematol | JALSG-AML92: adding etoposide to daunorubicin, behenoyl cytarabine and 6-MP gave no benefit in adult AML induction |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | Randomized trial | Cancer Chemother Pharmacol | Japanese nationwide study of 6-MP-containing regimens: complete remission 63.7% with daunorubicin vs 53.9% with aclarubicin (P = 0.0587) |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Cohort | J Korean Med Sci | Two years of oral 6-MP + methotrexate maintenance in transplant-ineligible AML. Leukemia-free and overall survival were assessed; results are not shown in the data provided |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Pilot trial | Cancer Invest | High-dose 6-MP followed by intermediate-dose cytarabine in first remission of pediatric AML. Feasibility study (17 children) |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Clinical trial | Int J Hematol | Behenoyl cytarabine + daunorubicin + 6-MP induction in 41 adults with AML; 71% achieved complete remission |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Clinical study | Cancer | Four-drug protocol including mercaptopurine or thioguanine in 18 children with AML; 78% initial remission rate, median survival 7 months |
| [4518586](https://pubmed.ncbi.nlm.nih.gov/4518586/) | 1973 | Clinical study | Cancer | Cytarabine combined with 6-MP in adult AML (no abstract available) |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Case series | Minn Med | Historical report of 6-MP and cyclophosphamide in AML (no abstract available) |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Case series | Blood | Three cases of juvenile chronic myeloid leukemia responded to sequential subcutaneous cytarabine and oral mercaptopurine. Likely symptom control rather than survival benefit |
| [28835099](https://pubmed.ncbi.nlm.nih.gov/28835099/) | 2017 | Preclinical | Biomacromolecules | CD44-targeted hyaluronic acid–6-MP nanoprodrug designed for AML. Laboratory work only |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN10810P | PURINETONE TABLETS 50 mg | Tablet (oral) | Korea United Pharmaceutical Inc |

The approved-indication text is not included in the registration record, so it cannot be confirmed whether myeloid leukemia is covered.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (purine antimetabolite, thiopurine class) |
| Myelosuppression Risk | Medium to High. Myelosuppression and neutropenia are dose-limiting, and NUDT15/TPMT variants greatly increase the risk in the retrieved literature |
| Emetogenicity Classification | Low (general classification for oral mercaptopurine; not from the evidence pack) |
| Monitoring Items | CBC with differential, liver function, blood glucose (hypoglycemia has been reported), TPMT/NUDT15 genotype before dosing |
| Handling Protection | Must follow cytotoxic drug handling regulations |

DrugBank toxicity data were not supplied. Please refer to the package insert warnings and precautions.

---

## Safety Considerations

Structured safety data (warnings, contraindications, drug interactions) were not available. Please refer to the package insert for safety information.

The retrieved literature raises these signals:
- **Pharmacogenomics:** TPMT, NUDT15 and ITPA variants are linked to mercaptopurine intolerance and severe neutropenia, including in Asian cohorts (Taiwan, China, Vietnam, Indonesia).
- **Allopurinol:** it changes mercaptopurine metabolism and should be co-administered only under specialist management.
- **Hypoglycemia:** rare but serious cases are reported during maintenance therapy.
- **Secondary neoplasms:** thiopurine exposure is associated with lymphoproliferative disorders in inflammatory bowel disease, and autoimmune disease therapy with therapy-related myeloid neoplasms (PMID 28152123).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mercaptopurine is already part of standard APL maintenance and older AML regimens, and several completed Phase 3 trials (mainly APL) include it in combination. However, no single-agent evidence exists, the mercaptopurine arms are unverified for most trials, and the Singapore indication text is unavailable. The evidence supports further evaluation, not routine use.

**To proceed, the following is needed:**
- Verify the mercaptopurine arms in the listed trial protocols (especially NCT00962767, NCT00002701, NCT00599937).
- Obtain the HSA package insert to fill the warnings, contraindications and approved-indication gaps.
- Confirm the mechanism of action from DrugBank.
- Set guardrails: TPMT/NUDT15 genotype-guided dosing, CBC and liver monitoring, allopurinol interaction management, and adherence support.
- Confirm whether use in myeloid leukemia would be on-label in Singapore.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

