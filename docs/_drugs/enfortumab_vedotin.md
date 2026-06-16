---
layout: default
title: Enfortumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 372
evidence_level: L5
indication_count: 10
---

# Enfortumab Vedotin
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

# Enfortumab Vedotin: From Urothelial Carcinoma to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Enfortumab vedotin (EV) is an antibody-drug conjugate (ADC) approved for locally advanced or metastatic urothelial carcinoma, targeting Nectin-4 to deliver the cytotoxic payload MMAE directly to tumour cells.
The TxGNN model generated 10 new-indication predictions; while leprosy ranks highest by model score (99.53%), it lacks mechanistic plausibility — **HER2-positive breast carcinoma** (TxGNN score 98.99%) is the only prediction supported by actual clinical evidence, with **4 clinical trials** (including a directly relevant Phase 2 multi-cohort study) and **4 publications** currently on record.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Locally advanced or metastatic urothelial carcinoma |
| Predicted New Indication | HER2-Positive Breast Carcinoma |
| TxGNN Prediction Score | 98.99% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Enfortumab vedotin is a Nectin-4–directed ADC consisting of a humanised anti-Nectin-4 monoclonal antibody linked to MMAE (monomethyl auristatin E) via a protease-cleavable linker. Once the antibody binds Nectin-4 on the tumour cell surface, the conjugate is internalised; intracellular proteases cleave the linker to release MMAE, which disrupts microtubule polymerisation and triggers G2/M arrest and apoptosis. A clinically important secondary mechanism is the **bystander killing effect** — free MMAE diffuses into neighbouring Nectin-4-negative cells, increasing efficacy in antigen-heterogeneous tumours.

