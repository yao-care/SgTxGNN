# Acebutolol: From Hypertension / Ventricular Arrhythmia to Malignant Renovascular Hypertension

## One-Sentence Summary

Acebutolol is a cardioselective β1-adrenergic blocker with Class II antiarrhythmic properties, internationally established for the treatment of hypertension and ventricular arrhythmias, though it holds no Singapore registration.
The TxGNN model predicts it may have utility in **Malignant Renovascular Hypertension**, currently supported by **0 clinical trials** and **1 historical publication** — with important mechanistic safety concerns that must be addressed before any development decision.
Overall evidence strength is rated **L4** (preclinical/mechanistic level), and the recommended stance is **Hold** pending safety characterisation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; internationally approved for hypertension and ventricular arrhythmias (premature ventricular contractions) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.10% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, acebutolol is a cardioselective β1-adrenergic receptor antagonist with mild intrinsic sympathomimetic activity (ISA). Its principal antihypertensive actions include reducing cardiac output, slowing the heart rate, and — critically — suppressing β1-mediated renin release from the juxtaglomerular cells of the kidney. This renin-suppressing effect is the mechanistic thread that connects acebutolol to renovascular hypertension.

Malignant renovascular hypertension arises from renal artery stenosis (RAS), which triggers pathologically elevated renin secretion and downstream angiotensin II overactivation, driving dangerously accelerated blood pressure elevation with end-organ damage. Because acebutolol can blunt this renin surge via β1 blockade, the TxGNN prediction carries a biologically coherent rationale — the model is, in effect, capturing acebutolol's renin-suppression mechanism and matching it to a renin-driven disease.

However, this mechanistic plausibility comes with a significant safety caveat. In bilateral renal artery stenosis — the most common cause of renovascular hypertension — the angiotensin II-mediated efferent arteriolar vasoconstriction is the primary mechanism maintaining glomerular filtration pressure. Suppressing the renin-angiotensin axis (whether via ACE inhibitor, ARB, or beta-blocker renin suppression) risks precipitous loss of renal perfusion. The single supporting publication (1975, non-randomised, n=50 general hypertensives) does not specifically evaluate patients with malignant or bilateral RAS presentations, so direct efficacy and safety conclusions cannot be drawn. Safety evaluation must precede any repurposing investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [768911](https://pubmed.ncbi.nlm.nih.gov/768911/) | 1975 | Non-randomised Clinical Study | La Nouvelle presse medicale | Open-label, 1-year trial of acebutolol (alone or in combination with other antihypertensives) in 50 hypertensive patients; good-to-moderate response in 74%, treatment failure in 26%; mean dose 10 mg/kg (max 22 mg/kg); described as well tolerated; cohort included some renovascular hypertension cases but results are not disaggregated by subtype |

---

## Singapore Market Information

Acebutolol is currently not registered in Singapore. No marketing authorisation records are available. Prescribers requiring product information should consult international monographs (e.g., FDA label, EMA SmPC for Sectral® or equivalent).

---

## Safety Considerations

Please refer to the package insert for safety information. As acebutolol holds no Singapore registration, no local prescribing information is available; practitioners must consult international product monographs.

The following mechanistic safety concern is directly relevant to the predicted indication:

- **Renal perfusion risk in bilateral RAS**: In bilateral renal artery stenosis (the typical substrate for renovascular hypertension), beta-blocker–mediated renin suppression may eliminate the compensatory angiotensin II tone maintaining glomerular filtration, potentially precipitating acute kidney injury. This is a known class-level safety concern requiring renal function monitoring and careful patient selection.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the renin-suppression mechanism of acebutolol provides a plausible biological link to malignant renovascular hypertension, the entire evidence base consists of a single 50-year-old non-randomised study that does not specifically address malignant or bilateral RAS presentations. Combined with the known risk of worsening renal perfusion in bilateral RAS — the most common aetiology of this condition — the safety profile for this specific indication is uncharacterised and potentially harmful. No progression is warranted until foundational safety data are available.

**Notable secondary finding:** Among all 10 TxGNN-predicted indications, **atrial flutter** (rank 10, TxGNN score 59.1%) holds the strongest evidence base — 3 publications including 1 randomised controlled trial (PMID [3535474](https://pubmed.ncbi.nlm.nih.gov/3535474/)) — and has been scored **L3 / Proceed with Guardrails**. Acebutolol is already approved for supraventricular arrhythmias in several international markets, making atrial flutter the most actionable repurposing opportunity in Singapore where it is currently unapproved.

**To proceed with malignant renovascular hypertension, the following is needed:**
- Mechanism of action (MOA) data from DrugBank to formally document the renin-suppression pathway and its role in renovascular pathophysiology
- Package insert safety data (TFDA or FDA/EMA monograph) to characterise contraindications, renal warnings, and dose-adjustment guidance
- Clarification of bilateral vs. unilateral RAS prevalence in the target population — this is the critical safety stratification gate
- Targeted literature review restricted to acebutolol (or cardioselective beta-blockers) specifically in renovascular or malignant hypertension subgroups
- Review of whether any international market has granted acebutolol an indication covering renovascular hypertension

> ⚠️ *This report is generated for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*