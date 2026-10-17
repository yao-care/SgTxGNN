---
layout: default
title: Inclisiran
parent: Low Evidence (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Inclisiran: predicted new indication Potassium deficiency disease (evidence level L5). Approved use: Not stated in the Singapore licence data (the approved indication tex…"
monitor_inn: "Inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "migraine with or without aura, susceptibility to", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
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

# Inclisiran: From Lipid Lowering to Potassium Deficiency Disease

## One-Sentence Summary

Inclisiran is a small interfering RNA (siRNA) drug marketed in Singapore as LEQVIO, which silences PCSK9 in the liver to lower LDL cholesterol.
The TxGNN model predicts it may be effective for **potassium deficiency disease**, but **no clinical trials and no publications** currently support this prediction.
The model score is very high, yet it appears to be a model artifact rather than a real biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence data (the approved indication text is empty). Mechanistically, it is an LDL-C-lowering drug. |
| Predicted New Indication | Potassium deficiency disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, inclisiran is an siRNA that targets PCSK9 mRNA in hepatocytes, which increases LDL receptor availability and lowers LDL-C.

This mechanism has no known role in potassium homeostasis. No plausible mechanistic link between the original use and potassium deficiency disease was identified. The high TxGNN score appears to be a model artifact, and there are no trials or publications to back it.

**Other predictions reviewed:** The nine other top-ranked predictions are also weak. All are scored at the same L5 level, except aortic malformation (L4, see below).

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Esophageal disease | 99.87% | No established link; prediction only |
| 3 | Atypical coarctation of aorta | 99.86% | Congenital structural anomaly; LDL-C lowering would not correct it |
| 4 | Migraine disorder | 99.83% | Speculative vascular or lipid link only |
| 5 | Non-syndromic esophageal malformation | 99.83% | Developmental malformation; no plausible link |
| 6 | Migraine with brainstem aura | 99.78% | Neurological/channelopathy etiology; no link |
| 7 | Migraine with or without aura, susceptibility to | 99.78% | Redundant with other migraine entries, likely a shared-graph-neighbourhood effect |
| 8 | Aortic malformation | 99.76% | Related trials are not about this condition (see below) |
| 9 | Esophageal ulcer | 99.73% | No plausible mechanism |
| 10 | Raynaud disease | 99.73% | Only a speculative endothelial link |

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for potassium deficiency disease.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16295P | LEQVIO Solution for Injection in Prefilled Syringe 284 mg/1.5 mL | Injection, solution | Not available |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for inclisiran in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. There are no trials or publications, and no plausible mechanistic link between PCSK9 silencing and potassium homeostasis. The same applies to the other nine top-ranked predictions.

For aortic malformation (rank 8), two Phase 3 pediatric inclisiran trials were matched (NCT06597019 and NCT06597006). Both study familial hypercholesterolemia in children, not aortic malformation, so they do not support that indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- The approved indication text for the Singapore licence
- Any mechanistic or clinical rationale linking PCSK9 silencing to potassium deficiency disease, before further evaluation is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

