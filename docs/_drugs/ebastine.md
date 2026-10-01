---
layout: default
title: Ebastine
parent: Low Evidence (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Ebastine
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

# Ebastine: From Allergic Conditions to Coronary Artery Disease

## One-Sentence Summary

Ebastine is a peripherally selective H1 antihistamine, marketed in Singapore as KESTINE 10 mg tablets. The TxGNN model predicts it may be effective for **coronary artery disease** with a very high score, but there are **0 clinical trials** and only **1 publication**, a computational study that does not test the prediction. This is a model-only signal, and the mechanistic hint from that paper points the opposite way.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration record (ebastine is an H1 antihistamine used for allergic conditions) |
| Predicted New Indication | Coronary artery disease |
| TxGNN Prediction Score | 99.18% |
| Evidence Level | L4 (preclinical/computational only; the other nine predictions are L5) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the record. Ebastine is known as a peripherally selective H1 receptor antagonist, and it has no established anti-atherosclerotic or anti-ischaemic mechanism.

The only linked paper is a molecular docking study of CYP2J2, an enzyme that makes cardioprotective epoxyeicosatrienoic acids (EETs). Ebastine appears in it as a CYP2J2 ligand or inhibitor. Inhibiting CYP2J2 would plausibly work against cardiovascular benefit, not for it. The same reasoning applies to the second-ranked prediction, myocardial ischaemia, which rests on the same paper.

The prediction is therefore best read as a knowledge-graph association, not a mechanistically grounded hypothesis. The high score is not backed by any clinical signal. Cardiac-population caution is also warranted because of QT/hERG liability considerations in this drug class.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18004755](https://pubmed.ncbi.nlm.nih.gov/18004755/) | 2008 | In silico / computational | Proteins | Homology modelling, molecular dynamics and docking of ligand binding to human CYP2J2. CYP2J2 is linked to coronary artery disease, hypertension and cancer, but the study does not test ebastine in any disease. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09435P | KESTINE TABLET 10 mg (manufacturer: Industrias Farmaceuticas Almirall (IFA) S.A.) | Tablet, film coated | Not listed in the record |

## Safety Considerations

- **Cardiac caution**: QT/hERG liability considerations for this drug class argue for caution in cardiac populations.

Please refer to the package insert for other safety information, including warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and one computational paper whose mechanism suggests a possibly adverse direction. Beyond this top-ranked prediction, the other nine (myocardial ischaemia, anomalous left coronary artery from the pulmonary artery, leprosy, candidiasis, pneumocystosis, hypertrichosis, and vocal cord, middle ear and uterine polyps) are also rated Hold, with no supporting clinical data.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening
- Mechanism of action data for ebastine, for example from DrugBank
- Preclinical or clinical evidence that ebastine has a benefit, not harm, in coronary or ischaemic settings, taking CYP2J2/EET biology and QT liability into account
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

