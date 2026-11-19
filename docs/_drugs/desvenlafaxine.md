---
layout: default
title: Desvenlafaxine
parent: Medium Evidence (L3-L4)
nav_order: 318
evidence_level: L4
indication_count: 8
last_modified_at: 2026-11-12
monitor_inn: "Desvenlafaxine"
predicted_indications: ["obsessive-compulsive disorder", "histrionic personality disorder (disease)", "schizoid personality disorder", "schizotypal personality disorder", "paranoid personality disorder", "Ohdo syndrome and variants", "benign paroxysmal torticollis of infancy", "agoraphobia"]
description: "Desvenlafaxine: predicted new indication Obsessive-compulsive disorder (evidence level L4). In Singapore: 1 HSA registration (1 valid)"
---

# Desvenlafaxine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **8** 
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

## Desvenlafaxine: Obsessive-compulsive disorder
{: .text-alpha }

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally used to treat depression and anxiety disorders.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**, but there are currently **0 registered clinical trials** and only **3 loosely related publications** supporting this direction. The prediction rests mainly on class-level reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L4 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for desvenlafaxine: "The exact mechanism of the antidepressant action of desvenlafaxine is unknown, but is thought to be related to the potentiation of serotonin and norepinephrine in the central nervous system, through inhibition of their reuptake. Non-clinical studies have shown that desvenlafaxine is a potent and selective SNRI." ([DailyMed: Pristiq Extended-Release (desvenlafaxine succinate) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f43610c-f290-46ea-d186-4f998ed99fce), label version 2026-04-28; accessed 2026-11-19.) Based on known information, desvenlafaxine is an SNRI, and its efficacy in major depressive disorder is established. Mechanistically, it may be applicable to OCD.

Serotonin reuptake inhibition is the established pharmacological basis of OCD treatment, with SSRIs and clomipramine as the standard agents. A published review of double-blind studies of serotonergic antidepressants in OCD confirms the key role of the serotonin system in OCD. This gives the prediction a plausible class-level rationale.

There are two important caveats:
- Desvenlafaxine's serotonergic effect is weaker than that of SSRIs.
- Its noradrenergic component has no established benefit in OCD.

The mechanistic link is inferred from drug class, not from desvenlafaxine-specific data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | Reviews double-blind studies of serotonergic antidepressants in OCD and confirms the key role of the serotonin system. It does not address desvenlafaxine specifically. |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | Augmentation study (somatic symptom disorder) | Psychiatry Clin Psychopharmacol | Risperidone augmentation in antidepressant-resistant somatic symptom disorder. OCD is mentioned only as a related condition, so relevance is indirect. |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | Review of postpartum depression. OCD appears only as a possible later complication, so relevance is weak. |

None of these publications tests desvenlafaxine in OCD.

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN13859P | Pristiq Extended-Release Tablet 50mg | TABLET, EXTENDED RELEASE | Valid |

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these come from a drug-disease relationship database, not from the package insert):
  - Cardiovascular and blood pressure: hypertension, cardiovascular disease, heart disease, cerebrovascular disorder
  - Psychiatric and neurological: epilepsy, bipolar disorder, major affective disorder
  - Organ function and bleeding: liver disease, gallbladder disease, impaired renal function, blood coagulation disease, hypertriglyceridemia
  - Eye: ocular hypertension, angle-closure glaucoma
  - Other syndromes: serotonin syndrome, neuroleptic malignant syndrome, SIADH (inappropriate ADH syndrome) and nephrogenic SIAD, interstitial lung disease
- **Drug Interactions**: 100 interactions were identified. The 20 listed in the data compiled for this report include these major-level interactions:
  - Bupropion
  - Lorcaserin
  - Dexfenfluramine
  - Fenfluramine
  - Diethylpropion
  - Mazindol
  - Dolasetron
  - Granisetron

  Moderate-level interactions include epinephrine, ephedrine, morphine, acetylsalicylic acid (aspirin), dronabinol, mannitol, and bowel-preparation agents. Cimetidine is minor. Many of these are linked to serotonergic or sympathomimetic effects.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high (0.9991), and the serotonergic mechanism is plausible. However, there are no clinical trials and no desvenlafaxine-specific literature in OCD. Desvenlafaxine's serotonergic action is weaker than that of SSRIs, which are already established for OCD, so the case for it is currently weak.

**To proceed, the following is needed:**
- Desvenlafaxine-specific efficacy data in OCD, such as case series or controlled trials
- Detailed mechanism of action data (MOA), including serotonin transporter occupancy relative to SSRIs
- Package insert warnings and contraindications, to complete safety screening
- Review of the knowledge-graph contraindications against the label text, particularly the cardiovascular and bleeding-related items

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Pristiq Extended-Release (desvenlafaxine succinate) prescribing information, Wyeth Pharmaceuticals LLC, a subsidiary of Pfizer Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0f43610c-f290-46ea-d186-4f998ed99fce) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

