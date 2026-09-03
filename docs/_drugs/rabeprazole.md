---
layout: default
title: Rabeprazole
parent: 僅模型預測 (L5)
nav_order: 837
evidence_level: L5
indication_count: 10
---

# Rabeprazole
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

# Rabeprazole: From Acid-Peptic Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

> Rabeprazole is a proton pump inhibitor whose established use — based on literature within this evidence pack — is acid-peptic disease (duodenal/gastric ulcer, GERD, *H. pylori* eradication); formal TFDA-equivalent labeling data is currently missing (Blocking Data Gap).
> The TxGNN model's top-ranked prediction is **Smouldering Systemic Mastocytosis**,
> but this candidate is supported by **0 clinical trials** and **0 publications** — it is a pure graph-neural-network association with no identified mechanistic basis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured regulatory data (Blocking Data Gap DG001). Literature in this pack confirms rabeprazole as a PPI for acid-peptic disease (duodenal/gastric ulcer, GERD, *H. pylori* eradication), but no formal approved-indication text was retrieved. |
| Predicted New Indication | Smouldering Systemic Mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data is not available (High-severity Data Gap DG002). Based on the literature evidence contained in this pack, rabeprazole is a proton pump inhibitor that irreversibly inhibits gastric H+/K+-ATPase, reducing acid secretion — a mechanism well established for acid-peptic disease.

For the top-ranked predicted indication, **Smouldering Systemic Mastocytosis**, the evidence pack explicitly states: *"無已知機轉連結 PPI 抑酸作用與肥大細胞增生疾病之病理生理"* — there is no known mechanistic link between PPI-mediated acid suppression and mast cell proliferative disease pathophysiology. Despite the very high TxGNN similarity score (99.44%), this association is not corroborated by any clinical trial or publication.

This should be read as a pure knowledge-graph pattern-match rather than a biologically grounded hypothesis. Notably, within the same prediction batch, lower-ranked candidates such as *active peptic ulcer disease* (rank 3) and *gastric ulcer* (rank 9) show much stronger evidence (L1, multiple Phase 2/3 RCTs) — but these largely reflect rabeprazole's already-known pharmacology rather than genuine repurposing opportunities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Rabeprazole currently has no marketing authorization on record in Singapore (0 registrations, market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Smouldering Systemic Mastocytosis) has no clinical trials, no literature, and no established mechanistic link — it sits at Evidence Level L5 (model prediction only). Combined with the drug's unmarketed status in Singapore and missing TFDA-equivalent safety labeling, there is no basis to advance this candidate beyond model output at this time.

**To proceed, the following is needed:**
- TFDA/regulatory labeling data — warnings, contraindications, approved indications (Blocking Data Gap DG001)
- DrugBank mechanism-of-action data (Data Gap DG002)
- Preclinical or mechanistic studies exploring any biological plausibility between PPI acid suppression and mast cell disease pathophysiology
- If pursuing repurposing more broadly, prioritize re-evaluating rank 3/9 candidates (active peptic ulcer disease, gastric ulcer) only after confirming they are not simply the drug's existing approved use rather than true new indications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

