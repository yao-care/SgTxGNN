# Hydralazine: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Hydralazine is a direct-acting arteriolar vasodilator with a long-standing clinical history in hypertensive emergencies, pre-eclampsia, and chronic heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease** with a prediction score of **96.86%**,
though currently **no clinical trials** and **no publications** directly evaluate this specific disease subtype, placing the primary prediction at evidence level L4.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / hypertensive emergency (antihypertensive agent; no Singapore registration on record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 96.86% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available in this Evidence Pack. Based on established pharmacological knowledge, Hydralazine is a direct-acting vasodilator that relaxes arteriolar smooth muscle — likely through opening K⁺ channels and inhibiting IP3-induced intracellular Ca²⁺ release — which lowers systemic vascular resistance. Its decades of clinical use in hypertensive emergencies, gestational hypertension, and refractory heart failure confirm its potency as a peripheral vasodilator.

Malignant hypertensive renal disease is characterised by fibrinoid necrosis of renal arterioles and glomerular capillaries driven by severely elevated blood pressure, resulting in rapid deterioration of renal function. The theoretical rationale for Hydralazine is straightforward: by acutely reducing systemic arterial pressure, it may decompress intraglomerular hypertension and slow the progression of hypertensive arteriolar injury. Its historical use in hypertensive crises — a clinical context that frequently overlaps with malignant hypertension presentations — provides indirect supporting experience.

However, this mechanistic link must be weighed against a critical limitation. No clinical trial or published study has specifically evaluated Hydralazine as a targeted therapy for *malignant hypertensive renal disease* as a distinct pathological entity. Modern management of malignant hypertension employs renin-angiotensin-aldosterone system (RAAS) blockers and calcium channel antagonists as preferred agents, partly because Hydralazine's non-selective vasodilation can trigger reflex tachycardia and RAAS activation — effects that may paradoxically worsen renal outcomes in renin-dependent states.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Hydralazine is **not currently registered** in Singapore. There are no active marketing authorisations on record, and no dosage form data is available from the Singapore Health Sciences Authority (HSA).

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Both warning/contraindication data from the Taiwan FDA package insert and DrugBank drug interaction data are currently unavailable (identified as Data Gaps DG001 and DG002 in this Evidence Pack). These gaps are flagged as Blocking and High severity respectively and must be resolved before any safety assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high score (96.86%) reflects mechanistic plausibility — Hydralazine's arteriolar vasodilation could theoretically relieve intraglomerular hypertensive stress — but with zero direct clinical trial or literature support for this specific renal disease subtype, and no Singapore regulatory registration, there is insufficient evidence to advance this candidate at present.

> **Broader Landscape Note:** Among all 10 TxGNN-predicted indications for Hydralazine, **Chronic Pulmonary Heart Disease (cor pulmonale)** (Rank 6; score 88.29%) currently carries the strongest evidence base — multiple direct haemodynamic studies from the 1976–1987 period (including PMID 6692695, 6407295, 7225252, 825327, 3979067) support afterload reduction in right heart failure secondary to COPD, placing it at Evidence Level L3 with a "Proceed with Guardrails" recommendation. Investigators wishing to pursue a Hydralazine repurposing programme may consider prioritising this indication.

**To proceed with the primary prediction (Malignant Hypertensive Renal Disease), the following is needed:**

- **Safety data (Blocking):** Obtain and parse the Taiwan FDA (TFDA) package insert PDF to extract warnings and contraindications (Data Gap DG001)
- **MOA data (High):** Query DrugBank API for formal mechanism of action documentation (Data Gap DG002)
- **Targeted literature search:** Commission a systematic search specifically combining "hydralazine" with "malignant hypertension," "hypertensive nephropathy," and "fibrinoid necrosis of renal arterioles" to identify any indirect evidence
- **Clinical context review:** Determine whether existing hypertensive emergency indications already cover the malignant hypertension population, which may reduce the need for a separate repurposing programme
- **Singapore regulatory pathway assessment:** Evaluate whether HSA registration would be required before any clinical application, given zero current market presence
- **Comparator analysis:** Benchmark Hydralazine against currently preferred agents (ACE inhibitors, ARBs, calcium channel blockers) in the malignant hypertension setting to assess whether a clinical niche exists

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application. Data cut-off: 2026-04-04.*