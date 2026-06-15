---
layout: default
title: Cisatracurium
parent: 僅模型預測 (L5)
nav_order: 228
evidence_level: L5
indication_count: 10
---

# Cisatracurium
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

# Cisatracurium: From Neuromuscular Blockade to Cauda Equina Syndrome

## One-Sentence Summary

Cisatracurium is a non-depolarizing neuromuscular blocking agent (NMBA) used perioperatively to facilitate tracheal intubation and maintain skeletal muscle relaxation during surgery and mechanical ventilation.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, yet **no clinical trials** and **no publications** currently support this direction.
Despite a near-perfect prediction score (99.99%), evidence is confined to model prediction alone (L5), and mechanistic analysis strongly suggests this is a false positive arising from anesthesia co-occurrence patterns rather than a genuine therapeutic relationship.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neuromuscular blockade: facilitation of tracheal intubation and skeletal muscle relaxation during surgery or mechanical ventilation |
| Predicted New Indication | Cauda Equina Syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacology, Cisatracurium is a benzylisoquinolinium non-depolarizing NMBA that competitively antagonizes nicotinic acetylcholine receptors (nAChR) at the neuromuscular junction, producing reversible skeletal muscle paralysis. Its defining pharmacokinetic advantage is **Hofmann elimination** — a spontaneous, pH- and temperature-dependent degradation pathway that renders drug clearance entirely independent of renal or hepatic function, making it particularly suitable for critically ill patients.

Cauda equina syndrome (CES) is a surgical emergency caused by compression of the lumbosacral nerve roots within the spinal canal — most commonly by a massive disc herniation, tumour, or haematoma. The definitive treatment is urgent surgical decompression. There is no known pharmacological mechanism by which blocking peripheral nAChR at the neuromuscular junction could relieve nerve root compression, reduce intraspinal pressure, or accelerate neurological recovery. Cisatracurium acts exclusively at the skeletal muscle level and does not penetrate the central nervous system.

The TxGNN model's high score in this case most plausibly reflects **statistical co-occurrence** within the knowledge graph: Cisatracurium is routinely administered as an anesthetic adjunct during spinal surgery, including CES decompression procedures. This operational association in surgical settings is not equivalent to a therapeutic relationship. The prediction is assessed as a probable false positive, and the mechanistic rationale does not support repurposing in this indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert warnings, contraindications, and drug interaction data were not available at the time of this report. Retrieval from the relevant regulatory authority (e.g., FDA, EMA label for Nimbex®) is recommended before any clinical decision is made.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN prediction score is near-perfect (99.99%), the mechanistic analysis does not support repurposing of Cisatracurium for Cauda Equina Syndrome — the drug blocks peripheral neuromuscular junctions and has no known capacity to relieve nerve root compression, modulate neuroinflammation, or promote neurological recovery. The high score most likely reflects anesthetic co-occurrence in spinal surgery settings within the knowledge graph, which is a recognised limitation of graph-based prediction models, not a clinically actionable signal.

**To proceed, the following is needed:**

- **MOA data retrieval:** Query DrugBank API for complete mechanism of action and secondary target profile to rule out any unexpected neuroprotective activity
- **Regulatory label review:** Download and parse the FDA/EMA package insert (e.g., Nimbex® label) to complete the safety assessment — currently a blocking data gap
- **Preclinical plausibility screen:** Before any clinical consideration, in vitro or animal model data demonstrating activity in nerve root compression or neuroinflammation models would be required
- **Knowledge graph audit:** Review whether the TxGNN score reflects genuine mechanistic links or anesthesia co-occurrence artefacts — if the latter, this candidate should be formally deprioritised from the repurposing pipeline
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

