---
layout: default
title: Felodipine
parent: Medium Evidence (L3-L4)
nav_order: 420
evidence_level: L4
indication_count: 10
---

# Felodipine
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

# Felodipine: From Hypertension to Pulmonary Hypertension Owing to Lung Disease and/or Hypoxia

## One-Sentence Summary

Felodipine is an L-type calcium channel blocker originally used to treat hypertension.
The TxGNN model predicts it may be effective for **pulmonary hypertension owing to lung disease and/or hypoxia** with a very high score, but **no clinical trials** are registered and the 9 publications retrieved are all preclinical or ex vivo studies.
This top-ranked prediction rests on model output alone, so the evidence is weak. Other predicted indications, notably cerebrovascular disorder and Prinzmetal angina, have much stronger supporting evidence (see the end of this report).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder); the Singapore licence records list no indication text |
| Predicted New Indication | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, felodipine is a dihydropyridine L-type calcium channel blocker with vasodilatory activity. Its efficacy in hypertension is established, and mechanistically it may be applicable to pulmonary vascular disease.

Hypoxic pulmonary vasoconstriction is partly calcium-dependent, so a calcium channel blocker could plausibly lower pulmonary vascular tone. However, the retrieved literature does not address pulmonary hypertension directly. It consists of hypoxia or anoxia experiments in rat kidney tubules, human atrial muscle, cerebral arteries and rodent behaviour models.

There is also a safety concern. In patients with lung disease, dihydropyridine calcium channel blockers may blunt hypoxic pulmonary vasoconstriction and worsen gas exchange. The very high TxGNN score is therefore not backed by direct clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

All retrieved publications for this indication are preclinical or ex vivo studies. None is a clinical study in pulmonary hypertension.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8584414](https://pubmed.ncbi.nlm.nih.gov/8584414/) | 1995 | Preclinical (rat tubules) | Pflugers Arch | Felodipine protected isolated rat proximal tubules from hypoxic injury through a calcium-independent mechanism |
| [9431863](https://pubmed.ncbi.nlm.nih.gov/9431863/) | 1997 | Ex vivo (human atrial muscle) | Int J Cardiol | Felodipine pretreatment protected human atrial muscle from hypoxia-reoxygenation dysfunction in an in vitro stunning model |
| [8394565](https://pubmed.ncbi.nlm.nih.gov/8394565/) | 1993 | Preclinical | Pflugers Arch | Effect of felodipine and a verapamil analogue on anoxia-induced rises in intracellular calcium in rabbit proximal tubule cells |
| [3961832](https://pubmed.ncbi.nlm.nih.gov/3961832/) | 1986 | Animal study | Stroke | Felodipine and nifedipine depressed the anoxia-induced increase in cerebral blood flow in rats |
| [3343292](https://pubmed.ncbi.nlm.nih.gov/3343292/) | 1988 | Animal study | J Cereb Blood Flow Metab | Both drugs suppressed hypoxia-evoked adenosine and inosine release from rat cerebral cortex |
| [8110031](https://pubmed.ncbi.nlm.nih.gov/8110031/) | 1993 | Animal behavioural study | Arch Int Pharmacodyn Ther | Effects of three calcium channel blockers on passive avoidance behaviour in intact and hypoxia-exposed rats |
| [8160846](https://pubmed.ncbi.nlm.nih.gov/8160846/) | 1994 | Preclinical (vascular) | Am J Physiol | A prior anoxic episode attenuated vasorelaxation to a later anoxic episode in rat aortic rings |
| [3142891](https://pubmed.ncbi.nlm.nih.gov/3142891/) | 1988 | Preclinical (cerebral arteries) | J Cereb Blood Flow Metab | Reoxygenation and calcium-induced contractions in dog cerebral arteries as affected by vasodilators |
| [9864178](https://pubmed.ncbi.nlm.nih.gov/9864178/) | 1999 | Preclinical | Blood | Nitric oxide augmented free radical generation by rat white cells after hypoxia-reoxygenation |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08768P | PLENDIL TABLET 10 mg | Tablet, extended release | Not stated in the licence record |
| SIN07738P | PLENDIL TABLET 2.5 mg | Tablet, extended release | Not stated in the licence record |
| SIN08781P | PLENDIL TABLET 5 mg | Tablet, extended release | Not stated in the licence record |

All three licences are valid single-ingredient oral products from AstraZeneca Pharmaceutical Co. Ltd and Saneca Pharmaceuticals a.s.

## Safety Considerations

- **Contraindication signals from the knowledge graph** (not package insert text): kidney disease, liver disease, gallbladder disease, angioedema (several forms), neutropenia and agranulocytosis, aortic stenosis, hypotensive disorder, hypertrophic cardiomyopathy, renal artery obstruction, myocardial infarction, coronary artery disease and atherosclerosis. These need verification against the label.
- **Drug interactions** (100 recorded; examples from the first 20 shown):
  - **Major:** dolasetron.
  - **Moderate:** corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), cimetidine, clarithromycin, aprepitant, bupropion, morphine, acetylsalicylic acid, SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), calcium salts, magnesium sulfate, dronabinol and nabilone.
- **Disease-specific concern:** possible worsening of gas exchange in lung disease, plus fluid retention and reflex tachycardia.

Package insert warnings and contraindications could not be obtained for this report. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, pulmonary hypertension owing to lung disease and/or hypoxia, has no clinical trials and only preclinical or ex vivo literature (L4). Dihydropyridine calcium channel blockers may also worsen oxygenation in patients with lung disease. The 99.91% TxGNN score is not supported by direct clinical data.

**Other predicted indications worth noting:**

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation | Comment |
|------|------|------|------|------|
| Cerebrovascular disorder | 98.47% | L1 | Proceed with Guardrails | The FEVER trial (9,711 Chinese hypertensive patients, randomized, double-blind, placebo-controlled) and the HOT study support stroke prevention. The benefit is largely from blood pressure lowering, so it overlaps with the approved indication. No registry trial data were provided. |
| Prinzmetal angina | 99.07% | L2 | Proceed with Guardrails | Small comparative and provocation studies, including once-daily felodipine versus four-times-daily nifedipine, with surrogate endpoints and no Phase 3 outcome RCT. |
| Chronic pulmonary heart disease | 99.19% | L3 | Research question | Small haemodynamic studies in severe COPD showed reductions in pulmonary and systemic vascular resistance. These are physiological studies, not outcome trials. |
| Other predictions | — | L5 | Hold | Pulmonary hypertension of unclear mechanism, malignant renovascular hypertension, malignant hypertensive renal disease, Braddock syndrome, spinal cord ischemia and obsolete susceptibility to ischemic stroke are prediction only. Several largely restate the existing hypertension indication. |

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which block safety screening
- Mechanism of action data
- For pulmonary hypertension: controlled haemodynamic or outcome studies in the target population, with attention to oxygenation
- For cerebrovascular disorder and Prinzmetal angina: a review of the full trial data and a clear definition of how the new use differs from the approved hypertension indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

