---
layout: default
title: Inclisiran
parent: Low Evidence (L5)
nav_order: 527
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
description: "Inclisiran: predicted new indication Potassium deficiency disease (evidence level L5). Approved use: Not stated in the Singapore licence data (the approved indication tex…"
monitor_inn: "Inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
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

## Inclisiran: From Lipid Lowering to Potassium Deficiency Disease
{: .text-alpha }

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
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for inclisiran: "Inclisiran is a double-stranded small interfering ribonucleic acid (siRNA), conjugated on the sense strand with triantennary N-Acetylgalactosamine (GalNAc) to facilitate uptake by hepatocytes. In hepatocytes, inclisiran utilizes the RNA interference mechanism and directs catalytic breakdown of mRNA for PCSK9." ([DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44), label version 2026-08-19; accessed 2026-11-19.) Based on known information, inclisiran is an siRNA that targets PCSK9 mRNA in hepatocytes, which increases LDL receptor availability and lowers LDL-C.

This mechanism has no known role in potassium homeostasis. No plausible mechanistic link between the original use and potassium deficiency disease was identified. The high TxGNN score appears to be a model artifact, and there are no trials or publications to back it.

**Other predictions reviewed:** The nine other top-ranked predictions are also weak. All are scored at the same L5 level, except aortic malformation (L4, see below).

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 2 | Esophageal disease | 0.9987 | No established link; prediction only |
| 3 | Atypical coarctation of aorta | 0.9986 | Congenital structural anomaly; LDL-C lowering would not correct it |
| 4 | Migraine disorder | 0.9983 | Speculative vascular or lipid link only |
| 5 | Non-syndromic esophageal malformation | 0.9983 | Developmental malformation; no plausible link |
| 6 | Migraine with brainstem aura | 0.9978 | Neurological/channelopathy etiology; no link |
| 8 | Aortic malformation | 0.9976 | Related trials are not about this condition (see below) |
| 9 | Esophageal ulcer | 0.9973 | No plausible mechanism |
| 10 | Raynaud disease | 0.9973 | Only a speculative endothelial link |

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for potassium deficiency disease.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN16295P | LEQVIO SOLUTION FOR INJECTION IN PREFILLED SYRINGE 284 MG/1.5 ML | INJECTION, SOLUTION | Valid |

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Leqvio (inclisiran) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6fc0afca-4513-4c35-b594-6544aee29a44) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

