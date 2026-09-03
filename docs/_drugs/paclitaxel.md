---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 746
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class cytotoxic chemotherapy originally developed and globally approved for ovarian cancer, later extended to NSCLC and Kaposi's sarcoma. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, and this prediction is already strongly corroborated — **50 clinical trials** and **20 publications** are on file, including the landmark CALGB 9344/9741 trial (n=3,677).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer, NSCLC, Kaposi's sarcoma (globally approved indications; not registered in Singapore) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Paclitaxel is a microtubule-stabilizing agent: it binds β-tubulin, prevents spindle depolymerization, arrests cells at the G2/M checkpoint, and induces apoptosis. This mechanism underlies its broad activity against rapidly dividing solid-tumour cells and is not restricted to any single tissue of origin. A structured DrugBank MOA field is not present in this evidence pack (database field gap), but the mechanism itself is well established in the literature reviewed below.

Notably, breast carcinoma is not really a "novel" repurposing target for paclitaxel — it is already one of paclitaxel's globally approved indications (alongside ovarian cancer, NSCLC, and Kaposi's sarcoma) and is used routinely as a neoadjuvant, adjuvant, and metastatic-setting chemotherapy backbone worldwide, often in combination with trastuzumab, pertuzumab, or platinum agents for HER2-positive and other subtypes. What the TxGNN prediction and this evidence pack primarily surface, therefore, is a **local registration gap in Singapore** (0 authorizations on file) rather than a true mechanistic or clinical uncertainty — the underlying efficacy evidence base is mature and extensive.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00991263](https://clinicaltrials.gov/study/NCT00991263) | N/A | Completed | 3,677 | Landmark CALGB 9344/9741 correlative study establishing paclitaxel's benefit by intrinsic breast cancer subtype in adjuvant/dose-dense therapy |
| [NCT00433420](https://clinicaltrials.gov/study/NCT00433420) | Phase 3 | Active, not recruiting | 2,000 | EC-followed-by-paclitaxel vs FEC-followed-by-paclitaxel, every 2 vs 3 weeks, node-positive breast cancer |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2,005 | Sequential doxorubicin/paclitaxel/cyclophosphamide vs concurrent AC-then-paclitaxel at 14- or 21-day intervals, node-positive Stage II/IIIA breast cancer |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy ± trastuzumab in node-positive/high-risk node-negative HER2-low breast cancer, including weekly paclitaxel arm |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: dose-dense/dose-intensified regimens (incl. weekly paclitaxel + dual HER2 blockade) for high-risk early breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo-ALTTO: neoadjuvant lapatinib and/or trastuzumab plus paclitaxel in HER2-positive primary breast cancer |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Phase 3 | Completed | 725 | Randomized, double-blind comparison of biosimilar ABP 980 vs trastuzumab (paclitaxel-based regimen) in HER2-positive early breast cancer |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Terminated | 63 | Paclitaxel + trastuzumab + lapatinib vs paclitaxel + trastuzumab + placebo in ErbB2-overexpressing metastatic breast cancer |
| [NCT00915018](https://clinicaltrials.gov/study/NCT00915018) | Phase 2 | Completed | 479 | Randomized comparison of neratinib + paclitaxel vs trastuzumab + paclitaxel as first-line therapy for ErbB2-positive recurrent/metastatic breast cancer |
| [NCT00709761](https://clinicaltrials.gov/study/NCT00709761) | Phase 2 | Completed | 60 | Single-arm study of weekly nab-paclitaxel + lapatinib in ErbB2-overexpressing metastatic breast cancer |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, including resistance mechanisms |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early review establishing paclitaxel/docetaxel efficacy extension from ovarian cancer to metastatic breast carcinoma |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Cohort | BioMed Research International | Real-world study of neoadjuvant epirubicin/cyclophosphamide + weekly paclitaxel-trastuzumab in HER2-positive breast carcinoma |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Cohort/Clinical | Cancer | Phase II trial of doxorubicin + paclitaxel in advanced breast carcinoma; importance of prior adjuvant anthracycline therapy |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase 2 (ECOG) | Journal of Clinical Oncology | Biweekly paclitaxel + cisplatin in advanced breast carcinoma, building on prior 85% response rate signal |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | — | Chemical Biology & Drug Design | Unveils therapeutic potential of paclitaxel combinations against breast carcinoma with in vivo biomarker identification |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | — | Nature Communications | Identifies TEKT4 germline variations enriched in breast cancer resistant to paclitaxel via exome sequencing |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | — | Cancer | Role of paclitaxel in multimodality treatment for inflammatory breast carcinoma |
| [24068539](https://pubmed.ncbi.nlm.nih.gov/24068539/) | 2013 | — | Breast Cancer Research and Treatment | Phase I-II of tipifarnib + sequential weekly paclitaxel and doxorubicin-cyclophosphamide in HER2-negative inflammatory and ER-positive breast carcinoma |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | — | Journal for ImmunoTherapy of Cancer | Novel insights into paclitaxel's effect on tumor-associated macrophages enhancing PD-1 blockade in breast cancer |

---

## Singapore Market Information

No paclitaxel product is currently registered or marketed in Singapore under this evidence pack (0 authorizations on file). Local registration status should be verified directly against the HSA product register before any regulatory action.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is the principal dose-limiting toxicity of paclitaxel; monitor closely, particularly with weekly/dose-dense regimens |
| Emetogenicity Classification | Low-to-moderate (per standard taxane emetogenic risk classification) |
| Monitoring Items | CBC with differential, hepatic function, peripheral neuropathy assessment, infusion-related hypersensitivity monitoring |
| Handling Protection | Yes — must be handled and administered per standard cytotoxic/hazardous drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information (key warnings, contraindications, and drug-interaction data were not available in this evidence pack).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paclitaxel's efficacy in breast carcinoma is supported by an extensive, mature evidence base (L1 — multiple completed Phase 3 RCTs, including the landmark CALGB 9344/9741 trial), and breast cancer is already an established global indication for this drug. The primary gap is local: paclitaxel is not currently registered or marketed in Singapore, and this specific evidence pack lacks local safety labeling data.

**To proceed, the following is needed:**
- Confirmation of local (HSA) regulatory registration status and any planned market authorization for Singapore
- Local package insert / safety labeling data (key warnings, contraindications, drug interactions) to complete safety review (currently flagged as a blocking data gap)
- Formal DrugBank/structured MOA record to replace the current database field gap
- Route-of-administration and dosage-form compatibility confirmation for the local market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

