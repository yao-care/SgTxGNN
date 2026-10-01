---
layout: default
title: Efavirenz
parent: Medium Evidence (L3-L4)
nav_order: 362
evidence_level: L4
indication_count: 10
---

# Efavirenz
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) used in HIV-1 antiretroviral regimens. The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**. The supporting evidence is weak: **1 clinical trial** (withdrawn, 0 participants, and not about efavirenz) and **15 publications**, almost all animal or laboratory studies using an HIV-1/SIV hybrid virus. This looks like a model-organism mapping artifact rather than a real repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV-1 infection (based on drug class; the Singapore licence text was not supplied) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Efavirenz is known to be an HIV-1 NNRTI that binds an allosteric pocket of HIV-1 reverse transcriptase (RT).

The prediction is probably not biologically meaningful. Native SIV reverse transcriptase is naturally insensitive to NNRTIs, so efavirenz would not be expected to treat true SIV infection. The macaque studies in the literature use **RT-SHIV**, a chimeric virus that carries HIV-1 RT inside an SIV backbone. This design lets researchers test HIV-1 drugs in monkeys. The studies therefore model HIV-1 therapy in a primate. They do not show that efavirenz treats SIV.

The high score (~0.998) is not backed by any human trial. This is best read as a species and disease-term mapping artifact.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | Not applicable | Withdrawn | 0 | Planned study of HIV decay kinetics with raltegravir. It concerns raltegravir, not efavirenz, and HIV rather than SIV. No usable evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal study | Antimicrob Agents Chemother | Efavirenz antiviral activity evaluated in rhesus macaques infected with RT-SHIV. |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal study | J Virol | Efavirenz plus lamivudine and tenofovir lowered plasma viral RNA in RT-SHIV-infected macaques (HAART model). |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Preclinical animal study | J Virol | Viral genetic diversity persisted in macaques despite therapy, including short efavirenz monotherapy. |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal study | Retrovirology | Tracked wild-type and drug-resistant RT-SHIV variants in macaques after efavirenz monotherapy and combination therapy. |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal study | Antimicrob Agents Chemother | Enhanced four- and five-drug regimens improved RT-SHIV viral decay in rhesus macaques. |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Preclinical laboratory study | J Virol | Ultrasensitive PCR found rare pre-existing drug-resistant variants in RT-SHIV-infected macaques. |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro characterisation | J Virol | Characterised the SIV/HIV-1 RT chimera as a tool for studying NNRTI resistance in pigtail macaques. |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Preclinical imaging study | Antimicrob Agents Chemother | Imaging of antiretroviral distribution, viral RNA and fibrosis in the spleens of nonhuman primates. |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | Laboratory study | Antivir Ther | Compared susceptibility of HIV-2, SIV and SHIV strains to approved anti-HIV drugs. |
| [20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) | 2010 | Animal study | PLoS One | Viral decay kinetics in a HAART-treated rhesus macaque model of AIDS. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15719P | EFAVIRENZ SANDOZ FILM COATED TABLET 600MG (Sandoz Private Limited) | Tablet, film coated (oral) |

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications or drug interactions were retrieved for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction rests only on primate and laboratory models that use an HIV-1 RT chimera. There is no human trial, and native SIV is not sensitive to NNRTIs.
- Efavirenz is already established for HIV-1, so there is nothing new to repurpose here. The score reflects a species-mapping artifact.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indication) to confirm the on-label HIV-1 use
- Detailed mechanism of action data from DrugBank
- Rank 6 of this candidate list, congenital HIV, has Phase 3 data (for example NCT03048422) and could be reviewed separately with guardrails. It also appears to be an HIV-1 use rather than a novel indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

