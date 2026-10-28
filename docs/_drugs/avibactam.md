---
layout: default
title: Avibactam
parent: Low Evidence (L5)
nav_order: 125
evidence_level: L5
indication_count: 4
monitor_inn: "Avibactam"
predicted_indications: ["ureter tuberculosis", "urinary schistosomiasis", "polyclonal hyperviscosity syndrome", "hyperamylasemia"]
last_modified_at: 2026-10-23
description: "Avibactam: predicted new indication Ureter tuberculosis (evidence level L5). Approved use: Pyelonephritis"
---

# Avibactam
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Avibactam: From Pyelonephritis to Ureter Tuberculosis
{: .text-alpha }

## One-Sentence Summary

Avibactam is a beta-lactamase inhibitor, and pyelonephritis is its original indication.
The TxGNN model predicts it may be useful for **ureter tuberculosis**, but **no clinical trials and no publications** were found for this prediction, so it is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pyelonephritis (a relation recorded in the knowledge graph; the Singapore licence record has no indication text) |
| Predicted New Indication | Ureter tuberculosis |
| TxGNN Prediction Score | 0.9911 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Avibactam is a non-beta-lactam beta-lactamase inhibitor (diazabicyclooctane). It restores the activity of ceftazidime against Ambler class A, class C and some class D enzymes. Detailed mechanism of action data is not available in the data compiled for this report, so this description comes from general pharmacological knowledge.

*Mycobacterium tuberculosis* produces a chromosomally encoded class A beta-lactamase (BlaC). Preclinical work has reported that avibactam can inhibit BlaC, which gives a plausible but indirect rationale. The high score probably reflects the shared genitourinary infection context of the original pyelonephritis relation, rather than any direct evidence in tuberculosis.

Ceftazidime-avibactam is not a standard anti-tuberculosis regimen. Any use would need confirmation of activity and dosing in dedicated studies.

Other predictions for this drug were also screened and are weaker:
- **Urinary schistosomiasis** (score 0.9906): the cause is a parasite, with no plausible target for avibactam. The only link is treating a secondary bacterial urinary infection. Praziquantel remains the standard of care.
- **Polyclonal hyperviscosity syndrome** (0.9901) and **hyperamylasemia** (0.9901): no mechanistic link could be identified. The scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15870P | ZAVICEFTA Powder for Concentrate for Solution for Infusion 2G/0.5G | Injection, powder, for solution | Not stated in the licence record |

The number of approvals is 1 licence, which is valid and marketed.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no clinical trials or publications for ureter tuberculosis. The mechanistic link through BlaC inhibition is indirect and preclinical, and ceftazidime-avibactam is not part of standard tuberculosis treatment.

**To proceed, the following is needed:**
- Download and review the HSA package insert for warnings and contraindications, which is currently a blocking gap
- Obtain detailed mechanism of action data from DrugBank
- Preclinical or clinical evidence of activity against *M. tuberculosis* in the urinary tract
- Dosing, penetration and safety data for this use, and a comparison against standard anti-tuberculosis therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

