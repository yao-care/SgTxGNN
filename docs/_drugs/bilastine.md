---
layout: default
title: Bilastine
parent: Low Evidence (L5)
nav_order: 160
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bilastine: predicted new indication Duodenal obstruction (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, urticaria, angioedema"
monitor_inn: "Bilastine"
predicted_indications: ["duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "gastric ulcer (disease)", "leather-bottle stomach", "duodenitis", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization"]
---

# Bilastine
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

# Bilastine: From Allergic Rhinitis to Duodenal Obstruction

## One-Sentence Summary

Bilastine is a second-generation antihistamine, originally used for allergic rhinitis and urticaria.
The TxGNN model predicts it may be effective for **duodenal obstruction**, but **0 clinical trials** and **0 publications** currently support this direction. The prediction is a graph-based inference only, and it has no plausible mechanism.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, urticaria, angioedema (from the knowledge graph; Singapore licence records contain no indication text) |
| Predicted New Indication | Duodenal obstruction |
| TxGNN Prediction Score | 97.73% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Bilastine is a selective H1 histamine receptor antagonist. Its action is on H1-mediated allergic responses such as wheal, flare and itch. Detailed mechanism of action data is not available beyond this H1 target.

On closer review, the prediction is hard to justify. Duodenal obstruction is a mechanical condition, and no H1-mediated mechanism is known to relieve it. Bilastine also has minimal effect on gastric acid secretion, which is an H2-mediated process. The high score most likely reflects shared histamine-pathway neighbours in the knowledge graph rather than real pharmacology. The score should be read as a hypothesis-generating signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17104P | BILAXTEN Tablet 20 mg (Pharmacy Only) | Tablet | Not stated in the licence record |
| SIN14661P | BILAXTEN Tablet 20 mg | Tablet | Not stated in the licence record |
| SIN15963P | BILAXTEN Oral Solution 2.5 mg/mL | Solution | Not stated in the licence record |
| SIN15874P | BILAXTEN Orodispersible Tablet 10 mg | Orally disintegrating tablet | Not stated in the licence record |
| SIN16474P | ALIGRIN Tablet 20 mg | Tablet | Not stated in the licence record |

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction query returned no drug-drug interactions. It returned only a pharmacology record identifying the H1 receptor as bilastine's target.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for duodenal obstruction rests only on a model score. There are no trials or publications, and there is no plausible H1-mediated mechanism for a mechanical obstruction. No further investment is justified at this time.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking H1 antagonism to duodenal obstruction, with preclinical support
- Any clinical or observational evidence, which does not currently exist
- The package insert (warnings, contraindications and approved indications) for the Singapore licences, to complete safety screening

**Note on other predictions in the same analysis:** Two lower-ranked predictions have real clinical support, but both are extensions of the already-approved urticaria indication.
- **Cold urticaria** has one completed Phase 2/3 placebo-controlled crossover trial (NCT01271075, n=20) and a supporting publication (PMID 23742030). It is rated L2 and treated as a research question.
- **Allergic urticaria** has a completed Phase 3 RCT (NCT00421109, n=522) and a 2023 meta-analysis (PMID 36380619). It is rated L1 and "Proceed with Guardrails", but it largely confirms the existing label rather than representing true repurposing.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

