---
layout: default
title: Maribavir
parent: 僅模型預測 (L5)
nav_order: 631
evidence_level: L5
indication_count: 10
---

# Maribavir
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

# Maribavir: From Cytomegalovirus (CMV) Infection to Bronchitis

## One-Sentence Summary

Maribavir is a narrow-spectrum antiviral (UL97 kinase inhibitor) associated with cytomegalovirus (CMV) infection/CMV retinitis management in immunocompromised patients — this is inferred from the evidence pack's own analyst notes, since the formal `original_indications` and `original_moa` fields are marked as data gaps. The TxGNN model's top-ranked new-indication signal for this drug is **Bronchitis** (score 87.79%), but this candidate is supported by **zero clinical trials** and **zero publications**, and the evidence pack's own mechanistic review explicitly flags the biological rationale as weak. This is a model-score-only (L5) signal that has not progressed past initial screening (decision stage S0).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not confirmed in evidence pack (`original_indications` is empty); internal analyst notes reference "CMV infection / CMV retinitis" as Maribavir's known indication — treat as unverified until sourced from a primary label |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 87.79% |
| Evidence Level | L5 (model prediction only, no supporting clinical trials or literature) |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for Maribavir is a **flagged data gap (DG002, High severity)** in this evidence pack. What is available comes only from the analyst rationale attached to the predicted indications, which consistently describes Maribavir as a **narrow-spectrum anti-CMV UL97 kinase inhibitor**, with its known relevant indication being CMV infection/retinitis (referenced when discussing candidates #2 and #4 below).

Critically, the evidence pack's own mechanistic assessment for this top candidate does **not** support the prediction. The recorded rationale states:

> "無合理機轉關聯。Maribavir 為窄譜抗CMV UL97激酶抑制劑，對一般（多為病毒性/細菌性）支氣管炎病原無已知活性；即使考慮免疫低下患者CMV肺部感染，'bronchitis'亦非CMV典型表現型，機轉推論薄弱。"

In plain terms: Maribavir's antiviral activity is specific to CMV replication via UL97 kinase inhibition. It has no known activity against the typical viral or bacterial pathogens that cause bronchitis, and even in immunocompromised patients where CMV pulmonary disease is a concern, "bronchitis" is not a typical clinical presentation of CMV disease. **This is not being presented as a mechanistically well-supported repurposing candidate** — it is a model-score-driven signal that failed the plausibility check applied during evidence review, consistent with its "Hold" recommendation and S0 (earliest) decision stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Maribavir currently has **no registered pharmaceutical product license** in Singapore (0 registrations on file; market status: not marketed). No authorization number, product name, dosage form, or approved indication text is available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data are all marked as data gaps in this evidence pack; a DDI query for Maribavir returned no results.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This candidate is an L5, screening-stage (S0) signal supported only by a TxGNN model score, with no clinical trials, no literature, and — per the evidence pack's own mechanistic review — a weak/implausible biological rationale linking Maribavir's narrow anti-CMV activity to bronchitis. In addition, safety review cannot proceed at all: the missing TFDA/HSA label warnings and contraindications are flagged as a **Blocking** data gap (DG001), which by itself prevents entry into initial safety assessment (S1) regardless of efficacy evidence.

**To proceed, the following is needed:**
- TFDA/HSA-equivalent package insert (warnings, contraindications) — currently blocking (DG001)
- Confirmed mechanism of action from DrugBank API — currently a data gap (DG002)
- Verified original/registered indication for Maribavir (the "CMV infection" association used above is inferred from internal notes, not a confirmed evidence-pack field, and should be sourced from a primary regulatory label)
- Independent confirmation of clinical or preclinical rationale connecting anti-CMV kinase inhibition to bronchitis before any advancement beyond S0

**Note for model QA:** All 10 top-ranked TxGNN candidates for this drug in this evidence pack received a "Hold" recommendation with similarly weak mechanistic rationale. Two of them (rank 2: severe nonproliferative diabetic retinopathy; rank 4: diabetic retinopathy) are explicitly flagged by the analyst notes as likely **false positives from knowledge-graph entity confusion** between "CMV retinitis" (Maribavir's actual associated indication) and "diabetic retinopathy" (an unrelated metabolic/vascular disease). This suggests a possible entity-resolution issue in the underlying knowledge graph for this drug that may warrant review at the model/data level before further candidates from this node are evaluated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

