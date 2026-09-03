---
layout: default
title: Zoledronic Acid
parent: 僅模型預測 (L5)
nav_order: 1078
evidence_level: L5
indication_count: 10
---

# Zoledronic Acid
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

# Zoledronic Acid: From Osteoporosis/Paget's Disease to HIV Infectious Disease

## One-Sentence Summary

Zoledronic acid is a nitrogen-containing bisphosphonate whose established use — per the evidence in this pack — is treatment of postmenopausal osteoporosis and Paget's disease of bone.
The TxGNN model predicts it may be effective for **HIV infectious disease**, though the underlying evidence actually points to a more specific benefit: managing **HIV/ART-associated osteoporosis and osteopenia**, with a secondary immune-modulatory signal.
This is currently supported by **4 clinical trials** and **20 publications**, including several completed randomized controlled trials.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore; per clinical trial documentation in this evidence pack, ZA's efficacy is established in postmenopausal osteoporosis (high fracture risk) and Paget's disease of bone |
| Predicted New Indication | HIV infectious disease (evidence indicates this functionally means HIV/ART-associated osteoporosis-osteopenia) |
| TxGNN Prediction Score | 93.95% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed original-MOA registry data is not available for this drug (flagged as a High-severity data gap). However, based on the pharmacological class and the mechanistic detail documented across the clinical trials and literature in this evidence pack, zoledronic acid is a nitrogen-containing bisphosphonate that inhibits farnesyl pyrophosphate synthase (FPPS) in the mevalonate pathway. This blocks osteoclast-mediated bone resorption — the same mechanism that underlies its proven efficacy in osteoporosis and Paget's disease. As a downstream effect, FPPS inhibition causes intracellular accumulation of isopentenyl pyrophosphate (IPP), which activates Vγ9Vδ2 γδ T lymphocytes — an immune-modulatory side effect of the same core mechanism.

People living with HIV — particularly those on tenofovir-containing antiretroviral therapy (ART) — experience accelerated bone loss and a high prevalence of osteopenia/osteoporosis. Because ZA's core anti-resorptive action directly treats this bone pathology, the pharmacological link to "HIV disease" in the TxGNN prediction is real, but is best understood as **treating an HIV/ART-associated comorbidity**, not the viral infection itself. A second, weaker signal in the evidence involves ZA's γδ T-cell-activating property being explored as an adjunct immunotherapy to improve immune reconstitution in HIV — this is mechanistically plausible but much less mature.

