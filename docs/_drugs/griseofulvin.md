---
layout: default
title: Griseofulvin
parent: Low Evidence (L5)
nav_order: 492
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Griseofulvin: predicted new indication Myiasis (evidence level L5). Approved use: Dermatophyte infections (tinea pedis, tinea corporis, tinea unguium…"
monitor_inn: "Griseofulvin"
predicted_indications: ["myiasis", "creeping myiasis", "wound myiasis", "furuncular myiasis", "echinococcus granulosus infectious disease", "cutaneous candidiasis", "toxoplasmosis", "alveolar echinococcosis", "blastomycosis", "Bacteroidaceae infectious disease"]
---

# Griseofulvin
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

# Griseofulvin: From Tinea (Dermatophyte) Infections to Myiasis

## One-Sentence Summary

Griseofulvin is an oral antifungal originally used to treat dermatophyte infections such as tinea pedis, tinea corporis, tinea unguium and tinea barbae.
The TxGNN model predicts it may be effective for **myiasis** (score 99.41%), but **no clinical trials and no publications** currently support this prediction.
It is a model-only signal (evidence level L5), and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatophyte infections (tinea pedis, tinea corporis, tinea unguium, tinea barbae, scalp or beard dermatophytosis, groin and perianal dermatophytosis). Singapore licence records contain no approved-indication text, so these come from the knowledge-graph indication data. |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data compiled for this report. Based on general knowledge, griseofulvin is a fungistatic agent that disrupts fungal microtubules and mitosis. Its efficacy is established in dermatophyte infections of skin, hair and nails.

Myiasis is an infestation of tissue by fly larvae. Larvae are arthropods, so there is no plausible shared target with a fungal-specific agent. The high TxGNN score is a graph-based prediction only. The closely related subtypes (creeping, wound and furuncular myiasis) share an identical score of 99.34%, which suggests a shared ontology-derived signal rather than independent evidence.

Other predicted indications are similarly weak:
- **Echinococcosis (E. granulosus and alveolar)**: a speculative parallel exists, because benzimidazoles also act on tubulin. No data show that griseofulvin affects helminth tubulin.
- **Cutaneous candidiasis** (score 98.71%): the only prediction with literature, but griseofulvin is generally considered ineffective against Candida. The 20 retrieved publications are mostly reviews of superficial mycoses and other antifungals (terbinafine, itraconazole, ketoconazole, tolnaftate). They are indirect evidence at best (evidence level L4).
- **Blastomycosis** (score 97.08%): a systemic fungal infection, so class plausibility is higher. Azoles and amphotericin B are the standard treatments, and the three retrieved publications (1963–1994) are general reviews with only indirect support (L4).
- **Toxoplasmosis and Bacteroidaceae infection**: no plausible mechanism, and no evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for myiasis.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00899P | HEXENE-FORTE TABLET 500 mg | Tablet | Not stated in registration record |
| SIN07993P | HOVID-GRISEOFULVIN 500 TABLET B.P. 500mg | Tablet, film coated | Not stated in registration record |
| SIN00896P | HEXENE TABLET 125 mg | Tablet | Not stated in registration record |

All three licences are valid single-ingredient oral products. No topical formulation is registered.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

