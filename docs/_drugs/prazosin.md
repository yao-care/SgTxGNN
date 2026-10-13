---
layout: default
title: Prazosin
parent: Low Evidence (L5)
nav_order: 820
evidence_level: L5
indication_count: 10
---

# Prazosin
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

# Prazosin: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Prazosin is an alpha-1 adrenergic blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**, but **no clinical trials and no directly relevant publications** currently support this prediction, so it rests on model inference alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the Singapore licence records contain no approved indication text, so this is taken from the knowledge-graph indication data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 90.23% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, prazosin is an alpha-1 adrenergic antagonist. It relaxes vascular smooth muscle and lowers peripheral vascular resistance, which is how it lowers blood pressure in hypertension.

Malignant hypertensive renal disease is a severe form of hypertension with kidney involvement. Because blood pressure lowering is the main therapeutic goal, the prediction is mechanistically plausible. The high score probably reflects how close this condition sits to the already approved hypertension indication in the knowledge graph, rather than new, independent evidence.

Caution is needed. Kidney perfusion must be protected, and there is a risk of excessive hypotension. The knowledge graph also lists chronic kidney disease, chronic renal failure and end-stage renal failure as contraindication associations for prazosin, which sits uneasily with a kidney-related indication and needs clarification.

Other predicted indications in the same list include:

| Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|
| Malignant renovascular hypertension | 90.23% | L4 | Only indirect literature (a 1975 case series, a rat model, a methods paper); overlaps with the approved hypertension use |
| Attention deficit-hyperactivity disorder | 89.74% | L4 | Mostly preclinical or mechanistic papers, several about other drugs. Alpha-2 agonists, not alpha-1 antagonists, are the established non-stimulant class. Classed as a research question |
| ADHD, inattentive type | 89.71% | L5 | Prediction only |
| Faciodigitogenital syndrome | 89.45% | L5 | No mechanistic link identified |
| Pulmonary hypertension (two categories) | 89.27% | L5 / L4 | Systemic vasodilators may worsen ventilation-perfusion matching; evidence is preclinical and indirect |
| Specific developmental disorder | 87.15% | L5 | Retrieved literature concerns alcohol use disorder, so it is mismatched |
| Braddock syndrome | 86.16% | L5 | No mechanistic link identified |
| Chondromyxoid fibroma | 77.30% | L5 | No plausible mechanistic link |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature was retrieved for malignant hypertensive renal disease. The closest related predicted indication, malignant renovascular hypertension, has only indirect publications, listed below for reference.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1055318](https://pubmed.ncbi.nlm.nih.gov/1055318/) | 1975 | Case series | N Z Med J | 24 hypertensive patients on prazosin; 20 reached standing BP below 140/90 mmHg after 6 weeks; two severe renovascular hypertension cases responded excellently |
| [22294399](https://pubmed.ncbi.nlm.nih.gov/22294399/) | 2009 | Preclinical | Curr Protoc Pharmacol | Rat models (SHR, DOCA-salt, Goldblatt); prazosin was the most active reference antihypertensive in the SHR model |
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review | Horm Metab Res | Factors affecting the aldosterone/renin ratio; not specific to prazosin treatment |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07264P | APO-PRAZO TABLET 1 mg | Tablet | Not stated in the licence record |
| SIN07529P | ATODEL 1 TABLET 1 mg | Tablet | Not stated in the licence record |
| SIN07263P | APO-PRAZO TABLET 5 mg | Tablet | Not stated in the licence record |
| SIN07260P | APO-PRAZO TABLET 2 mg | Tablet | Not stated in the licence record |
| SIN16122P | MINISON TABLET 1MG | Tablet | Not stated in the licence record |

All five licences are valid single-ingredient oral tablets.

---

## Safety Considerations

- **Contraindication associations (knowledge graph, not label text)**: chronic kidney disease, chronic renal failure syndrome, end stage renal failure, intraoperative floppy iris syndrome, narcolepsy, narcolepsy-cataplexy syndrome, central nervous system disease, Balo concentric sclerosis, X-linked adrenoleukodystrophy.
- **Drug Interactions**: 77 interactions were identified. Those listed are all moderate or of unknown severity:
  - Corticosteroids: hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone
  - Opioids and cannabinoids: morphine (including liposomal), opium, dronabinol, nabilone
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin, ertugliflozin
  - Others: bupropion, acetylsalicylic acid
  - Unknown severity: pantoprazole, metformin

Package insert warnings and contraindications are not available in the data compiled for this report. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score, but no clinical trials or direct literature support it, so the evidence level is L5. The score probably reflects its closeness to the approved hypertension indication rather than new evidence. Prazosin has a long history in hypertension, but no evidence shows an added benefit in malignant hypertensive renal disease. The renal-related contraindication associations also need clarification.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data
- Clinical evidence in malignant hypertension with renal involvement, including renal perfusion and hypotension risk
- Clarification of the knowledge-graph renal contraindication associations
- A comparison against standard therapies for hypertensive emergencies to show whether prazosin adds value beyond its approved hypertension use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

