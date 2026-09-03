---
layout: default
title: Proline
parent: 僅模型預測 (L5)
nav_order: 822
evidence_level: L5
indication_count: 10
---

# Proline
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

# Proline: From No Registered Indication to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Proline is a non-essential amino acid with no registered therapeutic indication in Singapore and no market presence in this evidence pack.
> The TxGNN model predicts a possible link to **Congenital Prothrombin Deficiency**,
> but this prediction is currently supported by **0 clinical trials** and **0 publications** — evidence level L5 (prediction only, no supporting studies).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore registration exists; Proline appears in this dataset as a biochemical/amino-acid entity rather than a registered drug product |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 98.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Proline, and no original therapeutic indication is on record in this evidence pack. Proline is a non-essential amino acid involved in collagen synthesis and general protein metabolism; it does not have an established pharmacological role in coagulation.

The evidence pack's own mechanistic assessment is explicit that this prediction lacks biological plausibility: *"Proline has no known causal mechanism linking it to prothrombin production. The high TxGNN score likely reflects an indirect knowledge-graph connection between amino acid metabolism nodes and coagulation-related genes, rather than a direct pharmacological relationship."* No clinical or literature evidence exists to support the connection.

This pattern is consistent across the full candidate list — 9 of the 10 predicted indications for Proline (vitamin D deficiency, Paget's disease of bone, hypophosphatemic rickets, biotin metabolic disease, folic acid deficiency anemia, familial hypoparathyroidism, etc.) show the same characteristic: high TxGNN scores driven by proline appearing incidentally as a metabolic biomarker or urinary breakdown product (e.g., hydroxyproline in bone turnover, glycyl-prolinuria in renal tubular disorders) rather than as a therapeutic intervention. Only "dyspepsia" (rank 4) and "vitamin deficiency disorder" (rank 5) show marginally more direct evidence (L4), but even there the relevant literature treats proline as a metabolomic marker, not a treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Proline has no registered product license in Singapore (total registrations: 0; market status: Not Marketed). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data are currently available for Proline in this evidence pack, and no TFDA/HSA-approved labelling exists given its unregistered status.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Congenital Prothrombin Deficiency) has no clinical trial or literature support and evidence level L5 — the evidence pack itself flags the association as a likely knowledge-graph artifact rather than a genuine pharmacological signal. Across all 10 predicted indications reviewed, none reach a decision stage beyond S0, and all carry a "Hold" recommendation. Proline is also not marketed in Singapore and has no established mechanism of action, so there is no basis to advance this candidate.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data for Proline (currently a blocking data gap, DG002)
- TFDA/HSA package insert warnings and contraindications (currently a blocking data gap, DG001) — required before any S1 safety review
- Direct pharmacological or clinical evidence testing Proline as an intervention (not merely as a metabolic biomarker) for any of the 10 predicted indications
- If pursuing the higher-evidence candidates (dyspepsia, vitamin deficiency disorder), clarification of whether Proline was the actual tested intervention in the cited trials, as current titles/abstracts do not confirm this
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

