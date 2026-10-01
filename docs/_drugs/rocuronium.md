---
layout: default
title: Rocuronium
parent: Low Evidence (L5)
nav_order: 871
evidence_level: L5
indication_count: 10
---

# Rocuronium
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

# Rocuronium: From Neuromuscular Blockade in Anesthesia to Migraine Disorder

## One-Sentence Summary

Rocuronium is a non-depolarizing neuromuscular blocker given by injection, used as an adjunct in anesthesia.
The TxGNN model predicts it may be effective for **migraine disorder**, but only **1 clinical trial** (unrelated to migraine efficacy) and **0 publications** are linked to this prediction.
The prediction is model output only, and the evidence does not support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (rocuronium is generally used as a neuromuscular blocker in anesthesia) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

It is not well supported. Detailed mechanism of action data is not available in the input. Rocuronium is known to block nicotinic acetylcholine receptors at the neuromuscular junction, causing skeletal muscle relaxation. It has no known action on migraine pathways such as CGRP, the trigeminovascular system, or cortical spreading depression.

Its original use (skeletal muscle paralysis during surgery) is pharmacologically unrelated to migraine, which is a neurovascular headache disorder. The very high TxGNN score (about 99.9%) is most likely an artifact of how the knowledge graph propagates scores, not a real therapeutic signal.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3520 | Pharmacokinetics of understudied drugs given to children as standard of care. No migraine endpoint; relevance grade C. |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17025P | NOVERON SOLUTION FOR INJECTION 10MG/ML | Injection, solution | Not listed in record |
| SIN15106P | ROCURONIUM KABI SOLUTION FOR INJECTION/INFUSION 10MG/ML | Injection, solution | Not listed in record |
| SIN09479P | ESMERON INJECTION 50 mg/5ml | Injection | Not listed in record |
| SIN15237P | ROCURONIUM-HAMELN INJECTION 10MG/ML | Injection, solution | Not listed in record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction rests on model score alone, with no efficacy trials, no relevant literature, and no plausible mechanism. The other nine ranked predictions (for example migraine with brainstem aura, cauda equina syndrome, irritable bowel syndrome, and sciatic neuropathy) are also at L5 with no mechanistic rationale. Headache disorder has some anesthesia-related trials and publications, but headache appears there only as a perioperative side effect or secondary outcome, not as a treatment target.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are currently missing and block safety screening
- Mechanism of action data from DrugBank, to allow a proper mechanistic-link assessment
- Any preclinical or clinical evidence that neuromuscular blockade benefits migraine. Without it, this candidate should not advance.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

