---
layout: default
title: Tamsulosin
parent: 僅模型預測 (L5)
nav_order: 945
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

Using the report template to produce the Tamsulosin evidence pack report as specified.

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

> Tamsulosin is a selective alpha-1A adrenergic receptor antagonist conventionally used for benign prostatic hyperplasia (BPH)-related urinary symptoms.
> The TxGNN model's top-ranked prediction suggests possible relevance to **Ambras Type Hypertrichosis Universalis Congenita**, a rare congenital hair-growth disorder,
> but this candidate is supported by **0 clinical trials** and **0 publications**, and the evidence pack itself flags the signal as likely a knowledge-graph artifact rather than a genuine pharmacological relationship.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign Prostatic Hyperplasia (BPH) — inferred from known drug class; no local (Singapore) regulatory license text is available |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed structured mechanism-of-action (MOA) data is flagged as a data gap. Based on the pharmacological context embedded in the evidence pack's own rationale text, Tamsulosin is a selective alpha-1A adrenergic receptor antagonist that relaxes smooth muscle in the prostate and bladder neck — a mechanism used to relieve lower urinary tract symptoms associated with BPH.

There is no known biological pathway connecting alpha-1A adrenergic receptor blockade to hair follicle growth cycles or congenital hypertrichosis. Ambras Type Hypertrichosis Universalis Congenita is caused by a chromosome 8q genomic rearrangement and has no documented relationship to adrenergic receptor signaling. The evidence pack's own repurposing rationale explicitly states that this high TxGNN score is most likely due to indirect clustering noise around "hair-related" nodes in the knowledge graph, rather than a genuine mechanistic inference.

Reviewing the full list of 10 predicted indications for this drug reinforces this conclusion: 7 of 10 candidates have zero supporting clinical trials or literature, several (e.g., Dandy-Walker malformation, periodontal malformation syndrome, isolated hair shaft abnormality) are developmentally or anatomically unrelated to adrenergic receptor pharmacology, and even the literature that was retrieved for candidates like "periodontal malformation syndrome" and "alopecia" does not mention Tamsulosin at all — it was linked purely through co-occurring clinical context (e.g., studies on finasteride, a different drug class also used in BPH-adjacent care). This pattern is consistent with embedding-similarity noise rather than a validated repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Tamsulosin currently has no registered product license under this evidence pack (`total_licenses: 0`, `market_status: 未上市 / Not Marketed`). No authorization records are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack; no drug interaction records were found.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication has no supporting clinical trials or literature, no plausible mechanistic link, and is explicitly characterized in the evidence pack's own rationale as likely knowledge-graph noise. None of the 10 predicted indications for Tamsulosin reach even L3 evidence strength with a genuine drug-specific mechanistic or clinical basis; the closest exception (rank 9, "alopecia," L4) is supported only by literature discussing a different drug (finasteride) in an adjacent clinical context, not Tamsulosin itself.

**To proceed, the following is needed:**
- Structured original MOA and indication data (currently data gaps, marked Blocking/High severity in the evidence pack)
- TFDA/regulatory label data (warnings, contraindications) before any safety pre-screening (S1) can begin
- Independent pharmacological or preclinical evidence directly implicating Tamsulosin (not adjacent drugs) in hair-growth or dermatologic pathways, if this candidate is to be reconsidered
- Re-scoring or filtering of TxGNN outputs to down-weight likely embedding-noise candidates before advancing any indication in this list past S0
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

