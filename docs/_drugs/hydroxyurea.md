---
layout: default
title: Hydroxyurea
parent: Medium Evidence (L3-L4)
nav_order: 511
evidence_level: L4
indication_count: 10
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Hydroxyurea: From Melanoma and Sickle Cell Anaemia to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is an oral antimetabolite originally used for melanoma, ovarian cancer and sickle cell anaemia.
The TxGNN model predicts it may be effective for **female breast carcinoma**, but **no clinical trials** are registered for this indication, and the **20 publications** retrieved are almost entirely preclinical, in-silico or indirect.
The prediction is therefore supported mainly by the computational score rather than by clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Melanoma, sickle cell anaemia, ovarian cancer (the Singapore licence has no indication text recorded) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, hydroxyurea inhibits ribonucleotide reductase. This depletes the deoxynucleotide (dNTP) pool needed for DNA synthesis and causes replication stress in rapidly dividing cells. That is the basis of its use in cancers such as melanoma and ovarian cancer.

Breast cancer cells are also sensitive to replication stress. The retrieved laboratory studies link replication-stress and DNA-repair pathways (ATR, RPA2) to how breast cancer cells respond to hydroxyurea. For example, valproic acid sensitised breast cancer cells to hydroxyurea by blocking RPA2-mediated DNA repair. This makes the prediction mechanistically plausible.

However, no direct clinical efficacy evidence in breast cancer was found. The studies retrieved are mostly cell-line work, in-silico design of hydroxyurea–lipid conjugates, or old phase I combination-chemotherapy studies in mixed solid tumours. The very high TxGNN score is a computational prediction only.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for female breast carcinoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 | Am J Clin Oncol | 5-FU/leucovorin followed by hydroxyurea with allopurinol protection in 20 patients with advanced GI and breast cancer; dose-finding only |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1/2 | Cancer Chemother Pharmacol | 5-FU, leucovorin, hydroxyurea and escalating cisplatin with radiotherapy in mixed advanced solid tumours |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitises breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid, a valproic acid analogue, as a potential hydroxyurea sensitiser in breast carcinoma |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico | Drug Research | Design of hydroxyurea–lipid conjugates targeting PI3K/AKT/mTOR to improve uptake in breast cancer |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | Preclinical | Naunyn-Schmiedeberg's Arch Pharmacol | Hydroxyurea-loaded magnetic nanoparticles with pH-dependent release; effects on cell-cycle arrest and p53 expression |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Mol Cancer | EYA4 promotes breast cancer progression through replication-stress avoidance |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | ATR inhibitor NU6027 evaluated in breast and ovarian cancer cell lines |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Breast cancer coexisting with essential thrombocythemia; therapeutic management |
| [25814515](https://pubmed.ncbi.nlm.nih.gov/25814515/) | 2015 | Preclinical | Mol Pharmacol | Ribonucleotide reductase inhibitor COH29 impairs DNA repair in BRCA1-defective breast cancer cells; hydroxyurea is a reference RNR inhibitor |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11083P | HYDRINE CAPSULES 500 mg | Capsule | Not recorded in the compiled data |

The single licence is valid, covers a single-ingredient oral product, and is held by Korea United Pharm. Inc.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High (the contraindication-linked conditions include leukopenia, thrombocytopenia and anaemia) |
| Emetogenicity Classification | Low |
| Monitoring Items | Complete blood count with differential, renal function, liver function |
| Handling Protection | Follow cytotoxic drug handling regulations |

For authoritative details, please refer to the package insert warnings and precautions.

---

## Safety Considerations

- **Contraindication-linked conditions (knowledge-graph association, not label text)**: kidney disease, pyoureter, thrombocytopenia, anaemia, macrocytic anaemia, leukopenia, cutaneous vasculitis.
- **Drug Interactions**: 100 potential interactions were identified. Levofloxacin is the one with a graded level (Minor). Others, such as doxycycline, amphotericin B, hydrocortisone, famotidine, acetylsalicylic acid, pantoprazole, metformin, omeprazole, morphine and simvastatin, have no severity grade assigned.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high and the mechanism (replication stress) is plausible. However, there is no registered breast cancer trial and no direct clinical efficacy evidence, so the evidence is at L4 (preclinical and mechanistic). The drug also has significant myelosuppression risk.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Singapore package insert warnings and contraindications, and the approved indication text for the local licence
- Clinical efficacy data in breast cancer (for example, a phase 2 trial or a systematic review of earlier studies)
- Evidence that hydroxyurea, alone or in combination, adds benefit over current breast cancer standard of care
- A haematological safety monitoring plan, including drug interaction review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

