---
layout: default
title: Glimepiride
parent: 僅模型預測 (L5)
nav_order: 477
evidence_level: L5
indication_count: 10
---

# Glimepiride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Glimepiride: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Glimepiride is a third-generation sulfonylurea oral antidiabetic agent, established in clinical practice for the management of Type 2 Diabetes Mellitus (T2DM) by stimulating pancreatic insulin secretion.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**,
however, **no clinical trials or publications** currently exist to support this specific repurposing direction — this is a purely model-derived prediction with no independent empirical backing.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus (third-generation sulfonylurea) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Glimepiride is a third-generation sulfonylurea that stimulates insulin secretion by binding to the SUR1 (sulfonylurea receptor 1) subunit of the pancreatic β cell K-ATP channel, causing channel closure, membrane depolarization, calcium influx, and insulin release. It also possesses partial PPAR-γ agonist activity and has been shown to enhance insulin receptor phosphorylation, giving it a limited insulin-sensitising profile beyond pure secretagogue activity.

Focal Stiff Limb Syndrome (FSLS) is a rare, localized variant of Stiff Person Syndrome (SPS) — an autoimmune neurological disorder whose hallmark is circulating GAD65 (glutamic acid decarboxylase 65) autoantibodies. Crucially, GAD65 is also a principal autoantigen in Type 1 Diabetes Mellitus (T1DM), and SPS/FSLS is well documented to co-occur with T1DM. This shared autoimmune target almost certainly represents the biological edge through which the TxGNN knowledge graph connects Glimepiride (a diabetes drug) to FSLS.

Despite the elegant autoantigen overlap, the mechanistic reasoning is fragile at the therapeutic level. Glimepiride acts downstream of autoimmunity — it stimulates residual β cells via the SUR1 receptor — and has no demonstrated direct effect on GAD65 autoantibody production, T-cell regulation, or GABAergic inhibitory tone in the spinal cord (the proximate cause of FSLS rigidity). The predicted association is therefore considered highly speculative and requires systematic experimental validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Glimepiride in Focal Stiff Limb Syndrome.

---

## Literature Evidence

Currently no related literature available for Glimepiride in Focal Stiff Limb Syndrome.

---

## Singapore Market Information

Glimepiride is currently **not marketed in Singapore**. No product registrations were identified in the regulatory database (total licenses: 0).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence for this predicted indication rests solely on a TxGNN model score (L5); no clinical trials, observational data, or peer-reviewed publications support the use of Glimepiride in Focal Stiff Limb Syndrome. The postulated mechanistic link — shared GAD65 autoimmunity — does not translate into a plausible pharmacodynamic pathway for Glimepiride's known molecular targets, making a biological rationale difficult to construct at this stage.

**To proceed, the following is needed:**
- Preclinical mechanistic studies examining whether Glimepiride or any sulfonylurea exerts immunomodulatory effects on GAD65-driven autoimmunity or GABAergic signalling (the BB rat data for T1DM prevention, PMID 7475982, offers a distant precedent worth reviewing)
- Literature search broadened to encompass the full SPS spectrum and co-morbid diabetes to identify any indirect signal
- Clarification of Glimepiride's MOA from DrugBank (remediation: query DrugBank API, Data Gap DG002)
- Regulatory safety data from the package insert to enable baseline safety profiling (remediation: download TFDA/SmPC PDF, Data Gap DG001)
- Assessment of whether Singapore market entry is feasible, given current zero-registration status

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

