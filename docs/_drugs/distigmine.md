---
layout: default
title: Distigmine
parent: Low Evidence (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
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

# Distigmine: From Detrusor Underactivity to Myasthenia Gravis with Thymus Hyperplasia

## One-Sentence Summary

Distigmine is a long-acting cholinesterase inhibitor. The literature describes it as a treatment for detrusor underactivity, but the Singapore registration record does not state an indication.
The TxGNN model predicts it may be effective for **myasthenia gravis with thymus hyperplasia**.
There are currently **0 clinical trials** and **0 publications** for this indication, so the prediction rests on model output and class-level reasoning only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Detrusor underactivity (per PMID 20410601; not stated in the Singapore registration record) |
| Predicted New Indication | Myasthenia gravis with thymus hyperplasia |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 (no studies for this indication; the source pack labels it L4 on mechanism reasoning) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Distigmine is a long-acting cholinesterase inhibitor. Blocking acetylcholinesterase raises acetylcholine levels at the neuromuscular junction. This is the standard symptomatic mechanism used in autoimmune myasthenia gravis.

A receptor-binding study (PMID 20410601) found that distigmine binds muscarinic and nicotinic receptors. It also inhibited blood acetylcholinesterase more weakly than neostigmine did. This supports its cholinergic pharmacology, but it was studied in detrusor underactivity, not in myasthenia gravis.

The link to myasthenia gravis is indirect. It rests on the drug class, not on any distigmine study in this subtype. The high TxGNN score is a model output and is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this indication.

Two publications turned up under other predictions, and neither supports this one:
- PMID 20410601 (2010, *Biological & Pharmaceutical Bulletin*) is a receptor-binding study in detrusor underactivity. It was found under "disease of receptor activity".
- PMID 19172815 (2009, *No to Hattatsu*) is a case-level report on congenital myasthenic syndrome with acetylcholine receptor deficiency. It was found under the refractory congenital myasthenia prediction.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02915P | UBRETID TABLET 5 mg (Globopharm) | Tablet (oral) | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information. No interactions were found in the drug interaction query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanism is plausible for autoimmune myasthenia gravis, but there are no trials or publications for this indication and no safety data. Other candidates in the list are weaker. Several have no plausible link (hypersplenism, atypical hemolytic-uremic syndrome). Others conflict with the mechanism (myasthenia refractory to acetylcholinesterase inhibitors) or carry unfavourable safety concerns (neonatal and fetal indications).

**To proceed, the following is needed:**
- Obtain the HSA package insert and confirm the registered indication, warnings and contraindications
- Retrieve mechanism of action data from DrugBank
- Search for distigmine-specific clinical evidence in myasthenia gravis, including regional registries
- Compare distigmine against established cholinesterase inhibitors, given its long duration of action

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

