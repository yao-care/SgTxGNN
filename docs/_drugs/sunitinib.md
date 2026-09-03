---
layout: default
title: Sunitinib
parent: 僅模型預測 (L5)
nav_order: 936
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Sunitinib is a multi-targeted tyrosine kinase inhibitor (VEGFR1-3, PDGFR-α/β, KIT) with renal cell carcinoma as its established, already-approved core indication.
The TxGNN model predicts it may also be effective for **Liposarcoma**,
with **3 clinical trials** and **9 publications** currently supporting this direction.
This evidence pack covers 10 predicted indications in total; liposarcoma (rank 1 by TxGNN score) is the primary focus of this report, with the remaining candidates summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (see Market Status below); internationally, Renal Cell Carcinoma is documented in this evidence pack as Sunitinib's established, approved core indication (see rank 9 evidence) |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form (Data Gap DG002, High severity). Based on the evidence available in this pack, Sunitinib is a multi-targeted oral tyrosine kinase inhibitor blocking VEGFR1-3, PDGFR-α/β and KIT, and this profile underlies its established use in metastatic renal cell carcinoma.

Liposarcoma — particularly the dedifferentiated and myxoid subtypes — frequently shows PDGFR overexpression and marked angiogenesis dependence, which provides a plausible mechanistic bridge from Sunitinib's known anti-angiogenic/anti-PDGFR activity in RCC to a role in liposarcoma. This is reinforced by a completed Phase II trial (NCT00400569) that directly tested Sunitinib in metastatic/unresectable soft tissue sarcoma including liposarcoma, and by a case report of long-lasting clinical benefit in heavily pre-treated metastatic liposarcoma (PMID 23482782).

That said, liposarcoma is histologically heterogeneous, and response rates across subtypes are inconsistent; the mechanistic rationale is reasonable but not yet confirmed by subtype-specific randomized evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | Completed | 48 | Open-label Phase II trial of Sunitinib malate in metastatic/unresectable soft tissue sarcoma (leiomyosarcoma, **liposarcoma**, fibrosarcoma, MFH); directly evaluated Sunitinib (Grade A relevance). |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | Completed | 53 | Multicenter continuous-dosing Sunitinib basket trial in non-GIST sarcomas, including a liposarcoma subgroup (Grade B relevance). |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | Completed | 131 | SARC024 study of oral regorafenib (not Sunitinib) in selected sarcoma subtypes; provides background on SMOKI-class activity in soft tissue sarcoma only (Grade C relevance). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Phase 2 (RCT) | Int J Cancer | Phase II study of Sunitinib malate in relapsed/refractory soft tissue sarcoma, with dedicated focus on leiomyosarcoma, liposarcoma and MFH. |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Phase 2 RCT protocol | BMC Cancer | REGOSARC trial protocol: multinational, randomized, placebo-controlled Phase II of regorafenib in advanced soft tissue sarcoma; supports angiogenesis-targeting rationale shared with Sunitinib. |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histology-driven therapy for soft tissue sarcoma; notes high activity of trabectedin specifically in myxoid liposarcoma and outlines targeted-therapy landscape. |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | Overview of emerging therapies for adult soft tissue sarcoma, including anti-angiogenic tyrosine kinase inhibitors. |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | Medical treatment of soft tissue sarcomas stratified by histological subtype. |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review/Genomic | Cancers | Genetic, epigenetic and transcriptomic alterations in liposarcoma relevant to target therapy selection. |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Genomic Cohort | Oncotarget | Next-generation sequencing of extraskeletal myxoid chondrosarcoma; evaluates predictive factors for Sunitinib benefit in a related sarcoma entity. |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case Report | Anticancer Research | Long-lasting clinical benefit of Sunitinib malate in a heavily pre-treated metastatic liposarcoma patient. |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Case Series/Pathology | Am J Surg Pathol | Clinicopathologic analysis of a related myxoid myofibroblastic sarcoma entity; background pathology reference. |

---

## Other Predicted Indications (Overview)

This evidence pack contains 10 TxGNN-predicted indications for Sunitinib. Beyond liposarcoma (above), the remaining candidates are:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Decision Stage | Recommendation |
|------|----------------------|-------------|-----------------|-----------------|-----------------|
| 2 | Ovarian myxoid liposarcoma | 99.84% | L4 | S0 | Hold |
| 3 | RCC associated with neuroblastoma | 99.78% | L5 | S0 | Hold |
| 4 | RCC with Xp11.2/TFE3 fusion | 99.78% | L2 | S2 | Research Question |
| 5 | Unclassified RCC | 99.78% | L2 | S3 | Proceed with Guardrails |
| 6 | Dermatofibrosarcoma protuberans | 99.73% | L2 | S3 | Proceed with Guardrails |
| 7 | Childhood kidney cell carcinoma | 99.72% | L4 | S1 | Research Question |
| 8 | Angiolipoma | 99.67% | L5 | S0 | Hold |
| 9 | Renal carcinoma | 99.65% | L1 | S3 | Proceed with Guardrails* |
| 10 | Heart fibrosarcoma | 99.63% | L5 | S0 | Hold |

\*Rank 9 (renal carcinoma) is flagged in the evidence pack as Sunitinib's **already-approved core indication**, not a novel repurposing candidate — its strong evidence base (Phase 3 pivotal data, L1) reflects internal validation of the knowledge graph rather than a new opportunity.

Of the genuinely novel candidates, **unclassified RCC** (L2, S3) and **dermatofibrosarcoma protuberans** (L2, S3) currently carry the most mature evidence and warrant priority follow-up alongside liposarcoma.

---

## Singapore Market Information

Currently no marketing authorization records available — Sunitinib is not registered in Singapore under this evidence pack (0 licenses).

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor: VEGFR1-3, PDGFR-α/β, KIT) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
A single completed Phase II trial directly testing Sunitinib in liposarcoma, supported by a positive case report, establishes biological plausibility (L2 evidence), but subtype heterogeneity in liposarcoma means efficacy has not been confirmed in a dedicated, adequately powered trial.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert with warnings, contraindications and drug interaction data (Blocking gap, DG001)
- Formal DrugBank-sourced mechanism of action confirmation (High-priority gap, DG002)
- A liposarcoma-subtype-specific prospective trial (or subgroup re-analysis of NCT00400569/NCT00474994) to confirm activity signal
- Singapore market entry pathway assessment, given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

