---
layout: default
title: Repaglinide
parent: Low Evidence (L5)
nav_order: 852
evidence_level: L5
indication_count: 10
---

# Repaglinide
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

# Repaglinide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Repaglinide is an oral insulin secretagogue used to control blood sugar in type 2 diabetes. The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia. There are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

The Singapore registration records do not include approved indication text, so the original indication is not listed in the table. Type 2 diabetes is taken from the mechanism and literature context in the Evidence Pack.

## Why is This Prediction Reasonable?

It is not well supported. Repaglinide blocks K-ATP channels (SUR1/Kir6.2) on pancreatic beta cells, which stimulates insulin release. Opsismodysplasia is an INPPL1-related skeletal dysplasia with impaired endochondral ossification. No pathway connects K-ATP channel blockade to bone development, so the high score (0.988) looks like a graph-based artefact rather than a biological signal.

The other nine predictions show the same pattern. They fall into three groups:

| Predicted Indication | Score | Assessment |
|------|------|------|
| Classic stiff person syndrome | 98.48% | Weak and indirect. The link is likely the co-occurrence with type 1 diabetes in the graph. Repaglinide does not act on the autoimmune neurological disease. |
| Focal stiff limb syndrome | 98.48% | Same as above. The identical score suggests it is inherited from the parent disease node. |
| Thiamine-responsive dysfunction syndrome | 98.47% | Limited plausibility. Repaglinide could treat the diabetes component symptomatically, but it would not address the anaemia or deafness. Thiamine is the primary treatment. |
| Drug-induced localized lipodystrophy | 97.80% | No direct link. Repaglinide is oral and does not restore fat tissue. |
| Centrifugal lipodystrophy | 97.65% | No direct link. |
| Pressure-induced localized lipoatrophy | 97.61% | No direct link. |
| Pancreatic agenesis | 97.58% | Mechanistically contradictory. Repaglinide needs functional beta cells, and these patients have little or none. Two reviews on repaglinide in type 2 diabetes are indirect evidence only. |
| Idiopathic localized lipodystrophy | 97.43% | No direct link. |
| Autoimmune oophoritis | 93.59% | No identifiable link. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Six registrations are on record. Five are listed below, and none includes approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN10674P | NOVONORM TABLET 2 mg | Tablet |
| SIN10673P | NOVONORM TABLET 1 mg | Tablet |
| SIN16374P | REPAGLINIDE MEVON TABLETS 2 MG | Tablet |
| SIN16376P | REPAGLINIDE MEVON TABLETS 0.5 MG | Tablet |
| SIN16375P | REPAGLINIDE MEVON TABLETS 1 MG | Tablet |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no trials or publications for opsismodysplasia, and the mechanism of repaglinide has no plausible link to skeletal dysplasia. None of the other nine candidates has clinical support, and pancreatic agenesis is mechanistically contradictory.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are required before any safety screening
- Detailed mechanism of action data from DrugBank
- A plausible biological pathway linking K-ATP channel blockade to INPPL1-related bone development, ideally supported by preclinical data
- Any published or registered studies of repaglinide in the predicted conditions

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

