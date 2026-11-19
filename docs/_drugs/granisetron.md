---
layout: default
title: Granisetron
parent: Low Evidence (L5)
nav_order: 491
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Granisetron: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not listed in the Singapore licence records"
monitor_inn: "Granisetron"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "acute contagious conjunctivitis", "angioedema", "allergic urticaria", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "bronchitis", "cold urticaria", "conjunctivitis"]
---

# Granisetron
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

## Granisetron: From Chemotherapy-Related Nausea and Vomiting to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Granisetron is a selective 5-HT3 receptor antagonist. It is marketed in Singapore as an injectable and oral product, but the data compiled for this report contain no approved indication text.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but **no clinical trials and no publications** currently support this prediction.
It rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the Singapore licence records |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 7 of 7) |
| Number of Registrations | 7 (valid: 7) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Granisetron is a selective 5-HT3 receptor antagonist. According to the Mechanism of Action section of the US FDA-approved prescribing information for granisetron: "Granisetron is a selective 5-hydroxytryptamine 3 (5-HT 3 ) receptor antagonist with little or no affinity for other serotonin receptors, including 5-HT 1, 5-HT 1A, 5-HT 1B/C, 5-HT 2; for alpha 1-, alpha 2-, or beta-adrenoreceptors; for dopamine-D 2; or for histamine-H 1; benzodiazepine; picrotoxin or opioid receptors. Serotonin receptors of the 5-HT 3 type are located peripherally on vagal nerve terminals and centrally in the chemoreceptor trigger zone of the area postrema." ([DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56), label version 2026-04-30; accessed 2026-11-19.) The licence records give no approved indication text. Granisetron's established use, as a 5-HT3 antagonist anti-emetic, is general knowledge and is not confirmed by the compiled data.

The proposed link to mood disorders is speculative. 5-HT3 modulation has been hypothesised to influence dopaminergic and serotonergic signalling relevant to mood regulation. The high TxGNN score (0.9962) is a model prediction only. It does not show clinical benefit.

Other lower-ranked predictions include Tourette syndrome, trichotillomania, angioedema, allergic urticaria, cold urticaria, bronchitis, conjunctivitis, acute contagious conjunctivitis and nephrogenic syndrome of inappropriate antidiuresis. Some have loose class-level rationale, for example the serotonergic and dopaminergic involvement in Tourette syndrome and trichotillomania. Others, such as nephrogenic syndrome of inappropriate antidiuresis and infectious conjunctivitis, have no plausible mechanistic link; their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN07089P | KYTRIL FOR INFUSION 3 mg/3ml | INJECTION | Valid |
| SIN07800P | KYTRIL TABLET 1 mg | TABLET, FILM COATED | Valid |
| SIN13539P | KYTRIL FOR INFUSION 1MG/ML | INJECTION | Valid |
| SIN14409P | Granisetron Kabi concentrate for solution for infusion 1mg/ml | INFUSION, SOLUTION CONCENTRATE | Valid |
| SIN14612P | GRANISETRON-AFT SOLUTION FOR INJECTION 1MG/ML | INJECTION, SOLUTION | Valid |

Showing 5 of 7 HSA registrations.

<!-- licenses:end -->

Seven valid single-ingredient licences exist in total. Both injectable and oral forms are available.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease network edges, not label text): long QT syndrome, familial long QT syndrome, potassium deficiency disease, sudden cardiac arrest and heart conduction disease. These point to a QT-prolongation concern.
- **Drug Interactions**: 100 interactions were identified. Examples of **Major** interactions include fentanyl, dextromethorphan, tramadol, alfentanil, almotriptan, sumatriptan, amiodarone, amisulpride, amitriptyline and anagrelide. These involve serotonergic and QT-prolonging combinations. Examples of **Moderate** interactions include abametapir, abiraterone, dihydrocodeine, codeine, famotidine, formoterol, adenosine, salbutamol, alfuzosin and propofol.

Please refer to the package insert for label warnings and contraindications, as these were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has Evidence Level L5, with no clinical trials or literature. The mechanistic rationale is speculative. Safety signals around QT prolongation and serotonergic interactions matter in a psychiatric population, where co-medications are common.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- A literature and trial search for granisetron or 5-HT3 antagonists in bipolar mania
- Preclinical or mechanistic evidence supporting a role in mood regulation
- A QT and drug-interaction risk assessment for the target population
- Route and dosage compatibility assessment, which is currently pending

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data are not available in the data compiled for this report, and t" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Sustol (granisetron) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f7c7ffdd-8270-4030-bc1e-a1cb28a6de56) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

