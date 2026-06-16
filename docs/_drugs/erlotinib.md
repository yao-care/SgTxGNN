---
layout: default
title: Erlotinib
parent: 僅模型預測 (L5)
nav_order: 392
evidence_level: L5
indication_count: 10
---

# Erlotinib
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

# Erlotinib: From Non-Small Cell Lung Cancer to Ewing Sarcoma

## One-Sentence Summary

Erlotinib (Tarceva®) is a first-generation EGFR tyrosine kinase inhibitor (TKI) approved in the US for non-small cell lung cancer (NSCLC) and pancreatic cancer, though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Ewing Sarcoma**, with **1 clinical trial** and **2 publications** currently supporting this direction.
However, the sole clinical trial was withdrawn before any patient was enrolled, and the evidence base remains at the preclinical and early exploratory stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Non-Small Cell Lung Cancer (NSCLC); Pancreatic Cancer |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 95.77% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable from the DrugBank integration in this evidence pack. Based on published literature within this pack, erlotinib is a selective, reversible inhibitor of the EGFR (HER1/ErbB1) intracellular tyrosine kinase domain. By blocking EGFR autophosphorylation, it suppresses downstream RAS–MAPK and PI3K–AKT signalling cascades that drive tumour cell proliferation, survival, angiogenesis, and metastasis. Its clinical efficacy in EGFR-mutated NSCLC and pancreatic cancer is well established globally, though it is not registered in Singapore.

The mechanistic rationale for Ewing sarcoma rests on documented EGFR and HER3 (ErbB3) co-expression in Ewing sarcoma cell lines. HGF/c-MET cross-activation with EGFR has been shown to promote tumour survival in these cells. A preclinical xenograft study (Bandyopadhyay et al., 2018; PMID 29080385) directly tested the combination of the anti-HER3 antibody patritumab with erlotinib alongside standard cytotoxic agents (cisplatin, vincristine, cyclophosphamide) in paediatric sarcoma models expressing relevant ErbB receptors and ligands — providing the most direct preclinical rationale available.

While Ewing sarcoma (a primitive neuroectodermal tumour) and NSCLC differ substantially in histological origin, shared dependency on ErbB family signalling provides a biologically plausible but unproven therapeutic bridge. The TxGNN model's prediction is mechanistically coherent, but no patient-level efficacy data yet exist to support clinical translation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02689336](https://clinicaltrials.gov/study/NCT02689336) | Phase 2 | Withdrawn | 0 | Planned trial of erlotinib + temozolomide in relapsed/recurrent/refractory paediatric solid tumours with EGFR, ERBB2, or JAK2V617F mutations (Ewing sarcoma-eligible); withdrawn before any patient enrollment — no efficacy or safety data generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [29080385](https://pubmed.ncbi.nlm.nih.gov/29080385/) | 2018 | Preclinical Study | Pediatric Blood & Cancer | Evaluated patritumab (anti-HER3) ± erlotinib combined with cisplatin, vincristine, and cyclophosphamide in paediatric sarcoma xenograft models expressing ErbB receptors; assessed dual ErbB axis inhibition strategy in the context of standard cytotoxic backbones. |
| [26835334](https://pubmed.ncbi.nlm.nih.gov/26835334/) | 2014 | Review | Translational Pediatrics | Broad review of advances in paediatric cancer treatment over the past decade; contextualises the role of risk-adapted and molecularly targeted therapies in childhood solid tumours including Ewing sarcoma. |

---

## Singapore Market Information

Erlotinib is currently **not registered** in Singapore. No HSA marketing authorisations are on record. Physicians wishing to use erlotinib in Singapore would need to proceed via the Special Access Route (SAR) or equivalent regulatory pathway.

---

## Cytotoxicity

Erlotinib is an anticancer agent approved for malignant indications (NSCLC, pancreatic cancer).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — EGFR tyrosine kinase inhibitor (4-anilinoquinazoline class) |
| Myelosuppression Risk | Low — haematological toxicity is uncommon with EGFR TKIs; myelosuppression is not a primary concern |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (ALT, AST, bilirubin), renal function, CBC, pulmonary function/chest imaging (ILD risk), skin and ophthalmological assessment |
| Handling Protection | Oral tablet formulation; standard cytotoxic handling precautions apply per institutional policy |

---

## Safety Considerations

No drug–drug interaction data or formal regulatory safety text is available in the current evidence pack. Please refer to the Tarceva® (erlotinib) prescribing information for complete warnings, contraindications, and interaction data.

Based on established class-effect knowledge for EGFR TKIs:

- **Skin toxicity**: Acneiform/papulopustular rash is very common (>50% of patients) and may paradoxically correlate with therapeutic response
- **Interstitial Lung Disease (ILD)**: Rare but potentially fatal; any new or worsening pulmonary symptoms require prompt investigation and treatment discontinuation
- **Hepatotoxicity**: Transaminase elevation observed; baseline and periodic liver function monitoring required
- **Gastrointestinal toxicity**: Diarrhoea and stomatitis are dose-dependent and common
- **Ocular toxicity**: Dry eye, keratitis, and corneal ulceration reported (PMID 37026321)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only identified clinical trial (NCT02689336) was withdrawn before enrolling a single patient, yielding no clinical efficacy or safety data for erlotinib in Ewing sarcoma. The mechanistic hypothesis — dual ErbB axis inhibition via EGFR/HER3 co-expression in Ewing sarcoma — is biologically plausible and supported by one preclinical xenograft study, but this falls short of the evidence threshold required to advance to clinical evaluation without further groundwork.

**To proceed, the following is needed:**

- **Preclinical validation**: Confirm EGFR/HER3 expression levels and erlotinib sensitivity in contemporary Ewing sarcoma cell lines and patient-derived xenograft (PDX) models
- **Biomarker strategy**: Define EGFR/ErbB pathway activation status as a patient selection criterion before any clinical trial design
- **Safety data gap**: Obtain full erlotinib prescribing information (Tarceva® SmPC or FDA label) and complete drug interaction profile, particularly for paediatric populations
- **MOA data**: Retrieve complete DrugBank pharmacology and pharmacokinetic profile
- **Regulatory pathway**: Identify whether compassionate use or Special Access Route application would be required for Singapore use
- **Clinical opportunity**: Monitor for open Phase 1/2 basket trials including paediatric EGFR-pathway-aberrant solid tumours that could accommodate Ewing sarcoma patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

