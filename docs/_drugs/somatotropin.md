---
layout: default
title: Somatotropin
parent: 僅模型預測 (L5)
nav_order: 919
evidence_level: L5
indication_count: 10
---

# Somatotropin
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

# Somatotropin: From Undocumented Original Indication to Middle Ear Neuroendocrine Tumor

## One-Sentence Summary

Somatotropin (recombinant human growth hormone, DB00052) has no original indication or mechanism-of-action data available in this evidence pack, and it is not currently registered in the Singapore market. TxGNN's top-ranked prediction links it to **Middle Ear Neuroendocrine Tumor**, but this is supported by only **2 loosely related publications and zero clinical trials**, and the underlying biology (GH/IGF-1 axis activation) points toward a tumor-growth risk signal rather than a therapeutic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented (no Singapore/Taiwan license data available; `original_indications` empty) |
| Predicted New Indication | Middle Ear Neuroendocrine Tumor |
| TxGNN Prediction Score | 96.82% |
| Evidence Level | L5 (model prediction only; no clinical trials, no directly relevant studies) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for somatotropin in this evidence pack. In general, recombinant GH acts through the GH receptor to stimulate hepatic IGF-1 production, driving linear growth and metabolic effects — this is a **growth-promoting/proliferative pathway**, not a mechanism that would typically be repurposed for an oncologic condition.

For the top-ranked prediction (middle ear neuroendocrine tumor), the two supporting publications do not actually study GH treatment of this tumor type: one examines stress-hormone profiles (including endogenous GH) in Ménière's disease and acoustic neuroma patients, and the other is a histopathology study of vestibular schwannoma growth factors. Neither establishes a treatment rationale. Because GH/IGF-1 signaling is a known growth-promoting axis, its presence in a tumor-adjacent context is more plausibly read as a **safety signal (potential tumor stimulation)** than as a repurposing opportunity — consistent with the evidence pack's own rationale annotation.

It is worth noting that other, lower-ranked predictions in this same evidence pack (mixed gonadal dysgenesis, mosaic monosomy X, and Turner syndrome due to structural X chromosome anomalies — ranks 5–7) have a **much stronger and more coherent mechanistic basis**: GH is an established therapy for short stature in Turner syndrome and related sex-chromosome mosaicism conditions, supported by a completed Phase 3 RCT (NCT00191113, Humatrope in Turner syndrome) and multiple cohort studies. These may represent more productive repurposing candidates than the current top-ranked hit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15925138](https://pubmed.ncbi.nlm.nih.gov/15925138/) | 2005 | Review/Observational | Brain Research Bulletin | Investigated stress hormones (including endogenous GH) in Ménière's disease and acoustic neuroma patients vs. controls; found correlation between cortisol and ACTH, not a GH-treatment study |
| [11200590](https://pubmed.ncbi.nlm.nih.gov/11200590/) | 2000 | Immunohistochemical study | Acta Oto-Laryngologica | Examined histopathological growth factors in 69 vestibular schwannoma specimens; no involvement of exogenous GH therapy |

---

## Singapore Market Information

Somatotropin is currently not registered in the Singapore market (0 licenses on record).

---

## Safety Considerations

Please refer to the package insert for safety information. Note: TFDA/HSA package insert warnings and contraindications for this drug are flagged as a **blocking data gap (DG001)** in this evidence pack and have not yet been reviewed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (middle ear neuroendocrine tumor) has no clinical trial support and only indirect, non-mechanistic literature; furthermore, GH/IGF-1 axis activation is mechanistically more consistent with a tumor-growth risk than a therapeutic benefit. Combined with a blocking safety data gap, this candidate does not meet the threshold to advance.

**To proceed, the following is needed:**
- Resolve DG001 (TFDA/HSA package insert warnings and contraindications) before any further safety evaluation (S1)
- Resolve DG002 (confirmed mechanism of action) to properly assess mechanistic plausibility
- Consider re-prioritizing evaluation toward the Turner syndrome / mixed gonadal dysgenesis / mosaic monosomy X predictions in this same evidence pack (ranks 5–7), which already carry L3 evidence and a completed Phase 3 RCT, and represent a substantially stronger repurposing signal than the current top-ranked candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

