---
layout: default
title: Peppermint Oil
parent: 僅模型預測 (L5)
nav_order: 769
evidence_level: L5
indication_count: 10
---

# Peppermint Oil
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

# Peppermint Oil: From No Registered Indication to Leprosy

## One-Sentence Summary

Peppermint oil (DrugBank DB11198) has no registered original indication and is not currently marketed in Singapore, so this evaluation starts without an established therapeutic baseline. The TxGNN model's top-ranked prediction is **Leprosy**, with a very high similarity score (99.80%), but **zero clinical trials and zero publications** currently support this specific link — it is a pure knowledge-graph embedding prediction with no mechanistic, clinical, or literature backing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license/registration on file |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for peppermint oil is not available in this evidence pack. Based on the information provided, peppermint oil has no defined original indication and no Singapore market presence, so there is no established pharmacological baseline from which to reason toward leprosy.

Leprosy is caused by *Mycobacterium leprae* infection and is treated with anti-mycobacterial regimens. The evidence pack's own rationale for this prediction states plainly that there is no known mechanistic link between peppermint oil and leprosy: no in vitro or clinical evidence of anti-mycobacterial activity exists for this compound. The high TxGNN score reflects embedding-space similarity within the knowledge graph rather than any biological or pharmacological reasoning, and should be treated as a hypothesis-generation signal only, not as mechanistic support.

Given the complete absence of supporting trials or literature, this prediction currently has no scientific rationale beyond the model's statistical output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/HSA labeling warnings and contraindications for peppermint oil are currently a documented data gap — see Conclusion below.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.80% TxGNN score for leprosy is unsupported by any mechanism, clinical trial, or published literature — it reflects knowledge-graph similarity only (Evidence Level L5). In addition, peppermint oil is not marketed in Singapore and lacks basic regulatory safety documentation, so it cannot yet clear even a preliminary safety screen.

**To proceed, the following is needed:**
- Complete mechanism of action (MOA) data for peppermint oil (currently a data gap)
- TFDA/HSA label warnings and contraindications, required before any preliminary (S1) safety assessment — this is currently a **blocking** data gap
- In vitro or mechanistic evidence for any anti-mycobacterial activity, since none currently exists to support the leprosy hypothesis
- Consider re-prioritizing evaluation toward **cardiovascular disease** (rank 9 in this same prediction set), which already has a materially stronger evidence base: 3 completed clinical trials (n=36–40) and 8 literature records including 1 RCT protocol, reaching Evidence Level L3 / decision stage S2 ("Research Question") — a substantially more actionable candidate than leprosy for this drug.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

