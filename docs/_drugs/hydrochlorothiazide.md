---
layout: default
title: Hydrochlorothiazide
parent: Low Evidence (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydrochlorothiazide: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder, hypertension, congestive heart failure"
monitor_inn: "Hydrochlorothiazide"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "primary hereditary glaucoma", "open-angle glaucoma", "hypotrichosis simplex of the scalp"]
---

# Hydrochlorothiazide
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

# Hydrochlorothiazide: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Hydrochlorothiazide is a thiazide diuretic, originally used to treat hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, congestive heart failure (the approved indication text in the Singapore licence records is blank, so this comes from the knowledge graph) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 98.42% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, hydrochlorothiazide is a thiazide diuretic with established efficacy in hypertension and heart failure. Mechanistically, it may be relevant to hypertensive kidney disease because it lowers blood pressure and reduces volume load.

The link is conceptual, however. Malignant hypertension is a hypertensive emergency that is usually managed with rapid-acting parenteral agents, and thiazides are not standard therapy in that setting. The high score most likely reflects the drug's existing hypertension indication rather than new evidence.

Other predictions in the same set show a similar pattern:

- **Malignant renovascular hypertension** (98.42%): a hypertension subtype that overlaps with the approved use. No evidence was provided.
- **Pulmonary hypertension** (98.35%): pulmonary pressure is regulated differently from systemic pressure, and thiazides have no established pulmonary vasodilatory action. The one safety signal found was a case report of hydrochlorothiazide-associated pulmonary edema.
- **Chronic pulmonary heart disease** (97.80%) and **acute pulmonary heart disease** (93.17%): diuretics may relieve congestion in right heart failure, which gives indirect plausibility. This is supportive, not disease-modifying, and both are classed as research questions (L4).
- **Glaucoma, Braddock syndrome and hypotrichosis simplex of the scalp**: no mechanism is established, and these are likely graph artifacts. Hydrochlorothiazide's weak carbonic anhydrase inhibitory activity is a speculative link to open-angle glaucoma.

## Clinical Trial Evidence

Currently no clinical trials are registered for the top predicted indication, malignant hypertensive renal disease.

For reference, the only trial found among the other predictions relates to acute pulmonary heart disease and is indirect:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07469722](https://clinicaltrials.gov/study/NCT07469722) | Phase 2/3 | Not yet recruiting | 128 | Ultrasound-guided diuretic strategy in acute decompensated heart failure. It tests a strategy rather than hydrochlorothiazide, and targets heart failure rather than acute cor pulmonale. |

## Literature Evidence

Currently no related literature is available for malignant hypertensive renal disease.

The most relevant publications found for other predicted indications are listed below. They give only indirect support.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11219471](https://pubmed.ncbi.nlm.nih.gov/11219471/) | 2001 | RCT | Clin Ther | Telmisartan vs atenolol, with hydrochlorothiazide added as required, in mild to moderate hypertension |
| [38215973](https://pubmed.ncbi.nlm.nih.gov/38215973/) | 2024 | Post hoc analysis | Rev Clin Esp | CLOROTIC trial: adding hydrochlorothiazide to furosemide improved diuretic response in acute heart failure; sex-difference analysis |
| [36595088](https://pubmed.ncbi.nlm.nih.gov/36595088/) | 2023 | Review | Eur J Pediatr | Overview of diuretic indications, mechanisms and side effects in children |
| [28711447](https://pubmed.ncbi.nlm.nih.gov/28711447/) | 2017 | Review | JACC Heart Fail | Transition from hypertension to heart failure |
| [2766837](https://pubmed.ncbi.nlm.nih.gov/2766837/) | 1989 | Case report | Chest | Low-pressure pulmonary edema after a triamterene-hydrochlorothiazide tablet (safety signal) |
| [2924690](https://pubmed.ncbi.nlm.nih.gov/2924690/) | 1989 | Small randomised crossover | Dtsch Med Wochenschr | Hydrochlorothiazide + triamterene vs digitalis in chronic heart failure (16 patients) |

## Singapore Market Information

There are 20 valid single-licence registrations, all oral tablets. The approved indication text is not recorded in the licence data. The first five are shown below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01959P | HYDROZIDE TABLET 50 mg | Tablet | Not recorded |
| SIN00108P | DI-ERTRIDE TABLET 25 mg | Tablet | Not recorded |
| SIN03676P | APO-HYDROCHLOROTHIAZDE TABLET 25 mg | Tablet | Not recorded |
| SIN03675P | APO-HYDROCHLOROTHIAZIDE TABLET 50 mg | Tablet | Not recorded |
| SIN09429P | HYZAAR TABLET | Film-coated tablet | Not recorded |

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not label text): liver failure, liver disease, cirrhosis, kidney disease, pancreatitis, gallbladder disease, porphyria, systemic lupus erythematosus, angioedema (including hereditary and RAAS-blocker-induced), autoimmune hemolytic anemia, peptic ulcer disease, myopathy, familial periodic paralysis, epilepsy, asthma, bronchitis, anxiety and neurotic disorders.
- **Drug Interactions**: 100 interactions were found. Most of those listed are moderate, including acarbose, rabeprazole, hydrocortisone, albiglutide, alogliptin, amphotericin B formulations, bupropion, bisacodyl, vitamin D analogues (cholecalciferol, calcifediol, calcitriol) and several corticosteroids. Doxycycline and atropine are minor.
- **Literature safety signal**: a case report of hydrochlorothiazide-associated pulmonary edema.

Please also refer to the package insert, as label warnings and contraindications were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials or publications for malignant hypertensive renal disease, and standard care for this emergency uses rapid-acting parenteral agents. The prediction most likely reflects the existing hypertension indication rather than new evidence, so the evidence level is L5. The pulmonary heart disease indications (L4, research questions) are the only ones with even indirect support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are required for safety screening
- Detailed mechanism of action data from DrugBank
- Clinical evidence specific to hydrochlorothiazide in hypertensive renal disease or malignant hypertension
- A clear clinical rationale for how a thiazide would add value over existing standard therapy
- Direct hydrochlorothiazide data in cor pulmonale or right heart failure, if the pulmonary heart disease indications are pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

