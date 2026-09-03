---
layout: default
title: Venlafaxine
parent: 僅模型預測 (L5)
nav_order: 1052
evidence_level: L5
indication_count: 10
---

# Venlafaxine
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

# Venlafaxine: From Depression/Anxiety Spectrum (SNRI Class) to Ohdo Syndrome and Variants

## One-Sentence Summary

> Venlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI); the evidence pack does not contain formal Singapore-approved indication data (the drug is not marketed here), but internal rationale annotations consistently describe it as an antidepressant used across the depression/anxiety spectrum.
> The TxGNN model's **top-ranked** prediction is **Ohdo Syndrome and Variants**, a rare genetic developmental disorder — but this candidate has **zero supporting clinical trials and zero literature**, and the evidence pack itself flags the high score as likely embedding-space noise rather than a genuine mechanistic signal.
> Several **lower-ranked** predictions (dysthymic disorder, melancholia, OCD, agoraphobia) are far better supported, with real Phase 2–4 trials and RCT-level literature — these are discussed in the Conclusion as the more credible repurposing leads from this pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — Venlafaxine has no Singapore regulatory license on file (0 registrations); rationale annotations describe it generically as an SNRI antidepressant |
| Predicted New Indication | Ohdo Syndrome and Variants |
| TxGNN Prediction Score | 95.86% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (flagged as a High-severity data gap, DG002). Based on the rationale annotations included in this evidence pack, venlafaxine is consistently characterized as a serotonin-norepinephrine reuptake inhibitor (SNRI) whose established therapeutic domain is depressive and anxiety-spectrum disorders — this is corroborated by the strong clinical/literature support found for several *other* candidates in this same pack (e.g., dysthymic disorder, melancholia, OCD, agoraphobia).

Ohdo syndrome and its variants, however, are rare congenital developmental disorders caused by mutations in chromatin-modifying genes (e.g., KAT6A/KAT6B), involving structural and epigenetic regulatory abnormalities. There is no established pharmacological or pathophysiological link between this gene-driven developmental condition and venlafaxine's monoamine reuptake inhibition mechanism.

The evidence pack's own rationale is explicit on this point: the high TxGNN score for this candidate is assessed as likely reflecting **proximity noise in the knowledge-graph embedding space**, not a genuine signal of mechanistic plausibility. No clinical trials or publications exist to support this indication, and the model's top numerical rank should not be interpreted as its most clinically credible prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA/HSA label warnings and contraindications for venlafaxine could not be retrieved for this evidence pack — flagged as a **Blocking** data gap, DG001 — and drug-drug interaction data was not found. These must be resolved before any safety evaluation stage.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Ohdo Syndrome and Variants) has no clinical trial or literature support (L5, decision stage S0) and no plausible mechanistic link to venlafaxine's SNRI activity; the evidence pack itself attributes the high score to embedding noise rather than a true signal. Combined with a Blocking data gap on safety labeling (DG001) and missing MOA data (DG002), this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Resolve DG001 (HSA/regulatory safety label) and DG002 (formal MOA) before any further evaluation of this or other candidates for this drug
- If pursuing Ohdo syndrome specifically: obtain preclinical/mechanistic rationale linking monoamine reuptake inhibition to KAT6A/KAT6B-driven pathology — currently none exists
- **Redirect evaluation effort toward better-supported candidates in this same pack**, which warrant separate "Proceed with Guardrails" review:
  - *Dysthymic disorder* (rank 5, L2, direct RCT/open-label evidence including elderly and SCI populations)
  - *Melancholia* (rank 6, L2, multiple double-blind RCTs including hospitalized cohorts)
  - *Obsessive-compulsive disorder* (rank 9, L2, multiple double-blind head-to-head trials in treatment-resistant OCD)
  - *Agoraphobia* (rank 10, L2, large double-blind RCTs in panic disorder with agoraphobia)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

