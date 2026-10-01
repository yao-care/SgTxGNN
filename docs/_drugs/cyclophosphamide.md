---
layout: default
title: Cyclophosphamide
parent: Low Evidence (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Cyclophosphamide
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

# Cyclophosphamide: From Established Oncology Use to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy drug marketed in Singapore, but its original approved indication is not recorded in the registry data.
The TxGNN model predicts it may be useful for **myeloid leukemia**. The search returned **50 clinical trials** and **20 publications**, but most of this evidence is indirect: cyclophosphamide appears mainly as a transplant conditioning or post-transplant agent rather than as a stand-alone antileukemic therapy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (all Singapore license entries have empty indication text) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L2 (as scored in the Evidence Pack; indirect, see below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Cyclophosphamide is a well-known prodrug. The liver enzyme CYP2B6 converts it to phosphoramide mustard, which cross-links DNA and kills rapidly dividing cells, including leukemic blasts.

In the retrieved evidence, cyclophosphamide's role in myeloid leukemia is mostly as a **transplant backbone**:
- It is the "Cy" in busulfan-cyclophosphamide (BuCy) myeloablative conditioning before allogeneic stem-cell transplant.
- It is the "Cy" in fludarabine-cyclophosphamide (Flu/Cy) reduced-intensity conditioning.
- It is used as post-transplant cyclophosphamide (PTCy), which depletes alloreactive T cells to prevent graft-versus-host disease.

The high TxGNN score is consistent with this pattern, but it is not independent confirmation. Evidence for cyclophosphamide as a stand-alone antileukemic drug in myeloid disease is limited.

## Clinical Trial Evidence

The record lists 50 trials. The 10 most relevant are shown below. Most are transplant studies in which cyclophosphamide is one component, so its individual contribution cannot be separated.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002549](https://clinicaltrials.gov/study/NCT00002549) | Phase 3 | Unknown | 1520 | AML 10 protocol: induction and consolidation chemotherapy followed by marrow transplant. The arms shown are not clearly cyclophosphamide-based. |
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Venetoclax + azacitidine, then modified BuCy conditioning, for high-risk MDS and high-risk or relapsed/refractory AML. |
| [NCT05598593](https://clinicaltrials.gov/study/NCT05598593) | Phase 2 | Unknown | 70 | Modified TBF conditioning before allogeneic transplant for T-ALL/lymphoblastic lymphoma. Cyclophosphamide is likely part of the regimen. |
| [NCT05126849](https://clinicaltrials.gov/study/NCT05126849) | Phase 2 | Recruiting | 31 | Haploidentical transplant with PTCy. The title focuses on refractory aplastic anemia, so the myeloid link is partial. |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor marrow transplant with PTCy, sirolimus and MMF for hematologic malignancies. |
| [NCT03314974](https://clinicaltrials.gov/study/NCT03314974) | Phase 2 | Recruiting | 300 | Myeloablative allogeneic transplant followed by PTCy, tacrolimus and MMF for GVHD prophylaxis. |
| [NCT00002502](https://clinicaltrials.gov/study/NCT00002502) | Phase 2 | Completed | N/A | Busulfan + cyclophosphamide cytoreduction before marrow transplant in acute and chronic leukemias and MDS. |
| [NCT04888741](https://clinicaltrials.gov/study/NCT04888741) | Phase 2 | Unknown | 400 | Thymoglobulin vs PTCy-based GVHD prophylaxis after unrelated donor transplant. |
| [NCT03699475](https://clinicaltrials.gov/study/NCT03699475) | Phase 2/3 | Terminated | 1 | Rivogenlecleucel vs PTCy after haploidentical transplant in AML/MDS. Terminated after one patient, so no usable data. |
| [NCT03007147](https://clinicaltrials.gov/study/NCT03007147) | Phase 3 | Active, not recruiting | 475 | Imatinib with two chemotherapy backbones in Ph+ ALL. This is a lymphoid, not myeloid, leukemia, so it is indirect support only. |

**Evidence level note:** None of the Phase 3 trials above is both completed and cyclophosphamide-specific in myeloid leukemia. The L2 grade therefore rests on indirect support, not on a direct randomized test.

## Literature Evidence

No randomized controlled trial was found for myeloid leukemia. The 10 most relevant publications, mostly cohort studies and reviews, are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28883081](https://pubmed.ncbi.nlm.nih.gov/28883081/) | 2017 | Position statement | Haematologica | EBMT position on haploidentical transplant for adult AML, covering GVHD prophylaxis and conditioning. |
| [32857869](https://pubmed.ncbi.nlm.nih.gov/32857869/) | 2020 | Review | Am J Hematol | NK-cell alloreactivity in AML in the post-transplant cyclophosphamide era. |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Cohort | Bone Marrow Transplant | 1,823 AML patients in first remission given PTCy. Conditioning intensity was compared by cytogenetic and molecular risk. |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | BuCy vs fludarabine-busulfan conditioning for AML. FluBu appears similarly effective with less toxicity. |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Cohort | Eur J Haematol | Myeloablative vs reduced-intensity conditioning in adults under 65 with AML receiving ATG and PTCy. |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | Prognostic factors in haploidentical transplant with PTCy for AML. |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort | Int J Mol Sci | PTCy after matched-donor transplant in pediatric AML. |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Cy/Flu nonmyeloablative vs myeloablative transplant in 165 AML patients. Survival was not different in univariate analysis. |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | Cohort | Pediatr Hematol Oncol | Clofarabine + cyclophosphamide + etoposide in 17 children with relapsed/refractory AML. 7 (41%) responded. |
| [25612567](https://pubmed.ncbi.nlm.nih.gov/25612567/) | 2015 | Case report | Int J Clin Pharm | Secondary AML arising early after cyclophosphamide treatment (a safety signal, not efficacy). |

## Singapore Market Information

The registry record contains no approved-indication text for any of these licenses.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00929P | ENDOXAN TABLET 50 mg | Sugar-coated tablet | Not provided in the record |
| SIN01747P | ENDOXAN FOR INJECTION 1 g/vial | Powder for injection solution | Not provided in the record |
| SIN01748P | ENDOXAN FOR INJECTION 500 mg/vial | Powder for injection solution | Not provided in the record |
| SIN00930P | ENDOXAN FOR INJECTION 200 mg/vial | Powder for injection solution | Not provided in the record |
| SIN10355P | CYCRAM FOR INJECTION 1 g/vial | Powder for injection solution | Not provided in the record |

## Cytotoxicity

The Evidence Pack contains no toxicity data. The entries below reflect general knowledge of the drug class and should be confirmed against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard prodrug) |
| Myelosuppression Risk | High (leukopenia and neutropenia are expected, especially at conditioning doses) |
| Emetogenicity Classification | Moderate (higher at high intravenous doses) |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, urinalysis for bladder toxicity |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. The registry warnings and contraindications are missing from the Evidence Pack, and no drug-interaction records were found.

The literature does report that cyclophosphamide is associated with therapy-related AML ([PMID 25612567](https://pubmed.ncbi.nlm.nih.gov/25612567/)). This is a relevant theoretical concern when treating myeloid disease.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide is established in transplant conditioning and PTCy-based GVHD prophylaxis for myeloid leukemia, supported by many Phase 2 trials and cohort studies. The prediction is therefore plausible. However, no direct randomized evidence isolates its stand-alone antileukemic benefit, and the safety data are missing.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications. This is a blocking gap and must be resolved before safety screening.
- The Singapore-approved indication text for each license, to establish the original indication.
- DrugBank mechanism-of-action data to complete the mechanistic analysis.
- A defined use scenario (conditioning, PTCy, or cytoreduction) so the evidence can be matched to a specific clinical role.
- A monitoring plan for myelosuppression, infection and secondary myeloid neoplasm risk.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

