---
layout: default
title: Dolutegravir
parent: Low Evidence (L5)
nav_order: 343
evidence_level: L5
indication_count: 3
monitor_inn: "Dolutegravir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-20
description: "Dolutegravir: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease, AIDS"
---

# Dolutegravir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Dolutegravir: From HIV Infection to Feline Acquired Immunodeficiency Syndrome
{: .text-alpha }

## One-Sentence Summary

Dolutegravir is an HIV integrase inhibitor, originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, a veterinary disease in cats.
Evidence is thin: **0 clinical trials** and **1 publication** that studies a combination antiretroviral regimen in FIV-infected cats.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease, AIDS (relation recorded in the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 4 of 4) |
| Number of Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for dolutegravir: "Dolutegravir is an HIV-1 antiretroviral agent. […] Dolutegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral DNA integration which is essential for the HIV replication cycle. Strand transfer biochemical assays using purified HIV-1 integrase and pre-processed substrate DNA resulted in IC 50 values of 2.7 nM and 12.6 nM." ([DailyMed: Tivicay (dolutegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=63df5af3-b8ac-4e76-9830-2dbb340af922), label version 2026-08-25; accessed 2026-11-19.) Based on the known drug class, dolutegravir is an integrase strand transfer inhibitor (INSTI) that blocks the integration of viral DNA into the host genome. Feline immunodeficiency virus (FIV) is a lentivirus, like HIV, and has its own integrase enzyme, so the mechanism is plausible. This reasoning comes from general knowledge of the drug class, not from the supplied data.

The very high TxGNN score probably reflects the shared antiretroviral and lentiviral target space. The only supporting publication evaluated a combination regimen that included dolutegravir in FIV-infected cats. It is a veterinary study, so it does not point to a new human indication.

Other predictions in the data are weaker or not relevant to human use:
- **Simian immunodeficiency virus infection** (score 0.9985): several preclinical macaque and in vitro studies exist, mainly on dolutegravir resistance and antiretroviral therapy models. It is a research model of HIV, not a new human indication.
- **A rare neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter** (score 0.9980): no trials or publications and no plausible mechanism. Evidence level L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Preclinical/veterinary study | Viruses | Evaluated the pharmacokinetics and clinical outcomes of a combination regimen (dolutegravir, tenofovir, emtricitabine) in FIV-infected domestic cats. The available text does not state the efficacy results. |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN14579P | TIVICAY TABLET 50MG | TABLET, FILM COATED | Valid |
| SIN16504P | TIVICAY DISPERSIBLE TABLET 5 MG | TABLET, FOR SUSPENSION | Valid |
| SIN15100P | TRIUMEQ FILM COATED TABLET 50mg/600mg/300mg | TABLET, FILM COATED | Valid |
| SIN15989P | DOVATO FILM-COATED TABLET 50MG/300MG | TABLET, FILM COATED | Valid |

<!-- licenses:end -->

Note: DOVATO and TRIUMEQ are fixed-dose combination products. Their licences are not evidence of how single-ingredient dolutegravir is approved.

## Safety Considerations

- **Drug Interactions**: 62 interactions are recorded. The listed ones include:
  - Major: polyvalent cation products such as aluminium hydroxide, calcium salts (acetate, carbonate, citrate, gluconate, lactate, phosphate), iron, magnesium salts, kaolin, attapulgite, and magaldrate. These likely reduce dolutegravir absorption, so dosing should be separated from these products.
  - Minor: aprepitant, cimetidine, clarithromycin, clotrimazole, dexamethasone.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only evidence for the top prediction is a single veterinary study of a combination regimen, with no clinical trials. The predicted disease affects cats, so it does not translate into a human repurposing opportunity.

**To proceed, the following is needed:**
- The full text of PMID 37112803 to confirm the efficacy results attributable to dolutegravir in FIV-infected cats
- Clarification of whether a veterinary development path is within scope
- Mechanism of action data for the drug
- Package insert warnings and contraindications from the HSA, to complete safety screening
- Approved indication text for the Singapore licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Tivicay (dolutegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=63df5af3-b8ac-4e76-9830-2dbb340af922) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

