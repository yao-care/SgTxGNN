---
layout: default
title: Griseofulvin
parent: Low Evidence (L5)
nav_order: 488
evidence_level: L5
indication_count: 10
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

# Griseofulvin: From Dermatophyte (Tinea) Infections to Myiasis

## One-Sentence Summary

Griseofulvin is an oral antifungal used mainly for dermatophyte skin infections.
The TxGNN model predicts it may be effective for **myiasis** (fly-larva infestation) with a very high score, but **no clinical trials** and only **1 publication** (a 1970 veterinary review that does not show efficacy) are linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatophyte (tinea) infections (from general drug knowledge; the local registrations do not state an indication) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Griseofulvin is known as an antifungal that disrupts fungal microtubules and mitosis and is deposited in keratin. That is why it works in superficial skin, hair and nail fungal infections.

Myiasis is an infestation by fly larvae, not a fungal disease, so this mechanism has no plausible link to it. The high score most likely reflects the drug's position in the knowledge graph, close to other skin-infection and parasitic-disease terms. The same pattern applies to the related terms creeping, wound and furuncular myiasis, all scoring about 99.3% with no trials or literature.

Other predicted indications are also weak:
- **Cutaneous candidiasis (98.7%, L4):** Griseofulvin is generally considered inactive against *Candida*. The 20 retrieved records are general reviews of skin fungal infections and other antifungals, and none shows griseofulvin efficacy in candidiasis. Azole and allylamine alternatives are well established.
- **Blastomycosis (97.1%, L4):** This is a systemic fungal infection. Griseofulvin is a superficial-infection agent, and standard treatment is itraconazole or amphotericin B.
- **Echinococcosis (98.4-99.3%, L5):** The only rationale is a speculative tubulin analogy to benzimidazoles such as albendazole, with no experimental data.
- **Toxoplasmosis and Bacteroidaceae infections (L5):** No mechanism or data support them.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Review | The Veterinary Record | Review of parasitic skin diseases of dogs and cats. No abstract is available, and it does not show griseofulvin efficacy against myiasis. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN00899P | HEXENE-FORTE TABLET 500 mg (Sunward Pharmaceutical) | Tablet |
| SIN07993P | HOVID-GRISEOFULVIN 500 TABLET B.P. 500mg (Hovid Bhd.) | Film-coated tablet |
| SIN00896P | HEXENE TABLET 125 mg (Sunward Pharmaceutical) | Tablet |

All three products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5). There are no clinical trials, and the only publication is a 1970 veterinary review that does not support efficacy. The antifungal mechanism has no plausible link to fly-larva infestation, and established treatments exist for the other predicted indications.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications. This is a blocking gap for safety screening.
- Detailed mechanism of action data from DrugBank.
- Any experimental (in vitro or in vivo) evidence of griseofulvin activity against the predicted target organisms. If none is found, the myiasis prediction is unlikely to justify further work.
- For the fungal predictions (cutaneous candidiasis, blastomycosis), direct comparative data showing an advantage over current standard therapy.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

