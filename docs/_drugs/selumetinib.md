---
layout: default
title: Selumetinib
parent: 僅模型預測 (L5)
nav_order: 895
evidence_level: L5
indication_count: 10
---

# Selumetinib
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

# Selumetinib: From an Undocumented Original Indication to Familial Generalized Lentiginosis

## One-Sentence Summary

Selumetinib's original approved indication and mechanism-of-action data are not available in this evidence pack — the drug is not registered in Singapore, and detailed MOA is flagged as a blocking data gap. TxGNN's top-ranked prediction points to **Familial Generalized Lentiginosis**, but this is supported by **zero clinical trials and zero publications**, making it a pure algorithmic signal rather than an actionable candidate. Notably, this same evidence pack contains other candidates (peripheral nerve schwannoma, rhabdoid tumor) with substantially stronger real-world evidence — these are summarized separately below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no approved indication text exists because Selumetinib has 0 registrations in Singapore, and original MOA is also unrecorded (see Data Gaps) |
| Predicted New Indication | Familial Generalized Lentiginosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

**Blocking data gaps affecting this evaluation:**
- **DG001 (Blocking)**: HSA/label warnings and contraindications are unavailable, preventing any S1 safety pre-screen.
- **DG002 (High)**: Detailed mechanism of action is unavailable, limiting mechanistic-linkage analysis.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for Selumetinib in this evidence pack. Based on the rationale text accompanying the model's predictions, Selumetinib is understood to act as a MEK inhibitor targeting the RAS-MAPK signaling pathway — this description recurs consistently across multiple predicted-indication rationales in the pack, even though it is not formally captured in the `original_moa` field.

Familial Generalized Lentiginosis belongs to the RASopathy spectrum of conditions (overlapping phenotypically with LEOPARD/Legius syndrome), which is theoretically linked to RAS-MAPK pathway activation. This gives the prediction a plausible mechanistic rationale in principle. However, the evidence pack explicitly notes that **no experimental or clinical data currently support MEK inhibitor use in this specific indication** — the link is described as "purely a TxGNN algorithmic inference" (`repurposing_rationale.mechanistic_link`). This is consistent with the L5 evidence level (model prediction only, no actual studies) and the resulting Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Selumetinib is **not currently registered in Singapore** (0 licenses on file). No product name, dosage form, or approved indication text is available for this market.

---

## Cytotoxicity (Antineoplastic Drugs Only)

Selumetinib is understood to be a targeted oncology agent (MEK inhibitor acting on the RAS-MAPK pathway), based on mechanism descriptions embedded in this evidence pack's repurposing rationales.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Other Predicted Indications in This Evidence Pack

This evidence pack ("multi" candidate set) contains 10 TxGNN-predicted indications for Selumetinib. Most share the same pattern as the headline prediction above — high TxGNN scores (>99.9%) but **zero corroborating evidence** (L5, Hold): familial generalized lentiginosis, gastrocutaneous syndrome, acromelanosis, congenital café-au-lait/SCE syndrome, Moynahan syndrome, and three other ultra-rare syndromes.

Two candidates, however, stand apart with real supporting evidence and warrant separate tracking as research questions:

| Rank | Disease | Evidence Level | Decision Stage | Key Support |
|------|---------|----------------|-----------------|--------------|
| 9 | Peripheral nerve schwannoma | **L2** | S2 (Research Question) | A dedicated Phase 2 trial ([NCT03095248](https://clinicaltrials.gov/study/NCT03095248)) in NF2-related tumors — terminated early due to poor accrual (n=10) — plus 7 supporting publications, including a preclinical study on MEK1/2 inhibition (AZD6244) in primary schwannoma cells (PMID [19804833](https://pubmed.ncbi.nlm.nih.gov/19804833/)) and a case report of partial response in NF2-associated disease (PMID [38058737](https://pubmed.ncbi.nlm.nih.gov/38058737/)) |
| 3 | Rhabdoid tumor | **L3** | S1 (Research Question) | Screened within the NCI-COG Pediatric MATCH basket trial ([NCT03155620](https://clinicaltrials.gov/study/NCT03155620)); preclinical evidence that MAPK pathway activation is a druggable driver in atypical teratoid/rhabdoid tumors (PMID [25638158](https://pubmed.ncbi.nlm.nih.gov/25638158/)) |

These two candidates should be considered the more scientifically credible outputs of this evidence pack and, if this evaluation is to be extended, are better starting points than the nominally highest-scoring but evidence-free prediction above.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Familial Generalized Lentiginosis) is an L5, evidence-free algorithmic output with no clinical trials, no literature, and an explicitly acknowledged lack of biological validation. Combined with the blocking absence of HSA label/safety data (DG001) and MOA data (DG002), and the drug's unregistered status in Singapore, there is no basis to advance this specific indication.

**To proceed, the following is needed:**
- Resolve DG001: obtain HSA-equivalent (or originating regulator, e.g., FDA/EMA) label warnings and contraindications before any safety pre-screen (S1) can begin.
- Resolve DG002: confirm Selumetinib's original approved indication and formal mechanism of action via DrugBank or manufacturer labeling.
- If pursuing repurposing signals from this evidence pack, redirect evaluation toward the two evidence-backed candidates — **peripheral nerve schwannoma (L2)** and **rhabdoid tumor (L3)** — rather than the top TxGNN score alone.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

