---
layout: default
title: Memantine
parent: Low Evidence (L5)
nav_order: 641
evidence_level: L5
indication_count: 10
---

# Memantine
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

# Memantine: From an NMDA Receptor Antagonist to Pulmonary Hypertension

## One-Sentence Summary

Memantine is an NMDA receptor antagonist that is marketed in Singapore as oral film-coated tablets, but the registration records do not state its approved indication.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but **0 clinical trials** and only **2 loosely related publications** currently support this direction.
The prediction is model-only, so the recommendation is **Hold**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the dataset. Memantine is an NMDA receptor antagonist, so any rationale rests on glutamate/NMDA receptor signalling.

One 2021 paper (Theranostics) notes that evidence has suggested a role for the glutamate/NMDA receptor axis in pulmonary arterial hypertension. However, its own data concern insulin sensitivity and lipid metabolism, not the pulmonary vasculature. The other paper is an early-phase safety and pharmacokinetic study of MN-08, a nitrate derivative of memantine under development for pulmonary arterial hypertension. That study enrolled healthy volunteers only, and MN-08 is a different molecule from memantine.

The review of the retrieved evidence found no credible mechanistic link. The high model score is not backed by any pulmonary vascular data on memantine itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Preclinical (mechanistic) | Theranostics | Studies NMDA receptor activation in insulin sensitivity and lipid metabolism. Pulmonary hypertension is mentioned only as background. |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/safety (healthy volunteers) | Clinical Drug Investigation | Single and multiple ascending doses of MN-08, a nitrate derivative of memantine being developed for pulmonary arterial hypertension. It reports safety and pharmacokinetics in healthy Chinese volunteers, not efficacy in patients. |

---

## Singapore Market Information

Showing 5 of 8 registrations.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15609P | ADMENTA 10 Film Coated Tablet 10 mg | Film-coated tablet | — |
| SIN15599P | AVANTEN Film-Coated Tablets 10 mg | Film-coated tablet | — |
| SIN15300P | MEMANTINE MEVON Film-Coated Tablets 10 mg | Film-coated tablet | — |
| SIN15120P | MARIXINO Film-Coated Tablets 10 mg | Film-coated tablet | — |
| SIN16928P | COGNIMET Film-Coated Tablet 10 mg | Film-coated tablet | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no registered trials, and the two retrieved papers do not test memantine in pulmonary hypertension. The related MN-08 work is a different molecule studied only in healthy volunteers.

**To proceed, the following is needed:**
- Mechanism of action data for memantine (currently unavailable)
- The HSA package insert, including warnings and contraindications
- Preclinical evidence that NMDA antagonism affects pulmonary vascular remodelling or pressure
- Review of MN-08 development results to see whether they carry over to memantine

**Note on other candidates:** In the same Evidence Pack, **migraine disorder** (rank 2) is much better supported. It has a completed Phase 3 trial (NCT04698525, n=33, versus sodium valproate), meta-analyses and a systematic review, and is graded L1 with a "Proceed with Guardrails" recommendation. Because the trial is small and lacks a placebo arm, a confirmatory placebo-controlled trial would still be needed. If the aim is near-term repurposing, this candidate deserves its own evaluation.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

