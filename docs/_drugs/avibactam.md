---
layout: default
title: Avibactam
parent: Low Evidence (L5)
nav_order: 125
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Avibactam: predicted new indication Streptococcal pneumonia (evidence level L5). Approved use: Pyelonephritis"
monitor_inn: "Avibactam"
predicted_indications: ["streptococcal pneumonia", "influenza, severe, susceptibility to", "ureter tuberculosis", "urinary schistosomiasis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "staphylococcus aureus infection", "renal tuberculosis", "squamous cell lung carcinoma", "congenital analbuminemia"]
---

# Avibactam
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

# Avibactam: From Pyelonephritis to Streptococcal Pneumonia

## One-Sentence Summary

Avibactam is a beta-lactamase inhibitor used only in combination with a beta-lactam antibiotic (ceftazidime), originally for pyelonephritis.
The TxGNN model predicts it may be effective for **streptococcal pneumonia**, but **no clinical trials and no related publications** currently support this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pyelonephritis (from the knowledge-graph indication record; the Singapore licence text is blank) |
| Predicted New Indication | Streptococcal pneumonia |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, avibactam is a non-beta-lactam beta-lactamase inhibitor with no antibacterial activity of its own. It is used only alongside a beta-lactam such as ceftazidime, and its role is to protect that partner drug from being broken down by bacterial enzymes.

The link to streptococcal pneumonia is weak. Resistance in *Streptococcus pneumoniae* is mainly caused by altered penicillin-binding proteins rather than by beta-lactamase enzymes, so a beta-lactamase inhibitor is unlikely to add much. The high TxGNN score is a model output only, and it should not be read as evidence of benefit. No trials or publications were found for this indication.

For context, other predicted indications for this drug also lack support. The few with some related literature are:
- **Staphylococcus aureus infection** (score 98.97%): the literature is limited to reviews, resistance surveillance and in vitro studies of MDR/XDR infections (Evidence Level L4). Methicillin-resistant strains resist through PBP2a, which avibactam does not address.
- **Renal tuberculosis** (score 98.93%): the one linked paper concerns ceftazidime-avibactam treatment failure in carbapenem-resistant Enterobacteriaceae infections, not tuberculosis. A theoretical rationale exists because *M. tuberculosis* produces a beta-lactamase (BlaC) that avibactam inhibits in vitro.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for streptococcal pneumonia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15870P | ZAVICEFTA Powder for Concentrate for Solution for Infusion 2G/0.5G | Injection, powder, for solution | Not stated in the data compiled for this report |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based on the model score alone. There are no trials or publications for streptococcal pneumonia, and the mechanism is poorly matched because pneumococcal resistance is not mainly beta-lactamase-driven. The package insert safety data has also not been obtained.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently missing and blocking safety screening)
- Mechanism of action data for avibactam
- Microbiological evidence (in vitro susceptibility or animal data) for ceftazidime-avibactam against *S. pneumoniae*
- Clinical studies in streptococcal pneumonia, if the microbiological data are supportive
- Optionally, a separate review of the Staphylococcus aureus direction (L4), though its mechanistic rationale is also limited
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

