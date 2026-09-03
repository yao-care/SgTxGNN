---
layout: default
title: Thiotepa
parent: 僅模型預測 (L5)
nav_order: 972
evidence_level: L5
indication_count: 10
---

# Thiotepa
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

# Thiotepa: From High-Dose Conditioning Chemotherapy to Adult Germ Cell Tumor

## One-Sentence Summary

> Thiotepa is a classical alkylating agent whose original approved indication is not registered in this evidence pack — the drug is currently **not marketed in Singapore** (0 licenses), so no local label indication text is available.
> The TxGNN model predicts it may be effective for **Adult Germ Cell Tumor**,
> with **16 clinical trials** and **20 publications** currently identified, several of which directly evaluate thiotepa-based high-dose chemotherapy in germ cell tumor patients.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no registration/license record in the evidence pack (see Safety Considerations) |
| Predicted New Indication | Adult Germ Cell Tumor |
| TxGNN Prediction Score | 98.51% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, no formal mechanism-of-action monograph is available for Thiotepa in this evidence pack (flagged as a High-severity data gap, DG002). Based on the pharmacological information embedded in the repurposing rationale, Thiotepa is an **ethylenimine-class DNA alkylating agent**, non-cell-cycle-specific, that induces DNA interstrand cross-links leading to tumor cell apoptosis.

Although the drug's original, regulator-approved indication is not recorded here, the supporting clinical trial evidence consistently shows Thiotepa being used as a **component of high-dose (myeloablative) conditioning regimens prior to autologous stem cell transplantation**, across a broad range of malignancies — CNS tumors, sarcomas, neuroblastoma, medulloblastoma, and germ cell tumors. This non-selective alkylating mechanism is precisely what makes it applicable across chemosensitive solid tumors, including germ cell tumors.

