---
layout: default
title: Isotretinoin
parent: Low Evidence (L5)
nav_order: 558
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Isotretinoin: predicted new indication Malignant renovascular hypertension (evidence level L5). Approved use: Hypertensive disorder / hypertension"
---

# Isotretinoin
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

# Isotretinoin: From Hypertensive Disorder to Malignant Renovascular Hypertension

## One-Sentence Summary

Isotretinoin is listed in the source knowledge graph with an original indication of hypertensive disorder. This listing is questionable, because isotretinoin is a retinoid marketed in Singapore as an oral capsule, and a hypertension indication should be verified. The TxGNN model predicts it may be effective for **malignant renovascular hypertension**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder / hypertension (from the knowledge graph; the Singapore licence records contain no indication text, and this listing needs verification) |
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.01% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Isotretinoin is a retinoid (a vitamin A–related compound). Nothing in the data compiled for this report establishes a link between retinoid activity and blood pressure control, and isotretinoin is not a recognised antihypertensive.

The high score (0.990) is a graph-based prediction. The next-ranked prediction, malignant hypertensive renal disease, has an identical score. This suggests the two share a neighbourhood in the ontology rather than representing independent signals. Retinoid effects on the renin-angiotensin system or on renal fibrosis are hypothetical and unsupported by the data compiled here.

Other predicted indications are similarly unsupported:
- **Pulmonary hypertension (two entries, score 0.989):** retinoid signalling has been discussed in pulmonary vascular remodelling, but no supporting evidence was found. Isotretinoin's teratogenicity and possible effects on the pulmonary vasculature argue for caution.
- **Braddock syndrome (0.987) and chronic pulmonary heart disease (0.887):** no evidence, and any link is indirect or unsupported.
- **Cholangiocarcinoma susceptibility (0.619):** retinoids have antiproliferative effects in some cancers, but this entry describes genetic susceptibility rather than a treatable disease.
- **Obsolete functional visual loss (0.592), myxomatous mitral valve prolapse (0.591) and ocular tuberculosis (0.587):** low scores with no supporting rationale. Isotretinoin is associated with visual adverse effects, which runs opposite to a therapeutic rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked prediction. The only publications retrieved were for the fourth-ranked prediction (pulmonary hypertension owing to lung disease and/or hypoxia), and they do not address that condition. They appear to be keyword matches on hypoxia or oxygenation.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10030263](https://pubmed.ncbi.nlm.nih.gov/10030263/) | 1999 | Clinical study | Int J Radiat Oncol Biol Phys | Tumour oxygenation in cervical cancer during radiotherapy, with and without 13-cis-retinoic acid/interferon-alpha-2a |
| [9830438](https://pubmed.ncbi.nlm.nih.gov/9830438/) | 1998 | Clinical study | Strahlenther Onkol | A 2-week pretreatment with 13-cis-retinoic acid plus interferon-alpha-2a before radiation improved tumour oxygenation in cervical cancer |
| [16549710](https://pubmed.ncbi.nlm.nih.gov/16549710/) | 2006 | Case report | Arch Dermatol | Diffuse dermal angiomatosis of the breast, a rare dermatological condition |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13051P | ACNOTIN 20 | Capsule | Not stated in the data |
| SIN14628P | ORATANE CAPSULE 5 mg | Capsule | Not stated in the data |
| SIN11781P | ORATANE CAPSULE 20 mg | Capsule | Not stated in the data |
| SIN13333P | ACNOTIN 10 | Capsule | Not stated in the data |
| SIN11782P | ORATANE CAPSULE 10 mg | Capsule | Not stated in the data |

Eight licences are valid in total (all single-ingredient oral capsules). The remaining three are ROACCUTANE 20 mg (SIN04921P), ROACCUTANE 10 mg (SIN04920P) and NIMEGEN SOFT CAP. 10 mg (SIN10767P).

## Safety Considerations

The package insert warnings and contraindications were not available for this report, so please refer to the package insert for them.

- **Contraindication signals from the knowledge graph (not label text):** these include liver disease, kidney disease, pancreatitis, gallbladder disease, inflammatory bowel disease, osteoporosis, diabetes mellitus and diabetic ketoacidosis, psychotic and other mental disorders, anxiety disorder, systemic lupus erythematosus, neutropenia, agranulocytosis, angioedema (several forms) and hypotensive disorder.
- **Drug interactions:** 98 interactions were recorded. The **Major** ones are:
  - Doxycycline
  - Minocycline
  - Tetracycline
  - Vitamin A

  **Moderate** ones include systemic corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone, prednisolone, prednisone, triamcinolone), warfarin, dicoumarol, naltrexone, ethanol, nitisinone, fostamatinib, ivacaftor, lumacaftor and topical abametapir.
- **Teratogenicity and ocular effects:** isotretinoin's known teratogenicity and visual adverse effects (such as impaired night vision) are important concerns for any new use.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a graph-based score alone, with no clinical trials or relevant publications (Evidence Level L5). The stated original indication of hypertension is doubtful, no mechanism of action is available, and safety data are incomplete. The knowledge graph also flags a hypotensive disorder contraindication.

**To proceed, the following is needed:**
- Verification of the original indication, since the Singapore licence records contain no indication text
- Mechanism of action data, for example from DrugBank
- HSA package insert warnings and contraindications, which block safety screening
- Preclinical or mechanistic evidence linking retinoid activity to blood pressure regulation or renal and pulmonary vascular disease
- A teratogenicity risk assessment and a review of the knowledge graph contraindications against the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

