---
layout: default
title: Axitinib
parent: Low Evidence (L5)
nav_order: 126
evidence_level: L5
indication_count: 10
---

# Axitinib
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

# Axitinib: From Advanced Renal Cell Carcinoma to Renal Cell Carcinoma Associated with Neuroblastoma

## One-Sentence Summary

Axitinib is an oral VEGFR inhibitor. Per the Evidence Pack it is an established treatment for advanced renal cell carcinoma (RCC), but the Singapore label text was not captured.
The TxGNN model ranks **renal cell carcinoma associated with neuroblastoma** as its top prediction, but this rare entity has **0 clinical trials and 0 publications**.
Evidence is much stronger for other RCC entries in the top 10, such as unclassified RCC, TFE3-translocation RCC and collecting duct carcinoma.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Renal cell carcinoma associated with neuroblastoma |
| TxGNN Prediction Score | 99.90% (identical to ranks 2 and 3, so it does not discriminate between them) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

The pack lists no original indication and gives no approved-indication text for the Singapore licences. The "advanced RCC" origin in the title comes from the pack's own rationale for the RCC entry (rank 6).

## Why is This Prediction Reasonable?

Axitinib inhibits VEGFR-1, -2 and -3, and also acts on PDGFR and c-KIT. The DrugBank mechanism field was empty in this pack; the mechanism here comes from the pack's rationale text. Blocking tumour blood-vessel growth is a validated strategy in RCC. Axitinib has Phase 3 support as second-line therapy (AXIS) and in first-line combinations with pembrolizumab or avelumab.

The top prediction is a very rare RCC variant linked to neuroblastoma. The only supporting logic is that it is a kidney cancer, and this is a general RCC rationale rather than evidence for this variant. The TxGNN score is nearly identical across all RCC-related entries, so it cannot tell the well-supported subtypes from the unsupported ones.

The other top-10 predictions fall into three groups:
- **Established use:** renal carcinoma (rank 6), which is an existing marketed indication rather than a repurposing signal.
- **Plausible RCC subtypes with early trials:** unclassified RCC, Xp11.2/TFE3-translocation RCC, collecting duct carcinoma and childhood kidney carcinoma.
- **Prediction-only or weak entries:** ovarian myxoid liposarcoma, angiolipoma and familial spontaneous pneumothorax have no evidence. Liposarcoma has one 2016 preclinical study.

## Clinical Trial Evidence

