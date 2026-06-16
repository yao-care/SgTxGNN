---
layout: default
title: Cisplatin
parent: 僅模型預測 (L5)
nav_order: 254
evidence_level: L5
indication_count: 10
---

# Cisplatin
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

# Cisplatin: From Platinum-Based Cancer Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Cisplatin is a platinum-based cytotoxic agent and one of the cornerstones of modern oncology, widely used across multiple solid tumours including testicular, cervical, and ovarian cancers, though its original approved indications are not on file for Singapore.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** — particularly in BRCA-mutated and triple-negative subtypes — with a mechanistic basis grounded in DNA crosslinking and homologous recombination deficiency.
This prediction is currently supported by **46 clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available (Cisplatin is not registered in Singapore) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 97.39% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Formal mechanism of action data was not retrieved from DrugBank for this assessment. Based on established pharmacological knowledge, Cisplatin is a platinum-containing inorganic compound. Once inside a tumour cell, it undergoes aquation to form reactive platinum species that bind covalently to DNA — primarily creating intrastrand crosslinks at GpG and ApG sequences, as well as interstrand crosslinks. These adducts physically obstruct DNA replication and transcription machinery, ultimately triggering apoptosis predominantly via the p53 pathway and mitochondrial cascade.

The key to predicting efficacy in breast carcinoma lies in **Homologous Recombination Deficiency (HRD)**. Cells harbouring BRCA1 or BRCA2 mutations cannot repair Cisplatin-induced DNA crosslinks through HR — a mechanism termed synthetic lethality. Triple-negative breast cancer (TNBC) is the subtype most enriched in BRCA1 mutations and basal-like features, making it selectively vulnerable to Cisplatin at doses tolerable to proficient normal tissues. This mechanistic overlap is well-documented: PMID 33500735 demonstrates that Cisplatin at sub-cytotoxic doses blocks epithelial-mesenchymal transition (EMT) and suppresses breast cancer metastasis; PMID 32124501 identifies CtBP1-driven RAD51 overexpression as a clinically relevant resistance mechanism; and PMID 38043199 shows that the Set7/9 methyltransferase modulates PARP1 expression, altering the threshold for Cisplatin response — collectively establishing BRCA deficiency as the central predictive biomarker for clinical translation.