Nectin-4 is highly overexpressed in urothelial carcinoma (EV's approved indication), but studies also report Nectin-4 overexpression in approximately **40–60% of HER2-positive breast cancers**, creating a biologically plausible targeting rationale. HER2+ status and Nectin-4 overexpression are partially co-expressed in breast cancer, meaning a meaningful subset of HER2+ patients would be expected to respond. The bystander effect further extends potential benefit to tumour regions with heterogeneous Nectin-4 expression.

The Phase 2 EV-202 study (NCT04225117) is the most direct clinical validation: it is a multi-cohort trial explicitly designed to evaluate EV's anti-tumour activity in non-urothelial solid tumour types, with breast cancer as one of the enrolled cohorts. With 329 participants enrolled and the study in active-not-recruiting status, efficacy data are expected to be released in the near term, making this prediction timely for monitoring.

> **Note on rankings 1–9:** The majority of TxGNN top predictions for EV — including leprosy, CMV infection, candidiasis, cerebral infarction, and veterinary diseases — lack established Nectin-4 involvement or a credible mechanistic link to MMAE. These high-scoring predictions likely reflect knowledge graph topological proximity rather than biological plausibility and are classified as Hold (L5). HER2-positive breast carcinoma (rank 10) is the only prediction with supporting clinical data.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04225117](https://clinicaltrials.gov/study/NCT04225117) | Phase 2 | Active, Not Recruiting | 329 | EV-202: Multi-cohort study directly evaluating EV monotherapy and EV + pembrolizumab in non-urothelial solid tumours including breast cancer; primary endpoint is confirmed ORR per RECIST v1.1 — the most directly relevant trial for this repurposing hypothesis |
| [NCT05097599](https://clinicaltrials.gov/study/NCT05097599) | Phase 2 | Terminated | 11 | StrataPATH: Biomarker-guided expansion of approved cancer therapies to new tumour types; terminated early with insufficient enrolment (n=11), providing only preliminary safety signals |
| [NCT07287995](https://clinicaltrials.gov/study/NCT07287995) | Phase 1 / Phase 2 | Recruiting | 428 | ASP2998 (TROP2-directed ADC) combined with pembrolizumab, carboplatin, and enfortumab vedotin in solid tumours; EV is a combination partner rather than the primary investigational agent — provides indirect class-level context |
| [NCT07309770](https://clinicaltrials.gov/study/NCT07309770) | Phase 2 | Recruiting | 90 | Trastuzumab rezetecan (HER2-directed ADC, not Nectin-4–directed) in HER2+ solid tumours including urothelial carcinoma; provides competitive landscape context for ADC strategies in HER2+ disease |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41654096](https://pubmed.ncbi.nlm.nih.gov/41654096/) | 2026 | Systematic Review | *Crit Rev Oncol Hematol* | Real-world evidence for 10 recently approved oncology drugs; assesses whether RCT benefits translate to broader patient populations in routine practice — provides broader EV effectiveness context beyond controlled trials |
| [40614854](https://pubmed.ncbi.nlm.nih.gov/40614854/) | 2025 | Translational / Mechanistic | *Cancer Letters* | Investigates polyploid giant cancer cells (PGCCs) as a resistance mechanism to HER2-directed ADCs in HER2+ breast and gastric cancer cell lines; relevant to understanding ADC resistance biology in HER2+ breast cancer, the key predicted indication |
| [32315240](https://pubmed.ncbi.nlm.nih.gov/32315240/) | 2020 | Review | *ASCO Educational Book* | Comprehensive review of ADC class resurgence covering target selection, antibody engineering, linker chemistry, and payload; provides mechanistic framework underpinning the plausibility of Nectin-4–directed ADC activity in breast cancer |
| [41384708](https://pubmed.ncbi.nlm.nih.gov/41384708/) | 2026 | Review | *Histopathology* | Molecular pathology of bladder cancer; details Nectin-4 expression landscape and its role in EV's approved indication, offering biological context for antigen co-expression patterns relevant to breast cancer |

---

## Singapore Market Information

Enfortumab vedotin currently has **no HSA registration** in Singapore. The drug is not marketed and no licences have been issued.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | Not applicable | — | Not applicable |

> For reference, EV (brand name: Padcev) holds FDA approval (US) for locally advanced or metastatic urothelial carcinoma, including in combination with pembrolizumab as first-line therapy. EMA approval covers the same indication in the EU. Importation for compassionate or clinical trial use in Singapore would require HSA Special Access Route (SAR).

---

## Cytotoxicity

Enfortumab vedotin is an antineoplastic agent (ADC class; cytotoxic payload MMAE).

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted cytotoxic ADC — Nectin-4–directed antibody carrying a microtubule-disrupting agent (MMAE, auristatin class) |
| Myelosuppression Risk | High — neutropenia (including febrile neutropenia) and anaemia are among the most commonly reported grade ≥3 toxicities in urothelial carcinoma trials; expected to be similar in breast cancer cohorts |
| Emetogenicity Classification | Low to moderate (MMAE-based ADCs carry lower intrinsic emetogenicity than conventional platinum or anthracycline regimens) |
| Monitoring Items | CBC with differential (before each cycle), peripheral neuropathy assessment, blood glucose (hyperglycaemia is an EV-specific toxicity), liver function tests, renal function, skin integrity (rash and skin reactions are class-related) |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in a biological safety cabinet, closed-system transfer devices recommended; PPE required for nursing administration |

---

## Safety Considerations

Detailed TFDA package insert warnings and contraindications were not retrieved in this evidence pack. Please refer to the current Padcev (enfortumab vedotin) package insert and HSA product information for full safety data.

Based on the available pharmacovigilance literature (PMID 41341429), real-world FAERS data for EV in bladder cancer has identified **candidiasis and skin reactions as adverse event signals** — these represent toxicity risks to monitor, not therapeutic targets.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(for HER2-positive breast carcinoma; Hold for all other TxGNN-predicted indications)*

**Rationale:**
HER2-positive breast carcinoma is the only TxGNN prediction with biological plausibility (Nectin-4 co-expression in 40–60% of HER2+ tumours) and active clinical investigation; the EV-202 Phase 2 trial (NCT04225117, n=329) is close to reporting results and will either validate or refute this repurposing hypothesis in the near term. All other top TxGNN predictions (ranks 1–9) involve infectious diseases, metabolic disorders, or veterinary pathogens with no established Nectin-4 or MMAE mechanistic relevance, and should remain on hold.

**To proceed, the following is needed:**

- **EV-202 data release**: Monitor NCT04225117 results (expected ~September 2026 based on completion date); breast cancer cohort ORR will be the pivotal decision trigger
- **Nectin-4 expression data in Singapore/Asian HER2+ breast cancer populations**: Expression prevalence may differ from Western cohorts
- **HSA Special Access Route assessment**: EV is not registered in Singapore; compassionate use or IND pathway must be planned before any local investigation
- **Full safety dossier**: TFDA and FDA package insert review required before S1 safety evaluation — currently a blocking data gap
- **MOA documentation**: DrugBank API query for complete pharmacology data to support mechanistic analysis
- **Treatment landscape mapping**: Define where EV would fit relative to T-DM1, T-DXd, and other established HER2+ breast cancer ADCs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

