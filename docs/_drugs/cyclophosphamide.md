---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Cyclophosphamide
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

# Cyclophosphamide: From Lymphoma and Autoimmune Disease to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is a classic broad-spectrum alkylating cytotoxic agent, historically established in the treatment of non-Hodgkin's lymphoma, breast cancer, and autoimmune diseases such as lupus nephritis, but currently carrying no Singapore HSA registration.
The TxGNN model predicts it may be effective for **Myeloid Leukemia** with a confidence score of 99.47%, supported by **multiple Phase 2–3 clinical trials** (including 3 directly high-relevance studies) and **20 publications** — notably, Cyclophosphamide already serves as the backbone of the standard BuCy myeloablative conditioning regimen and post-transplant GVHD prophylaxis (PTCy) in AML/MDS transplantation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Lymphoma, breast cancer, autoimmune diseases (global use; not registered in Singapore) |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved in this evidence pack. Based on established pharmacology, Cyclophosphamide is a prodrug bioactivated in the liver by cytochrome P450 enzymes into phosphoramide mustard — a potent DNA alkylating agent that forms covalent cross-links between DNA strands, halting cell replication. This mechanism is particularly cytotoxic to rapidly dividing cells, including the malignant myeloblasts that characterise acute myeloid leukaemia (AML).

Cyclophosphamide's role in myeloid malignancies extends across two well-established clinical contexts. In myeloablative conditioning prior to allogeneic haematopoietic stem cell transplantation (allo-HSCT), the BuCy regimen (Busulfan + Cyclophosphamide) has been a gold standard for decades, destroying residual leukaemic clones and providing sufficient immunosuppression for donor stem cell engraftment. More recently, post-transplant cyclophosphamide (PTCy — administered on days +3 and +4 after transplant) has become a standard strategy for graft-versus-host disease (GVHD) prophylaxis in haploidentical transplantation for AML and MDS, selectively eliminating alloreactive T cells while preserving the graft-versus-leukaemia effect.

