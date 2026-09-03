---
layout: default
title: Selenium Sulfide
parent: 僅模型預測 (L5)
nav_order: 891
evidence_level: L5
indication_count: 10
---

# Selenium Sulfide
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

Using no additional skill — this is a direct content-generation task with an explicit, detailed template already provided; I'll follow it precisely against the supplied Evidence Pack.

# Selenium Sulfide: From Seborrheic Dermatitis/Tinea Versicolor to Vulvar Inverted Follicular Keratosis

## One-Sentence Summary

> Selenium sulfide is a topical agent conventionally used for seborrheic dermatitis, dandruff, and tinea versicolor; a specific Taiwan-approved indication is not present in this evidence pack, as the product is currently **not marketed** in Taiwan.
> The TxGNN model's top-ranked prediction is **Vulvar Inverted Follicular Keratosis**, a rare benign follicular tumor,
> but this prediction is supported by **0 clinical trials** and **0 publications** — it is a pure model-similarity output with no mechanistic or clinical corroboration.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in evidence pack (product not marketed in Taiwan); conventionally used for seborrheic dermatitis / tinea versicolor |
| Predicted New Indication | Vulvar Inverted Follicular Keratosis |
| TxGNN Prediction Score | 89.52% |
| Evidence Level | L5 |
| Taiwan Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for selenium sulfide is not available (flagged as a High-severity data gap, DG002). Based on known pharmacological information, selenium sulfide is a topical antifungal and keratolytic agent, primarily active against *Malassezia* (*Pityrosporum*) species, and its efficacy in seborrheic dermatitis, dandruff, and tinea versicolor is well established through decades of clinical use.

Vulvar inverted follicular keratosis, however, is a rare benign follicular epithelial tumor with a pathophysiology unrelated to fungal colonization or excess keratin turnover of the type selenium sulfide targets. Per the evidence pack's own rationale, "no published mechanism literature supports selenium sulfide's keratolytic/antifungal action affecting this pathological process; this is purely a TxGNN embedding-similarity prediction, without any clinical or mechanistic support." There is no plausible pharmacological bridge between the drug's known activity and this candidate indication.

**Note on alternative candidates:** Among the other 9 predictions in this pack, rank 2 — *cutaneous candidiasis* (score 83.86%, evidence level L4, decision stage S1, recommendation "Research Question") — is supported by 2 descriptive review articles discussing selenium sulfide as one of several topical options for superficial fungal skin infections. While still lacking controlled trial data specific to *Candida*, it is mechanistically closer to the drug's established antifungal profile than the top-ranked candidate and may warrant separate evaluation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Taiwan Market Information

This drug currently has no approved license registrations in Taiwan (market status: 未上市 / Not marketed; total licenses: 0). No dosage form or approved indication text is available from TFDA sources.

---

## Safety Considerations

Please refer to the package insert for safety information. (Note: TFDA label warnings/contraindications are flagged as a **Blocking** data gap — DG001 — meaning this candidate cannot yet proceed to the S1 safety pre-assessment stage until label data is obtained.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (vulvar inverted follicular keratosis) has no clinical trial, literature, or mechanistic support — it is evidence level L5 with no explanatory pathway connecting the drug's known antifungal/keratolytic action to this rare tumor. Additionally, a Blocking-severity data gap (missing TFDA label/warnings) prevents any formal safety pre-assessment.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain TFDA label/warnings and contraindications, or equivalent foreign labeling (e.g., US FDA) if the drug remains unmarketed in Taiwan
- Resolve DG002 (High): confirm mechanism of action via DrugBank/pharmacology reference
- If pursuing repurposing further, redirect evaluation toward rank 2 (cutaneous candidiasis), which has at minimum descriptive literature support and closer mechanistic plausibility than the current top-ranked candidate
- Given the rarity of vulvar inverted follicular keratosis, any future evaluation would likely require case-report-level evidence generation rather than large trials
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

