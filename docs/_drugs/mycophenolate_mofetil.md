---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 684
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Transplant Rejection Prophylaxis to HIV Infection

## One-Sentence Summary

Mycophenolate mofetil (MMF) is internationally used as an immunosuppressant for the prophylaxis of organ transplant rejection. The TxGNN model predicts it may have adjunctive antiretroviral value in **HIV infectious disease**, with **10 clinical trials** and **20 publications** currently identified, though most of the direct evidence is small, older, or of uncertain/terminated status.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Singapore regulatory data (drug is not registered/marketed in Singapore); internationally, MMF is indicated for prophylaxis of organ transplant rejection (renal, cardiac, hepatic) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (drug-level data gap, source: DrugBank, not yet retrieved). Based on the mechanistic rationale associated with this prediction, MMF's active metabolite mycophenolic acid (MPA) inhibits IMPDH (inosine monophosphate dehydrogenase), depleting intracellular guanine nucleotide pools. This has two theoretically relevant downstream effects: (1) it reduces T-cell activation and proliferation, which could lower the chronic immune-activation burden that drives HIV disease progression; and (2) it can potentiate the intracellular phosphorylation/activity of certain nucleoside reverse transcriptase inhibitors (e.g., abacavir, and the investigational agent DAPD/amdoxovir), giving a potential pharmacodynamic synergy with antiretroviral therapy.

This is a mechanistically well-defined hypothesis that has already been tested in several proof-of-concept clinical studies (see below) rather than a purely computational association — several groups investigated MMF as an adjunct to HAART/ART from the late 1990s through the mid-2000s. However, the clinical signal is old, small-scale, and mixed (including a withdrawn trial with zero enrollment and two "unknown status" Phase 4 studies), so it should be regarded as a research hypothesis rather than an established therapeutic use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | Completed | 56 | Double-blind, placebo-controlled pilot of DAPD (amdoxovir) vs. DAPD + MMF in treatment-experienced HIV patients; directly tests MMF's antiviral-potentiating mechanism |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | Withdrawn | 0 | Planned safety/tolerability/antiretroviral-activity study of MMF added to abacavir in heavily treatment-experienced patients; withdrawn before enrollment, no data generated |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 substudy assessing effect of MMF 500 mg BID on cardiovascular surrogate markers in ART-naive HIV-1 patients |
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 study: evaluates whether MMF reduces chronic immune hyperactivation and CD4+ T-cell decline, and its effect on plasma HIV-1 RNA, in untreated chronic HIV-1 infection |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | Renal transplantation in HIV-1 patients under raltegravir-based ART; evaluates acute graft rejection, with MMF used as standard post-transplant immunosuppression rather than as an HIV-directed therapy |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Safety/efficacy of renal transplantation in HIV-infected patients with ESRD; MMF is part of the standard immunosuppressive regimen, not the primary study intervention against HIV |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic HSCT to induce mixed hematopoietic chimerism in HIV-1-infected patients; MMF used as post-transplant immunosuppression |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Cyclosporine + MMF vs. cyclophosphamide + prednisolone for anti-EPO-associated pure red cell aplasia; unrelated disease, not HIV-specific |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | Completed | 80 | HLA-mismatched unrelated donor bone marrow transplant with post-transplant cyclophosphamide, sirolimus and MMF for GVHD prophylaxis in hematologic malignancies; not related to HIV treatment |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | Recruiting | 56 | Thiotepa/busulfan/fludarabine conditioning for haploidentical HSCT in high-risk AML; unrelated to HIV or MMF's antiviral mechanism |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | RCT | J Acquir Immune Defic Syndr | Adding MMF 500 mg BID to abacavir-containing ART depleted intracellular dGTP and was associated with decreased plasma HIV-1 RNA in patients failing maximal therapy (n=5) |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Reviews immunosuppressive drugs, including MMF, as adjuncts targeting chronic immune activation in HIV disease progression |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | Cohort | J Clin Invest | Explores antiproliferative drugs (including MPA-related mechanisms) for selectively targeting clonally expanded HIV-infected CD4+ T cells as a cure strategy |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | Cohort | Clin Pharmacokinet | PK/PD of low-dose MMF in HIV-infected patients on abacavir, efavirenz, and nelfinavir; supports monitoring feasibility |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Cohort | AIDS Res Hum Retroviruses | MMF combined with HAART showed no detrimental immunological effects in treatment-naive acute/chronic HIV-1 patients |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | Cohort | Clin Pharmacokinet | MMF's effect on pharmacokinetics of antiretrovirals and intracellular nucleoside triphosphate pools |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Cohort | J Acquir Immune Defic Syndr | Randomized pilot study: MMF's effect on immune response and viral load during/after HAART interruption (n=17) |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Cohort | J Acquir Immune Defic Syndr | Pilot study of MMF as a component of therapy for multidrug-resistant HIV-1 infection (n=7), well tolerated, no consistent virologic benefit shown |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Study | AIDS | Studied effect of MMF on plasma HIV-1 RNA decay rate and latent reservoir in treatment-naive patients starting ART |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Study | AIDS | Safety, tolerability and antiretroviral activity of DAPD with or without MMF in drug-resistant HIV infection |

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack (DDI query status: not found).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV repurposing hypothesis for MMF has a clear pharmacological mechanism and is supported by an RCT plus several small cohort/pilot studies (Evidence Level L2), but the direct evidence base is largely 15–25 years old, small-scale, and includes a withdrawn trial (n=0) and two Phase 4 studies of unknown status. Combined with a **Blocking** data gap on TFDA/HSA label warnings and contraindications (DG001) — which prevents completion of the S1 safety screening stage — and the fact that MMF currently has zero registrations/market presence in Singapore, the candidate is not ready to advance.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the regulatory authority (resolves DG001, currently blocking)
- Detailed mechanism of action documentation from DrugBank (resolves DG002)
- A completed drug-drug interaction (DDI) query (currently not_found)
- Confirmation of a registration/import pathway, since the drug is not currently marketed in Singapore
- An updated literature/trial search to assess whether more recent (post-2010) confirmatory studies exist, given that most direct MMF-HIV evidence predates modern ART regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

