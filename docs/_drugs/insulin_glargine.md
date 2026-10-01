---
layout: default
title: Insulin Glargine
parent: Low Evidence (L5)
nav_order: 532
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog. It is used to control blood glucose in diabetes, although the Singapore registration data does not state the approved indication text.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The evidence is model prediction only, so the recommended decision is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diabetes mellitus (general drug knowledge; the registration data has no indication text) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Insulin glargine is a basal insulin analog that acts on the insulin receptor to control glucose. Its efficacy in diabetes is well established.

There is no plausible direct mechanism linking it to autoimmune oophoritis. The high score most likely reflects knowledge-graph proximity through autoimmune polyendocrine syndromes, where autoimmune diabetes and oophoritis co-occur. In that setting, insulin would treat only the diabetes component, not the ovarian autoimmunity.

The prediction should therefore be read as a knowledge-graph association, not as a mechanistically supported new use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications (Top 10)

The other nine predictions are also weak. Only one has any retrieved literature.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Thiamine-responsive dysfunction syndrome | 99.61% | L5 | Insulin manages the diabetes symptom only, not the SLC19A2 transporter defect. |
| 3 | Focal stiff limb syndrome | 99.60% | L5 | Link is through anti-GAD autoimmunity and co-existing type 1 diabetes. |
| 4 | Classic stiff person syndrome | 99.60% | L5 | Same rationale as rank 3. |
| 5 | Opsismodysplasia | 99.59% | L5 | Speculative link through INPPL1/SHIP2 in insulin signaling; no clinical rationale. |
| 6 | Pancreatic agenesis | 99.43% | L4 | Insulin replacement is mechanistically direct, but this is hormone replacement rather than repurposing. The 6 retrieved papers are general insulin or diabetes reviews, a MODY5 case, and veterinary reports. None is specific to pancreatic agenesis or to insulin glargine. |
| 7 | Drug-induced localized lipodystrophy | 99.42% | L5 | Insulin is a known cause of this condition, so this is a safety signal, not a therapy. |
| 8 | Centrifugal lipodystrophy | 99.39% | L5 | Speculative link only. |
| 9 | Pressure-induced localized lipoatrophy | 99.38% | L5 | No known mechanism. |
| 10 | Idiopathic localized lipodystrophy | 99.34% | L5 | Insulin is a recognized cause of localized lipodystrophy, which argues against therapeutic use. |

## Singapore Market Information

Six registrations exist. Five are listed below; the registration data has no approved-indication text for any of them.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16009P | Semglee Solution for Injection in a Prefilled Pen 100U/ml | Injection, solution |
| SIN15138P | Toujeo SoloStar 300 units/ml solution for injection in a pre-filled pen | Injection, solution |
| SIN11934P | Lantus 100 Units/ml Solution for injection in a vial | Injection |
| SIN13426P | Lantus SoloStar 100 Units/ml Solution for injection in a pre-filled pen | Injection, solution |
| SIN15540P | Soliqua Solution for Injection in a Pre-filled Pen 100 units/ml + 50 mcg/ml | Injection, solution |

## Safety Considerations

- **Adverse effect relevant to the predictions**: Injection-site lipodystrophy (lipoatrophy and lipohypertrophy) is a known effect of subcutaneous insulin.
- **Drug Interactions**: No interaction records were found in the queried data.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, autoimmune oophoritis, rests on model prediction alone, with no trials, no literature and no plausible mechanism. Insulin would address only the co-existing diabetes. Among the other top 10 predictions, pancreatic agenesis is standard insulin replacement rather than repurposing. The lipodystrophy entries reflect insulin as a cause, not a treatment.

**To proceed, the following is needed:**
- Singapore package insert warnings, contraindications and approved indications, which are currently blocking safety screening
- Mechanism of action data, for example from the DrugBank API
- Expert review of whether pancreatic agenesis should be handled as standard replacement therapy outside the repurposing pipeline
- Dropping the lipodystrophy predictions from repurposing consideration and recording them as safety signals

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

