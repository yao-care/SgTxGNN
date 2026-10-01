---
layout: default
title: Paclitaxel
parent: High Evidence (L1-L2)
nav_order: 746
evidence_level: L1
indication_count: 10
---

# Paclitaxel
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
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

# Paclitaxel: From Cytotoxic Chemotherapy (Original Indication Not Recorded) to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane chemotherapy drug marketed in Singapore under 14 registrations, but the registry extract gives no approved-indication text.
The TxGNN model predicts it for **female breast carcinoma**, with **50 clinical trials** and **20 publications** linked to this prediction.
Paclitaxel is already an established breast cancer treatment, so this result confirms an existing use rather than a true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded (HSA indication text is empty) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not retrieved from DrugBank. The evidence pack does describe paclitaxel as stabilizing microtubules. This causes mitotic arrest and apoptosis in rapidly dividing tumour cells.

Breast cancer is one of the most common settings for taxane chemotherapy. The trial list shows paclitaxel in neoadjuvant, adjuvant and metastatic regimens, alone or with anthracyclines, platinum, HER2-targeted agents, bevacizumab and immunotherapy. Because the mechanism acts on cell division rather than on a specific receptor, it applies across breast cancer subtypes.

Caution: many of the Phase 3 trials use paclitaxel as a backbone or comparator arm rather than as the variable being tested. They support its use in breast cancer but do not isolate its own effect.

## Clinical Trial Evidence

