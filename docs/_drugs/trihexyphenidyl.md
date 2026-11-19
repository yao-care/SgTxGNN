---
layout: default
title: Trihexyphenidyl
parent: Low Evidence (L5)
nav_order: 1026
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Trihexyphenidyl: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Parkinson disease and related parkinsonian and dystonic disorders"
monitor_inn: "Trihexyphenidyl"
predicted_indications: ["attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "attention deficit hyperactivity disorder, inattentive type", "Rasmussen subacute encephalitis", "PLA2G6-associated neurodegeneration", "congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "myelitis", "Charcot-Marie-Tooth disease, demyelinating, type 1G"]
---

# Trihexyphenidyl
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

## Trihexyphenidyl: From Parkinson Disease to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Trihexyphenidyl is a central anticholinergic drug originally used to treat Parkinson disease and related movement disorders such as dystonia.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but this rests on a computational prediction only: **0 clinical trials** and **1 loosely related publication** (on tic disorder with dystonia, not ADHD treatment) are currently available.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian and dystonic disorders (the Singapore licence has no indication text recorded) |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for trihexyphenidyl: "Trihexyphenidyl Hydrochloride is the substituted piperidine salt, 3-(1-piperidyl)- 1-phenylcyclohexyl-1-propanol hydrochloride, which exerts a direct inhibitory effect upon the parasympathetic nervous system. It also has a relaxing effect on smooth musculature; exerted both directly upon the muscle tissue itself and indirectly through an inhibitory effect upon the parasympathetic nervous system." ([DailyMed: trihexyphenidyl hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60ef86c-b8b6-4530-baaf-d4671ce961af), label version 2026-07-23; accessed 2026-11-19.) Based on known pharmacology, trihexyphenidyl is a central muscarinic antagonist with a preference for the M1 receptor. It modulates the balance between cholinergic and dopaminergic signalling in the striatum, which is the basis for its use in Parkinson disease and dystonia.

ADHD involves dopaminergic and noradrenergic dysregulation, so an indirect link through striatal neurotransmitter balance is conceivable. However, anticholinergic drugs typically impair attention and cognition, which argues against benefit and may even worsen inattention. The only retrieved paper concerns tic disorder with dystonia, a related movement phenotype, and does not test trihexyphenidyl in ADHD. The very high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21506147](https://pubmed.ncbi.nlm.nih.gov/21506147/) | 2011 | Cohort | Movement Disorders | Large clinical series of patients with tics and persistent dystonia, describing the prevalence and clinical features of this combined syndrome. It does not evaluate trihexyphenidyl for ADHD. |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN05827P | AA PHARMA TRIHEXYPHENIDYL TABLET 2 mg | TABLET | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (not package insert text)**: The drug is linked to contraindication with angle-closure and open-angle glaucoma, benign prostatic hyperplasia, myasthenia gravis, paralytic ileus, achalasia, ulcerative colitis and inflammatory bowel disease, hiatus hernia, and several cardiovascular conditions (hypertension, hypotension, coronary artery disease, heart conduction disease, sudden cardiac arrest). It is also linked to chronic obstructive pulmonary disease, kidney disease, liver disease, gallbladder disease, gastric ulcer and Clostridium difficile colitis.
- **Drug Interactions** (100 interactions were found; the main ones are listed):
  - **Major**: potassium chloride and potassium citrate.
  - **Moderate**: other anticholinergic or antimuscarinic agents (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline, methscopolamine, mepenzolate), opioids and gut-motility agents (morphine, loperamide, eluxadoline), prokinetics (metoclopramide, prucalopride), pramlintide, cannabinoids (dronabinol, nabilone) and magnesium hydroxide.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by model score alone, with no registered trials and no ADHD-specific literature. The pharmacology (central anticholinergic effects that can impair attention and cognition) argues against benefit, and the safety profile includes many potential contraindications and anticholinergic drug interactions.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Preclinical or clinical evidence on trihexyphenidyl in ADHD, including its cognitive effects
- Review of the other predicted indications, particularly PLA2G6-associated neurodegeneration, which overlaps most closely with the drug's parkinsonian and dystonic uses. It is a research question at evidence level L4, based on an indirect case report only.

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: trihexyphenidyl hydrochloride prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b60ef86c-b8b6-4530-baaf-d4671ce961af) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

