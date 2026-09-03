---
layout: default
title: Mycophenolic Acid
parent: 僅模型預測 (L5)
nav_order: 685
evidence_level: L5
indication_count: 10
---

# Mycophenolic Acid
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

# Mycophenolic Acid: From Organ Transplant Rejection Prevention to Hemoglobinopathy

## One-Sentence Summary

Mycophenolic acid (as mycophenolate mofetil/MMF) was originally developed as an immunosuppressant for the prevention of acute organ transplant rejection. The TxGNN model predicts it may also support treatment of **hemoglobinopathy** (e.g., sickle cell disease, thalassemia) — not as a disease-modifying drug, but as the standard immunosuppressive backbone for curative allogeneic stem cell transplantation — with **27 clinical trials** and **9 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prevention of acute organ (renal) transplant rejection *(per literature record in this evidence pack; no Singapore registration data available)* |
| Predicted New Indication | Hemoglobinopathy |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism-of-action data for this drug record is not yet available (marked as a data gap). However, the literature captured in this evidence pack independently documents the mechanism: mycophenolic acid (MPA), the active metabolite of MMF, is a selective, reversible inhibitor of inosine monophosphate dehydrogenase (IMPDH), blocking the de novo pathway of guanine nucleotide synthesis. Because proliferating T and B lymphocytes depend heavily on this de novo pathway (unlike most other cell types, which can use a salvage pathway), MPA acts as a lymphocyte-selective cytostatic and immunosuppressive agent (PMID 1826793, 9399601).

MMF was originally developed and approved for prevention of acute renal allograft rejection, used in combination with a calcineurin inhibitor (cyclosporine/tacrolimus) and corticosteroids (PMID 9399601, 9646007). Hemoglobinopathies such as sickle cell disease and beta-thalassemia major are increasingly managed with curative allogeneic hematopoietic stem cell transplantation (HSCT) — a procedure that requires the same class of graft-versus-host disease (GVHD) prophylaxis MMF already provides in solid-organ transplantation. The TxGNN signal therefore does not imply MMF treats hemoglobinopathy directly; rather, it captures MMF's role as the standard-of-care immunosuppressive companion drug (with tacrolimus/cyclosporine) that enables safe engraftment in these HSCT protocols.