The TxGNN high prediction score (99.47%) reflects the deep mechanistic, preclinical, and clinical evidence base connecting Cyclophosphamide to myeloid malignancies. Both its traditional cytoreductive role in induction/consolidation and its modern immune-modulatory applications in HSCT are extensively documented, making this one of the most strongly supported predictions in this evidence pack.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002549](https://clinicaltrials.gov/study/NCT00002549) | Phase 3 | Unknown | 1,520 | Landmark AML induction Phase 3 trial comparing regimens including MICE (Cyclophosphamide as core component) followed by intensive consolidation and bone marrow transplantation; one of the largest direct AML studies |
| [NCT05823714](https://clinicaltrials.gov/study/NCT05823714) | Phase 2 | Unknown | 70 | Prospective study of Venetoclax + Azacitidine followed by modified BUCY (Busulfan-Cyclophosphamide) as conditioning for high-risk MDS and R/R AML undergoing allo-HSCT |
| [NCT05126849](https://clinicaltrials.gov/study/NCT05126849) | Phase 2 | Recruiting | 31 | Nationwide Phase 2 study of haploidentical allo-HSCT with post-transplant Cyclophosphamide (PTCy) for refractory aplastic anaemia and haematologic malignancies including AML |
| [NCT06786533](https://clinicaltrials.gov/study/NCT06786533) | Phase 1 | Recruiting | 18 | Anti-FLT3 CAR-T cell therapy for R/R AML; Cyclophosphamide used as lymphodepletion conditioning prior to CAR-T infusion, supporting its role in modern cell therapy platforms |
| [NCT00005892](https://clinicaltrials.gov/study/NCT00005892) | N/A | Completed | N/A | Moderate-dose Cyclophosphamide + radiotherapy as conditioning for allogeneic BMT in MDS and acute leukaemia related to Fanconi's anaemia; establishes Cy's efficacy in myeloid disease transplantation |
| [NCT02208037](https://clinicaltrials.gov/study/NCT02208037) | Phase 2 | Completed | 279 | Multi-centre Phase 2 trial (BMT CTN #1203) randomising novel GVHD prevention approaches including PTCy vs standard prophylaxis in allo-HSCT for AML/MDS patients |
| [NCT04678401](https://clinicaltrials.gov/study/NCT04678401) | Phase 1 | Recruiting | 30 | Immunosuppression-free Treg-graft-engineered haploidentical HCT for R/R and ultra-high-risk AML/MDS; Cyclophosphamide included in the conditioning component |
| [NCT03300492](https://clinicaltrials.gov/study/NCT03300492) | Phase 1/2 | Recruiting | 10 | Pre-emptive NK cell immunotherapy after haplo-HSCT with PTCy for AML/MDS; evaluates PTCy as GVHD prophylaxis backbone alongside adoptive immunotherapy |
| [NCT02799147](https://clinicaltrials.gov/study/NCT02799147) | Phase 1/2 | Completed | 27 | Dose-escalation study comparing high-dose post-transplant bendamustine vs PTCy for GVHD prophylaxis in haploidentical SCT for refractory acute leukaemia |
| [NCT00002502](https://clinicaltrials.gov/study/NCT00002502) | Phase 2 | Completed | N/A | Landmark Phase 2 study establishing Busulfan-Cyclophosphamide (BuCy) myeloablative conditioning for allogeneic BMT in patients with acute/chronic leukaemia and MDS unable to tolerate total body irradiation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Comparative Study | Future Oncology | Head-to-head comparison of BuCy vs FluBu myeloablative conditioning for AML allo-HSCT; BuCy remains a standard-of-care reference regimen with comparable efficacy |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Clinical Trial | Transplant Immunology | Cladribine + Busulfan + Cyclophosphamide (ClaBuCy) as intensive conditioning for R/R AML prior to allo-HSCT; demonstrates feasibility and efficacy of Cy-intensified conditioning regimens |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Retrospective Cohort | Haematologica | 217 AML patients in complete remission undergoing HCT with myeloablative conditioning + PTCy-based GVHD prophylaxis; 2-year OS 77%, EFS 72%, confirming prognostic significance of genetic risk classification |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Retrospective Cohort | Bone Marrow Transplantation | Cytogenetic/molecular risk-stratified analysis of conditioning intensity in 1,823 AML patients receiving first HSCT with PTCy; largest study informing personalised Cy-based conditioning strategy |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Retrospective Cohort | European Journal of Haematology | Impact of MAC vs RIC conditioning on AML survival (patients under 65 years) using ATG + PTCy + cyclosporine GVHD prophylaxis; supports individualised conditioning selection |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Retrospective Cohort | Int. Journal of Molecular Sciences | First published data on PTCy after matched sibling and unrelated donor HSCT in paediatric AML patients; demonstrates safety and efficacy of PTCy across age groups |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Retrospective Cohort | Cytotherapy | Identifies prognostic factors in haploidentical HCT with PTCy for AML; provides evidence base for patient selection and donor matching in PTCy-based strategies |
| [32857869](https://pubmed.ncbi.nlm.nih.gov/32857869/) | 2020 | Review | American Journal of Hematology | NK cell alloreactivity in AML in the PTCy era; reviews mechanistic interaction between post-transplant Cyclophosphamide and NK-mediated graft-versus-leukaemia effects |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort Study | American Journal of Hematology | Cy/Flu non-myeloablative allotransplant vs myeloablative allotransplant for AML in remission; comparable long-term event-free and overall survival at median 61-month follow-up |
| [31628924](https://pubmed.ncbi.nlm.nih.gov/31628924/) | 2020 | Comparative Study | Hematology/Oncology and Stem Cell Therapy | BuCy vs BuFlu myeloablative conditioning for allo-HCT in AML and MDS with quality-of-life focus; both standard-of-care options with distinct toxicity and QOL profiles |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic chemotherapy (Nitrogen mustard alkylating agent) |
| Myelosuppression Risk | **High** — Leukopenia, neutropenia, thrombocytopenia, and anaemia are expected and dose-dependent; blood count nadir typically occurs 7–14 days after administration |
| Emetogenicity Classification | **Moderate to High** (dose-dependent); high-dose conditioning regimens carry high emetogenic risk and require scheduled prophylactic antiemetics |
| Monitoring Items | CBC with differential (frequent during and after treatment), hepatic function, renal function (serum creatinine, BUN), urinalysis with urine cytology (haemorrhagic cystitis risk), cardiac function assessment for high-dose regimens, serum electrolytes |
| Handling Protection | Yes — must be prepared and administered according to cytotoxic drug handling regulations; closed-system transfer devices required, appropriate PPE (gloves, gown, eye protection), preparation in a biological safety cabinet or pharmaceutical isolator |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple Phase 2 and Phase 3 clinical trials — including a landmark 1,520-patient randomised study (NCT00002549) and two additional Grade A Phase 2 studies — support Cyclophosphamide's efficacy in myeloid leukaemia across induction, myeloablative conditioning, and post-transplant GVHD prophylaxis settings. The evidence level (L1) is the highest available, and the mechanistic basis is thoroughly established. The primary barriers to immediate clinical use in Singapore are the absence of HSA registration and two unresolved data gaps (package insert safety profile and formal MOA documentation).

**To proceed, the following is needed:**
- Obtain Singapore HSA registration or apply for an import licence / clinical trial exemption before patient use
- Retrieve the full package insert (Singapore HSA or internationally harmonised version) to address Data Gap DG001: warnings, contraindications, and precautions
- Confirm detailed pharmacological MOA from DrugBank API or equivalent authoritative source to address Data Gap DG002
- Define the specific clinical context (direct AML induction vs. HSCT myeloablative conditioning vs. PTCy for GVHD prophylaxis), as each requires a distinct dosing regimen, monitoring schedule, and safety protocol
- Implement mesna uroprotection for all high-dose Cyclophosphamide regimens to prevent haemorrhagic cystitis
- Establish cardiac monitoring protocols for high-dose conditioning regimens
- Include long-term surveillance for therapy-related myeloid neoplasms (t-MDS / t-AML), a recognised late complication of alkylating agent exposure requiring patient counselling and follow-up planning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

