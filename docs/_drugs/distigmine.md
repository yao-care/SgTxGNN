---
layout: default
title: Distigmine
parent: Low Evidence (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Distigmine: predicted new indication Myasthenia gravis with thymus hyperplasia (evidence level L5). Approved use: Myasthenia gravis"
---

# Distigmine
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

# Distigmine: From Myasthenia Gravis to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Distigmine is a long-acting cholinesterase inhibitor, originally used to treat myasthenia gravis and related neuromuscular junction disorders.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**,
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myasthenia gravis (the approved indication text for the Singapore licence is not available; the original indications come from the knowledge graph: myasthenia gravis, adult-onset myasthenia gravis, neuromuscular junction disease, acute cystitis) |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, distigmine is a long-acting acetylcholinesterase inhibitor. Its efficacy in myasthenia gravis is established, and mechanistically it may be applicable to this subtype. By slowing the breakdown of acetylcholine, it enhances cholinergic transmission at the neuromuscular junction.

Myasthenia gravis with thymus hyperplasia is a variant of the already approved indication. The underlying problem, reduced functional acetylcholine receptors at the neuromuscular junction, is the same, so symptomatic cholinesterase inhibition is plausible.

The very high TxGNN score most likely reflects how close this disease is to the original indication in the knowledge graph. It is not independent clinical evidence for this subtype.

### Other Predictions Reviewed

| Rank | Predicted Indication | Score | Assessment |
|------|------|------|------|
| 2 | Myasthenia, limb-girdle, autoimmune | 99.998% | Shares the pathophysiology of myasthenia; plausible but no evidence |
| 3 | Neonatal myasthenia gravis | 99.998% | Similar mechanism; neonatal safety and dosing for distigmine are undocumented |
| 4 | Autoimmune disease of peripheral nervous system | 99.998% | Broad category; only the myasthenia-like portion has a mechanistic link |
| 5 | Disease of receptor activity | 99.998% | Non-specific term; one preclinical paper points to detrusor underactivity (bladder) as a research question |
| 6 | Hypersplenism | 99.964% | No clear mechanistic link; likely a knowledge-graph artifact |
| 7 | Atypical haemolytic-uraemic syndrome with B factor anomaly | 99.957% | Complement-mediated; no plausible link, likely spurious |
| 8 | Fetal akinesia deformation sequence | 99.941% | Tenuous link via neuromuscular dysfunction; fetal exposure raises safety concerns |
| 9 | Congenital myasthenic syndrome with tubular aggregates | 99.674% | Response to cholinesterase inhibitors is variable by subtype |
| 10 | Congenital myasthenia refractory to acetylcholinesterase inhibitors | 99.671% | By definition refractory, and some subtypes may worsen; the score is not credible |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (myasthenia gravis with thymus hyperplasia), currently no related literature is available.

One paper was found for a lower-ranked prediction (rank 5, "disease of receptor activity"):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20410601](https://pubmed.ncbi.nlm.nih.gov/20410601/) | 2010 | Preclinical (receptor binding study) | Biological & Pharmaceutical Bulletin | Distigmine binds directly to muscarinic and nicotinic receptors in radioreceptor assays. Its inhibition of blood acetylcholinesterase was weaker than neostigmine. Studied in the context of detrusor underactivity. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02915P | UBRETID TABLET 5 mg (Globopharm) | Tablet | Not stated in available data |

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found in the data compiled for this report. Two cautions arise from the prediction review:
- Neonatal and fetal use: pediatric, neonatal and fetal safety and dosing for distigmine are undocumented.
- Congenital myasthenic syndromes: some subtypes (e.g., slow-channel syndrome, DOK7) can be worsened by cholinesterase inhibitors.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a subtype of an indication distigmine already treats, so it is mechanistically plausible. However, there are no trials or literature for this subtype, and the score mainly reflects closeness in the knowledge graph. Several lower-ranked predictions (hypersplenism, atypical haemolytic-uraemic syndrome) have no plausible mechanism.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- The approved indication text for the Singapore licence, to confirm how far the current label already covers myasthenia gravis subtypes
- A targeted literature and trial search on distigmine in thymic hyperplasia-associated myasthenia gravis
- Dosing and safety data for neonatal or paediatric use before considering those predictions
- Optional research question: distigmine in detrusor underactivity, supported by the 2010 receptor-binding study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

