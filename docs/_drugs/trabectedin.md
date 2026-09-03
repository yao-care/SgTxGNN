---
layout: default
title: Trabectedin
parent: 僅模型預測 (L5)
nav_order: 998
evidence_level: L5
indication_count: 10
---

# Trabectedin
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

# Trabectedin: From Soft Tissue Sarcoma to Female Breast Carcinoma

## One-Sentence Summary

> Trabectedin is a marine-derived DNA-binding antineoplastic agent, established internationally for the treatment of soft tissue sarcoma and platinum-sensitive ovarian cancer (in combination with pegylated liposomal doxorubicin).
> The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
> with **2 clinical trials** and **19+ publications** currently supporting this direction, though sample sizes remain small.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Soft Tissue Sarcoma / Ovarian Cancer (per published literature — no Singapore registration record exists) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, official mechanism of action (MOA) data from DrugBank is not available (flagged as a High-severity data gap). Based on published pharmacology literature, trabectedin is a DNA minor-groove alkylator that binds guanine N2 and interferes with transcription-coupled nucleotide excision repair (TC-NER). This gives it selective cytotoxicity against tumor cells with DNA repair deficiencies — particularly homologous recombination (HR) deficiency such as BRCA1/2 mutations.

Breast cancer, like ovarian cancer (an already-approved indication for trabectedin in combination with PLD), harbors a meaningful BRCA1/2-mutated and HR-deficient subpopulation (up to ~25% of sporadic tumors show a "BRCAness" phenotype). This shared molecular vulnerability is the primary mechanistic bridge supporting the TxGNN prediction. Additional literature also suggests trabectedin has an immunomodulatory effect — depleting tumor-associated macrophages/myeloid-derived suppressor cells — which may synergize with immunotherapy (e.g., IL-12) specifically in triple-negative breast cancer (TNBC).

It should be noted that this mechanistic rationale is derived from general pharmacology literature rather than a validated `original_moa` field, so it should be treated as supportive context rather than confirmed regulatory information.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03470805](https://clinicaltrials.gov/study/NCT03470805) | Phase 2 | Completed | 9 | Olaparib maintenance after trabectedin–PLD response in recurrent ovarian carcinoma; enriched for BRCA1/2 mutation carriers, directly using trabectedin as induction therapy relevant to DNA-repair-deficient tumors |
| [NCT00786838](https://clinicaltrials.gov/study/NCT00786838) | Phase 2 | Completed | 76 | Single-blind, placebo-controlled, sequential-design study assessing QT/QTc interval effects of a single trabectedin dose in advanced solid tumors — the largest trial in this evidence set, though focused on cardiac safety rather than efficacy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25239225](https://pubmed.ncbi.nlm.nih.gov/25239225/) | 2014 | RCT / Phase 2 | Clinical Breast Cancer | Multicenter randomized Phase 2 study comparing two trabectedin administration regimens in advanced breast cancer after anthracycline/taxane failure |
| [27266804](https://pubmed.ncbi.nlm.nih.gov/27266804/) | 2016 | Phase 2 | Clinical Breast Cancer | Phase 2 trial of trabectedin in HR+/HER2- advanced breast cancer, stratified by XPG gene expression as a predictive biomarker |
| [24692579](https://pubmed.ncbi.nlm.nih.gov/24692579/) | 2014 | Phase 2 | Annals of Oncology | First-in-class international Phase 2 study of trabectedin in germline BRCA1/2-mutated metastatic breast cancer |
| [26592307](https://pubmed.ncbi.nlm.nih.gov/26592307/) | 2016 | Review | Expert Opin Investig Drugs | Overview of trabectedin's antiproliferative and tumor-microenvironment-modulating mechanisms, with rationale for breast cancer use |
| [27710871](https://pubmed.ncbi.nlm.nih.gov/27710871/) | 2016 | Review/Clinical | Cancer Treatment Reviews | Reviews trabectedin as a chemotherapy option specifically in BRCA-deficient tumors |
| [19114300](https://pubmed.ncbi.nlm.nih.gov/19114300/) | 2009 | Phase 1 PK | Eur J Cancer | Phase 1 pharmacokinetic study of trabectedin + doxorubicin combination in soft tissue sarcoma and advanced breast cancer |
| [25722380](https://pubmed.ncbi.nlm.nih.gov/25722380/) | 2015 | Phase 3 (exploratory) | Annals of Oncology | Exploratory analysis of Phase 3 OVA-301 trial showing BRCA1/XPG mutation status predicts trabectedin+PLD response |
| [23364677](https://pubmed.ncbi.nlm.nih.gov/23364677/) | 2013 | Biomarker/Translational | Mol Cancer Ther | Identifies CUL4A as a biomarker of trabectedin response in HRR-deficient breast cancer cell lines |
| [39777457](https://pubmed.ncbi.nlm.nih.gov/39777457/) | 2025 | Preclinical | Cancer Immunol Res | Trabectedin depletes immunosuppressive myeloid cells and enhances IL-12 antitumor activity in TNBC models |
| [23792433](https://pubmed.ncbi.nlm.nih.gov/23792433/) | 2013 | In vitro mechanistic | Toxicology Letters | Demonstrates diverse apoptosis induction by trabectedin across HER2+/ER- and HER2-/ER+ breast cancer cell lines |

---

## Singapore Market Information

Trabectedin is currently **not registered** in Singapore (0 licenses on file). No local authorization number, product name, or approved indication text is available for reference.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (marine-derived DNA minor-groove alkylator) |
| Myelosuppression Risk | High — literature reports Grade 3–4 neutropenia in ~50% and thrombocytopenia in ~20% of patients (PMID 19496709) |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential, liver function tests (transaminases, bilirubin — hepatotoxicity and reversible cholangitis reported), renal function, cardiac QT interval |
| Handling Protection | Must follow cytotoxic drug handling regulations (preparation, administration, and disposal) |

---

## Safety Considerations

Please refer to the package insert for safety information. (No TFDA/local label warnings, contraindications, or drug interaction data are currently available; this is flagged as a **Blocking** data gap.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction (female breast carcinoma) has reasonable mechanistic support and L2-level clinical evidence, but the two supporting trials are small (n=9 and n=76) and not both efficacy-focused. Critically, a Blocking data gap exists for local safety labeling (warnings/contraindications), which prevents even a preliminary (S1) safety assessment, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- Obtain official TFDA/manufacturer package insert (warnings, contraindications, DDI) to close the Blocking data gap (DG001)
- Retrieve verified mechanism of action data from DrugBank (DG002)
- Larger, breast-cancer-specific Phase 2/3 RCT data (current evidence is limited to small trials and preclinical/mechanistic studies)
- Assessment of local regulatory pathway if Singapore market entry is being considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

