---
layout: default
title: Secukinumab
parent: 僅模型預測 (L5)
nav_order: 889
evidence_level: L5
indication_count: 10
---

# Secukinumab
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

# Secukinumab: From Undocumented Original Indication to Primary Release Disorder of Platelets

## One-Sentence Summary

Secukinumab is an anti-IL-17A monoclonal antibody, but its original approved indication is not documented in this evidence pack because the drug is currently **not registered in Singapore**. The TxGNN model's top-ranked prediction is **Primary Release Disorder of Platelets** (score 98.16%), but this is supported by **zero clinical trials and zero literature**, and the model's own mechanistic review flags it as a likely knowledge-graph artifact rather than a biologically credible lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (no licenses on file; drug not registered in Singapore) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.16% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured MOA field (flagged as a High-severity data gap, DG002). Based on the mechanistic notes embedded in the evidence pack, secukinumab is known to act as an anti-IL-17A monoclonal antibody targeting the Th17/IL-17 inflammatory axis — the same axis underlying its established use in IL-17-driven autoimmune conditions. However, because this drug is not registered in Singapore, no approved-indication text is available to compare against the predicted indication.

More importantly, the evidence pack's own mechanistic rationale for the top-ranked prediction is unfavorable: primary release disorder of platelets is a structural/signaling defect in platelet granule secretion with no established connection to IL-17A biology. The rationale explicitly states this high TxGNN score is *"suspected to be knowledge-graph embedding noise (an indirect drug-disease node linkage, not a biologically plausible pathway)."* Ranks 2, 3, 6, 7, 9, and 10 share the same pattern — congenital/structural platelet or hormone-receptor-driven diseases with no IL-17A pathway involvement and no supporting trials or literature.

Among the 10 candidates reviewed, only rank 5 (drug-induced osteoporosis) carries a partially plausible mechanism — IL-17A is known to promote osteoclast differentiation, and secukinumab has been associated with relative bone mineral density preservation in axial spondyloarthritis populations — but it is explicitly scored as a **research hypothesis**, not a supported indication, since no trial or publication in this dataset addresses it directly.

### Other TxGNN Predictions Reviewed (Ranks 2–10)

| Rank | Disease | Score | Recommendation | Note |
|------|---------|-------|-----------------|------|
| 2 | Pseudo-von Willebrand disease | 97.74% | Hold | Structural GPIbα defect, no IL-17A link |
| 3 | Glanzmann thrombasthenia | 97.34% | Hold | Congenital GPIIb/IIIa defect, no IL-17A link |
| 4 | HER2+ breast carcinoma | 96.48% | Hold | No mechanistic overlap, no supporting evidence |
| 5 | Drug-induced osteoporosis | 95.27% | Research Question | Only candidate with plausible mechanism (osteoclast/IL-17), no direct evidence |
| 6 | Normal breast-like subtype breast carcinoma | 95.09% | Hold | No mechanistic overlap |
| 7 | PR-positive breast cancer | 95.09% | Hold | Hormone-receptor pathway, unrelated to IL-17A |
| 8 | Breast tumor luminal A/B | 94.98% | Hold | 19 literature hits retrieved, but all are keyword-noise matches on "B" (B-cell biology, hepatitis B vaccines) — no relevance to breast cancer or secukinumab |
| 9 | PR-negative breast cancer | 94.51% | Hold | No mechanistic overlap |
| 10 | Fetal/neonatal alloimmune thrombocytopenia | 92.69% | Hold | Alloimmune/IVIG-driven pathology, not Th17-mediated |

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Secukinumab is not currently registered or marketed in Singapore under this evidence pack (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: TFDA/HSA warnings and contraindications are recorded as a **Blocking** data gap (DG001) — this drug cannot proceed to a Stage 1 (S1) safety review until package insert data is obtained.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 10 predicted indications rest solely on TxGNN model scores (L5, no trials, no literature). The top-ranked candidate is explicitly flagged by the model's own mechanistic rationale as a probable knowledge-graph artifact with no biological link to secukinumab's IL-17A mechanism, and the one literature-linked candidate (breast tumor luminal A/B) turned out to be keyword noise unrelated to the disease or drug. Combined with a Blocking safety data gap and no Singapore market registration, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- TFDA/HSA package insert data (warnings, contraindications) — Blocking gap DG001
- Structured MOA confirmation via DrugBank API — High-severity gap DG002
- If pursuing the drug-induced osteoporosis research hypothesis (rank 5): a targeted literature/trial search on IL-17A inhibition and bone mineral density outcomes
- Independent verification of secukinumab's actual original indication(s), since this evidence pack contains no registry data to confirm it
- Re-run literature retrieval with disease-specific search terms (not single-letter keyword matching) to avoid noise matches like those seen in rank 8
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

