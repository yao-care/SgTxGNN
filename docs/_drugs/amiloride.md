---
layout: default
title: Amiloride
parent: Low Evidence (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Amiloride
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

# Amiloride: From a Potassium-Sparing Diuretic to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Amiloride is a potassium-sparing diuretic that blocks the epithelial sodium channel (ENaC). The Singapore registration record does not state an approved indication.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** (score 99.82%), but **no clinical trials and no publications** currently support this specific prediction.
The evidence is model prediction only (L5), so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.82% (rank 3168) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

The registration record has no approved-indication text, so the original indication is not listed here.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. As general pharmacology, amiloride blocks ENaC in the distal nephron. This reduces sodium reabsorption and can lower volume-dependent blood pressure.

Malignant hypertensive renal disease is severe hypertension with kidney injury. In principle, a drug that reduces sodium retention could be relevant. This link is plausible, but it comes from general pharmacology and from the graph-based score. No study in the Evidence Pack tests amiloride in this condition.

### Other Predicted Indications

Some lower-ranked predictions have more supporting material than the top-ranked one. None reaches a level that would change the decision.

| Predicted Indication | Score | Evidence Level | What the Evidence Shows |
|------|------|------|------|
| Malignant renovascular hypertension | 99.82% | L5 | One review on mineralocorticoid hypertension work-up. It does not show amiloride use in renovascular disease. |
| Pulmonary hypertension (multifactorial; lung disease/hypoxia) | 99.81% | L5 | No usable evidence. The 20 retrieved papers are keyword matches on "hypoxia" and were treated as noise. |
| Braddock syndrome | 99.75% | L5 | No trials or literature. |
| Chronic pulmonary heart disease | 99.68% | L4 | Human studies in chronic congestive heart failure only, so the evidence is indirect (see below). |
| Acute pulmonary heart disease | 98.40% | L4 | One rat study on alveolar fluid reabsorption; weak link. |
| Primary hereditary glaucoma | 92.06% | L5 | No trials or literature. |
| Open-angle glaucoma | 87.41% | L5 | No trials or literature. |
| Chronic renal failure syndrome | 85.53% | L3 | One Phase 4 trial and pharmacokinetic studies. These mainly show a safety constraint, not efficacy (see below). |

**Chronic pulmonary heart disease (L4):**
- A double-blind crossover study in 11 heart failure patients on digoxin found that amiloride improved hemodynamics ([PMID 1888694](https://pubmed.ncbi.nlm.nih.gov/1888694/), 1991).
- A randomised crossover trial in 14 patients compared captopril alone with furosemide plus amiloride in mild heart failure ([PMID 2888942](https://pubmed.ncbi.nlm.nih.gov/2888942/), 1987).
- Both studied congestive heart failure, not cor pulmonale.

**Chronic renal failure syndrome (L3):**
- The one relevant trial is [NCT02832973](https://clinicaltrials.gov/study/NCT02832973), a completed Phase 4 study (n=72) of sequential nephron blockade in resistant hypertension.
- Its title alone does not confirm the amiloride arm, the CKD population or the randomisation.
- Amiloride clearance falls in renal impairment, and early renal failure limits its use ([PMID 3987787](https://pubmed.ncbi.nlm.nih.gov/3987787/), 1985; [PMID 3428342](https://pubmed.ncbi.nlm.nih.gov/3428342/), 1987).

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN06538P | AA-AMILZIDE TABLET | Tablet (oral) | Apotex Inc |

## Safety Considerations

- **Hyperkalaemia risk in renal impairment:** Amiloride clearance is reduced in renal failure, which prolongs its half-life. Published work cautions against its use in early renal failure ([PMID 3987787](https://pubmed.ncbi.nlm.nih.gov/3987787/), [PMID 3428342](https://pubmed.ncbi.nlm.nih.gov/3428342/)).
- **Potassium-raising co-medication:** A case report describes severe hyperkalaemia (serum potassium 9.3 mEq/L) in a geriatric patient on trimethoprim-sulfamethoxazole ([PMID 8615380](https://pubmed.ncbi.nlm.nih.gov/8615380/)). The report is included here as a general potassium-safety signal.

Package insert warnings, contraindications and drug interaction data were not retrieved. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction has a very high model score but no trials or literature, so it is at L5.
- Amiloride's main risk in kidney-related uses is hyperkalaemia, which weighs against moving forward without direct evidence.

**To proceed, the following is needed:**
- The HSA package insert, with warnings and contraindications (currently a blocking gap).
- Mechanism-of-action data from DrugBank.
- Direct clinical or preclinical evidence for amiloride in malignant hypertensive renal disease.
- If the team pursues the better-supported candidates (chronic renal failure syndrome, chronic pulmonary heart disease), a research question with strict potassium and eGFR guardrails.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

