---
layout: default
title: Lipegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 598
evidence_level: L5
indication_count: 10
---

# Lipegfilgrastim
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

# Lipegfilgrastim: From Chemotherapy-Induced Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Lipegfilgrastim is a long-acting PEGylated granulocyte colony-stimulating factor (G-CSF) analog, generally used to support neutrophil recovery in patients undergoing myelosuppressive chemotherapy (detailed original indication and mechanism-of-action records are currently unavailable). The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, but this direction is currently supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic assessment flags the link as a likely knowledge-graph artifact rather than a genuine pharmacological relationship.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Singapore registration data (drug is a G-CSF analog generally indicated for chemotherapy-induced neutropenia) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 (model prediction only — no clinical trials or literature) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Lipegfilgrastim is not available in the evidence pack. Based on general pharmacological classification, Lipegfilgrastim is a PEGylated analog of granulocyte colony-stimulating factor (G-CSF); drugs in this class act on G-CSF receptors to stimulate proliferation and differentiation of myeloid (neutrophil) precursor cells in the bone marrow. This is a lineage-specific mechanism aimed at the granulocyte pathway, not at megakaryocyte function or platelet release.

The predicted new indication, "primary release disorder of platelets," involves defective platelet release from megakaryocytes — a process governed by different marrow-lineage signaling than the granulocyte pathway targeted by G-CSF. The evidence pack's own repurposing rationale explicitly states there is no known direct molecular pathway connecting the two, and attributes the high TxGNN score more plausibly to proximity between "hematologic disease" nodes within the underlying knowledge graph than to a true causal or mechanistic relationship.

Given the unresolved mechanism-of-action gap, the complete absence of supporting clinical trials or literature, and the caution flagged directly within the rationale itself, this prediction should be treated as a hypothesis-generating signal only — not as evidence of therapeutic plausibility. The same caveat broadly applies to the other nine candidate indications in this evidence pack, all of which likewise carry L5 evidence and Hold recommendations.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Lipegfilgrastim is not currently registered or marketed in Singapore (0 authorizations on file; market status: Not Marketed).

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication lacks any direct mechanistic, clinical trial, or literature support, and the rationale itself identifies the association as a probable knowledge-graph artifact rather than a genuine drug-disease relationship. In addition, a **Blocking** data gap (HSA/TFDA label warnings and contraindications, DG001) means an initial safety screening cannot yet be performed, and Lipegfilgrastim is not currently registered in the Singapore market.

**To proceed, the following is needed:**
- HSA-approved package insert data (key warnings, contraindications) — currently a **Blocking** data gap (DG001)
- Confirmed mechanism of action from DrugBank or primary literature — currently a **High**-severity data gap (DG002)
- Preclinical or mechanistic studies directly linking G-CSF pathway activity to megakaryocyte function or platelet release
- Any real-world or case-level evidence supporting use in platelet release disorders
- Clarification of Singapore market/registration status before further local development is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

