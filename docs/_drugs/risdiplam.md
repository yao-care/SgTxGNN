---
layout: default
title: Risdiplam
parent: Low Evidence (L5)
nav_order: 874
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Risdiplam: predicted new indication Acne (evidence level L5). Approved use: Not listed in the Singapore license record (the drug is known as an S…"
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)"]
---

# Risdiplam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Risdiplam: From Spinal Muscular Atrophy to Acne
{: .text-alpha }

## One-Sentence Summary

Risdiplam is an oral SMN2 splicing modifier that is marketed in Singapore as EVRYSDI and is generally used for spinal muscular atrophy (SMA). The Singapore license record compiled for this report does not list an indication text.
The TxGNN model predicts it may be effective for **acne**, but there are currently **0 clinical trials** and **0 publications** supporting this direction. This is a model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore license record (the drug is known as an SMA treatment) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 0.9945 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Risdiplam is known to be an SMN2 splicing modifier that increases inclusion of exon 7 in SMN2 transcripts, and it is used in spinal muscular atrophy. No mechanistic pathway is supported that links SMN2 splicing modulation to sebaceous gland biology or *Cutibacterium acnes*.

The high TxGNN score (0.9945, rank 6885) is therefore best read as a possible TxGNN model (deep learning) artifact, for example driven by shared gene-network neighbours or off-target associations, and not as independent biological evidence. The other top-ranked predictions are also unsupported by the data:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16349P | EVRYSDI POWDER FOR ORAL SOLUTION 0.75 MG/ML | Powder, for solution | Not listed in the license record |

---

## Safety Considerations

- **Drug Interactions** (2 moderate-level interactions found):
  - Metformin (Moderate)
  - Methylnaltrexone (Moderate)

Please refer to the package insert for other safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. No clinical trials or publications were found for acne or for any of the other nine top-ranked indications, and no plausible mechanistic link is supported. The evidence level is L5 for all of them.

**To proceed, the following is needed:**
- Mechanism of action data for risdiplam from DrugBank, to allow a proper mechanistic analysis
- The HSA package insert, to confirm the approved indication, warnings and contraindications, and complete safety screening
- Preclinical or mechanistic evidence connecting SMN2 splicing modulation to acne biology
- A route compatibility assessment: risdiplam is available only as an oral solution, while acne is commonly treated topically
- A review of whether the prediction is a TxGNN model (deep learning) artifact, for example by checking the shared neighbours that drive the score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

