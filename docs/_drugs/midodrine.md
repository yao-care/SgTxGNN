---
layout: default
title: Midodrine
parent: Low Evidence (L5)
nav_order: 673
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Midodrine: predicted new indication Variably protease-sensitive prionopathy (evidence level L5). Approved use: Orthostatic hypotension"
---

# Midodrine
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

# Midodrine: From Orthostatic Hypotension to Variably Protease-Sensitive Prionopathy

## One-Sentence Summary

Midodrine is a peripheral alpha-1 adrenergic agonist, originally used for orthostatic hypotension and related autonomic disorders (multiple system atrophy, postural orthostatic tachycardia syndrome).
The TxGNN model's top-ranked prediction is **variably protease-sensitive prionopathy**, but there are **0 clinical trials** and **0 publications** supporting it, so this is a model prediction only.
The best-supported prediction in the list is **hypotensive disorder** (1 Phase 2 trial, 19 publications), but this largely overlaps with midodrine's existing approved use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Orthostatic hypotension (also multiple system atrophy and postural orthostatic tachycardia syndrome, per the knowledge graph); the Singapore licence text is blank |
| Predicted New Indication | Variably protease-sensitive prionopathy (top-ranked) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

For reference, the other predictions, ranked by evidence:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Hypotensive disorder | 99.90% | L2 | Proceed with Guardrails (largely existing use) |
| Sinoatrial node disease | 99.77% | L4 | Hold (safety concern) |
| Attention deficit-hyperactivity disorder | 99.94% | L5 | Hold |
| Other predictions (ranks 2, 5, 7–10) | 99.66–99.95% | L5 | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Midodrine is a prodrug whose active metabolite, desglymidodrine, selectively activates peripheral alpha-1 adrenergic receptors. This increases vascular tone and raises blood pressure, which is why it is used for orthostatic hypotension.

**For the top-ranked prediction (variably protease-sensitive prionopathy), no plausible mechanistic link was identified.** Midodrine does not appreciably cross the blood-brain barrier, and prion pathology is not known to respond to alpha-1 agonism. The high score reflects knowledge-graph proximity only. The same applies to faciodigitogenital syndrome, monogenic obesity, specific developmental disorder and the obsolete hypertelorism term, which is likely a graph artefact and should be excluded.

**Hypotensive disorder is the only mechanistically strong prediction.** Raising vascular tone directly addresses low blood pressure. However, this overlaps with the existing approved use, so it is not a true repurposing signal. Predictions in the ADHD family are weak and indirect because midodrine has minimal central activity. For sinoatrial node disease and sinoatrial block, midodrine can cause reflex bradycardia, so these are safety concerns rather than therapeutic opportunities.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction. The only trial in the predicted list relates to hypotensive disorder (rank 4):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | Completed | 21 | Effect of normalising blood pressure on cerebral blood flow in hypotensive individuals with spinal cord injury; small sample, not a Phase 3 confirmatory study |

## Literature Evidence

No literature is available for the top-ranked prediction (variably protease-sensitive prionopathy). Selected publications for hypotensive disorder (rank 4), the best-supported prediction:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | RCT | Hepatology | Terlipressin plus albumin vs midodrine and octreotide plus albumin in hepatorenal syndrome |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Review / expert position statement | Revue Neurologique | Orthostatic hypotension, including management when supine hypertension coexists |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Scientific statement | Hypertension | AHA statement on orthostatic hypotension in adults with hypertension |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | Consensus panel | Journal of Neurology | Screening, diagnosis and treatment of neurogenic orthostatic hypotension and supine hypertension |
| [41941194](https://pubmed.ncbi.nlm.nih.gov/41941194/) | 2026 | Review | JAMA Internal Medicine | Management of orthostatic hypotension |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Review | Autonomic Neuroscience | Pharmacologic treatment of neurogenic orthostatic hypotension |
| [37978969](https://pubmed.ncbi.nlm.nih.gov/37978969/) | 2024 | Clinical practice update | Gastroenterology | AGA update on vasoactive drugs and albumin in cirrhosis |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Review | Drugs | Midodrine pharmacology and use in orthostatic and secondary hypotensive disorders |

Other predictions have little or no literature. For ADHD, the single paper (PMID 42351284, a 2026 cohort study) describes healthcare use for orthostatic dysregulation in Japan and is not evidence of efficacy in ADHD. For sinoatrial node disease, the single paper (PMID 24634993) concerns baroreflex dysfunction in spinal cord injury and is not directly relevant.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11500P | GUTRON TABLET 5 mg (Takeda GmbH, Oranienburg plant) | Tablet (oral) | Not stated in the data compiled for this report |

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not from label text): pheochromocytoma (adrenal and sympathetic paraganglioma), thyrotoxicosis, hyperthyroidism, Graves disease, and several cancers (duodenum, small intestine, heart, adrenal gland).
- **Drug interactions:** 81 known interactions were identified. Examples:
  - Moderate: epinephrine (including ophthalmic and topical forms), ephedrine, bupropion, phentermine, diethylpropion, sibutramine, lorcaserin, mazindol, isometheptene, trospium, rolapitant, glycerol phenylbutyrate.
  - Minor: ranitidine, cimetidine, metformin.
- **Guardrails flagged for the hypotension use:** supine hypertension, urinary retention and bradycardia, especially with other vasoactive or AV-nodal agents. Reflex bradycardia is also a concern in sinus node dysfunction and sinoatrial block.

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, variably protease-sensitive prionopathy, has no trials, no literature and no plausible mechanism, since midodrine is peripherally restricted. The best-supported prediction, hypotensive disorder, largely restates the existing approved use rather than offering a new one, and could proceed with guardrails only as an extension of current practice.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications, which block safety screening
- Detailed mechanism of action data from DrugBank
- A defined approved-indication statement for licence SIN11500P
- For hypotensive disorder, confirmation of which specific populations (for example, spinal cord injury or hepatorenal syndrome) would be new relative to the approved use, together with a supine hypertension and bradycardia monitoring plan
- For the other predictions, no further work is suggested unless new mechanistic or clinical evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

