---
layout: default
title: Mebeverine
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 10
---

# Mebeverine
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

# Mebeverine: From Intestinal Smooth-Muscle Spasm to Cauda Equina Syndrome

## One-Sentence Summary

> Mebeverine is referenced throughout this evidence pack as a peripherally-acting intestinal smooth-muscle relaxant (antispasmodic), though no formal original-indication or mechanism-of-action record is present in this pack, and the drug is not currently registered in Singapore.
> TxGNN's top-ranked prediction is **Cauda Equina Syndrome** (score **98.01%**), but the model's own rationale flags this as the weakest mechanistically-supported candidate of the 10 outputs — likely a knowledge-graph embedding artifact — with **zero supporting clinical trials or literature**.
> Given **L5 evidence** (prediction-only) and an explicit internal **Hold** recommendation, this candidate does not currently support further development.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented in this evidence pack (Mebeverine is not registered in Singapore, no license record). Rationale text across multiple predictions consistently characterizes it as a peripherally-acting intestinal smooth-muscle relaxant (antispasmodic) |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 98.01% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Mebeverine (DrugBank ID DB12554) is not available in this evidence pack, and no original indication is on record for Singapore since the drug is not currently registered there. Based on the pharmacological classification referenced repeatedly across the TxGNN rationale entries, Mebeverine is a peripherally-acting intestinal/gastrointestinal smooth-muscle relaxant, functioning via sodium-channel blockade to reduce smooth-muscle tone — a class most established for functional GI spasm-type conditions.

The mechanistic link to the top-ranked prediction, however, is explicitly flagged as weak by the evidence pack's own analysis. Cauda equina syndrome is a neurosurgical emergency caused by structural nerve-root compression (leading to bladder/bowel sphincter dysfunction), not a pharmacologically reversible smooth-muscle disorder. Mebeverine has no known neuroprotective or nerve-decompression mechanism. The pack's rationale explicitly attributes this top TxGNN score (0.98, rank 16995) to a likely **false-positive association in the knowledge-graph embedding space** — plausibly arising through a shared "bladder/bowel dysfunction" node connecting the two conditions rather than genuine shared pharmacology.

For context, among the 10 candidates in this pack, gastroduodenitis (rank 8, score 81.1%) is flagged internally as the mechanistically strongest candidate — Mebeverine's antispasmodic action could plausibly extend to gastroduodenal smooth muscle — and it is the only candidate with any supporting literature (one Tier-3 review, PMID 19334485). That signal is weak on its own (L4, single review, "Research Question" stage) but is comparatively better grounded than the top-ranked cauda equina syndrome prediction and may warrant attention in future evidence cycles.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Mebeverine is not currently registered in Singapore — `taiwan_regulatory.total_licenses = 0`, no license records exist in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA-equivalent labeling warnings/contraindications for Mebeverine are recorded as a **Blocking** data gap (DG001) in this evidence pack, meaning a formal S1 safety screen cannot yet be completed. Drug-interaction lookup also returned `not_found` (0 interactions on record), which reflects a data gap rather than a confirmed absence of interactions.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The highest-ranked prediction, Cauda Equina Syndrome, has no supporting clinical trials or literature and is explicitly flagged by the model's own rationale as a likely knowledge-graph artifact rather than a mechanistically plausible repurposing signal (L5, decision stage S0). Combined with a Blocking data gap on safety labeling (DG001) and a High-severity gap on mechanism of action (DG002), there is currently no basis to advance this candidate.

**To proceed, the following is needed:**
- TFDA-equivalent package-insert warnings and contraindications (resolves Blocking gap DG001, required before any S1 safety screen)
- Confirmed mechanism-of-action data via DrugBank or equivalent source (resolves High-severity gap DG002)
- Confirmation of Mebeverine's original approved indication(s), since no license or indication record exists for Singapore in this pack
- If gastroduodenitis (rank 8) is pursued as an alternative signal: additional literature and clinical-trial searches to move beyond a single Tier-3 review
- A completed DDI screen, since the current query returned `not_found` rather than a confirmed negative result
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

