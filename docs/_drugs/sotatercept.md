---
layout: default
title: Sotatercept
parent: 僅模型預測 (L5)
nav_order: 923
evidence_level: L5
indication_count: 10
---

# Sotatercept
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

# Sotatercept: From Pulmonary Arterial Hypertension to Acute Lymphoblastic Leukemia

## One-Sentence Summary

Sotatercept is an Activin receptor IIA-Fc fusion protein internationally approved for pulmonary arterial hypertension (PAH); it is **not yet registered in Singapore**. TxGNN's top-ranked prediction flags **Acute Lymphoblastic Leukemia** with a 99.78% score, but this is a **model-only signal with zero supporting clinical trials or literature**, and the evidence pack's own mechanistic review judges it as likely knowledge-graph noise rather than a genuine repurposing hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary arterial hypertension (PAH) — based on known clinical use; not present in Singapore regulatory data, as the drug has no local approval history |
| Predicted New Indication | Acute Lymphoblastic Leukemia (disease) |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only, no clinical trials or literature) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Sotatercept is currently unavailable in this evidence pack (data gap DG002). Based on known information, Sotatercept is an Activin receptor IIA-Fc fusion protein that inhibits Activin/GDF ligands (TGF-β superfamily), modulating erythropoiesis and vascular smooth muscle proliferation; it is clinically approved for pulmonary arterial hypertension.

The evidence pack's own mechanistic review for this top-ranked candidate is explicit that **this prediction is not well supported**: Acute Lymphoblastic Leukemia arises from malignant transformation of hematopoietic/lymphoid progenitor cells (e.g., BCR-ABL and related pathways), which has no known mechanistic overlap with the Activin/GDF signaling axis targeted by Sotatercept. The rationale text itself concludes this is likely **knowledge-graph node-proximity noise** rather than a biologically grounded hypothesis.

This pattern extends across most of the other nine predicted indications in this batch — diabetic retinopathy, diabetic cataract, HER2+ breast carcinoma, and a cluster of four urothelial/transitional cell carcinoma variants (ranks 7–10) all show no mechanistic link and are explicitly flagged as likely embedding-similarity artifacts. The one partial exception is **rank 4, drug-induced osteoporosis**, where Activin A's known role in osteoclast differentiation gives a plausible (though still unverified) mechanistic rationale — but even this candidate has no supporting trials or literature in the current dataset and is scored only as a "Research Question," not an actionable candidate.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Sotatercept currently has no marketing authorization in Singapore (0 registrations); no license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

*Note: TFDA-equivalent package insert warnings/contraindications for Sotatercept could not be retrieved (data gap DG001, severity: Blocking), which prevents this candidate from advancing to the S1 safety pre-assessment stage.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (Acute Lymphoblastic Leukemia) has no clinical trial or literature support, is explicitly assessed by the evidence pack as lacking biological plausibility, and cannot pass safety pre-screening due to a blocking data gap in TFDA-equivalent warning/contraindication data. Evidence level is L5 — model prediction only.

**To proceed, the following is needed:**
- TFDA (or equivalent) package insert warnings and contraindications (data gap DG001, blocking) — required before any S1 safety evaluation
- Confirmed mechanism of action data via DrugBank API (data gap DG002)
- If pursuing repurposing research at all, prioritize the more biologically plausible drug-induced osteoporosis hypothesis (rank 4) over the top-scored but mechanistically unsupported ALL prediction, and seek independent literature/trial evidence before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

