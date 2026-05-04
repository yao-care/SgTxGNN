---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Irbesartan
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

# Irbesartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Irbesartan is an angiotensin II receptor blocker (ARB) widely used in clinical practice for hypertension and diabetic nephropathy. The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** with a high confidence score of **99.31%**, though currently there are **no registered clinical trials** and **no direct supporting publications** for this specific indication — the prediction is primarily mechanistically driven.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; diabetic nephropathy in Type 2 diabetes (known clinical use; no Singapore HSA registration on record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 (Mechanistic reasoning; no dedicated clinical studies) |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is unavailable from the data source. Based on established pharmacology, Irbesartan is an Angiotensin II Type 1 (AT1) receptor antagonist. By selectively blocking AT1 receptors, it prevents angiotensin II (AngII) from triggering vasoconstriction, aldosterone release, and pro-fibrotic signalling — lowering systemic blood pressure and shielding the kidneys from pressure- and AngII-mediated injury.

Malignant hypertensive renal disease sits precisely at the intersection of these mechanisms. In this condition, severely elevated circulating AngII drives intense efferent and afferent arteriolar vasoconstriction, raising intraglomerular hydraulic pressure and accelerating glomerulosclerosis and tubular fibrosis. AT1 blockade directly interrupts this cascade: reducing glomerular capillary hypertension, suppressing TGF-β–mediated extracellular matrix deposition, and slowing nephron loss. The TxGNN mechanistic rationale notes that "malignant hypertensive renal disease is precisely an AngII-driven glomerular injury model, making the mechanistic fit very high."

In broader clinical practice, ARBs — including Irbesartan — are already guideline-recommended for hypertensive nephropathy. The extension to the "malignant" subtype (characterised by rapid-onset, accelerated end-organ damage) is mechanistically coherent. However, this specific disease subtype lacks dedicated prospective evidence, placing the prediction at Evidence Level L4 rather than allowing immediate clinical translation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Irbesartan currently holds no marketing authorizations with the Singapore Health Sciences Authority (HSA). There are no registered products on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert warnings, contraindications, and drug interaction data were not available at the time of this report (Data Gaps DG001 and DG002). These must be resolved before any clinical or regulatory decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic case for Irbesartan in malignant hypertensive renal disease is internally consistent and scientifically plausible — AT1 antagonism directly addresses the AngII-driven pathophysiology of the disease. However, the complete absence of dedicated clinical trials, direct supporting literature, and Singapore regulatory data means the evidence base is insufficient to advance beyond a research hypothesis at this stage.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001:** Retrieve package insert warnings and contraindications from an official source (e.g., EMA SmPC or FDA label) to complete the safety profile
- **Resolve Data Gap DG002:** Query DrugBank API for full mechanism of action data to strengthen the mechanistic analysis
- **Literature expansion:** Conduct a systematic search specifically targeting ARBs in hypertensive emergency/malignant hypertension nephropathy (search terms: "ARB malignant hypertension kidney", "irbesartan hypertensive emergency renal")
- **Disease coding clarification:** Confirm ICD-10 / OMOP mapping for "malignant hypertensive renal disease" and check whether published studies use alternative terminology (e.g., "hypertensive crisis nephropathy", "accelerated hypertension renal damage")
- **Research question formulation:** If literature review yields supporting preclinical data, define a focused research question suitable for a retrospective cohort study or registry analysis using existing hypertension databases
- **Market pathway assessment:** Given that Irbesartan is not registered in Singapore, a regulatory pathway analysis (new indication extension or import approval) would be required before any clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

