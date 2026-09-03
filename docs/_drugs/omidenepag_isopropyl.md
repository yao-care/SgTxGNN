---
layout: default
title: Omidenepag Isopropyl
parent: 僅模型預測 (L5)
nav_order: 733
evidence_level: L5
indication_count: 10
---

# Omidenepag Isopropyl
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

# Omidenepag Isopropyl: From Ocular Hypertension (EP2 Agonism) to Pancreatitis

## Summary

Omidenepag isopropyl (DrugBank DB15071) is not formally documented with an original indication in the current evidence pack, but internal rationale notes describe it as a selective EP2 (prostaglandin E2 receptor) agonist used as an intraocular-pressure-lowering ophthalmic drug. The TxGNN model's top prediction is **Pancreatitis**, with a prediction score of **99.76%**, but this is currently supported by **zero clinical trials** and **zero publications** — the connection is a pure knowledge-graph embedding similarity with no known biological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded (data gap); mechanistic notes describe the drug as an EP2 receptor agonist for intraocular pressure lowering |
| Predicted New Indication | Pancreatitis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 (model prediction only, no supporting trials or literature) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Omidenepag isopropyl is not available from DrugBank in this evidence pack (flagged as a High-severity data gap). Based on information embedded in the prediction rationale, the drug is a selective EP2 (prostaglandin E2 receptor) agonist, developed as an ophthalmic agent to lower intraocular pressure — consistent with its known clinical use in glaucoma/ocular hypertension management.

There is no established pharmacological or biological pathway linking EP2 receptor agonism to pancreatitis. The evidence pack itself states explicitly that "EP2 receptor activation has no known direct relationship to inflammatory pathways of the pancreas, and this connection derives only from TxGNN knowledge-graph embedding similarity, lacking mechanistic plausibility." This prediction should therefore be treated as a hypothesis-generating signal only, not a mechanistically grounded candidate.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Omidenepag isopropyl currently has no product registration in Singapore (0 licenses on record); market status is "Not Marketed."

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: key warnings, contraindications, and drug-drug interaction data are all currently unavailable — DDI query returned no results, and TFDA/HSA label data is flagged as a Blocking data gap in the evidence pack.)*

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a purely computational (L5) prediction with no corroborating clinical trials, literature, or plausible mechanistic link between EP2 receptor agonism and pancreatitis. The drug also lacks confirmed MOA data, is unmarketed in Singapore, and has no available safety profile — insufficient basis to advance past initial screening.

**To proceed, the following is needed:**
- Confirmed mechanism of action from DrugBank API (currently a High-severity data gap)
- Regulatory label data — warnings/contraindications (currently a Blocking data gap preventing safety pre-screening)
- Preclinical or mechanistic evidence connecting EP2 agonism to pancreatic inflammatory pathways
- Independent literature/clinical trial search to confirm the absence of supporting evidence is not a search-coverage artifact

*Note: this evidence pack lists 9 additional predicted indications (all L5, all Hold) for this drug, including hyperphosphatemia, esophageal varices, blepharospasm, and others — none currently have supporting clinical or literature evidence either.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

