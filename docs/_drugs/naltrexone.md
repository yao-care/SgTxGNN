---
layout: default
title: Naltrexone
parent: 僅模型預測 (L5)
nav_order: 688
evidence_level: L5
indication_count: 10
---

# Naltrexone
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

# Naltrexone: From No Singapore-Registered Indication to Hypervitaminosis

## One-Sentence Summary

> Naltrexone currently holds no marketing authorization in Singapore (0 registrations on file), so its originally proven indication cannot be confirmed from this evidence pack.
> The TxGNN model's top-ranked prediction is **Hypervitaminosis**, but this candidate is supported by **0 clinical trials** and **0 publications**, and the model's own rationale states there is no known mechanistic link.
> Across all 10 predicted indications in this pack, none clear the bar for further development — this is a **Hold** across the board.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not established — Naltrexone has no marketed product in Singapore (0 licenses on file) |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 98.66% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed drug-level mechanism of action data is not available for Naltrexone in this evidence pack (flagged as a High-severity data gap). However, the evidence pack's own repurposing rationale for a lower-ranked candidate (restless legs syndrome, rank 5) identifies Naltrexone as a **μ-opioid receptor antagonist**, which is consistent with its known pharmacological class.

For the top-ranked candidate, **Hypervitaminosis**, the evidence pack explicitly states there is **no known mechanistic connection**: hypervitaminosis is a vitamin-toxicity state with no physiological relationship to opioid receptor antagonism. The high TxGNN score (98.66%) appears to reflect a statistical association in the knowledge graph rather than a biologically grounded hypothesis, and it is not corroborated by any clinical trial or literature evidence.

Looking across all 10 ranked candidates in this pack, none present a coherent mechanistic story supported by real-world evidence. The best-evidenced candidate is restless legs syndrome (rank 5, L4, 5 supporting papers), but the rationale itself flags a **mechanistic contradiction**: standard effective RLS therapies are opioid *agonists*, so an opioid *antagonist* like Naltrexone would theoretically risk worsening rather than treating RLS symptoms. Of the 5 papers, only one (PMID 39893547) directly concerns Naltrexone, and it is a pharmacovigilance/adverse-event signal study — suggesting RLS may be a Naltrexone side effect rather than a treatable indication. The remaining candidates (proximal 16p11.2 microdeletion syndrome, obsolete hypertelorism, frontorhiny, DECR deficiency leukodystrophy, myxomatous mitral valve prolapse, ADHD inattentive type, bridged sella turcica, autosomal hypospadias 3) are genetic, structural, or developmental conditions with no plausible link to opioid receptor pharmacology and zero supporting evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Naltrexone currently has no marketing authorization on file in Singapore (0 registrations; market status: Not Marketed).

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (Hypervitaminosis) has zero clinical or literature support and no plausible mechanistic link per the model's own rationale — it does not meet the bar for further evaluation.
- No candidate among the 10 ranked predictions reaches L1–L3 evidence; the single L4 candidate (restless legs syndrome) has a mechanistic rationale that argues *against* efficacy, not for it.
- Naltrexone is not currently marketed in Singapore, and a Blocking-severity data gap (TFDA/local label warnings and contraindications) means a safety assessment (S1) cannot be initiated regardless of indication choice.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): retrieve and parse the official product label for warnings/contraindications before any S1 safety review.
- Resolve DG002 (High): confirm Naltrexone's mechanism of action from DrugBank to validate or refute candidate mechanistic links.
- If pursuing repurposing further, prioritize re-scoring or expert review of lower-score-but-literature-supported candidates over the top raw TxGNN score, given the disconnect seen here between score rank and biological plausibility.
- Independent pharmacological review of the restless legs syndrome hypothesis is needed before dismissal or advancement, given the contradictory direction of effect noted above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

