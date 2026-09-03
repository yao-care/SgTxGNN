---
layout: default
title: Sotalol
parent: 僅模型預測 (L5)
nav_order: 922
evidence_level: L5
indication_count: 10
---

# Sotalol
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

# Sotalol: From Cardiac Arrhythmia to Sick Sinus Syndrome 2, Autosomal Dominant

## One-Sentence Summary

> Sotalol is a class III antiarrhythmic/beta-blocker long used for atrial fibrillation and ventricular arrhythmias.
> The TxGNN model's top-ranked prediction links it to **Sick Sinus Syndrome 2, Autosomal Dominant**,
> but this association has **no supporting clinical trials or literature**, and the mechanistic rationale itself flags a potential safety conflict rather than a therapeutic opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not captured in registration data; sotalol is clinically established for atrial fibrillation and ventricular arrhythmias (general pharmacological knowledge, not extracted from structured records) |
| Predicted New Indication | Sick Sinus Syndrome 2, Autosomal Dominant |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for sotalol is not available in this Evidence Pack (flagged as data gap DG002). Based on established pharmacology, sotalol combines non-selective beta-adrenergic blockade with cardiac potassium-channel (IKr) blockade, producing negative chronotropic effects and prolonged repolarization. This profile underlies its established use in suppressing atrial fibrillation/flutter and ventricular tachyarrhythmias — a mechanism reflected throughout the clinical trial and literature evidence in this Evidence Pack (e.g., NCT00007605, NCT05279833, PMID 37485722).

Sick Sinus Syndrome 2 is a genetic disorder of sinoatrial node dysfunction that typically presents as pathological **bradycardia**. Sotalol's own negative chronotropic action runs counter to this disease process rather than supporting it. The repurposing rationale attached to this candidate states this explicitly: sotalol "may aggravate bradycardia in patients with sinus node dysfunction," describing the relationship as a **mechanistic conflict, not a treatment opportunity**.

Given the absence of any clinical trial or literature evidence, the high TxGNN score for this candidate should be read as a graph-embedding pattern match rather than a validated therapeutic hypothesis. This is effectively a **safety-signal candidate**, not a repurposing opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Sotalol currently holds no valid registration in Singapore (0 registrations, market status: Not Marketed). No authorization records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: The specific safety concern for this candidate — potential worsening of bradycardia in sinus node dysfunction — is discussed above under mechanistic rationale, as it originates from the repurposing analysis rather than the drug's general safety dataset, which remains a data gap.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked candidate has no clinical trial or literature support (Evidence Level L5), and its proposed mechanism conflicts with the target disease's pathophysiology — sotalol's negative chronotropic effect could worsen, rather than treat, bradycardia in sinus node dysfunction. This should be treated as a potential contraindication signal rather than a repurposing lead.

**To proceed, the following is needed:**
- Confirmed mechanism of action (MOA) data from DrugBank to complete a formal mechanistic evaluation (DG002)
- TFDA/HSA label warnings and contraindications, currently a **Blocking** data gap (DG001) preventing entry into safety pre-screening (S1)
- Consider redirecting evaluation effort to other candidates in this Evidence Pack with substantially stronger support — notably **rank 4 (stroke disorder / atrial fibrillation)**, which is backed by 20+ clinical trials and 20 publications directly involving sotalol, rather than pursuing this top-ranked but mechanistically contradictory candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

