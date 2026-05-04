---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Amiloride
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

# Amiloride: From Hypertension and Edema to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC) in the distal renal tubule, traditionally used internationally for hypertension and fluid overload in conditions such as heart failure and liver cirrhosis — though it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, yet there are presently **0 clinical trials** and **0 publications** directly supporting this specific indication.
This candidate remains at the hypothesis-generation stage; mechanistic plausibility exists but is complicated by significant safety concerns related to drug accumulation in impaired renal function.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension and edema (potassium-sparing diuretic) — not registered in Singapore |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known pharmacological information, Amiloride is a potassium-sparing diuretic in the ENaC blocker class. It acts by binding to and blocking the epithelial sodium channel (ENaC) in the distal convoluted tubule and collecting duct of the kidney, reducing sodium reabsorption and secondarily retaining potassium. It is commonly used in combination with loop or thiazide diuretics to prevent hypokalemia.

Malignant hypertensive renal disease involves severely and acutely elevated blood pressure that causes rapid end-organ renal damage. When such conditions are accompanied by secondary hyperaldosteronism — a known compensatory response to renovascular compromise — ENaC channels are upregulated, creating a theoretically sound mechanistic rationale for ENaC blockade. Reducing sodium retention in this context could theoretically attenuate the hypertensive load and slow renal injury progression.

However, there is a critical opposing safety factor: acute renal injury in the malignant hypertension setting reduces glomerular filtration, and since Amiloride is predominantly renally excreted, drug accumulation and significantly elevated risk of life-threatening hyperkalemia become primary concerns. This double-edged mechanistic profile — plausible benefit on one hand, pharmacokinetic hazard on the other — explains why clinical evidence in this specific indication is absent and warrants caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

---

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

---

## Singapore Market Information

Amiloride is not currently registered in Singapore. There are no active product licenses on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or published literature directly supports Amiloride for malignant hypertensive renal disease (L5 — model prediction only), and the pharmacokinetic safety profile in acute renal injury raises a blocking concern that cannot be resolved without additional data.

**To proceed, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to strengthen the biological rationale and inform the mechanistic link analysis
- Safety data from the package insert (key warnings and contraindications), particularly regarding use in renal impairment and hyperkalemia risk
- Preclinical studies or case series examining ENaC inhibition specifically in the context of malignant hypertension or hypertensive emergency with renal involvement
- Pharmacokinetic/pharmacodynamic (PK/PD) data in patients with varying degrees of renal impairment, clarifying safe dose thresholds
- Assessment of whether any of the related higher-evidence indications (see Multi-Indication Summary below) could serve as a bridging study population

---

## Multi-Indication Summary

Given that this is a multi-indication evaluation (10 predicted indications were analyzed), the table below provides a consolidated overview to aid prioritisation.

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Clinical Trials | Literature | Decision |
|------|---------------------|-------------|---------------|-----------------|------------|----------|
| 1 | Malignant Hypertensive Renal Disease | 99.82% | L5 | 0 | 0 | Hold |
| 2 | Malignant Renovascular Hypertension | 99.82% | L4 | 0 | 1 | Research Question |
| 3 | Pulmonary Hypertension (Multifactorial) | 99.81% | L5 | 0 | 0 | Hold |
| 4 | Pulmonary Hypertension (Lung Disease/Hypoxia) | 99.81% | L5 | 0 | 20* | Hold |
| 5 | Braddock Syndrome | 99.75% | L5 | 0 | 0 | Hold |
| 6 | **Chronic Pulmonary Heart Disease** | 99.68% | **L3** | 0 | 5 | **Proceed with Guardrails** |
| 7 | Acute Pulmonary Heart Disease | 98.40% | L4 | 0 | 1 | Research Question |
| 8 | Primary Hereditary Glaucoma | 92.06% | L5 | 0 | 0 | Hold |
| 9 | Open-Angle Glaucoma | 87.41% | L5 | 0 | 0 | Hold |
| 10 | **Chronic Renal Failure Syndrome** | 85.53% | **L3** | 2 | 20 | **Proceed with Guardrails** |

> \* 20 publications retrieved for Pulmonary Hypertension (Lung Disease/Hypoxia), but content review indicates these are general hypoxia biology articles with no direct relevance to Amiloride use in this indication; evidence level remains L5.

**Prioritisation Recommendation:** Among all 10 indications, **Chronic Pulmonary Heart Disease (Rank 6)** and **Chronic Renal Failure Syndrome (Rank 10)** carry the strongest evidence bases (L3, "Proceed with Guardrails") and should be evaluated with dedicated full reports. **Malignant Renovascular Hypertension (Rank 2)** is a reasonable secondary research question given its mechanistic overlap with ENaC-mediated secondary aldosteronism.

---

> ⚠️ **Disclaimer:** This report is for research reference purposes only and does not constitute medical advice. All drug repurposing candidates require prospective clinical validation before any therapeutic application. All website pages and outputs must include a YMYL disclaimer in accordance with project guidelines.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

