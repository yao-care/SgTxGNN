---
layout: default
title: Tropicamide
parent: Low Evidence (L5)
nav_order: 1032
evidence_level: L5
indication_count: 10
---

# Tropicamide
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

# Tropicamide: From Cycloplegia to Cauda Equina Syndrome

## One-Sentence Summary

Tropicamide is a short-acting antimuscarinic eye drop, originally used for cycloplegia and pupil dilation during eye examinations.
The TxGNN model predicts it may be effective for **cauda equina syndrome**, but **no clinical trials and no supporting publications** exist for this prediction.
It is a computational prediction only, and the mechanistic rationale is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cycloplegia (the Singapore licence records contain no approved-indication text) |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.53% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tropicamide is a muscarinic receptor antagonist. Pharmacology data list activity at the M2, M3, M4 and M5 receptors, and its established clinical use is as a short-acting mydriatic for examining the lens, vitreous humour and retina.

In theory, blocking muscarinic receptors could affect bladder (detrusor) and bowel function, which are disrupted in cauda equina syndrome. However, cauda equina syndrome is a surgical emergency caused by compression of the nerve roots. A topical eye drop with minimal systemic exposure has no plausible role in changing the course of the disease. The high score reflects a network-based computational association, not demonstrated benefit.

Other top-ranked predictions are also weak:
- **Neurogenic bladder, irritable bowel syndrome, nasal cavity disease and nasopharyngitis**: class-level antimuscarinic plausibility only. There is no tropicamide-specific data and no suitable formulation. Approved agents such as oxybutynin already serve the bladder indication.
- **Primary hereditary glaucoma**: pharmacologically contradictory. Tropicamide can raise intraocular pressure or precipitate angle closure, so this is a safety concern rather than an opportunity.
- **Allergic urticaria**: the only retrieved paper reports anaphylaxis from a different mydriatic (cyclopentolate), which is an adverse reaction and not evidence of benefit.
- **Pharyngitis, acute laryngopharyngitis and recalcitrant atopic dermatitis**: no credible mechanism. Drying effects could even be undesirable.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for cauda equina syndrome.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04202P | MINIMS TROPICAMIDE EYE DROPS 1% w/v | Solution | Not stated in the licence record |
| SIN04715P | MYDRIACYL STERILE OPHTHALMIC SOLUTION 1% | Solution | Not stated in the licence record |

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: the knowledge graph links tropicamide with caution or contraindication in the following conditions:
  - Eye: open-angle glaucoma, angle-closure (closed-angle) glaucoma, ocular hypertension
  - Cardiovascular: hypertension and hypertensive disorder, sudden cardiac arrest, heart conduction disease, myocardial ischemia, coronary artery disease
  - Metabolic: diabetes mellitus, diabetic ketoacidosis
  - Thyroid: hyperthyroidism, Graves disease, thyrotoxicosis
- **Drug Interactions**: 10 interactions were recorded in the DDInter database, all with unclassified severity. They involve atropine, potassium chloride, vancomycin, simvastatin, prednisolone, famotidine, warfarin, lidocaine, fluconazole and brimonidine. Additive anticholinergic effects with atropine are the most mechanistically obvious. Pharmacology records also show binding to the M2 to M5 muscarinic receptors.
- **Hypersensitivity signal**: a published case report of anaphylaxis with the related mydriatic cyclopentolate suggests hypersensitivity is a possible class concern, although rare.

Please also refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (evidence level L5). There are no trials or publications, and the mechanism is implausible for a topical ophthalmic antimuscarinic in a compression-related surgical emergency. None of the other top-ten predictions has stronger support.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- Evidence of a plausible disease mechanism and a suitable route of administration (route compatibility has not been assessed)
- Any preclinical or clinical studies in the predicted indication
- Consideration of other predictions only if a credible mechanism and systemic-exposure safety data are available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

