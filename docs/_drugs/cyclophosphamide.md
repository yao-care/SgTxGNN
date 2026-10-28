---
layout: default
title: Cyclophosphamide
parent: High Evidence (L1-L2)
nav_order: 286
evidence_level: L2
indication_count: 4
last_modified_at: 2026-10-14
description: "Cyclophosphamide: predicted new indication Myeloid leukemia (evidence level L5). Approved use: Lymphoma, plasma cell myeloma…"
monitor_inn: "Cyclophosphamide"
predicted_indications: ["myeloid leukemia", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "lymph node cancer"]
---

# Cyclophosphamide
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **4** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Cyclophosphamide: From Lymphoma and Breast Carcinoma to Myeloid Leukemia
{: .text-alpha }

## One-Sentence Summary

Cyclophosphamide is an alkylating chemotherapy drug, originally used for lymphomas, multiple myeloma, neuroblastoma, breast carcinoma and retinoblastoma, among others.
The TxGNN model predicts it may be useful for **myeloid leukemia**, with **34 clinical trials** and **20 publications** currently supporting this direction.
Most of this evidence concerns transplant conditioning and post-transplant graft-versus-host disease (GVHD) prevention, not cyclophosphamide alone as a leukemia treatment.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Lymphoma, plasma cell myeloma, cutaneous T-cell lymphoma (including mycosis fungoides), neuroblastoma, breast carcinoma, retinoblastoma (from the knowledge-graph indication list; no approved-indication text is recorded for the Singapore licences) |
| Predicted New Indication | Myeloid leukemia |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L2 (one completed randomized Phase 2/3 trial; no completed Phase 3 trials) |
| Singapore Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Cyclophosphamide is an alkylating agent. In the body it is converted to phosphoramide mustard, which cross-links DNA and triggers cell death in rapidly dividing cells. It also suppresses the immune system and depletes lymphocytes. Detailed mechanism-of-action data are not available beyond this general description.

Its original indications are lymphoid and solid cancers that respond to DNA damage, which is the same basic vulnerability found in leukemic cells. In myeloid leukemia, cyclophosphamide is used in two main ways:

- **Conditioning before stem cell transplant**, for example busulfan-cyclophosphamide, to eliminate leukemic cells and make room for donor cells.
- **Post-transplant cyclophosphamide (PTCy)**, which selectively depletes the donor T cells that cause GVHD.

