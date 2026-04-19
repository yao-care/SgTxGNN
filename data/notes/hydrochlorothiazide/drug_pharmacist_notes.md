# Hydrochlorothiazide: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Hydrochlorothiazide (HCTZ) is a first-generation thiazide diuretic with a decades-long track record in managing hypertension and oedema by reducing circulating blood volume.
The TxGNN model predicts it may have utility in **Malignant Hypertensive Renal Disease** with a score of 98.42%,
however **no clinical trials** and **no publications** currently directly support this specific indication, making the evidence base limited to mechanistic inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, oedema |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 98.42% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on established pharmacological knowledge, Hydrochlorothiazide is a thiazide diuretic that inhibits the Na-Cl co-transporter (NCC) in the distal convoluted tubule of the kidney. This reduces sodium and water reabsorption, decreases circulating blood volume, and consequently lowers systemic blood pressure — a well-validated mechanism in the management of essential hypertension.

Malignant hypertensive renal disease sits at the severe end of the hypertensive disease spectrum, characterised by accelerated hypertension driving acute kidney injury, fibrinoid necrosis of the renal arterioles, and rapid deterioration of renal function. The TxGNN prediction likely stems from the disease's direct mechanistic proximity to hypertension in the knowledge graph: controlling blood pressure is the cornerstone of preventing further renal damage in this condition.

However, a critical clinical caveat substantially limits HCTZ's applicability here. In malignant hypertensive renal disease, renal function is typically severely compromised (eGFR often <30 mL/min/1.73 m²), at which point thiazide diuretics lose most of their diuretic and antihypertensive efficacy. Clinical practice guidelines therefore favour loop diuretics (e.g., furosemide) or intravenous agents in this acute context. This prediction represents an indirect extrapolation from hypertension rather than a disease-specific therapeutic rationale, and it carries no direct supporting trial or literature evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
HCTZ shares a conceptual mechanistic link with malignant hypertensive renal disease through blood pressure reduction, but thiazide diuretics are pharmacologically ineffective in the setting of severely reduced renal function (eGFR <30), which is characteristic of this condition — undermining both the clinical rationale and the practical utility of this repurposing hypothesis.

**To proceed, the following is needed:**
- Obtain and review the full package insert (including warnings, contraindications, and renal dosing adjustments) to complete the safety gap (DG001)
- Retrieve confirmed mechanism of action data from DrugBank API to complete the MOA gap (DG002)
- Conduct a focused literature search examining HCTZ or thiazide-class agents specifically in malignant hypertension or hypertensive emergency with renal involvement
- Evaluate whether the prediction score reflects a genuine disease-specific signal or an artefact of the broad hypertension node connectivity in the TxGNN knowledge graph
- If a research question is to be formalised, define an eGFR threshold for patient eligibility and pre-specify a safety monitoring plan for electrolyte imbalance and worsening renal function

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.