---
layout: default
title: Tedizolid Phosphate
parent: 僅模型預測 (L5)
nav_order: 948
evidence_level: L5
indication_count: 10
---

# Tedizolid Phosphate
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

# Tedizolid Phosphate: From Antibacterial Therapy (ABSSSI) to Post-Infectious Syndrome

## One-Sentence Summary

Tedizolid phosphate is an oxazolidinone antibiotic; publicly available trial data show its established use is for Acute Bacterial Skin and Skin Structure Infections (ABSSSI) and investigational use in ventilator-associated bacterial pneumonia (VABP).
The TxGNN model's top prediction, **post-infectious syndrome**, is supported by only **1 clinical trial** and **no literature**, and that single trial is a known ABSSSI study whose relevance to this disease label is judged low-confidence.
This candidate should be treated with caution — the underlying signal likely reflects re-detection of tedizolid's known antibacterial use rather than a genuine new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (0 licenses). Globally, tedizolid is approved for Acute Bacterial Skin and Skin Structure Infections (ABSSSI); it was also studied (unsuccessfully pursued) for ventilator-associated bacterial pneumonia |
| Predicted New Indication | Post-infectious syndrome |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is flagged as a data gap in this evidence pack. Based on the supporting trial descriptions, tedizolid phosphate is an oxazolidinone-class antibiotic that inhibits bacterial 50S ribosomal protein synthesis, giving it activity against Gram-positive organisms including MRSA.

The relationship between the drug's known use and the predicted indication is weak. "Post-infectious syndrome" is a broad ontology term rather than a specific diagnostic entity, and its only supporting trial (NCT01967225) is a Phase 3 MRSA skin/soft-tissue infection study — i.e., evidence for tedizolid's **already-known** antibacterial indication, not a distinct new disease area. The reviewer-assigned relevance grade for this trial is "C" (low), explicitly noting the disease term likely reflects an ontology mapping error rather than a true signal.

Notably, the closely related candidate "post-bacterial disorder" (rank 2) has much stronger evidence (9 trials, L1), but all 9 trials are tedizolid's pivotal ABSSSI and VABP development trials — confirming that these top-ranked "predictions" are largely the model re-identifying tedizolid's existing antibacterial profile rather than surfacing a genuine repurposing opportunity. This substantially lowers confidence in the mechanistic novelty of the top-ranked indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01967225](https://clinicaltrials.gov/study/NCT01967225) | Phase 3 | Completed | 125 | Randomized, open-label, active-controlled study of tedizolid (BAY 1192631) in Japanese patients with MRSA skin/soft-tissue infection and related bacteremia — relevance to "post-infectious syndrome" graded low (C), likely ontology mismatch |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Tedizolid phosphate has no registered product license in Singapore (0 total registrations); no market authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction is supported by a single trial with low relevance confidence, and the broader evidence set (including the closely related rank-2 candidate) suggests the model is re-detecting tedizolid's known antibacterial indication rather than identifying a genuinely new therapeutic use. Combined with missing safety/MOA data, this candidate does not currently meet the bar to advance.

**To proceed, the following is needed:**
- TFDA/HSA product label with warnings and contraindications (Blocking data gap — DG001)
- Confirmed mechanism of action from DrugBank (High-priority data gap — DG002)
- Ontology review to clarify whether "post-infectious syndrome" represents a distinct clinical entity or a mapping artifact of tedizolid's existing ABSSSI indication
- If pursued, independent evidence (trials or literature) not already attributable to the drug's approved antibacterial use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

