---
layout: default
title: Benzydamine
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Benzydamine
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

# Benzydamine: From Oral Mucosal Inflammation to Benign Prostatic Hyperplasia

## One-Sentence Summary

Benzydamine is a locally-acting non-steroidal anti-inflammatory drug (NSAID) with additional local anaesthetic properties, widely used globally for the management of oral mucositis, pharyngitis, and sore throat — though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Oral mucosal inflammation / sore throat (globally established use; no Singapore registration) |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not currently available. Based on pharmacological information drawn from the evidence pack, Benzydamine acts through at least three mechanisms: (1) weak COX inhibition to reduce prostaglandin-mediated inflammation; (2) sodium ion channel blockade providing local anaesthetic and analgesic effects on mucous membranes; and (3) suppression of pro-inflammatory cytokines (TNF-α, IL-1β) to dampen local inflammatory cascades. Its clinical niche is therefore firmly anchored in *localised* mucosal and soft-tissue inflammation.

BPH is increasingly recognised to have a chronic inflammatory component within the prostatic stroma and periurethral tissue. In theory, systemic or locally-delivered COX inhibition and cytokine suppression could modulate peri-prostatic inflammation and slow symptom progression. This provides a plausible, if indirect, mechanistic bridge from Benzydamine's anti-inflammatory profile to BPH pathophysiology.

However, the TxGNN knowledge graph score of 0.9926 almost certainly reflects graph-level path co-clustering — specifically, the proximity of "inflammation" and "prostate tissue" nodes — rather than validated pharmacological activity in prostatic tissue. No preclinical, histological, or clinical research has examined Benzydamine in the context of BPH. The absence of any supporting evidence means this prediction cannot advance beyond the model hypothesis stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Singapore-specific label warnings and contraindications were not available at the time of this report. Drug–drug interaction data was also not identified in this search. These gaps should be resolved before any clinical evaluation proceeds.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.26%) to Benzydamine for BPH, but this is supported by zero clinical trials and zero publications, placing this candidate firmly at Evidence Level L5 — model prediction only. The mechanistic link via peri-prostatic inflammation is biologically plausible in principle but entirely unvalidated, and Benzydamine's primary pharmacological strength lies in *local* mucosal delivery, not systemic anti-inflammatory activity relevant to the prostate.

**To proceed, the following is needed:**

- **MOA data from DrugBank** — confirm whether Benzydamine has any known activity on prostatic tissue targets or systemic androgen-related pathways
- **Singapore label (package insert)** — obtain full warnings and contraindications before any safety evaluation can begin
- **Preclinical feasibility study** — animal or in-vitro BPH models to test whether Benzydamine achieves meaningful prostatic tissue concentrations and anti-inflammatory effect via a systemically deliverable route
- **Route-of-administration assessment** — Benzydamine's established formulations are topical/mucosal; systemic formulations suitable for BPH indications would need to be identified or developed
- **Comparator landscape review** — BPH already has well-established medical therapies (α-blockers, 5α-reductase inhibitors); any repurposing path must define a differentiated value proposition

---

> ⚠️ *This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

