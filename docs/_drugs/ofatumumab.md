---
layout: default
title: Ofatumumab
parent: 僅模型預測 (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
---

# Ofatumumab
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

# Ofatumumab: From Chronic Lymphocytic Leukemia to Follicular Lymphoma

## One-Sentence Summary

Ofatumumab (DrugBank DB06650) is a fully human anti-CD20 monoclonal antibody originally developed and globally approved for chronic lymphocytic leukemia (CLL/SLL) refractory to fludarabine and alemtuzumab; it is **not currently registered in Singapore**.
Among the TxGNN model's predicted indications, **Follicular Lymphoma** is the strongest candidate with an actual evidence trail, supported by **15 clinical trials** and **20 publications**, including a randomized Phase 2 trial and a large single-arm registration-supporting study.
Closely related, higher-scoring nodes (CLL/SLL molecular subtypes, and CLL/SLL itself) score even higher on the model but largely restate the drug's known original indication rather than a genuinely new use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic Lymphocytic Leukemia (CLL/SLL), refractory to fludarabine and alemtuzumab — approved elsewhere; not documented in the local (Singapore) registry (data gap) |
| Predicted New Indication | Follicular Lymphoma |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L2 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed DrugBank mechanism-of-action text is not available for this drug (data gap). Based on the supporting literature in this evidence pack, ofatumumab is a fully human IgG1κ anti-CD20 monoclonal antibody that binds a distinct membrane-proximal epitope on CD20 and depletes CD20⁺ B cells primarily through complement-dependent cytotoxicity (CDC), with antibody-dependent cellular cytotoxicity (ADCC) and phagocytosis as secondary mechanisms — a stronger CDC effect than its predecessor rituximab.

Follicular lymphoma and CLL/SLL are both CD20⁺ B-cell lymphoid malignancies within the same "indolent B-cell malignancy" spectrum, and share the same anti-CD20 treatment paradigm already used for rituximab. Multiple trials in this evidence pack (e.g. NCT00394836, PMID 22389254) specifically demonstrate ofatumumab retains activity in **rituximab-refractory** follicular lymphoma, indicating the CDC-driven mechanism provides complementary activity even after resistance to a first-generation anti-CD20 agent.

This extrapolation is further reinforced by the model's related, higher-scoring nodes: two finer CLL/SLL molecular subtypes (IGHV-mutated and pre-germinal-center CLL/SLL) and the general CLL/SLL node itself (evidence level L1, decision stage S3) — all sharing the same CD20 target biology. Because CLL/SLL is essentially the drug's known original use, however, the follicular lymphoma signal represents the more genuinely novel and independently evidenced repurposing opportunity.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01077518](https://clinicaltrials.gov/study/NCT01077518) | Phase 3 | Terminated | 346 | Randomized ofatumumab + bendamustine vs. bendamustine alone in rituximab-refractory indolent B-NHL |
| [NCT01286272](https://clinicaltrials.gov/study/NCT01286272) | Phase 2 | Completed | 135 | Randomized ofatumumab + bendamustine ± bortezomib, head-to-head, in untreated follicular lymphoma |
| [NCT00394836](https://clinicaltrials.gov/study/NCT00394836) | Phase 2 | Completed | 116 | Ofatumumab monotherapy in rituximab-refractory follicular lymphoma (large single-arm study) |
| [NCT02710643](https://clinicaltrials.gov/study/NCT02710643) | Phase 2 | Completed | 110 | MIRO trial: local radiotherapy ± ofatumumab in early-stage (I/II) follicular lymphoma |
| [NCT00823719](https://clinicaltrials.gov/study/NCT00823719) | Phase 2 | Completed | 61 | Ofatumumab + ICE/DHAP salvage chemotherapy pre-autologous transplant in relapsed/refractory aggressive lymphoma |
| [NCT00494780](https://clinicaltrials.gov/study/NCT00494780) | Phase 2 | Completed | 59 | Randomized two-dose ofatumumab + CHOP in previously untreated follicular lymphoma |
| [NCT01190449](https://clinicaltrials.gov/study/NCT01190449) | Phase 2 | Completed | 51 | Ofatumumab monotherapy (CALGB) in previously untreated follicular NHL |
| [NCT01294579](https://clinicaltrials.gov/study/NCT01294579) | Phase 2 | Completed | 49 | Ofatumumab + bendamustine induction with ofatumumab maintenance, relapsed indolent B-NHL |
| [NCT01239394](https://clinicaltrials.gov/study/NCT01239394) | Phase 2 | Completed | 43 | Ofatumumab as initial systemic treatment for indolent B-cell lymphoma |
| [NCT00742144](https://clinicaltrials.gov/study/NCT00742144) | Phase 1 | Completed | 6 | Japanese PK/safety/tolerability study of ofatumumab in FL and CLL |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31174236](https://pubmed.ncbi.nlm.nih.gov/31174236/) | 2019 | RCT | Cancer | CALGB 50904 randomized trial: ofatumumab+bendamustine vs. +bortezomib in untreated high-risk FL |
| [22389254](https://pubmed.ncbi.nlm.nih.gov/22389254/) | 2012 | Cohort (multicenter) | Blood | Ofatumumab monotherapy in rituximab-refractory FL (n=116); ORR 13% |
| [22409295](https://pubmed.ncbi.nlm.nih.gov/22409295/) | 2012 | Cohort (Phase 2) | British Journal of Haematology | Ofatumumab + CHOP chemoimmunotherapy in previously untreated FL |
| [30723894](https://pubmed.ncbi.nlm.nih.gov/30723894/) | 2019 | Cohort (Phase 2 multicentre) | British Journal of Haematology | CALGB 50901: single-agent ofatumumab in untreated FL |
| [38937025](https://pubmed.ncbi.nlm.nih.gov/38937025/) | 2024 | Cohort | The Lancet Haematology | FIL MIRO final results: MRD-driven radiotherapy ± ofatumumab in early-stage FL |
| [24443277](https://pubmed.ncbi.nlm.nih.gov/24443277/) | 2014 | PK study | Journal of Clinical Pharmacology | Population pharmacokinetics of ofatumumab across CLL, FL, and RA |
| [29934061](https://pubmed.ncbi.nlm.nih.gov/29934061/) | 2018 | Review | Clinical Lymphoma, Myeloma & Leukemia | Evidence-based review of anti-CD20 regimens in R/R CLL, DLBCL, and FL |
| [18390837](https://pubmed.ncbi.nlm.nih.gov/18390837/) | 2008 | Phase 1/2 trial | Blood | First clinical use of ofatumumab in R/R follicular lymphoma |
| [28983798](https://pubmed.ncbi.nlm.nih.gov/28983798/) | 2017 | Review | Advances in Therapy | 20-year review of rituximab (anti-CD20 class context) in B-cell malignancies |
| [21083037](https://pubmed.ncbi.nlm.nih.gov/21083037/) | 2010 | Review | Expert Review of Hematology | Emerging therapeutic strategies in follicular lymphoma |

## Singapore Market Information

Ofatumumab currently holds **no product registration in Singapore** (0 licenses, market status: 未上市). No dosage form, authorization number, or approved local indication text is available.

## Cytotoxicity

Ofatumumab's original indication (chronic lymphocytic leukemia) is an antineoplastic use, so this section applies.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy / Immunotherapy (anti-CD20 monoclonal antibody; not a conventional cytotoxic agent) |
| Myelosuppression Risk | Medium — neutropenia and cytopenias are reported, particularly when combined with chemotherapy backbones (bendamustine, CHOP, FC); monotherapy generally better tolerated |
| Emetogenicity Classification | Low — monoclonal antibodies carry minimal emetogenic risk; the main acute concern is infusion-related reactions rather than nausea/vomiting |
| Monitoring Items | CBC with differential, infusion-related reaction monitoring during and after each infusion, hepatitis B reactivation screening (standard precaution for anti-CD20 agents), renal function |
| Handling Protection | As a biologic monoclonal antibody, standard cytotoxic drug handling precautions (per hazardous drug regulations) generally do not apply; institutional infusion-reaction management protocols should still be followed |

Please refer to the package insert for institution-specific handling and monitoring requirements once available (local labeling is a data gap — see Conclusion).

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were returned by the current queries (TFDA/HSA label not yet retrieved; DDI query: not found).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Follicular lymphoma is supported by multiple completed Phase 2 trials — including a randomized head-to-head design (NCT01286272, n=135) and a large single-arm registration-supporting study in rituximab-refractory disease (NCT00394836, n=116) — plus a completed RCT in the literature (PMID 31174236). No FL-specific confirmatory Phase 3 trial has completed successfully (NCT01077518 was terminated), so evidence sits at L2 rather than L1; the parallel, more mature CLL/SLL evidence (L1, multiple completed Phase 3 trials) supports the same CD20-targeting mechanism as class-level precedent.

**To proceed, the following is needed:**
- TFDA/HSA product label (warnings, contraindications) — currently a Blocking data gap (DG001)
- DrugBank-sourced mechanism of action detail — currently a High-severity data gap (DG002)
- Formal local registration pathway assessment, since ofatumumab has zero market presence in Singapore
- A confirmatory Phase 3 trial (or real-world evidence) specifically in follicular lymphoma
- A safety monitoring plan, particularly for infusion reactions, cytopenias, and hepatitis B reactivation screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