The evidence pack links 50 trials to this prediction. The 10 most relevant are shown below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00991263](https://clinicaltrials.gov/study/NCT00991263) | N/A (biomarker study) | Completed | 3677 | Tumour subtype analysis of paclitaxel benefit in CALGB 9344 and CALGB 9741 cohorts |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3270 | Adjuvant chemotherapy (including weekly paclitaxel) with or without trastuzumab in HER2-low invasive breast cancer |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2005 | Sequential versus concurrent doxorubicin, cyclophosphamide and paclitaxel at 14- or 21-day intervals in node-positive breast cancer |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: two dose-dense, dose-intensified neoadjuvant regimens in high-risk early breast cancer, one built on weekly paclitaxel |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo-ALTTO: neoadjuvant lapatinib, trastuzumab or both plus paclitaxel in HER2-positive breast cancer |
| [NCT01131195](https://clinicaltrials.gov/study/NCT01131195) | Phase 3 | Completed | 139 | Bevacizumab plus paclitaxel versus bevacizumab plus metronomic cyclophosphamide/capecitabine in HER2-negative metastatic disease |
| [NCT00433420](https://clinicaltrials.gov/study/NCT00433420) | Phase 3 | Active, not recruiting | 2000 | EC or FEC followed by paclitaxel, every 3 or 2 weeks with pegfilgrastim, in node-positive breast cancer |
| [NCT00272987](https://clinicaltrials.gov/study/NCT00272987) | Phase 3 | Terminated | 63 | Paclitaxel plus trastuzumab with lapatinib or placebo in ErbB2-overexpressing metastatic breast cancer; stopped early |
| [NCT00915018](https://clinicaltrials.gov/study/NCT00915018) | Phase 2 | Completed | 479 | Neratinib plus paclitaxel versus trastuzumab plus paclitaxel as first-line therapy in ErbB-2-positive disease |
| [NCT07327021](https://clinicaltrials.gov/study/NCT07327021) | Phase 2 | Recruiting | 54 | NOGA: MRI-guided de-escalation of neoadjuvant therapy in stage II-III triple-negative breast cancer |

## Literature Evidence

The evidence pack lists 20 publications, but none is a randomized controlled trial. The 10 most relevant are shown below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Paclitaxel's mechanisms of action, its first-line role in breast cancer, and resistance as a major cause of treatment failure |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Review | Chemical Biology & Drug Design | Paclitaxel combinations and in vivo biomarkers in breast carcinoma, aimed at overcoming drug resistance |
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase II trial | Cancer | Doxorubicin plus paclitaxel in metastatic breast carcinoma, examining the importance of prior adjuvant anthracycline |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase II trial | J Clin Oncol | ECOG study of biweekly paclitaxel and cisplatin in advanced breast carcinoma |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Real-world study | BioMed Research International | Neoadjuvant epirubicin/cyclophosphamide followed by weekly paclitaxel-trastuzumab in HER2-positive breast carcinoma |
| [24068539](https://pubmed.ncbi.nlm.nih.gov/24068539/) | 2013 | Phase I-II trial | Breast Cancer Res Treat | Tipifarnib plus weekly paclitaxel and doxorubicin-cyclophosphamide in locally advanced breast cancer |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical study | Cancer | Role of paclitaxel in multimodality treatment of inflammatory breast carcinoma |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Bulletin review | Drug and Therapeutics Bulletin | Review of paclitaxel and docetaxel licensing in breast and ovarian cancer |
| [39009452](https://pubmed.ncbi.nlm.nih.gov/39009452/) | 2024 | Mechanistic study | J Immunother Cancer | Paclitaxel's effect on tumour-associated macrophages when combined with PD-1 blockade in triple-negative breast cancer |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Translational study | Nature Communications | TEKT4 variations linked to breast cancer resistance to paclitaxel |

## Singapore Market Information

Paclitaxel has 14 registrations in Singapore, and 5 are listed below. The approved-indication text is empty for all of them in the registry extract.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16436P | PACLITERO 100 Solution for Injection 100mg/16.7ml | Injection, solution | Hetero Labs Limited |
| SIN12050P | GENEXOL Injection 6 mg/ml | Injection | Samsung Pharmaceutical Ind Co Ltd |
| SIN14532P | ABRAXANE for Injectable Suspension 100mg/vial | Injection, powder, for suspension | Abraxis BioScience, LLC / Baxter Oncology GmbH |
| SIN14102P | PAXEL Injection 6 mg/ml | Injection, solution, concentrate | Mylan Laboratories Limited |
| SIN13752P | Aclipak Concentrate for Solution for Infusion 6mg/ml | Infusion, solution concentrate | S.C. Sindan-Pharma S.R.L |

All registered forms are injectable. ABRAXANE is the albumin-bound (nab-paclitaxel) formulation, which is distinct from the solution products.

## Cytotoxicity

This section is drawn from general knowledge of the taxane class, not from the Evidence Pack. Confirm it against the package insert.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (taxane, microtubule stabilizer) |
| Myelosuppression Risk | High (neutropenia is the main dose-limiting haematological effect) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, liver function, signs of peripheral neuropathy and hypersensitivity |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information. The HSA warnings and contraindications were not retrieved, and no drug interaction records were found.

Several trials in this evidence set study paclitaxel-related toxicity in breast cancer patients. These include chemotherapy-induced peripheral neuropathy (NCT04932031, NCT03022162, NCT04001829) and subclinical cardiac dysfunction with taxanes (NCT01641562). They show that neuropathy and cardiac effects are recognised concerns, but they are not a substitute for the labelled safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Several completed Phase 3 trials and a very large biomarker analysis (CALGB 9344, n=3677) support paclitaxel in breast cancer. However, this is an existing use, not a new indication, and its Phase 3 evidence is largely combination regimens in which paclitaxel is a background arm. The one Phase 3 trial with paclitaxel in a placebo-controlled design (NCT00272987) was terminated early with only 63 patients.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Approved indication text for each Singapore registration, to confirm whether breast cancer is already labelled
- Detailed mechanism-of-action data from DrugBank
- Confirmation that paclitaxel is the studied variable in the Phase 3 trials cited, and whether findings differ between solution and nab-paclitaxel formulations

Predicted indications ranked 2-10 were not assessed here. Several look like model artifacts, such as Ehrlich tumor carcinoma (a mouse model), nipple carcinoma, and the two rhabdomyosarcoma predictions, which have no clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

