---
layout: default
title: Digoxin
parent: Low Evidence (L5)
nav_order: 330
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "Digoxin"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "hypoalphalipoproteinemia"]
description: "Digoxin: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Digoxin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Digoxin: Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Digoxin is a cardiac glycoside originally used to treat atrial fibrillation and digitalis poisoning.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but this is a model prediction only, with **0 clinical trials** and **1 publication** (an unrelated review), so supporting evidence is very weak.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 5 of 5) |
| Number of Registrations | 5 (valid: 5) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Digoxin is generally known as a Na+/K+-ATPase inhibitor. This raises intracellular calcium and produces a vagotonic effect, which is the basis of its use for rate control in atrial fibrillation.

The link to Prinzmetal (vasospastic) angina is weak. Standard therapy for vasospastic angina relies on calcium channel blockers and nitrates. Digoxin raises intracellular calcium, which could in theory promote vasospasm rather than relieve it. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The only retrieved publication is a 1999 review on chronopharmacology of antihypertensive treatment. It does not show that digoxin is useful in vasospastic angina.

Other top-ranked predictions are also unsupported. These include duodenal obstruction, duodenal ulcer, duodenogastric reflux, hypoalphalipoproteinemia, homozygous familial hypercholesterolemia and nephrogenic syndrome of inappropriate antidiuresis. None provides a plausible repurposing signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | Chronopharmacology and its impact on antihypertensive treatment; no direct evidence for digoxin in Prinzmetal angina |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01198P | LANOXIN TABLET 0.25 mg | Tablet | Not stated in the licence record |
| SIN17078P | DIGOKERN TABLETS 0.25MG | Tablet | Not stated in the licence record |
| SIN00544P | LANOXIN PAEDIATRIC/GERIATRIC ELIXIR 0.05 mg/ml | Elixir | Not stated in the licence record |
| SIN01203P | LANOXIN-PG PAEDIATRIC/GERIATRIC TABLET 0.0625 mg | Tablet | Not stated in the licence record |
| SIN00547P | LANOXIN INJECTION 0.5 mg/2 ml | Injection | Not stated in the licence record |

Available routes: oral (tablet), other (elixir), injectable.

---

## Safety Considerations

- **Contraindications flagged in the drug-disease knowledge graph** (not label text): kidney disease, potassium deficiency, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, myocardial infarction, coronary thrombosis, hemoglobinopathy, cor pulmonale, Wolff-Parkinson-White syndrome, sick sinus syndrome, ventricular fibrillation, hypertrophic cardiomyopathy, atrioventricular block, myxedema/hypothyroidism, myocarditis, constrictive pericarditis and restrictive cardiomyopathy.
  - Several of these are cardiac conditions that overlap with the predicted new indication population, such as myocardial infarction and coronary thrombosis.
- **Drug Interactions**: 100 interactions were recorded. The main ones listed include:
  - Moderate: acarbose, rabeprazole, doxycycline, tetracycline, epinephrine, hydrocortisone, dexamethasone, betamethasone, triamcinolone, cholecalciferol, calcium phosphate, metformin, amphotericin B, bupropion, acetylsalicylic acid.
  - Minor: albiglutide, hyoscyamine, atropine, glycopyrronium.
- Digoxin has a narrow therapeutic index, and observational registry data in atrial fibrillation raise safety questions.

Please also refer to the package insert for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction rests only on a high model score (L5). There are no clinical trials, no supporting literature, and no plausible mechanism. Digoxin may even theoretically worsen vasospasm through increased intracellular calcium. The drug's narrow therapeutic index and the many knowledge-graph contraindications in cardiac disease add further concern.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing and blocking for safety screening)
- Mechanism of action data (e.g., from DrugBank) to support a mechanistic analysis
- Preclinical or clinical data showing a benefit of digoxin in vasospastic angina
- A comparison against standard therapy (calcium channel blockers, nitrates) and a safety assessment for coronary disease populations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

