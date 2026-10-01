---
layout: default
title: Pirfenidone
parent: Low Evidence (L5)
nav_order: 790
evidence_level: L5
indication_count: 10
---

# Pirfenidone
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

# Pirfenidone: From Idiopathic Pulmonary Fibrosis to Extracutaneous Mastocytoma

## One-Sentence Summary

Pirfenidone is an oral anti-fibrotic drug, marketed in Singapore as Esbriet and used for idiopathic pulmonary fibrosis.
The TxGNN model predicts it may be effective for **extracutaneous mastocytoma**, but **0 clinical trials** and **0 publications** support this prediction, so it is a model output only.
Of the top 10 predictions, only "fibroblastic neoplasm" (rank 9) has any supporting literature, and that evidence is indirect.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Idiopathic pulmonary fibrosis (per the literature; the Singapore registration data do not state an indication) |
| Predicted New Indication | Extracutaneous mastocytoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Pirfenidone is known as an anti-fibrotic and anti-inflammatory agent. It dampens TGF-beta-driven fibroblast proliferation and collagen deposition, and it reduces TNF-alpha in preclinical models.

**The mechanistic link for this prediction is weak.** Mast cell neoplasms are typically driven by KIT signalling. Pirfenidone's anti-fibrotic and anti-inflammatory actions have no established connection to that pathway. The very high score (99.71%) is most likely an artefact of the knowledge graph rather than a biological signal.

The same weakness applies to the other top-10 predictions:
- **Mast cell disease** (aggressive systemic mastocytosis) is dominated by KIT D816V signalling, with no plausible link to pirfenidone.
- **Fibroblast-lineage tumours** (dermatofibrosarcoma protuberans, fibrosarcomas, low grade fibromyxoid sarcoma) have a speculative link through pirfenidone's anti-fibroblast activity. Suppressing fibrosis does not equal anti-tumour activity, and no preclinical or clinical data were found.
- **Autosomal recessive familial Mediterranean fever** has only an indirect anti-inflammatory rationale. Colchicine and IL-1 blockers already set a high bar.
- **Hepatic infarction** is an ischaemic vascular event, and an anti-fibrotic does not address the acute clinical need.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other Predictions With Evidence

Only one of the top 10 predictions has retrieved literature: **fibroblastic neoplasm** (rank 9, TxGNN score 99.23%, evidence level L4, stage S1). The evidence is indirect and comes mostly from benign fibroproliferative disease and case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27835939](https://pubmed.ncbi.nlm.nih.gov/27835939/) | 2016 | In vitro | BMC Musculoskelet Disord | Pirfenidone inhibited TGF-β1-mediated activity in Dupuytren's disease-derived fibroblasts |
| [30927912](https://pubmed.ncbi.nlm.nih.gov/30927912/) | 2019 | In vitro | BMC Musculoskelet Disord | Studied pirfenidone's effect on TGF-β1-stimulated non-SMAD signalling in Dupuytren's fibroblasts |
| [35129055](https://pubmed.ncbi.nlm.nih.gov/35129055/) | 2022 | Preclinical | Pharm Dev Technol | Explored pirfenidone as a locally injectable anti-fibrotic for Dupuytren's disease |
| [12907346](https://pubmed.ncbi.nlm.nih.gov/12907346/) | 2003 | Pilot clinical study | Am J Gastroenterol | Pilot project evaluating pirfenidone for desmoid tumours in familial adenomatous polyposis |
| [29702057](https://pubmed.ncbi.nlm.nih.gov/29702057/) | 2018 | Case report | Perm J | Undifferentiated pleomorphic sarcoma reported after pirfenidone use (safety signal) |
| [32572469](https://pubmed.ncbi.nlm.nih.gov/32572469/) | 2020 | Case report | Rheumatology (Oxford) | Multiple eruptive dermatofibromas aggravated by mycophenolate mofetil and pirfenidone in a patient with systemic sclerosis (safety signal) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15601P | ESBRIET FILM COATED TABLET 801MG | Tablet, film coated | Not stated in the registration data |
| SIN15600P | ESBRIET FILM COATED TABLET 267MG | Tablet, film coated | Not stated in the registration data |

Both products are oral tablets made by Delpharm Milano S.r.l.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for extracutaneous mastocytoma rests on a model score alone (L5). There are no trials or publications, and the drug's known mechanism does not fit KIT-driven mast cell neoplasms. None of the top 10 predictions has clinical-trial support or reached L3 or higher. Only fibroblastic neoplasm (L4) has any evidence, and it is indirect. It also comes with safety signals: case reports of a sarcoma after pirfenidone use and of aggravated dermatofibromas.

**To proceed, the following is needed:**
- The mechanism of action data for pirfenidone and the approved indication text from the Singapore package insert.
- The package insert warnings and contraindications, which are needed before any safety screening.
- For extracutaneous mastocytoma, preclinical evidence of an actual link to KIT or mast cell biology, which is currently missing.
- For fibroblastic neoplasm and desmoid tumours, confirmation of whether the 2003 pilot (PMID 12907346) was a prospective human efficacy study, which could support L3 for the desmoid tumour subset.
- A review of the sarcoma and dermatofibroma case reports before this direction advances beyond a research question.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

