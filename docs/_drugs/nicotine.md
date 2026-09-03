---
layout: default
title: Nicotine
parent: 僅模型預測 (L5)
nav_order: 703
evidence_level: L5
indication_count: 10
---

# Nicotine
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

Using the drug-repurposing evaluation report format to produce the Nicotine report from the supplied Evidence Pack.

# Nicotine: From Smoking Cessation to Exercise-Induced Malignant Hyperthermia

## One-Sentence Summary

Nicotine is a nicotinic acetylcholine receptor (nAChR) agonist generally known for its role in nicotine replacement therapy for smoking cessation and nicotine dependence; it is **not currently registered or marketed in Singapore** according to this evidence pack. The TxGNN model's top-ranked prediction for this candidate is **Exercise-Induced Malignant Hyperthermia**, but **no clinical trials and no literature** currently support this direction — the signal is a model-score-only prediction with no corroborating evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (nicotine is generally known as a nicotine replacement therapy agent for smoking cessation/nicotine dependence; no Singapore license record exists to confirm a formally approved indication) |
| Predicted New Indication | Exercise-Induced Malignant Hyperthermia |
| TxGNN Prediction Score | 83.91% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on generally known pharmacology, nicotine acts as an agonist at nicotinic acetylcholine receptors (nAChRs), a mechanism relevant to autonomic, neuromuscular, and central nervous system signaling — most clinically established in smoking cessation/nicotine replacement therapy.

Exercise-induced malignant hyperthermia, however, is a hereditary disorder of skeletal muscle calcium handling driven by mutations in the ryanodine receptor 1 (RYR1) calcium-release channel. This is a mechanistically distinct pathway from nicotinic cholinergic signaling, and the evidence pack's own repurposing rationale is explicit on this point: there is "no known connection between nicotinic acetylcholine receptor mechanisms and RYR1-related calcium channelopathy," and the association is assessed as "purely a TxGNN model prediction score, with no clinical evidence support."

Given the complete absence of clinical trials, literature, or a plausible mechanistic bridge, this prediction should be treated as a low-confidence, exploratory model output rather than a validated repurposing hypothesis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Nicotine has no registered product license on file in this evidence pack — market status is **Not Marketed**, with **0 registrations**. No dosage form, authorization number, or approved indication text is available to summarize.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (Exercise-Induced Malignant Hyperthermia, score 83.91%) has zero supporting clinical trials or literature and no plausible mechanistic link — it is a pure model-score signal (L5, decision stage S0) and does not warrant further action at this time. Notably, none of the 10 TxGNN-predicted indications for nicotine in this evidence pack reach a strong evidence tier: the relatively more evidence-backed candidates — blepharospasm (L3; two small pilot studies with inconsistent/negative results) and migraine disorder (L4; evidence largely shows nicotine withdrawal *triggers* migraine rather than treating it) — were both scored "Research Question," not "Go."

**To proceed, the following is needed:**
- Nicotine mechanism of action (MOA) data from DrugBank to properly evaluate mechanistic plausibility (currently a Blocking-severity data gap)
- Singapore product labeling/warnings and contraindications, since no registered license exists to source this from
- If pursuing any candidate from this predicted-indications list, prioritize blepharospasm or migraine disorder over Exercise-Induced Malignant Hyperthermia, given their (still weak) actual clinical/mechanistic evidence base, and commission a targeted literature/trial search before any further evaluation stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

