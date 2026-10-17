---
layout: default
title: Doravirine
parent: Low Evidence (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Doravirine: predicted new indication Feline acquired immunodeficiency syndrome (evidence level L5). Approved use: HIV infectious disease"
monitor_inn: "Doravirine"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "male reproductive organ cancer"]
---

# Doravirine
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

# Doravirine: From HIV Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Doravirine is an HIV-1 non-nucleoside reverse transcriptase inhibitor (NNRTI), originally used to treat HIV infection and AIDS.
The TxGNN model predicts it may be effective for **feline acquired immunodeficiency syndrome**, but there are currently **0 clinical trials** and **0 directly relevant publications** supporting this prediction.
The high score most likely reflects ontology proximity to HIV rather than independent evidence, and this is a veterinary indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HIV infectious disease; AIDS (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Feline acquired immunodeficiency syndrome |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, doravirine is an HIV-1 NNRTI. It binds to HIV-1 reverse transcriptase and blocks viral replication. Its efficacy in HIV infection is the basis of its existing approvals.

Feline immunodeficiency virus (FIV) is a lentivirus related to HIV, which is likely why the model scored this indication highly. However, NNRTIs generally have poor activity against FIV because the reverse transcriptase binding pocket differs. The high score therefore most likely reflects closeness to HIV/AIDS in the knowledge graph rather than independent evidence. Feline AIDS is also a veterinary indication, so it is not a human repurposing target.

Other predicted indications were reviewed as well:
- **Simian immunodeficiency virus infection** (99.93%): SIV, like HIV-2, is generally not susceptible to NNRTIs, so the mechanistic rationale is weak. It is primarily an animal-model indication.
- **Congenital HIV** and **AIDS related complex** (both 98.75%): These fall within the approved HIV-1 indication, so they are population or terminology extensions rather than true repurposing.
- Predictions for rare neurodevelopmental disorders and benign or malignant reproductive-system tumours have no plausible mechanistic link and look like knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature directly supports the top prediction. The only publications linked to the lower-ranked predictions are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | Islatravir (a different drug) for HIV-1 treatment and prevention; linked to the SIV prediction but not about doravirine |
| [34459470](https://pubmed.ncbi.nlm.nih.gov/34459470/) | 2021 | Review | Current Opinion in HIV and AIDS | Drug interactions and adverse reactions in contemporary antiretroviral therapy; indirect context for safety and DDI |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15869P | PIFELTRO FILM-COATED TABLET 100MG | Tablet, film coated | Not stated in the available records |
| SIN15909P | DELSTRIGO FILM COATED TABLET 100MG/300MG/300MG | Tablet, film coated | Not stated in the available records |

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

