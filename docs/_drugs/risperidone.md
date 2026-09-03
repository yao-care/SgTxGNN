---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 866
evidence_level: L5
indication_count: 10
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Risperidone: From Schizophrenia/Bipolar Disorder to Tourette Syndrome

## One-Sentence Summary

Risperidone is a well-established atypical antipsychotic used globally for schizophrenia, bipolar mania, and irritability associated with autism spectrum disorder.
The TxGNN model additionally predicts a broad set of neuropsychiatric associations, and among these, **Tourette Syndrome** stands out as the most clinically credible candidate,
supported by **2 registered clinical trials** and **19 publications**, including several placebo-controlled RCTs specifically testing risperidone in this condition.
Several other TxGNN-predicted indications (e.g., trichotillomania, Phelan-McDermid syndrome) have only case-report level support, and two top-ranked predictions have no supporting evidence at all — this is flagged explicitly below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in this evidence pack (Singapore: not marketed, 0 licenses). Globally, risperidone is approved for schizophrenia, bipolar mania, and irritability in autism spectrum disorder. |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 98.76% (rank 12,383 of all drug–disease pairs) |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

**Important caveat:** The single highest-scoring TxGNN prediction for this drug ("gaze palsy, familial horizontal, with progressive scoliosis," score 99.76%) and several other top-10 predictions have **zero** clinical trial or literature support. Raw TxGNN rank does not track directly with evidence quality — Tourette Syndrome was selected as the headline indication because it has the strongest independent clinical evidence among all ranked candidates, not because it has the single highest score.

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for risperidone is not available in this evidence pack (Data Gap DG002). Based on generally known pharmacology, risperidone is a combined dopamine D2 and serotonin 5-HT2A receptor antagonist, a mechanism shared across its approved psychiatric indications.

