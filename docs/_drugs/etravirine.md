---
layout: default
title: Etravirine
parent: Low Evidence (L5)
nav_order: 407
evidence_level: L5
indication_count: 10
---

# Etravirine
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

# Etravirine: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Etravirine is an oral non-nucleoside reverse transcriptase inhibitor (NNRTI) used to treat HIV-1 infection.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus (SIV) infection**, with a very high score.
Evidence is thin: **0 clinical trials** and **1 publication** (an in vitro HIV study), and SIV is generally reported to be poorly susceptible to NNRTIs, so the prediction is not supported by mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (the Singapore licence record contains no indication text) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 (preclinical/in vitro only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Etravirine is an HIV-1 NNRTI that binds reverse transcriptase. It is active against many strains resistant to first-generation NNRTIs. Detailed mechanism-of-action data was not available in the source record, so this description comes from the candidate's mechanistic assessment.

The graph link to SIV is probably driven by shared lentiviral biology, since HIV and SIV are related retroviruses. However, SIV (especially SIVmac) is generally reported to have reduced susceptibility to NNRTIs. The high graph score is therefore not backed by mechanism, and it should be treated as a likely graph-inference artifact. SIV infection is also an animal-model disease with no direct human clinical use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | In vitro study | Molecular Pharmaceutics | Nanoparticle-based antiretroviral drug combinations showed synergistic inhibition of cell-free and cell-cell **HIV** transmission. It did not study SIV directly. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN14535P | INTELENCE TABLET 200 MG | Tablet | Janssen Pharmaceutica NV (Spray Dried Powder) / Janssen Cilag S.p.A |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there are no clinical trials and only one in vitro HIV paper. SIV is reported to be poorly susceptible to NNRTIs, and the disease has no direct human relevance. The prediction is best treated as a model artifact.

**To proceed, the following is needed:**
- Direct evidence on etravirine susceptibility of SIV isolates (in vitro or animal model)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the Singapore Health Sciences Authority (HSA), which are currently missing

**Other predictions for this drug:**
- **Overlap with the HIV label:** "AIDS related complex" and "congenital human immunodeficiency virus" rank higher in evidence (L3), but they overlap with the approved HIV-1 use and are not true repurposing.
- **Separate signal:** a completed Phase 2 etravirine trial in Friedreich ataxia (NCT04273165, n=30) was found under another indication, and it may merit its own review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

