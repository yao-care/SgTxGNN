---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Darunavir
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

# Darunavir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Darunavir is an HIV-1 protease inhibitor (brand names: Prezista, Symtuza) widely used in combination antiretroviral therapy (cART) for HIV infection in treatment-naïve and treatment-experienced adults and children.
The TxGNN model predicts it may be effective for **Simian Immunodeficiency Virus (SIV) Infection** with a score of **99.97%**, supported by **0 clinical trials** and **4 publications** — all non-human primate animal studies — reflecting biological model proximity rather than a traditional clinical repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (treatment-naïve and treatment-experienced; not registered in Singapore) |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 (Preclinical / Animal Studies Only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack. Based on known information, Darunavir is an HIV-1 protease inhibitor — it competitively binds to the active site of the HIV-1 protease enzyme and prevents cleavage of the Gag-Pol polyprotein precursor into functional structural and enzymatic viral proteins, thereby blocking the maturation of infectious virions. Its efficacy and safety in treating HIV-1 infection have been extensively validated across large Phase 3 clinical trials globally.

The scientific rationale for the SIV prediction is well-grounded: SIV and HIV-1 share high structural and catalytic homology in their protease enzymes, and non-human primate (NHP) SIV infection models are the established gold-standard preclinical platform for studying HIV reservoir dynamics, viral eradication strategies, and novel antiretroviral combinations. In this context, Darunavir appears regularly as a component of intensified cART regimens used to suppress viremia in SIV-infected macaques — the same mechanistic logic as its HIV use.

However, this prediction represents **biological model extrapolation, not a genuine clinical repurposing opportunity.** SIV does not infect humans; therefore, no human clinical development path exists for this "indication." The high TxGNN score most likely reflects the SIV–HIV protease node proximity in the knowledge graph, and the existing literature confirms Darunavir's role within multi-drug NHP model cART regimens rather than as a new standalone clinical application. Separately, this Evidence Pack contains two predictions with substantially stronger clinical evidence — AIDS Related Complex (L2, Rank 5) and Congenital HIV Infection (L1, Rank 6) — which represent more actionable repurposing signals.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Darunavir in SIV infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study (NHP/SIV) | AIDS Research and Human Retroviruses | Two novel injectable cART regimens (including PI-class agents) evaluated in SIVmac239-infected rhesus macaques; demonstrated clinically relevant viral suppression necessary for HIV reservoir eradication studies |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Animal Study (NHP/SIV) | PLoS One | Intensive cART plus HDAC inhibitor SAHA in SIV-infected Chinese-origin rhesus macaques; assessed impact on viral reservoirs and latency reversal — mechanistic model for HIV cure strategies |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | Animal Study (NHP/SIV) | PLoS Pathogens | Highly intensified cART (multi-drug, including PI class) suppressed viremia across a wide viremic range (10³–10⁷ RNA copies/mL) in SIVmac251-infected macaques and significantly reduced the viral reservoir |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | Animal Study (NHP/SIV) | AIDS | Gold compound auranofin combined with cART (including PI) reduced CD4⁺ T cell reservoir and induced containment of viral load after ART suspension in the SIV macaque model |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All supporting evidence is derived from non-human primate SIV animal models (Evidence Level L4), and SIV is not a human pathogen — no clinical development pathway exists for this indication. The TxGNN prediction reflects valid biological reasoning about HIV–SIV protease homology, but this is a research tool application rather than a clinical repurposing candidate. Notably, two other predictions in this Evidence Pack with stronger clinical signals — **AIDS Related Complex (Rank 5, L2)** and **Congenital HIV Infection (Rank 6, L1)** — may deserve prioritized evaluation instead.

**To proceed with any further evaluation, the following is needed:**

- **Clarify research intent**: Distinguish between (a) use in NHP preclinical HIV reservoir/eradication models (scientifically valid, no regulatory pathway needed) vs. (b) clinical repurposing for a human indication (redirect to Rank 5 or Rank 6)
- **Obtain MOA data** from DrugBank (Data Gap DG002) to complete mechanistic analysis
- **Retrieve TFDA/prescribing information** (package insert PDF) for complete safety and contraindication profile (Data Gap DG001 — currently Blocking for S1 safety assessment)
- **Assess higher-priority indications**: Escalate AIDS Related Complex and Congenital HIV to full S1–S3 evaluation workflow given their L2/L1 evidence levels and direct mechanistic alignment with Darunavir's established antiviral mechanism
- **Singapore registration pathway**: As Darunavir is not currently registered in Singapore (0 HSA licenses), any clinical development would require a full new drug application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

