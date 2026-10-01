---
layout: default
title: Alemtuzumab
parent: Low Evidence (L5)
nav_order: 57
evidence_level: L5
indication_count: 10
---

# Alemtuzumab
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

# Alemtuzumab: From an Unstated Original Indication to Hepatic Infarction

## One-Sentence Summary

Alemtuzumab is an anti-CD52 lymphocyte-depleting antibody that is marketed in Singapore, but its original approved indication is not stated in the registration data provided.
The top-ranked TxGNN prediction is **hepatic infarction** (score 94.4%), and it has **no clinical trials and no publications** behind it, so it is a model prediction only.
Better-supported predictions appear further down the list, notably **combined immunodeficiency syndromes** (13 trials, 13 publications), but there alemtuzumab is a transplant-conditioning agent, not a disease-modifying treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data provided |
| Predicted New Indication | Hepatic infarction |
| TxGNN Prediction Score | 94.44% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

**Other predictions with evidence (for context):**

| Rank | Predicted Indication | Score | Evidence Level | Decision |
|------|------|------|------|------|
| 2 | Syndrome with combined immunodeficiency | 93.73% | L3 | Research Question |
| 3 | Hepatic veno-occlusive disease | 93.14% | L4 | Hold |
| 9 | Acquired HLH associated with malignant disease | 89.93% | L4 | Research Question |
| 10 | Hemophagocytic syndrome associated with an infection | 89.93% | L4 | Research Question |

Ranks 4–8 (urothelial carcinoma variants and peliosis hepatis) have no trials or literature and are L5 / Hold.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data was not retrieved from DrugBank. Based on the analysis provided, alemtuzumab is an anti-CD52 antibody that depletes lymphocytes. CD52 is expressed mainly on lymphocytes.

**Hepatic infarction (rank 1):** There is no mechanistic rationale. Anti-CD52 lymphodepletion has no known role in ischemic liver injury. The high score is likely a knowledge-graph artifact and should not be read as evidence of efficacy.

**Combined immunodeficiency (rank 2):** Alemtuzumab is used as T-cell-depleting serotherapy in reduced-intensity conditioning before allogeneic stem cell transplant, which is the definitive treatment for SCID and related disorders. It helps with host lymphodepletion, graft-versus-host disease prophylaxis and engraftment. It does not treat the immunodeficiency itself, and the drug can cause profound immunodeficiency. The KG link is probably driven by co-occurrence in transplant regimens.

**Hemophagocytic lymphohistiocytosis (ranks 9–10):** HLH is driven by uncontrolled T-cell and macrophage activation, so T-cell depletion is biologically plausible. Direct support is limited to one case report in lupus-associated HLH. Alemtuzumab also raises infection and EBV-lymphoproliferation risk, which could worsen infection-triggered HLH.

## Clinical Trial Evidence

**Hepatic infarction (rank 1):** Currently no related clinical trials registered.

