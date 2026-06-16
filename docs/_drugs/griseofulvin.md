---
layout: default
title: Griseofulvin
parent: 僅模型預測 (L5)
nav_order: 438
evidence_level: L5
indication_count: 10
---

# Griseofulvin
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

# Griseofulvin: From Dermatophyte Infections to Myiasis

## One-Sentence Summary

Griseofulvin is a well-established antifungal agent historically used to treat superficial dermatophyte infections, including tinea capitis and onychomycosis, through inhibition of fungal microtubule protein.
The TxGNN model predicts it may be effective for **Myiasis** (fly larva parasitic infection of skin and tissue),
however this prediction is supported by **0 clinical trials** and only **1 veterinary review**, with no plausible pharmacological rationale connecting the two.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Superficial dermatophyte infections (tinea capitis, onychomycosis, tinea corporis) |
| Predicted New Indication | Myiasis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Griseofulvin is a fungistatic agent that disrupts fungal cell division by binding to microtubule protein (tubulin) specific to dermatophytes, thereby arresting mitosis. Its efficacy has been proven for superficial dermatophytic infections such as tinea capitis, tinea corporis, tinea pedis, and onychomycosis.

Myiasis refers to infestation by the larvae (maggots) of dipteran flies, affecting skin, wounds, or body cavities. This is a parasitic infection of arthropod origin — entirely distinct from fungal disease. Griseofulvin's molecular target (fungal microtubule protein) has no known biological activity against arthropod larvae, whose tubulin isoforms are structurally divergent from fungal targets.

The high TxGNN score (0.994) for myiasis is therefore likely an artifact of knowledge graph topology: the model may have linked Griseofulvin and myiasis through a shared "skin infection" node in the graph, reflecting co-occurrence in dermatology literature rather than true pharmacological relevance. There is no published clinical, preclinical, or mechanistic evidence supporting this repurposing direction. The overall assessment is that this is a **false positive prediction**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The following is the sole publication retrieved for the top-ranked indication (Myiasis):

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [4098614](https://pubmed.ncbi.nlm.nih.gov/4098614/) | 1970 | Veterinary Review | The Veterinary Record | Overview of parasitic skin diseases in dogs and cats; no direct evidence for Griseofulvin use in myiasis |

> **Note:** This is a veterinary review from 1970. It does not provide clinical evidence for Griseofulvin efficacy in myiasis and is not directly supportive of this repurposing hypothesis.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Detailed warnings, contraindications, and drug interaction data were not available in this Evidence Pack. Key data gaps include TFDA package insert warnings (Blocking severity) and full mechanism of action documentation (High severity). These should be retrieved before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Griseofulvin has no known pharmacological activity against dipteran larvae or any arthropod parasite, making the TxGNN prediction for myiasis mechanistically implausible; this appears to be a knowledge graph topology artifact rather than a true drug-disease signal. With zero clinical trials, zero registered studies, a single 1970 veterinary review unrelated to Griseofulvin efficacy, and no Singapore market presence, there is insufficient basis to advance this candidate.

**To proceed, the following would be needed:**
- A credible mechanistic hypothesis explaining how Griseofulvin could affect fly larvae (currently none exists)
- At minimum one preclinical study (in vitro or animal model) demonstrating larvicidal or larvistatic activity
- Resolution of Blocking data gap: retrieval of full safety profile and contraindication data from official package inserts
- Clarification of original approved indications (current `original_indications` field is empty)
- Reassessment of whether the TxGNN knowledge graph accurately represents biological relationships in this disease category, or whether the high score reflects spurious topological proximity

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

