---
layout: default
title: Zanubrutinib
parent: Low Evidence (L5)
nav_order: 1072
evidence_level: L5
indication_count: 10
---

# Zanubrutinib
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

# Zanubrutinib: From B-Cell Malignancies to Myeloid Leukemia

## One-Sentence Summary

Zanubrutinib is an oral BTK (Bruton tyrosine kinase) inhibitor, used mainly for B-cell malignancies such as mantle cell lymphoma and chronic lymphocytic leukemia.
The TxGNN model predicts it may be effective for **myeloid leukemia**, but this is a graph-based prediction only.
The two registered trials and nine publications retrieved do not test zanubrutinib in myeloid leukemia, so **direct evidence is absent**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | B-cell malignancies (from the published literature; the Singapore label text is not in the record) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Zanubrutinib is a selective, covalent BTK inhibitor. BTK is central to B-cell receptor signaling, which is why the drug works in B-cell cancers. BTK is also expressed in some myeloid blasts and contributes to their survival signaling, so a preclinical rationale exists.

That link is weak. No data show zanubrutinib activity in myeloid leukemia. All retrieved zanubrutinib literature concerns lymphoid disease (CLL/SLL, Waldenström's macroglobulinemia, mantle cell lymphoma). The high TxGNN score (rank 5,133) should be read as network proximity, not as proof of efficacy.

## Clinical Trial Evidence

Neither registered trial tests zanubrutinib as the study drug in myeloid leukemia. Both were graded C (class-level context only).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Tests PRT2527 (a CDK9 inhibitor) alone or combined with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies. The study drug is not zanubrutinib. |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | Terminated | 45 | Tests CG-806 (luxeptinib, a multi-kinase inhibitor with BTK/FLT3 activity) in relapsed/refractory AML or higher-risk MDS. It is a different molecule, and the trial was terminated. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 5-year follow-up: zanubrutinib vs bendamustine + rituximab in untreated CLL/SLL (lymphoid disease) |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | Zanubrutinib is well tolerated and effective in CLL/SLL patients intolerant of ibrutinib or acalabrutinib |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Cohort | Blood Adv | Pooled analysis in CLL/SLL with del(17p) and/or TP53 mutation (N = 301) |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study in B-cell malignancies intolerant of prior BTK inhibitors |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Review of tyrosine kinase inhibitors in chronic leukemias (CML and CLL) |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Managing Waldenström's macroglobulinemia with BTK inhibitors |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | Hepatitis B reactivation in patients on BTK inhibitors, including zanubrutinib |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anticancer Agents Med Chem | Synthetic chemistry of FDA-approved anticancer drugs; no clinical evidence |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | Rare coexistence of Waldenström's macroglobulinemia and B-ALL; not evidence of efficacy |

All of these concern lymphoid disease or general topics. None reports zanubrutinib activity in myeloid leukemia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16341P | BRUKINSA™ CAPSULE 80MG | Capsule | Not stated in the available record (manufacturer listed: Catalent CTS (Kansas City), LLC, primary packager) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BTK inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No warnings or contraindications were captured, and no drug interactions were found.

- **Literature signal**: A published review reports hepatitis B virus reactivation in patients receiving BTK inhibitors, including zanubrutinib ([PMID 37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/)).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The myeloid leukemia prediction rests on a model score alone (L5). The retrieved trials test other drugs, and the literature covers only lymphoid disease.

**To proceed, the following is needed:**
- Preclinical or early clinical data for zanubrutinib in myeloid leukemia (AML/CML)
- HSA package insert warnings and contraindications, to allow safety screening
- Confirmation of the original approved indications and the detailed mechanism of action
- Separate review of rank 9 (non-Hodgkin lymphoma, L2, Proceed with Guardrails). Its evidence covers sporadic lymphoma subtypes that may already be label-covered, so it may not be true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

