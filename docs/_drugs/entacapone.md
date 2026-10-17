---
layout: default
title: Entacapone
parent: Low Evidence (L5)
nav_order: 378
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entacapone: predicted new indication PLA2G6-associated neurodegeneration (evidence level L5). Approved use: Parkinson disease (and related parkinsonian syndromes)"
monitor_inn: "Entacapone"
predicted_indications: ["PLA2G6-associated neurodegeneration", "Rasmussen subacute encephalitis", "myelitis", "transaldolase deficiency", "lethal infantile mitochondrial myopathy", "Lewy body dementia", "fructose-1,6-bisphosphatase deficiency", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "progressive supranuclear palsy-corticobasal syndrome"]
---

# Entacapone
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

# Entacapone: From Parkinson Disease to PLA2G6-Associated Neurodegeneration

## One-Sentence Summary

Entacapone is a COMT inhibitor used alongside levodopa, originally for Parkinson disease and related parkinsonian syndromes.
The TxGNN model predicts it may be effective for **PLA2G6-associated neurodegeneration**,
but **no clinical trials and no publications** currently support this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease (and related parkinsonian syndromes) |
| Predicted New Indication | PLA2G6-associated neurodegeneration |
| TxGNN Prediction Score | 99.76% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, entacapone is a catechol-O-methyltransferase (COMT) inhibitor. It extends the effect of levodopa, and its efficacy in Parkinson disease is established. Mechanistically, it may be applicable to neurodegenerative conditions that include parkinsonian features.

PLA2G6-associated neurodegeneration includes dystonia-parkinsonism phenotypes, so a dopaminergic or COMT-inhibitor rationale is conceivable. However, entacapone has no known effect on the underlying PLA2G6 lipid-metabolism defect. It only prolongs levodopa action, so any benefit would at most be symptomatic. The high score may reflect the closeness of this disease to parkinsonian conditions in the knowledge graph rather than independent evidence.

Other top-ranked predictions are mostly weak or implausible. Examples are Rasmussen encephalitis, myelitis, transaldolase deficiency and fructose-1,6-bisphosphatase deficiency, for which no mechanistic link was identified. "Paralysis agitans, juvenile, of Hunt" is a historical term for juvenile parkinsonism and largely overlaps with the original indications. Two predictions have limited indirect support and are worth noting as research questions:
- **Lewy body dementia** (score 99.25%): shares alpha-synuclein pathology and dopaminergic deficits with Parkinson disease. Support is preclinical only.
- **Progressive supranuclear palsy-corticobasal syndrome** (score 99.04%): conceptually plausible, but levodopa response is typically poor in these conditions.

## Clinical Trial Evidence

Currently no related clinical trials registered for PLA2G6-associated neurodegeneration.

For the lower-ranked predictions, the only trials found do not test entacapone:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04246437](https://clinicaltrials.gov/study/NCT04246437) | Phase 1 | Recruiting | 40 | [18F]F-DOPA imaging in autonomic failure (Lewy body dementia prediction). Diagnostic study, no entacapone efficacy or safety data |
| [NCT02994719](https://clinicaltrials.gov/study/NCT02994719) | N/A | Active, not recruiting | 120 | Observational gait analysis in neurological disease (PSP-corticobasal syndrome prediction). No entacapone intervention |

## Literature Evidence

Currently no related literature available for PLA2G6-associated neurodegeneration.

For the Lewy body dementia prediction, only preclinical work was found:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23913715](https://pubmed.ncbi.nlm.nih.gov/23913715/) | 2013 | In vitro study | J Neurosci Res | Effects of antiparkinsonian agents on β-amyloid and α-synuclein oligomer formation |
| [39259788](https://pubmed.ncbi.nlm.nih.gov/39259788/) | 2024 | Preclinical (iPSC organoid) | Sci Adv | Lewy body disease model with SNCA triplication cortical organoids, used to identify therapeutic drugs |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16544P | Encapia Film Coated Tablets 200mg | Film-coated tablet | Not specified |
| SIN11234P | Comtan Tablet 200 mg | Film-coated tablet | Not specified |
| SIN13142P | Stalevo Film Coated Tablets 100/25/200 mg | Film-coated tablet | Not specified |
| SIN16957P | Antipar Film Coated Tablet 150 mg/37.5 mg/200 mg | Film-coated tablet | Not specified |
| SIN13141P | Stalevo Film Coated Tablets 150/37.5/200 mg | Film-coated tablet | Not specified |

Three more valid registrations exist (Stalevo 50/12.5/200 mg, Stalevo 200/50/200 mg, Antipar 100/25/200 mg). All 8 are oral film-coated tablets.

## Safety Considerations

- **Knowledge-graph contraindication signals** (these come from the knowledge graph, not from label text, and should be checked against the package insert):
  - Cardiovascular: myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, postural orthostatic tachycardia syndrome
  - Neurological and psychiatric: epilepsy, drug-induced dyskinesia, multiple system atrophy, psychotic disorders, schizoaffective disorder, anxiety disorder
  - Organ function: liver disease, kidney disease, gallbladder disease
  - Gastrointestinal: peptic ulcer disease, gastric ulcer, diarrheal disease
  - Eye: open-angle and angle-closure glaucoma
  - Metabolic and other: diabetes mellitus, diabetic ketoacidosis, melanoma, hemoglobinopathy
- **Drug interactions**: 82 interactions were recorded. The Moderate-level ones include epinephrine (including ophthalmic and topical forms), morphine (including liposomal), dronabinol, opium, nabilone, metoclopramide and iron. Several others have an unclassified level, such as pantoprazole, omeprazole, lansoprazole, doxycycline, metformin, atropine, prednisone and simvastatin.
- A related COMT inhibitor, tolcapone, carries hepatotoxicity concerns. This calls for careful safety review in any new use involving mitochondrial or hepatic disease.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for PLA2G6-associated neurodegeneration has a high model score but no trials, no literature and only a speculative symptomatic rationale (Evidence Level L5). Among the other predictions, Lewy body dementia and PSP-corticobasal syndrome could be framed as research questions, but their supporting evidence is preclinical or non-interventional.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, since safety screening cannot start without them
- Mechanism of action data for entacapone
- Published case series or preclinical data on COMT inhibition or levodopa adjuncts in PLA2G6-associated neurodegeneration
- Interventional trials of entacapone, or levodopa with a COMT inhibitor, in Lewy body dementia, if that direction is pursued
- A review of the knowledge-graph contraindication signals, especially cardiovascular, hepatic and psychiatric conditions, against the product label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

