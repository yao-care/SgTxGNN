---
layout: default
title: Alverine
parent: Low Evidence (L5)
nav_order: 74
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
description: "Alverine: predicted new indication Dysthymic disorder (evidence level L5). Approved use: Not stated in the Singapore licence records. Reference sources descri…"
monitor_inn: "Alverine"
predicted_indications: ["dysthymic disorder", "neurotic disorder", "anxiety disorder", "migraine disorder", "neurotic depression", "melancholia", "benign paroxysmal torticollis of infancy", "agoraphobia", "congenital isolated adrenocorticotropic hormone deficiency (disease)"]
---

# Alverine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Alverine: From Smooth Muscle Spasm to Dysthymic Disorder
{: .text-alpha }

## One-Sentence Summary

Alverine is a smooth muscle relaxant used in some countries for gastrointestinal spasm and cramps. The TxGNN model predicts it may be effective for **dysthymic disorder**, but this is a model prediction only, with **0 clinical trials** and **0 publications** specific to this indication. The nearest supporting evidence is for related mood and anxiety conditions: one preclinical mouse study on anxiety and one computational repositioning study on depression.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records. Reference sources describe symptomatic relief of gastrointestinal smooth muscle spasm and cramps associated with dysmenorrhoea. |
| Predicted New Indication | Dysthymic disorder |
| TxGNN Prediction Score | 0.9983 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on the information compiled for this report, alverine is a synthetic smooth muscle relaxant with reported 5-HT1A receptor antagonist activity. Its pharmacology record also lists an interaction with the HNF4A transcription factor, but this has no clear link to mood disorders.

The serotonin system plays a recognised role in mood and anxiety disorders, so a link between alverine and dysthymia is plausible. However, no direct evidence supports it. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other predicted indications are mostly in the same mood and anxiety group, which gives the signal some internal consistency:

- **Anxiety disorder (rank 3):** A 2014 mouse study reported anxiolytic-like effects of alverine citrate, consistent with 5-HT1A antagonism (L4).
- **Neurotic depression and melancholia (ranks 5 and 6):** A 2018 network-based repositioning study nominated alverine as a potential antidepressant candidate (L4).
- **Other predictions:** Migraine, infantile torticollis and congenital ACTH deficiency have no supporting evidence. The ACTH deficiency score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered for dysthymic disorder, nor for any of the other top-10 predicted indications.

## Literature Evidence

Currently no related literature is available for dysthymic disorder itself. The following publications relate to neighbouring predicted indications and offer only indirect support:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25199966](https://pubmed.ncbi.nlm.nih.gov/25199966/) | 2014 | Preclinical (animal model) | European Journal of Pharmacology | Alverine citrate showed anxiolytic-like effects in mouse anxiety models, consistent with 5-HT1A antagonism. |
| [30087074](https://pubmed.ncbi.nlm.nih.gov/30087074/) | 2018 | Computational repositioning study | European Neuropsychopharmacology | A network-based repositioning approach nominated alverine as a potential antidepressant, with possible experimental validation. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17214P | ALMET CAPSULES | Capsule, liquid filled (oral) | Not recorded in the licence data |
| SIN16773P | ALVERSIME SOFT CAPSULES | Capsule (oral) | Not recorded in the licence data |

Both licences are valid single-ingredient products. None are cancelled.

## Safety Considerations

- **Drug Interactions:** The only entry compiled is a pharmacological target interaction with hepatocyte nuclear factor-4-alpha (HNF4A). It is not a drug-drug interaction and has no assigned severity level.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for dysthymic disorder is supported only by a high model score (0.9983), with no trials or literature for this indication. The related evidence is limited to one mouse study and one computational study, so the indication stays at L5. The safety package is also incomplete, because package insert warnings and contraindications are unavailable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which is a blocking gap for safety screening
- Detailed mechanism of action data, for example from DrugBank
- Confirmation of the approved indications for the two Singapore licences
- Human clinical or mechanistic evidence for dysthymia. A more promising near-term direction is anxiety disorder, where preclinical data exist, and this could be framed as a research question.
- Assessment of whether the doses and formulations used in gastrointestinal care are suitable for a psychiatric indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

