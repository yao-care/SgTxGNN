---
layout: default
title: Phenyltoloxamine
parent: 僅模型預測 (L5)
nav_order: 780
evidence_level: L5
indication_count: 10
---

# Phenyltoloxamine
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

# Phenyltoloxamine: From Antihistamine Combination Use to Allergic Urticaria

## One-Sentence Summary

> Phenyltoloxamine is a first-generation H1-antihistamine most commonly found as a component of combination cold/allergy products (e.g., Sinutab-type formulations); no standalone original indication is documented in the evidence pack.
> The TxGNN model predicts it may be effective for **Allergic Urticaria**,
> but this is currently supported by **0 clinical trials** and **0 publications** — the prediction rests on drug-class mechanism inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally documented; pharmacologically known as an H1-antihistamine component of combination cold/allergy products |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 96.24% |
| Evidence Level | L4 (mechanism-based, no direct clinical/literature support) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Phenyltoloxamine (DB11160). Based on known pharmacological classification, it is a first-generation ethanolamine-class H1-antihistamine (structurally similar to diphenhydramine), typically found as an adjunct component in multi-ingredient cold/allergy products rather than marketed as a standalone antihistamine.

Allergic urticaria's core pathology is mast cell histamine release acting through H1 receptors, and H1-antagonists are established first-line therapy for this condition. This gives the prediction reasonable mechanistic plausibility — but it is a **drug-class-level** inference (any H1-antihistamine would score similarly against urticaria-type diseases in the knowledge graph) rather than evidence specific to Phenyltoloxamine itself.

Notably, a lower-ranked prediction in this pack (pharyngitis, rank 6) is backed by an actual completed Phase 4 real-world trial (NCT00378144) of a Phenyltoloxamine-containing combination product (Sinutab), which is currently the strongest evidence in this evidence pack — stronger than the top-ranked allergic urticaria prediction, though it reflects combination-product data rather than monotherapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for allergic urticaria.

---

## Literature Evidence

Currently no related literature available for allergic urticaria.

---

## Singapore Market Information

Phenyltoloxamine currently has no product registrations in Singapore (market status: Not Marketed, 0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Note that a **Blocking** data gap (DG001) exists: TFDA/HSA-equivalent warnings and contraindications have not yet been retrieved, which prevents completion of an initial safety (S1) review for any predicted indication in this pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (allergic urticaria) has no clinical trial or literature support and rests solely on drug-class mechanism inference (L4). Combined with the drug's unregistered status in Singapore and a Blocking safety data gap, there is insufficient evidence to proceed at this time.

**To proceed, the following is needed:**
- Local regulatory package insert data — warnings and contraindications (DG001, Blocking)
- Confirmed mechanism of action data from DrugBank (DG002, High)
- Direct clinical or literature evidence specific to Phenyltoloxamine (not combination-product) for allergic urticaria
- Re-evaluation of the pharyngitis signal (rank 6, L3, Proceed with Guardrails) separately, as it currently carries the strongest real-world evidence in this pack despite a lower TxGNN score
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

