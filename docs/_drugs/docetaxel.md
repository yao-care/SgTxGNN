---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: From Globally Established Antineoplastic to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (Taxotere, DrugBank ID: DB01248) is a globally established taxane antineoplastic agent with regulatory approvals in the US (FDA), EU (EMA), and Japan (PMDA) for breast cancer, NSCLC, prostate cancer, gastric cancer, and head and neck cancer — but is currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a score of **99.90%**,
supported by at least **5 completed Phase 3 RCTs** and **20 publications** spanning HER2-positive, triple-negative, and hormone receptor-positive breast cancer subtypes.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore (HSA) registration |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacology, Docetaxel is a member of the taxane class of antineoplastic agents. It acts by binding to and stabilizing β-tubulin subunits within assembled microtubules, preventing their depolymerization during mitosis and thereby arresting cells in the G2/M phase of the cell cycle — ultimately triggering apoptosis preferentially in rapidly dividing tumor cells. Derived from the needles of *Taxus baccata* (European yew), Docetaxel has been a first- and second-line standard in oncology practice globally for over two decades, with an extensive track record across multiple solid tumor types.

Breast cancer is among the most mitotically active solid tumors, making it inherently vulnerable to microtubule-targeting agents. The disease encompasses biologically distinct subtypes, each with a well-characterized relationship to Docetaxel. In HER2-overexpressing tumors, Docetaxel combined with trastuzumab exerts synergistic antitumor activity: HER2 signal downregulation by trastuzumab sensitizes cells to cell cycle arrest induced by Docetaxel. In triple-negative breast cancer (TNBC) — which lacks established targeted therapy — cytotoxic chemotherapy remains the backbone of treatment, with taxane-based neoadjuvant regimens (EC → Docetaxel, Docetaxel + Carboplatin ± immunotherapy) achieving pathological complete response rates of 40–65%. For hormone receptor-positive/HER2-negative disease, Docetaxel + Cyclophosphamide (TC) is a guideline-endorsed adjuvant option for intermediate-to-high-risk patients.

