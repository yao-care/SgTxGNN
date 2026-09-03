---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 954
evidence_level: L5
indication_count: 10
---

# Tenofovir Disoproxil
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

# Tenofovir Disoproxil: From HIV/Hepatitis B Antiviral Therapy to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Tenofovir disoproxil is a nucleotide reverse transcriptase inhibitor (NRTI) whose established antiviral role against HIV and chronic hepatitis B is referenced throughout the supporting literature, though this evidence pack does not contain structured original-indication or mechanism-of-action data, and the drug is currently **not marketed in Singapore**. The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) Infection**, an animal-model disease rather than a human condition, supported by only 2 low-relevance clinical trials and 20 preclinical/animal publications — evidence that confirms known antiretroviral pharmacology in macaque models rather than pointing to a genuinely new human indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no `taiwan_regulatory.licenses` on file); supporting literature references tenofovir disoproxil's established use in HIV infection/PrEP and chronic hepatitis B |
| Predicted New Indication | Simian Immunodeficiency Virus (SIV) Infection |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 (preclinical/animal studies only; no completed RCT directly targets SIV) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap). Based on the supporting literature, tenofovir disoproxil is an NRTI-class antiviral whose activity against retroviruses (HIV) and hepadnaviruses (HBV) is well documented; mechanistically, this same reverse-transcriptase inhibition extends to simian immunodeficiency virus (SIV) and simian/human immunodeficiency virus (SHIV) chimeras, which are the standard non-human primate models used to study HIV pre-exposure prophylaxis (PrEP) and treatment.

However, the repurposing rationale supplied with this candidate is explicit that SIV/SHIV models are used to **re-confirm** tenofovir's known HIV PrEP mechanism in an animal system, not to identify a novel, directly translatable human indication. SIV itself is a veterinary/research disease entity that does not occur in humans, so this prediction functions as mechanistic validation rather than a clinical repurposing opportunity.

It is also worth noting that among this drug's other predicted indications, the strongest human-relevant evidence (L1, ≥2 completed Phase 3-class trials) attaches to **hepatitis B virus infection** (rank 6) and **AIDS-related complex** (rank 10) — both of which the underlying rationale identifies as re-confirmations of tenofovir disoproxil's already-approved indications, not new signals. The remaining candidates (ranks 3, 4, 5, 7, 8, 9) have no clinical trial or literature support at all (L5) and are already flagged "Hold" by the source pipeline.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | Unknown | 12 | Vedolizumab + ART in human HIV-infected subjects aiming at virological remission; no direct SIV/animal-model link (relevance grade C) |
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | HIV decay kinetics with raltegravir in humans; references SIV-macaque decay kinetics only as historical comparator, trial itself withdrawn (relevance grade C) |

Neither trial directly tests tenofovir disoproxil in an SIV/SHIV model; both are graded low relevance (C).

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36477356](https://pubmed.ncbi.nlm.nih.gov/36477356/) | 2022 | Preclinical/Animal | JCI Insight | Hypo-osmolar rectal tenofovir douche prevents SHIV acquisition in macaques |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | Preclinical/Animal | J Infect Dis | Oral TAF + emtricitabine protects macaques from rectal SHIV infection (PrEP model) |
| [22072766](https://pubmed.ncbi.nlm.nih.gov/22072766/) | 2012 | Preclinical/Animal | J Virol | 1% tenofovir vaginal gel provides durable protection against vaginal SHIV in macaques |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | Preclinical/Animal | J Infect Dis | FTC/TDF prevents vaginal SHIV infection in macaques co-infected with C. trachomatis/T. vaginalis |
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | Review | Pharmacotherapy | Review of systemic PrEP for HIV, citing SIV/SHIV macaque efficacy data |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | Preclinical/Animal | J Acquir Immune Defic Syndr | Oral TDF and topical GS-7340 protect infant macaques against repeated oral SIV challenge |
| [16960777](https://pubmed.ncbi.nlm.nih.gov/16960777/) | 2006 | Preclinical/Animal | J Infect Dis | TDF chemoprophylaxis gives partial protection against SHIV in macaques with multiple challenges |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | Preclinical/Animal | Nat Commun | SHIV remission in macaques with early ART initiation plus long-acting antivirals |
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | Preclinical/Animal | J Infect Dis | TAF/elvitegravir vaginal inserts give extended postexposure protection against SHIV in macaques |
| [23633402](https://pubmed.ncbi.nlm.nih.gov/23633402/) | 2013 | Preclinical/Animal | J Infect Dis | FTC/TDF prevents transmission of tenofovir-resistant (K65R) SHIV in macaques |

All 10 entries are preclinical/veterinary primate studies; none constitute human clinical trial or RCT evidence for SIV infection itself.

## Singapore Market Information

No Singapore (HSA) registrations are on file for tenofovir disoproxil in this evidence pack — market status is "Not Marketed" with 0 total licenses.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (SIV infection) is an animal-model disease with no completed human clinical trial support and only preclinical/animal literature (L4), representing mechanistic re-confirmation rather than a novel, clinically actionable human indication. Combined with a Blocking data gap on Singapore/TFDA safety labeling and the drug's current non-marketed status in Singapore, there is no basis to advance this candidate.

**To proceed, the following is needed:**
- HSA/TFDA-equivalent package insert data (key warnings, contraindications) to close the Blocking data gap
- Confirmed mechanism-of-action documentation (currently a data gap)
- If pursuing repurposing further, evaluate the higher-evidence candidates in this same prediction set — hepatitis B virus infection and AIDS-related complex (both L1, "Proceed with Guardrails") — while recognizing these reflect tenofovir disoproxil's already-established indications rather than new repurposing opportunities
- No further action recommended on the remaining L5 candidates (neurodevelopmental disorder, familial combined hyperlipidemia, fibroma of prostate, Brenner tumor, benign reproductive system neoplasm, benign prostate phyllodes tumor), which lack any supporting trial or literature evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

