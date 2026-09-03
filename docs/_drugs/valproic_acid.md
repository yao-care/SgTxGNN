---
layout: default
title: Valproic Acid
parent: 僅模型預測 (L5)
nav_order: 1043
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

# Valproic Acid: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

> Valproic acid (DB00313) is a broad-spectrum antiepileptic and mood-stabilizing drug, well documented across dozens of publications in this evidence pack for the treatment of generalized and reflex epilepsies.
> The TxGNN model's top-ranked prediction is **Trigeminal Nerve Neoplasm**, with a very high raw score (**99.97%**),
> but this is supported by **0 clinical trials** and only **1 unrelated case series**, indicating the prediction is very likely an algorithmic artifact rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (per literature evidence in this pack; no formal Singapore label text available — see Market Status) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank mechanism-of-action summary is not available in this evidence pack (marked as a High-severity data gap, DG002). However, the literature collected across multiple predicted indications consistently describes valproic acid as a broad-spectrum antiseizure medication that enhances GABAergic transmission, modulates voltage-gated sodium and T-type calcium channels, and raises the seizure threshold. This pharmacology underlies its established role across many epilepsy syndromes.

For the top-ranked prediction — trigeminal nerve neoplasm — the evidence pack's own rationale flags this as a weak match: there is no mechanistic pathway connecting VPA's antiepileptic/GABAergic activity to antitumor activity against trigeminal nerve tumors, and the single literature hit is a 1997 case series on Sturge-Weber syndrome (a vascular/neurocutaneous disorder with associated epilepsy), not a study of nerve tumors or VPA's antineoplastic use. This pattern is consistent with a TxGNN disease-entity matching artifact, where the model likely confused "trigeminal" with unrelated neurological entities in the knowledge graph rather than identifying a genuine pharmacological link.

Notably, this evidence pack also contains several other VPA-related predictions with substantially stronger support — for example, **visual epilepsy** (rank 2, L2 evidence, "Proceed with Guardrails") and **trigeminal neuralgia** (rank 3, L3 evidence, including a direct clinical study of sodium valproate in trigeminal neuralgia, PMID 6776393). These are mechanistically coherent extensions of VPA's known antiepileptic/analgesic profile and may warrant separate evaluation, whereas the rank 1 candidate discussed here does not.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | Anales españoles de pediatría | Review of 14 Sturge-Weber syndrome cases; not related to trigeminal nerve tumors or VPA's antitumor activity — relevance to this indication is unclear |

---

## Singapore Market Information

This drug is currently not marketed in Singapore (未上市), and no registration records (SIN numbers) are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The trigeminal nerve neoplasm prediction, despite its high raw TxGNN score, is backed by zero clinical trials and a single unrelated case series. The internal rationale explicitly characterizes this as likely knowledge-graph matching noise rather than a genuine mechanistic signal, so it does not meet the threshold to advance past initial screening (S0).

**To proceed, the following is needed:**
- Formal DrugBank/label mechanism-of-action data (DG002)
- Singapore/regional regulatory label warnings and contraindications (DG001, currently blocking safety pre-screening)
- If pursuing VPA repurposing further, prioritize re-evaluating the higher-evidence candidates already surfaced in this pack — **visual epilepsy** (L2, Proceed with Guardrails) and **trigeminal neuralgia** (L3, direct clinical evidence) — rather than this rank 1 candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

