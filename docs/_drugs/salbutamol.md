---
layout: default
title: Salbutamol
parent: 僅模型預測 (L5)
nav_order: 884
evidence_level: L5
indication_count: 10
---

# Salbutamol
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

# Salbutamol: From Asthma/Bronchospasm to Papillary Conjunctivitis

## One-Sentence Summary

> Salbutamol is a short-acting β2-adrenergic receptor agonist bronchodilator, classically used to relieve bronchospasm in asthma and other reversible airway obstruction (original indication data not captured in this evidence pack).
> The TxGNN model predicts it may be effective for **Papillary Conjunctivitis**,
> but **no clinical trials** and **no publications** currently support this specific direction — the prediction is model-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in evidence pack (data gap); Salbutamol is widely known clinically as a short-acting β2-agonist bronchodilator for asthma/reversible airway obstruction |
| Predicted New Indication | Papillary Conjunctivitis |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available (data gap DG002). Based on known information, Salbutamol is a short-acting β2-adrenergic receptor agonist commonly used to relax bronchial smooth muscle and relieve bronchospasm; its efficacy in respiratory conditions such as asthma is well established.

For the predicted indication, the model's own rationale states: *"No clinical trial or literature evidence supports this link; the high TxGNN score reflects only a knowledge-graph association — possibly an indirect connection via beta-adrenergic receptors present in ocular surface tissue — with no mechanistic validation data available."* Beta2-adrenergic receptors are known to be expressed in some ocular tissues, which offers a theoretical (not proven) rationale for the graph-level association, but this has not been tested in any dedicated study for papillary conjunctivitis.

Because there is neither corroborating trial data nor literature, this candidate should be treated as an unvalidated computational hypothesis rather than a clinically supported repurposing lead.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Salbutamol currently has **no marketing authorization registered** in Singapore (0 licenses; market status: Not Marketed). No product/dosage-form/indication data is available from `taiwan_regulatory.licenses`.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug interaction data were all flagged as data gaps in this evidence pack — notably DG001, a Blocking-severity gap for TFDA/HSA label warnings and contraindications required before any safety pre-assessment.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for papillary conjunctivitis is very high, but this is a pure model prediction (Evidence Level L5) with zero supporting clinical trials or literature, no mechanistic validation, and it comes from a drug with no current Singapore market registration and unresolved Blocking-severity safety data gaps. There is insufficient evidence to move this candidate beyond hypothesis stage.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001 — Blocking; required before any S1 safety pre-assessment)
- DrugBank-sourced mechanism of action data (DG002 — High priority; needed for mechanistic relevance analysis)
- Targeted preclinical/mechanistic studies on β2-agonist activity in ocular surface/conjunctival tissue specific to papillary conjunctivitis
- Confirmation of original indication and regulatory history for Salbutamol, currently absent from `drug.original_indications` and `taiwan_regulatory.licenses`

*Note: Other candidates in this same evidence pack (e.g., bronchitis, obstructive lung disease) carry substantially stronger evidence levels (L1) and clinical trial support, but bronchitis remains a "Research Question" and obstructive lung disease reflects an already-established indication rather than a novel repurposing opportunity — neither displaces papillary conjunctivitis as the top-ranked TxGNN candidate evaluated here.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

