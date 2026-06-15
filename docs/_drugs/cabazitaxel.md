---
layout: default
title: Cabazitaxel
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Cabazitaxel
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

# Cabazitaxel: From Metastatic Prostate Cancer to Female Breast Carcinoma

## One-Sentence Summary

Cabazitaxel is a next-generation taxane originally approved for docetaxel-refractory metastatic castration-resistant prostate cancer (mCRPC), distinguished by its low P-glycoprotein (P-gp) affinity that enables activity in multidrug-resistant tumours.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **0 registered clinical trials** and **20 publications** currently supporting this direction.
The mechanistic rationale is strong — paclitaxel and docetaxel (same class) are breast cancer cornerstones, and cabazitaxel's unique resistance-overcoming profile offers a distinct clinical niche in taxane-refractory or TNBC settings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Metastatic castration-resistant prostate cancer (mCRPC), docetaxel-refractory |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cabazitaxel belongs to the taxane class of microtubule-stabilising agents — the same mechanistic family as paclitaxel and docetaxel, both of which are firmly established as standard-of-care chemotherapy for breast cancer across multiple settings (neoadjuvant, adjuvant, and metastatic). By stabilising microtubule polymerisation, cabazitaxel arrests cells in the G2/M phase of mitosis, triggering apoptosis in rapidly dividing tumour cells. This shared mechanism provides the foundational rationale for extending cabazitaxel's use to breast cancer.

What differentiates cabazitaxel from its predecessors is its critically low affinity for P-glycoprotein (P-gp), the efflux pump responsible for multidrug resistance (MDR). Breast cancer patients who progress on paclitaxel or docetaxel frequently do so through P-gp upregulation; cabazitaxel can bypass this resistance mechanism. A mechanistic study (PMID 28567478) further demonstrated that tumours with high βIII-tubulin expression — a hallmark of triple-negative breast cancer (TNBC) and a marker of taxane resistance — are paradoxically more sensitive to cabazitaxel than to docetaxel, offering a precision advantage in the most treatment-refractory breast cancer subtype.