Specifically for germ cell tumors, high-dose Thiotepa combined with Carboplatin/Etoposide (TCE / CarboPEC regimens) as conditioning before autologous hematopoietic stem cell transplant has long been an **established salvage therapy** in clinical practice for relapsed or refractory disease. The mechanistic rationale is strong, and multiple generations of Phase 2 studies and long-term follow-up cohorts support this use — however, there is no formal Phase 3 RCT or drug-label indication specific to germ cell tumor, so this is best classified as **off-label established practice** rather than a formally approved use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00432094](https://clinicaltrials.gov/study/NCT00432094) | Phase 2 | Completed | 23 | Autologous PBSCT trial specifically titled for Germ Cell Tumors; GCT is highly chemosensitive and poor-risk/relapsed patients can be salvaged with high-dose chemo + ASCT. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | N/A | Completed | 174 | Pilot trial comparing high-dose chemo regimens ± total-body irradiation before autologous transplant, in hematologic malignancies and selected solid tumors (GCT as subgroup). |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemo regimens ± additional therapy before autologous transplant for hematologic malignancy and selected solid tumors. |
| [NCT04684368](https://clinicaltrials.gov/study/NCT04684368) | Phase 2 | Recruiting | 160 | Chemotherapy + response-based craniospinal irradiation for localized non-germinomatous CNS germ cell tumors. |
| [NCT00623077](https://clinicaltrials.gov/study/NCT00623077) | Phase 1 | Terminated | 23 | Dose escalation of total marrow irradiation added to alkylator-intense (thiotepa-containing) conditioning for high-risk/relapsed solid tumors. |
| [NCT00336024](https://clinicaltrials.gov/study/NCT00336024) | Phase 3 | Completed | 91 | RCT comparing induction chemo ± methotrexate before stem cell rescue in supratentorial PNET/high-risk medulloblastoma in children under 36 months. |
| [NCT00003101](https://clinicaltrials.gov/study/NCT00003101) | Phase 2 | Completed | 60 | Intensive chemotherapy + autologous bone marrow/PBSCT for newly diagnosed anaplastic oligodendroglioma. |
| [NCT00007982](https://clinicaltrials.gov/study/NCT00007982) | Phase 2 | Completed | 30 | Intensive BET chemotherapy for selected malignant CNS tumors. |
| [NCT04530487](https://clinicaltrials.gov/study/NCT04530487) | Phase 2 | Terminated | 1 | Allogeneic HSCT (regimen included thiotepa) for pediatric/AYA high-risk solid tumors; terminated with only 1 enrollee. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine chemoprotection with autologous stem cell transplant for high-risk/relapsed pediatric solid and brain tumors. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15143087](https://pubmed.ncbi.nlm.nih.gov/15143087/) | 2004 | Cohort study | J Clin Oncol | Thiotepa-based high-dose chemo + autologous stem-cell rescue directly evaluated in recurrent/progressive CNS germ cell tumors. |
| [11801470](https://pubmed.ncbi.nlm.nih.gov/11801470/) | 2002 | Review | Haematologica | Comprehensive review of high-dose chemotherapy + HSCT status specifically in germ cell tumor patients (salvage and poor-prognosis first-line). |
| [15659420](https://pubmed.ncbi.nlm.nih.gov/15659420/) | 2005 | Phase II multicenter (TAXIF) | Ann Oncol | Sequential high-dose chemo (thiotepa-containing) for relapsed poor-prognosis GCT, supported by autologous stem cell transplant. |
| [16503505](https://pubmed.ncbi.nlm.nih.gov/16503505/) | 2006 | Cohort study | Biol Blood Marrow Transplant | 64 patients over 10 years; intensive chemo + autologous PBSCT across high-, intermediate-, and refractory/relapsed low-risk GCT. |
| [28463397](https://pubmed.ncbi.nlm.nih.gov/28463397/) | 2017 | Cohort study | Int J Cancer | UK/German cohort (58 patients) with relapsed intracranial GCT; assesses value of HDC + autologous stem cell rescue. |
| [15803005](https://pubmed.ncbi.nlm.nih.gov/15803005/) | 2005 | Phase I/II | Am J Clin Oncol | High-dose etoposide/thiotepa/carboplatin (TVCa) + autologous HSC rescue for relapsed or refractory germ cell cancer. |
| [23824533](https://pubmed.ncbi.nlm.nih.gov/23824533/) | 2013 | Cohort study | J Neurooncol | KSPNO S-053 study: myeloablative chemo + autologous SCT in relapsed/progressed CNS germ cell tumors (20 patients). |
| [12483368](https://pubmed.ncbi.nlm.nih.gov/12483368/) | 2002 | Cohort study | Ann Hematol | Amifostine's influence on lymphocyte reconstitution after conventional- and high-dose (thiotepa-containing) chemo in GCT. |
| [11583199](https://pubmed.ncbi.nlm.nih.gov/11583199/) | 2001 | Cohort study | Ann Oncol | Amifostine protection from toxicities of conventional- and high-dose (thiotepa-containing) chemo in germ cell tumor patients. |
| [27749622](https://pubmed.ncbi.nlm.nih.gov/27749622/) | 2017 | Case report | Anticancer Drugs | Plerixafor remobilization of stem cells to support further HDC cycles in a GCT patient relapsing after prior tandem HDC/HSCT. |

---

## Singapore Market Information

Thiotepa currently has **no registration or license record** in Singapore (0 total licenses, market status: Not Marketed). No product-level information is available for this jurisdiction.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Alkylating agent, ethylenimine class) |
| Myelosuppression Risk | High — all identified trials require autologous/allogeneic stem cell rescue due to the myeloablative doses used, indicating severe, dose-limiting myelosuppression |
| Emetogenicity Classification | Moderate to High (consistent with high-dose alkylating agent conditioning regimens) |
| Monitoring Items | CBC with differential and platelet count, renal function, hepatic function, mucositis/infection surveillance during and after conditioning |
| Handling Protection | Must follow institutional cytotoxic/hazardous drug handling protocols |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were available in this evidence pack — this has been flagged internally as a **Blocking data gap (DG001: missing TFDA/HSA label warnings and contraindications)**, which prevents a formal safety pre-assessment (Stage S1).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 studies and long-term cohorts consistently support thiotepa-based high-dose chemotherapy with autologous stem cell rescue as an established salvage approach in relapsed/refractory germ cell tumors, giving reasonably strong (L2) mechanistic and clinical-practice evidence. However, this remains an off-label use with no dedicated Phase 3 RCT, and the drug is not currently registered in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent label data on warnings and contraindications (Blocking gap, DG001) before any safety pre-assessment can be completed
- Detailed mechanism-of-action documentation (DG002) to support the pharmacological rationale
- A formal Singapore registration/import pathway assessment, given the drug is currently not marketed locally
- Confirmation of local availability of the specific dosage forms required for high-dose conditioning use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

