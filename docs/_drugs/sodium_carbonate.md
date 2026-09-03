---
layout: default
title: Sodium Carbonate
parent: 僅模型預測 (L5)
nav_order: 909
evidence_level: L5
indication_count: 10
---

# Sodium Carbonate
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

# Sodium Carbonate: From No Approved Indication to Cauda Equina Syndrome

## One-Sentence Summary

Sodium carbonate (DrugBank DB09460) is not currently marketed in Singapore and has no documented approved indication.
The TxGNN model predicts a possible association with **Cauda Equina Syndrome** (rank 1, score 99.80%),
but this candidate is currently supported by **zero clinical trials** and **zero publications**, and the compound's own mechanism of action is unknown — this is a purely computational signal, not a clinically grounded hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — sodium carbonate is not marketed in Singapore and has no approved indication on record |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism of action (MOA) data for sodium carbonate is not currently available, and the compound has no documented approved indication in Singapore — it is not on the market here, so there is no established clinical use to compare against the predicted new indication. Without either an MOA or a reference indication, there is no pharmacological basis on which to judge biological plausibility for this prediction.

The evidence pack's own rationale for this candidate is explicit on this point: there is no clinical trial or literature evidence, and sodium carbonate's original MOA is missing because it is an unmarketed compound — the association with Cauda Equina Syndrome is purely an artifact of the TxGNN algorithm's scoring, with no assessable biological plausibility. This candidate should be treated as a hypothesis-generating signal only.

It is also worth noting that across all 10 TxGNN-predicted indications for this drug in the current evidence pack (including anaphylaxis, dry eye syndrome, and Sjögren syndrome), evidence quality tops out at L4 — and even those L4 "hits" are single, tangentially related studies (e.g., a sodium bicarbonate/xylitol oral spray study, and an epinephrine sublingual-formulation stability study) rather than direct evidence of therapeutic efficacy. No candidate in this batch reaches a recommendation stronger than Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Safety data specific to this compound and indication is not currently available. As sodium carbonate is not registered or marketed in Singapore, no local package insert exists for reference, and no drug-drug interaction data was found in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Cauda Equina Syndrome) has an L5 evidence level — a TxGNN score with no supporting clinical trials, literature, or known mechanism of action. Combined with the drug's unmarketed status in Singapore and missing MOA data, there is currently no basis to advance this candidate beyond algorithmic screening.

**To proceed, the following is needed:**
- MOA data for sodium carbonate (DrugBank API query, flagged as DG002/High severity)
- Confirmation of any regulatory approval/label in other jurisdictions, since none exists in Singapore
- Targeted literature search specifically on sodium carbonate (as opposed to sodium bicarbonate, which appears in several retrieved but likely mismatched records) in the context of Cauda Equina Syndrome
- If no direct evidence emerges, consider deprioritizing this candidate in favor of the other predicted indications in this batch (e.g., anaphylaxis, Sjögren syndrome) that at least have L4-level, if weak, supporting literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

