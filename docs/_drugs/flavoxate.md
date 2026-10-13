---
layout: default
title: Flavoxate
parent: Low Evidence (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Flavoxate
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

# Flavoxate: From Urinary Tract Antispasmodic Use to Attention Deficit Hyperactivity Disorder (Inattentive Type)

## One-Sentence Summary

Flavoxate is a urinary tract antispasmodic marketed in Singapore as single-ingredient oral tablets.
The TxGNN model predicts it may be effective for **attention deficit hyperactivity disorder, inattentive type**, but **no clinical trials and no publications** were found to support this prediction.
The top-ranked prediction appears to be a knowledge-graph artifact, and the most mechanistically credible candidate in the list is **irritable bowel syndrome**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (all four licences have an empty indication field); flavoxate is generally known as a urinary tract antispasmodic |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, flavoxate is a urinary tract antispasmodic with antimuscarinic, phosphodiesterase-inhibiting and local anaesthetic properties.

For the top-ranked prediction, **there is no clear mechanistic link**. ADHD pathophysiology centres on dopaminergic and noradrenergic dysregulation, which flavoxate does not target. Antimuscarinic effects on the central nervous system could even worsen attention. The high score is most likely a knowledge-graph artifact. The same applies to the related predictions "attention deficit-hyperactivity disorder" (a duplicate or parent concept) and "specific developmental disorder" (likely driven by graph proximity to ADHD-related nodes).

Among the ten predictions, the more plausible ones are:

- **Irritable bowel syndrome (score 99.74%)**: Smooth muscle relaxation through antimuscarinic activity and PDE inhibition parallels other antispasmodics used in IBS, such as hyoscine and dicyclomine. This is the most mechanistically credible candidate, but it is a prediction only.
- **Neurogenic bladder (obsolete ontology term, score 99.13%)**: The bladder smooth muscle relaxant and antimuscarinic actions overlap with management of detrusor overactivity and urgency. The obsolete term needs to be mapped to a current disease concept, and better-evidenced agents such as oxybutynin exist.

The remaining predictions (cauda equina syndrome, gastroduodenitis, peptic ulcer disease, pharyngitis, chondromyxoid fibroma) have weak, indirect, or no mechanistic rationale.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12299P | LAVOXEN TABLET 200 mg | Tablet, film coated | Not stated |
| SIN09677P | CLEANXATE TAB 200 mg | Tablet, sugar coated | Not stated |
| SIN16400P | URIPAX FILM COATED TABLET 200MG | Tablet, film coated | Not stated |
| SIN12007P | URISPAS 200 TABLET 200 mg | Tablet, film coated | Not stated |

All four licences are valid single-ingredient oral products.

---

## Safety Considerations

- **Disease contraindications from the knowledge graph** (not taken from label text): angle-closure glaucoma, closed-angle glaucoma, pyloric stenosis, paralytic ileus, intestinal obstruction, familial visceral myopathy, active peptic ulcer disease, urinary tract obstruction.
- **Drug Interactions**: 74 interactions were identified. Two are rated **Major**: potassium citrate and potassium chloride. Most of the others are rated Moderate and mainly involve other anticholinergic or antimuscarinic agents (e.g., hyoscyamine, atropine, glycopyrronium, dicyclomine, scopolamine, trospium, propantheline) and agents that slow gastrointestinal motility (e.g., loperamide, morphine, eluxadoline). Others include dronabinol, nabilone, metoclopramide, pramlintide and prucalopride.

Please refer to the package insert for warnings and label contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no supporting clinical trials or literature and no plausible mechanism, and its high score is likely a graph artifact. The evidence level is L5 (model prediction only). The known antimuscarinic profile could also worsen attention, and the knowledge graph lists several contraindicated conditions.

**To proceed, the following is needed:**
- Mechanism of action data for flavoxate
- Package insert warnings and contraindications from the HSA
- The approved indication text for the Singapore licences
- If pursuing a different direction, a focused literature and trial search for **irritable bowel syndrome** (the most plausible candidate) and a mapping of the obsolete neurogenic bladder term to a current disease concept
- A review of the anticholinergic burden and the Major potassium interactions before any new use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

