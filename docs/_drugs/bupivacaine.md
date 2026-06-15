---
layout: default
title: Bupivacaine
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Bupivacaine
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

# Bupivacaine: From Local/Regional Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Bupivacaine is a long-acting amide-type local anesthetic widely used for regional anesthesia, epidural analgesia, and perioperative pain management.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans** (a late cutaneous manifestation of Lyme borreliosis),
with **0 clinical trials** and **0 publications** currently supporting this direction — the prediction appears driven by knowledge graph proximity rather than a mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local/regional anesthesia and pain management |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, Bupivacaine is a long-acting amide-class local anesthetic that primarily blocks voltage-gated sodium channels (Nav1.7, Nav1.8), thereby preventing depolarisation and inhibiting nerve impulse conduction. Beyond its anesthetic effect, preclinical studies have reported that bupivacaine may modulate local inflammatory signalling — including suppression of NF-κB activation and reduced release of pro-inflammatory cytokines (TNF-α, IL-6) — at concentrations achievable within injected tissue.

Acrodermatitis chronica atrophicans (ACA) is the late-stage dermatological manifestation of Lyme borreliosis, caused by persistent *Borrelia burgdorferi* infection. The disease is characterised by chronic dermal lymphocytic infiltration, progressive skin atrophy, and collagen loss — driven primarily by ongoing spirochetal infection and the resulting host immune dysregulation, not by a purely inflammatory or channel-mediated process.

The mechanistic link between bupivacaine and ACA is implausible. ACA is fundamentally an infectious disease that responds to antibiotic therapy (doxycycline, amoxicillin); sodium channel blockade has no known role in clearing Borrelia or reversing the associated connective tissue destruction. The TxGNN score of 0.992 almost certainly reflects the model capturing a neighbourhood relationship between generic "skin inflammation" nodes in the knowledge graph — a non-specific signal rather than a genuine therapeutic hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not available in this evidence pack. Retrieval from the Singapore HSA package insert and DrugBank is required before any clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication (acrodermatitis chronica atrophicans) is an antibiotic-responsive infectious disease with no plausible biological connection to bupivacaine's mechanism of action; the evidence level is L5 (model prediction only), and no supporting clinical or preclinical literature exists.

**To proceed, the following is needed:**

- **Safety data gap closure (Blocking):** Retrieve Singapore HSA / Taiwan TFDA package insert warnings and contraindications (DG001) before any further evaluation stage can be entered.
- **MOA data from DrugBank (High):** Complete the DrugBank API query (DG002) to enable proper mechanistic linkage analysis across all predicted indications.
- **Re-prioritise the candidate list:** Among the 10 predictions evaluated, two carry clinically coherent rationales and at least some supporting evidence:
  - **Rank 8 — Epulis / Central Giant Cell Granuloma (L4, Research Question):** Six case-series publications document a specific intralesional protocol combining triamcinolone + bupivacaine for CGCG; bupivacaine serves as both a carrier vehicle and a post-injection analgesic, with one publication (PMID 11862204) explicitly reporting the bupivacaine mixture. This is the most clinically grounded finding in the pack.
  - **Rank 9 — Polyp of Vocal Cord (L4, Research Question):** A Phase 2 RCT (NCT06734975, n=28, recruiting) is formally testing whether bupivacaine superior laryngeal nerve block improves patient outcomes following microdirect laryngoscopy for benign vocal fold lesions. The study design is rigorous; results are pending (expected completion December 2026).
- **Formal evaluation of Ranks 8–9** should be prioritised over Rank 1, as these represent actionable research questions rather than graph artefacts.

---

> *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

