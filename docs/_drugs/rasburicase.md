---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 847
evidence_level: L5
indication_count: 10
---

# Rasburicase
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

# Rasburicase: From Hyperuricemia (Tumor Lysis Syndrome) to Renal Hypouricemia

## One-Sentence Summary

Rasburicase is a recombinant urate oxidase, established for managing hyperuricemia associated with tumor lysis syndrome in cancer patients undergoing chemotherapy.
The TxGNN model's top-ranked prediction is **Renal Hypouricemia**, with a score of **99.99%**,
but this is supported by **0 clinical trials** and **0 publications** — and the model's own mechanistic rationale flags this specific prediction as likely direction-reversed.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia / Tumor Lysis Syndrome (based on known pharmacology of urate oxidase enzymes; not present as a formal record in this evidence pack) |
| Predicted New Indication | Renal Hypouricemia (hypouricemia, renal) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, a formally documented mechanism of action is not available in this evidence pack (flagged as a High-severity data gap). Based on the mechanistic notes accompanying the predictions, Rasburicase is described as a recombinant urate oxidase that catalyzes oxidation of uric acid into allantoin, thereby **lowering** serum uric acid — the basis for its established use in hyperuricemia/tumor lysis syndrome.

**This is where the top-ranked prediction breaks down.** Renal hypouricemia is a condition of *abnormally low* uric acid (typically from a renal tubular transport defect, e.g., URAT1 mutation), not high uric acid. A drug whose entire pharmacological purpose is to further reduce uric acid has no plausible therapeutic role here — if anything it would be contraindicated by mechanism. The evidence pack's own annotation for this candidate explicitly states the mechanistic direction is reversed and attributes the prediction to a likely knowledge-graph artifact (proximity to urate-metabolism nodes without correct directionality).

A biologically more coherent candidate further down the list is **rank 2, HGPRT partial deficiency** (e.g., Kelley-Seegmiller syndrome), where impaired purine salvage causes uric acid *overproduction* — a scenario where urate oxidase's uric-acid-lowering action is mechanistically sensible. However, this candidate currently has zero supporting clinical trials or literature and remains purely a graph-based hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Rasburicase currently has no license records in this evidence pack — the drug is **not marketed** in Singapore (0 registrations).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA/HSA label warnings and contraindications are a Blocking data gap — DG001 — and must be resolved before any safety evaluation can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (renal hypouricemia) is mechanistically implausible — it runs counter to the drug's known uric-acid-lowering action — and no clinical trial or literature evidence exists for any of the ten predicted indications (all L5, score-only). Combined with the drug's unregistered status in Singapore and missing safety/MOA data, this candidate does not meet the threshold to advance past S0.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/HSA label warnings & contraindications) — blocking for any safety review
- Resolve DG002 (formal MOA confirmation via DrugBank API)
- Re-run or manually override the rank-1 prediction given its flagged directional inconsistency; it should likely be deprioritized or excluded rather than advanced
- If pursuing repurposing, prioritize mechanistically coherent candidates (e.g., HGPRT partial deficiency) and commission a targeted literature/trial search, since none currently exists
- Preclinical or case-level evidence is the minimum needed before any candidate here can move beyond S0/L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

