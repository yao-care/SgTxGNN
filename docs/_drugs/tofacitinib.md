---
layout: default
title: Tofacitinib
parent: 僅模型預測 (L5)
nav_order: 991
evidence_level: L5
indication_count: 10
---

# Tofacitinib
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

# Tofacitinib: From Rheumatoid Arthritis to Plasma Cell Myeloma (Research Hypothesis)

## One-Sentence Summary

Tofacitinib is a JAK1/JAK3 inhibitor used internationally for rheumatoid arthritis and other autoimmune conditions (not currently registered in Singapore). TxGNN screened 10 candidate indications for this drug, and while the top-ranked hits are statistically driven and biologically implausible, one credible signal emerges: **Plasma Cell Myeloma**, supported by preclinical mechanistic data and observational cohort literature — though still far from clinical-trial-grade evidence and complicated by the drug's own malignancy black-box warning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Rheumatoid arthritis (per international literature context; no Singapore license on file) |
| Predicted New Indication | Plasma Cell Myeloma |
| TxGNN Prediction Score | 96.09% (rank #24,051 of all disease nodes) |
| Evidence Level | L4 (preclinical/mechanistic study support) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** (research hypothesis only; blocked by missing safety label data) |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Tofacitinib is currently a data gap in this evidence pack. Based on the literature retrieved, however, Tofacitinib is a pan-JAK inhibitor (JAK1/JAK3) originally developed and FDA-approved for rheumatoid arthritis and other inflammatory/autoimmune diseases, working by blocking cytokine receptor signaling that drives immune cell activation.

The IL-6–JAK–STAT3 axis is a well-established survival and proliferation pathway for malignant plasma cells in multiple myeloma, and is also central to how the bone marrow microenvironment (e.g., mesenchymal stromal cells) promotes tumor growth and drug resistance. A prior in vitro drug-repurposing screen (PMID 29622655) specifically identified Tofacitinib as capable of reversing these tumor-stimulating microenvironmental effects, giving this prediction a concrete mechanistic anchor rather than being pure model output. Two additional pharmacovigilance/cohort studies (PMID 38071595, PMID 39819734) provide real-world observational context on immunosuppressive/DMARD exposure and hematologic malignancy risk in overlapping patient populations.

Importantly, of the 10 candidates TxGNN generated for this drug, 8 (including the #1-ranked "colobomatous microphthalmia-rhizomelic dysplasia syndrome") are congenital/developmental syndromes or anatomically-defined tumor categories with **no supporting literature or trials and no plausible JAK-STAT connection** — these are very likely knowledge-graph node-proximity artifacts rather than real signals, and are scored L5/Hold accordingly. Plasma cell myeloma (this report) and myeloid leukemia are the only two candidates that reach an actual evidence tier (L4 and L3 respectively).

---

## Full Candidate Screening Overview

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation | Note |
|------|---------|-------------|-----------------|-----------------|------|
| 1 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 98.96% | L5 | Hold | No mechanistic link; likely KG noise |
| 2 | Brachydactyly-syndactyly syndrome | 98.88% | L5 | Hold | No mechanistic link; likely KG noise |
| 3 | Indolent plasma cell myeloma | 96.66% | L5 | Hold | Subtype-specific evidence absent |
| **4** | **Plasma cell myeloma** | **96.09%** | **L4** | **Research Question** | **Featured in this report** |
| 5 | Myeloid leukemia | 95.43% | L3 | Research Question | Mixed signal — see Safety Considerations |
| 6 | Ganglioneuroblastoma | 79.55% | L5 | Hold | No mechanistic link |
| 7 | Macrothrombocytopenia with mitral valve insufficiency | 76.17% | L5 | Hold | No mechanistic link |
| 8 | Hereditary thrombocytopenia with normal platelets | 75.76% | L5 | Hold | No mechanistic link |
| 9 | Vertebral anomalies with T-cell dysfunction | 75.34% | L5 | Hold | Mechanism direction questionable (JAK3 inhibition could worsen immunodeficiency) |
| 10 | Retroperitoneal neoplasm | 75.26% | L5 | Hold | Anatomic category, no molecular basis |

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Plasma Cell Myeloma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29622655](https://pubmed.ncbi.nlm.nih.gov/29622655/) | 2018 | Preclinical (in vitro) | Haematologica | Repurposing screen identifies Tofacitinib as reversing bone-marrow-microenvironment-driven myeloma cell growth via JAK/STAT blockade |
| [39819734](https://pubmed.ncbi.nlm.nih.gov/39819734/) | 2025 | Cohort | BMC Rheumatology | US Veterans cohort examining whether b/tsDMARD use (including JAK inhibitors) affects multiple myeloma incidence in RA patients |
| [38071595](https://pubmed.ncbi.nlm.nih.gov/38071595/) | 2024 | Cohort (pharmacovigilance) | J Eur Acad Dermatol Venereol | FAERS analysis linking myeloma/immunosuppressant exposure to secondary malignancy reporting; contextual safety signal, not myeloma efficacy data |

---

## Singapore Market Information

Tofacitinib currently has no license records in Singapore (market status: Not Marketed). No authorization table can be generated.

---

## Safety Considerations

- **Malignancy risk signal**: Literature evidence for a related candidate (myeloid leukemia, rank 5) includes a case report of chronic myeloid leukemia developing during Tofacitinib therapy (PMID 31263618). JAK inhibitors as a class carry a known malignancy black-box warning; any myeloma repurposing hypothesis must be evaluated alongside this risk, not purely as a treatment opportunity.
- **Blocking data gap (DG001)**: TFDA/official label warnings and contraindications are not yet available for this drug, which prevents completion of the standard S1 safety screening stage.
- **High-priority data gap (DG002)**: Confirmed mechanism-of-action data (beyond literature inference) is still pending from DrugBank.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Plasma Cell Myeloma hypothesis has a genuine mechanistic anchor (IL-6-JAK-STAT3 pathway) and one directly supportive in vitro repurposing study, but evidence remains preclinical/observational only (L4), with no interventional trials, and the drug's own malignancy warning creates a safety tension that must be resolved before advancing. Nine of the ten TxGNN-predicted candidates lack any supporting evidence and should not be pursued.

**To proceed, the following is needed:**
- Obtain official drug label (warnings, contraindications) to clear the blocking S1 safety gate (DG001)
- Confirm mechanism of action via DrugBank to validate mechanistic rationale (DG002)
- Seek prospective or interventional data on JAK inhibition in multiple myeloma, specifically disentangling therapeutic potential from malignancy-risk signal
- Monitor whether any registry (ClinicalTrials.gov, ICTRP) initiates myeloma-related Tofacitinib trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

