---
layout: default
title: Fenofibric Acid
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 10
---

# Fenofibric Acid
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

# Fenofibric Acid: From Mixed Dyslipidemia to Cholesterol-Ester Transfer Protein Deficiency

## One-Sentence Summary

Fenofibric acid is the active metabolite of fenofibrate, a well-established fibrate-class lipid-lowering agent globally approved for mixed dyslipidemia and hypertriglyceridemia (marketed as Trilipix® in the US).
The TxGNN model predicts it may be effective for **Cholesterol-Ester Transfer Protein (CETP) Deficiency**, with **no clinical trials** and **no publications** currently supporting this specific direction.
Evidence remains at model-prediction only (L5), and this indication is currently classified as **Hold** pending further mechanistic and clinical investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mixed dyslipidemia / hypertriglyceridemia (FDA/EMA approved globally; not registered in Singapore) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 97.85% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on established pharmacological knowledge, fenofibric acid is the active form of fenofibrate and acts as a **PPARα (peroxisome proliferator-activated receptor alpha) agonist**. It upregulates lipoprotein lipase (LPL) to accelerate VLDL/TG clearance, suppresses apoC-III to reduce triglycerides, inhibits PCSK9 transcription to lower LDL-C, and increases apoA-I synthesis to raise HDL-C. As Trilipix®, it has been independently approved by the FDA for severe hypertriglyceridemia and mixed dyslipidemia.

CETP deficiency is a rare autosomal condition in which the cholesterol ester transfer protein — responsible for shuttling cholesterol esters from HDL to VLDL and LDL — is absent or non-functional. The result is markedly elevated HDL-C and paradoxically low LDL-C. Phenotypically, this profile partially overlaps with what fenofibric acid achieves pharmacologically (elevated HDL-C), though the underlying mechanisms are entirely distinct: PPARα-driven apoA-I synthesis versus impaired cholesterol ester exchange.

The TxGNN model likely captures the shared network proximity between fenofibric acid's PPARα targets and CETP-related lipid metabolism nodes in the knowledge graph. However, CETP deficiency's clinical significance remains scientifically debated — population studies (particularly in Japanese cohorts) suggest the phenotype may be cardioprotective or neutral rather than a true disease state requiring treatment. This renders the therapeutic rationale uncertain beyond a mechanistic curiosity, and no clinical or preclinical data exist to support this specific application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Fenofibric acid currently holds no product registrations with the Health Sciences Authority (HSA) of Singapore. The compound is not marketed in Singapore under any brand name or dosage form.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (97.85%), reflecting strong lipid-pathway network connectivity, but there is zero clinical or published evidence supporting fenofibric acid specifically in CETP deficiency — a condition whose pathological status and treatment need remain scientifically unresolved. The absence of Singapore registration adds a further regulatory barrier.

**To proceed, the following is needed:**
- Scientific consensus on whether CETP deficiency constitutes a disease state warranting pharmacological intervention (vs. a cardioprotective phenotype)
- Mechanistic studies characterising the interaction between PPARα activation and CETP pathway regulation
- At minimum, case series or observational evidence in CETP-deficient patients treated with fenofibrate/fenofibric acid
- MOA documentation from DrugBank (DG002) to support mechanistic link analysis
- Regulatory pathway assessment for fenofibric acid registration with HSA Singapore before any clinical application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

