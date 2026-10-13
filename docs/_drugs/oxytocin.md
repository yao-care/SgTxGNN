---
layout: default
title: Oxytocin
parent: Low Evidence (L5)
nav_order: 753
evidence_level: L5
indication_count: 10
---

# Oxytocin
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

# Oxytocin: From Pregnancy Disorder with Abortive Outcome to Allergic Urticaria

## One-Sentence Summary

Oxytocin was originally used for pregnancy disorders with abortive outcome.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but **no clinical trials and no publications** currently support this direction, so it is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pregnancy disorder with abortive outcome (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 95.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, oxytocin is a peptide hormone used in obstetric care, and its efficacy in pregnancy-related conditions is established. Whether this carries over to allergic urticaria cannot be judged from the data compiled for this report.

Oxytocin receptor signalling has been proposed to influence inflammation and mast cell activity, which could in theory relate to urticaria. This idea is speculative and is not supported by any trial or publication in the data compiled for this report. The high TxGNN score reflects a knowledge-graph pattern, not demonstrated clinical benefit.

**Other predicted indications (all L5, all Hold):**

| Rank | Predicted Indication | TxGNN Score | Notes |
|------|------|------|------|
| 2 | Nasopharyngitis | 94.70% | No trials or literature |
| 3 | Papillary conjunctivitis | 93.17% | No trials or literature |
| 4 | Recalcitrant atopic dermatitis | 82.88% | No trials or literature |
| 5 | Atopic conjunctivitis | 79.19% | No trials or literature |
| 6 | IgE responsiveness, atopic | 77.43% | A trait rather than a treatable indication |
| 7 | Cold urticaria | 77.20% | No trials or literature |
| 8 | Esotropia | 77.10% | One retrieved paper, likely a keyword mismatch (see below) |
| 9 | Rosacea conjunctivitis | 75.20% | No trials or literature |
| 10 | Aquagenic urticaria | 63.88% | No trials or literature |

Most of the predictions fall within allergic or atopic conditions, which suggests a shared pattern in the model. None has been validated.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (allergic urticaria), currently no related literature is available.

For the rank 8 prediction (esotropia), one publication was retrieved. It is not direct evidence:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37597111](https://pubmed.ncbi.nlm.nih.gov/37597111/) | 2024 | Cohort | Graefe's Archive for Clinical and Experimental Ophthalmology | Retrospective case series and review on work-up of infants with isolated congenital sixth nerve palsy. It does not appear to evaluate oxytocin, so it is likely a spurious keyword match. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17068P | Oxytocin Grindeks Solution for Injection and Infusion 10 IU/mL | Injection, solution | Not stated in the available records |
| SIN02496P | Syntocinon Injection 10 IU/mL | Injection | Not stated in the available records |
| SIN03588P | Syntometrine Injection | Injection | Not stated in the available records |

All three are valid single-ingredient licences, and all are injectable. No cancelled licences were found.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not from label text):** hypertensive disorder, hypertension, placenta praevia, asphyxia neonatorum.
- **Drug Interactions:** 100 interactions were found. Examples of the main ones:
  - **Major:** dolasetron, cisapride
  - **Moderate:** epinephrine, ephedrine, clarithromycin, levofloxacin, ondansetron, palonosetron, famotidine, isometheptene, loperamide, and several laxatives (bisacodyl, lactulose, lactitol, castor oil, glycerin, polyethylene glycol)
  - **Minor:** metronidazole

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for allergic urticaria rests only on a computational score. There are no clinical trials, no supporting literature and no established mechanistic link. All ten predicted indications are at evidence level L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which block safety screening
- Mechanism of action data for oxytocin
- A literature and trial search aimed at oxytocin in urticaria or allergic disease, including preclinical mast cell studies
- Assessment of route and formulation fit, since all Singapore products are injectables and the predicted indications may need other routes
- Approved indication text for the Singapore licences, to confirm the original indication locally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

