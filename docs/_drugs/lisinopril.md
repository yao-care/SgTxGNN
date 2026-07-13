---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 556
evidence_level: L5
indication_count: 10
---

# Lisinopril
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

# Lisinopril: From Hypertension and Heart Failure to Posterolateral Myocardial Infarction

## One-Sentence Summary

Lisinopril is an angiotensin-converting enzyme (ACE) inhibitor widely used for hypertension, heart failure, and post-myocardial infarction cardiac protection, and is one of the most extensively studied cardiovascular agents globally.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction** (a specific anatomical MI subtype), with **no dedicated clinical trials** registered but strong mechanistic support from large class-effect RCTs (GISSI-3, ISIS-4) demonstrating ACE inhibitor benefit broadly across MI presentations.
Across the full 10-indication prediction set, **chronic pulmonary heart disease (Cor Pulmonale, rank 9)** carries the highest direct Lisinopril-specific evidence, with two clinical studies directly examining this drug in that population.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension; Heart failure; Post-MI cardiac protection |
| Predicted New Indication | Posterolateral Myocardial Infarction |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Lisinopril inhibits ACE, blocking the conversion of angiotensin I to angiotensin II. This reduces systemic vasoconstriction, aldosterone secretion, and — critically for myocardial injury — blunts the pathological RAAS cascade activated during and after infarction. ACE is highly expressed in the myocardium and coronary vasculature, making it a biologically plausible target in any MI anatomical subtype.

Posterolateral myocardial infarction typically results from occlusion of the left circumflex artery (LCx) or a dominant right coronary artery (RCA), injuring the lateral and posterior left ventricular walls. Like all large MI events, this activates RAAS acutely, driving left ventricular remodelling, fibrosis, and progression to heart failure. The landmark GISSI-3 trial (n = 19,394) and ISIS-4 trial (n = 58,050) established that ACE inhibitors started early post-MI significantly reduce 30-day and 6-week mortality — establishing a class effect that applies across infarction territories, including posterior and lateral wall events. The TxGNN model's high prediction score for this indication reflects this well-characterised mechanistic link.

The critical evidence gap is that the posterolateral anatomical subtype has never been the subject of a dedicated, independently powered clinical trial for Lisinopril. Current support rests entirely on extrapolation from broad MI population trials and mechanistic inference — hence an L4 classification. Of note, the strongest direct Lisinopril evidence among all 10 TxGNN predictions in this pack is for **chronic pulmonary heart disease / Cor Pulmonale (rank 9, L3)**, where two clinical studies (PMID 17047621; PMID 14524095) directly examined Lisinopril's effect on pulmonary arterial pressure and right ventricular function. This finding merits parallel evaluation alongside the top-ranked prediction.

---

## Clinical Trial Evidence

Currently no clinical trials dedicated to Lisinopril in posterolateral myocardial infarction are registered.

> The mechanistic basis for this prediction rests on class-level evidence: GISSI-3 (lisinopril arm, n ≈ 9,700) and ISIS-4 (captopril, n ≈ 29,000) are the most relevant RCTs establishing ACE inhibitor benefit post-MI. These trials did not stratify results by anatomical MI subtype.

---

## Literature Evidence

Currently no literature directly addressing Lisinopril in posterolateral myocardial infarction is available.

---

## Singapore Market Information

Lisinopril is not currently registered in Singapore. No product authorisations were identified in the regulatory database.

> Lisinopril holds approved status in major regulatory jurisdictions worldwide (US FDA, EMA, UK MHRA, Japan PMDA) as a first-line treatment for hypertension, heart failure, and post-MI management. The absence of a Singapore registration likely reflects a commercial market-access decision rather than any safety or efficacy concern. Any clinical development or repurposing pathway would require a new regulatory submission to the Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Mechanistic Safety Signal Identified in This Evidence Pack**: The TxGNN prediction for **malignant renovascular hypertension (rank 6)** carries a critical contraindication flag. In patients with bilateral renal artery stenosis or a functionally solitary kidney, ACE inhibition removes the angiotensin II–dependent efferent arteriolar tone that sustains GFR — this can precipitate acute renal failure. The TxGNN model's high score for this entity reflects mechanistic overlap with hypertension/renal disease phenotypes but does not detect this contraindicated clinical scenario. Renal function and serum potassium should be assessed within 1–2 weeks of Lisinopril initiation in any hypertensive-with-renal-disease context.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Lisinopril's ACE inhibitor class effect in post-MI care is one of the best-established mechanisms in cardiovascular medicine, making the TxGNN prediction for posterolateral MI mechanistically credible; however, the absence of any subtype-specific trial data limits this to L4 evidence, and the zero Singapore regulatory registrations mean significant market access work would be required before any clinical application.

**To proceed, the following is needed:**

- Obtain the full package insert / SmPC to confirm approved indications, warnings, and contraindications for Lisinopril in a relevant reference market (e.g., US FDA label, EMA SmPC)
- Query DrugBank API (DB00722) to retrieve full MOA, pharmacokinetics, and toxicity data — currently a high-severity data gap (DG002)
- Assess whether GISSI-3 or ISIS-4 published subgroup analyses stratified by infarction territory (posterior/lateral wall) to determine whether L1 class-effect evidence can be leveraged
- Prioritise a focused systematic review of **chronic pulmonary heart disease (rank 9, L3)**: evaluate PMID 17047621 (Pribylov 2006, prospective study of Lisinopril 10 mg/day in COPD + IHD heart failure patients) and PMID 14524095 (Verbitskiy 2003, Lisinopril in chronic Cor Pulmonale) for study quality, sample size, and generalisability — this indication has the highest actionable direct evidence in the current pack
- Screen prospective patients for bilateral renal artery stenosis before initiating Lisinopril in any hypertensive-with-renal-disease setting (see rank 6 safety signal)
- Define a monitoring protocol: serum creatinine, eGFR, serum potassium, and blood pressure at baseline and at 1–2 weeks post-initiation
- Initiate a Singapore HSA regulatory pre-consultation if market registration is a strategic objective
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

