---
layout: default
title: Dicyclomine
parent: 僅模型預測 (L5)
nav_order: 299
evidence_level: L5
indication_count: 10
---

# Dicyclomine
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

# Dicyclomine: From Gastrointestinal Antispasmodic to Cauda Equina Syndrome

## One-Sentence Summary

Dicyclomine (Bentyl) is an anticholinergic antispasmodic agent internationally established for treating irritable bowel syndrome (IBS) and functional gastrointestinal spasm, though it carries no current Singapore registration.
The TxGNN model ranks **Cauda Equina Syndrome** as its top predicted new indication with a score of 99.66%, yet this is supported by **0 clinical trials** and **0 publications**.
Among all 10 ranked predictions, the more mechanistically credible candidates are **neurogenic bladder** (rank 2) and **gastroduodenitis** (rank 7), both of which align better with Dicyclomine's known M3-receptor antagonism; the top-ranked cauda equina prediction is likely a knowledge-graph artefact.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration; internationally known as antispasmodic for IBS and functional GI disorders |
| Predicted New Indication | Cauda Equina Syndrome (Rank 1) |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on known pharmacological information, Dicyclomine (Bentyl) is a muscarinic receptor antagonist (primarily M3) that relaxes smooth muscle in the gastrointestinal tract, reduces secretions, and blunts parasympathetic overactivity. It has been in clinical use since the early 1950s for cramping, IBS, and functional bowel disorders.

Cauda equina syndrome is a neurosurgical emergency caused by compression of the lumbosacral nerve roots, and its definitive management is urgent surgical decompression. There is no established pharmacological pathway by which muscarinic receptor blockade could decompress nerve roots, restore neural conduction, or address the structural pathology underlying this condition. The predicted mechanistic link is therefore extremely weak.

The high TxGNN score (99.66%) most likely reflects shared graph topology — Dicyclomine and cauda equina syndrome nodes are connected through the broader "nervous system" and "autonomic function" neighbourhood in the knowledge graph — rather than genuine pharmacological relevance. Of the 10 ranked predictions in this pack, **neurogenic bladder** (rank 2) is the most pharmacologically credible repurposing target: anticholinergic agents (M3 antagonism → detrusor muscle relaxation) are already a cornerstone of neurogenic bladder treatment. **Gastroduodenitis** (rank 7) and **peptic ulcer disease** (rank 9) are supported by direct early clinical reports of Dicyclomine (Bentyl) use, though these indications have been superseded by H₂ antagonists and PPIs in modern practice.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dicyclomine in Cauda Equina Syndrome.

---

## Literature Evidence

Currently no related literature available for Dicyclomine in Cauda Equina Syndrome.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were not retrievable in this evidence pack. Anticholinergic agents as a class carry well-known risks including urinary retention, tachycardia, constipation, cognitive impairment, and contraindication in angle-closure glaucoma — these should be confirmed from authoritative sources before any clinical consideration.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (cauda equina syndrome) has no mechanistic plausibility and zero supporting evidence; it is almost certainly a knowledge-graph false positive. Dicyclomine is additionally unregistered in Singapore and lacks retrievable MOA and safety data in this pack, making any forward progression premature.

**To proceed, the following is needed:**

- **Retrieve MOA and safety data** — Query DrugBank API (DB00804) for full pharmacology, key warnings, and contraindications; download the original package insert PDF for anticholinergic class warnings
- **Redirect prediction focus** — Shift primary investigation to mechanistically credible indications:
  - **Neurogenic bladder** (rank 2): M3 antagonism directly relaxes the detrusor; this is pharmacologically the strongest repurposing rationale among all 10 predictions
  - **Gastroduodenitis / Peptic ulcer disease** (ranks 7–9): Historical literature (1950–1956) documents direct clinical use of Bentyl; however, modern treatment paradigms (H. pylori eradication + PPI) largely supplant anticholinergic therapy
- **Conduct targeted literature search** for Dicyclomine specifically in neurogenic bladder (MEDLINE, Embase) and benchmark against first-line agents (oxybutynin, solifenacin, tolterodine)
- **Assess regulatory pathway** — Since Singapore currently has no registration, determine whether a new Drug Application or label extension via HSA would be required, and whether there is clinical differentiation over existing marketed anticholinergics
- **Clarify MONDO ontology status** for rank 2 ("obsolete neurogenic bladder") — map to current MONDO/ICD-11 equivalent before designing any study protocol
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

