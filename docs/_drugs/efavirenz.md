---
layout: default
title: Efavirenz
parent: Medium Evidence (L3-L4)
nav_order: 366
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Efavirenz: predicted new indication Simian immunodeficiency virus infection (evidence level L4). Approved use: HIV infectious disease"
monitor_inn: "Efavirenz"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor"]
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

# Efavirenz: From HIV Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is an antiretroviral drug originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **simian immunodeficiency virus infection**, but this is an animal-model disease and the support comes from **0 clinical trials** and **14 publications**, mostly preclinical macaque studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the Singapore licence text for the registered product is blank) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) that acts on HIV-1 reverse transcriptase, and its efficacy in HIV infection is established.

The macaque studies use RT-SHIV, a chimeric simian virus that carries HIV-1 reverse transcriptase. Efavirenz activity in these studies therefore reflects the HIV-1 RT component, not native SIV. This biological similarity to the approved HIV indication explains the high model score.

SIV infection is an animal-model disease, so this is not a human repurposing opportunity. The evidence supports efavirenz as a research tool in primate models of HIV therapy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The 14 publications are all preclinical or laboratory studies. The most relevant are listed below (the first two rows are the most directly relevant studies).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal study | Antimicrob Agents Chemother | Efavirenz therapy in rhesus macaques infected with RT-SHIV, a chimeric SIV carrying HIV-1 reverse transcriptase |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal study | J Virol | Efavirenz + lamivudine + tenofovir suppressed virus load in RT-SHIV-infected rhesus macaques |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal study | Antimicrob Agents Chemother | Enhanced four- and five-drug ART improved viral decay kinetics in RT-SHIV macaques |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal study | Retrovirology | Viral subpopulation dynamics in macaques given short-course efavirenz monotherapy followed by combination ART |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Animal study | J Virol | SIV genetic diversity persisted in macaques despite ART, including after efavirenz monotherapy |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Laboratory study | J Virol | Ultrasensitive PCR found rare preexisting drug-resistant variants in RT-SHIV macaques |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In vitro | J Virol | Characterization of an SIV-HIV chimera expressing HIV-1 RT for studying NNRTI resistance |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro | Antivir Ther | Susceptibility of HIV-2, SIV and SHIV to anti-HIV-1 compounds |
| [20032180](https://pubmed.ncbi.nlm.nih.gov/20032180/) | 2010 | Animal study | J Virol | Viral reservoirs and sanctuaries during HAART in a macaque model |
| [24505452](https://pubmed.ncbi.nlm.nih.gov/24505452/) | 2014 | Animal study | PLoS One | Residual viremia in an RT-SHIV macaque HAART model |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15719P | Efavirenz Sandoz Film Coated Tablet 600 mg (Sandoz Private Limited) | Tablet, film coated | Not stated in the registration record |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text)**: liver failure and liver disease, kidney disease, epilepsy, anxiety and other psychiatric disorders (neurotic, dysthymic, delusional disorders, paranoid schizophrenia), chronic hepatitis B and C virus infection, hypertriglyceridemia, fatty liver disease and non-alcoholic steatohepatitis, lactic acidosis, Fanconi renotubular syndrome, and bone and mineral disorders (osteomalacia, rickets, hypophosphatemia).
- **Drug Interactions**: 100 interactions were found. The only Major interaction in the displayed list is **dolasetron**. The others displayed are Moderate, including clarithromycin, bupropion, aprepitant, corticosteroids (dexamethasone, hydrocortisone, betamethasone, triamcinolone), pioglitazone, saxagliptin, famotidine, rabeprazole, and several laxatives and bowel-preparation agents.
- **Neuropsychiatric effects**: the literature reports neuropsychiatric side effects, including acute psychosis, with efavirenz.

The package insert warnings and contraindications could not be retrieved. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
SIV infection is an animal-model disease with only preclinical evidence (L4), and efavirenz acts through the HIV-1 RT component of the chimeric virus. This is a research-tool use, not a human repurposing opportunity.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, to complete safety screening
- Mechanism of action data (MOA)
- A decision on whether to pursue any human indication at all. Other predictions in this run do not offer a better route:
  - **Feline acquired immunodeficiency syndrome (rank 2)**: a veterinary indication with a single in vitro study (Hold).
  - **AIDS related complex (rank 5)**: a duplicate of the existing HIV indication, not new (Hold).
  - **Congenital HIV (rank 6)**: has one completed Phase 3 trial (NCT00102960, n=377) but its efavirenz-specific contribution is unclear, and first-trimester neural-tube defect and infant safety questions remain open. It is the only prediction with trial-level support and the best candidate for any follow-up.
  - **Ranks 3, 4 and 7–10 (model prediction only)**: no evidence, and efavirenz's neuropsychiatric and lipid-raising effects argue against benefit in some of them.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