In short: the disease label "HIV infectious disease" as scored by TxGNN is imprecise. The actual, evidence-backed repurposing opportunity is **zoledronic acid for HIV/ART-associated osteoporosis and osteopenia**, with an exploratory secondary application in γδ T-cell-based immune modulation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00795483](https://clinicaltrials.gov/study/NCT00795483) | Phase 4 | Completed | 33 | Evaluated efficacy/safety of annual and biennial ZA for osteoporosis treatment in an HIV-infected patient cohort |
| [NCT01228318](https://clinicaltrials.gov/study/NCT01228318) | Phase 2 | Completed | 63 | Assessed bone loss and immune reconstitution in HIV/AIDS via RANKL/OPG pathway |
| [NCT00102908](https://clinicaltrials.gov/study/NCT00102908) | Phase 2 | Unknown | 30 | Tested whether zoledronate improves bone mineral density (BMD) in HIV-infected adults with osteopenia |
| [NCT05493267](https://clinicaltrials.gov/study/NCT05493267) | Phase 4 | Recruiting | 30 | Explores ZA + IL-2 to expand Vγ2Vδ2 T cells as adjunct immunotherapy for MDR-TB (not HIV itself; shares ZA's γδ T-cell mechanism) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29927785](https://pubmed.ncbi.nlm.nih.gov/29927785/) | 2018 | RCT | AIDS | ZA superior to tenofovir-switching for low BMD in HIV-positive adults |
| [27193748](https://pubmed.ncbi.nlm.nih.gov/27193748/) | 2016 | RCT (Phase IIb) | Clin Infect Dis | Single-dose ZA infusion prevents ART-induced bone loss in treatment-naïve HIV patients |
| [31621838](https://pubmed.ncbi.nlm.nih.gov/31621838/) | 2020 | RCT (Phase IIB, extension) | Clin Infect Dis | Protection against ART-induced bone loss from a single ZA dose persists beyond initial follow-up |
| [19050386](https://pubmed.ncbi.nlm.nih.gov/19050386/) | 2009 | RCT (double-blind) | AIDS | Single IV zoledronate dose effective for HIV-associated osteopenia/osteoporosis |
| [17227801](https://pubmed.ncbi.nlm.nih.gov/17227801/) | 2007 | RCT | J Clin Endocrinol Metab | Annual zoledronate increases BMD in HAART-treated HIV-infected men |
| [31361922](https://pubmed.ncbi.nlm.nih.gov/31361922/) | 2019 | Cohort (RCT follow-up) | J Bone Miner Res | Prolonged BMD/turnover effects of ZA persist over 36 months in HIV adults on tenofovir |
| [30870576](https://pubmed.ncbi.nlm.nih.gov/30870576/) | 2019 | RCT extension (long-term) | J Bone Miner Res | Effects of IV zoledronate on bone turnover/density persist ≥11 years in HIV-infected men |
| [25300622](https://pubmed.ncbi.nlm.nih.gov/25300622/) | 2014 | Systematic Review/Meta-analysis | AIDS Reviews | Pooled analysis of 8 RCTs on bisphosphonates for BMD in HIV-infected patients |
| [19238075](https://pubmed.ncbi.nlm.nih.gov/19238075/) | 2009 | Clinical Trial (mechanistic) | AIDS | ZA + IL-2 improves immunocompetence in HIV via activation of Vγ9Vδ2 γδ T cells |
| [33637048](https://pubmed.ncbi.nlm.nih.gov/33637048/) | 2021 | Mechanistic study | Mol Med | ZA alleviates osteoporosis in HIV patients by suppressing osteoclastogenesis via RANKL regulation |

---

## Singapore Market Information

Zoledronic acid currently has no registered authorizations in Singapore under this evidence pack (0 licenses, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: This evidence pack flags TFDA-equivalent label warnings/contraindications as a Blocking data gap (DG001) — this must be resolved before any formal safety (S1) assessment. Separately, the literature in this pack repeatedly documents class-related bisphosphonate risks in real-world use (e.g., hypocalcemia, osteonecrosis of the jaw, renal impairment/Fanconi syndrome) — these should be incorporated once formal label data is obtained.*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed RCTs (including Phase IIb trials) consistently show zoledronic acid effectively prevents and treats bone loss in HIV-infected/ART-treated patients, supported by a systematic review of 8 RCTs — this meets an L2 evidence bar. However, the predicted indication label ("HIV infectious disease") is misleading relative to the actual evidence (HIV/ART-associated osteoporosis-osteopenia), and two data gaps (missing label warnings/contraindications, missing confirmed MOA) currently block a full safety evaluation.

**To proceed, the following is needed:**
- Resolve DG001: obtain official package insert / label warnings and contraindications for zoledronic acid
- Resolve DG002: confirm mechanism of action via DrugBank API for formal mechanistic sign-off
- Re-scope and rename the target indication to "HIV/ART-associated osteoporosis and osteopenia" for regulatory and clinical clarity
- Establish a safety monitoring plan addressing known class risks (hypocalcemia, renal function, osteonecrosis of the jaw), especially given vitamin D/calcium status in HIV patients
- Clarify whether the exploratory γδ T-cell immunotherapy application (ZA + IL-2) should be tracked as a separate, earlier-stage candidate given its much weaker evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

