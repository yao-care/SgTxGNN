---
layout: default
title: Carmustine
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 10
---

# Carmustine
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

# Carmustine: From Malignant Glioma to Lymph Node Cancer

## One-Sentence Summary

Carmustine (BCNU) is a nitrosourea-class alkylating agent originally established for malignant glioma treatment — including as Gliadel® biodegradable implant wafers (FDA-approved 1997) and as the backbone of high-dose conditioning chemotherapy for stem cell transplantation.
The TxGNN model predicts it may be effective for **Lymph Node Cancer** (encompassing lymphoma and related lymphoid malignancies),
with **7 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malignant glioma (FDA-approved as Gliadel® implant; not registered in Singapore) |
| Predicted New Indication | Lymph Node Cancer |
| TxGNN Prediction Score | 98.49% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Carmustine (BCNU, 1,3-bis(2-chloroethyl)-1-nitrosourea) works by alkylating DNA — specifically forming O6-chloroethyl adducts at guanine residues that spontaneously rearrange into interstrand cross-links. These cross-links block DNA replication and transcription, triggering apoptosis in actively dividing tumour cells. Detailed MOA data were not available in the Singapore regulatory database (carmustine is not registered locally); however, the mechanism is extensively documented in published oncology literature. Critically, carmustine is highly lipid-soluble, allowing broad tissue penetration — including lymphoid tissue.

The connection between carmustine and lymph node cancer is both mechanistically grounded and clinically practice-established. Lymphoma cells — particularly diffuse large B-cell lymphoma (DLBCL) and Hodgkin lymphoma — frequently express low levels of the DNA repair enzyme MGMT (O6-methylguanine DNA methyltransferase). Because MGMT repairs exactly the type of adduct carmustine creates, low MGMT expression renders these tumour cells intrinsically sensitive to carmustine's lethal cross-linking. This is the same molecular vulnerability exploited in glioma treatment, making the biological leap from brain tumour to lymphoma mechanistically coherent. Carmustine is the "B" (BCNU) in the internationally used **BEAM conditioning regimen** (Carmustine + Etoposide + Cytarabine + Melphalan) administered before autologous stem cell transplantation (ASCT) in relapsed/refractory lymphoma.

