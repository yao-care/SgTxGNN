---
layout: default
title: Atracurium Besylate
parent: Low Evidence (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Atracurium Besylate: predicted new indication Preeclampsia (evidence level L5). Approved use: Not stated in the Singapore licence records (the mechanism points to…"
monitor_inn: "Atracurium besylate"
predicted_indications: ["preeclampsia", "cauda equina syndrome", "blepharospasm", "migraine disorder", "obsolete neurogenic bladder (disease)", "thrombotic disease", "migraine with brainstem aura", "severe pre-eclampsia", "mild pre-eclampsia", "irritable bowel syndrome"]
---

# Atracurium Besylate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Atracurium Besylate: From Neuromuscular Blockade to Preeclampsia
{: .text-alpha }

## One-Sentence Summary

Atracurium besylate is a non-depolarizing neuromuscular blocker, used as an adjunct in anaesthesia. The TxGNN model predicts it may be effective for **preeclampsia**, but **no clinical trials and no publications** in the data compiled for this report support this prediction. It rests on a graph-based model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (the mechanism points to use as a neuromuscular blocker in anaesthesia) |
| Predicted New Indication | Preeclampsia |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Atracurium is known to be a non-depolarizing neuromuscular blocker that acts at nicotinic acetylcholine receptors at the motor endplate. This is the basis of its use for muscle relaxation during surgery and ventilation.

There is no established link between this mechanism and preeclampsia. Preeclampsia involves placental dysfunction, endothelial injury and angiogenic imbalance, none of which atracurium targets. The standard agent for seizure prevention in preeclampsia is magnesium sulfate, not atracurium. The high score is most likely a pattern in the knowledge graph rather than a pharmacological signal.

The other top-ranked predictions show the same weakness. The ten highest-scoring predictions each have no supporting trials or literature:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 1 | Preeclampsia | 99.97% | No mechanistic link |
| 2 | Cauda equina syndrome | 99.95% | Surgical compressive emergency; no direct mechanism |
| 3 | Blepharospasm | 99.92% | Conceptually plausible, but atracurium is systemic and short-acting; botulinum toxin is the established treatment |
| 4 | Migraine disorder | 99.91% | No link to trigeminovascular or CGRP pathways |
| 5 | Obsolete neurogenic bladder | 99.91% | Ontology term is obsolete, which lowers interpretability |
| 6 | Thrombotic disease | 99.89% | No antithrombotic activity |
| 7 | Migraine with brainstem aura | 99.88% | Same as migraine disorder |
| 8 | Severe pre-eclampsia | 99.86% | Same as preeclampsia |
| 9 | Mild pre-eclampsia | 99.86% | Same as preeclampsia |
| 10 | Irritable bowel syndrome | 99.84% | Acts on skeletal, not smooth, muscle |

Of these, blepharospasm is the only one with a conceptually plausible link, through reduced involuntary muscle contraction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06058P | TRACRIUM INJECTION 10 mg/ml | Injection | Not stated in the licence record |
| SIN14836P | ATRACURIUM LABATEC IV SOLUTION FOR INJECTION 10MG/ML | Injection, solution | Not stated in the licence record |

Both are valid single-ingredient licences and both are injectable products.

## Safety Considerations

- **Histamine release and hypotension**: Atracurium can release histamine, which may cause hypotension. This is a concern in a pregnant population with hypertensive disease.
- **Interaction with magnesium sulfate**: Magnesium sulfate potentiates neuromuscular blockade. In obstetric anaesthesia, such as caesarean section under general anaesthesia, this is a safety consideration.

Please refer to the package insert for further safety information, including formal warnings and contraindications. No drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no mechanistic basis. Its Evidence Level is L5, so it rests on model output only. In preeclampsia there is also a safety concern from histamine-related hypotension and potentiation by magnesium sulfate.

**To proceed, the following is needed:**
- The package insert from the Health Sciences Authority (HSA), covering warnings, contraindications and approved indications. This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Any preclinical or clinical evidence linking atracurium to the predicted disease. If the evaluation is redirected, blepharospasm is the only candidate with a plausible mechanism, but it would need to be compared against botulinum toxin.
- Route and formulation compatibility assessment for the predicted indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

