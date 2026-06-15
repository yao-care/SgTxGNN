---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 315
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Pancreatic Cancer to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a conventional cytotoxic nucleoside analog with established global approvals for pancreatic cancer, non-small cell lung cancer, and bladder cancer, though it currently holds no registration in Singapore.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, a prediction strongly grounded in biology — the FDA has already approved Gemcitabine (in combination with paclitaxel) for metastatic breast cancer following anthracycline failure.
This direction is supported by **over 50 clinical trials** and **20 publications** identified in the evidence review, with multiple completed Phase 3 RCTs underpinning an **L1 evidence level**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pancreatic cancer (primary global approval; no Singapore registration on record) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not marketed (0 HSA registrations) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Gemcitabine is a pyrimidine nucleoside antimetabolite. After intracellular phosphorylation, it competitively inhibits DNA polymerase (causing chain termination) and irreversibly inhibits ribonucleotide reductase (RRM1), depleting the deoxynucleotide pools needed for DNA synthesis. This leads to S-phase arrest and apoptosis. Critically, Gemcitabine exhibits **self-potentiation**: by depleting dCTP pools, it increases its own incorporation into DNA, amplifying cytotoxicity — a property that makes it particularly effective in rapidly dividing epithelial tumours.

Breast cancer cells are known to overexpress RRM1, making them mechanistically susceptible to Gemcitabine. More importantly, Gemcitabine and taxanes (paclitaxel, docetaxel) display complementary and synergistic mechanisms: taxanes stabilise microtubules and arrest cells in G2/M, while Gemcitabine drives S-phase arrest and sensitises tumour cells to subsequent DNA damage. This synergy is not merely theoretical — the FDA has formally approved **Gemcitabine + Paclitaxel** for metastatic breast cancer that has progressed after anthracycline-containing chemotherapy, making this one of the most scientifically validated repurposing examples in oncology.