Rank 1 (RCC associated with neuroblastoma) has no related clinical trials registered. The table below shows the most relevant trials for the RCC-related entries in the pack.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00678392](https://clinicaltrials.gov/study/NCT00678392) | Phase 3 | Completed | 723 | AXIS: axitinib vs sorafenib as second-line therapy in metastatic RCC (renal carcinoma, rank 6) |
| [NCT00835978](https://clinicaltrials.gov/study/NCT00835978) | Phase 2 | Completed | 213 | Randomized double-blind: axitinib with or without dose titration in metastatic RCC |
| [NCT01599754](https://clinicaltrials.gov/study/NCT01599754) | Phase 3 | Terminated | 724 | Adjuvant axitinib vs placebo in high-risk RCC after nephrectomy |
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | Active, not recruiting | 15 | Axitinib + nivolumab vs nivolumab in TFE/translocation RCC; no results |
| [NCT06211114](https://clinicaltrials.gov/study/NCT06211114) | Phase 2 | Recruiting | 30 | Checkpoint inhibitors + axitinib in previously treated collecting duct carcinoma |
| [NCT05808608](https://clinicaltrials.gov/study/NCT05808608) | Phase 1/2 | Recruiting | 33 | AK104 + axitinib, first-line, special pathological subtypes of RCC |
| [NCT04385654](https://clinicaltrials.gov/study/NCT04385654) | Phase 2 | Unknown | 40 | Toripalimab + axitinib as neoadjuvant therapy in non-clear-cell RCC |
| [NCT04387500](https://clinicaltrials.gov/study/NCT04387500) | Phase 2 | Active, not recruiting | 41 | Sintilimab + axitinib in fumarate hydratase-deficient RCC |
| [NCT02164838](https://clinicaltrials.gov/study/NCT02164838) | Phase 1 | Completed | 51 | First axitinib study in children with recurrent or refractory solid tumours (dose-finding) |
| [NCT04033991](https://clinicaltrials.gov/study/NCT04033991) | N/A | Completed | 684 | Real-world UK retrospective study of sunitinib then axitinib in advanced RCC |

## Literature Evidence

Rank 1 has no related literature available. The table below shows the most relevant publications for the RCC-related entries.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30779529](https://pubmed.ncbi.nlm.nih.gov/30779529/) | 2019 | RCT | N Engl J Med | KEYNOTE-426: pembrolizumab + axitinib vs sunitinib in untreated advanced RCC |
| [37500340](https://pubmed.ncbi.nlm.nih.gov/37500340/) | 2023 | RCT | Eur Urol | KEYNOTE-426 43-month follow-up: superior efficacy of pembrolizumab + axitinib in advanced clear cell RCC |
| [40750932](https://pubmed.ncbi.nlm.nih.gov/40750932/) | 2025 | RCT | Nat Med | KEYNOTE-426 5-year survival and biomarker analyses |
| [30779531](https://pubmed.ncbi.nlm.nih.gov/30779531/) | 2019 | RCT | N Engl J Med | JAVELIN Renal 101: avelumab + axitinib vs sunitinib in untreated advanced RCC |
| [37872020](https://pubmed.ncbi.nlm.nih.gov/37872020/) | 2024 | RCT | Ann Oncol | RENOTORCH: toripalimab + axitinib vs sunitinib in intermediate/poor-risk advanced RCC |
| [40810951](https://pubmed.ncbi.nlm.nih.gov/40810951/) | 2025 | Phase 2 trial | JAMA Oncol | Sintilimab + axitinib in advanced fumarate hydratase-deficient RCC |
| [35428926](https://pubmed.ncbi.nlm.nih.gov/35428926/) | 2022 | Review | Urologie | Collecting duct carcinoma: reports that nivolumab + axitinib with radiotherapy prolongs survival |
| [39326645](https://pubmed.ncbi.nlm.nih.gov/39326645/) | 2024 | Review | Crit Rev Oncol Hematol | Axitinib outcomes in children, young adults and adults with RCC; effects in children remain unclear |
| [26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/) | 2015 | Case report | Can Urol Assoc J | 12-year-old with malignant renal epithelioid angiomyolipoma treated with axitinib |
| [27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/) | 2016 | Preclinical | Sarcoma | Antiangiogenic and antitumorigenic activity in myxoid liposarcoma cell lines |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14321P | INLYTA TABLETS 1MG | Tablet, film coated | Not stated in the retrieved record |
| SIN14322P | INLYTA TABLETS 5MG | Tablet, film coated | Not stated in the retrieved record |

Both are manufactured by Pfizer Manufacturing Deutschland GmbH. The route is oral.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (VEGFR tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Blood pressure (hypertension is a recognised adverse effect of VEGFR TKIs in the RCC literature). For other parameters, refer to the package insert. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No interactions were found in the drug interaction query.

## Conclusion and Next Steps

**Decision: Hold** (for renal cell carcinoma associated with neuroblastoma)

**Rationale:**
This prediction has no trials or publications and only a generic RCC rationale. The model score does not separate it from better-supported RCC entries. The established RCC use is already supported by Phase 3 data. The rare subtypes worth a closer look are TFE3-translocation RCC and collecting duct carcinoma (both L2–L3, "Research Question"). They rest on small, ongoing Phase 2 trials without results.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- The Singapore approved-indication text, and the original indication and mechanism of action from DrugBank
- A literature search specific to RCC associated with neuroblastoma, to see if any case-level evidence exists
- Results from the small subtype trials (NCT03595124, NCT06211114) before advancing those entries
- Pediatric dosing and safety data if childhood kidney carcinoma is pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