**Combined immunodeficiency (rank 2, best-supported prediction):** 13 trials were retrieved; the 10 most relevant are shown. All are early-phase, single-arm or terminated studies, and none is a randomized comparison.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00579137](https://clinicaltrials.gov/study/NCT00579137) | Phase 1/2 | Terminated | 3 | Anti-CD45 plus alemtuzumab and fludarabine conditioning for transplant in SCID/PID; too few patients to be informative |
| [NCT05463133](https://clinicaltrials.gov/study/NCT05463133) | Phase 1/2 | Recruiting | 50 | Alemtuzumab, busulfan and TBI conditioning with IL-6 (± IFN-γ) antagonists for transplant in chronic granulomatous disease |
| [NCT04528355](https://clinicaltrials.gov/study/NCT04528355) | N/A | Recruiting | 50 | Prospective outcomes study of reduced-intensity conditioning with simple alemtuzumab dosing strata in non-malignant disorders |
| [NCT01182675](https://clinicaltrials.gov/study/NCT01182675) | Phase 2 | Terminated | 7 | Alemtuzumab plus plerixafor/filgrastim mobilization, avoiding chemotherapy conditioning, in pediatric SCID |
| [NCT01962415](https://clinicaltrials.gov/study/NCT01962415) | Phase 2 | Recruiting | 100 | Reduced-intensity conditioning for cord blood, marrow or PBSC transplant in non-malignant disorders; alemtuzumab role not confirmed from title |
| [NCT01019876](https://clinicaltrials.gov/study/NCT01019876) | Phase 2/3 | Completed | 38 | Risk-adapted transplant for mixed donor chimerism in non-malignant disease; single-arm design |
| [NCT01821781](https://clinicaltrials.gov/study/NCT01821781) | Phase 2 | Active, not recruiting | 20 | Reduced-intensity preparative regimen for transplant in immune function disorders |
| [NCT02512679](https://clinicaltrials.gov/study/NCT02512679) | Phase 2 | Terminated | 20 | Related-donor transplant protocol for genetic lymphohematological diseases including combined immune deficiency |
| [NCT01652092](https://clinicaltrials.gov/study/NCT01652092) | N/A | Active, not recruiting | 57 | Standard-of-care allogeneic transplant guideline in primary immune deficiencies |
| [NCT07284641](https://clinicaltrials.gov/study/NCT07284641) | Phase 2 | Recruiting | 25 | Reduced-conditioning transplant with TBI for CVID and immune regulatory disorders; drug link unconfirmed |

**Hepatic veno-occlusive disease (rank 3):** Three trials were retrieved (NCT02165007, NCT01596699, NCT02061800). All are transplant-conditioning or graft-manipulation studies in which VOD is only a toxicity concern, not the target, so they offer no support for alemtuzumab as a VOD treatment.

**HLH (ranks 9–10):** Neither retrieved trial tests alemtuzumab for HLH. NCT02255656 is a Phase 4 long-term safety follow-up in multiple sclerosis patients after alemtuzumab (n=1062, completed), and NCT00368355 is a Phase 2 CD34 selection study in transplant.

## Literature Evidence

**Hepatic infarction (rank 1):** Currently no related literature available.

**Combined immunodeficiency (rank 2):** 13 publications were retrieved; 10 are shown. All are cohorts or case reports.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27543157](https://pubmed.ncbi.nlm.nih.gov/27543157/) | 2016 | Cohort | Biol Blood Marrow Transplant | Alemtuzumab/fludarabine/melphalan reduced-intensity conditioning (n=4) vs. myeloablative regimen (n=14) in CGD |
| [21325599](https://pubmed.ncbi.nlm.nih.gov/21325599/) | 2011 | Cohort | Blood | Treosulfan-based conditioning with alemtuzumab in 70 children with primary immunodeficiency |
| [29155317](https://pubmed.ncbi.nlm.nih.gov/29155317/) | 2018 | Cohort | Biol Blood Marrow Transplant | Treosulfan/fludarabine conditioning in 160 children with primary immunodeficiency; UK experience |
| [23131490](https://pubmed.ncbi.nlm.nih.gov/23131490/) | 2013 | Cohort | Blood | International survey of 19 XIAP-deficiency transplants, mostly alemtuzumab-based reduced-intensity regimens; poor outcomes |
| [26073206](https://pubmed.ncbi.nlm.nih.gov/26073206/) | 2015 | Cohort | Pediatr Transplant | Single-center transplant experience (5 patients) in CD40L-deficient hyper-IgM syndrome |
| [18940685](https://pubmed.ncbi.nlm.nih.gov/18940685/) | 2008 | Case series | Biol Blood Marrow Transplant | Campath-1H plus fludarabine rescue for graft failure in 12 children, including 4 with SCID |
| [19471859](https://pubmed.ncbi.nlm.nih.gov/19471859/) | 2009 | Case report | Immunol Res | FOXP3 expression after reduced-intensity transplant for IPEX syndrome |
| [11841458](https://pubmed.ncbi.nlm.nih.gov/11841458/) | 2002 | Case report | Br J Haematol | Non-myeloablative transplant in an adult with Wiskott-Aldrich syndrome |
| [15590388](https://pubmed.ncbi.nlm.nih.gov/15590388/) | 2004 | Cohort | Haematologica | Infectious toxicity of alemtuzumab |
| [18502831](https://pubmed.ncbi.nlm.nih.gov/18502831/) | 2008 | Case report | Blood | EBV-positive lymphoproliferation after alemtuzumab-CHOP for peripheral T-cell lymphoma |

**Hepatic VOD (rank 3), most relevant:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20919852](https://pubmed.ncbi.nlm.nih.gov/20919852/) | 2010 | Phase 1 trial | Leuk Lymphoma | Dose-escalated busulfan with fludarabine/alemtuzumab; late VOD/SOS occurred as a toxicity |
| [22280517](https://pubmed.ncbi.nlm.nih.gov/22280517/) | 2012 | Cohort | Leuk Lymphoma | Eight cases of late-onset VOD/SOS after busulfan/fludarabine/alemtuzumab conditioning |

**HLH (ranks 9–10), most relevant:**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22426581](https://pubmed.ncbi.nlm.nih.gov/22426581/) | 2012 | Case report | J Clin Rheumatol | Alemtuzumab used to treat HLH in systemic lupus erythematosus |
| [34605776](https://pubmed.ncbi.nlm.nih.gov/34605776/) | 2022 | Guideline | Crit Care Med | Consensus guidelines for HLH in critically ill children and adults (indirect evidence) |
| [28621800](https://pubmed.ncbi.nlm.nih.gov/28621800/) | 2017 | Review | Cancer | Consensus review on malignancy-associated HLH in adults |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14919P | LEMTRADA Concentrate for Solution for Infusion 12 mg/1.2 mL | Infusion, solution concentrate | Not stated in the registration record |

The only registered route is injectable (intravenous infusion).

## Safety Considerations

- **Key Warnings and Contraindications:** Please refer to the package insert for safety information. Package insert content was not retrieved.
- **Drug Interactions:** No interaction records were found.
- **Signals from the retrieved literature:** Alemtuzumab is associated with infectious toxicity (PMID 15590388) and EBV-positive lymphoproliferation (PMID 18502831). This is especially relevant to any use in infection-triggered HLH or in already immunodeficient patients.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hepatic infarction, has no supporting trials or literature and no plausible link to CD52 biology. The best-supported prediction, combined immunodeficiency, reflects alemtuzumab's supportive role in transplant conditioning, not a therapeutic effect on the disease. HLH is a plausible research question, based on one case report and indirect guidelines.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which currently block safety screening
- Confirmed mechanism-of-action data and the original approved indication from HSA or DrugBank
- For HLH: prospective or comparative data on alemtuzumab, with an infection and EBV-lymphoproliferation risk assessment
- For immunodeficiency: clarification of whether the goal is a conditioning-regimen indication rather than a disease treatment
- Route compatibility and similarity-to-original assessments, which are still pending

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

