---
layout: default
title: Nusinersen
parent: Low Evidence (L5)
nav_order: 719
evidence_level: L5
indication_count: 10
---

# Nusinersen
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

# Nusinersen: From Spinal Muscular Atrophy to Tendinopathy

## One-Sentence Summary

Nusinersen is an antisense oligonucleotide given by injection into the spinal fluid, used to treat spinal muscular atrophy (SMA).
The TxGNN model lists **tendinopathy** as a possible new use, but the score is uninformative (50%).
There are **no clinical trials** and **no publications** for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Spinal muscular atrophy (the Singapore registration record has no indication text; SMA is taken from the retrieved literature) |
| Predicted New Indication | Tendinopathy |
| TxGNN Prediction Score | 50.0% (rank 51,833) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

It is not well supported. Nusinersen is an antisense oligonucleotide delivered into the spinal fluid. It changes how the SMN2 gene is spliced (exon 7 inclusion) in the central nervous system, which raises the level of functional SMN protein in SMA. Detailed mechanism-of-action data are not available in the Evidence Pack, so this description comes from the mechanistic assessment in the pack.

Tendinopathy is a peripheral musculoskeletal condition. It has no known link to SMN splicing, and nusinersen is designed to act in the central nervous system. A score of 0.5 carries no ranking information, so the prediction looks like a graph-level artifact rather than a biologically grounded signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16751P | SPINRAZA Solution for Injection 12mg/5mL | Injection, solution | Not listed in the registration record |

The manufacturers are Patheon Italia S.p.A. and Vetter Pharma-Fertigung GmbH & Co. KG. The only route is injectable.

---

## Safety Considerations

No warnings, contraindications or drug interaction records were found in the Evidence Pack. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or literature evidence for tendinopathy, no plausible mechanism, and the model score is uninformative. The other nine predicted indications also score 0.5 and also lack supporting evidence, so none of them offers a better lead.

**To proceed, the following is needed:**
- Mechanistic evidence, such as preclinical data, linking SMN2 splice modulation to tendon pathology
- Evidence that intrathecal delivery could work for a peripheral tendon condition
- HSA package insert warnings and contraindications, to enable safety screening
- Drug mechanism-of-action data from DrugBank
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

