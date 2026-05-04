---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Baricitinib
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

# Baricitinib: From Rheumatoid Arthritis to Myeloid Leukemia

## One-Sentence Summary

Baricitinib is a selective JAK1/2 inhibitor approved globally for rheumatoid arthritis, atopic dermatitis, and COVID-19, but not currently registered in Singapore.
This multi-indication TxGNN evaluation identified 10 novel repurposing candidates; **Myeloid Leukemia** (specifically GvHD prevention in the allogeneic HSCT setting) represents the most evidence-supported direction,
backed by **1 active Phase 2/3 clinical trial** and **4 publications** — while the highest TxGNN-scored predictions involve rare congenital syndromes with no supporting data.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis; atopic dermatitis; COVID-19 (approved in US/EU/Japan; **not registered in Singapore**) |
| Predicted New Indication (Best Evidence) | Myeloid Leukemia — GvHD prevention post-allogeneic HSCT |
| TxGNN Prediction Score | 91.01% (Rank 6 of 10; top-ranked predictions are model-only, L5) |
| Evidence Level | L2 (1 active Phase 2/3 trial) |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question for myeloid leukemia/HSCT context) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Baricitinib selectively inhibits Janus kinase 1 and 2 (JAK1/2), blocking downstream STAT signalling activated by pro-inflammatory cytokines including IL-6, IFN-γ, IL-2, and GM-CSF. This pathway is central to both immune-mediated diseases (its approved uses) and the cytokine storm driving graft-versus-host disease (GvHD) after allogeneic haematopoietic stem cell transplantation (allo-HSCT).

The mechanistic link to myeloid leukemia is indirect but clinically grounded: baricitinib would not target leukaemia cells directly, but rather modulate post-transplant immune activation. Donor T-cell alloreactivity in GvHD relies on JAK-STAT cascades — exactly the signalling axis baricitinib suppresses. Critically, ruxolitinib, a closely related JAK1/2 inhibitor in the same drug class, has received FDA approval for both steroid-refractory acute and chronic GvHD, providing strong mechanistic precedent and regulatory proof-of-concept.

The active Phase 2/3 trial (NCT06475820) directly tests baricitinib as part of a multi-agent GvHD prevention regimen in children and young adults with haematological malignancies (including myeloid) undergoing myeloablative HSCT — confirming this is an active and scientifically grounded research question, not merely a model artefact.

---

## All Predicted Indications — Overview

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.94% | L5 | Hold |
| 2 | Brachydactyly-syndactyly syndrome | 99.94% | L5 | Hold |
| 3 | Indolent plasma cell myeloma | 93.31% | L5 | Hold |
| 4 | WHIM syndrome | 93.12% | L5 | Hold |
| 5 | Plasma cell myeloma | 91.83% | L4 | Hold |
| 6 | **Myeloid leukemia** | **91.01%** | **L2** | **Research Question** |
| 7 | Meester-Loeys syndrome | 88.21% | L5 | Hold |
| 8 | Ganglioneuroblastoma | 87.59% | L5 | Hold |
| 9 | Heparin cofactor 2 deficiency | 86.31% | L5 | Hold |
| 10 | Vertebral anomalies and variable endocrine and T-cell dysfunction | 84.68% | L5 | Hold |

> **Why do ranks 1–4 score so high yet have no evidence?** High TxGNN scores for rare congenital syndromes (ranks 1, 2, 7, 8, 9, 10) likely reflect structural similarity within the cytokine/signalling network topology of the knowledge graph, not disease-specific biology. These conditions are caused by developmental genetic defects (e.g., structural eye/limb malformations, BGN mutations) where JAK inhibition has no established therapeutic rationale. They are classified as knowledge-graph artefacts rather than actionable repurposing signals.

> **Plasma cell myeloma (rank 5)** carries a biologically plausible mechanistic link (IL-6 → JAK1/2 → STAT3 is a validated survival axis in myeloma cells), and is supported by one case report. However, it remains at L4 pending dedicated trial evidence.

> **WHIM syndrome (rank 4)** has a secondary mechanistic connection via CXCR4 → JAK/STAT, but the established therapeutic target is CXCR4 directly (plerixafor), making JAK inhibition an unvalidated secondary pathway.

---

