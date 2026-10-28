---
layout: default
title: Adenosine
parent: Low Evidence (L5)
nav_order: 41
evidence_level: L5
indication_count: 1
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-10-28
description: "Adenosine: predicted new indication obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Adenosine: adenosine receptor agonist (AV nodal conduction slowing) → obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Adenosine is an injectable drug that acts on adenosine receptors and slows conduction through the atrioventricular (AV) node.
The TxGNN model predicts it may be effective for **obsolete bundle branch block**, but **no clinical trials and no publications** currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete bundle branch block |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, adenosine slows conduction through the AV node, which is the basis of its use as an injectable antiarrhythmic.

The mechanistic fit with bundle branch block is weak. Bundle branch block is a conduction defect located below the AV node, so slowing AV nodal conduction does not clearly address it. The disease term is also marked as obsolete, which suggests the high score (0.9994) may reflect an ontology artifact rather than a true therapeutic signal. The prediction should be treated as a model output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16391P | CADEN SOLUTION FOR INJECTION 6 MG / 2 ML | Injection, solution | Not recorded |
| SIN07679P | ADENOCOR INJECTION 3MG/ML | Injection | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interacting drugs were identified. Major-level interactions include:
  - Cisapride
  - Dolasetron
  - Papaverine

  Moderate-level interactions include famotidine, clarithromycin, granisetron, levofloxacin, ondansetron and palonosetron. Several QT-prolonging agents appear in this list, so combined use warrants caution.
- **Conditions of concern in the data compiled for this report**: Asthma and chronic obstructive pulmonary disease, aortic stenosis, atrioventricular block, sick sinus syndrome, acute coronary syndrome, coronary artery disease, hypotensive disorder, respiratory failure, pericarditis and mitral valve stenosis are listed as conditions where use may be problematic. These come from relationship data and are not label text; check the package insert.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5). The mechanistic rationale is weak, since the conduction defect lies below the AV node, and the disease term is obsolete. Adenosine may also worsen conduction in related conditions such as atrioventricular block and sick sinus syndrome.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data
- Confirmation of a current, valid disease term to replace the obsolete one
- Any clinical or preclinical studies that directly address this disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

