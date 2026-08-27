---
layout: default
title: Latanoprostene Bunod
parent: 僅模型預測 (L5)
nav_order: 576
evidence_level: L5
indication_count: 10
---

# Latanoprostene Bunod
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

# Latanoprostene Bunod: From Ocular Hypertension/Glaucoma to Visceral Calciphylaxis

## One-Sentence Summary

> Latanoprostene bunod is an ophthalmic agent (FP-receptor agonist + nitric oxide donor) used for intraocular-pressure lowering; its formal original indication and mechanism-of-action record are currently a data gap in this evidence pack, though clinical trial titles in the dataset confirm use in ocular hypertension/primary open-angle glaucoma populations. The TxGNN model's **top-ranked** prediction for this drug is **Visceral Calciphylaxis**, but this specific candidate is supported by **0 clinical trials** and **0 publications**, and the model's own mechanistic review flags it as likely statistical noise rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in structured data (Data Gap) — trial evidence in this pack (NCT03931317) indicates use in ocular hypertension / primary open-angle glaucoma populations |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for latanoprostene bunod is not available in the current record (Data Gap). Based on information embedded elsewhere in this evidence pack (repurposing rationale text and clinical trial titles), the compound acts through FP-receptor activation combined with nitric oxide (NO) release, a mechanism used to lower intraocular pressure — consistent with use in glaucoma / ocular hypertension.

For the top-ranked candidate specifically — **visceral calciphylaxis** — the model's own mechanistic assessment does **not** support the prediction. Calciphylaxis is pathologically driven by vascular calcification and microthrombosis, a disease process with no known mechanistic overlap with FP-receptor activation or NO-donor–mediated IOP reduction. No clinical trial, registry trial, or publication in this evidence pack addresses this drug-disease pair; the high TxGNN similarity score appears to reflect model-internal pattern matching rather than a biologically grounded hypothesis.

For transparency: two other candidates in this same prediction set carry materially stronger support and may warrant separate evaluation — **primary hereditary glaucoma** (rank 2, L4, mechanistically plausible via the same IOP-lowering pathway as the drug's presumed original use) and **vascular disease** (rank 6, L3, supported by two completed trials — NCT03949244 and NCT03931317 — directly measuring the drug's microvascular/nailfold capillary blood-flow effects). These are not the subject of this report but are noted here because they emerged from the same TxGNN run and materially change the interpretation of "how reasonable is this drug's repurposing profile overall" versus this specific rank-1 candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- This candidate (visceral calciphylaxis) has no clinical trial or literature support, no coherent mechanistic link to the drug's known pharmacology, and an evidence level of L5 (model prediction only) — the weakest tier in this framework. The drug's own repurposing rationale explicitly characterizes this as likely model noise rather than an actionable hypothesis.

**To proceed, the following is needed:**
- Confirmed original indication and full mechanism-of-action (MOA) data for latanoprostene bunod (currently Data Gap)
- TFDA/regulatory label warnings and contraindications (currently Data Gap, flagged as Blocking — required before any S1 safety evaluation)
- If repurposing investment is desired for this drug, consider redirecting attention to the higher-evidence candidates identified in the same run — **vascular disease** (L3, two supporting trials) and **primary hereditary glaucoma** (L4, strong mechanistic plausibility) — rather than pursuing visceral calciphylaxis further
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