The listed trials largely evaluate these transplant roles, not cyclophosphamide monotherapy for the leukemia itself. The prediction is therefore plausible, but it describes a supportive and combination role rather than a stand-alone new treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | Completed | 19 | Randomized comparison of conventional vs T-cell-depleted unrelated-donor marrow transplant; small study |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | Completed | 107 | Hyper-CVAD (includes cyclophosphamide) plus dasatinib in Ph-positive leukemia; mainly lymphoid, so only indirectly relevant to myeloid disease |
| [NCT05515029](https://clinicaltrials.gov/study/NCT05515029) | Phase 3 | Active, not recruiting | 56 | PTCy with abatacept, vedolizumab and a calcineurin inhibitor for GVHD prevention in children and young adults with blood cancers |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | N/A | Recruiting | 138 | Randomized trial of venetoclax-enhanced BUCY vs standard BUCY conditioning in high-risk AML and MDS |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | Active, not recruiting | 300 | HLA-mismatched unrelated-donor transplant with PTCy in hematologic malignancies |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | Completed | 213 | Cord blood transplant after cyclophosphamide/fludarabine/total body irradiation conditioning |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | Completed | 50 | Clofarabine plus etoposide and cyclophosphamide in pediatric relapsed or refractory acute leukemias |
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | Completed | 25 | Reduced-intensity haploidentical transplant with PTCy in AML and other blood cancers; early phase |
| [NCT02057770](https://clinicaltrials.gov/study/NCT02057770) | Phase 1 | Terminated | 25 | Myeloablative allogeneic or haploidentical transplant with high-dose PTCy in relapsed or refractory AML |
| [NCT00939653](https://clinicaltrials.gov/study/NCT00939653) | Phase 2 | Terminated | 6 | Clofarabine with etoposide and cyclophosphamide in relapsed or refractory AML; too small to interpret |

Most of the trials are early-phase, small or still ongoing.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | Systematic review / network meta-analysis | Bone Marrow Transplant | Compared myeloablative conditioning regimens in adults with AML in remission, with busulfan-cyclophosphamide (Bu/Cy) as a commonly used regimen |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Registry study | Cancer | PTCy vs anti-thymocyte globulin vs both for GVHD prevention in haploidentical transplant for adult AML |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Cohort | Haematologica | 217 AML patients in remission given PTCy-based transplant; 2-year overall survival 77% and event-free survival 72% |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | Busulfan-cyclophosphamide vs fludarabine-busulfan conditioning in AML |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | Cyclophosphamide/fludarabine non-myeloablative vs myeloablative transplant in 165 AML patients; survival outcomes were similar in unadjusted analysis |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | Prognostic factors in haploidentical transplant with PTCy for AML |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Registry study | Bone Marrow Transplant | Cord blood transplant vs haploidentical transplant with PTCy in AML in first remission |
| [36842566](https://pubmed.ncbi.nlm.nih.gov/36842566/) | 2023 | Cohort | Transplant Immunol | PTCy and early mixed donor chimerism in myeloid malignancies, weighing GVHD prevention against relapse risk |
| [14662323](https://pubmed.ncbi.nlm.nih.gov/14662323/) | 2003 | Review | Exp Hematol | Busulfan-cyclophosphamide vs TBI-cyclophosphamide before transplant in AML; results were conflicting |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Cohort | Int J Mol Sci | PTCy after matched-donor transplant in pediatric AML |

No randomized controlled trial publications specific to myeloid leukemia were identified, so the evidence is mainly observational.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00929P | ENDOXAN TABLET 50 mg | Sugar-coated tablet | Not stated in available data |
| SIN01747P | ENDOXAN FOR INJECTION 1 g/vial | Powder for injection solution | Not stated in available data |
| SIN01748P | ENDOXAN FOR INJECTION 500 mg/vial | Powder for injection solution | Not stated in available data |
| SIN00930P | ENDOXAN FOR INJECTION 200 mg/vial | Powder for injection solution | Not stated in available data |
| SIN10355P | CYCRAM FOR INJECTION 1 g/vial | Powder for injection solution | Not stated in available data |

All five licences are valid single-ingredient products. Both oral and injectable forms are available.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High, dose-dependent (leukopenia and neutropenia are common) |
| Emetogenicity Classification | Moderate; high at higher intravenous doses |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes, urinalysis (bladder toxicity) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

These entries are based on the drug class. Please refer to the package insert warnings and precautions for product-specific details.

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, with the main ones below; the first 20 listed are mostly moderate.
  - Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms)
  - Bupropion
  - Aprepitant
  - Metronidazole
  - Nitisinone
  - Troglitazone
  - Sulfonylurea and glinide antidiabetics: chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide, tolazamide, tolbutamide, nateglinide, repaglinide
  - Minor interactions: levofloxacin and ondansetron

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cyclophosphamide is already marketed in Singapore, and many transplant studies include it as a core component of conditioning (busulfan-cyclophosphamide) and PTCy for GVHD prevention in myeloid leukemia. However, there are no completed Phase 3 trials, and the trials test whole regimens rather than cyclophosphamide itself.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Singapore products, which are required before safety screening
- Detailed mechanism-of-action data
- Completed Phase 3 evidence, or a guideline or regulatory basis for the transplant-related indication
- A defined scope, such as conditioning or PTCy use, rather than stand-alone leukemia treatment
- A safety monitoring plan covering myelosuppression, bladder toxicity and the interactions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

