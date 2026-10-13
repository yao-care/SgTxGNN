---
layout: default
title: Losartan
parent: Medium Evidence (L3-L4)
nav_order: 617
evidence_level: L4
indication_count: 10
---

# Losartan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Losartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Losartan is an angiotensin II receptor blocker (ARB) originally used for hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but the evidence is thin: **0 clinical trials** and **2 publications** (one case report and one preclinical animal-model paper).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, hypertensive disorder, diabetic nephropathy (the Singapore licence records list no indication text) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, losartan blocks the angiotensin II type 1 (AT1) receptor and is already used for hypertension and diabetic kidney disease. Renovascular hypertension is driven largely by activation of the renin-angiotensin system, so AT1 blockade is mechanistically plausible.

There are important caveats. The malignant form is a hypertensive emergency, and ARBs carry a risk of acute kidney injury in bilateral renal artery stenosis or a solitary kidney. The only human evidence is a single case report (Takayasu's arteritis with renal artery stenosis, in which enalapril plus losartan lowered blood pressure without deterioration of renal function). The other publication is a rat hypertension-model methods paper.

Other predictions in the same list (ranked by score) have a similar profile:
- **Malignant hypertensive renal disease** (99.73%): preclinical evidence only (L4).
- **Pulmonary hypertension owing to lung disease/hypoxia** (99.71%): small human physiological studies and animal data, with mixed or negative findings (L4).
- **Brain small vessel disease 1** (99.37%): indirect evidence from blood-pressure-lowering agents in general small vessel disease and from Marfan/Alport literature (L4).
- **Chronic pulmonary heart disease** (98.59%): one Phase 3 trial whose losartan arm could not be confirmed, plus small physiological and preclinical studies (L4).
- **Intracerebral hemorrhage** (97.30%): preclinical only, with some adverse signals (L4).
- **Pulmonary hypertension of unclear multifactorial mechanism, Braddock syndrome, Prinzmetal angina and COL4A1-related hematuria-retinal arteriolar tortuosity syndrome**: prediction score only (L5).

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant renovascular hypertension.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10667645](https://pubmed.ncbi.nlm.nih.gov/10667645/) | 2000 | Case report | Angiology | In a unilaterally nephrectomized patient with Takayasu's arteritis and malignant hypertension from renal artery stenosis, enalapril plus losartan improved blood pressure without deterioration of renal function |
| [22294399](https://pubmed.ncbi.nlm.nih.gov/22294399/) | 2009 | Preclinical animal model | Current Protocols in Pharmacology | Protocols for measuring antihypertensive activity in conscious rats (SHR, DOCA-salt, Goldblatt models); not a losartan efficacy study |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08588P | COZAAR TABLET 50 mg | Film-coated tablet | Not listed in licence record |
| SIN11614P | COZAAR TABLET 100 mg | Film-coated tablet | Not listed in licence record |
| SIN14729P | LOSAGEN (Losartan Potassium) Tablets 100 mg | Tablet | Not listed in licence record |
| SIN16973P | LOSARTAN-TEVA FC Tablet 100 mg | Film-coated tablet | Not listed in licence record |
| SIN13851P | Losartan Hexal 100 mg film-coated tablets | Film-coated tablet | Not listed in licence record |

There are 20 valid single-ingredient registrations in total, all oral tablets or film-coated tablets. Only five are shown here.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** The TxGNN knowledge graph links losartan to contraindications or cautions in conditions including pancreatitis, liver disease, hepatic encephalopathy, gallbladder disease, systemic lupus erythematosus, diabetes mellitus and diabetic ketoacidosis, gout, hypotensive disorder, hyperparathyroidism, hypercalcemia, anuria, renal artery obstruction and impaired renal function. These should be confirmed against the approved package insert.
- **Drug Interactions:** 100 interactions were identified in total. The **Major**-level interactions among those listed are with **potassium citrate** and **potassium bicarbonate** (risk of hyperkalaemia). Moderate interactions include corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, aspirin, morphine and bupropion.
- **Indication-specific concerns:** In renovascular disease, ARBs can cause acute kidney injury in bilateral renal artery stenosis or a solitary kidney. One published case reported transient anuria after the first losartan dose in a patient with a solitary kidney.

The package insert warnings and contraindications for the Singapore products were not available and should be reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.73%), but human evidence is limited to one case report, with no registered trials. Safety in the target population is a real concern, because renal artery stenosis is a recognised risk setting for ARB-induced kidney injury. The evidence level is L4.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications, to enable safety screening
- Mechanism of action data from DrugBank
- Clinical data on losartan in renovascular hypertension, ideally controlled studies with renal function monitoring
- A risk plan for bilateral renal artery stenosis, solitary kidney and acute hypertensive emergency settings
- A comparison with existing standard therapy (ACE inhibitors, calcium channel blockers, revascularisation) to define any added value
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