The TxGNN prediction is therefore mechanistically and clinically grounded: Docetaxel's microtubule-stabilizing action directly targets the high proliferative index that defines breast carcinoma biology across its subtypes. The fact that Docetaxel is not registered in Singapore — despite robust global regulatory approval and an L1-strength evidence base — positions this as a high-priority candidate for HSA registration rather than a speculative repurposing hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|--------------|-------|--------|------------|--------------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant chemotherapy ± trastuzumab in node-positive or high-risk HER2-low invasive breast cancer; compares TC-based regimens (TC×6 or AC→weekly paclitaxel) against each other, with the largest enrollment of any Docetaxel breast cancer trial |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel + Trastuzumab (DH) vs Docetaxel + Carboplatin + Trastuzumab (TCH) as first-line chemotherapy in HER2-amplified advanced breast cancer; a pivotal trial establishing TCH as an anthracycline-sparing standard |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Completed | 736 | Bevacizumab (two doses) + Docetaxel vs Docetaxel + placebo in HER2-negative metastatic breast cancer not previously treated with chemotherapy for metastatic disease; assessed PFS and safety in taxane-eligible patients |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | Completed | 1,384 | EC×4 → Docetaxel×4 vs Epirubicin + Docetaxel×4 → Capecitabine×4 as adjuvant treatment in HER2-negative, node-positive breast cancer; directly compared EC→T to an ET-based experimental arm |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Phase 3 | Completed | N/A | AC followed by weekly or 3-weekly Paclitaxel or Docetaxel in axillary node-positive Stage II/IIIA breast cancer; established optimal scheduling of taxane consolidation after anthracycline |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Triple Negative Trial: Carboplatin vs Docetaxel (standard of care) in ER−/PR−/HER2− metastatic or recurrent locally advanced breast cancer; directly tests Docetaxel as the control arm in TNBC |
| [NCT00464646](https://clinicaltrials.gov/study/NCT00464646) | Phase 2 | Completed | 105 | Epirubicin + Cyclophosphamide followed by Docetaxel + Trastuzumab + Bevacizumab as neoadjuvant (or adjuvant for Stage III) therapy in HER2-positive breast cancer; evaluated cardiac safety and pCR |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | TARMAC study: EC → Docetaxel + Carboplatin in Nigerian women with TNBC; evaluates pCR and blood-based omic biomarkers of chemotherapy resistance in an underrepresented population |
| [NCT05843292](https://clinicaltrials.gov/study/NCT05843292) | Phase 4 | Not Yet Recruiting | 48 | Short-term Sintilimab (PD-1 inhibitor) combined with Taxane + Carboplatin as neoadjuvant therapy in early-stage TNBC; assesses pCR, objective response, and safety in the contemporary chemo-immunotherapy era |
| [NCT01641562](https://clinicaltrials.gov/study/NCT01641562) | N/A | Completed | 60 | Prospective evaluation of subclinical cardiac dysfunction induced by taxane therapy (paclitaxel and docetaxel) in breast cancer; informs cardiac monitoring requirements during Docetaxel treatment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | Phase 3 RCT | J Clin Oncol | ABC Trials (USOR 06-090, NSABP B-46-I, NSABP B-49): TC×6 versus TaxAC (TAC, AC→T, AC→weekly paclitaxel) as adjuvant therapy in early breast cancer; TC6 was non-inferior but not superior to TaxAC, validating Docetaxel-containing regimens as a cornerstone of adjuvant treatment |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Drug Review | J Clin Oncol | Foundational review of Docetaxel's preclinical pharmacology and early clinical trial results; established its mechanism and dose-response in breast and other solid tumors |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Prospective Cohort | Breast Cancer (Tokyo) | DCH (Docetaxel + Cyclophosphamide + Trastuzumab) as neoadjuvant chemotherapy in HER2-positive breast cancer; demonstrated clinically meaningful pCR rates and acceptable tolerability without anthracyclines |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Cohort/Biomarker | Br J Cancer | Microarray gene expression profiling in HER2-positive breast cancer treated with trastuzumab-docetaxel; identified predictive biomarkers of pathological complete response to guide patient selection |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Res Treat | Docetaxel-anthracycline combinations (doxorubicin or epirubicin) in metastatic breast cancer; reviewed mechanistic rationale (non-overlapping toxicity, non-cross-resistance) and Phase II/III trial results |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospective Cohort | Anti-Cancer Drugs | Retrospective investigation of adjuvant Docetaxel-based chemotherapy and breast cancer-related lymphedema; identifies lymphedema as a clinically relevant long-term risk for monitoring |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Critical review of paclitaxel and docetaxel in breast and ovarian cancer; assessed early evidence for licensing extensions and concluded taxoids showed meaningful activity in breast cancer |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | Phase 2 | Oncology | Docetaxel + Vinorelbine combination in metastatic breast cancer; early combination evidence demonstrating Docetaxel's contribution to multi-drug regimen efficacy |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 | Tumori | Dose-finding study of weekly Docetaxel + Gemcitabine as first-line therapy in anthracycline-refractory metastatic breast cancer; established a low-toxicity schedule for taxane-gemcitabine combination |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | Multicenter Phase II study of weekly Docetaxel + Gemcitabine as first-line treatment for metastatic breast cancer; evaluated clinical efficacy, toxicity profile, and dose intensity |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilizing agent) |
| Myelosuppression Risk | **High** — Neutropenia is the dose-limiting toxicity; febrile neutropenia occurs in 10–15% of patients on 3-weekly 75–100 mg/m² regimens; prophylactic G-CSF (filgrastim or pegfilgrastim) is routinely recommended |
| Emetogenicity Classification | Low to moderate — Chemotherapy-induced nausea and vomiting is less prominent than with platinum agents; standard antiemetic prophylaxis (dexamethasone premedication also serves for hypersensitivity and fluid retention) is recommended |
| Monitoring Items | CBC with differential and platelet count before each cycle (ANC ≥1,500/mm³ required before dosing); liver function tests (ALT, AST, total bilirubin, alkaline phosphatase — dose modifications required for hepatic impairment); body weight and fluid retention assessment (peripheral edema, pleural effusion, ascites monitoring); peripheral neuropathy grading |
| Handling Protection | Must follow cytotoxic drug handling regulations; preparation in a vertical laminar flow biological safety cabinet (Class II); personnel PPE required (double gloves, impermeable gown, eye/face protection); disposal as hazardous pharmaceutical waste per local regulation |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel achieves an L1 evidence level for female breast carcinoma, underpinned by at least five large completed Phase 3 RCTs — including the 3,270-patient NSABP B-49 (NCT01275677), the 1,384-patient EC→T adjuvant trial (NCT00129935), the 736-patient AVADO bevacizumab trial (NCT00333775), and the pivotal TCH registration trial (NCT00047255). With global approvals already in place across the US, EU, and Japan, and no Singapore HSA registration currently established, this represents a critical gap in patient access to a proven therapy rather than an exploratory repurposing hypothesis.

**To proceed, the following is needed:**
- Submit HSA (Health Sciences Authority) registration application referencing FDA/EMA approvals and pivotal Phase 3 trial datasets
- Obtain a complete Singapore prescribing information document (SmPC equivalent) with full pharmacovigilance plan
- Resolve the MOA data gap via DrugBank API query (DG002 remediation)
- Acquire TFDA package insert warnings and contraindications for Singapore safety assessment (DG001 remediation)
- Define patient eligibility stratification by breast cancer subtype (HER2 status, ER/PR, nodal involvement, performance status)
- Establish hospital-level cytotoxic drug preparation, handling, and administration protocols prior to formulary listing
- Implement cardiac monitoring protocol to detect taxane-associated cardiotoxicity, particularly in anthracycline-pretreated patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

