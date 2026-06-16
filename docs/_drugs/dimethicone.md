---
layout: default
title: Dimethicone
parent: 僅模型預測 (L5)
nav_order: 329
evidence_level: L5
indication_count: 10
---

# Dimethicone
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

# Dimethicone: From Skin Protectant / Antifoaming Agent to Insomnia

## One-Sentence Summary

Dimethicone (DB11074) is an inert silicone polymer widely used as a topical skin barrier protectant and gastrointestinal antifoaming agent; no approved therapeutic indication is documented in the Singapore regulatory database.
The TxGNN model predicts it may be effective for **Insomnia**, with a prediction score of **94.35%** —
however, **no supporting clinical trials or literature** for this indication exist, and the mechanistic rationale is absent. This prediction is assessed as a likely knowledge-graph artifact rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No approved indication on record (Singapore: not marketed) |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 94.35% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Dimethicone (DB11074). Based on known pharmaceutical information, Dimethicone is a polydimethylsiloxane (PDMS) silicone polymer that functions as a **physical barrier agent and antifoaming agent**. It is chemically inert and pharmacologically passive — it does not bind to receptors, inhibit enzymes, or modulate signalling pathways in any known therapeutic sense.

Insomnia involves complex central neurological pathways including GABAergic signalling, adenosine receptor modulation, and the melatonin circadian system. Dimethicone has no known intersection with any of these pathways. The high TxGNN score (94.35%) is most likely attributable to an indirect knowledge-graph traversal artifact — a plausible but biologically unsupported path such as "skin barrier → comfort → sleep quality" — rather than a direct pharmacological mechanism.

The one clinical trial retrieved (NCT04872946) assessed skin health and inner wellness using a topical/oral skin care regimen that included Dimethicone as a formulation excipient. This trial has no relevance to insomnia as a primary indication and does not constitute evidence of therapeutic activity against sleep disorders.

---

## Clinical Trial Evidence

> ⚠️ The single trial retrieved is rated **Grade C (not relevant)** — Dimethicone was used as a topical cosmetic/skin care ingredient, and insomnia was not a study endpoint.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04872946](https://clinicaltrials.gov/study/NCT04872946) | NA | Completed | 74 | Assessed oral + topical skin care regimen (Inner Calm + Super Calm) for skin redness and sensitivity. No insomnia endpoints. Dimethicone appears as a formulation component, not as an active drug for sleep disorders. **Not supportive evidence.** |

---

## Literature Evidence

Currently no related literature available for Dimethicone in the treatment of insomnia.

---

## Singapore Market Information

Dimethicone (DB11074) has **no registered products** in Singapore. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction data, key warnings, or contraindication records were retrieved from available databases for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for Dimethicone are rated L5 (model prediction only, no clinical or preclinical evidence). The top-ranked indication — insomnia — lacks any mechanistic plausibility: Dimethicone is a chemically inert silicone polymer with no known neuroactive properties. The single clinical trial retrieved is entirely unrelated to sleep disorders. The TxGNN scores across all 10 candidates (insomnia and multiple cataract subtypes) are consistent with knowledge-graph clustering artifacts rather than true biological signals.

**To proceed, the following would be needed:**

- Identification of a credible pharmacological mechanism linking Dimethicone to sleep regulation (e.g., preclinical receptor binding data, in vitro CNS activity)
- Retrieval and review of TFDA/HSA package insert warnings and contraindications (currently a blocking data gap)
- MOA data from DrugBank API (currently missing)
- At minimum one hypothesis-generating preclinical study before any clinical translation could be considered
- Re-evaluation of whether the TxGNN graph scoring is driven by formulation co-occurrence (Dimethicone as excipient in products containing active sleep aids) rather than intrinsic pharmacological activity of Dimethicone itself
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

