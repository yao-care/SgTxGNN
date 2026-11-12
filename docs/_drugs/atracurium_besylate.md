---
layout: default
title: Atracurium Besylate
parent: Low Evidence (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
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

Atracurium besylate is a non-depolarizing neuromuscular blocker, used as an adjunct in anaesthesia. The TxGNN model predicts it may be effective for **preeclampsia**, but **no clinical trials and no publications** in the data compiled for this report support this prediction. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (the mechanism points to use as a neuromuscular blocker in anaesthesia) |
| Predicted New Indication | Preeclampsia |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 4 of 4) |
| Number of Registrations | 4 (valid: 4) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Atracurium is known to be a non-depolarizing neuromuscular blocker that acts at nicotinic acetylcholine receptors at the motor endplate. This is the basis of its use for muscle relaxation during surgery and ventilation.

There is no established link between this mechanism and preeclampsia. Preeclampsia involves placental dysfunction, endothelial injury and angiogenic imbalance, none of which atracurium targets. The standard agent for seizure prevention in preeclampsia is magnesium sulfate, not atracurium. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same weakness. The ten highest-scoring predictions each have no supporting trials or literature:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 1 | Preeclampsia | 0.9997 | No mechanistic link |
| 2 | Cauda equina syndrome | 0.9995 | Surgical compressive emergency; no direct mechanism |
| 3 | Blepharospasm | 0.9992 | Conceptually plausible, but atracurium is systemic and short-acting; botulinum toxin is the established treatment |
| 4 | Migraine disorder | 0.9991 | No link to trigeminovascular or CGRP pathways |
| 5 | Obsolete neurogenic bladder | 0.9991 | Ontology term is obsolete, which lowers interpretability |
| 6 | Thrombotic disease | 0.9989 | No antithrombotic activity |
| 7 | Migraine with brainstem aura | 0.9988 | Same as migraine disorder |
| 8 | Severe pre-eclampsia | 0.9986 | Same as preeclampsia |
| 9 | Mild pre-eclampsia | 0.9986 | Same as preeclampsia |
| 10 | Irritable bowel syndrome | 0.9984 | Acts on skeletal, not smooth, muscle |

Of these, blepharospasm is the only one with a conceptually plausible link, through reduced involuntary muscle contraction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin sg-lic-20261106-atracurium_besylate-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Both are valid single-ingredient licences and both are injectable products." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 4 registrations for this drug, 4 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-atracurium_besylate-1 -->

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN06058P | TRACRIUM INJECTION 10 mg/ml | INJECTION | Valid |
| SIN14533P | Atracurium-hameln Injection 10mg/ml | INJECTION, SOLUTION | Valid |
| SIN14836P | ATRACURIUM LABATEC IV SOLUTION FOR INJECTION 10MG/ML | INJECTION, SOLUTION | Valid |
| SIN16945P | NOTRIXUM INJECTION 10MG/ML | INJECTION, SOLUTION | Valid |

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Both are valid single-ingredient licences and both are injectable products" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

