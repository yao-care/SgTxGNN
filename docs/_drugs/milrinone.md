---
layout: default
title: Milrinone
parent: Low Evidence (L5)
nav_order: 676
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Milrinone"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
description: "Milrinone: predicted new indication Alopecia (evidence level L5). Approved use: Not recorded in the local data"
---

# Milrinone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Milrinone: Alopecia
{: .text-alpha }

## One-Sentence Summary

Milrinone is an injectable PDE3 inhibitor used for congestive heart failure. The TxGNN model predicts it may be effective for **alopecia**, but **no clinical trials and no publications** currently support this direction. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action text is not available in the data compiled for this report. Pharmacology records, however, list milrinone as acting on phosphodiesterase 3A and 3B, and also on PDE2A and PDE5A. Inhibiting PDE3 raises cAMP. In the heart this increases contractility, and in vascular smooth muscle it causes vasodilation. That profile explains its use in decompensated heart failure.

The link to alopecia is speculative. One could argue that vasodilation might improve hair follicle perfusion, or that cAMP signalling might influence follicle biology. No study in the compiled data tests either idea. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Milrinone is not an established treatment for any hair disorder.

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
| SIN15249P | Milrinone-Baxter Concentrated Solution for Injection 10mg/10ml (Baxter Pharmaceuticals India Private Limited) | Injection, solution, concentrate | Not listed in the licence record |

The only registered product is an injectable. A systemic injection is a poor fit for a non-life-threatening condition like alopecia, so route compatibility would need to be addressed if this direction were pursued.

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from drug-disease relationships in the knowledge graph, not from package insert text): kidney disease, pyoureter, hypotensive disorder, myocardial infarction, coronary thrombosis, hemoglobinopathy, sudden cardiac arrest, heart conduction disease, pulmonary valve stenosis, hypertrophic cardiomyopathy (including the familial form).
- **Drug Interactions**: Five moderate-level interactions were identified: amifostine, diatrizoate, anagrelide, ozanimod and procarbazine.

For label-based warnings and contraindications, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The alopecia prediction has a very high model score but no supporting trials, literature or plausible mechanism. The safety profile of a systemic cardiac inotrope (hypotension, arrhythmia, cardiovascular contraindication signals) is hard to justify for a non-life-threatening condition.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence linking PDE3 inhibition or cAMP signalling to hair follicle biology
- Package insert warnings and contraindications from the HSA, to complete the safety screening
- Mechanism-of-action data from DrugBank
- An assessment of route compatibility, since only an injectable form is registered in Singapore

**Note on other predictions:** Among the other predicted indications compiled for milrinone, **congestive heart failure** and **acute pulmonary heart disease** have much stronger support (L2, Proceed with Guardrails). They are better candidates for further evaluation than alopecia. However, congestive heart failure is already milrinone's established use, so it is not a repurposing opportunity. The pulmonary heart disease support comes mainly from acute heart failure studies and one Phase 4 comparison with dobutamine.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

