---
layout: default
title: Griseofulvin
parent: Low Evidence (L5)
nav_order: 492
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-20
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "creeping myiasis", "furuncular myiasis", "wound myiasis", "echinococcus granulosus infectious disease"]
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). In Singapore: 1 HSA registration (1 valid)"
---

# Griseofulvin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Griseofulvin: Myiasis
{: .text-alpha }

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used to treat dermatophyte infections such as tinea pedis, tinea corporis, tinea unguium and tinea barbae.
The TxGNN model predicts it may be effective for **myiasis** (score 0.9941), but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal (evidence level L5), and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for griseofulvin: "The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. […] The mechanism of griseofulvin consists of binding microtubular proteins, which are required for mitosis. Activity In Vivo Griseofulvin may be active against most strains of the following dermatophytes as described in the INDICATIONS AND USAGE section: Epidermophyton floccosum, Microsporum audouinii, Microsporum canis, Microsporum gypseum, Trichophyton crateriformis, Trichophyton gallinae, Trichophyton interdigitalis, Trichophyton megnini, Trichophyton mentagrophytes, Trichophyton rubrum, Trichophyton sulphureum, Trichophyton schoenleini, Trichophyton tonsurans and Trichophyton verrucosum." ([DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d), label version 2025-05-14; accessed 2026-11-19.) Based on general knowledge, griseofulvin is a fungistatic agent that disrupts fungal microtubules and mitosis. Its efficacy is established in dermatophyte infections of skin, hair and nails.

Myiasis is an infestation of tissue by fly larvae. Larvae are arthropods, so there is no plausible shared target with a fungal-specific agent. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The closely related subtypes (creeping, wound and furuncular myiasis) share an identical score of 0.9934, which suggests a shared learned similarity rather than independent evidence.

Other predicted indications are similarly weak:
- **Echinococcosis (E. granulosus and alveolar)**: a speculative parallel exists, because benzimidazoles also act on tubulin. No data show that griseofulvin affects helminth tubulin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for myiasis.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN07993P | HOVID-GRISEOFULVIN 500 TABLET B.P. 500mg | TABLET, FILM COATED | Valid |

<!-- licenses:end -->

No topical formulation is registered.

<!-- review:begin sg-lic-20261106-griseofulvin-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All three licences are valid single-ingredient oral products. No topical formulation is registered." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The Quick Overview and the table under Singapore Market Information show the current number of HSA registrations. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-griseofulvin-1 -->

---

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease links, not package insert text)**:
  - Liver failure
  - Porphyria (inherited porphyria and porphyrin metabolism disease)
  - Systemic lupus erythematosus (including paediatric)
  - Substance abuse/dependence
  - Agranulocytosis and neutropenia (including cyclic hematopoiesis and several congenital neutropenia syndromes)
- **Drug Interactions**: 100 interactions were identified. Most listed are Moderate, and a few are Minor. Notable examples:
  - Anticoagulants and antiplatelets: warfarin, apixaban, rivaroxaban, ticagrelor, dicoumarol (Moderate)
  - Antidiabetic agents: repaglinide, saxagliptin, linagliptin (Moderate); liraglutide (Minor)
  - Antiemetics: aprepitant, rolapitant (Moderate)
  - Antimalarials and antiparasitics: artemether, mefloquine, praziquantel (Moderate)
  - Others: eliglustat, naloxegol, nitisinone, macimorelin, fostamatinib (Moderate); acetylsalicylic acid (Minor)

Please refer to the package insert for key warnings, as label-based warnings and contraindications were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. There are no clinical trials or publications for myiasis, and no plausible mechanism links an antifungal to fly-larvae infestation. The near-identical scores across the myiasis subtypes suggest an ontology artifact rather than real signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, as the safety screening cannot proceed without them
- Mechanism of action data
- Any in vitro, animal or clinical evidence of griseofulvin activity against fly larvae (or, alternatively, a review of other predicted indications with more plausible links, such as systemic fungal infections)
- Confirmation of route compatibility, since only oral tablets are registered in Singapore

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "All three licences are valid single-ingredient oral products" | Corrected (revised 2026-11-24; earlier version kept in the record) | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-19 | "Detailed mechanism of action data is not currently available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: griseofulvin prescribing information, Sandoz Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=98829d90-b289-4bec-a625-7af412a5cb2d) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

