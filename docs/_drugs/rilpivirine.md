---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 859
evidence_level: L5
indication_count: 10
---

# Rilpivirine
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

# Rilpivirine: From HIV-1 Infection to Simian Immunodeficiency Virus (SIV) Infection

## One-Sentence Summary

Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used in antiretroviral therapy for HIV-1 infection. The TxGNN model's top-ranked prediction points to **Simian Immunodeficiency Virus (SIV) Infection**, but this is a non-human primate preclinical model rather than a treatable human disease, currently supported only by **4 publications** and **no clinical trials**. Several lower-ranked candidates in this evidence pack (e.g. AIDS-related complex, congenital HIV) carry far stronger, Phase 3-level human evidence — see the summary table below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from drug class/NNRTI mechanism referenced throughout the evidence pack; no formal HSA-approved indication text is on file because the drug is not registered in Singapore) |
| Predicted New Indication | Simian immunodeficiency virus infection (SIV) — non-human primate model |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed structured mechanism-of-action data from DrugBank is not available for Rilpivirine in this evidence pack. Based on the information available, Rilpivirine is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that blocks the reverse transcriptase enzyme of HIV-1, and it is used both as oral therapy and as a long-acting injectable (with cabotegravir) for HIV-1 treatment and prevention.

SIV (simian immunodeficiency virus) is a lentivirus closely related to HIV-1 and shares a highly homologous reverse transcriptase target, which is why Rilpivirine's mechanism translates directly to SIV-infected macaque models. This mechanistic overlap explains the very high TxGNN score.

However, SIV infection is not a human disease — it is a macaque research model used to study long-acting antiretroviral regimens for HIV remission, pre-exposure prophylaxis (PrEP), and post-exposure prophylaxis (PEP) before those regimens are tested in humans. Consequently, while the mechanistic rationale is sound, this "predicted indication" does not represent a new human clinical use case; it reflects the drug's established antiretroviral mechanism being applied in animal translational research.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Macaque model study | Nature Communications | Long-acting cabotegravir/rilpivirine plus immune agent tested for SHIV remission in early-treated macaques |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | Review | Current Opinion in HIV and AIDS | Reviews cabotegravir (partner drug to rilpivirine in long-acting regimens) for ART and PrEP |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | Macaque model study | Antimicrobial Agents and Chemotherapy | Long-acting rilpivirine PrEP selects only low-frequency resistance in SIV/HIV-RT chimeric virus-infected macaques |
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | Preclinical (macaque model) | EBioMedicine | Single-injection long-acting cabotegravir/rilpivirine evaluated as HIV post-exposure prophylaxis in macaques |

---

## Singapore Market Information

Rilpivirine is currently **not registered or marketed in Singapore** (0 licenses on file). No product-level authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other Predicted Indications (Full Ranked List)

This evidence pack contains 10 TxGNN-predicted indications for Rilpivirine. For completeness, and because several carry materially stronger evidence than the top-ranked candidate above, they are summarized here:

| Rank | Disease | Score | Evidence Level | Decision | Note |
|------|---------|-------|-----------------|----------|------|
| 2 | Feline acquired immunodeficiency syndrome | 99.97% | L5 | Hold | Veterinary indication; only in-vitro enzyme comparison, no in-vivo/clinical data |
| 3 | Neurodevelopmental disorder (ataxic gait, absent speech, decreased white matter) | 99.97% | L5 | Hold | No mechanistic plausibility or evidence; likely embedding-space false positive |
| **4** | **AIDS related complex** | 99.56% | **L1** | **Proceed with Guardrails** | Extension within HIV disease spectrum, not true repurposing; supported by a Phase 3 RCT (NCT01792570) on darunavir/ritonavir + rilpivirine dual therapy |
| **5** | **Congenital human immunodeficiency virus** | 99.56% | **L1** | **Proceed with Guardrails** | Strongest evidence set: multiple completed/ongoing Phase 3 trials (e.g. NCT02422797, NCT02938520, NCT03299049) plus pregnancy/perinatal safety literature for long-acting CAB/RPV |
| 6 | Obsolete familial combined hyperlipidemia | 98.57% | L5 | Hold | Disease category itself is obsolete; no mechanism or evidence |
| 7 | Chronic hepatitis C virus infection | 95.16% | L3 | Research Question | Evidence is indirect — mainly HIV/HCV coinfection DDI and liver-safety studies; one cohort (PMID 36737372) suggests rilpivirine may improve liver stiffness, but no HCV-specific efficacy trial exists |
| 8 | Fibroma of prostate | 93.87% | L5 | Hold | No mechanism or evidence; false-positive signal |
| 9 | Benign reproductive system neoplasm | 93.23% | L5 | Hold | No mechanism or evidence; false-positive signal |
| 10 | Brenner tumor | 93.21% | L5 | Hold | No mechanism or evidence; false-positive signal |

**Interpretation:** Ranks 4 and 5 are the only candidates with genuine, extensive human clinical evidence (multiple Phase 3 RCTs), but both represent extensions within Rilpivirine's existing HIV indication rather than novel repurposing. Rank 7 (chronic HCV) is the only candidate that could represent a genuine adjacent indication worth hypothesis-generating research, via a possible antifibrotic effect in HIV/HCV-coinfected liver disease. Ranks 2, 3, 6, 8, 9, and 10 lack any supporting mechanism or evidence and should not be pursued.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked candidate, SIV infection)

**Rationale:**
SIV infection is a non-human primate research model, not a human clinical indication; despite the high TxGNN score and sound mechanistic rationale (shared reverse transcriptase target), there is no clinical trial evidence and the evidence level is only L4. This candidate cannot proceed as a human drug-repurposing opportunity.

**To proceed, the following is needed:**
- DrugBank-sourced structured MOA data for Rilpivirine (currently a data gap)
- TFDA/HSA package insert warnings and contraindications (currently a data gap)
- If pursuing genuine repurposing rather than label extension, prioritize evaluation of **chronic HCV infection** (rank 7, L3) as a hypothesis-generating research question, since it is the only candidate with a plausible novel mechanism (antifibrotic effect) and independent literature support
- Ranks 4–5 (AIDS-related complex, congenital HIV) should be treated as label-extension/pediatric-perinatal indication questions, not new repurposing candidates, and referred to the appropriate regulatory pathway rather than this repurposing pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

