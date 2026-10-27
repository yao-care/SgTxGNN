---
layout: default
title: Apalutamide
parent: Medium Evidence (L3-L4)
nav_order: 102
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Apalutamide: predicted new indication Benign neoplasm of prostate (evidence level L4). Approved use: Prostate cancer"
monitor_inn: "Apalutamide"
predicted_indications: ["prostate leiomyoma", "Brenner tumor", "benign reproductive system neoplasm", "fibroma of prostate", "prostate phyllodes tumor", "benign neoplasm of prostate", "benign prostate phyllodes tumor", "palmoplantar keratoderma-sclerodactyly syndrome"]
---

# Apalutamide
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Apalutamide: From Prostate Cancer to Benign Neoplasm of Prostate
{: .text-alpha }

## One-Sentence Summary

Apalutamide is an androgen receptor inhibitor originally used to treat prostate cancer.
The TxGNN model predicts it may be effective for **benign neoplasm of prostate** (score 97.5%), but the 20 publications retrieved for this term are about prostate cancer, the approved indication, and **no clinical trials** were found for this term.
The evidence is therefore indirect, and the prediction should be treated as a **hypothesis, not a validated new indication**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prostate cancer (the Singapore licence text is blank; the original indications come from the TxGNN knowledge graph: prostate cancer, familial prostate carcinoma, prostate carcinoma) |
| Predicted New Indication | Benign neoplasm of prostate (rank 7 in the TxGNN list; see the note below) |
| TxGNN Prediction Score | 97.45% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

**Note on candidate selection:** The top-ranked prediction, "prostate cancer/brain cancer susceptibility" (98.43%), is a genetic susceptibility label rather than a treatable disease, and it has no supporting evidence. The candidates ranked 2 to 6 and 9 to 10 have no trials or literature. Rank 8, "male reproductive organ cancer", mostly captures the already approved prostate cancer indication. Benign neoplasm of prostate (rank 7) is the highest-ranked candidate that is a genuine disease and has any supporting literature, so this report focuses on it.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on known information, apalutamide is an oral, selective androgen receptor (AR) inhibitor. Published reviews describe it as binding the ligand-binding domain of the receptor, which blocks androgen-driven signalling. Its efficacy in prostate cancer is well established, including metastatic castration-sensitive disease, non-metastatic castration-resistant disease, and high-risk localized disease.

Prostate tissue growth depends on androgen signalling, so blocking the AR gives a plausible mechanistic rationale for benign prostatic neoplasms. However, this link is **theoretical**. The retrieved publications concern malignant disease, not benign prostatic tumours, so they show the drug works in the approved indication and say little about benign disease.

The high TxGNN score probably reflects the closeness of benign and malignant prostate neoplasm nodes in the knowledge graph, rather than a new, independent signal. Whether this prediction overlaps with the approved indication should be checked before treating it as a true repurposing candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for benign neoplasm of prostate.

For context, the broader category "male reproductive organ cancer" (rank 8) retrieved many apalutamide trials. They all concern prostate cancer, the approved indication, and do not support a benign-prostate indication. Examples include [NCT02489318](https://clinicaltrials.gov/study/NCT02489318) (TITAN, Phase 3, mHSPC) and [NCT02867020](https://clinicaltrials.gov/study/NCT02867020) (Phase 2, completed).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31150574](https://pubmed.ncbi.nlm.nih.gov/31150574/) | 2019 | RCT | N Engl J Med | Apalutamide plus ADT in metastatic castration-sensitive prostate cancer (TITAN) |
| [33914595](https://pubmed.ncbi.nlm.nih.gov/33914595/) | 2021 | RCT (final analysis) | J Clin Oncol | Final survival analysis of TITAN; improved overall survival and radiographic progression-free survival in mCSPC |
| [29420164](https://pubmed.ncbi.nlm.nih.gov/29420164/) | 2018 | RCT | N Engl J Med | Apalutamide improved metastasis-free survival in non-metastatic castration-resistant prostate cancer (SPARTAN) |
| [42223077](https://pubmed.ncbi.nlm.nih.gov/42223077/) | 2026 | RCT | N Engl J Med | Perioperative apalutamide in high-risk localized prostate cancer |
| [39417629](https://pubmed.ncbi.nlm.nih.gov/39417629/) | 2025 | Comparative study | The Prostate | Real-world comparison of abiraterone, enzalutamide, and apalutamide in metastatic hormone-sensitive prostate cancer |
| [33480983](https://pubmed.ncbi.nlm.nih.gov/33480983/) | 2021 | Review | Endocr Rev | Overview of hormonal therapy for prostate cancer, including direct AR inhibition |
| [35750683](https://pubmed.ncbi.nlm.nih.gov/35750683/) | 2022 | Review | Signal Transduct Target Ther | Signalling pathways and clinical trials in prostate cancer, including next-generation AR inhibitors |
| [32907777](https://pubmed.ncbi.nlm.nih.gov/32907777/) | 2021 | Commentary/Review | Eur Urol | Overall survival data for apalutamide in nmCRPC (SPARTAN) |

All of these publications address prostate cancer. None evaluates apalutamide in benign prostatic neoplasms.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15698P | ERLEADA FILM-COATED TABLET 60MG | Tablet, film coated | Not stated in the data compiled for this report |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted hormonal therapy (androgen receptor inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records in total; 20 are listed in the data compiled for this report, including these notable ones:
  - **Major**: bupropion, cisapride, dolasetron, eliglustat
  - **Moderate**: for example famotidine, rabeprazole, esomeprazole, hydrocortisone, clarithromycin, loperamide, dapagliflozin, empagliflozin, glimepiride, glipizide

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for these.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score and indirect literature about prostate cancer, the approved indication. No trial or study has tested apalutamide in benign prostatic neoplasms, and the score likely reflects knowledge-graph proximity rather than a new clinical signal.

**To proceed, the following is needed:**
- Clarify whether "benign neoplasm of prostate" is a distinct target disease or overlaps with the approved prostate cancer indication
- Targeted literature and trial searches for apalutamide in benign prostatic disease
- Preclinical or early-phase evidence in benign prostatic tumours
- Detailed mechanism of action data
- The package insert warnings and contraindications for Singapore (SIN15698P), needed for safety screening
- A review of the major interactions, especially with bupropion, cisapride, dolasetron, and eliglustat
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

