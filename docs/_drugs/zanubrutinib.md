---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 1072
evidence_level: L5
indication_count: 10
---

# Zanubrutinib
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

# Zanubrutinib: From B-Cell Malignancies to Myeloid Leukemia

## One-Sentence Summary

> Zanubrutinib is a second-generation Bruton's tyrosine kinase (BTK) inhibitor originally developed for B-cell malignancies (e.g., mantle cell lymphoma, CLL/SLL).
> The TxGNN model assigns its highest computational score to **Myeloid Leukemia**, but the **2 clinical trials** and **9 publications** identified for this pairing are almost entirely about other drugs or other B-cell lymphoid diseases — not zanubrutinib treating myeloid leukemia — suggesting this is likely a knowledge-graph artifact rather than a genuine signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (drug unmarketed); globally known for B-cell malignancies (mantle cell lymphoma, CLL/SLL, marginal zone lymphoma, Waldenström macroglobulinemia) per literature evidence |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Zanubrutinib inhibits BTK, blocking B-cell receptor (BCR) signaling downstream. This pathway is the core disease driver in B-cell lymphoid malignancies (CLL/SLL, MCL, MZL, FL, WM) — but BTK is not established as a primary oncogenic driver in myeloid leukemia biology.

Of the two clinical trials returned for this pairing, neither actually tests zanubrutinib as the investigational agent: NCT05665530 studies PRT2527 (a CDK9 inhibitor) alone or combined with zanubrutinib/venetoclax, and NCT04477291 studies CG-806 (luxeptinib), a terminated trial. The nine literature citations overwhelmingly describe zanubrutinib's efficacy in CLL/SLL, WM, and B-ALL/WM overlap case reports — not myeloid leukemia.

Given the mechanistic mismatch and the absence of any study directly evaluating zanubrutinib in myeloid leukemia, this prediction should be treated as a high-scoring but low-specificity model artifact rather than a validated repurposing hypothesis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | Completed | 86 | Dose-escalation study of PRT2527 (CDK9 inhibitor) as monotherapy and combined with zanubrutinib or venetoclax in relapsed/refractory hematologic malignancies; zanubrutinib is a combination partner, not the primary study drug. |
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | Terminated | 45 | Evaluated CG-806 (luxeptinib) in relapsed/refractory AML/high-risk MDS; unrelated to zanubrutinib and terminated before completion. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | 5-year follow-up update of SEQUOIA trial: zanubrutinib vs bendamustine+rituximab in treatment-naïve CLL/SLL (not myeloid leukemia). |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Advances | Updated safety/efficacy of zanubrutinib in CLL/SLL patients intolerant of ibrutinib/acalabrutinib. |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | Pooled analysis | Blood Advances | Pooled SEQUOIA/ALPINE analysis of zanubrutinib in del(17p)/TP53-mutated CLL/SLL (N=301). |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Cohort | Lancet Haematol | Phase 2 single-arm study of zanubrutinib in B-cell malignancy patients intolerant of prior BTK inhibitors. |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | Review of tyrosine kinase inhibitor therapy in chronic leukemias (CML, CLL); BTK inhibitors discussed in CLL context only. |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | Review of BTK inhibitors, including zanubrutinib, in Waldenström macroglobulinemia management. |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | Case report of coexisting Waldenström macroglobulinemia and B-cell ALL with KMT2D/MECOM mutations; not treatment-focused. |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Case series | Clin Lymphoma Myeloma Leuk | HBV reactivation reported in patients receiving BTK inhibitors, including zanubrutinib, for B-cell malignancies. |
| [38288815](https://pubmed.ncbi.nlm.nih.gov/38288815/) | 2024 | Review | Anti-Cancer Agents Med Chem | Broad synthetic-chemistry review of FDA-approved anticancer drugs (2018–2021); zanubrutinib mentioned only as one of 56 listed agents. |

## Singapore Market Information

Zanubrutinib is not currently registered or marketed in Singapore. No HSA license records are available in the evidence pack.

## Cytotoxicity

Zanubrutinib is an antineoplastic agent (BTK inhibitor used in hematologic malignancies), so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (Bruton's tyrosine kinase inhibitor; not conventional cytotoxic chemotherapy) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between BTK inhibition and myeloid leukemia is not established, and none of the identified trials or literature directly evaluate zanubrutinib in myeloid leukemia — the top-ranked TxGNN signal is not supported by drug-specific evidence.

**To proceed, the following is needed:**
- Preclinical/mechanistic studies confirming a role for BTK signaling in myeloid leukemia pathogenesis
- A dedicated clinical trial testing zanubrutinib (not combination partner drugs) in myeloid leukemia
- Drug label/MOA and safety data (currently flagged as Data Gaps: TFDA/HSA labeling, DrugBank MOA)
- Singapore (HSA) registration status, since the drug is currently unmarketed there

---

**Note on portfolio prioritization:** Among the 10 predicted indications in this evidence pack, rank #9 ("lymphoma, non-Hodgkin, familial" — effectively B-cell non-Hodgkin lymphoma subtypes) has substantially stronger support: evidence level **L1**, multiple completed Phase 3 RCTs directly testing zanubrutinib (e.g., ALPINE/SEQUOIA-related, ROSEWOOD, MAGNOLIA), and a "Proceed with Guardrails" recommendation. If the goal is identifying a viable repurposing candidate for this drug, that indication — not myeloid leukemia — merits evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

