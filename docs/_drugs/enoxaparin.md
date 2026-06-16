---
layout: default
title: Enoxaparin
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Enoxaparin
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

# Enoxaparin: From Venous Thromboembolism to Thrombophilia due to Protein C Deficiency (Autosomal Recessive)

## One-Sentence Summary

Enoxaparin is a low molecular weight heparin (LMWH) internationally established for the prevention and treatment of venous thromboembolism, deep vein thrombosis, pulmonary embolism, and acute coronary syndromes.
The TxGNN model predicts it may be effective for **Thrombophilia due to Protein C Deficiency, Autosomal Recessive**, with a prediction score of **99.58%**.
However, the current dataset contains **zero clinical trials** and **zero published literature** specific to this indication, limiting the evidence to Level 5 (model prediction only) — though it is worth noting that LMWH use in Protein C deficiency is already an internationally recognized clinical practice, making this less a true repurposing than a formalization of existing off-label use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Internationally used for VTE prevention and treatment (not registered in Singapore) |
| Predicted New Indication | Thrombophilia due to Protein C Deficiency, Autosomal Recessive |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not available in the current data package. Based on established pharmacological knowledge, Enoxaparin is a low molecular weight heparin that acts primarily by binding to antithrombin III, which then accelerates the inactivation of Factor Xa and, to a lesser extent, Factor IIa (thrombin). This interrupts both the intrinsic and extrinsic coagulation cascades, producing a predictable anticoagulant effect without requiring laboratory monitoring in most standard dosing scenarios.

Protein C is a critical natural anticoagulant. When activated by the thrombin–thrombomodulin complex on endothelial surfaces, activated Protein C degrades Factors Va and VIIIa, thereby suppressing further thrombin generation. In autosomal recessive Protein C deficiency, both PROC gene copies are non-functional, resulting in near-complete loss of this regulatory pathway. Clinically, this manifests as neonatal purpura fulminans, recurrent venous thromboembolism, and warfarin-induced skin necrosis — a severe, life-threatening phenotype.

The mechanistic rationale for Enoxaparin in this setting is straightforward: by directly suppressing thrombin generation via anti-Xa/IIa inhibition, it compensates upstream for the absent Protein C brake on the coagulation cascade. This approach is already practiced internationally as part of acute thrombosis management and bridge therapy in Protein C-deficient patients. The TxGNN model's high confidence score (99.58%) likely reflects this strong and biologically direct connection. The principal limitation is not mechanistic plausibility, but rather the complete absence of prospective clinical trial data in this specific genetic subtype in the current dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite strong mechanistic plausibility and established real-world use of LMWH in Protein C deficiency, the current dataset contains no clinical trials and no publications specific to this genetic indication (L5 evidence), and Enoxaparin is not registered in Singapore — making any formal deployment premature without further evidence gathering and regulatory clarification.

**To proceed, the following is needed:**

- **Prescribing information**: Retrieve the HSA-registered or internationally approved Enoxaparin product labelling (SmPC / USPI) to document confirmed indications, key warnings, contraindications, and dosing recommendations
- **Targeted literature review**: Conduct a dedicated search in PubMed, Orphanet, and ISTH guidelines for LMWH use in autosomal recessive Protein C deficiency — including neonatal purpura fulminans protocols and long-term anticoagulation strategies
- **Regulatory pathway**: Clarify the applicable pathway in Singapore for use in an ultra-rare inherited thrombophilia — off-label prescribing, compassionate use, or HSA pre-submission consultation
- **Specialist consultation**: Engage haematologists with expertise in inherited thrombophilias to define clinical positioning of Enoxaparin versus alternatives (Protein C concentrate, fresh frozen plasma, DOACs in older patients)
- **Paediatric safety plan**: Given that the most severe phenotype presents in neonates, a dedicated safety monitoring protocol for this high-risk population is essential before any clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

