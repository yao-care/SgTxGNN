---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 210
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Platinum-Based Antineoplastic Agent to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum coordination compound used globally as a backbone cytotoxic agent across multiple solid tumours, though it carries no current registration in Singapore.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **50 registered clinical trials** and **20 publications** currently supporting this direction.
Evidence strength is classified at the highest level — **L1** — based on multiple completed Phase 3 randomised controlled trials in both triple-negative (TNBC) and HER2-positive breast cancer subtypes.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Singapore registration (globally indicated for ovarian cancer and other solid tumours) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carboplatin is a platinum coordination compound that works by forming covalent inter-strand and intra-strand DNA cross-links, permanently blocking DNA replication and triggering programmed cell death. Detailed mechanism of action data is not available in the current Evidence Pack. Based on known published literature, Carboplatin belongs to the platinum-based cytotoxic class — mechanistically analogous to cisplatin but with a different toxicity profile, notably lower nephrotoxicity and neurotoxicity — making it clinically preferred in settings where renal preservation or dose-intensive regimens are priorities.

The mechanistic rationale for breast carcinoma is strongest in two molecular subtypes. In **triple-negative breast cancer (TNBC)**, up to 15–20% of tumours harbour germline *BRCA1/2* mutations causing homologous recombination (HR) repair deficiency. Carboplatin-induced DNA cross-links cannot be repaired in HR-deficient cells, triggering apoptosis through a synthetic lethality mechanism — the same biological principle that underlies PARP inhibitor sensitivity. This explains why TNBC, unlike other breast cancer subtypes, shows a particularly large benefit from platinum addition in the neoadjuvant setting. In **HER2-positive breast cancer**, the TCH regimen (Docetaxel–Carboplatin–Trastuzumab) was validated in a landmark Phase 3 trial (BCIRG 006) demonstrating equivalent survival to anthracycline-containing regimens with a substantially better cardiac safety profile, cementing Carboplatin's role in this subtype.

