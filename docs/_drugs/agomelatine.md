---
layout: default
title: Agomelatine
parent: Low Evidence (L5)
nav_order: 45
evidence_level: L5
indication_count: 10
---

# Agomelatine
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

# Agomelatine: From Major Depressive Disorder to Benign Paroxysmal Torticollis of Infancy

## One-Sentence Summary

Agomelatine is a melatonergic antidepressant. The literature supplied for the other predicted indications describes it as an antidepressant for major depressive disorder, but the HSA record supplied does not state an approved indication.
The TxGNN model ranks **benign paroxysmal torticollis of infancy** first, but this is a model prediction only, with **0 clinical trials** and **0 publications** behind it.
Better-supported predictions exist further down the list, but they are depressive-disorder terms that are effectively already on-label (see Conclusion).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (inferred from the literature; the HSA indication text is blank) |
| Predicted New Indication | Benign paroxysmal torticollis of infancy |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the DrugBank record. Based on the supplied evidence review, agomelatine is a melatonin MT1/MT2 receptor agonist and a 5-HT2C receptor antagonist.

Benign paroxysmal torticollis of infancy is a pediatric paroxysmal movement disorder. Agomelatine's pharmacology has no established relevance to it, and no plausible mechanistic link was identified. The high score (rank 1,027 in the model's overall ranking) appears to be a model artifact, not a signal backed by biology or clinical data.

Agomelatine's safety in infants has also not been established, which makes this a difficult candidate to pursue even as a research question.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13770P | VALDOXAN Tablet 25mg | Tablet, film coated (oral) | Not stated in the supplied record |

Manufacturers: Les Laboratoires Servier Industrie; Servier (Ireland) Industries Ltd.

## Safety Considerations

- **Drug Interactions**: The DrugBank query returned no interaction records. This does not mean none exist; CYP1A2 inhibitors are a known concern for agomelatine.
- **Pediatric use**: Safety in infants is unestablished.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature and no plausible mechanism, and the target population (infants) has no established safety data. It should not advance.

**Other predicted indications from the same run (for reference):**

| Predicted Indication | Evidence Level | Recommendation | Note |
|------|------|------|------|
| Melancholia | L1 | Proceed with Guardrails | Effectively on-label MDD; level rests on systematic reviews and meta-analyses; primary Phase 3 trials still need confirming |
| Neurotic depression | L1 | Proceed with Guardrails | Legacy term for depressive disorders; effectively on-label |
| Dysthymic disorder | L4 | Research Question | Only a class-level antidepressant meta-analysis; agomelatine-specific data needed |
| Agoraphobia | L4 | Hold | Only retrieved paper studies depression, not agoraphobia |
| Neurotic disorder | L4 | Hold | Only a general antidepressant review |
| Six other predictions (including Ohdo syndrome variants, ligneous conjunctivitis, Keppen-Lubinsky syndrome) | L5 | Hold | No plausible mechanistic link and no evidence |

**To proceed, the following is needed:**
- HSA package insert (approved indication, warnings, contraindications)
- Mechanism-of-action data from DrugBank
- For the depressive-disorder candidates: confirmation against the primary Phase 3 RCTs, plus liver function monitoring and a CYP1A2 interaction review
- For dysthymic disorder: a targeted search for agomelatine-specific studies

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

