---
layout: default
title: Brigatinib
parent: Low Evidence (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brigatinib: predicted new indication Fibromatosis, gingival (evidence level L5). Approved use: Non-small cell lung carcinoma / lung cancer"
---

# Brigatinib
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

# Brigatinib: From Non-Small Cell Lung Cancer to Gingival Fibromatosis

## One-Sentence Summary

Brigatinib is an oral kinase inhibitor (ALK inhibitor) originally used to treat ALK-positive non-small cell lung cancer.
The TxGNN model's top-ranked prediction is **gingival fibromatosis**, but this rests on a graph-based score alone, with **0 clinical trials** and **0 publications** supporting it.
Other lower-ranked predictions (notably NF2-related schwannomatosis, which appears under a different label) have more literature, but none has been validated for the predicted label.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Non-small cell lung carcinoma / lung cancer (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Fibromatosis, gingival |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, brigatinib is a next-generation ALK inhibitor with additional activity against other tyrosine kinases. Its efficacy in ALK-positive NSCLC has been proven, but a mechanistic link to gingival fibromatosis has not been identified.

The high TxGNN score (99.89%) is a graph-based prediction only. No trials or publications support brigatinib in gingival fibromatosis, so the prediction should be treated as a hypothesis, not as evidence of benefit.

Other predictions in the list show a similar pattern:
- **Lung-related labels** (fibroma of lung, hamartoma of lung, lung benign neoplasm, pulmonary sulcus neoplasm): the shared lung location with the approved NSCLC use does not imply activity against benign tumours. Literature attached to "lung benign neoplasm" is about ALK-positive malignant NSCLC (e.g., the ALTA-1L Phase 3 trial), which is the approved indication and does not support benign tumours.
- **Lung hilum carcinoma**: anatomically close to NSCLC and plausible, but no indication-specific evidence was found.
- **Lung germ cell tumour**: no germ-cell-specific evidence. Related literature shows case reports of response in ALK-altered pheochromocytoma and lung large cell neuroendocrine carcinoma, plus preclinical neuroblastoma work. Any relevance depends on ALK alteration, which is not established.
- **NF2-related schwannomatosis** (attached to the rare-syndrome label at rank 10): a small clinical study (NEJM 2024) and preclinical work show tumour shrinkage in NF2-deficient meningioma and schwannoma through inhibition of multiple tyrosine kinases other than ALK. This is the most interesting signal in the data, but it belongs to NF2-related schwannomatosis, not to the syndrome it was matched to, and should be evaluated as its own indication.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication.

## Literature Evidence

No literature is available for the top-ranked indication (gingival fibromatosis). The following publications were retrieved for lower-ranked predictions and are shown for context only. Most concern NSCLC or NF2-related schwannomatosis, not the predicted labels.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/) | 2024 | Clinical study (small) | N Engl J Med | Brigatinib in NF2-related schwannomatosis with progressive tumours |
| [34264955](https://pubmed.ncbi.nlm.nih.gov/34264955/) | 2021 | Preclinical | PLoS One | Tumour shrinkage in NF2-deficient meningioma and schwannoma via multiple tyrosine kinases, not ALK |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | RCT | N Engl J Med | Brigatinib vs crizotinib in ALK-positive NSCLC (ALTA-1L) |
| [34537440](https://pubmed.ncbi.nlm.nih.gov/34537440/) | 2021 | RCT | J Thorac Oncol | Final ALTA-1L results; brigatinib superior PFS vs crizotinib |
| [36038416](https://pubmed.ncbi.nlm.nih.gov/36038416/) | 2022 | RCT (subgroup) | Clin Lung Cancer | Asian vs non-Asian patients in ALTA-1L |
| [34371380](https://pubmed.ncbi.nlm.nih.gov/34371380/) | 2021 | Case report | ESMO Open | Sustained response in refractory metastatic pheochromocytoma with ALK mutation |
| [39395329](https://pubmed.ncbi.nlm.nih.gov/39395329/) | 2024 | Case report | Respir Investig | Therapeutic effect in lung large cell neuroendocrine carcinoma with EML4-ALK fusion |
| [37773318](https://pubmed.ncbi.nlm.nih.gov/37773318/) | 2023 | Review | NPJ Precis Oncol | ALK fusions across cancers as a possible tumour-agnostic target |
| [34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/) | 2021 | Case report (adverse event) | Front Pharmacol | Fatal tumour lysis syndrome induced by brigatinib |
| [27049722](https://pubmed.ncbi.nlm.nih.gov/27049722/) | 2016 | Preclinical | Oncotarget | Brigatinib inhibits ALK-positive neuroblastoma cells, Drosophila and mice |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15659P | ALUNBRIG FILM-COATED TABLET 90mg | Film-coated tablet | Not specified in the compiled data |
| SIN15660P | ALUNBRIG FILM-COATED TABLET 180mg | Film-coated tablet | Not specified in the compiled data |
| SIN15658P | ALUNBRIG FILM-COATED TABLET 30mg | Film-coated tablet | Not specified in the compiled data |
| SIN15661P | ALUNBRIG INITIATION PACK | Film-coated tablet | Not specified in the compiled data |

All four licences are valid single-ingredient oral products (manufacturers: Penn Pharmaceutical Services Limited / Takeda Ireland Limited).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (ALK / multi-kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert; a fatal tumour lysis syndrome case has been reported (PMID 34987411), and cardiac toxicity has been examined in pharmacovigilance analyses |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

**Drug Interactions**: The interaction query returned 100 interacting drugs in total; 20 were available for review. Major-level interactions include:
- Aprepitant
- Dexamethasone
- Clarithromycin

Moderate-level interactions include antidiabetic agents (e.g., metformin, pioglitazone, canagliflozin, dapagliflozin, alogliptin, albiglutide, acarbose, chlorpropamide, acetohexamide), acid-suppressing drugs (famotidine, ranitidine, rabeprazole, cimetidine), and others (loperamide, morphine, cisapride, clotrimazole).

**Other safety signals from the literature**: a case report of fatal tumour lysis syndrome (PMID 34987411).

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (gingival fibromatosis) is supported only by a graph-based score, with no trials, no literature, and no identified mechanistic link. The evidence level is L5. The data compiled for this report also lack package insert safety information, so safety screening cannot proceed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap)
- Mechanism of action data from DrugBank
- Approved indication text for the Singapore licences
- A separate evaluation of NF2-related schwannomatosis as its own indication, where the most relevant brigatinib evidence exists
- For any lung-related or ALK-altered tumour candidate, confirmation of ALK alteration status and indication-specific studies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

