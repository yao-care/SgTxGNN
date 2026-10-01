---
layout: default
title: Fingolimod
parent: Low Evidence (L5)
nav_order: 428
evidence_level: L5
indication_count: 10
---

# Fingolimod
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

# Fingolimod: From Multiple Sclerosis to Borderline Ovarian Serous Tumor

## One-Sentence Summary

Fingolimod (FTY720) is an oral sphingosine-1-phosphate (S1P) receptor modulator, marketed in Singapore as Gilenya and approved for multiple sclerosis according to the cited literature.
The TxGNN model predicts it may be effective for **borderline ovarian serous tumor**, but there are **0 clinical trials** and **0 publications** for this specific disease.
The only support is indirect preclinical work in malignant ovarian cancer, so this is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (per PMID 30388910; the HSA indication text was not provided in the Evidence Pack) |
| Predicted New Indication | Borderline ovarian serous tumor |
| TxGNN Prediction Score | 94.94% (model rank 26,856) |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Fingolimod is known as an S1P receptor modulator that traps lymphocytes in lymph nodes. Its efficacy in multiple sclerosis is established. Any link to ovarian tumors is therefore inferred from preclinical work, not from mechanism data for this disease.

The preclinical literature retrieved for ovarian indications suggests several possible links:
- FTY720 induces necrotic cell death and autophagy in ovarian cancer cells (PMID 20935520).
- Sphingosine kinase 1 (SphK1) is proposed as a therapeutic target in epithelial ovarian cancer (PMID 25429856).
- FTY720 enhanced carboplatin and tamoxifen activity in a patient-derived ovarian cancer xenograft model (PMID 30120964).

There are important caveats:
- All of these studies used **malignant** epithelial ovarian cancer models. None examined borderline serous tumors, which are a distinct, generally lower-grade entity.
- One study found that combining FTY720 with cisplatin was **antagonistic** in ovarian cancer cells (PMID 23592281). This argues against assuming benefit from combination use.
- The TxGNN score reflects knowledge-graph similarity, not tested efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for borderline ovarian serous tumor.

For context only, the pack lists these preclinical papers under other ovarian predictions. They concern malignant ovarian cancer and are indirect evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30120964](https://pubmed.ncbi.nlm.nih.gov/30120964/) | 2018 | Preclinical (patient-derived xenograft) | Cancer Letters | FTY720 enhanced the anti-tumor activity of carboplatin and tamoxifen in drug-resistant ovarian cancer models |
| [25429856](https://pubmed.ncbi.nlm.nih.gov/25429856/) | 2015 | Preclinical / target validation | Int J Cancer | SphK1 inhibition or FTY720 affected proliferation, apoptosis, angiogenesis and invasion in epithelial ovarian cancer cell lines |
| [20935520](https://pubmed.ncbi.nlm.nih.gov/20935520/) | 2010 | Preclinical (in vitro) | Autophagy | FTY720 was cytotoxic to ovarian cancer cells via necrosis and autophagy, with autophagy playing a protective role |
| [23592281](https://pubmed.ncbi.nlm.nih.gov/23592281/) | 2013 | Preclinical (in vitro) | Int J Oncol | FTY720 combined with cisplatin was antagonistic in ovarian cancer cells, with autophagy involved |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN14153P | Gilenya Capsule 0.5mg | Capsule | Novartis Pharma Stein AG / Novartis Pharmaceutical Manufacturing LLC |
| SIN15761P | Gilenya Capsule 0.25mg | Capsule | Novartis Pharmaceutical Manufacturing LLC |

Both products are oral capsules.

---

## Safety Considerations

Please refer to the package insert for safety information.

Fingolimod sequesters lymphocytes and causes lymphopenia. This is relevant to any use in oncology settings, especially alongside chemotherapy.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on the model score (L5), with no clinical trials or disease-specific literature. The indirect preclinical data come from malignant ovarian cancer, and one study showed antagonism with cisplatin.

**To proceed, the following is needed:**
- The HSA package insert, to obtain the approved indication, warnings and contraindications. This is currently a blocking gap for safety screening.
- Mechanism of action data (for example from DrugBank), to support a mechanistic-link analysis.
- Disease-specific preclinical evidence in borderline serous tumor models.
- A decision on whether a broader "serous neoplasm" question is worth pursuing, since it has one xenograft study (L4, Research Question).
- A review of the rank 10 prediction (immunoerythromyeloid hypoplasia), which is likely a knowledge-graph artifact.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

