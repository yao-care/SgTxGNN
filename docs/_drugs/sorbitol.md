---
layout: default
title: Sorbitol
parent: 僅模型預測 (L5)
nav_order: 921
evidence_level: L5
indication_count: 10
---

# Sorbitol
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

# Sorbitol: From Unspecified Original Indication to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

> Sorbitol (DrugBank DB01638) has no documented original indication or mechanism of action in the current dataset, and is not marketed in Singapore.
> The TxGNN model predicts a possible association with **Exercise-Induced Malignant Hyperthermia**,
> but this ranking carries **zero supporting clinical trials and zero supporting literature**, and the evidence pack's own mechanistic review found no identifiable pharmacological rationale for the link.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current dataset (no `original_indications` recorded) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Sorbitol is currently unavailable (flagged as a High-severity data gap, DG002). Sorbitol is generically known as an inert polyol used as an osmotic laxative/diuretic excipient, but no original indication record exists in this dataset to anchor a repurposing rationale.

Critically, the evidence pack's own mechanistic assessment for this top-ranked candidate states there is **no identifiable mechanistic basis**: exercise-induced malignant hyperthermia is driven by ryanodine receptor (RYR1) dysfunction in skeletal muscle, a pathway with no known relationship to sorbitol's pharmacology. The high TxGNN score (99.40%) reflects graph-embedding similarity only, unsupported by any clinical trial or publication. This candidate should be treated as a pure computational signal, not a pharmacologically grounded hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Sorbitol currently has no marketing authorizations registered in Singapore (0 registrations; market status: not marketed). No approved indication text is available to reference.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Exercise-Induced Malignant Hyperthermia) is Evidence Level L5 — a model score with no corroborating trials, literature, or plausible mechanism. Combined with missing MOA and safety data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- MOA data for Sorbitol from DrugBank (currently High-severity data gap, DG002)
- TFDA/HSA package insert warnings and contraindications (currently Blocking data gap, DG001, required before any S1 safety review)
- Confirmed original indication history to establish a baseline pharmacological rationale
- If this specific indication is pursued, independent preclinical mechanistic work, since no supporting evidence currently exists

---

## Additional Observations on Other Candidates in This Evidence Pack

Not part of the top-ranked prediction, but relevant for anyone reviewing the full candidate list:

- **Infectious otitis media (rank 4, L4, S1 "Research Question")** is the only candidate with any indirect supportive signal — an RCT and literature exist for **xylitol** (a related polyol) preventing acute otitis media via anti-adhesion effects on *S. pneumoniae*/*H. influenzae*. This is an analogy from a structurally similar compound, not direct sorbitol evidence, but it is meaningfully stronger than the other nine candidates.
- **Congestive heart failure (rank 3) and Acute pulmonary heart disease (rank 6)** should be treated with caution: nearly all associated trials and literature concern **isosorbide dinitrate/mononitrate** and **hydralazine**, which share only the "isosorbide" root with sorbitol but have an unrelated pharmacology (nitric oxide donor/vasodilator vs. inert osmotic polyol). This strongly suggests an entity-linkage error in the underlying literature/trial search rather than genuine repurposing evidence, and these candidates should not be advanced without independent verification.
- The remaining six candidates (epiglottitis, toxocariasis, middle ear cholesterol granuloma, otosalpingitis, allergic otitis media, familial periodic paralysis) have no supporting evidence at all and are pure model output.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

