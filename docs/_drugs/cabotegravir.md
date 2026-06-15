---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Cabotegravir
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

# Cabotegravir: From HIV Infection to Rheumatoid Arthritis

## One-Sentence Summary

Cabotegravir (CAB) is an integrase strand transfer inhibitor (INSTI) approved for HIV-1 treatment and pre-exposure prophylaxis (PrEP), available as a long-acting injectable formulation.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis**, with **0 clinical trials** and **0 publications** currently supporting this direction.
This prediction is classified as model-only (L5) and is considered highly speculative at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection treatment and pre-exposure prophylaxis (PrEP) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the data pack. Based on known pharmacological information, Cabotegravir is an integrase strand transfer inhibitor (INSTI) — it works by binding to and blocking HIV integrase, the viral enzyme responsible for inserting viral DNA into the host cell genome. The cellular cofactor LEDGF/p75, which HIV exploits for nuclear targeting, is also known to interact with certain host transcriptional pathways.

The proposed mechanistic link to rheumatoid arthritis (RA) is highly speculative: LEDGF/p75 has been associated with stress-response gene regulation, and there are indirect hypotheses that INSTI-mediated interference with this cofactor could modulate NF-κB-related inflammatory signalling — a pathway central to RA pathogenesis. Additionally, some observational data from HIV patients on antiretroviral therapy (ART) have noted improvement in inflammatory arthropathy symptoms, though this has not been specifically attributed to CAB.

However, no direct mechanistic studies, animal models, or clinical investigations have tested Cabotegravir specifically in RA. The mechanistic link remains at the level of biological conjecture. The TxGNN high score likely reflects graph-proximity between HIV-related immune nodes and autoimmune disease nodes in the knowledge graph, rather than a genuine treatment signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Cabotegravir is currently not registered in Singapore. No product authorisations on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for reviewers:** Cabotegravir is known from post-marketing experience to carry a risk of mild hepatotoxicity (cholestatic injury cases reported). INSTI class agents including CAB are also associated with metabolic effects such as weight gain and insulin resistance, which would be relevant considerations if any future RA indication were explored.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature evidence supporting Cabotegravir's use in rheumatoid arthritis. The TxGNN prediction is based entirely on knowledge graph topology, and the mechanistic link between HIV integrase inhibition and RA pathophysiology is highly speculative with no experimental validation.

**To proceed, the following is needed:**

- **Mechanism of action clarification**: Retrieve formal DrugBank MOA data to assess whether any downstream target of CAB (e.g., LEDGF/p75-NF-κB axis) has a plausible validated role in RA
- **Preclinical evidence**: In vitro or animal model data demonstrating any anti-inflammatory effect of CAB on RA-relevant pathways (e.g., TNF-α, IL-6, synovial fibroblast activity)
- **Comparative INSTI review**: Evaluate whether other INSTI agents (dolutegravir, bictegravir) show any signals in inflammatory arthritis, to support or refute class-level extrapolation
- **Safety data gap resolution**: Obtain TFDA/FDA prescribing information to assess hepatotoxicity and metabolic risk in potential RA patient populations (who may already have liver or metabolic comorbidities)
- **Singapore regulatory pathway**: CAB is not marketed in Singapore; any repurposing programme would need to address regulatory registration strategy from the ground up
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

