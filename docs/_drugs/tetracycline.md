---
layout: default
title: Tetracycline
parent: 僅模型預測 (L5)
nav_order: 967
evidence_level: L5
indication_count: 10
---

# Tetracycline
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

# Tetracycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

> Tetracycline is a broad-spectrum antibiotic; no specific original indication or Singapore registration record is available in this evidence pack, and it is currently **not marketed** in Singapore.
> The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
> but this is currently supported by only **1 case report** and **no clinical trials**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — no Singapore license records exist for this drug |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Tetracycline belongs to the tetracycline class of broad-spectrum antibiotics, known to have activity against *Chlamydia trachomatis*, the causative organism of follicular conjunctivitis and related ocular infections.

The mechanistic rationale for this prediction rests on tetracycline's antichlamydial activity: punctate epithelial keratoconjunctivitis can occur secondary to chlamydial follicular conjunctivitis, so an antibiotic active against *C. trachomatis* is a plausible candidate.

However, the mechanistic link is weak in practice. The single supporting publication (Hardten et al., 1992) describes two cases in which punctate epithelial keratitis **persisted or recurred after** the underlying chlamydial follicular conjunctivitis had already resolved with oral tetracycline/doxycycline treatment. This is a description of a post-treatment complication, not evidence that tetracycline treats or prevents punctate epithelial keratoconjunctivitis. The prediction should therefore be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Report | Cornea | Two cases of chlamydial follicular conjunctivitis treated with oral tetracycline/doxycycline subsequently developed recurrent bilateral punctate epithelial keratitis — describes a post-treatment complication, not a treatment effect |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only available evidence is a single 1992 case report describing keratitis that occurred *after* chlamydial conjunctivitis resolved with treatment — this does not demonstrate that tetracycline is effective for punctate epithelial keratoconjunctivitis. Combined with the absence of any clinical trials, MOA data, safety data, or Singapore market presence, evidence is insufficient to advance this candidate.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank
- Package insert warnings/contraindications (currently a Blocking data gap per meta.data_gaps)
- Prospective or comparative clinical evidence (not just a single case report) supporting antichlamydial therapy for punctate epithelial keratoconjunctivitis
- Confirmation of Singapore regulatory status, since the drug currently has zero registrations

**Note:** Within this same evidence pack, **chronic rhinosinusitis** (rank 3, TxGNN score 99.15%) shows substantially stronger evidence — an L2 evidence level with completed Phase 2/3 RCTs, a Cochrane systematic review, and a dedicated meta-analysis — though nearly all of that evidence is for doxycycline rather than tetracycline itself (same-class extrapolation). This candidate may warrant a separate, dedicated evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

