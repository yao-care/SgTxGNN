---
layout: default
title: Entrectinib
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 10
---

# Entrectinib
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

# Entrectinib: From NTRK Fusion-Positive Solid Tumors to Female Breast Carcinoma

## One-Sentence Summary

Entrectinib (Rozlytrek) is a first-generation multi-kinase inhibitor targeting TRK (TRKA/B/C), ROS1, and ALK, approved internationally for NTRK gene fusion-positive solid tumors and ROS1-positive non-small cell lung cancer — though currently not registered in Singapore.
Among 10 TxGNN-predicted new indications, **female breast carcinoma** carries the strongest supporting evidence, with **5 clinical trials** and **7 publications** (Evidence Level L2), underpinned by a well-established mechanistic link through NTRK3 fusions in secretory breast carcinoma and ROS1 rearrangements in invasive lobular carcinoma.
The highest TxGNN prediction score belongs to multiple endocrine neoplasia (98.58%), but that indication is currently at L4 evidence only, making female breast carcinoma the priority actionable finding for clinical evaluation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | NTRK fusion-positive solid tumors; ROS1-positive NSCLC (internationally approved as Rozlytrek; no Singapore registration) |
| Predicted New Indication (Primary) | Female Breast Carcinoma |
| TxGNN Prediction Score | 97.76% (Female Breast Carcinoma, TxGNN Rank #8 by score) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Entrectinib selectively inhibits the tropomyosin receptor kinases TRKA, TRKB, and TRKC (encoded by NTRK1, NTRK2, and NTRK3 respectively), along with ROS1 and ALK — all of which become oncogenic drivers when fused to partner genes due to chromosomal rearrangements. Crucially, the **ETV6::NTRK3 fusion gene** is a defining molecular hallmark of **breast secretory carcinoma** (BSC), occurring in the vast majority of BSC cases. This constitutively active TrkC kinase drives tumour proliferation through the MAPK, PI3K/AKT, and PLC-γ pathways — all direct molecular targets of Entrectinib. The mechanistic connection is therefore direct, not inferential.

Beyond secretory carcinoma, **invasive lobular carcinoma (ILC)** — the second most common breast cancer histology — exhibits ROS1 rearrangements that create synthetic lethality in the context of CDH1 (E-cadherin) loss. Pre-clinical data have shown that ROS1 inhibitors suppress ILC tumour growth in models of E-cadherin deficiency, forming the scientific basis for the ongoing ROSALINE Phase 2 trial (NCT04551495), which uses Entrectinib combined with endocrine therapy in ER+/HER2− ILC patients.

This repurposing opportunity is therefore **target-driven and biomarker-selected**, representing the classic tumour-agnostic paradigm: the same kinase targets Entrectinib inhibits in approved indications (NTRK fusions, ROS1 rearrangements in NSCLC) are oncogenic drivers in defined breast cancer subtypes. The large Phase 2 STARTRK-2 basket trial (NCT02568267, n=534) — one of the pivotal studies supporting Entrectinib's FDA approval — already included breast cancer patients with qualifying NTRK or ROS1 fusions. For Singapore, where Entrectinib is not yet registered, this constitutes a genuine repurposing opportunity requiring a regulatory pathway.

## TxGNN Prediction Summary

The table below summarises all 10 TxGNN-predicted indications and their clinical evidence assessment. Female breast carcinoma ranks 8th by TxGNN score but 1st by evidence strength.

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|------------|----------------|----------------|
| 1 | Multiple Endocrine Neoplasia | 98.58% | L4 | Research Question |
| 2 | Amenorrhea | 98.37% | L5 | Hold |
| 3 | Thrombocytopenia | 98.11% | L5 | Hold ⚠️ |
| 4 | Cytomegalovirus Infection | 97.97% | L5 | Hold |
| 5 | Pulmonary Hypertension | 97.87% | L5 | Hold ⚠️ |
| 6 | Macrothrombocytopenia + Mitral Valve Insufficiency | 97.80% | L5 | Hold |
| 7 | Hereditary Thrombocytopenia (Normal Platelets) | 97.79% | L5 | Hold |
| **8** | **Female Breast Carcinoma** | **97.76%** | **L2** | **Proceed with Guardrails** |
| 9 | Transient Neonatal Thrombocytopenia | 97.76% | L5 | Hold |
| 10 | Infectious Bovine Rhinotracheitis | 97.74% | L5 | Hold |

> ⚠️ **Safety contradiction flags**: Thrombocytopenia (rank 3) and conditions associated with pulmonary thrombotic microangiopathy (rank 5) should be noted as Entrectinib adverse effect signals rather than potential indications — published case reports describe platelet reduction and pulmonary complications occurring during Entrectinib therapy (PMID: 41002576). These are therefore fundamentally unsuitable as repurposing targets.
>
> **Multiple Endocrine Neoplasia note**: MEN2A/2B is driven by RET proto-oncogene activating mutations. Entrectinib has documented off-target RET inhibitory activity (IC₅₀ ~7 nM in preclinical assays), but is significantly less potent than selective RET inhibitors (selpercatinib, pralsetinib). Neither available clinical trial directly studies Entrectinib in MEN patients, and the one relevant paper (PMID: 38438731) concerns RET TKI resistance mechanisms in medullary thyroid carcinoma — not Entrectinib efficacy. This warrants mechanistic research before any clinical evaluation.

## Clinical Trial Evidence

*Focus: Female Breast Carcinoma*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02568267](https://clinicaltrials.gov/study/NCT02568267) | Phase 2 | Active, Not Recruiting | 534 | STARTRK-2: Global basket study of Entrectinib in NTRK1/2/3, ROS1, or ALK fusion-positive solid tumors. Breast cancer with relevant fusions was included. This trial formed one of the primary bases for FDA approval of Entrectinib and represents the largest prospective evidence base for NTRK/ROS1-driven breast cancer. |
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | Active, Not Recruiting | 65 | ROSALINE trial: Entrectinib (as ROS1 inhibitor) combined with endocrine therapy in ER+/HER2− invasive lobular breast carcinoma (ILC) with CDH1 loss. Directly tests the synthetic lethality hypothesis of ROS1 inhibition in E-cadherin–deficient ILC. Completion expected January 2025. |
| [NCT02650401](https://clinicaltrials.gov/study/NCT02650401) | Phase 1/2 | Active, Not Recruiting | 69 | Pediatric dose-escalation and expansion study for Entrectinib in NTRK/ROS1 fusion-positive solid tumors. Clinically relevant as secretory breast carcinoma occurs in adolescent and young adult populations; supports pharmacokinetic data in younger patients. |

## Literature Evidence

*Focus: Female Breast Carcinoma*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38852701](https://pubmed.ncbi.nlm.nih.gov/38852701/) | 2024 | Preclinical | Cancer Letters | Entrectinib combined with pacritinib (dual TrkA + JAK2 inhibition) suppresses growth and metastasis in HER2-positive and triple-negative breast cancer in vitro and in vivo models. Provides direct preclinical evidence of Entrectinib anti-tumour activity specifically in breast cancer cell lines. |
| [35695563](https://pubmed.ncbi.nlm.nih.gov/35695563/) | 2022 | Phase 2 Protocol | Future Oncology | ROSALINE trial design and scientific rationale. Outlines the CDH1 synthetic lethality mechanism in ILC, ROS1 as a candidate target, and early results supporting the rationale for Entrectinib in endocrine-sensitive ILC. |
| [37330338](https://pubmed.ncbi.nlm.nih.gov/37330338/) | 2023 | Review | Pathology | Comprehensive review of NTRK fusions across solid tumors. Highlights that secretory carcinoma of the breast consistently harbors the ETV6::NTRK3 fusion and is specifically listed as a prime indication for larotrectinib and Entrectinib; includes pathology detection guidance. |
| [35927900](https://pubmed.ncbi.nlm.nih.gov/35927900/) | 2023 | Review | Current Medicinal Chemistry | Review of first- and second-generation TRK small molecule inhibitors. Documents Entrectinib's approved use in NTRK-driven cancers including secretory breast carcinoma, and discusses resistance mechanisms and next-generation agents. |
| [35163586](https://pubmed.ncbi.nlm.nih.gov/35163586/) | 2022 | Review | Int J Molecular Sciences | Review of emerging therapies for chemotherapy-resistant TNBC. Contextualises NTRK inhibitors as an actionable biomarker-driven approach within the broader landscape of targeted agents for difficult-to-treat breast cancer subtypes. |
| [34176200](https://pubmed.ncbi.nlm.nih.gov/34176200/) | 2021 | Case Report/Small Series | The Oncologist | Locally recurrent secretory carcinoma of the breast with NTRK3 gene fusion. Demonstrates clinical case workup, molecular diagnosis workflow, and eligibility for TRK inhibitor therapy — directly applicable to Singapore clinical practice. |
| [41064088](https://pubmed.ncbi.nlm.nih.gov/41064088/) | 2025 | Case Report | Frontiers in Oncology | 72-year-old female with BSC and ETV6::NTRK3 fusion presenting with pleuro-mediastinal metastases 10 years post-mastectomy. Illustrates the late-relapsing biology of BSC and the importance of NTRK3 testing even in delayed recurrence scenarios. |

## Singapore Market Information

Entrectinib is **not currently registered with the Health Sciences Authority (HSA) of Singapore**. No product licences are on record as of the data cut-off date (June 2026).

| Jurisdiction | Brand Name | Approved Indications | Regulatory Status |
|------|------|------|------|
| United States (FDA) | Rozlytrek | ROS1-positive metastatic NSCLC; NTRK fusion-positive solid tumors (tumor-agnostic, ≥12 years) | Approved (2019) |
| European Union (EMA) | Rozlytrek | ROS1-positive advanced NSCLC; NTRK fusion-positive solid tumors | Approved (2020) |
| Japan (PMDA) | Rozlytrek | NTRK fusion-positive solid tumors; ROS1-positive NSCLC | Approved (2019) |
| Singapore (HSA) | — | Not registered | Not Marketed |

Any use in Singapore would require either an HSA New Drug Application (NDA) or access via the Special Access Route (SAR) for individual compassionate use cases pending local registration.

## Cytotoxicity

Entrectinib is classified as an antineoplastic targeted therapy. This section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy — Multi-kinase inhibitor (TRK/ROS1/ALK); not conventional cytotoxic |
| Myelosuppression Risk | Low to Moderate (anaemia and neutropenia reported in clinical trials; less severe than conventional cytotoxics) |
| Emetogenicity Classification | Low to Moderate (nausea is a frequently reported adverse effect; routine prophylaxis with high-emetogenic antiemetics not typically required) |
| Monitoring Items | CBC with differential; liver function tests (ALT/AST/bilirubin); renal function; ECG for QTc prolongation; body weight and oedema; neurological/cognitive status (CNS penetration); bone density with prolonged use |
| Handling Protection | Follow institutional cytotoxic drug handling guidelines; consult manufacturer Safety Data Sheet (Roche/Genentech); standard PPE applicable as for all oral targeted oncologics |

Detailed Singapore-specific label warnings are not available in this Evidence Pack. Until local registration is obtained, refer to the Rozlytrek EU SmPC or US Prescribing Information for complete toxicity and handling guidance.

## Safety Considerations

Singapore-specific package insert data (HSA label, TFDA package insert) is not available in this Evidence Pack. Please refer to the **Rozlytrek EU Summary of Product Characteristics (SmPC) or US Prescribing Information (USPI)** for complete warnings, contraindications, and drug-drug interaction information.

Based on published literature and internationally approved labels, the following class-effect safety signals are relevant:

- **CNS adverse effects**: Entrectinib has robust CNS penetration — a therapeutic advantage for brain metastases, but also a source of CNS-related adverse events including cognitive impairment, mood changes, dizziness, and ataxia requiring monitoring and dose adjustment
- **QTc prolongation**: Cardiac monitoring (baseline and periodic ECG) is recommended; caution in patients with pre-existing QTc prolongation or concomitant QTc-prolonging agents
- **CYP3A4 drug interactions**: Entrectinib is a CYP3A4 substrate; strong CYP3A4 inhibitors (e.g. azole antifungals, certain HIV antiretrovirals) significantly increase Entrectinib exposure, while strong inducers (e.g. rifampicin, phenytoin) may reduce efficacy — formal DDI review is essential given breast cancer patients' polypharmacy profile
- **Weight gain and oedema**: Commonly reported; monitor fluid status particularly in patients with cardiac comorbidities
- **Hepatotoxicity**: Liver function monitoring recommended; potential for drug-induced liver injury

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (Female Breast Carcinoma)**

**Rationale:**
Female breast carcinoma with NTRK3 fusion (secretory carcinoma subtype) and ROS1 rearrangement (invasive lobular carcinoma subtype) represents a **target-driven, biomarker-selected** repurposing opportunity with Phase 2 clinical evidence from multiple studies. The STARTRK-2 basket trial (n=534) already included these patients and contributed to regulatory approval in the US, EU, and Japan. The active ROSALINE trial specifically evaluates Entrectinib in ILC. The principal barrier to clinical use in Singapore is the absence of HSA registration and local molecular diagnostic infrastructure — not a lack of supporting evidence.

**To proceed, the following is needed:**

- **HSA regulatory pathway**: Evaluate eligibility for HSA Conditional Approval or Expedited Review; assess whether a reliance pathway based on existing FDA/EMA approval of Rozlytrek is available; consider interim access via the Special Access Route (SAR) for individual patients with confirmed NTRK or ROS1 fusion-positive breast cancer
- **Molecular diagnostic access**: Establish or confirm availability of NTRK fusion testing (pan-TRK IHC screening + FISH or NGS confirmation) and ROS1 FISH/NGS testing in Singapore-accredited pathology laboratories — biomarker selection is a prerequisite for any use of Entrectinib
- **Full safety documentation**: Obtain Rozlytrek SmPC/USPI and conduct a structured drug interaction review addressing CYP3A4 interactions and QTc risk in the intended breast cancer population; fill identified data gaps DG001 (label warnings) and DG002 (MOA documentation)
- **Multidisciplinary clinical review**: Engage medical oncology, breast surgery, pathology, and pharmacy teams to define institutional eligibility criteria (NTRK3 fusion-positive secretory carcinoma; ROS1-rearranged ILC), counselling approach, and monitoring protocol
- **Multiple Endocrine Neoplasia (TxGNN Rank 1)**: Classify as Research Question only; mechanistic investigation of Entrectinib's off-target RET activity in MEN2A/2B context is warranted as a research hypothesis, but no clinical studies currently support this and it should not proceed to clinical evaluation without pre-clinical validation data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

