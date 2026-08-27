---
layout: default
title: Fosnetupitant
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
---

# Fosnetupitant
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

# Fosnetupitant: From Unknown Original Indication to Leprosy

## One-Sentence Summary

Fosnetupitant is referenced in this evidence pack only by mechanistic notes describing it as a Neurokinin-1 (NK1) receptor antagonist prodrug (related to netupitant); no confirmed original indication, approved MOA text, or Singapore market registration is currently on file. TxGNN's top-ranked prediction points to **Leprosy**, but this signal sits at the lowest evidence tier (**L5**) — **0 clinical trials** and **0 publications** — and the model's own mechanistic review flags it as a probable false-positive embedding artifact rather than a biologically grounded lead.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on record (no `original_indications` or licensed-product indication text available) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 96.44% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for fosnetupitant is not available in this evidence pack (`original_moa` = Data Gap), and no original/approved indication is on record. The only mechanistic context available comes from the rationale notes attached to each predicted candidate, which consistently identify fosnetupitant (and its active moiety, netupitant) as an **NK1 receptor antagonist** — the pharmacological basis TxGNN used to compute embedding-similarity scores across the ten candidate indications below.

For the top-ranked candidate, **Leprosy**, the model's own annotation is explicit that the link is **not biologically plausible**: leprosy is an infectious disease caused by *Mycobacterium leprae*, and there is no known mechanistic relationship between NK1 receptor antagonism and antimycobacterial activity. The rationale text concludes this is most likely a false-positive signal driven by knowledge-graph embedding similarity rather than a genuine pharmacological hypothesis.

Reviewing the full rank 1–10 list (see below), none of the ten candidates has a mechanistic link rated as strong. The two candidates with even a theoretical (not fosnetupitant-specific) rationale — coronary artery disease (rank 3) and myocardial ischemia (rank 6) — rely on preclinical, cross-drug-class literature about substance P/NK1 signaling in vascular inflammation, not on any human or fosnetupitant-specific data. The remaining candidates (mycotic corneal ulcer, ALCAPA, candidiasis, and four polyp-related conditions) are annotated as having little to no mechanistic justification.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Other TxGNN-Predicted Indications (Ranks 2–10, Not Further Evaluated)

All ten candidates share the same evidence profile: 0 clinical trials, 0 literature, Evidence Level L5, Recommendation Hold. For transparency, the internal mechanistic assessment for each is summarized below.

| Rank | Disease | Score | Internal Mechanistic Assessment |
|------|---------|-------|----------------------------------|
| 2 | Mycotic corneal ulcer | 96.21% | No plausible link; direction is inverted (substance P/NK1 *agonism*, not antagonism, is associated with corneal epithelial repair) |
| 3 | Coronary artery disease | 95.96% | Speculative — preclinical NK1/vascular-inflammation literature only, not drug-specific or human data |
| 4 | Anomalous left coronary artery from pulmonary artery (ALCAPA) | 95.70% | Not applicable — a structural congenital defect requiring surgical correction, not a pharmacologically modifiable condition |
| 5 | Candidiasis | 95.08% | No plausible link; NK1 antagonists have no reported antifungal activity |
| 6 | Myocardial ischemia | 94.96% | Speculative — same caveat as CAD; indirect, cross-class animal-model inference only |
| 7 | Uterine polyp | 94.81% | Very weak; sparse literature on substance P in endometrial inflammation, wrong pharmacological direction |
| 8 | Polyp of vocal cord | 94.70% | No known mechanistic link (mechanical/traumatic etiology) |
| 9 | Polyp of middle ear | 94.65% | No direct link; only a loose inflammatory-pathway association |
| 10 | Polyp of ureter | 94.56% | No known mechanistic link (local mucosal hyperplasia) |

---

## Singapore Market Information

Fosnetupitant is currently **not marketed** in Singapore (`market_status` = 未上市) and has **0 registered licenses** on file. No product name, dosage form, or approved indication text is available for this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: A Blocking-severity data gap (DG001 — regulatory label/warnings and contraindications) has not been remediated. This prevents a preliminary (S1) safety assessment for this candidate.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Every predicted indication in this evidence pack sits at the lowest evidence tier (L5) with zero supporting clinical trials or literature, and the model's own review identifies the top candidate (leprosy) as a likely false-positive signal with no biological plausibility.
- Foundational drug-level data — original indication, mechanism of action, and Singapore market/registration status — are all unavailable, and a Blocking-severity data gap (TFDA/HSA label) blocks even a preliminary safety screen.

**To proceed, the following is needed:**
- Confirmation of fosnetupitant's approved original indication(s) and full mechanism of action (e.g., via DrugBank API or manufacturer labeling)
- Retrieval of the official package insert / regulatory safety label to close the Blocking data gap (DG001)
- If the cardiovascular-inflammation hypotheses (coronary artery disease, myocardial ischemia) are of interest, a targeted literature review of NK1/substance-P signaling in vascular inflammation, since current support is indirect and not drug-specific
- No further evaluation recommended for leprosy, mycotic corneal ulcer, candidiasis, or ALCAPA — internal mechanistic review indicates these lack biological plausibility
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

