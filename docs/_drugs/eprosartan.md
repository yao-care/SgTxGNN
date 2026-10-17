---
layout: default
title: Eprosartan
parent: Low Evidence (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Eprosartan: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Eprosartan"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease", "obsolete susceptibility to ischemic stroke", "ocular tuberculosis", "congenital temporomandibular joint ankylosis", "obsolete functional visual loss"]
---

# Eprosartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Eprosartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Eprosartan is an angiotensin II receptor blocker (ARB), originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The evidence is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 93.69% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, eprosartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is established, and mechanistically it may be applicable to renovascular hypertension.

Renovascular hypertension depends strongly on the renin-angiotensin system (RAS), so blocking the AT1 receptor is biologically plausible. However, this prediction is essentially an extension of the approved hypertension indication rather than a distinct repurposing opportunity. ARBs are also generally used with caution in bilateral renal artery stenosis because of the risk of acute decline in renal function.

Other predicted indications are weaker still. The next-ranked prediction, malignant hypertensive renal disease (score 93.69%), overlaps with the original indication, and malignant hypertension is an acute emergency usually managed with intravenous agents rather than an oral ARB. The pulmonary hypertension predictions (score 93.01%) rest only on a theoretical role of RAS in pulmonary vascular remodelling. Several lower-ranked predictions, such as Braddock syndrome and ocular tuberculosis, show no identifiable mechanistic link and are likely network artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for the top-ranked prediction. For the third-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), one publication was retrieved, but it does not address pulmonary hypertension:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33942446](https://pubmed.ncbi.nlm.nih.gov/33942446/) | 2021 | Preclinical (animal study) | J Biochem Mol Toxicol | Eprosartan showed neuroprotective activity in rats with focal cerebral ischemia-reperfusion injury (MCAO model) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11807P | TEVETEN TABLET 600 mg | Tablet, film coated (oral) | Not specified in the available data |

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** pancreatitis, systemic lupus erythematosus (including paediatric), potassium deficiency, diabetes mellitus, diabetic ketoacidosis, hyperuricaemia, hypotensive disorder, hyperparathyroidism, osteitis fibrosa, hepatic coma/encephalopathy, neonatal jaundice, anuria, gout, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, and renal artery obstruction. These come from drug-disease network edges and should be verified against the package insert.
- **Drug Interactions:** 84 interactions were recorded. Major-level interactions include **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia is the expected concern). Moderate-level interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins (aspart, degludec, detemir), acetylsalicylic acid, morphine, bupropion, dronabinol, and bowel-preparation products (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes).

Package insert warnings and contraindications were not available; please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials or linked literature. It also largely overlaps with the already approved hypertension indication, so it offers little new repurposing value. The renal artery obstruction contraindication flag is directly relevant to renovascular disease and needs careful review.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Clinical or observational evidence of eprosartan in renovascular hypertension, including renal safety in renal artery stenosis
- Confirmation of the approved indication text for SIN11807P
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

