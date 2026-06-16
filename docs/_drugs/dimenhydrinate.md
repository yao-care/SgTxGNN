---
layout: default
title: Dimenhydrinate
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Dimenhydrinate
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

The txgnn-pipeline skill confirms this is an SgTxGNN report generation task. Proceeding to produce the evaluation report from the Evidence Pack.

---

# Dimenhydrinate: From Motion Sickness to Allergic Urticaria

## One-Sentence Summary

Dimenhydrinate is a salt compound of diphenhydramine (a first-generation H1 antihistamine) and 8-chlorotheophylline, classically used to prevent and treat nausea, vomiting, and dizziness associated with motion sickness.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, supported by **0 clinical trials** and **1 pharmacokinetic publication** — evidence derived primarily from the mechanistic activity of its diphenhydramine component rather than direct clinical study of dimenhydrinate itself.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Motion sickness (nausea, vomiting, dizziness) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Dimenhydrinate is a molecular salt formed by combining diphenhydramine with 8-chlorotheophylline. The antihistaminic activity resides entirely in the diphenhydramine component — a prototypical first-generation H1 receptor antagonist — while 8-chlorotheophylline (a theophylline analogue) acts as a mild CNS stimulant to offset diphenhydramine's sedative burden. This pairing was historically engineered to retain antihistaminic benefit while improving tolerability in motion sickness contexts.

Allergic urticaria is driven by IgE-mediated mast cell degranulation, releasing histamine that binds H1 receptors on cutaneous vasculature and sensory nerve fibres, producing the characteristic wheal-and-flare response, vasodilation, and itch. First-generation H1 antihistamines — diphenhydramine among them — have a long clinical history in acute urticaria management and remain guideline-recognised agents (EAACI/WAO 2022) for situations requiring rapid H1 blockade. The pharmacokinetic study retrieved in this pack (PMID 30779257) further showed that oral dimenhydrinate delivers superior diphenhydramine bioavailability compared to standalone oral diphenhydramine in a canine model, suggesting that the dimenhydrinate formulation may actually improve the antihistaminic delivery that underlies this indication.

The mechanistic link is therefore biologically coherent, and the TxGNN model's high confidence score (99.74%) is consistent with that reasoning. The critical caveat is that the entire evidence chain is indirect: it flows through the diphenhydramine component rather than from any clinical study of dimenhydrinate as a single investigational drug for urticaria, and the single supporting publication used a veterinary model. No human urticaria data exist for dimenhydrinate itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Dimenhydrinate in Allergic Urticaria.

> Note: Clinical trial searches across all 10 predicted indications returned either zero results or clearly mismatched records unrelated to Dimenhydrinate (e.g., oncology biomarker studies, bowel preparation devices). All retrieved trials were graded "C — irrelevant" by the evidence pipeline and are excluded from this report.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | Pharmacokinetic study | *Veterinary Dermatology* | Oral dimenhydrinate produced superior diphenhydramine plasma exposure vs. oral diphenhydramine alone in healthy dogs; diphenhydramine suppressed histamine-induced wheal formation in vivo, confirming H1-mediated antihistaminic activity directly relevant to allergic urticaria pathophysiology |

---

## Singapore Market Information

Dimenhydrinate is not currently registered with Singapore's Health Sciences Authority (HSA). No authorisation records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Note: No key warnings, contraindications, or drug interaction data were available in the current evidence pack. TFDA package insert retrieval was flagged as a blocking data gap (DG001). Clinicians should independently review anticholinergic effects, sedation, and QTc implications — particularly relevant given dimenhydrinate's first-generation antihistamine class.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Dimenhydrinate in allergic urticaria is scientifically coherent (H1 blockade via diphenhydramine component), and TxGNN assigns high confidence (99.74%). However, current evidence sits at L4 — derived entirely from the component drug via a veterinary pharmacokinetic model — with no human clinical trials and no direct urticaria studies of dimenhydrinate as a tested entity. Absent even Phase 1/2 human data, clinical development cannot be recommended at this stage.

**To proceed, the following is needed:**
- Formal pharmacokinetic bridging study confirming that human H1 receptor occupancy from dimenhydrinate-derived diphenhydramine is equivalent to or superior to standalone diphenhydramine at therapeutic doses
- At least one Phase 2 proof-of-concept trial evaluating dimenhydrinate in acute allergic urticaria (comparator: cetirizine or loratadine as second-generation H1 standard of care)
- Complete MOA documentation from DrugBank (data gap DG002) to formalise the mechanistic rationale in regulatory submissions
- Singapore HSA registration package and package insert review to characterise safety profile, contraindications, and drug interactions (data gap DG001)
- Comparative positioning analysis: given that second-generation H1 antihistamines (non-sedating) are now the preferred first-line agents for urticaria, a clinical differentiation argument (e.g., faster onset, IV route availability for acute presentations) would be needed to justify development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

