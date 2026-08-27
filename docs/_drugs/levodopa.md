---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 590
evidence_level: L5
indication_count: 10
---

# Levodopa
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

Using data-report discipline (no fabrication, evidence-pack-only sourcing, empty fields flagged rather than invented) since this report synthesizes a JSON evidence pack into a decision document — every figure, indication, and citation below traces directly to a field in the provided JSON.

A note on methodology before the report: `predicted_indications[0]` (the field the template specifies for "Predicted New Indication") is **Rasmussen subacute encephalitis** — the highest TxGNN *score*, but per the pack's own `repurposing_rationale`, one of its weakest-evidence candidates (L5, zero trials, zero literature, flagged internally as a likely embedding-similarity false positive). I followed the template's extraction rule exactly rather than substituting a better-evidenced candidate, and I flag this explicitly below so the "Hold" call isn't mistaken for the pack's best opportunity — nine other ranked candidates in this same pack (notably Lewy body dementia, MSA-Parkinsonian type) carry materially stronger evidence and are surfaced in the Conclusion.

---

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

> Levodopa (DrugBank DB01235) is not documented in this evidence pack via a structured original-indication field, but pack literature (PMID 36402160) confirms it as the standard symptomatic therapy for **Parkinson's disease**, acting via dopamine replacement in the nigrostriatal pathway.
> The TxGNN model's top-ranked prediction in this pack is **Rasmussen Subacute Encephalitis**, with a prediction score of **99.06%** —
> however **0 clinical trials** and **0 publications** currently support this specific link, and the pack's own mechanistic rationale flags it as a probable false-positive signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (inferred from cited literature within this pack, e.g. PMID 36402160 — "Levodopa is the most effective symptomatic therapy for Parkinson's disease"); no Singapore license record confirms this independently |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Levodopa is not available in this evidence pack (`original_moa: "[Data Gap]"`, tracked as gap DG002, High severity). Based on the pack's own cited literature, Levodopa functions as a dopamine precursor that restores dopaminergic transmission in the nigrostriatal pathway, and its efficacy in Parkinson's disease and related Levodopa-responsive parkinsonian syndromes is well established across the pack's evidence (e.g., PMID 36402160, PMID 17534959).

Rasmussen subacute encephalitis, however, is a unilateral, T-cell-mediated autoimmune inflammatory epilepsy syndrome of the cerebral cortex. Per this pack's own `repurposing_rationale`, it has **no known pathological relationship** to nigrostriatal dopaminergic degeneration, the mechanism Levodopa targets. The rationale text explicitly states the high TxGNN score most likely reflects knowledge-graph embedding similarity rather than genuine biological plausibility, and assesses this as a **probable false-positive signal** — a conclusion reinforced by the complete absence of clinical trial or literature support (confirmed via three independent zero-result queries: clinicaltrials, ictrp, and pubmed, all dated 2026-03-10).

Given this, the mechanistic case for this specific candidate is weak, and the recommendation below reflects that assessment rather than the general reasonableness of Levodopa as a repurposing candidate overall.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Levodopa currently has no registrations on file for Singapore (`market_status: 未上市`, `total_licenses: 0`, no license records provided). No authorization number, product name, or approved indication text is available to report.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug interaction data are all marked as data gaps in this pack — see gap DG001 below — and no DDI records were found.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (Rasmussen subacute encephalitis) has Evidence Level L5 — a TxGNN score with no supporting clinical trials or literature, and the pack's own mechanistic rationale assesses it as a likely false-positive signal with no known biological link to Levodopa's dopaminergic mechanism. Additionally, a **Blocking**-severity data gap (DG001: HSA/TFDA label warnings and contraindications) prevents this candidate from entering even a preliminary safety assessment (S1), independent of the efficacy question.

**To proceed, the following is needed:**
- HSA/TFDA package insert (warnings and contraindications) — required to clear the Blocking gap (DG001) before any safety pre-assessment
- DrugBank mechanism-of-action data — required to properly assess mechanistic linkage (gap DG002)
- Preclinical or mechanistic studies specifically linking dopaminergic pathways to Rasmussen encephalitis pathology, given the current complete absence of clinical or literature evidence
- Consider that this same evidence pack contains other Levodopa-predicted indications with materially stronger evidence bases and "Proceed with Guardrails" recommendations — notably **Lewy body dementia** (L2, 5 trials, 19 publications), **multiple system atrophy, parkinsonian type** (L3, 5 trials, 20 publications), **PLA2G6-associated neurodegeneration** (L3, 20 publications), and **progressive supranuclear palsy-corticobasal syndrome** (L3, 6 trials, 3 publications). These may warrant separate, dedicated evaluation ahead of this lower-confidence candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