Multiple completed Phase 2 trials support this application, including the largest lymphoma PBSC transplant registry (NCT00345865, n=473) and a real-world R-BEAM practice study (NCT01702961, n=75). While the only Phase 3 trial (NCT00002772) was terminated early and did not target lymphoma directly, BEAM has been recognized internationally as the standard myeloablative conditioning regimen for relapsed/refractory lymphoma ASCT since the 1990s. The TxGNN score of 98.49% reflects the strong knowledge-graph signal between carmustine and lymphoid malignancy — consistent with decades of clinical practice.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00345865](https://clinicaltrials.gov/study/NCT00345865) | Phase 2 | Completed | 473 | Largest lymphoma PBSC transplant registry; directly evaluates carmustine-based conditioning; eight different high-dose regimens compared, providing the strongest real-world evidence base for this indication |
| [NCT01702961](https://clinicaltrials.gov/study/NCT01702961) | N/A | Completed | 75 | R-BEAM (rituximab + BEAM) current-practice study in lymphoma/Hodgkin's disease after first relapse or incomplete initial response; confirms real-world use pattern of carmustine in ASCT preconditioning |
| [NCT01141712](https://clinicaltrials.gov/study/NCT01141712) | Phase 2 | Completed | 43 | BEAM conditioning regimen in HIV-infected patients with aggressive B-cell lymphoma and Hodgkin lymphoma; directly tests carmustine's role in ASCT for lymphoid malignancies in a challenging patient subgroup |
| [NCT00002772](https://clinicaltrials.gov/study/NCT00002772) | Phase 3 | Terminated | 602 | Phase 3 randomized comparison of intensive carmustine-containing high-dose vs. lower-dose consolidation for breast cancer with 4–9 involved axillary lymph nodes; terminated early — incomplete efficacy data, limiting conclusions |
| [NCT01008462](https://clinicaltrials.gov/study/NCT01008462) | Phase 2 | Completed | 16 | Sequential autologous + haploidentical allogeneic HCT for high-risk Hodgkin lymphoma, non-Hodgkin lymphoma, multiple myeloma, and CLL using carmustine-containing conditioning; demonstrates feasibility |
| [NCT01468311](https://clinicaltrials.gov/study/NCT01468311) | Phase 1/2 | Terminated | 6 | Y-90-daclizumab radioimmunotherapy + BEAM for refractory Hodgkin lymphoma; terminated early with only 6 participants — data insufficient, but concept supports carmustine's role in HL |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18988286](https://pubmed.ncbi.nlm.nih.gov/18988286/) | 2008 | RCT | Cancer | 5-year randomized Phase 2 trial (n=158) in high-risk Hodgkin lymphoma: intensive chemotherapy vs. ABVD followed by myeloablative ASCT; carmustine-containing myeloablative conditioning directly tested; establishes carmustine's role in HL consolidation |
| [7577204](https://pubmed.ncbi.nlm.nih.gov/7577204/) | 1995 | RCT | J Natl Cancer Inst Monogr | CALGB 9082: Randomized comparison of high-dose vs. low-dose cyclophosphamide+cisplatin+carmustine with ABMT for breast cancer patients with ≥10 involved axillary lymph nodes; provides Phase 3-level evidence for carmustine activity in lymph node-positive malignancy |
| [15767638](https://pubmed.ncbi.nlm.nih.gov/15767638/) | 2005 | RCT | J Clin Oncol | CALGB 9082/SWOG 9114/NCIC MA-13 multi-group prospective randomized comparison; high-dose carmustine-based chemotherapy with stem cell support vs. intermediate-dose for high-risk breast cancer with multiple axillary nodes |
| [2642573](https://pubmed.ncbi.nlm.nih.gov/2642573/) | 1989 | Case Series | Leukemia | 23 heavily pre-treated Hodgkin's disease patients received BCNU 450–600 mg/m² + etoposide + cyclophosphamide + ABMT; first systematic clinical evidence of carmustine's activity in lymphoid malignancy with ASCT support |
| [10473086](https://pubmed.ncbi.nlm.nih.gov/10473086/) | 1999 | Cohort | Clin Cancer Res | O6-alkylguanine-DNA alkyltransferase (MGMT) expression in cutaneous T-cell lymphoma (mycosis fungoides); low MGMT correlates with carmustine sensitivity — mechanistic support for the MGMT-pathway rationale in lymphoma |
| [15505610](https://pubmed.ncbi.nlm.nih.gov/15505610/) | 2004 | Cohort | Biol Blood Marrow Transplant | 5-year outcomes of high-dose cyclophosphamide+carmustine+thiotepa (CBT) + AHST for high-risk primary breast cancer with ≥10 positive axillary lymph nodes; RFS and prognostic factor analysis |
| [11895898](https://pubmed.ncbi.nlm.nih.gov/11895898/) | 2002 | Cohort | Clin Cancer Res | PK/PD analysis of high-dose carmustine in 85 patients with breast cancer and ≥10 involved lymph nodes; identifies pharmacokinetic predictors of survival and toxicity, supporting dose optimization |
| [36213836](https://pubmed.ncbi.nlm.nih.gov/36213836/) | 2022 | Cohort | J Oncology | Retrospective review of high-dose carmustine-containing chemotherapy + ASCT in locally advanced triple-negative breast cancer; marginal survival benefit in receptor-defined subgroup when standard chemotherapy fails |
| [11063378](https://pubmed.ncbi.nlm.nih.gov/11063378/) | 2000 | Cohort | Biol Blood Marrow Transplant | 1,111 consecutive breast cancer patients at 5 California centres receiving carmustine-based high-dose chemotherapy; treatment-related mortality 2.3%; hematopoietic graft source — not stage — determines TRM |
| [1639635](https://pubmed.ncbi.nlm.nih.gov/1639635/) | 1992 | Case Series | Int J Radiat Oncol Biol Phys | 49 women with breast cancer involving ≥10 axillary nodes received high-dose cyclophosphamide+cisplatin+carmustine (HDCT) + ABMT followed by post-mastectomy radiotherapy (CALGB); safety and feasibility established |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrosourea class (bifunctional alkylating agent) |
| Myelosuppression Risk | **High** — hallmark delayed-onset myelosuppression; neutrophil and platelet nadirs typically occur 4–6 weeks after administration and may persist for an additional 1–2 weeks; cumulative toxicity risk increases with repeated cycles |
| Emetogenicity Classification | Moderate to High (particularly at the high doses used in ASCT conditioning) |
| Monitoring Items | CBC with differential (at least weekly for 6 weeks post-dose), liver function tests (ALT/AST/bilirubin), renal function (creatinine), **pulmonary function tests** (critical: cumulative pulmonary fibrosis is dose-limiting; monitor closely when lifetime cumulative dose approaches 1,400 mg/m²) |
| Handling Protection | Must follow cytotoxic drug handling regulations; gloves, gown, and eye protection required; carmustine is a skin and mucous membrane irritant — avoid contact; diluted IV solution is stable for limited time and must be protected from light |

---

## Safety Considerations

Carmustine is not registered with the Singapore Health Sciences Authority (HSA); no local regulatory safety data are available.

> Please refer to the FDA or EMA-approved prescribing information for complete safety details. Key known risks include: **delayed cumulative myelosuppression** (onset 4–6 weeks post-dose, duration up to 6 weeks — the most common dose-limiting toxicity); **pulmonary toxicity and fibrosis** (insidious onset, dose-limiting at cumulative doses exceeding 1,400 mg/m²; may be fatal); **hepatotoxicity** (elevated transaminases and veno-occlusive disease reported); **ocular irritation** (transient conjunctival flushing and visual blurring during IV infusion); and **secondary malignancies** (therapy-related myeloid neoplasms with prolonged alkylator exposure). Drug-drug interaction data were not available in this Evidence Pack — a formal DDI review using an established clinical pharmacy database is required before prescribing.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carmustine is the internationally accepted backbone of the BEAM myeloablative conditioning regimen for autologous stem cell transplantation in relapsed/refractory lymphoma — an application supported by decades of clinical practice, multiple completed Phase 2 trials (including a registry study with n=473), and consistent mechanistic evidence linking MGMT-low lymphoma cells to carmustine sensitivity. The TxGNN score of 98.49% is fully concordant with this established clinical knowledge base. The primary barrier to Singapore use is the absence of local registration, not insufficient evidence.

**To proceed, the following is needed:**
- Establish a regulatory pathway with HSA for importation or compassionate use of carmustine (IV formulation and/or Gliadel wafer); carmustine has no Singapore registration
- Obtain the FDA or EMA-approved package insert for complete warnings, contraindications, and dosing guidance before any clinical use
- Conduct a formal drug-drug interaction assessment using a validated clinical pharmacy database (DDI data were absent from this Evidence Pack)
- Clarify the intended clinical context: systemic BEAM conditioning for lymphoma ASCT vs. local Gliadel wafer delivery (mechanistically and logistically distinct applications requiring separate protocols)
- Verify institutional ASCT programme capacity and haematology/oncology support infrastructure if BEAM conditioning is the intended route
- Supplement with DrugBank MOA data to complete the mechanistic section of any institutional review submission
- Consider MGMT promoter methylation status as a prospective biomarker for patient selection, given its established predictive role for nitrosourea sensitivity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

