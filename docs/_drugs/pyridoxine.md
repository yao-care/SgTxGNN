---
layout: default
title: Pyridoxine
parent: Low Evidence (L5)
nav_order: 835
evidence_level: L5
indication_count: 10
---

# Pyridoxine
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

# Pyridoxine: From Original Indication (Not Recorded) to Gonococcal Urethritis

## One-Sentence Summary

Pyridoxine (vitamin B6) is marketed in Singapore in several oral and injectable products, but the Evidence Pack does not record its original indications.
The TxGNN model predicts it may be effective for **gonococcal urethritis**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 93.87% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Pyridoxine is a vitamin B6 form that the body converts to pyridoxal 5'-phosphate, a cofactor in amino acid and neurotransmitter metabolism. Its established roles are correcting B6 deficiency and treating B6-dependent conditions.

Mechanistically, this prediction is hard to justify. Gonococcal urethritis is a bacterial infection caused by *Neisseria gonorrhoeae*, and pyridoxine has no known antimicrobial action against it. The model gave "Ureaplasma urethritis" exactly the same score (93.87%), which suggests the signal comes from shared neighbours in the knowledge graph rather than from pharmacology. No trials or publications were found to support a link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Five of the 14 registrations are shown. Approved indication text is not available for any of them.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15301P | DICLECTIN DELAYED RELEASE TABLETS 10MG/10MG | Tablet, delayed release |
| SIN16865P | BONJESTA EXTENDED-RELEASE TABLETS 20 MG/20 MG | Tablet, film coated, extended release |
| SIN06258P | NEUROBION TABLET | Tablet, sugar coated |
| SIN12077P | DANEURON TABLET | Tablet, film coated |
| SIN15098P | NEUROBION TABLET (OTC) | Tablet, sugar coated |

Registered dosage forms across all licences include oral tablets and injectables (injection; powder for solution).

---

## Safety Considerations

Please refer to the package insert for safety information.

The pack also notes that excess pyridoxine can cause sensory neuropathy (PMIDs 25137514 and 1463588, from another candidate indication's literature). Any dose-related risk for this drug should be checked against the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There is no antimicrobial rationale, no trial and no literature, so the signal is likely a graph artifact. Pyridoxine would also not replace antibiotic treatment of a bacterial urethral infection.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any in vitro or clinical evidence of anti-gonococcal activity, which does not currently exist in the pack
- Original approved indications, to assess the relationship to the predicted one

**Other candidates in the pack:** Among the ten predicted indications, "vitamin deficiency disorder" (rank 10, score 85.50%) has the most supporting evidence. It is rated L2 in the pack with a "Proceed with Guardrails" recommendation. However, its supporting trials are mostly multivitamin or multi-nutrient studies, with limited B6-specific evidence. It is also likely a rediscovery of existing nutritional use rather than true repurposing. It would warrant a dedicated report with dose caps and neuropathy monitoring.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

