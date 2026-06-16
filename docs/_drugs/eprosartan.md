---
layout: default
title: Eprosartan
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 10
---

# Eprosartan
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

# Eprosartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Eprosartan is an angiotensin II type 1 (AT1) receptor blocker (ARB) used for the treatment of essential hypertension, notable among its class for its additional ability to suppress sympathetic nervous activity by blocking pre-synaptic neuronal AT1 receptors.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension** — a severe, RAAS-driven form of hypertension arising from renal artery stenosis — with a prediction score of **93.7%**.
Currently, **no clinical trials or published literature** specifically support this application for Eprosartan, placing the evidence at the mechanistic inference level only.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Essential hypertension (ARB class; no Singapore registration available) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 93.7% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in the evidence pack. Based on established pharmacology, Eprosartan is a selective angiotensin II type 1 (AT1) receptor antagonist. What distinguishes Eprosartan from other ARBs is its dual blockade capability: in addition to the canonical vascular smooth muscle AT1 blockade that lowers blood pressure, Eprosartan also blocks pre-synaptic sympathetic neuronal AT1 receptors, thereby reducing norepinephrine release and attenuating the sympathetic component of hypertension. This dual mechanism has been the basis for clinical investigations comparing Eprosartan to calcium channel blockers in stroke secondary prevention (the MOSES trial).

The connection to malignant renovascular hypertension is mechanistically direct. Renal artery stenosis triggers massive renin release → elevated angiotensin II (AngII) → AT1 receptor activation → severe systemic vasoconstriction and aldosterone hypersecretion, creating a self-amplifying loop of malignant hypertension. Blocking AT1 receptors with Eprosartan can theoretically interrupt this cascade at the core effector step, making this one of the more pharmacologically coherent predictions in the ranked list.

However, a critical safety consideration must accompany any assessment: in patients with bilateral renal artery stenosis — a common cause of renovascular hypertension — ARBs carry a risk of acute and potentially severe renal function deterioration, because AngII-mediated efferent arteriolar tone is required to maintain glomerular filtration under ischemic conditions. This represents a recognized contraindication that substantially limits the scope of this predicted indication and explains the "Hold" recommendation despite the logical mechanistic link.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Eprosartan is not currently registered with the Health Sciences Authority (HSA) in Singapore. No product authorizations or approved indications are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic link between Eprosartan's AT1 blockade and malignant renovascular hypertension is pharmacologically coherent, but the complete absence of clinical trial data and published literature — combined with the bilateral renal artery stenosis contraindication — means there is insufficient evidence to advance this indication at this time.

---

**⚠️ Priority Finding Elsewhere in the Ranked List — Ischemic Stroke Prevention (Rank #7)**

The rank #7 prediction — **susceptibility to ischemic stroke** (TxGNN score: 66.1%) — carries an **L1 evidence level** and a **"Proceed with Guardrails"** recommendation, making it the most clinically actionable finding in this entire evidence pack despite its lower TxGNN rank.

The mechanistic basis is Eprosartan's unique dual action:
1. **AT1 vascular blockade** → blood pressure reduction → reduced stroke risk (shared with all ARBs)
2. **Pre-synaptic sympathetic AT1 blockade** → reduced norepinephrine release → decreased vascular tension and thrombotic tendency (specific to Eprosartan; no other ARB shares this property)

This dual mechanism was the core hypothesis of the **MOSES trial** (*Morbidity and Mortality After Stroke — Eprosartan Compared with Nitrendipine for Secondary Prevention*), a Phase 3 head-to-head study demonstrating that Eprosartan reduced recurrent cerebrovascular events more effectively than the calcium channel blocker nitrendipine in hypertensive patients with a prior stroke. This constitutes L1-level evidence supporting stroke secondary prevention as Eprosartan's most evidence-supported repurposing direction.

**To proceed with the malignant renovascular hypertension indication, the following is needed:**
- Retrospective cohort or case-control analyses of ARB use in confirmed malignant renovascular hypertension patients
- Bilateral vs. unilateral renal artery stenosis stratification to define a safe patient subset
- Renal function monitoring protocols (creatinine, eGFR, potassium) for risk mitigation
- Formal safety data retrieval (package insert PDF, contraindication verification)
- Mechanism of action data from DrugBank to support regulatory submissions

**To advance the ischemic stroke indication (highest-priority direction):**
- Retrieve the full MOSES trial data (NCT reference and published outcomes)
- Review Singapore stroke secondary prevention guidelines for ARB positioning
- Assess drug availability pathway given current non-registration status in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

