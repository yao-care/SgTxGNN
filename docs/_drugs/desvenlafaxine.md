---
layout: default
title: Desvenlafaxine
parent: Medium Evidence (L3-L4)
nav_order: 318
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Desvenlafaxine: predicted new indication Obsessive-compulsive disorder (evidence level L4). Approved use: Unipolar depression, endogenous depression, major depressive disorder…"
monitor_inn: "Desvenlafaxine"
predicted_indications: ["schizotypal personality disorder", "schizoid personality disorder", "paranoid personality disorder", "histrionic personality disorder (disease)", "Ohdo syndrome and variants", "benign paroxysmal torticollis of infancy", "agoraphobia"]
---

# Desvenlafaxine
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

# Desvenlafaxine: From Depression to Obsessive-Compulsive Disorder

## One-Sentence Summary

Desvenlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) originally used to treat depression and anxiety disorders.
The TxGNN model predicts it may be effective for **obsessive-compulsive disorder (OCD)**, but there are currently **0 registered clinical trials** and only **3 loosely related publications** supporting this direction. The prediction rests mainly on class-level reasoning.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Unipolar depression, endogenous depression, major depressive disorder, anxiety disorder (the Singapore licence record has no indication text, so these come from the knowledge-graph indication list) |
| Predicted New Indication | Obsessive-compulsive disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, desvenlafaxine is an SNRI, and its efficacy in major depressive disorder is established. Mechanistically, it may be applicable to OCD.

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

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13859P | Pristiq Extended-Release Tablet 50mg (Pfizer Ireland Pharmaceuticals) | Extended-release tablet (oral) | Indication text not recorded in the licence data |

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
The prediction score is high (99.91%), and the serotonergic mechanism is plausible. However, there are no clinical trials and no desvenlafaxine-specific literature in OCD. Desvenlafaxine's serotonergic action is weaker than that of SSRIs, which are already established for OCD, so the case for it is currently weak.

**To proceed, the following is needed:**
- Desvenlafaxine-specific efficacy data in OCD, such as case series or controlled trials
- Detailed mechanism of action data (MOA), including serotonin transporter occupancy relative to SSRIs
- Package insert warnings and contraindications, to complete safety screening
- Review of the knowledge-graph contraindications against the label text, particularly the cardiovascular and bleeding-related items

**Note on other predictions:** In the same candidate list, **dysthymic disorder** has stronger support. It has two desvenlafaxine trials (a placebo-controlled Phase 4 trial with 59 participants and an open-label study with 30), plus a meta-analysis of antidepressants in dysthymia. It is rated L2 with a recommendation of Proceed with Guardrails, and may be a better first candidate for further evaluation than OCD.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

