---
layout: default
title: Mannitol
parent: Low Evidence (L5)
nav_order: 629
evidence_level: L5
indication_count: 10
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

# Mannitol: From Osmotic Diuretic Use to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an intravenous osmotic diuretic that is marketed in Singapore under 2 registrations.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**.
This prediction has **0 clinical trials** and **1 general review** behind it, and the review does not mention mannitol, so the evidence is **model prediction only**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (mannitol is an osmotic diuretic) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Mannitol is known as an osmotic diuretic. It draws water out of cells and increases urine flow through osmotic water shift.

On mechanism, the prediction is hard to defend. NSIAD is a hyponatraemic condition driven by inappropriate antidiuresis (the body retains too much water). Mannitol lowers serum sodium through osmotic water shift. This is the opposite of what such a patient needs, and it could worsen the sodium imbalance. The very high TxGNN score is most likely an artefact of proximity in the knowledge graph. No mannitol-specific evidence supports it.

The 10 predictions in the Evidence Pack all sit at Hold. Several (malignant hyperthermia, periodic paralysis) show only indirect or supportive links, such as mannitol as a formulation excipient or a forced-diuresis aid. None shows disease-modifying activity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in evaluating patients with hyponatraemia, including under- and over-treatment. It contains no mannitol-specific data. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN10315P | Mannitol Intravenous Injection 20% | Injection | Euro-Med Laboratories Phil Inc |
| SIN05957P | Osmofundin Injection 20% | Injection | B. Braun Medical Industries Sdn Bhd |

The registry records do not list approved indication text for either product.

---

## Safety Considerations

Please refer to the package insert for safety information.

One mechanism-based concern applies to this prediction. Mannitol's osmotic effect may aggravate water and sodium imbalance in a hyponatraemic condition.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score is not backed by any trial, mannitol-specific literature or plausible mechanism, and the mechanism points the wrong way. Evidence stays at L5, and the safety review is blocked because package insert data are missing.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to support mechanistic analysis
- Any mannitol-specific clinical or preclinical evidence in NSIAD. Without it, the prediction should not advance.
- Review of the other nine predicted indications in the Evidence Pack, in case any has stronger support than this one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