## Clinical Trial Evidence — Myeloid Leukemia

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06475820](https://clinicaltrials.gov/study/NCT06475820) | Phase 2/3 | Active, Not Recruiting | 150 | GvHD prevention using post-transplantation cyclophosphamide combined with abatacept, vedolizumab, and baricitinib in children and young adults with haematological malignancies (including myeloid) following myeloablative HSCT from unrelated or haploidentical donors; completion expected April 2027 |

---

## Literature Evidence — Myeloid Leukemia & Haematological Malignancies

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34730109](https://pubmed.ncbi.nlm.nih.gov/34730109/) | 2021 | Preclinical/Translational | J Clinical Investigation | Antibody-drug conjugates combined with JAK inhibitors enable MHC-mismatched allogeneic HSCT in leukaemia models — direct mechanistic support for baricitinib in the transplant setting |
| [36569952](https://pubmed.ncbi.nlm.nih.gov/36569952/) | 2022 | Narrative Review | Frontiers in Immunology | Review of BCL-2 and JAK1/2 inhibitor repurposing in viral and immune dysregulation contexts; discusses baricitinib mechanism broadly applicable to haematological immune modulation |
| [34856779](https://pubmed.ncbi.nlm.nih.gov/34856779/) | 2021 | Case Report | Minerva Medica | Concurrent management of critical COVID-19 and newly diagnosed high-risk multiple myeloma with baricitinib; demonstrates real-world feasibility of baricitinib in a haematological malignancy setting |
| [35442720](https://pubmed.ncbi.nlm.nih.gov/35442720/) | 2022 | Methodology Study | JCO Precision Oncology | Nanopore mRNA sequencing for acute leukaemia subtype classification in low-resource settings — background context on leukaemia disease classification, indirect relevance |
| [31816725](https://pubmed.ncbi.nlm.nih.gov/31816725/) | 2020 | PK/Analytical | Talanta | Validated LC-MS/MS method for therapeutic drug monitoring of 11 kinase inhibitors including agents used in CML and leukaemia — supports TDM planning for baricitinib in haematological malignancy populations |

---

## Singapore Market Information

Baricitinib is **not currently registered** with the Health Sciences Authority (HSA) of Singapore. No product authorisations are on record.

For reference, baricitinib (Olumiant®, Eli Lilly) holds regulatory approvals in the following markets:

| Market | Approved Indications |
|--------|---------------------|
| US (FDA) | Rheumatoid arthritis, atopic dermatitis, alopecia areata, COVID-19 (hospitalised adults) |
| EU (EMA) | Rheumatoid arthritis, atopic dermatitis, COVID-19 |
| Japan (PMDA) | Rheumatoid arthritis, atopic dermatitis |

Any investigational use in Singapore would require HSA authorisation and appropriate ethical review.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important**: No Singapore HSA or TFDA package insert data, contraindications, or drug interaction information were available in this Evidence Pack (Data Gaps DG001, DG002). Clinicians should be aware that baricitinib carries an FDA **class-wide JAK inhibitor Boxed Warning** covering serious infections (including opportunistic infections and tuberculosis), malignancy risk, thrombosis (DVT/PE/arterial), and major adverse cardiovascular events (MACE). These risks are of heightened relevance in the immunocompromised haematological malignancy and HSCT population. Full prescribing information should be consulted prior to any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The majority of TxGNN predictions (9 of 10) are either rare congenital syndromes without mechanistic basis or early-stage oncological predictions without trial evidence; none currently meet criteria for immediate clinical advancement. The myeloid leukemia / HSCT-GvHD prevention indication (rank 6, L2) is the sole actionable research question, supported by a running Phase 2/3 trial — but no completed efficacy data are yet available.

**To proceed, the following is needed:**

- **Await NCT06475820 results** (expected completion April 2027) before any decision on GvHD prevention indication
- **Obtain full safety profile**: retrieve Singapore HSA and TFDA package insert, boxed warnings, contraindications, and drug interaction data (remediate Data Gaps DG001/DG002)
- **Clarify regulatory pathway** for investigational use in Singapore; baricitinib is currently unregistered and would require HSA authorisation for any local clinical study
- **Plasma cell myeloma (rank 5) deserves dedicated evaluation**: IL-6/JAK/STAT3 mechanistic rationale is plausible — commission a focused literature review and assess feasibility of a Phase 1/2 study design
- **Compare baricitinib vs. ruxolitinib** in the GvHD context: given ruxolitinib's established approval, define where baricitinib's selectivity profile offers a meaningful clinical differentiation
- **Do not pursue ranks 1–2, 7–10**: no mechanistic or empirical basis to justify further investigation at this time
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

