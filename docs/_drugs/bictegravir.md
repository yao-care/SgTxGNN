---
layout: default
title: Bictegravir
parent: Low Evidence (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Bictegravir
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

# Bictegravir: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Bictegravir is an HIV-1 integrase inhibitor, marketed in Singapore as part of the Biktarvy combination tablet for HIV-1 treatment.
The TxGNN model predicts it may be effective against **simian immunodeficiency virus (SIV) infection**, a non-human primate model of HIV, and the support is preclinical only: **0 clinical trials** and **3 publications** (in vitro, structural review, and animal model).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (inferred from known pharmacology; the Singapore registration record lists no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank. Based on known pharmacology, bictegravir is an integrase strand-transfer inhibitor (INSTI). It blocks the step in which viral DNA is inserted into the host genome. Its efficacy in HIV-1 infection is established, and it is used with emtricitabine and tenofovir alafenamide in Biktarvy.

SIV and HIV-1 are closely related lentiviruses, and their integrase enzymes are structurally similar. This is why an INSTI would be expected to act on SIV as well. The literature supports this: bictegravir was tested in vitro against integrase-inhibitor-resistant SIVmac239, and structural work shows that HIV and SIV integrase share inhibitor-binding features.

SIV infection is a research model in non-human primates, not a human disease. This prediction is therefore best read as support for using SIV models to test antiviral strategies, not as a new treatment for patients. No human clinical benefit can follow from it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In vitro antiviral study | Antimicrob Agents Chemother | Tested bictegravir and cabotegravir against integrase-inhibitor-resistant SIVmac239 and HIV-1. Bictegravir has a higher genetic barrier to resistance than raltegravir and elvitegravir. |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Review (structural) | FEBS J | HIV/SIV intasome structures explain how INSTIs, including second-generation bictegravir and dolutegravir, bind integrase and how resistance arises. |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | Preclinical animal model | Front Immunol | A humanized mouse model for testing antiviral regimens against both SIV and HIV, intended for evaluating new drug combinations in cure studies. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15604P | BIKTARVY FILM-COATED TABLETS 50MG/200MG/25MG | Tablet, film coated (oral) | Not listed in the registration record |

Manufacturers: Rottendorf Pharma GmbH; Gilead Sciences Ireland UC.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is limited to in vitro, structural, and animal-model work. SIV is a non-human research model with no human patient population, so there is no clinical repurposing opportunity here. The other high-scoring predictions for bictegravir either duplicate its existing HIV-1 use or lack a plausible mechanistic link (for example, hepatitis A, C and E, which have no integrase target).

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- A decision on whether SIV or humanized-mouse models are a valid research use case, given that no human indication is involved
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