The TxGNN score of 99.98% is therefore not surprising: the knowledge graph correctly identifies the mechanistic and clinical overlap between Gemcitabine's established oncology profile and breast cancer biology. The absence of Singapore registration reflects a regulatory filing gap rather than a clinical evidence gap. A robust body of Phase 2 and Phase 3 trial data — spanning adjuvant, neoadjuvant, and metastatic settings — across multiple breast cancer subtypes (TNBC, HER2+, HR+) exists globally, providing a strong foundation for regulatory consideration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | Unknown | ~800 | **tAnGo Trial**: Randomised comparison of Paclitaxel–Epirubicin–Cyclophosphamide ± Gemcitabine as adjuvant chemotherapy for ER/PgR-poor early breast cancer — the core Phase 3 RCT directly evaluating Gemcitabine addition in breast cancer adjuvant setting |
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | N/A | Gemcitabine + Paclitaxel vs Paclitaxel alone for unresectable/locally recurrent or metastatic breast cancer — landmark Phase 3 study that formed the basis for FDA approval of this combination |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | Completed | 326 | Maintenance vs observation after achieving clinical response with Gemcitabine + Paclitaxel (GP) first-line chemotherapy in metastatic breast cancer; evaluates durability of GP regimen |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1,206 | Neoadjuvant: Adding Capecitabine or Gemcitabine to Docetaxel before AC ± Bevacizumab in palpable, operable breast cancer; primary endpoint is pathological complete response (pCR) |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Completed | 50 | Weekly nab-Paclitaxel + Gemcitabine for metastatic breast cancer; demonstrates efficacy and safety of this albumin-bound taxane combination |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | Gemcitabine + Trastuzumab + Pertuzumab for HER2-positive metastatic breast cancer after prior anti-HER2–based therapy; evaluates dual HER2 blockade with chemotherapy backbone |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Active, not recruiting | 36 | **ToPCourT**: Trilaciclib + Pembrolizumab + Gemcitabine + Carboplatin for locally advanced or metastatic triple-negative breast cancer (TNBC); assesses myeloprotection combined with immunotherapy–chemotherapy |
| [NCT00027989](https://clinicaltrials.gov/study/NCT00027989) | Phase 2 | Unknown | N/A | Liposomal Doxorubicin (Doxil) + Gemcitabine for metastatic breast cancer; evaluates an anthracycline-avoiding combination in pretreated patients |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | Completed | 30 | Gemcitabine monotherapy for metastatic breast cancer previously treated with doxorubicin and paclitaxel; establishes single-agent activity in heavily pretreated disease |
| [NCT00014456](https://clinicaltrials.gov/study/NCT00014456) | Phase 1 | Completed | 35 | Docetaxel + Gemcitabine + Filgrastim (G-CSF) dose escalation for advanced solid tumours including breast cancer; provides safety profile and recommended doses for combination use |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [14719116](https://pubmed.ncbi.nlm.nih.gov/14719116/) | 2004 | Review (Mechanism) | Int J Oncol | Comprehensive rationale for Gemcitabine in breast cancer: reviews pyrimidine antimetabolite mechanism (self-potentiation, RRM1 inhibition), single-agent and combination activity data |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Semin Oncol | ~20 Phase 2 trials confirm Gemcitabine single-agent response rates of 16–37% in metastatic breast cancer (first-line and refractory); reviews combinations with taxanes, platinum, and targeted agents |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology | Gemcitabine + Paclitaxel in metastatic breast cancer: 52% response rate across Phase 2 trials; reviews scheduling (day 1/8 every 3 weeks vs day 1/14 every 4 weeks) and toxicity management |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review/Meta-analysis | Oncology | Gemcitabine combined with anthracyclines and taxanes for advanced breast cancer; summarises impressive response rates and survival data from prospective studies |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Cohort | Oncology | Gemcitabine + platinum compounds in metastatic breast cancer: significant clinical benefit and response rates documented; positions this combination for anthracycline/taxane-refractory patients |
| [14754468](https://pubmed.ncbi.nlm.nih.gov/14754468/) | 2004 | Retrospective Cohort | Clin Breast Cancer | Gemcitabine + platinum in anthracycline- and taxane-pretreated breast cancer; non–cross-resistant profile and favourable tolerability supports use in sequential therapy |
| [12057038](https://pubmed.ncbi.nlm.nih.gov/12057038/) | 2002 | Review | Clin Breast Cancer | Overview of Gemcitabine as single-agent in advanced breast cancer; describes unique self-potentiation mechanism and role in an era of increasingly complex treatment sequencing |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase 1/2 | Breast Cancer Res Treat | Carboplatin + Gemcitabine + Mifepristone (GR antagonist) for advanced breast and ovarian cancer; demonstrates that GR antagonism with mifepristone enhances Gemcitabine cytotoxicity in GR-positive tumours |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase 1 | Gynecol Oncol | Mirvetuximab soravtansine + Gemcitabine for FRα-positive TNBC (and ovarian/endometrial cancer); establishes MTD and recommended Phase 2 dose for the TNBC cohort |
| [25398698](https://pubmed.ncbi.nlm.nih.gov/25398698/) | 2015 | Cohort | Cancer Chemother Pharmacol | Docetaxel + Gemcitabine + Bevacizumab biweekly for HER2-negative metastatic breast cancer; evaluates activity and safety as salvage chemotherapy in pretreated patients |

---

## Singapore Market Information

Gemcitabine is currently **not registered with the Health Sciences Authority (HSA) of Singapore**. No product authorisations are on record.

| Registration | Status |
|---|---|
| HSA (Singapore) | No registrations found |

> **Context for Decision-Making:** Gemcitabine is widely approved and commercially available in major reference markets. Key approvals include:
> - **FDA (USA):** Pancreatic cancer, NSCLC, bladder cancer, and metastatic breast cancer (in combination with paclitaxel after anthracycline failure)
> - **EMA (Europe):** Pancreatic cancer, NSCLC, bladder cancer, breast cancer, and ovarian cancer
> - **Multiple Asian markets** (Japan, Korea, Taiwan, etc.)
>
> For Singapore clinical use, Gemcitabine may be accessed through the HSA's Special Access Route (SAR) while a formal registration application is pursued.

---

## Cytotoxicity

Gemcitabine is a **conventional cytotoxic antineoplastic agent** classified as a nucleoside analog/antimetabolite. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nucleoside Analog / Antimetabolite (Fluoropyrimidine-related class) |
| Myelosuppression Risk | **High** — Neutropenia is the primary dose-limiting toxicity; thrombocytopenia and anemia are also common. G-CSF support (e.g., filgrastim) is frequently used in combination regimens. Nadir typically at day 8–14 |
| Emetogenicity Classification | **Low to Moderate** — Gemcitabine monotherapy is low emetogenic risk; moderate risk when combined with carboplatin or cisplatin (per MASCC/ESMO classification) |
| Monitoring Items | CBC with differential and platelet count (before each cycle and on day 8); liver function tests (ALT, AST, bilirubin, alkaline phosphatase); renal function (serum creatinine, eGFR); pulmonary function assessment if new respiratory symptoms emerge (risk of gemcitabine-induced pneumonitis) |
| Handling Protection | Cytotoxic handling regulations apply — closed-system drug transfer devices (CSTDs) required for preparation; full PPE (gloves, gown, eye protection) for pharmacists and nurses; dedicated preparation in a biological safety cabinet |

---

## Safety Considerations

Detailed safety data (key warnings, contraindications, drug interactions) were not available in this Evidence Pack.

> Please refer to the current package insert (US Prescribing Information or EU Summary of Product Characteristics) for complete safety information. Known areas of clinical importance include: **pulmonary toxicity** (interstitial pneumonitis, pulmonary oedema), **haemolytic uraemic syndrome (HUS)**, **hepatotoxicity**, **capillary leak syndrome**, and **radiation sensitisation** effects. Formal TFDA/HSA package insert review is required before any clinical application in Singapore (see Data Gap DG001).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The TxGNN prediction of 99.98% is mechanistically justified and clinically validated — Gemcitabine already holds FDA and EMA approval for breast cancer in combination with paclitaxel, underpinned by completed Phase 3 RCTs (tAnGo, NCT00006459) and a large body of Phase 2 evidence across all major breast cancer subtypes. The L1 evidence level represents one of the strongest drug repurposing cases in this dataset. The primary barrier to use in Singapore is the absence of an HSA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway:** Initiate HSA product registration application for the breast cancer indication, using FDA/EMA approvals as reference; in the interim, apply for Special Access Route (SAR) authorisation for individual patients
- **Safety data completion (DG001 — Blocking):** Obtain and review the full package insert (USPI or SmPC), specifically extracting key warnings (pulmonary toxicity, HUS, hepatotoxicity), contraindications, and dose-modification guidelines
- **MOA documentation (DG002 — High):** Retrieve structured mechanism-of-action data from DrugBank API to support clinical decision support integration
- **Subtype targeting strategy:** Define the intended breast cancer subtype(s) — TNBC (Gemcitabine + Carboplatin or + Pembrolizumab), HER2+ (Gemcitabine + Trastuzumab ± Pertuzumab), or HR+ (salvage setting) — and align with current NCCN/ESMO guidelines
- **Drug interaction assessment:** Conduct formal DDI review, particularly for combinations with anti-HER2 agents, immune checkpoint inhibitors, and CDK4/6 inhibitors
- **Local safety monitoring plan:** Develop a site-specific monitoring protocol covering CBC nadir management, pulmonary surveillance, and renal function monitoring appropriate for the Singapore oncology setting
- **Supply chain confirmation:** Verify availability of Gemcitabine (as Gemzar® or approved generic) through licensed Singapore importers or regional distributors
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