Multiple meta-analyses confirm that adding Carboplatin to standard neoadjuvant chemotherapy significantly improves pathological complete response (pCR) rates in TNBC — a surrogate endpoint strongly associated with improved event-free and overall survival — supporting the TxGNN model's prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Randomised comparison of Docetaxel + Trastuzumab ± Carboplatin in HER2-amplified advanced breast cancer; corresponds to BCIRG 006, establishing the TCH regimen as the anthracycline-free standard for HER2+ disease |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Directly compares Carboplatin vs Docetaxel as monotherapy in metastatic TNBC (ER−/PR−/HER2−); highest-level direct efficacy evidence for Carboplatin in TNBC; n=400 provides adequate statistical power |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, not recruiting | 720 | Randomised trial of weekly paclitaxel alone vs weekly paclitaxel + Carboplatin as neoadjuvant therapy in locally advanced TNBC; large-scale confirmation of pCR benefit from platinum addition |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: dose-dense epirubicin/taxane/cyclophosphamide vs weekly paclitaxel/liposomal doxorubicin ± Carboplatin as neoadjuvant therapy in high-risk early breast cancer; myelosuppression is the primary safety concern |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | Evaluates TCHP (Docetaxel–Carboplatin–Trastuzumab–Pertuzumab) ± oestrogen deprivation in HR+/HER2+ neoadjuvant breast cancer; confirms Carboplatin as the platinum backbone of dual-blockade regimens |
| [NCT07327021](https://clinicaltrials.gov/study/NCT07327021) | Phase 2 | Recruiting | 54 | NOGA: MRI-guided de-escalation trial using Carboplatin in Stage II–III TNBC neoadjuvant therapy; represents the current precision oncology direction — using early MRI response to guide treatment intensity |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | TARMAC: Evaluates pCR rates with epirubicin/cyclophosphamide followed by docetaxel + Carboplatin in Nigerian TNBC patients; addresses critical real-world data gaps in underrepresented populations |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Active, not recruiting | 36 | ToPCourT: Trilaciclib + Pembrolizumab + Gemcitabine + Carboplatin in metastatic TNBC; confirms Carboplatin's central role in next-generation immunotherapy combination strategies |
| [NCT00117442](https://clinicaltrials.gov/study/NCT00117442) | Phase 2 | Completed | 61 | Dose-intensive Carboplatin/Paclitaxel with pegfilgrastim-supported progenitor cell re-infusion in breast cancer; provides dose-escalation and schedule-optimisation data for the combination |
| [NCT04771871](https://clinicaltrials.gov/study/NCT04771871) | Phase 2 | Unknown | 42 | Evaluates microRNA biomarkers in TNBC patients receiving standard chemotherapy including Carboplatin; supports development of blood-based response monitoring tools |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief trial: camrelizumab (anti-PD-1) + platinum-containing neoadjuvant chemotherapy (including carboplatin) in early/locally advanced TNBC; confirms platinum backbone is essential to immunotherapy combination efficacy |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | RCT | Nature Communications | MUKDEN 06 phase 2b RCT comparing ARX788 + pyrotinib vs TCbHP (docetaxel, carboplatin, trastuzumab, pertuzumab) as neoadjuvant for HER2+ breast cancer; validates TCbHP as the current gold-standard comparator |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase 3 RCT | European Journal of Cancer | BROCADE3 final overall survival results: adding veliparib to carboplatin + paclitaxel significantly improved progression-free survival in germline BRCA1/2-mutated, HER2-negative advanced breast cancer; OS data confirm durable benefit |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Quantitative meta-analysis confirming that adding carboplatin to neoadjuvant chemotherapy significantly improves pCR rate in TNBC; key synthesis of RCT-level evidence supporting the prediction |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Medical Oncology | Comprehensive review summarising accumulating preclinical synergy evidence and clinical efficacy data for the paclitaxel–carboplatin combination in advanced breast cancer; covers multiple Phase II cohorts |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I/II Trial | Breast Cancer Research and Treatment | Carboplatin + gemcitabine + mifepristone (glucocorticoid receptor antagonist) in GR-positive advanced breast and ovarian cancer; demonstrates that GR antagonism enhances carboplatin-induced apoptosis, offering a resistance-overcome strategy |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase II Trial | Breast Cancer Research | Phase II trial of bevacizumab + carboplatin specifically in breast cancer brain metastases; demonstrates activity in CNS disease, expanding carboplatin's role to a high unmet-need setting |
| [9516604](https://pubmed.ncbi.nlm.nih.gov/9516604/) | 1998 | Phase II Trial | Oncology | 66-patient phase II study of paclitaxel + carboplatin as first-line in advanced breast cancer (58% with prior anthracycline); establishes early efficacy benchmark for the combination |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Phase II Trial | Seminars in Oncology | Foundational evaluation of paclitaxel alone, carboplatin alone, and their combination in advanced breast cancer; establishes the pharmacological rationale and initial clinical activity data |
| [39944694](https://pubmed.ncbi.nlm.nih.gov/39944694/) | 2025 | Retrospective/Translational | Frontiers in Immunology | Identifies a DNA damage repair (DDR) gene signature associated with carboplatin resistance in breast cancer; links immune infiltration patterns to treatment outcome, informing future patient stratification |

---

## Singapore Market Information

Carboplatin (DrugBank ID: DB00958) is currently **not registered** in Singapore. No Health Sciences Authority (HSA) product licences are on record, and there are no approved product listings available. Carboplatin is widely available internationally as a generic intravenous infusion product and is included in NCCN, ESMO, and major Asian oncology guidelines as a standard-of-care component for breast, ovarian, lung, and other solid tumours.

Institutions in Singapore wishing to use Carboplatin for clinical or research purposes may explore the HSA Special Access Route (SAR) or the Therapeutic Products Regulations framework for importation under authorised clinical use.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum coordination compound (alkylating-like mechanism) |
| Myelosuppression Risk | **High**: Thrombocytopenia is the dose-limiting toxicity (platelet nadir typically Day 14–21 per cycle); neutropenia and anaemia also common; risk is amplified with increasing AUC, renal impairment, and prior chemotherapy exposure |
| Emetogenicity Classification | **Moderate to High** — AUC-dependent: doses targeting AUC ≥4 mg/mL·min are classified as High emetic risk per MASCC/ESMO/ASCO guidelines; prophylactic antiemetic regimen (5-HT3 antagonist + dexamethasone ± NK1 antagonist) required |
| Monitoring Items | Complete blood count with differential and platelet count before each cycle; serum creatinine and estimated GFR (Carboplatin dose is calculated by the Calvert formula: Dose = AUC × [GFR + 25]); electrolytes (magnesium, potassium, calcium); audiometry for high-dose regimens (≥AUC 6–7 per cycle) |
| Handling Protection | Must comply with cytotoxic drug handling regulations — preparation in a negative-pressure biological safety cabinet with closed-system drug transfer devices (CSTD); appropriate personal protective equipment (double gloves, gown, eye protection) for pharmacy and nursing staff; cytotoxic waste disposal per national pharmacy guidelines |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carboplatin has the strongest available evidence level (L1) for use in female breast carcinoma, supported by at least five completed or active Phase 3 randomised controlled trials across TNBC and HER2-positive subtypes, reinforced by a meta-analysis confirming pCR improvement and final OS data from the BROCADE3 trial in BRCA-mutated disease. The mechanistic basis via HR deficiency synthetic lethality in TNBC is well-characterised. However, Carboplatin is not currently registered in Singapore, and formal safety data from the package insert has not yet been reviewed.

**To proceed, the following is needed:**
- **Regulatory pathway**: Initiate HSA Special Access Route application or formal product registration — Carboplatin cannot be prescribed clinically in Singapore without regulatory authorisation
- **Safety data review** (DG001 — Blocking): Obtain and parse the package insert (Paraplatin® or generic equivalent) to extract full warnings, contraindications, and precautions before any safety assessment can be completed
- **MOA documentation** (DG002 — High): Query DrugBank API for Carboplatin (DB00958) to formally document mechanism of action for the mechanistic linkage analysis
- **Biomarker stratification plan**: Define patient selection criteria — at minimum, BRCA1/2 germline testing and/or HR deficiency assay for TNBC; HER2 status confirmation for TCH-regimen eligibility
- **Renal function monitoring protocol**: Establish creatinine clearance baseline and per-cycle monitoring; Carboplatin dosing is entirely GFR-dependent (Calvert formula) — underdosing risks efficacy, overdosing risks severe thrombocytopenia
- **Haematological safety monitoring**: Define platelet count thresholds for dose delay/reduction; consider prophylactic growth factor support (G-CSF) per institutional protocol for high-AUC regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

