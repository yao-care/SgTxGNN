---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Atenolol
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

# Atenolol: From Hypertension & Angina Pectoris to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a highly β1-selective adrenergic blocker with a long-established role in treating hypertension and angina pectoris, widely used in cardiovascular medicine for decades.
The TxGNN model predicts it may be effective for **Posterolateral Myocardial Infarction** (TxGNN rank #2,482 among all drug–disease pairs), a specific anatomical subtype of MI involving the circumflex or right coronary artery territory.
However, **no clinical trials and no publications** directly address this specific subtype indication, meaning the prediction rests entirely on mechanistic class-effect inference and model scoring at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, angina pectoris (no Singapore registration on record) |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on known clinical pharmacology, atenolol is a cardioselective β1-adrenergic receptor antagonist with minimal β2 activity at therapeutic doses. It reduces heart rate, myocardial contractility, and oxygen demand by competitively blocking catecholamine binding at β1 receptors in the heart — actions that are broadly protective across all myocardial ischaemia contexts.

Posterolateral MI is caused by occlusion of the circumflex artery (Cx) or a dominant right coronary artery (RCA), producing ischaemia in the lateral and inferior-posterior walls of the left ventricle. The pathophysiology shares the same final common pathway as all MI subtypes: sympathetic hyperactivation, catecholamine surge, increased myocardial oxygen demand, and progressive ventricular remodelling. Beta-blockers as a class are well-supported in post-MI care regardless of infarction territory, and the TxGNN knowledge graph likely captures this mechanistic continuity across MI anatomical subtypes.

The specific gap here is that no clinical trial has enrolled patients stratified for *posterolateral* MI as a distinct indication. The TxGNN prediction therefore reflects a pharmacologically plausible class-effect extrapolation rather than a directly tested hypothesis. Until subtype-specific evidence exists, this remains a research-stage prediction.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

---

## Singapore Market Information

Atenolol has no registered products in Singapore. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug interaction data were not retrievable for this report. Obtaining the full prescribing information from a regulatory source (e.g., TFDA, EMA, or FDA label) is a prerequisite before any clinical use assessment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.87%) for atenolol in posterolateral MI, which is pharmacologically coherent given that β1-blockers reduce post-MI sympathetic overactivation and ventricular remodelling across all infarction territories. However, there is no direct clinical trial or published literature specifically addressing this anatomical MI subtype, and Singapore has no registered atenolol products to reference for safety labelling — together these gaps preclude moving beyond a research question at this stage.

**To proceed, the following is needed:**

- **Mechanism of action data:** Retrieve atenolol MOA from DrugBank API (DrugBank ID: DB00335) to formally document β1-selectivity profile and known receptor binding kinetics
- **Safety labelling:** Download and parse the TFDA or FDA prescribing information PDF to populate key warnings, contraindications, and clinically significant drug interactions
- **Subtype-specific literature search:** Conduct a targeted PubMed/EMBASE search combining "atenolol" with "posterolateral infarction", "circumflex artery occlusion", and "lateral wall MI" to confirm absence of evidence or identify any overlooked studies
- **Class-effect evidence review:** Assess whether large beta-blocker post-MI RCTs (e.g., COMMIT, CAPRICORN) enrolled patients with posterolateral MI and whether subgroup analyses are available
- **Singapore regulatory pathway:** If evidence strengthens, evaluate whether atenolol's non-marketed status in Singapore represents a gap to be filled or a reason to consider an already-registered alternative beta-blocker (e.g., metoprolol, bisoprolol)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

