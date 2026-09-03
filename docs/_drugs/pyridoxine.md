---
layout: default
title: Pyridoxine
parent: 僅模型預測 (L5)
nav_order: 835
evidence_level: L5
indication_count: 10
---

# Pyridoxine
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

Using no additional skill — this is a direct content-generation task matching the provided report template; I'll follow it as instructed.

# Pyridoxine: From Vitamin B6 Deficiency/Supplementation to Gonococcal Urethritis

## One-Sentence Summary

> Pyridoxine (Vitamin B6) is a water-soluble vitamin classically used to treat or prevent vitamin B6 deficiency and related conditions (e.g., sideroblastic anemia, isoniazid-induced neuropathy, pyridoxine-dependent seizures).
> The TxGNN model predicts it may be effective for **Gonococcal Urethritis**,
> but currently **0 clinical trials** and **0 publications** support this specific direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in regulatory data (drug not registered in Singapore); commonly used for vitamin B6 deficiency and related metabolic conditions |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 93.87% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available for this evaluation. Based on known pharmacology, pyridoxine functions as a cofactor (via its active form pyridoxal 5'-phosphate) in amino acid, neurotransmitter, and one-carbon metabolism — none of which are known to involve antimicrobial or anti-inflammatory activity against *Neisseria gonorrhoeae*.

There is no established pharmacological, preclinical, or clinical rationale linking vitamin B6 to gonococcal urethritis. The evidence review for this candidate explicitly notes that the high TxGNN score likely reflects an artifact of the knowledge graph: pyridoxine and gonococcal urethritis may share connections through general "urethritis/urinary system" nodes, producing a spuriously high similarity score rather than a genuine mechanistic or clinical relationship.

Given the complete absence of supporting clinical trials or literature, this prediction should be treated as a hypothesis-generation signal only, not as a candidate ready for further clinical evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

This drug currently has no registered product license in Singapore (0 registrations, market status: not marketed). No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or literature evidence supporting pyridoxine's use in gonococcal urethritis, and the underlying mechanistic rationale is assessed as biologically implausible — likely a knowledge-graph artifact from shared "urethritis/urinary" node connections rather than a true pharmacological signal.

**To proceed, the following is needed:**
- TFDA/HSA package insert data (warnings, contraindications) — currently a blocking data gap (DG001)
- Confirmed mechanism of action (MOA) data from DrugBank or primary literature (DG002)
- Preclinical evidence (e.g., in vitro antimicrobial or anti-inflammatory activity against *N. gonorrhoeae*) before any further evaluation is warranted
- Note: among the other TxGNN predictions reviewed for this drug, "vitamin deficiency disorder" (rank 10, score 85.5%) has substantially more supporting literature and trial evidence and a mechanistically coherent rationale, but represents an already-known use rather than a novel repurposing candidate — it is not proposed as a substitute conclusion here, only flagged for context.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

