---
layout: default
title: Hydroxyurea
parent: Low Evidence (L5)
nav_order: 507
evidence_level: L5
indication_count: 10
---

# Hydroxyurea
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

# Hydroxyurea: From an Antineoplastic Antimetabolite to Female Breast Carcinoma

## One-Sentence Summary

Hydroxyurea is an oral antineoplastic drug that inhibits ribonucleotide reductase, but its approved indication is not recorded in the Singapore registration data.
The TxGNN model predicts it may be effective for **female breast carcinoma**, with **0 registered clinical trials** and **about 10 relevant publications**, mostly preclinical work and 1990s Phase I/II combination studies.
This is a hypothesis that needs testing, not a validated direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the available data |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (preclinical and mechanistic studies, plus early-phase combination studies with no breast-specific efficacy confirmed) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Based on known information, hydroxyurea is a ribonucleotide reductase inhibitor. It depletes the dNTP pools that cells need for DNA synthesis, which causes S-phase arrest and replication stress.

Breast cancer cells often depend on replication-stress tolerance and DNA-damage-response signalling, such as ATR and RPA2 phosphorylation. Preclinical studies show that blocking these pathways makes breast cancer cells more sensitive to hydroxyurea, or to drugs of the same class. This gives the model's prediction a plausible biological basis.

The link has not been validated in patients. No registered trial tests hydroxyurea in breast cancer. The 1990s combination studies did not lead to hydroxyurea being adopted for this disease. A high graph score by itself does not indicate efficacy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7914447](https://pubmed.ncbi.nlm.nih.gov/7914447/) | 1994 | Phase I/II trial | Bone Marrow Transplant | Hydroxyurea (18 g/m²) added to high-dose cyclophosphamide and thiotepa with stem cell rescue in 26 women with responding metastatic breast cancer; the authors describe it as an effective consolidation regimen |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase I trial | Am J Clin Oncol | Sequential 5-FU/leucovorin then hydroxyurea with allopurinol in 20 patients with advanced GI and breast cancers; a mixed population, so breast-specific results are unclear |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase I/II trial | Cancer Chemother Pharmacol | Dose-escalation of cisplatin added to 5-FU, hydroxyurea and radiotherapy in advanced solid tumours; not breast-specific |
| [2245491](https://pubmed.ncbi.nlm.nih.gov/2245491/) | 1990 | Pilot / Phase I | Cancer Chemother Pharmacol | Cisplatin preceded by cytarabine and hydroxyurea, based on an in vitro colon carcinoma model; a toxicity study, not breast-specific |
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico / preclinical | Drug Research | Designs hydroxyurea–lipid conjugates to overcome its hydrophilicity and improve cell uptake, targeting the PI3K/AKT/mTOR pathway |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitizes breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | 2-hexyl-4-pentynoic acid, a valproic acid analogue, is explored as a hydroxyurea sensitizer in breast carcinoma cells through the same DNA-repair mechanism |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical (mechanistic) | Mol Cancer | EYA4 helps breast cancer cells avoid replication stress, linking tumour progression to dependence on replication-stress tolerance |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | NU6027, an ATR inhibitor, is evaluated in breast and ovarian cancer cell lines, supporting the importance of ATR signalling in DNA damage |
| [34661718](https://pubmed.ncbi.nlm.nih.gov/34661718/) | 2022 | Preclinical (drug delivery) | Naunyn Schmiedebergs Arch Pharmacol | Hydroxyurea-loaded magnetic chitosan nanoparticles with pH-dependent release; studies cell-cycle arrest and p53 and lincRNA-p21 expression |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11083P | HYDRINE CAPSULES 500 mg (Korea United Pharm. Inc.) | Capsule (oral) | Not listed in the registration data |

---

## Cytotoxicity

This section is based on the drug's general pharmacology. The Evidence Pack contains no toxicity data.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | High (dose-limiting; neutropenia, thrombocytopenia and anaemia are expected) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, renal and liver function |
| Handling Protection | Follow cytotoxic drug handling regulations (gloves; avoid contact with capsule contents) |

Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no registered breast cancer trial, and the supporting literature is mainly preclinical work plus old, mixed-population combination studies. The Singapore package insert has not been reviewed, so the safety screen cannot proceed.

**To proceed, the following is needed:**
- The HSA package insert, covering warnings, contraindications and the approved indication
- Mechanism of action data from DrugBank
- Breast-cancer-specific clinical data, or a prospective study showing benefit over current standard therapy
- A myelosuppression monitoring plan, given the drug's cytotoxic profile

**Note:** Hydroxyurea in hemoglobin SC disease (rank 4 in this pack) has much stronger evidence, including several Phase 2 trials and a 2025 NEJM Evidence publication. It is worth evaluating separately.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

