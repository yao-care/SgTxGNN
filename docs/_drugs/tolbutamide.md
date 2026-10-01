---
layout: default
title: Tolbutamide
parent: Low Evidence (L5)
nav_order: 992
evidence_level: L5
indication_count: 10
---

# Tolbutamide
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

# Tolbutamide: From Diabetes Treatment to Opsismodysplasia

## One-Sentence Summary

Tolbutamide is an oral sulfonylurea that blocks beta-cell KATP channels to trigger insulin secretion, and it is marketed in Singapore as a tablet.
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal dysplasia, with a score of 96.8%.
There are **0 clinical trials** and **0 publications** for this prediction, so it is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (tolbutamide is a sulfonylurea antidiabetic) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 96.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Tolbutamide is a sulfonylurea that closes KATP channels (Kir6.2/SUR1) in pancreatic beta-cells, which triggers insulin secretion.

Opsismodysplasia is a skeletal dysplasia linked to the INPPL1 gene. No identifiable biological link connects KATP-channel blockade to this condition. The high score (0.968) comes from graph proximity in the knowledge graph and is not backed by clinical or literature evidence. The prediction should be treated as a hypothesis only.

**Other predicted indications (all Hold, none with trials):**
- **Stiff person syndrome (classic and focal):** no direct mechanism. Any link would be indirect, through autoimmune and diabetes comorbidity (anti-GAD), and the provided data do not support it.
- **Thiamine-responsive dysfunction syndrome:** a theoretical link through its diabetes component and sulfonylurea-mediated insulin secretion. It is unverified.
- **Localized lipodystrophy cluster (drug-induced, centrifugal, pressure-induced, idiopathic):** speculative, based on graph proximity.
- **Autoimmune oophoritis:** lowest score (0.767), no identifiable mechanism.
- **Pancreatic agenesis (score 0.931):** the only candidate with retrieved literature, rated L4. The papers cover neonatal diabetes, KATP-channel (Kir6.2) activating mutations and hyperinsulinemia, not agenesis itself. True agenesis lacks functional beta-cells, so a secretagogue is unlikely to work. Any relevance probably applies only to KATP-related neonatal diabetes, which is a different condition. Only 10 of the 19 reported papers were provided, and relevance was not confirmed.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN04045P | TOBUMIDE TABLET 500 mg | Tablet | Sunward Pharmaceutical Private Limited |
| SIN04257P | TOLMIDE TABLET 500 mg | Tablet | Beacons Pharmaceuticals Pte. Ltd. |

Both products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph score, with no trials, no literature and no plausible mechanism linking KATP-channel blockade to opsismodysplasia. The Singapore package insert safety data have also not been obtained, which blocks safety screening.

**To proceed, the following is needed:**
- HSA package insert (warnings and contraindications), downloaded and parsed
- Mechanism of action data from DrugBank
- Any mechanistic or preclinical evidence linking tolbutamide to INPPL1-related skeletal dysplasia
- If pancreatic agenesis or KATP-related neonatal diabetes is pursued instead, the full 19-paper literature set with relevance review
- Route compatibility and similarity-to-original-indication assessments (currently pending)

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

