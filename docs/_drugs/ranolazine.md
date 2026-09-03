---
layout: default
title: Ranolazine
parent: 僅模型預測 (L5)
nav_order: 845
evidence_level: L5
indication_count: 10
---

# Ranolazine
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

# Ranolazine: From Chronic Angina to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

> Ranolazine is a piperazine derivative used as a second-line treatment for chronic stable angina.
> The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
> but this prediction is currently supported by **no clinical trials and no literature** — it is a pure knowledge-graph association with no known mechanistic basis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic angina pectoris (per literature; no Singapore license data available) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for ranolazine is not available in this evidence pack (DrugBank query pending). Based on literature identified elsewhere in this pack, ranolazine's known pharmacology involves inhibition of the late cardiac sodium current (late I<sub>Na</sub>), and it is used clinically as second-line therapy for stable, poorly controlled chronic angina.

NSIAD, by contrast, is caused by a gain-of-function mutation in the renal V2 vasopressin receptor, leading to constitutive receptor activation independent of vasopressin. This pathway has no known overlap with cardiac sodium channel modulation. The model's own rationale field explicitly states there is no known mechanistic path connecting late I<sub>Na</sub> inhibition to V2-receptor-driven antidiuresis.

No clinical trials or publications in this evidence pack address ranolazine in the context of NSIAD or any related water-balance disorder. Taken together, this top-ranked prediction appears to be a knowledge-graph artifact rather than a biologically plausible repurposing candidate, and should not be advanced without independent mechanistic or preclinical validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Ranolazine is not currently registered in Singapore (0 authorizations on file). No product license, dosage form, or approved indication data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN similarity score (99.65%), the top-ranked prediction (NSIAD) has no supporting clinical trials, no supporting literature, and the model's own rationale confirms no known mechanistic link — this is L5 evidence (model prediction only). Combined with the drug's unregistered status in Singapore, there is no basis to advance this candidate at this time.

**To proceed, the following is needed:**
- Confirm ranolazine's mechanism of action via DrugBank API (DG002, High severity)
- Obtain HSA/regulatory label warnings and contraindications before any safety (S1) review can begin (DG001, Blocking)
- Independent mechanistic or preclinical evidence linking late I<sub>Na</sub> inhibition to V2-receptor-mediated antidiuresis, if this hypothesis is to be pursued further
- Consider evaluating lower-ranked candidates with stronger evidence instead — e.g., rank 9 "headache disorder" reached L4 evidence (S1, Research Question) with 3 supporting publications, including a 2025 case report and a 2025 FAERS pharmacovigilance study, and has a plausible sodium-channel-mediated neuronal excitability rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

