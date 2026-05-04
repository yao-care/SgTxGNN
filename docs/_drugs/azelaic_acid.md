---
layout: default
title: Azelaic Acid
parent: 僅模型預測 (L5)
nav_order: 129
evidence_level: L5
indication_count: 10
---

# Azelaic Acid
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

# Azelaic Acid: From Rosacea to Demodicidosis of Sebaceous Gland

## One-Sentence Summary

Azelaic acid is a topical dicarboxylic acid with well-established anti-inflammatory, antimicrobial, and antikeratinizing properties, approved internationally for acne vulgaris and rosacea.
The TxGNN model predicts it may be effective for **Demodicidosis of Sebaceous Gland** — a condition driven by pathological *Demodex* mite proliferation in sebaceous follicles, which shares biological overlap with rosacea.
However, **no clinical trials and no published literature** currently support this specific prediction, placing this candidate at the lowest evidence tier (L5).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acne vulgaris and rosacea (based on international approvals; no Singapore registration found) |
| Predicted New Indication | Demodicidosis of Sebaceous Gland |
| TxGNN Prediction Score | 98.05% |
| Evidence Level | L5 — Model prediction only, no supporting studies |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for this report. Based on known information, azelaic acid is a naturally occurring saturated C9 dicarboxylic acid with diverse biological activities: it inhibits reactive oxygen species (ROS) production, suppresses neutrophil-mediated inflammation, exerts antimicrobial activity against *Cutibacterium acnes* and *Malassezia* species, and inhibits follicular hyperkeratinization. These properties underpin its established use in acne vulgaris and rosacea.

Demodicidosis of sebaceous glands refers to clinically symptomatic infestation by *Demodex folliculorum* or *Demodex brevis* — mites that reside in sebaceous follicles and, when overabundant, trigger an inflammatory cascade involving Toll-like receptor activation and IL-17/IL-18 signaling. This pathophysiology substantially overlaps with rosacea, in which *Demodex* density is elevated and azelaic acid is an approved first-line treatment. The TxGNN model likely identified this indirect biological relationship: while azelaic acid has **no confirmed direct acaricidal activity**, its anti-inflammatory and follicular-normalizing mechanisms may attenuate *Demodex*-associated skin inflammation.

It is important to note that this mechanistic rationale remains indirect and speculative. The connection is through shared disease biology with rosacea rather than any demonstrated anti-*Demodex* effect. Without experimental or clinical validation specifically targeting demodicidosis, this prediction should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Azelaic acid currently has no registered products in Singapore. The drug is internationally available in multiple markets (e.g., EU, US) as topical formulations for acne and rosacea, but has not obtained Singapore Health Sciences Authority (HSA) registration.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products found | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (98.05%), this prediction is supported exclusively by knowledge-graph network inference — the mechanistic link between azelaic acid and demodicidosis of sebaceous glands is indirect (mediated through its rosacea indication), and there are currently no clinical trials, case series, or experimental studies specifically investigating this repurposing direction.

**To proceed, the following is needed:**
- In vitro studies confirming azelaic acid's direct or indirect activity against *Demodex* mites, or skin barrier effects in demodicidosis
- Detailed mechanism of action data (MOA) retrieved from DrugBank API (Data Gap DG002)
- Safety data from the Singapore-available package insert or FDA/EMA label (Data Gap DG001)
- At minimum, a retrospective clinical observation or pilot case series demonstrating symptomatic improvement in demodicidosis patients treated with azelaic acid before any prospective study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

