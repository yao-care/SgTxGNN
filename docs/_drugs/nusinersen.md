---
layout: default
title: Nusinersen
parent: 僅模型預測 (L5)
nav_order: 719
evidence_level: L5
indication_count: 10
---

# Nusinersen
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

Using the evidence pack as given — this one is a genuine low/no-signal case (all 10 candidates score exactly 0.5, ranked ~51,800+ out of the candidate pool, with rationale text explicitly stating "no mechanistic link" for most). I'll write the report honestly rather than dressing it up.

# Nusinersen: From Spinal Muscular Atrophy to Tendinopathy

## One-Sentence Summary

Nusinersen (based on literature context in this evidence pack) is known as a treatment for spinal muscular atrophy (SMA); formal original-indication data was not supplied for this evaluation.
The TxGNN model's top-ranked candidate in this pack is **Tendinopathy**, but the prediction score is **50.00%** (the model's non-significant baseline) with a rank of ~51,833 out of the full candidate pool, and **0 clinical trials** and **0 publications** support this specific pairing.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed via structured data — drug is not marketed in Singapore, so no license-based indication text is available. Literature in this pack (attached to a different candidate) refers to Nusinersen as an approved SMA therapy, but this is not a verified original-indication field. |
| Predicted New Indication | Tendinopathy |
| TxGNN Prediction Score | 50.00% (non-significant; rank 51,833) |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form for this drug (flagged as a **High-severity data gap**, DG002). Based on literature captured elsewhere in this evidence pack, Nusinersen is described as an antisense oligonucleotide (ASO) that corrects SMN2 pre-mRNA splicing, restoring functional SMN protein in spinal muscular atrophy.

For the top-ranked candidate in this pack, **tendinopathy**, the model-generated rationale is explicit that there is **no mechanistic link**: tendinopathy is a connective-tissue/mechanical-load pathology, unrelated to SMN2 splicing regulation. The TxGNN score of 0.5 is the model's non-informative baseline, and the candidate's rank (~51,833) places it near the bottom of the scored pool rather than among genuinely high-confidence predictions — this is consistent with an absence of real signal rather than a promising repurposing lead.

The same pattern holds across all 10 candidates in this pack: every one scores exactly 0.5 with ranks in the ~51,800s, and 9 of the 10 have zero clinical trials and zero literature. The one exception (Rowley-Rosenberg syndrome, rank 4) returned 19 PubMed hits, but on inspection every hit is a general Nusinersen/SMA safety or comparative-effectiveness paper with no connection to Rowley-Rosenberg syndrome — a keyword-matching artifact, not real evidence, as already noted in that candidate's own rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Nusinersen has no license registrations in Singapore (`total_licenses: 0`, market status: 未上市), so no market information table can be produced.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: TFDA-equivalent label warnings/contraindications are flagged as a **Blocking** data gap (DG001) — this must be resolved before any S1 safety screening can proceed, regardless of the indication decision below.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked predicted indication (tendinopathy) has a non-significant TxGNN score (0.5), a near-bottom rank, no mechanistic rationale, and zero clinical/literature evidence.
- No candidate in this pack reaches even L4 evidence; all are L5 with an explicit "Hold" recommendation from the scoring layer itself.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/label warnings and contraindications — Blocking) and DG002 (mechanism of action — High) before any further evaluation.
- Re-query the TxGNN model for this drug's genuinely top-scoring candidates — the 10 candidates in this pack are clustered at ranks ~51,800+, which suggests these are not the model's highest-confidence outputs and a proper top-N extraction should be re-run.
- If a repurposing signal for an SMN2-splicing-related condition exists, prioritize evaluating that over the candidates currently listed here.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

