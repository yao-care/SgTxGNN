---
layout: default
title: Mannitol
parent: Low Evidence (L5)
nav_order: 635
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Brain oedema, intracranial hypertension, ocular hypertension…"
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "King-Denborough syndrome"]
---

# Mannitol
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

# Mannitol: From Intracranial Hypertension and Cerebral Oedema to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent originally used for conditions such as brain oedema, intracranial hypertension, ocular hypertension, pseudotumor cerebri, congestive heart failure and cystic fibrosis.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials** and only **1 general review article** behind this prediction, so the evidence is **model prediction only**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Brain oedema, intracranial hypertension, ocular hypertension, pseudotumor cerebri, congestive heart failure, cystic fibrosis (from the knowledge graph; the Singapore licences list no approved indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic diuretic. It stays in the blood and filtered urine, draws water out of tissues (for example the brain and eye) and promotes urine flow. Its efficacy in raised intracranial and intraocular pressure is established, and in theory it could influence water balance in hyponatraemia.

The mechanistic link to the predicted indication is weak. NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor, which makes the kidney retain water inappropriately. An osmotic load does not correct that receptor defect. The only linked paper is a general review of pitfalls in evaluating hyponatraemia, and it does not study mannitol. The high score is therefore a computational prediction without supporting clinical or mechanistic evidence.

The lower-ranked predictions are similarly weak:

- **Acute pulmonary heart disease:** only indirect links, such as hyperosmolar therapy in respiratory distress (1977) and a report of pulmonary oedema during mannitol treatment of water intoxication (1976), which suggests possible harm.
- **Malignant hyperthermia and related RYR1 myopathies:** mannitol appears only as an excipient in dantrolene products, and no therapeutic mechanism is supported.
- **Periodic paralysis:** mannitol is at most a carrier fluid or possible precipitant, not a treatment.
- **Nephrogenic diabetes insipidus:** osmotic diuresis would be expected to worsen polyuria, so harm is more plausible than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes ten common pitfalls in evaluating hyponatraemia. It is a general review and contains no mannitol-specific evidence. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10315P | MANNITOL INTRAVENOUS INJECTION 20% | Injection | Not stated in the data compiled for this report |
| SIN05957P | OSMOFUNDIN INJECTION 20% | Injection | Not stated in the data compiled for this report |

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not package insert text):** liver failure, hepatic coma and encephalopathy, anuria, impaired renal function, pulmonary oedema, intracranial haemorrhage, porphyria, thrombocytopenia, neutropenia, agranulocytosis, anaemia, sleep apnoea syndromes, anxiety and related disorders, and substance-related disorders. These should be confirmed against the official package insert.
- **Drug Interactions:** 100 interactions were identified. The one rated Major is **amikacin**. Examples rated Moderate include lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, carbamazepine, citalopram, desvenlafaxine, canagliflozin, dapagliflozin, cisatracurium, amifostine, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, and the contrast agents diatrizoate and iothalamic acid. Doxycycline is rated Minor.
- **Prediction-specific concerns:** the literature suggests possible harm in nephrogenic diabetes insipidus (worsened polyuria), hypokalaemic periodic paralysis (fluid and potassium shifts) and pulmonary oedema (volume expansion).

Please refer to the package insert for the official warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no clinical trials, the only linked paper is a general hyponatraemia review, and the proposed mechanism (osmotic load for a V2-receptor gain-of-function disorder) is not plausible. Several other top predictions show possible harm signals rather than benefit.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A specific mechanistic or preclinical rationale for mannitol in NSIAD, plus any mannitol-specific clinical data
- Review of the knowledge-graph contraindications (renal, hepatic, pulmonary oedema) against the target population
- Approved indication text for the two Singapore licences
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

