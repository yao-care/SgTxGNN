---
layout: default
title: Doxorubicin
parent: High Evidence (L1-L2)
nav_order: 348
evidence_level: L1
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Cytotoxic Cancer Chemotherapy to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is an anthracycline cytotoxic anticancer drug. The supplied registration data does not state its approved indication text.
The TxGNN model predicts it may be effective for **Ewing sarcoma**, with **47 clinical trials** and **20 publications** retrieved for this direction.
This looks like an already-established standard-of-care use rather than a novel repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the supplied registration data (doxorubicin is a cytotoxic anticancer agent) |
| Predicted New Indication | Ewing sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

The DrugBank mechanism field is not populated for this record, so the mechanism below comes from the report's repurposing rationale, not from DrugBank. Doxorubicin intercalates into DNA and poisons topoisomerase II. This makes it active against rapidly dividing tumours such as small round cell sarcomas.

Doxorubicin is a standard component of the multi-agent regimens used for Ewing sarcoma. These are typically vincristine-doxorubicin-cyclophosphamide alternating with ifosfamide-etoposide (VDC/IE). Several completed Phase 3 and randomized trials of these regimens are in the data.

Two caveats apply:
- Many trial titles are truncated, so doxorubicin's presence in some regimens is inferred rather than confirmed.
- Doxorubicin is a background component, not the variable being tested, so its individual contribution is not isolated.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Randomized dose intensification vs standard treatment in non-metastatic Ewing sarcoma |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to the standard 5-drug regimen (including doxorubicin) in non-metastatic Ewing sarcoma |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Chemotherapy intensification through interval compression in Ewing sarcoma and related tumours |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: combination chemotherapy with or without radiotherapy and/or stem cell transplantation |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multi-agent chemotherapy (including doxorubicin) in newly diagnosed metastatic Ewing sarcoma |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, not recruiting | 437 | Vincristine-irinotecan-regorafenib added to VDC/IE vs VDC/IE alone in metastatic Ewing sarcoma |
| [NCT01313884](https://clinicaltrials.gov/study/NCT01313884) | Phase 2 | Terminated | 3 | Cyclophosphamide/doxorubicin/vincristine alternating with irinotecan/temozolomide in metastatic disease; too small to be informative |
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Completed | 45 | First-line therapy in Ewing tumours with extrapulmonary dissemination; regimen composition not shown |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Intensive therapy with growth factor support for Ewing tumour metastatic at diagnosis; regimen not confirmed |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | Completed | N/A | Vincristine, doxorubicin, cyclophosphamide and dexrazoxane with or without ImmTher in high-risk Ewing sarcoma |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Tested adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma and primitive neuroectodermal tumour of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012: compared the two standard European and US chemotherapy strategies in newly diagnosed Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in newly diagnosed metastatic Ewing sarcoma (Children's Oncology Group) |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (vincristine-doxorubicin-cyclophosphamide alternating with ifosfamide-etoposide) in localized Ewing sarcoma |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | RCT | J Clin Oncol | High-dose treosulfan/melphalan consolidation vs standard therapy in high-risk metastatic Ewing sarcoma |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Trial long-term update | J Clin Oncol | Long-term outcomes of interval-compressed chemotherapy in localized Ewing sarcoma (AEWS0031) |
| [28710342](https://pubmed.ncbi.nlm.nih.gov/28710342/) | 2017 | Retrospective review | Oncologist | Vincristine, ifosfamide and doxorubicin (VID) for initial treatment of Ewing sarcoma in adults |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Dose-intensity analysis | J Natl Cancer Inst | Analysis of published trials on the influence of doxorubicin dose intensity on outcome in osteogenic and Ewing sarcoma |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Chemotherapy raised survival from about 10% to about 75% in localized disease; metastatic disease still fares badly |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Current management: risk-adapted intensive chemotherapy plus surgery and/or radiotherapy |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10992P | K. U. Doxorubicin HCl for Injection 10 mg/vial | Injection, powder, for solution | Not stated in supplied data |
| SIN10991P | K. U. Doxorubicin HCl for Injection 50 mg/vial | Injection, powder, for solution | Not stated in supplied data |
| SIN16102P | Chemodox Concentrate for Infusion 2 mg/ml | Injection, solution | Not stated in supplied data |
| SIN13676P | Ebedoxo 2 mg/ml Injection | Injection, solution, concentrate | Not stated in supplied data |
| SIN10426P | Caelyx Concentrate for Infusion 2 mg/ml | Injection | Not stated in supplied data |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; DNA intercalation and topoisomerase II inhibition) |
| Myelosuppression Risk | High. Ewing regimens containing doxorubicin cause severe myelosuppression, and G-CSF prophylaxis has been reviewed for this setting |
| Emetogenicity Classification | Moderate to high (dose-dependent) |
| Monitoring Items | CBC with differential, cardiac function (anthracycline cardiotoxicity rises with cumulative dose), liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials of multi-agent Ewing sarcoma regimens support this use (L1). These regimens typically include doxorubicin, but it is a background component and its individual contribution is not isolated. This is best read as confirmation of an established standard-of-care use, not new repurposing.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications. This is a blocking data gap for safety screening.
- Mechanism of action data from DrugBank.
- Confirmation that doxorubicin is in the arms of the key trials, since several titles are truncated.
- Singapore approved-indication text for the 11 registrations, to check whether Ewing sarcoma is already covered.
- A cardiac and haematological monitoring plan for the Ewing sarcoma population, which is mostly children and young adults.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