Beyond direct cytotoxicity, preclinical evidence (PMID 33753567) reveals that cabazitaxel reprogrammes tumour-associated macrophages (TAMs) from the immunosuppressive M2 phenotype, thereby amplifying the efficacy of CD47-targeted immunotherapy in TNBC. This immunomodulatory dimension, combined with cabazitaxel's documented ability to cross the blood-brain barrier (relevant for CNS metastases in HER2+ and TNBC), positions it as a mechanistically versatile candidate for breast cancer repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for the specific query of cabazitaxel in female breast carcinoma. However, published Phase I/II studies have been conducted (see Literature Evidence below), and at least one Phase II trial (NCT01934894) was conducted for HER2+ breast cancer with CNS metastases per PMID 29678476.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28768217](https://pubmed.ncbi.nlm.nih.gov/28768217/) | 2017 | Phase II RCT | European Journal of Cancer | GENEVIEVE study: cabazitaxel vs weekly paclitaxel as neoadjuvant therapy in HER2-negative BC (TNBC / luminal B); assessed pCR rate as primary endpoint |
| [21339064](https://pubmed.ncbi.nlm.nih.gov/21339064/) | 2011 | Phase I/II | European Journal of Cancer | Multicentre dose-escalation of cabazitaxel + capecitabine in MBC progressing after anthracyclines and taxanes; established MTD and documented antitumour activity |
| [29678476](https://pubmed.ncbi.nlm.nih.gov/29678476/) | 2018 | Phase II | Clinical Breast Cancer | Cabazitaxel + lapatinib in HER2+ MBC with intracranial metastases (NCT01934894); exploited cabazitaxel's BBB-penetrating ability |
| [25416788](https://pubmed.ncbi.nlm.nih.gov/25416788/) | 2015 | Review | Molecular Cancer Therapeutics | Resistance mechanisms in MCF-7 breast cancer cells; cabazitaxel showed 15-fold less cross-resistance vs 200-fold for paclitaxel in MDR variants |
| [33247980](https://pubmed.ncbi.nlm.nih.gov/33247980/) | 2021 | Review | British Journal of Clinical Pharmacology | TDM-based dose individualisation for taxanes; reviews PK-PD relationships and clinical application of cabazitaxel alongside classical taxanes |
| [28567478](https://pubmed.ncbi.nlm.nih.gov/28567478/) | 2017 | Preclinical | Cancer Chemotherapy and Pharmacology | βIII-tubulin high expression (common in TNBC) enhances cabazitaxel efficacy relative to docetaxel; mechanistic rationale for TNBC application |
| [33753567](https://pubmed.ncbi.nlm.nih.gov/33753567/) | 2021 | Preclinical (In Vivo) | Journal for Immunotherapy of Cancer | Cabazitaxel reprogrammes tumour-associated macrophages, synergising with CD47-targeted immunotherapy in TNBC preclinical models |
| [21076710](https://pubmed.ncbi.nlm.nih.gov/21076710/) | 2010 | Review | Drugs of Today | Overview of cabazitaxel properties: low P-gp affinity, favourable PK, broad preclinical activity including Pgp-expressing tumour models |
| [30529259](https://pubmed.ncbi.nlm.nih.gov/30529259/) | 2019 | Preclinical | Journal of Controlled Release | Cabazitaxel-loaded PEBCA nanoparticles in patient-derived basal-like breast cancer xenograft; complete remission in 6/8 tumours vs 2/8 for free drug |
| [38562610](https://pubmed.ncbi.nlm.nih.gov/38562610/) | 2024 | Preclinical | International Journal of Nanomedicine | PACA nanoparticle variants of cabazitaxel in TNBC PDX models; modulation of tumour microenvironment with reduction in M2 macrophages |

---

## Singapore Market Information

Cabazitaxel is currently **not registered in Singapore**. No marketing authorisations are on record as of the data cutoff (2026-06-02). Cabazitaxel (Jevtana®, Sanofi) holds FDA and EMA approval for mCRPC; Singapore-specific registration would require a separate HSA submission.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Taxane class — semisynthetic taxoid derived from 10-deacetylbaccatin III) |
| Myelosuppression Risk | **High** — neutropenia is the dose-limiting toxicity; febrile neutropenia documented in clinical trials; G-CSF prophylaxis typically required |
| Emetogenicity Classification | Low to moderate (consistent with other taxanes at standard IV doses) |
| Monitoring Items | CBC with differential (before each cycle), liver function tests (ALT/AST/bilirubin), renal function (creatinine), neurological assessment (peripheral neuropathy), diarrhoea severity |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system transfer devices, PPE (gloves, gown, eye protection), dedicated preparation area |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Formal TFDA/HSA package insert data was not available in this Evidence Pack (Data Gap DG001). Based on the known class profile and published clinical literature, key risks include severe neutropenia, febrile neutropenia, severe diarrhoea, peripheral neuropathy, and hypersensitivity reactions. Pre-medication with antihistamine, corticosteroid, and H2 antagonist is standard practice. Use in patients with hepatic impairment or severe renal impairment requires dose reduction or is contraindicated.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between cabazitaxel and breast cancer is strong and well-grounded — paclitaxel and docetaxel (same class) are standard backbone therapies, and cabazitaxel's specific advantages in MDR settings (low P-gp affinity, βIII-tubulin sensitivity) address an unmet need in taxane-refractory TNBC. A completed Phase II RCT (GENEVIEVE) and Phase I/II clinical data confirm the concept is clinically testable, supporting an L2 evidence classification. The absence of registered clinical trials in Singapore and the drug's non-marketed status mean this repurposing path is early-stage but scientifically credible.

**To proceed, the following is needed:**

- **MOA data formalisation**: Retrieve full DrugBank entry for DB06772 to document cabazitaxel's mechanism, targets, and pharmacological class formally (remediate Data Gap DG002)
- **Safety package**: Obtain and parse the official package insert (Jevtana SmPC or FDA label) to complete contraindications, black box warnings, and dose adjustment guidance (remediate Data Gap DG001)
- **ClinicalTrials.gov targeted search**: Expand query beyond "female breast carcinoma" to include "breast cancer," "TNBC," "triple-negative," and "HER2-positive" to capture relevant registered trials not matched by the original query
- **HSA regulatory pathway assessment**: Determine whether a new indication application or off-label use protocol is the appropriate regulatory pathway in Singapore given the current non-registered status
- **Population-specific safety plan**: Design a risk mitigation protocol for G-CSF prophylaxis, hepatic/renal monitoring, and neurotoxicity surveillance appropriate for the target breast cancer population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

