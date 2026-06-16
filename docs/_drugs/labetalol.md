---
layout: default
title: Labetalol
parent: 僅模型預測 (L5)
nav_order: 515
evidence_level: L5
indication_count: 10
---

# Labetalol
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

# Labetalol: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Labetalol is a combined alpha-1 and non-selective beta-adrenergic blocker, clinically established for hypertension management and hypertensive emergencies.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with **0 clinical trials** and **2 case report publications** currently supporting this direction.
Overall evidence is limited to mechanistic rationale and incidental case observations, warranting a hold pending further dedicated investigation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Hypertensive Emergency |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank source. Based on established pharmacological knowledge, Labetalol belongs to the combined alpha-1 / non-selective beta-adrenergic blocker class. Its antihypertensive action operates through two complementary pathways: alpha-1 blockade reduces peripheral vascular resistance by relaxing arteriolar smooth muscle, while beta-blockade decreases heart rate and cardiac output. This dual mechanism makes it effective for rapid blood pressure reduction in hypertensive crises, including intravenous administration in emergency settings.

Malignant renovascular hypertension is a severe, end-organ-threatening condition arising from renal artery stenosis, characterised by markedly elevated blood pressure and excessive renin-angiotensin-aldosterone system (RAAS) activation. Labetalol's beta-blockade component can suppress renin release from juxtaglomerular cells, theoretically interrupting the RAAS feedback loop. Combined with alpha-1 mediated vasodilation, this provides a mechanistically rational dual-target approach specifically relevant to the renovascular pathophysiology driving this condition.

The two retrieved publications each describe patients with malignant hypertension involving renal vascular abnormalities, in which labetalol was used for acute blood pressure control. While neither study was designed to formally evaluate labetalol for this specific indication, both cases demonstrate clinical feasibility. An important caution is that labetalol clearance may be reduced in renal impairment — a common comorbidity in this patient population — requiring careful dose titration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case Report | The Medical Journal of Australia | 20-year-old male with hallucinogenic drug-induced vasculitis presenting as malignant hypertension; renal angiography showed arteritic changes and renal cortical infarction. Labetalol achieved impressive initial blood pressure control; prednisone resolved the arteritis. |
| [15113447](https://pubmed.ncbi.nlm.nih.gov/15113447/) | 2004 | Case Report | BMC Nephrology | 18-month-old child with hyponatremic hypertensive syndrome (HHS) secondary to renovascular disease, presenting as malignant hypertension — a rare paediatric manifestation. Highlights the clinical complexity of managing malignant renovascular hypertension across age groups. |

---

## Singapore Market Information

Labetalol is currently **not registered** in Singapore. No product authorisations, approved indications, or dosage forms are on record with HSA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Package insert warnings and contraindications were not available in this evidence pack (Data Gap DG001). Drug-drug interaction data query returned no results. Before any clinical use or trial planning, a full safety review via the originator product monograph (e.g., Trandate® or equivalent) is required, with particular attention to beta-blocker contraindications (asthma, decompensated heart failure, second/third-degree AV block) and the requirement for dose adjustment in renal impairment.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.08%) and the mechanistic link between labetalol's dual adrenergic blockade and renovascular hypertension pathophysiology is scientifically plausible, the supporting evidence consists solely of two decades-old incidental case reports with no dedicated clinical trials. Additionally, labetalol is not currently registered in Singapore, and key safety data (package insert warnings, contraindications) remain unverified.

**To proceed, the following is needed:**
- Retrieve and review the full product monograph / package insert warnings and contraindications (DG001 — Blocking severity)
- Obtain complete MOA data from DrugBank API (DG002 — High severity)
- Conduct a systematic literature review specifically targeting labetalol or combined alpha/beta-blockers in renovascular or malignant hypertension
- Assess pharmacokinetic profile of labetalol in patients with renal impairment, given that malignant renovascular hypertension commonly presents with concurrent renal dysfunction
- Evaluate Singapore regulatory pathway requirements for labetalol market entry or compassionate use, given zero current registrations
- Design a registry-based or retrospective observational study as a precursor to any prospective trial
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

