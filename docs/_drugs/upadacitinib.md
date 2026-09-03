---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 1032
evidence_level: L5
indication_count: 10
---

# Upadacitinib
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

# Upadacitinib: From JAK1-Mediated Inflammatory Disease to Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome

## One-Sentence Summary

> Upadacitinib is a JAK1 inhibitor used for immune-mediated inflammatory diseases (structured original-indication data is a gap in this evidence pack, but the model's own rationale notes reference its approved use in axial spondyloarthritis). The TxGNN model's top-ranked prediction, **Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome**, is supported by **0 clinical trials** and **0 publications** — and the model's own annotation explicitly flags this as a likely false positive from knowledge-graph embedding similarity rather than genuine biological plausibility.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (drug is a known JAK1 inhibitor; TFDA label data pending — see Data Gap DG001/DG002) |
| Predicted New Indication | Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available as a structured field in this evidence pack. Based on information embedded directly in the prediction rationales, upadacitinib is a JAK1 inhibitor used to treat immune-mediated inflammatory conditions — the rationale for a lower-ranked candidate (axial spondylometaphyseal dysplasia, rank 10) explicitly references upadacitinib's approved indication of "axial spondyloarthritis," suggesting the drug's known therapeutic domain is autoimmune/inflammatory disease via JAK-STAT pathway modulation.

The top-ranked prediction, however, is a congenital syndrome combining colobomatous microphthalmia (an eye development anomaly) with rhizomelic skeletal dysplasia — a genetic developmental disorder with no known link to JAK1 signaling or immune-inflammatory pathophysiology. The model's own rationale states this directly: *"高度懷疑為知識圖譜嵌入相似性造成之偽陽性預測"* (highly suspected to be a false positive caused by knowledge-graph embedding similarity). This is corroborated by rank 2 (brachydactyly-syndactyly syndrome, also a skeletal dysplasia flagged as likely KG noise) and rank 10 (axial spondylometaphyseal dysplasia, flagged as probable ontology-label confusion with "axial spondyloarthritis").

Notably, among the 10 candidates in this evidence pack, only the plasma cell myeloma-related predictions (ranks 3 and 7) and the ALS-related predictions (ranks 4, 6, 8, 9) carry any stated mechanistic rationale (IL-6/JAK1-STAT3 signaling in myeloma; neuroinflammatory JAK-STAT activation in ALS) — but even these are explicitly described as theoretical, with **no direct clinical or preclinical data** supporting upadacitinib's use in any of the 10 indications. This case illustrates a common TxGNN failure mode: high embedding-similarity scores driven by disease-name or ontology proximity rather than shared pathophysiology.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Upadacitinib is not currently registered under the tracked regulatory data for this jurisdiction — market status is "Not Marketed" with 0 licenses on file. No product/dosage-form details are available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are currently unavailable — TFDA label parsing is flagged as a **Blocking** data gap, DG001.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has a high TxGNN score (99.61%) but zero clinical or literature evidence, and the model's own rationale explicitly flags it as a likely false positive driven by knowledge-graph embedding artifacts rather than plausible biology. The drug is also unregistered in this jurisdiction, and safety/MOA data are both marked as unresolved data gaps (one Blocking).

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain and parse the TFDA package insert for warnings/contraindications before any S1 safety screening
- Resolve DG002: confirm mechanism of action via DrugBank API to validate/invalidate the mechanistic plausibility of each candidate
- Independent expert review of ontology labels for ranks 1, 2, and 10 to rule out disease-name/embedding confusion before further model-based prioritization
- If pursuing repurposing signal further, prioritize the myeloma (ranks 3, 7) or ALS (ranks 4, 6, 8, 9) candidates instead, as these at least carry a stated (if unproven) IL-6/JAK-STAT mechanistic hypothesis — though none currently meet the evidence bar to exit Hold status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

