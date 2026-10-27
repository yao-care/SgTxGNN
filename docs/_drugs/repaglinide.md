---
layout: default
title: Repaglinide
parent: Low Evidence (L5)
nav_order: 861
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Repaglinide: predicted new indication Opsismodysplasia (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Repaglinide"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "pancreatic agenesis", "idiopathic localized lipodystrophy", "autoimmune oophoritis"]
---

# Repaglinide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Repaglinide: From Type 2 Diabetes Mellitus to Opsismodysplasia
{: .text-alpha }

## One-Sentence Summary

Repaglinide is an oral insulin secretagogue, originally used to treat type 2 diabetes mellitus.
The TxGNN model predicts it may be effective for **Opsismodysplasia** (a rare skeletal dysplasia), but there are **0 clinical trials** and **0 relevant publications** supporting this direction. The prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (the Singapore licence records contain no indication text, so this is taken from the knowledge-graph indication data) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 98.77% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, repaglinide is a short-acting insulin secretagogue that closes ATP-sensitive potassium (K-ATP) channels on pancreatic beta cells to trigger insulin release. Its efficacy in type 2 diabetes is well established.

Opsismodysplasia is a rare skeletal dysplasia caused by mutations in *INPPL1* (SHIP2). **No mechanistic link to repaglinide has been identified.** SHIP2 is involved in insulin signalling, which may be one reason the knowledge graph connects the two, but this is a network association and not evidence of a pharmacological effect.

The high score (0.988) should therefore be read as a graph-based signal only. The other top-ranked predictions show the same pattern: they cluster around diabetes comorbidity, GAD autoimmunity, lipodystrophy and metabolic disease nodes, and none has trial or literature support. Examples include classic stiff person syndrome and focal stiff limb syndrome (score 98.48%), thiamine-responsive dysfunction syndrome (98.47%) and pancreatic agenesis (97.58%). For pancreatic agenesis, a beta-cell secretagogue would be expected to be ineffective because beta cells are absent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for opsismodysplasia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10672P | NOVONORM TABLET 0.5 mg | Tablet | Not stated in the licence record |
| SIN10673P | NOVONORM TABLET 1 mg | Tablet | Not stated in the licence record |
| SIN10674P | NOVONORM TABLET 2 mg | Tablet | Not stated in the licence record |
| SIN16376P | REPAGLINIDE MEVON TABLETS 0.5 MG | Tablet | Not stated in the licence record |
| SIN16375P | REPAGLINIDE MEVON TABLETS 1 MG | Tablet | Not stated in the licence record |

A sixth licence, SIN16374P (REPAGLINIDE MEVON TABLETS 2 MG), is also valid. All 6 licences are single-ingredient oral tablets.

## Safety Considerations

- **Contraindications (from knowledge-graph associations, not label text)**: kidney disease, liver disease, gallbladder disease, pituitary hormone deficiencies (hypopituitarism and related genetic forms), adrenal insufficiency (including Addison disease), thymus gland disease and infectious disease.
- **Drug Interactions**: 100 interactions were found in total. The ones shown are mostly Moderate, and some are Minor. Examples include:
  - Antidiabetic agents: albiglutide, alogliptin
  - Beta-agonists and sympathomimetics: salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine
  - Corticosteroids: hydrocortisone
  - Other: ethanol, ibuprofen, ketorolac, nifedipine, hydrochlorothiazide, acetazolamide, acebutolol, ethinylestradiol, abiraterone

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score. There are no clinical trials or relevant literature, and no plausible mechanism links a K-ATP channel blocker to a skeletal dysplasia caused by *INPPL1* mutations. Safety review also cannot proceed, because label warnings and contraindications have not been retrieved.

**To proceed, the following is needed:**
- Retrieval of the HSA package insert, covering warnings, contraindications and the approved indication text
- Mechanism of action data, to allow a proper mechanistic analysis
- Preclinical evidence on the SHIP2/INPPL1 pathway and repaglinide, if the team wants to pursue this prediction
- Reassessment of the other top-ranked predictions only if new supporting evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

