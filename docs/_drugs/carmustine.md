---
layout: default
title: Carmustine
parent: Low Evidence (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Carmustine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Carmustine: From Registered Alkylating Chemotherapy to Lymph Node Cancer

## One-Sentence Summary

Carmustine is a nitrosourea alkylating chemotherapy, marketed in Singapore as an injectable and as an implantable wafer (Gliadel). The registration records supplied contain no approved-indication text.
The TxGNN model predicts it may be effective for **lymph node cancer**, with **7 clinical trials** and **20 publications** attached to this prediction.
Most of that evidence is high-dose combination regimens with stem cell rescue, and the "lymph node cancer" label is ambiguous.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data |
| Predicted New Indication | Lymph node cancer |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L2 (see caveat under Clinical Trial Evidence) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on known information, carmustine is a lipophilic nitrosourea that cross-links DNA strands. In lymphoma it is a component of the BEAM (carmustine, etoposide, cytarabine, melphalan) and CBV high-dose conditioning regimens given before autologous stem cell transplant.

The label "lymph node cancer" is broad. The only Phase 3 trial attached (NCT00002772) is in node-positive breast cancer, not lymphoma. The lymphoma-relevant support comes from Phase 2 BEAM and transplant trials, plus Hodgkin lymphoma literature. Carmustine is rarely the single variable tested in these studies, so its individual contribution is hard to separate.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01141712](https://clinicaltrials.gov/study/NCT01141712) | Phase 2 | Completed | 43 | BEAM (with carmustine) plus autologous transplant in HIV-associated aggressive B-cell and Hodgkin lymphoma; the primary endpoint is overall survival. |
| [NCT00345865](https://clinicaltrials.gov/study/NCT00345865) | Phase 2 | Completed | 473 | Autologous stem cell transplant for lymphoma with ICE-type chemotherapy and rituximab. Carmustine-based conditioning is likely but not confirmed from the title. |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential autologous then haploidentical transplant in high-risk lymphoma, myeloma or CLL. Small, and carmustine's role is not isolated. |
| [NCT01702961](https://clinicaltrials.gov/study/NCT01702961) | N/A | Completed | 75 | Practice study of rituximab with BEAM and autologous transplant in high-risk lymphoma or Hodgkin's disease. |
| [NCT01468311](https://clinicaltrials.gov/study/NCT01468311) | Phase 1/2 | Terminated | 6 | Radiolabelled anti-CD25 with BEAM in refractory Hodgkin lymphoma. Too small to be informative. |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Intensive chemotherapy vs high-dose chemotherapy with stem cell support in breast cancer with 4-9 involved axillary nodes. Not a lymphoma study. |
| [NCT02788201](https://clinicaltrials.gov/study/NCT02788201) | Phase 2 | Completed | 8 | Genomic-guided therapy in advanced urothelial carcinoma. Not relevant to lymphoma. |

**Caveat on the evidence level:** the L2 grade comes from the supplied scoring. The lymphoma-relevant trials are mostly single-arm Phase 2 studies, and the only Phase 3 is in breast cancer. Strictly, no completed Phase 3 or randomised lymphoma trial isolates carmustine.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15767638](https://pubmed.ncbi.nlm.nih.gov/15767638/) | 2005 | RCT | J Clin Oncol | CALGB 9082, SWOG 9114 and NCIC MA-13: high-dose chemotherapy with stem cell support vs intermediate-dose chemotherapy in high-risk primary breast cancer with multiple involved axillary nodes. |
| [7577204](https://pubmed.ncbi.nlm.nih.gov/7577204/) | 1995 | RCT | J Natl Cancer Inst Monogr | CALGB 9082: high-dose vs low-dose cyclophosphamide, cisplatin and carmustine as consolidation in breast cancer with ≥10 involved nodes. |
| [18988286](https://pubmed.ncbi.nlm.nih.gov/18988286/) | 2008 | Randomised Phase 2 | Cancer | GOELAMS trial in 158 high-risk Hodgkin lymphoma patients: early intensification vs ABVD followed by myeloablative chemotherapy and autologous transplant. The supplied excerpt does not name carmustine. |
| [2642573](https://pubmed.ncbi.nlm.nih.gov/2642573/) | 1989 | Clinical study | Leukemia | 23 patients with advanced Hodgkin's disease received BCNU (carmustine), etoposide and cyclophosphamide with autologous marrow. 19 had progressive disease on prior chemotherapy. |
| [15505610](https://pubmed.ncbi.nlm.nih.gov/15505610/) | 2004 | Clinical study | Biol Blood Marrow Transplant | 5-year results of high-dose cyclophosphamide, carmustine and thiotepa with autologous transplant in high-risk breast cancer with nodal involvement. |
| [11895898](https://pubmed.ncbi.nlm.nih.gov/11895898/) | 2002 | PK/clinical study | Clin Cancer Res | Pharmacokinetics of high-dose cyclophosphamide, cisplatin and carmustine in 85 breast cancer patients with ≥10 nodes, related to survival and toxicity. |
| [12523579](https://pubmed.ncbi.nlm.nih.gov/12523579/) | 2002 | Phase 2 | Biol Blood Marrow Transplant | High-dose chemotherapy with hematopoietic support in 61 breast cancer patients with 4-9 involved nodes. |
| [11063378](https://pubmed.ncbi.nlm.nih.gov/11063378/) | 2000 | Registry analysis | Biol Blood Marrow Transplant | 1,111 breast cancer patients given high-dose chemotherapy with stem cell rescue; overall treatment-related mortality was 2.3%. |
| [10473086](https://pubmed.ncbi.nlm.nih.gov/10473086/) | 1999 | Mechanistic study | Clin Cancer Res | O6-alkylguanine-DNA alkyltransferase in cutaneous T-cell lymphoma, and what it implies for alkylating agents such as carmustine. |
| [1642408](https://pubmed.ncbi.nlm.nih.gov/1642408/) | 1992 | Non-randomised trial | Ann Plast Surg | Adjuvant dacarbazine, carmustine, cisplatin and tamoxifen in melanoma with ≥4 positive nodes. |

Most of these papers concern breast cancer with nodal involvement, not lymphoma. They support the "lymph node" wording of the label rather than a lymphoma indication.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15502P | BiCNU-100MG (Carmustine for Injection USP 100 mg) with Dehydrated Alcohol Injection USP, combipack | Injection, powder, for solution | Emcure Pharmaceuticals Limited (OSD and Potent Injectables) |
| SIN13348P | Gliadel Wafer | Implant | Eisai Inc |

The record has no approved-indication text for either licence.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (nitrosourea alkylating agent, DNA cross-linker) |
| Myelosuppression Risk | High. Delayed myelosuppression is a recognised feature of nitrosoureas and should be confirmed against the package insert. |
| Emetogenicity Classification | High at high-dose conditioning doses. Please refer to the package insert. |
| Monitoring Items | CBC with differential, pulmonary function (lung injury after BCNU-containing conditioning is reported), liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations (applies to both the injection and the wafer) |

The myelosuppression and emetogenicity ratings are general drug-class knowledge and are not drawn from the Evidence Pack.

## Safety Considerations

- **Pulmonary toxicity:** a registered trial summary (NCT02278796) notes that BCNU is a common cause of lung injury after high-dose BEAM.
- **Drug interactions:** the drug-interaction query returned no records.

Please refer to the package insert for warnings and contraindications. The Singapore package insert has not yet been obtained.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carmustine-containing high-dose regimens (BEAM/CBV) have a long track record in Hodgkin and non-Hodgkin lymphoma, backed by multiple completed Phase 2 trials. However, no randomised trial isolates carmustine, and the Phase 3 evidence is in breast cancer. This is a plausible repurposing signal, not a confirmed indication.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications, approved indications). This blocks the safety screening.
- Mechanism of action data from DrugBank.
- A defined target: which lymphoma subtype or nodal disease is meant, and whether it is already covered by existing labels.
- Confirmation that carmustine is part of the conditioning regimen in trials such as NCT00345865.
- A safety monitoring plan for myelosuppression and pulmonary toxicity, with supply and cytotoxic-handling arrangements. Carmustine-free alternatives to BEAM (BeEAM, cisplatin substitution) are being studied because of supply and toxicity issues.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