Tourette Syndrome is understood to involve striatal dopaminergic hyperactivity contributing to motor and vocal tics. Risperidone's D2-antagonist action directly addresses this proposed pathophysiology, which is why it is already listed as a recognized pharmacological option in tic-disorder treatment guidelines, alongside — rather than instead of — its approved psychiatric uses. This makes the mechanistic rationale for repurposing considerably stronger than for most of the other TxGNN-predicted candidates in this pack, several of which (e.g., amelocerebrohypohidrotic syndrome, chromosome 15q11.2 deletion syndrome) show no plausible mechanistic overlap and no supporting evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00004393](https://clinicaltrials.gov/study/NCT00004393) | Phase 2 | Completed | 50 | Randomized, double-blind, placebo-controlled trial of risperidone in children and adults with moderate-to-severe Tourette Syndrome; also evaluated safety |
| [NCT03522168](https://clinicaltrials.gov/study/NCT03522168) | N/A (Phase 4-type registry) | Completed | 509 | Long-term pediatric safety trial evaluating weight changes with multi-year risperidone/aripiprazole therapy; safety-focused, not a Tourette-specific efficacy trial |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12682319](https://pubmed.ncbi.nlm.nih.gov/12682319/) | 2003 | RCT | Neurology | Placebo-controlled trial confirming efficacy and safety of risperidone in children and adults with Tourette syndrome |
| [11799340](https://pubmed.ncbi.nlm.nih.gov/11799340/) | 2002 | RCT | J Clin Psychopharmacol | Double-blind, placebo-controlled trial (n=48); risperidone 0.5–6.0 mg/day reduced tic severity over 8 weeks |
| [11886028](https://pubmed.ncbi.nlm.nih.gov/11886028/) | 2002 | RCT | J Am Acad Child Adolesc Psychiatry | Head-to-head comparison of risperidone vs. clonidine in children/adolescents with Tourette syndrome |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Clinical Guideline | Eur Child Adolesc Psychiatry | European (ESSTS) clinical guidelines list risperidone among evidence-based pharmacological treatments for Tourette syndrome |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network Meta-analysis | Lancet Child Adolesc Health | Comparative efficacy/tolerability of pharmacological interventions for Tourette's syndrome in children/adolescents |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | Systematic evaluation of efficacy of treatments for tics, including antipsychotics |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic Review | J Psychopharmacol | Review of evidence quality for pharmacological Tourette syndrome treatments in children and adults |
| [32856174](https://pubmed.ncbi.nlm.nih.gov/32856174/) | 2020 | Review | Neurotherapeutics | Overview of current behavioral, pharmacologic, and surgical management of tics/Tourette syndrome |
| [8543544](https://pubmed.ncbi.nlm.nih.gov/8543544/) | 1996 | Open-label Trial | J Clin Psychiatry | Early open-label trial assessing efficacy and safety of risperidone for Tourette's syndrome |
| [37303178](https://pubmed.ncbi.nlm.nih.gov/37303178/) | 2023 | Comparative Study | Curr Drug Discov Technol | Semi-experimental comparison of aripiprazole vs. risperidone effects/side effects in pediatric Tourette syndrome |

---

## Singapore Market Information

Risperidone currently has **no marketing authorisation records** in Singapore in this evidence pack (0 registrations; market status: not marketed). No product-level dosage form or approved-indication data is available for this jurisdiction. Any repurposing pathway would require a new registration submission rather than an indication-extension to an existing license.

---

## Other Predicted Indications (For Context)

TxGNN generated 10 top-ranked disease associations for risperidone with widely varying evidence quality. For transparency, they are summarized below rather than omitted:

| Rank | Disease | Evidence Level | Recommendation | Note |
|------|---------|----------------|-----------------|------|
| 1 | Gaze palsy, familial horizontal, with progressive scoliosis | — | — | No clinical trials or literature; score is highest but unsupported |
| 2 | Asperger syndrome, susceptibility to | L4 | Research Question | Overlaps with approved autism-irritability use; no direct evidence |
| 3 | Amelocerebrohypohidrotic syndrome | L5 | Hold | No mechanistic or evidentiary link |
| 4 | Phelan-McDermid syndrome | L4 | Research Question | Case reports/animal models only |
| 5 | Trichotillomania | L3 | Research Question | Small case series/case reports as SRI augmentation; no RCTs |
| 6 | Major affective disorder | pending | pending | Substantial trial/literature volume (augmentation in depression/bipolar disorder) but not yet scored |
| **7** | **Tourette Syndrome** | **L2** | **Proceed with Guardrails** | **Headline indication — see above** |
| 8 | Intellectual disability | pending | pending | Overlaps with autism-related behavioral use |
| 9 | Autism, susceptibility to | L2 | Proceed with Guardrails | Evidence base is mostly pharmacogenomic (side-effect prediction), not new efficacy; overlaps with already-approved use |
| 10 | Chromosome 15q11.2 deletion syndrome | L5 | Hold | No direct evidence, pure graph inference |

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were available in this evidence pack (Data Gap DG001, flagged as **Blocking** severity — the local regulatory label/insert has not yet been obtained, which prevents completion of the S1 safety pre-assessment).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Tourette Syndrome has the strongest independent evidence among all TxGNN-predicted indications for risperidone — multiple placebo-controlled RCTs and inclusion in international clinical guidelines — making it a credible, mechanistically coherent repurposing candidate (L2, decision stage S3). However, the drug has no existing Singapore registration and the mandatory safety pre-assessment (S1) is currently blocked by a missing local label/insert.

**To proceed, the following is needed:**
- Obtain the HSA/local package insert (warnings, contraindications, DDI) to resolve Blocking gap DG001 and complete the S1 safety review
- Obtain formal DrugBank/manufacturer MOA documentation to close High-severity gap DG002
- Confirm regulatory pathway, since risperidone has 0 existing Singapore licenses (a new indication would require new registration, not a label extension)
- If pursuing autism-susceptibility or intellectual-disability candidates further, distinguish new-indication evidence from side-effect/pharmacogenomic evidence, as current literature for these two candidates is largely safety- rather than efficacy-focused
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

