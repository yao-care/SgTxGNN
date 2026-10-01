---
layout: default
title: Ixekizumab
parent: Low Evidence (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
---

# Ixekizumab
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

# Ixekizumab: Predicted New Indication — Rheumatoid Vasculitis

## One-Sentence Summary

Ixekizumab is an IL-17A-neutralizing antibody, marketed in Singapore as Taltz, and it is used in immune-mediated inflammatory diseases.
The TxGNN model predicts it may be effective for **rheumatoid vasculitis** (score 97.5%), but only **1 loosely related clinical trial** and **0 publications** are linked to this prediction, so it rests almost entirely on the model.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Rheumatoid vasculitis |
| TxGNN Prediction Score | 97.53% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ixekizumab neutralizes IL-17A, a cytokine that drives inflammation in several autoimmune conditions. IL-17 signaling has been implicated in autoimmune vasculitis and rheumatoid-type inflammation, so a link to rheumatoid vasculitis is biologically plausible.

However, the plausibility is unproven. The only linked trial studies how to manage immunosuppressants around shoulder surgery in rheumatology patients, and it does not test ixekizumab against vasculitis. No publications support this indication. The high score most likely reflects proximity to related inflammatory-disease nodes in the knowledge graph rather than direct clinical evidence.

Detailed mechanism-of-action data was not supplied for this drug. The mechanism described above comes from the analysis of the prediction itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not yet recruiting | 80 | Compares stopping vs. briefly holding immunosuppressants before shoulder replacement in rheumatology patients. Not an ixekizumab efficacy study (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15501P | TALTZ Solution for Injection in Pre-filled Pen 80 mg/ml | Injection, solution | Eli Lilly and Company |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is L5, model-only. The single linked trial does not test ixekizumab, and no publications exist for rheumatoid vasculitis. The mechanism is plausible, but nothing yet shows benefit.

Two lower-ranked predictions in the same Evidence Pack look different. Inflammatory spondylopathy (rank 6) and vertebral disease (rank 9, which in this data maps to axial spondyloarthritis) are each supported by multiple completed Phase 3 RCTs and rated L1 with "Proceed with Guardrails". They appear to be established uses of the drug rather than true repurposing, and they should be reviewed separately from this one.

**To proceed, the following is needed:**
- Any clinical or observational evidence of IL-17A blockade in rheumatoid vasculitis, such as case series, mechanistic studies or a pilot trial
- Package insert warnings and contraindications from HSA, which are still missing and block safety screening
- The Singapore-approved indication text and the drug's original indication, both missing from the input
- Detailed mechanism-of-action data from DrugBank
- Route compatibility and similarity-to-original-indication assessments, which are still pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