Since GVHD is fundamentally a donor-lymphocyte-driven alloimmune process, MPA's lymphocyte-selective antiproliferative mechanism extends naturally from solid-organ transplant to the HSCT setting for hemoglobinopathies — a link already reflected in a substantial body of registered trials and supporting literature.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00919503](https://clinicaltrials.gov/study/NCT00919503) | Phase 2 | Completed | 98 | Treosulfan-based (± low-dose radiation) reduced-toxicity conditioning before allo-HSCT for nonmalignant diseases incl. hemoglobinopathies; MMF part of standard GVHD prophylaxis |
| [NCT03263559](https://clinicaltrials.gov/study/NCT03263559) | Phase 2 | Completed | 95 | Reduced-intensity haploidentical BMT for symptomatic sickle cell disease (BMTCTN1507); MMF core immunosuppressive agent |
| [NCT03121001](https://clinicaltrials.gov/study/NCT03121001) | Phase 2 | Recruiting | 50 | HLA-haploidentical HSCT with TBI + fludarabine/cyclophosphamide conditioning for clinically aggressive sickle cell disease; MMF as adjunct immunosuppressant |
| [NCT03924401](https://clinicaltrials.gov/study/NCT03924401) | Phase 2 | Active, not recruiting | 30 | Abatacept added to tacrolimus + MMF to prevent acute/chronic GVHD in pediatric non-malignant unrelated-donor HSCT (ASCENT) |
| [NCT01050855](https://clinicaltrials.gov/study/NCT01050855) | Phase 2 | Active, not recruiting | 75 | Reduced-intensity conditioning for non-malignant disorders; evaluates engraftment/toxicity with MMF-based GVHD prophylaxis |
| [NCT03249831](https://clinicaltrials.gov/study/NCT03249831) | Phase 1 | Active, not recruiting | 3 | Non-myeloablative conditioning + CD4-depleted haploidentical transplant to induce mixed chimerism in sickle cell disease |
| [NCT01810588](https://clinicaltrials.gov/study/NCT01810588) | Phase 2 | Active, not recruiting | 270 | Optimal cord unit selection (IPA/NIMA matching) to improve haplo-cord transplant outcomes |
| [NCT00489281](https://clinicaltrials.gov/study/NCT00489281) | Phase 2 | Terminated | 43 | Non-myeloablative HLA-mismatched/matched BMT for sickle cell anemia and other hemoglobinopathies |
| [NCT01850108](https://clinicaltrials.gov/study/NCT01850108) | N/A | Unknown | 26 | Non-myeloablative partially HLA-mismatched/matched BMT for sickle cell disease and other hemoglobinopathies |
| [NCT01350232](https://clinicaltrials.gov/study/NCT01350232) | N/A | Terminated | 2 | Novel reduced-intensity preparative regimen for allogeneic HSCT in sickle cell anemia from matched/partially-matched related donors |

*17 additional trials in this indication area are on record but not yet graded for relevance (see evidence pack for full list).*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Review (PK modeling) | European Journal of Drug Metabolism and Pharmacokinetics | Population pharmacokinetic model proposing MMF off-label dosing regimen for pediatric thalassemia patients undergoing HSCT |
| [15126382](https://pubmed.ncbi.nlm.nih.gov/15126382/) | 2004 | Review | Genetics | General review on genetics-medicine interface by MPA's discoverer; limited direct relevance (abstract unavailable) |
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Cohort | Transplantation and Cellular Therapy | Retrospective study: boosting immunosuppression with MMF helps maintain mixed chimerism and prevent graft failure in thalassemia transplants |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Cohort | Biology of Blood and Marrow Transplantation | Alternative-donor HSCT with post-transplant cyclophosphamide for nonmalignant disorders incl. hemoglobinopathies, reducing graft failure/GVHD risk |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Cohort | Biology of Blood and Marrow Transplantation | Stable long-term donor engraftment in 7 sickle cell disease patients after reduced-intensity HSCT with MMF-containing regimen |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Cohort (Phase 1 trial) | Biology of Blood and Marrow Transplantation | Unrelated cord blood transplant for SCD after reduced-intensity conditioning with added thiotepa; Phase I results |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Cohort | Biology of Blood and Marrow Transplantation | First 4 severe SCD patients receiving unrelated-donor HSCT with post-transplant cyclophosphamide plus tacrolimus/MMF for GVHD prophylaxis |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Cohort | Hematology (Amsterdam) | Risk factors for pure red cell aplasia after major ABO-incompatible allo-HSCT (26.1% incidence in a 42-patient cohort) |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case Report | Journal of Perinatology | Neonatal anemia and hydrops fetalis reported after maternal MMF use during pregnancy — a hematologic safety signal |

---

## Singapore Market Information

No marketing authorizations are currently on file — the evidence pack records **0 registered licenses** and a market status of **未上市 (Not Marketed)** for this drug in Singapore.

---

## Safety Considerations

Formal safety data (key warnings, contraindications, drug-drug interactions) is not available in this evidence pack. Please refer to the package insert for safety information.

One relevant safety signal does appear in the supporting literature: a case report (PMID 17180133) links maternal MMF use during pregnancy to neonatal anemia and hydrops fetalis, indicating a hematologic/reproductive safety concern relevant to any hemoglobinopathy population that may include women of childbearing age.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link is indirect (MMF supports HSCT-based cures rather than treating hemoglobinopathy directly) but is backed by 27 registered trials, including two completed Phase 2 studies (NCT00919503, n=98; NCT03263559, n=95) and consistent supporting literature. This meets an L2 evidence bar, but the drug's fundamental role remains adjunctive/supportive rather than disease-modifying.

**To proceed, the following is needed:**
- Formal safety labeling data (warnings, contraindications) — currently a **blocking** data gap that must be resolved before any safety pre-assessment (S1) can be completed
- Confirmed mechanism-of-action documentation (currently a data gap; this report's mechanistic narrative is reconstructed from supporting literature, not a primary MOA source)
- Drug-drug interaction data (query previously returned no results)
- Clarification that the intended use case is as a GVHD-prophylaxis component of HSCT protocols for hemoglobinopathy, not monotherapy for the underlying disease

*Note: within this same evidence pack, rheumatoid arthritis (rank 9, score 99.18%) also reaches L2 evidence with a "Proceed with Guardrails" recommendation, supported by 22 trials and 20 publications describing decades of off-label MMF use in refractory RA and RA-associated vasculitis/ILD — a candidate worth parallel evaluation.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

