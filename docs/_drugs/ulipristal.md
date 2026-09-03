---
layout: default
title: Ulipristal
parent: 僅模型預測 (L5)
nav_order: 1029
evidence_level: L5
indication_count: 10
---

# Ulipristal
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

# Ulipristal: From Original Indication Not on Record to Rheumatoid Arthritis (Predicted)

## One-Sentence Summary

> Ulipristal (DrugBank DB08867) has no original indication or market license data currently on file in Singapore, and mechanism-of-action data is also unavailable.
> The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**,
> but this is currently supported by only **1 clinical trial** (assessed as low relevance) and **no publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 90.31% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Ulipristal is not available in this evidence pack, and no original indication is on record. Based on the repurposing rationale provided alongside the prediction, Ulipristal is understood to be a **selective progesterone receptor modulator (SPRM)** — but there is no established mechanistic pathway connecting SPRM activity to the immune-inflammatory processes underlying rheumatoid arthritis.

The prediction score (90.31%) reflects knowledge graph embedding similarity computed by TxGNN, not a validated biological hypothesis. The single clinical trial retrieved for this indication (NCT04300465, a community-based cardiovascular lifestyle intervention study) was independently graded **C (not relevant)** — likely a keyword-matching artifact rather than genuine supporting evidence. No literature was found to corroborate the association.

Given the absence of MOA data, original indication data, and relevant clinical/literature evidence, this prediction should be treated as an early-stage hypothesis generated purely by the model, requiring substantial additional validation before any translational consideration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04300465](https://clinicaltrials.gov/study/NCT04300465) | N/A | Unknown | 64 | Community-based lifestyle intervention program targeting cardiovascular risk factors; does not involve Ulipristal or RA-directed treatment. Relevance graded **C (not relevant)** — likely a keyword mismatch rather than genuine supporting evidence. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Ulipristal is currently **not registered** in the Singapore market (0 licenses on file); no authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data are not currently available in this evidence pack.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is based solely on TxGNN embedding similarity (Evidence Level L5), with no mechanistically relevant clinical trials, no supporting literature, no mechanism-of-action data, and no market presence in Singapore. There is currently insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Original indication and confirmed mechanism of action (MOA) data for Ulipristal
- TFDA/HSA-equivalent package insert warnings and contraindications (currently a **Blocking** data gap per DG001)
- Targeted literature and clinical trial search specific to Ulipristal and rheumatoid arthritis (current trial match appears to be a false positive)
- A biologically plausible mechanistic hypothesis linking SPRM activity to RA pathophysiology before further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

