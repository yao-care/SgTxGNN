---
layout: default
title: Magnesium Chloride
parent: 僅模型預測 (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Magnesium Chloride
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

# Magnesium Chloride: From Electrolyte Replacement to Congestive Heart Failure

## One-Sentence Summary

Magnesium chloride (MgCl₂) is an inorganic salt used clinically as an electrolyte replacement agent to correct hypomagnesaemia, a condition frequently arising in patients on long-term diuretic therapy.
The TxGNN model predicts it may be effective for **congestive heart failure (CHF)**, supported by a mechanistically compelling rationale: CHF patients are prone to diuretic-induced magnesium wasting, and MgCl₂ oral supplementation has been shown to reduce arrhythmia risk and improve myocardial function.
Current evidence includes **1 directly relevant small clinical trial** (PMID 8237806) and **multiple observational and review publications**, placing overall support at **Evidence Level L3**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Electrolyte replacement / correction of hypomagnesaemia (no formal Singapore registration) |
| Predicted New Indication | Congestive Heart Failure |
| TxGNN Prediction Score | 97.07% |
| Evidence Level | L3 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Magnesium is the second most abundant intracellular cation and plays a critical role in cardiac electrophysiology. It stabilises cell membrane potential, regulates the Na⁺/K⁺-ATPase pump, and acts as a physiological antagonist to voltage-gated calcium channels. In cardiomyocytes, adequate Mg²⁺ is essential for normal action potential duration and prevention of triggered arrhythmias such as torsades de pointes.

In congestive heart failure, the use of loop diuretics (e.g. furosemide) and thiazides is the standard of care for decongestion. However, these agents promote urinary wasting of magnesium alongside potassium and sodium. The resulting hypomagnesaemia significantly increases susceptibility to ventricular ectopy, Q-T prolongation, and sudden cardiac death — complications that contribute substantially to the high CHF mortality burden. Animal studies further confirm that dietary magnesium deficiency alone can induce a reversible, metabolic diastolic cardiomyopathy (PMID 34096318).

Magnesium chloride, as the most bioavailable oral magnesium salt, is well-positioned to correct this deficiency. A landmark randomised crossover trial (PMID 8237806) directly studied long-term oral MgCl₂ replacement in 21 CHF patients on loop diuretics, demonstrating restoration of serum and tissue magnesium levels and associated antiarrhythmic benefits. Combined with its synergistic effect on potassium repletion (refractory hypokalaemia often resolves only after magnesium correction), the mechanistic case for MgCl₂ supplementation in CHF is biologically plausible and clinically grounded.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03980574](https://clinicaltrials.gov/study/NCT03980574) | N/A | Completed | 10 | Pilot crossover study of dietary supplementation (potentially including magnesium) in CHF patients with and without diabetes; assessed 6-minute walk distance and readmission rates |
| [NCT03439514](https://clinicaltrials.gov/study/NCT03439514) | Phase 3 | Terminated | 77 | Dilated cardiomyopathy (LMNA mutation) treated with p38α MAPK inhibitor ARRY-371797; indication relevant but intervention unrelated to MgCl₂ |
| [NCT02560519](https://clinicaltrials.gov/study/NCT02560519) | Phase 4 | Completed | 1,386 | Albumin vs Ringer's lactate (containing Mg²⁺) in cardiac surgery; large study exploring electrolyte-containing crystalloids, though primary endpoint was colloid selection |
| [NCT04393493](https://clinicaltrials.gov/study/NCT04393493) | Phase 2 | Completed | 80 | Two furosemide strategies in type 1 cardiorenal syndrome; relevant to diuretic-electrolyte context in CHF |
| [NCT03031496](https://clinicaltrials.gov/study/NCT03031496) | Phase 1 | Completed | 42 | Bioequivalence study of hydrochlorothiazide/amiloride for CHF, hypertension, and cirrhosis with ascites; electrolyte-sparing diuretic context relevant |
| [NCT07163936](https://clinicaltrials.gov/study/NCT07163936) | N/A | Not Yet Recruiting | 80 | Citrate-based dialysate with added magnesium to prevent vascular calcification in CKD; directly tests Mg²⁺ supplementation in a related cardiovascular-renal population |
| [NCT06021860](https://clinicaltrials.gov/study/NCT06021860) | Phase 4 | Unknown | 96 | Spironolactone oral suspension PK/PD in paediatric oedema due to heart failure or cirrhosis; electrolyte management context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8237806](https://pubmed.ncbi.nlm.nih.gov/8237806/) | 1993 | Controlled Trial (RCT crossover) | Am J Cardiology | Long-term oral MgCl₂ replacement in 21 CHF patients on loop diuretics restored serum Mg and reduced arrhythmia susceptibility; **only direct trial of oral MgCl₂ in CHF** |
| [2755214](https://pubmed.ncbi.nlm.nih.gov/2755214/) | 1989 | Controlled Trial | Magnesium | K⁺ alone vs K⁺+Mg combination in CHF on hydrochlorothiazide; demonstrated that combined K⁺-Mg supplementation more effectively corrected hypokalaemia |
| [40530753](https://pubmed.ncbi.nlm.nih.gov/40530753/) | 2025 | Review | Eur J Heart Failure | Comprehensive review of water and electrolyte homeostasis during decongestion in CHF; highlights that Mg²⁺/K⁺ co-depletion is a key consequence of loop diuretic use |
| [8861138](https://pubmed.ncbi.nlm.nih.gov/8861138/) | 1995 | Critical Review | Magnesium Research | Antiarrhythmic actions of magnesium in CHF; epidemiological evidence for Mg deficit in sudden cardiac death, enzymatic roles in myocyte function |
| [34096318](https://pubmed.ncbi.nlm.nih.gov/34096318/) | 2021 | Preclinical Study | J Am Heart Assoc | Low-Mg diet in C57BL/6J mice produced reversible diastolic cardiomyopathy; fully reversed upon Mg repletion — establishes direct causal link between Mg deficiency and cardiac dysfunction |
| [2650515](https://pubmed.ncbi.nlm.nih.gov/2650515/) | 1989 | Review | Am J Cardiology | Cardiovascular consequences of Mg deficiency: arterial/myocardial lesions, atherogenesis, thrombogenesis; Mg and Cl⁻ loss complicates K⁺ repletion |
| [4091044](https://pubmed.ncbi.nlm.nih.gov/4091044/) | 1985 | Observational | Acta Med Scandinavica | 108 CHF/hypertension patients on long-term diuretics showed consistent Mg and K⁺ depletion in skeletal muscle even with normal serum levels |
| [2309624](https://pubmed.ncbi.nlm.nih.gov/2309624/) | 1990 | Review | Am J Cardiology | Diuretic-electrolyte interaction in CHF; kaliuresis worsens with continued therapy, Mg depletion underlies refractory hypokalaemia |
| [25660927](https://pubmed.ncbi.nlm.nih.gov/25660927/) | 2015 | Review | J Am Coll Cardiology | Depletional hyponatraemia in acute decompensated CHF driven by diuretics; Mg/K supplementation recommended when plasma levels are low |
| [2436474](https://pubmed.ncbi.nlm.nih.gov/2436474/) | 1987 | Review | Am J Medicine | Potassium and magnesium depletion from diuretic therapy; serum levels can appear normal despite significant tissue depletion, underscoring need for empirical supplementation |

---

## Singapore Market Information

Magnesium chloride (DB09407) currently has **no registered products** with the Health Sciences Authority (HSA) in Singapore. The drug is not approved or commercially marketed in Singapore under any dosage form or indication.

There are no authorization records to display.

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore HSA-specific warnings, contraindications, or drug interaction data were retrievable for this submission. Clinicians should consult the relevant product monograph and standard pharmacology references before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic and epidemiological case for magnesium chloride in congestive heart failure is strong — diuretic-induced hypomagnesaemia is well-documented, MgCl₂ oral replacement has been directly studied in CHF in a small RCT (PMID 8237806) with positive signals, and animal data confirm that Mg deficiency alone can cause reversible cardiomyopathy. However, evidence remains at Level L3 (observational and small controlled studies), with no large-scale Phase 2/3 RCT specifically evaluating oral MgCl₂ supplementation as an adjunct in CHF management.

**To proceed, the following is needed:**

- **Safety data retrieval**: Obtain and review the MgCl₂ product monograph / prescribing information to confirm contraindications (e.g. renal impairment, hypermagnesaemia) and drug interactions (e.g. with digoxin, aminoglycosides)
- **Singapore regulatory pathway**: Determine if MgCl₂ oral formulation can be registered as a supplement or prescription product via HSA; assess GMP-compliant supply chain
- **Dose-finding clarification**: The 1993 trial (PMID 8237806) used oral MgCl₂ at a specific replacement dose — confirm optimal dosing, frequency, and target serum Mg levels for CHF
- **Renal function gating**: Mg supplementation is contraindicated in significant renal impairment (eGFR < 30 mL/min typically); a patient selection framework is required
- **Larger prospective study**: Design a Phase 2 RCT evaluating oral MgCl₂ supplementation (vs placebo) in CHF patients on loop diuretics, with endpoints of serum Mg normalisation, arrhythmia burden (24-hour Holter), hospitalisation rates, and NYHA class
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

