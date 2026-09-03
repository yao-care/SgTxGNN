---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 848
evidence_level: L5
indication_count: 10
---

# Ravulizumab
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

# Ravulizumab: From PNH/aHUS to Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency

## One-Sentence Summary

> Ravulizumab is a long-acting anti-C5 terminal complement inhibitor, currently used for paroxysmal nocturnal hemoglobinuria (PNH) and atypical hemolytic uremic syndrome (aHUS).
> The TxGNN model predicts it may be effective for **autosomal recessive severe congenital neutropenia due to G6PC3 deficiency**,
> but this ranks as **L5 evidence** — a model prediction only, with **no clinical trials** and **no literature** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Paroxysmal Nocturnal Hemoglobinuria (PNH), atypical Hemolytic Uremic Syndrome (aHUS) *(inferred from evidence pack rationale; not confirmed via Singapore licensing data, as drug is unregistered)* |
| Predicted New Indication | Autosomal recessive severe congenital neutropenia due to G6PC3 deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, DrugBank-sourced mechanism of action data is not available (data gap). Based on the repurposing rationale captured in this evidence pack, Ravulizumab is an eculizumab derivative that binds complement protein C5, blocking its cleavage into C5a and C5b and thereby preventing terminal complement complex (C5b-9) formation. It is used clinically for PNH and aHUS — both diseases driven by uncontrolled complement activation causing hemolysis and/or thrombotic microangiopathy (TMA).

The predicted indication, G6PC3-deficient severe congenital neutropenia, is mechanistically distinct. Its neutropenia arises from glucose-6-phosphatase catalytic subunit 3 deficiency, which causes endoplasmic reticulum stress and increased neutrophil apoptosis — a cell-intrinsic metabolic defect, not a complement-mediated process. There is no established biological pathway linking C5 inhibition to correction of this apoptotic defect.

Given this mismatch, the evidence pack itself flags that the high TxGNN score likely reflects proximity between "immunodeficiency/hematologic disease" nodes in the knowledge graph rather than genuine mechanistic similarity. Among the 10 predicted indications in this batch, **primary hyperoxaluria (rank 3)** shows comparatively higher mechanistic plausibility, since oxalate-related nephropathy can present with TMA-like renal injury that theoretically overlaps with complement-mediated pathology — though this too remains unconfirmed by trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

Currently no related literature available

---

## Singapore Market Information

Ravulizumab is not currently registered in Singapore (0 licenses on file). No approved indication, dosage form, or authorization data is available for this jurisdiction.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: Data gap DG001 flags that TFDA/HSA label warnings and contraindications are currently missing, which blocks progression to the S1 safety pre-assessment stage.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has no clinical trial or literature support (L5 — model prediction only), and the drug's own mechanistic profile (terminal complement inhibition) does not align biologically with the proposed indication's pathophysiology (ER stress-driven neutrophil apoptosis). The drug is also unregistered in Singapore, and safety documentation (warnings/contraindications) is a blocking data gap (DG001).

**To proceed, the following is needed:**
- Confirmed MOA data from DrugBank/regulatory sources (DG002)
- TFDA/HSA label warnings and contraindications (DG001, blocking)
- Preclinical or mechanistic studies testing complement pathway involvement in G6PC3-deficient neutropenia
- If pursuing this program, consider re-prioritizing toward **primary hyperoxaluria** (rank 3), which has a more defensible TMA-complement mechanistic link, despite currently lacking trial/literature evidence
- Singapore market entry pathway assessment, given current unregistered status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

