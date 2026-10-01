---
layout: default
title: Ivabradine
parent: Low Evidence (L5)
nav_order: 555
evidence_level: L5
indication_count: 10
---

# Ivabradine
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

# Ivabradine: From Angina and Heart Rate Control to Hypertrichosis

## One-Sentence Summary

Ivabradine is a heart-rate-lowering drug that inhibits the HCN (If) channel. A trial summary in the pack notes it is licensed for angina, and it is marketed in Singapore.
The TxGNN model predicts it may be effective for **hypertrichosis** with a very high score, but there are **0 clinical trials** and **0 publications** for this indication.
The prediction is a knowledge-graph signal only and is not supported by any clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Angina (from a trial summary in the pack; the Singapore licence records contain no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.79% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ivabradine slows heart rate by inhibiting HCN (If) channels in the pacemaker cells of the sinus node. Detailed mechanism data was not retrieved from DrugBank, so this description comes only from the pack's rationale text.

The pack finds no established pathway from HCN channel inhibition to hair growth. Hypertrichosis is a hair-growth disorder, while ivabradine's known actions are cardiac. The very high score (rank 3,572 in the model) most likely reflects graph proximity rather than biology. The other hair-related predictions (Ambras syndrome, hair shaft abnormality, trichomegaly) appear to be neighbours of the same artifact.

In short, this prediction should be treated as a hypothesis-generating signal and not as a credible repurposing direction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Six licences are registered. Five are listed below. No approved-indication text is recorded for any of them.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16202P | IVASWIFT Film-Coated Tablet 5 mg | Film-coated tablet | Ind-Swift Limited |
| SIN16201P | IVASWIFT Film-Coated Tablet 7.5 mg | Film-coated tablet | Ind-Swift Limited |
| SIN17220P | VARADIN Film-Coated Tablets 7.5 mg | Film-coated tablet | Genepharm S.A |
| SIN17221P | VARADIN Film-Coated Tablets 5 mg | Film-coated tablet | Genepharm S.A |
| SIN13409P | CORALAN Tablet 7.5 mg | Film-coated tablet | Les Laboratoires Servier Industrie |

All available products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone. There are no trials or literature for hypertrichosis, and no plausible mechanistic link between HCN inhibition and hair growth. The evidence level is L5.

**A better-supported alternative in the same output:**
- Among the model's other predictions, **pulmonary hypertension** (score 98.50%) has the strongest support at L3. It has rodent studies showing improved right ventricular function and fibrosis, plus small human studies in systemic-sclerosis PAH and COPD-associated PH suggesting tolerability. There are no Phase 3 or adequately powered randomized trials, and the registered trials listed do not test PH directly. It is best treated as a research question, not a decision-ready candidate.

**To proceed, the following is needed:**
- Approved indication text and safety information (warnings, contraindications) from the HSA package insert
- Mechanism of action data from DrugBank to allow a proper mechanistic assessment
- Any experimental or clinical rationale linking HCN channels to hair follicle biology, before further work on hypertrichosis
- If pulmonary hypertension is pursued, a dedicated evidence review, with a controlled trial as the eventual requirement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

