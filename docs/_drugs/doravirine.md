---
layout: default
title: Doravirine
parent: Low Evidence (L5)
nav_order: 347
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-20
monitor_inn: "Doravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Doravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). In Singapore: 1 HSA registration (1 valid)"
---

# Doravirine
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

## Doravirine: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## One-Sentence Summary

Doravirine is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 directly relevant publications** supporting this prediction.
The high score most likely reflects ontology proximity to HIV rather than independent evidence, and this is a veterinary indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for doravirine: "Doravirine is an antiretroviral drug. […] Doravirine is a pyridinone non-nucleoside reverse transcriptase inhibitor of HIV-1 and inhibits HIV-1 replication by non-competitive inhibition of HIV-1 reverse transcriptase (RT). The inhibitory concentration at 50% (IC 50 ) of doravirine for RNA-dependent DNA polymerization of recombinant wild-type HIV-1 RT in a biochemical assay was 12.2±2.0 nM (n=3)." ([DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25), label version 2026-07-09; accessed 2026-11-19.) Based on known information, doravirine is an HIV-1 NNRTI. It binds to HIV-1 reverse transcriptase and blocks viral replication. Its efficacy in HIV infection is the basis of its existing approvals.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, which is likely why the model scored this indication highly. However, NNRTIs generally have poor activity against FIV because the reverse transcriptase binding pocket differs. The high score of feline acquired immunodeficiency syndrome (0.9993) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Feline AIDS is also a veterinary indication, so it is not a human repurposing target.

Other predicted indications were reviewed as well:
- **Simian immunodeficiency virus infection** (0.9993): SIV, like HIV-2, is generally not susceptible to NNRTIs, so the mechanistic rationale is weak. It is primarily an animal-model indication.
- **Congenital HIV** and **AIDS related complex** (both 98.75%): These fall within the approved HIV-1 indication, so they are population or terminology extensions rather than true repurposing.
- Predictions for rare neurodevelopmental disorders and benign or malignant reproductive-system tumours have no plausible mechanistic link and look like TxGNN model (deep learning) artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports the top prediction. The only publications linked to the lower-ranked predictions are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Islatravir (a different drug) for HIV-1 treatment and prevention; linked to the SIV prediction but not about doravirine |
| [34459470](https://pubmed.ncbi.nlm.nih.gov/34459470/) | 2021 | Review | Current Opinion in HIV and AIDS | Drug interactions and adverse reactions in contemporary antiretroviral therapy; indirect context for safety and DDI |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN15869P | PIFELTRO FILM-COATED TABLET 100MG | TABLET, FILM COATED | Valid |

<!-- licenses:end -->

## Safety Considerations

**Drug Interactions**: 59 interactions were identified. Examples of the more significant ones include:
- **Major**: Dexamethasone, Lumacaftor
- **Moderate**: Glycerol phenylbutyrate, Metreleptin, Troglitazone, Deferasirox, Praziquantel, Griseofulvin
- **Minor**: Aprepitant, Cimetidine, Clarithromycin, Clotrimazole, Miconazole, Cobicistat, Ticagrelor, Ivacaftor, Zafirlukast, Chloramphenicol, Erythromycin, Fluconazole

Doravirine has a CYP3A-related interaction profile, so co-medications that induce or inhibit CYP3A need careful review.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. There are no trials or directly relevant literature, the mechanistic link is weak because NNRTIs generally lack FIV activity, and feline AIDS is a veterinary rather than human indication. The remaining predictions are either extensions of the existing HIV indication or lack any plausible mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Detailed mechanism of action data
- In vitro evidence of doravirine activity against FIV, if the veterinary direction is of interest
- For congenital HIV, which is the most clinically plausible item, pediatric and neonatal dosing, safety and efficacy data, to be evaluated as a population extension of the approved indication

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Pifeltro (doravirine) prescribing information, A-S Medication Solutions](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ff06e5cc-f47a-4779-816b-0e5b13e88a25) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

