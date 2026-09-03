---
layout: default
title: Sodium Acetate
parent: 僅模型預測 (L5)
nav_order: 906
evidence_level: L5
indication_count: 10
---

# Sodium Acetate
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

# Sodium Acetate: From Electrolyte Replacement to Congenital Prothrombin Deficiency

## One-Sentence Summary

> Sodium acetate is a source of acetate ions, pharmacologically used as an electrolyte replenisher / alkalinizing agent (acetate is metabolized to bicarbonate); no specific indication text is on file for this evidence pack.
> The TxGNN model's top-ranked prediction is **Congenital Prothrombin Deficiency**,
> but currently **0 clinical trials** and **0 publications** support this specific prediction, and no plausible mechanistic link has been identified.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Electrolyte replenisher / alkalinizing agent (no approved indication text on file; drug not marketed in Singapore) |
| Predicted New Indication | Congenital Prothrombin Deficiency |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for sodium acetate is not available (data gap). Based on general pharmacological knowledge, sodium acetate is an electrolyte/acid-base buffering agent — the acetate anion is metabolized to bicarbonate, and it is typically used as a component of IV fluids or as an alkalinizing/electrolyte-replacement agent rather than for a disease-specific therapeutic indication.

For the top-ranked prediction, **congenital prothrombin deficiency**, the evidence pack itself states there is no identifiable mechanistic link: this is a genetic coagulation factor disorder, and sodium acetate has no known pathway connecting it to prothrombin synthesis or function. The high TxGNN score therefore appears to reflect a graph-embedding association rather than a biologically grounded hypothesis, and no clinical trials or literature exist to support it.

It is worth noting that lower-ranked candidates in this same prediction set — such as dyspepsia (rank 7) and gastroparesis (rank 9) — have a more plausible (though still indirect) mechanistic rationale, since acetate is a short-chain fatty acid (SCFA) known to interact with SCFA receptors and vagal pathways affecting gastric emptying and gut motility. However, even for these, no study has directly tested sodium acetate itself against the disease, and the rank-1 prediction discussed here remains the least mechanistically supported of the set.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Sodium acetate currently holds **no marketing authorization in Singapore** (0 registrations on file); the product is not marketed in this jurisdiction. No approved indication text is therefore available for cross-reference.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are currently unavailable — this is flagged as a **Blocking** data gap in the underlying evidence pack, meaning a formal safety pre-assessment (S1) cannot proceed until the local product label is retrieved.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (congenital prothrombin deficiency) has a TxGNN score of 99.98% but zero supporting clinical trials, zero literature, and no identifiable mechanistic rationale — this is an L5, model-only prediction. Combined with the drug's non-marketed status in Singapore and a blocking gap in safety/label data, there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- Retrieve sodium acetate's package insert / warnings and contraindications (blocking gap, DG001)
- Obtain confirmed mechanism of action data via DrugBank (DG002)
- If pursuing repurposing, prioritize candidates with at least indirect mechanistic and literature support (e.g., dyspepsia, gastroparesis) over the current top-ranked, evidence-free prediction
- Any further evaluation of congenital prothrombin deficiency would require de novo preclinical or mechanistic studies, as none currently exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

