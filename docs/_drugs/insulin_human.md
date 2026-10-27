---
layout: default
title: Insulin Human
parent: Low Evidence (L5)
nav_order: 538
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Insulin Human: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus, type 1 diabetes mellitus…"
monitor_inn: "Insulin human"
predicted_indications: ["autoimmune oophoritis", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy"]
---

# Insulin Human
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Insulin Human: From Diabetes Mellitus to Autoimmune Oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin human is a replacement hormone originally used to treat type 1 and type 2 diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but **no clinical trials and no publications** currently support this prediction.
The prediction rests on knowledge-graph signals alone and is best read as a hypothesis rather than a therapeutic lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus, type 1 diabetes mellitus, diabetic ketoacidosis (the registered indication text for the Singapore product is not available) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin human is a recombinant human insulin whose efficacy in diabetes mellitus is well established, and it acts through insulin receptor signaling to regulate glucose and lipid metabolism.

A plausible but unproven link is that insulin signaling influences ovarian granulosa cell function and steroidogenesis. A more likely explanation is comorbidity. Autoimmune oophoritis is immune-mediated and often occurs within autoimmune polyendocrine syndromes that include type 1 diabetes. The model may therefore be picking up a disease-association pattern rather than a therapeutic effect of insulin.

Other top-ranked predictions show similar patterns:
- **Stiff person syndrome and focal stiff limb syndrome** (scores 99.81%): linked to anti-GAD65 autoimmunity and type 1 diabetes comorbidity. Insulin would treat the diabetes, not the neurological disease.
- **Thiamine-responsive dysfunction syndrome and pancreatic agenesis**: insulin already manages the associated diabetes, so these are extensions of the existing indication rather than new uses.
- **Localized lipodystrophies** (drug-induced, centrifugal, pressure-induced, idiopathic): injection-site lipodystrophy is a known adverse effect of subcutaneous insulin, so these predictions may reflect adverse-effect associations.
- **Opsismodysplasia**: a theoretical link exists through INPPL1 (SHIP2), a regulator of insulin/PI3K signaling, but there is no evidence that exogenous insulin helps.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02395P | ACTRAPID INJECTION 100 IU/ml | Injection | Not stated in the available data |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The ones listed below are examples, not the full list, and most are Moderate:
  - Sympathomimetics and bronchodilators: phenylephrine, pseudoephedrine, epinephrine, salbutamol
  - Other antidiabetic agents: metformin, pioglitazone, alogliptin, albiglutide
  - Corticosteroids and hormones: hydrocortisone, estradiol, ethinylestradiol
  - Cardiovascular and other drugs: acebutolol, benazepril, hydrochlorothiazide, acetazolamide, doxycycline, alpelisib
  - Ethanol (Moderate)
  - Minor: topical hydrocortisone and topical alclometasone

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a knowledge-graph score, with no clinical trials or literature. The likely drivers are autoimmune comorbidity with type 1 diabetes and disease-similarity propagation, not a therapeutic mechanism of insulin.

**To proceed, the following is needed:**
- Retrieval of the package insert (warnings, contraindications, approved indication) from the HSA website
- Detailed mechanism of action data for insulin human
- A literature and trial search specific to autoimmune oophoritis, including whether any insulin-related benefit has been reported beyond glycaemic control
- Review of the drug's relevance and route compatibility for the predicted condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

