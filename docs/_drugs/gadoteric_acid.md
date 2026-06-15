---
layout: default
title: Gadoteric Acid
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Gadoteric Acid
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

# Gadoteric Acid: From MRI Contrast Agent to Osteoarthritis

## One-Sentence Summary

Gadoteric acid (Gd-DOTA) is a macrocyclic gadolinium-based MRI contrast agent used intravenously to enhance magnetic resonance imaging in various diagnostic contexts.
The TxGNN model predicts it may be effective for **Osteoarthritis**, however this prediction is most likely a **diagnostic co-occurrence false signal** — the drug is widely used to image osteoarthritic joints (via the dGEMRIC technique), and the model may have learned this diagnostic association as a therapeutic one.
There are currently **0 clinical trials** and **0 publications** supporting a therapeutic role in osteoarthritis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | MRI contrast enhancement (no Singapore regulatory data available) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 98.57% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on well-established knowledge, Gadoteric acid (brand name: Dotarem) is a macrocyclic, ionic, gadolinium-chelate contrast agent. It functions by shortening the T1 relaxation time of protons in surrounding tissues, thereby enhancing signal intensity on T1-weighted MRI sequences. It has no known pharmacodynamic effect on any tissue — it is purely a diagnostic tool.

The link between gadoteric acid and osteoarthritis almost certainly reflects a **diagnostic co-occurrence artefact**. Gd-DOTA is used in the dGEMRIC (delayed Gadolinium-Enhanced MRI of Cartilage) technique to evaluate glycosaminoglycan content in articular cartilage, enabling non-invasive assessment of osteoarthritic joint damage. The TxGNN knowledge graph contains associations between Gd-DOTA and osteoarthritis because the agent is used *to diagnose and monitor* the disease — not to treat it.

This same pattern recurs across all top-10 predictions in this Evidence Pack: the drug appears alongside musculoskeletal diseases (osteoarthritis, rheumatoid arthritis, gout, skeletal dysplasias) in the medical literature and clinical databases exclusively in a diagnostic imaging context. There is no known mechanism by which an extracellular gadolinium chelate could modify disease biology in any of these conditions. The prediction score reflects diagnostic co-occurrence, not therapeutic potential.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for the osteoarthritis indication.

> **Note on rank-3 indication (Rheumatoid Arthritis):** Two publications were retrieved — [PMID 1727317](https://pubmed.ncbi.nlm.nih.gov/1727317/) (Radiology, 1992) and [PMID 2115261](https://pubmed.ncbi.nlm.nih.gov/2115261/) (AJR, 1990) — both classified as **Diagnostic Imaging Studies**. They document Gd-DOTA uptake in inflamed synovium as a marker of disease activity, not as a treatment. These publications reinforce rather than contradict the false-signal interpretation.

---

## Singapore Market Information

Gadoteric acid is **not registered** in Singapore. No product authorisations are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Specific caution flagged by the Evidence Pack:** For the hepatic porphyria prediction (rank 5), the mechanistic rationale notes that heavy metal chelates may potentially trigger a porphyric crisis. While this is not directly relevant to the top osteoarthritis prediction, it should be documented as a background safety signal if any exploratory use is ever considered.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 TxGNN-predicted indications for gadoteric acid share the same fundamental problem: the drug is a passive diagnostic contrast agent with no pharmacodynamic activity on disease biology. The high prediction scores (98.57%–97.38% across all ranks) represent a systematic **diagnostic co-occurrence false signal** — the model has learned that gadolinium MRI is used alongside these diseases, and incorrectly interpreted this as a therapeutic relationship. No clinical trials or supportive therapeutic literature exist for any predicted indication.

**To proceed, the following is needed:**
- **Do not pursue further repurposing evaluation** without a credible mechanistic hypothesis that is independent of diagnostic imaging use
- Conduct a formal false-positive signal review: confirm whether the TxGNN knowledge graph encodes diagnostic imaging relationships separately from therapeutic relationships; if not, all gadolinium-based contrast agents in the dataset should be flagged as a class
- If MRI-guided drug delivery applications are of interest (a genuinely distinct research area), a separate evidence pack with focused literature search on theranostic gadolinium platforms would be required — this is a different question from standard repurposing
- Singapore regulatory pathway is moot at this stage given zero market presence and no therapeutic evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