Crucially, this is not purely theoretical. Multiple Phase II trials have directly tested Cisplatin-based regimens in BRCA-mutated or HER2-positive breast cancers (NCT01670500, NCT01611727, NCT04126525), and a Phase III trial (NCT03201861, n=762) is actively enroling patients to evaluate weekly paclitaxel + Cisplatin as adjuvant therapy for high-risk HER2-negative breast cancer — lending strong clinical plausibility to this TxGNN prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04126525](https://clinicaltrials.gov/study/NCT04126525) | Phase 2 | Active, Not Recruiting | 53 | Neoadjuvant trastuzumab + pyrotinib combined with weekly paclitaxel/cisplatin in HER2+ locally advanced breast cancer; prospective open-label efficacy and safety evaluation |
| [NCT01670500](https://clinicaltrials.gov/study/NCT01670500) | Phase 2 | Completed | 118 | Randomised comparison of neoadjuvant cisplatin vs. doxorubicin/cyclophosphamide (AC) in newly diagnosed breast cancer patients with germline BRCA mutations; directly evaluates cisplatin in a biomarker-selected population |
| [NCT03201861](https://clinicaltrials.gov/study/NCT03201861) | Phase 3 | Recruiting | 762 | Weekly paclitaxel + cisplatin as adjuvant chemotherapy for high-risk, HER2-negative breast cancer; hypothesis that cisplatin improves outcomes vs. standard regimens |
| [NCT01611727](https://clinicaltrials.gov/study/NCT01611727) | Phase 2 | Completed | 20 | Cisplatin monotherapy in BRCA1-positive metastatic breast cancer; one of the first trials to systematically probe cisplatin sensitivity in BRCA1 carriers |
| [NCT00535509](https://clinicaltrials.gov/study/NCT00535509) | Phase 2 | Completed | 285 | Neoadjuvant FEC100 followed by cisplatin-docetaxel ± trastuzumab in HER2-overexpressed or amplified locally advanced breast cancer |
| [NCT02365805](https://clinicaltrials.gov/study/NCT02365805) | Phase 2 | Completed | 30 | Randomised trial of BRCA1 mRNA expression-guided neoadjuvant chemotherapy selection (cisplatin-based vs. taxane-based) in HER2-negative primary breast cancer |
| [NCT01031446](https://clinicaltrials.gov/study/NCT01031446) | Phase 1/2 | Completed | 55 | Cisplatin + paclitaxel + everolimus (mTOR inhibitor) in metastatic breast cancer; investigates potential synergy between platinum-based DNA damage and mTOR blockade |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Intensive sequential chemotherapy (doxorubicin/paclitaxel/cyclophosphamide) vs. high-dose chemotherapy + peripheral stem cell transplant in breast cancer with 4–9 involved axillary lymph nodes; terminated before primary endpoint |
| [NCT02466971](https://clinicaltrials.gov/study/NCT02466971) | Phase 3 | Active, Not Recruiting | 450 | Radiation + cisplatin ± triapine (ribonucleotide reductase inhibitor) in newly diagnosed bulky cervical/vaginal cancer; provides highest-level evidence for cisplatin + radiotherapy combination in gynaecological cancers with mechanistic relevance to HRD tumours |
| [NCT05007106](https://clinicaltrials.gov/study/NCT05007106) | Phase 2 | Completed | 613 | Basket study of pembrolizumab/vibostolimab co-formulation ± other anticancer therapies including cisplatin-based regimens in advanced solid tumours; includes cervical cancer cohort |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [24824628](https://pubmed.ncbi.nlm.nih.gov/24824628/) | 2015 | Phase II Clinical Study | Int J Cancer | Cisplatin (25 mg/m² d1–3) + gemcitabine as first-line therapy in metastatic TNBC (NCT00601159): ORR 37.5%, median PFS 7.0 months; establishes GP as an active regimen specifically in mTNBC |
| [2643295](https://pubmed.ncbi.nlm.nih.gov/2643295/) | 1989 | Clinical Series | Am J Clin Oncol | Cisplatin 100 mg/m² + etoposide 300 mg/m² in 29 evaluable patients with refractory metastatic breast carcinoma: 3 CR + 8 PR (38% response rate); early evidence that platinum is active after prior anthracycline/hormone failure |
| [22593470](https://pubmed.ncbi.nlm.nih.gov/22593470/) | 2012 | Clinical Study | Anticancer Res | Salvage cisplatin + 5-fluorouracil in heavily pretreated metastatic breast cancer; noteworthy activity against liver metastases where other regimens often fail |
| [24344005](https://pubmed.ncbi.nlm.nih.gov/24344005/) | 2013 | Clinical Study | J BUON | Capecitabine + cisplatin doublet in anthracycline- and taxane-pretreated, HER-2 negative metastatic breast carcinoma; evaluates activity and tolerability in a late-line setting |
| [33500735](https://pubmed.ncbi.nlm.nih.gov/33500735/) | 2021 | Preclinical/Mechanistic | Theranostics | At low doses, cisplatin blocks EMT by downregulating vimentin/N-cadherin and upregulating E-cadherin in breast cancer cells; combined with paclitaxel, retards both growth and metastasis — mechanistic basis for anti-metastatic activity |
| [40295796](https://pubmed.ncbi.nlm.nih.gov/40295796/) | 2025 | Network Pharmacology | Sci Rep | Network pharmacology identifies shared targets and converging pathways underlying olaparib + cisplatin synergy in breast cancer; supports PARP-HR axis as the central therapeutic node |
| [32124501](https://pubmed.ncbi.nlm.nih.gov/32124501/) | 2020 | Preclinical/Mechanistic | Mol Carcinog | CtBP1 transcriptionally activates RAD51, conferring cisplatin resistance in breast cancer cells; RAD51 overexpression identified as a druggable resistance biomarker relevant to BRCA-deficient tumours |
| [38043199](https://pubmed.ncbi.nlm.nih.gov/38043199/) | 2024 | Preclinical/Mechanistic | Biochem Biophys Res Commun | Methyltransferase Set7/9 controls PARP1 expression and modulates cisplatin response in breast cancer; epigenetic layer of sensitivity regulation with translational implications for patient stratification |
| [25992773](https://pubmed.ncbi.nlm.nih.gov/25992773/) | 2015 | Preclinical/Mechanistic | Oncotarget | Pit-1 transcription factor downregulates BRCA1 gene expression in breast cancer cells, sensitising them to cisplatin-induced DNA damage; confirms BRCA1 suppression as a mechanism of acquired cisplatin sensitivity |
| [27448297](https://pubmed.ncbi.nlm.nih.gov/27448297/) | 2016 | Review | Tumour Biol | Comprehensive review of miRNA-mediated cisplatin resistance in breast cancer; covers EMT-related miRNAs, DNA damage response modification, and anti-apoptotic pathway upregulation — roadmap for overcoming resistance |

---

## Singapore Market Information

Cisplatin (DrugBank ID: DB00515) currently holds **no marketing authorisation** in Singapore. There are no registered products on file.

> **Note for procurement:** Cisplatin is a long-established generic cytotoxic agent included on the WHO Essential Medicines List and is commercially available worldwide (e.g., as intravenous concentrate from multiple manufacturers). Availability via institutional import or hospital tender should be confirmed with the relevant hospital pharmacy and the Health Sciences Authority (HSA) of Singapore under the applicable regulatory framework for unregistered medicines.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum-based DNA crosslinking agent |
| Myelosuppression Risk | Moderate (leukopenia and thrombocytopenia occur; myelosuppression is generally less severe than with carboplatin at standard doses, but cumulative over multiple cycles) |
| Emetogenicity Classification | **High** — classified as a highly emetogenic agent; requires prophylactic triple antiemetic therapy (5-HT₃ antagonist + NK1 antagonist + dexamethasone) before each dose |
| Monitoring Items | Serum creatinine / eGFR and 24-hour urine output (nephrotoxicity — dose-limiting); CBC with differential (myelosuppression); pure-tone audiogram at baseline and periodically (ototoxicity, especially at cumulative doses); neurological assessment for peripheral neuropathy; serum electrolytes — magnesium, potassium, sodium (electrolyte wasting); liver function tests |
| Handling Protection | Must be prepared and administered according to cytotoxic drug handling regulations; personal protective equipment (gloves, gown, eye protection) required; preparation in a designated biological safety cabinet in pharmacy; waste disposal per cytotoxic waste protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug-drug interactions were not available in this evidence pack (identified as a blocking data gap: DG001). Retrieval from the TFDA package insert PDF and DrugBank API is recommended before any clinical use decision. Of particular importance are contraindications in renal impairment and interactions with other nephrotoxic agents (e.g., aminoglycosides, NSAIDs).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cisplatin's activity in BRCA-mutated and triple-negative breast cancer is supported by multiple completed Phase II trials with direct evidence, an ongoing Phase III trial (NCT03201861, n=762), and a well-characterised mechanistic rationale built on synthetic lethality with HRD. The TxGNN score of 97.39% reflects a prediction strongly consistent with the clinical evidence already in the public domain.

**To proceed, the following is needed:**
- **Safety data retrieval**: Download and parse TFDA package insert PDF to obtain key warnings, contraindications, and drug-drug interactions (DG001 — Blocking severity; required before S1 safety screening)
- **DrugBank MOA data**: Query DrugBank API to formally populate mechanism of action and pharmacokinetic parameters (DG002 — High severity)
- **Patient selection strategy**: Define eligibility criteria based on BRCA1/2 germline/somatic mutation status or validated HRD assay score; TNBC subtype is the primary enrichment strategy
- **Singapore procurement pathway**: Confirm mechanism for importation or hospital-based sourcing of Cisplatin as an unregistered medicine under HSA regulations
- **Renal function threshold**: Establish institution-specific creatinine clearance cut-off (typically ≥60 mL/min) and hydration/antiemetic protocol before first infusion
- **Long-term toxicity monitoring plan**: Pre-specify audiological follow-up and neurotoxicity grading schedule, given cumulative dose-dependent ototoxicity and peripheral neuropathy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

