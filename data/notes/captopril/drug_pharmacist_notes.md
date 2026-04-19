# Captopril: From Hypertension and Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Captopril is a well-established angiotensin-converting enzyme (ACE) inhibitor, clinically recognised for treating hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
with **0 clinical trials** and **1 publication** currently supporting this specific direction — placing confidence primarily in mechanistic plausibility rather than direct clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension, congestive heart failure (established clinical use; no Singapore registration on record) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.28% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on established pharmacological knowledge, Captopril inhibits angiotensin-converting enzyme (ACE), blocking the conversion of angiotensin I to angiotensin II and suppressing the renin-angiotensin-aldosterone system (RAAS). This reduces systemic vascular resistance, lowers blood pressure, and — critically for renal implications — decreases efferent arteriolar tone, thereby reducing intraglomerular hypertension and proteinuria.

Malignant hypertensive renal disease is a severe end-organ complication driven by extreme hypertension and pathological RAAS hyperactivation, resulting in accelerated glomerular damage, fibrinoid necrosis of arterioles, and rapidly progressive renal failure. The mechanistic rationale is therefore coherent: ACEI-mediated RAAS suppression could attenuate the glomerular hypertensive injury central to this disease, mirroring established renoprotective roles of ACEIs in diabetic nephropathy and hypertensive nephrosclerosis.

However, a critical clinical caveat undermines straightforward application. In the setting of bilateral renal artery stenosis — which may coexist or underlie malignant hypertensive presentations — ACEI use carries a documented risk of precipitating acute renal failure due to loss of angiotensin II-mediated efferent tone needed to maintain GFR. Careful renal imaging and close monitoring of renal function are prerequisites before initiating therapy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Captopril in malignant hypertensive renal disease.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | Case Report | Clinical Nuclear Medicine | A patient with positive captopril renography found to have chromophobe renal cell carcinoma (not renal artery stenosis); nephrectomy relieved renin-dependent hypertension. Illustrates the diagnostic complexity of renin-mediated renal hypertension in non-atherosclerotic etiologies — tangential to malignant hypertensive renal disease but highlights captopril's role in identifying renin-dependent vascular pathology |

---

## Singapore Market Information

Captopril is currently not registered in Singapore. No product authorisations are on file. Physicians wishing to use Captopril would need to access it through special import channels or consider alternative ACE inhibitors with local registration.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note from evidence pack:** Full safety data including TFDA package insert warnings, contraindications, and drug interaction records were not retrieved for this analysis. This is flagged as a blocking data gap (DG001) that must be resolved before any clinical safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.28%), direct clinical evidence for Captopril in malignant hypertensive renal disease is limited to a single tangentially relevant case report. The mechanistic rationale is plausible but insufficient on its own to support a repurposing recommendation, particularly given the known risk of acute renal decompensation in bilateral renovascular disease that may accompany malignant hypertensive presentations.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Obtain and review the full package insert — warnings, contraindications, and renal function monitoring requirements — before any safety assessment can proceed
- **MOA confirmation:** Query DrugBank API to retrieve formal mechanism of action and pharmacological class data (DG002)
- **Renal imaging prerequisite:** Any clinical application must first exclude bilateral renal artery stenosis (risk of ACE inhibitor-induced acute kidney injury)
- **Targeted literature search:** Expand PubMed search to malignant hypertension with renal involvement specifically under ACEI therapy, including hypertensive emergency guidelines
- **Subpopulation analysis:** Review whether existing large ACEI trials (e.g., SAVE, SOLVD) captured malignant hypertensive renal disease subpopulations as secondary endpoints
- **Consider higher-priority indications:** The evidence pack identifies **malignant renovascular hypertension** (Rank 2, L3, 20 publications) and **chronic renal failure syndrome** (Rank 10, L3, 18 publications + 2 clinical trials) as better-evidenced repurposing candidates with "Proceed with Guardrails" recommendations — these may warrant prioritisation over Rank 1