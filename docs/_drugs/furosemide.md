---
layout: default
title: Furosemide
parent: 僅模型預測 (L5)
nav_order: 455
evidence_level: L5
indication_count: 10
---

# Furosemide
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

# Furosemide: From Diuretic Therapy (Edema/Hypertension) to Malignant Renovascular Hypertension

## One-Sentence Summary

Furosemide is a loop diuretic long used internationally for fluid overload (edema due to cardiac, hepatic, or renal disease) and hypertension. The TxGNN model predicts it may also be effective for **Malignant Renovascular Hypertension**, but currently only **0 clinical trials** and **14 literature articles** support this direction, and most of that literature describes furosemide's use as a diagnostic *renin-stimulation test* rather than as a proven treatment for this specific condition.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Edema (cardiac/hepatic/renal) and hypertension — general international indication for this loop diuretic; no Singapore-specific approved indication text is available (drug is not currently registered) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 98.03% |
| Evidence Level | L3 (Observational studies; no RCTs identified) |
| Singapore Market Status | ✗ Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the structured record used for this evaluation (Data Gap DG002, severity High). Based on well-established pharmacology, furosemide is a loop diuretic that inhibits the Na⁺-K⁺-2Cl⁻ (NKCC2) cotransporter in the thick ascending limb of the loop of Henle, producing potent natriuresis and diuresis. Its efficacy in edema and hypertension is proven internationally, and mechanistically it may be applicable to malignant renovascular hypertension through its known effects on renal sodium handling and the renin-angiotensin-aldosterone system (RAAS).

Malignant renovascular hypertension arises from severe renal artery stenosis, which chronically activates the RAAS and drives extreme, organ-damaging blood pressure elevation. Furosemide's diuretic action reduces intravascular volume and is known to *stimulate* renin release — a property literature has long exploited as a "furosemide stimulation test" to help diagnose secondary and renovascular hypertension, rather than as a direct disease-modifying treatment. Volume control with loop diuretics is nonetheless a recognized adjunct in managing the hypertensive-emergency component of malignant hypertension, typically alongside RAAS blockers (ACE inhibitors/ARBs) and, where indicated, revascularization.

The TxGNN model's link between furosemide and malignant renovascular hypertension most likely reflects shared knowledge-graph connections through renin/RAAS pathway genes and hypertension-related disease nodes. This mechanistic plausibility is reasonable, but the supporting literature reflects furosemide's diagnostic and adjunctive volume-management role rather than confirmed therapeutic efficacy specifically for malignant renovascular hypertension, so the prediction should be interpreted cautiously.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [397653](https://pubmed.ncbi.nlm.nih.gov/397653/) | 1979 | Clinical Review | Transactions of the American Association of Genito-Urinary Surgeons | Furosemide stimulates renin release and is used with saline suppression testing to differentiate causes of secondary hypertension, including renovascular disease |
| [15080378](https://pubmed.ncbi.nlm.nih.gov/15080378/) | 2004 | Prospective Observational Study | Hypertension Research | In 1,020 hypertensive patients, a furosemide-plus-upright test was used in secondary screening to identify causes of secondary hypertension, including renovascular hypertension |
| [844016](https://pubmed.ncbi.nlm.nih.gov/844016/) | 1977 | Case Report | Canadian Medical Association Journal | Furosemide screening test showed elevated plasma renin activity in a patient ultimately diagnosed with pheochromocytoma rather than renovascular hypertension, illustrating its differential-diagnostic use |
| [2944248](https://pubmed.ncbi.nlm.nih.gov/2944248/) | 1986 | Observational Study | Tohoku Journal of Experimental Medicine | Furosemide altered active/inactive renin levels in hypertensive patients and was studied alongside renal angioplasty outcomes in renovascular hypertension |
| [6321850](https://pubmed.ncbi.nlm.nih.gov/6321850/) | 1984 | Case Report | Klinische Wochenschrift | Describes a patient with malignant renovascular hypertension and chronic renal failure from bilateral renal artery occlusion, with reversible ACE-inhibitor-induced renal insufficiency |
| [7977845](https://pubmed.ncbi.nlm.nih.gov/7977845/) | 1994 | Preclinical (Animal Study) | American Journal of Physiology | In a Goldblatt rat model of renovascular hypertension, thromboxane A2 receptor blockade reduced progression to malignant hypertension, supporting a renin/vascular-mediated mechanism |
| [659766](https://pubmed.ncbi.nlm.nih.gov/659766/) | 1978 | Observational Study | Journal of the American Geriatrics Society | Serum uric acid and plasma renin activity were both elevated in malignant and renovascular hypertension versus essential hypertension, supporting a shared RAAS pathophysiology |
| [30401909](https://pubmed.ncbi.nlm.nih.gov/30401909/) | 2019 | Prospective Registry Study | Hypertension Research | The SHRIMP study evaluated predictors of confirmatory testing for secondary hypertension causes, including renovascular disease, in patients with elevated aldosterone-to-renin ratio |
| [3283072](https://pubmed.ncbi.nlm.nih.gov/3283072/) | 1988 | Retrospective Study | International Urology and Nephrology | Renal/renovascular lesions were more prominent in aldosteronism patients whose hypertension persisted despite treatment |
| [34782](https://pubmed.ncbi.nlm.nih.gov/34782/) | 1979 | Case Series | Medizinische Klinik | Angiotensin-II blockade (saralasin) normalized blood pressure in resistant hypertensive crises, including a renovascular hypertension case, after conventional vasodilator therapy failed |

---

## Singapore Market Information

Furosemide currently has no registered product license in Singapore (0 authorizations on file; market status: Not Marketed). No indication or dosage-form data is available for this market.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-interaction data for this evaluation are currently unavailable — TFDA/HSA label data has not yet been obtained, Data Gap DG001, severity Blocking.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials support furosemide's use in malignant renovascular hypertension, and the existing literature primarily describes furosemide's role as a diagnostic renin-stimulation reagent rather than proven therapy for this condition. Critically, package-insert safety data (warnings/contraindications) is missing and classified as a Blocking data gap, which prevents even an initial safety assessment (S1). The drug is also not currently registered in the Singapore market.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — required to clear the Blocking data gap before any safety review can begin
- Structured mechanism-of-action data from DrugBank to support mechanistic-relevance analysis
- A targeted literature/expert review distinguishing furosemide's diagnostic (renin-stimulation test) use from any genuine treatment-efficacy evidence for malignant renovascular hypertension
- Clarification of the regulatory pathway if Singapore market entry for this indication is being considered
- Given the weak evidence for this top-ranked indication, consider evaluating other candidates in the same prediction set with stronger clinical trial support (e.g., chronic pulmonary heart disease, rank 6, which has 22 registered clinical trials) as a separate line of review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

