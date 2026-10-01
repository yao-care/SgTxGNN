---
layout: default
title: Abemaciclib
parent: Low Evidence (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Abemaciclib
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

# Abemaciclib: From HR+/HER2- Breast Cancer to Rheumatoid Arthritis

## One-Sentence Summary

Abemaciclib is an oral CDK4/6 inhibitor used for hormone receptor-positive, HER2-negative breast cancer. The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this direction has **0 clinical trials** and **1 publication**, an observational breast cancer cohort study that does not test efficacy in RA. The prediction currently rests almost entirely on the model score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | HR+/HER2- breast cancer (inferred from the trial and literature context; the Singapore registration records contain no indication text) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 97.32% |
| Evidence Level | L4 (no RA trials; only one observational study, on safety and prevalence rather than efficacy) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known pharmacology, abemaciclib is a CDK4/6 inhibitor, and its efficacy in HR+/HER2- breast cancer is established. CDK4/6 blockade could plausibly limit the proliferation of activated lymphocytes and synovial fibroblasts, both of which drive joint inflammation in RA. This is a hypothesis, not something the supplied data demonstrates.

Breast cancer and RA are very different diseases, so the link to the original indication is weak. The only linked publication studied pre-existing and emerging immune-mediated diseases in breast cancer patients taking CDK4/6 inhibitors. That is a safety-type question, not a test of RA treatment. Immune-mediated events during treatment could even point the other way. The high TxGNN score is a knowledge-graph prediction only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort (observational) | The Oncologist | Investigates the prevalence of autoimmune diseases in HR+/HER2- breast cancer patients on CDK4/6 inhibitors plus endocrine therapy, to identify predictive biomarkers and the impact on outcomes. It does not test abemaciclib as an RA treatment. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15789P | VERZENIO 100 mg | Film-coated tablet | Not stated in the record |
| SIN15790P | VERZENIO 150 mg | Film-coated tablet | Not stated in the record |
| SIN16574P | YULAREB 50 mg | Film-coated tablet | Not stated in the record |
| SIN16575P | YULAREB 100 mg | Film-coated tablet | Not stated in the record |
| SIN16576P | YULAREB 150 mg | Film-coated tablet | Not stated in the record |

The table shows 5 of the 6 registrations. All are oral products manufactured by Lilly del Caribe, Inc.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (CDK4/6 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions (neutropenia is a recognised CDK4/6 inhibitor class effect) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with differential) and liver function; confirm the schedule against the package insert |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

The RA-linked cohort study also asks whether CDK4/6 inhibitors may trigger or worsen autoimmune disease. That question should be resolved before any use in patients with autoimmune conditions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The RA prediction has a high model score but no clinical trials, and the single linked study is observational and addresses safety, not efficacy. The mechanistic link is plausible but unverified, and the immune-mediated event signal could argue against benefit.

**To proceed, the following is needed:**
- Mechanism of action data for abemaciclib (DrugBank).
- Package insert warnings and contraindications from HSA, plus the approved indication text for the Singapore registrations.
- RA-specific preclinical evidence, such as CDK4/6 inhibition in synovial fibroblasts or arthritis models.
- Full results of the linked cohort study on how CDK4/6 inhibitors affect pre-existing and new autoimmune disease.
- Route compatibility assessment for RA use.

Among the other predicted indications, amyotrophic lateral sclerosis has a preclinical study of abemaciclib on TDP-43 clearance. It is flagged in the data as a research question, and may be a better next candidate to examine.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

