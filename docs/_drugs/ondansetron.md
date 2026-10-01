---
layout: default
title: Ondansetron
parent: Low Evidence (L5)
nav_order: 734
evidence_level: L5
indication_count: 10
---

# Ondansetron
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

# Ondansetron: From Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Ondansetron is a 5-HT3 receptor antagonist used as an antiemetic for chemotherapy-induced and anesthesia-related nausea and vomiting. The TxGNN model's top-ranked prediction is **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are **0 clinical trials and 0 publications** behind it, so it rests on the model score alone. The strongest evidence in this pack is for a lower-ranked prediction, **Tourette syndrome**, with **1 completed Phase 4 trial and 2 randomized controlled trials**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nausea and vomiting (chemotherapy-induced and post-operative), taken from published literature; the HSA records in this pack carry no indication text |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.65% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 16 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ondansetron is a selective 5-HT3 receptor antagonist. Detailed mechanism-of-action data are not available in the source record, so this description comes from general pharmacology and the retrieved literature.

For NSIAD, **no mechanistic rationale can be established.** NSIAD is an ultra-rare disorder caused by gain-of-function of the vasopressin V2 receptor, and it has no obvious link to 5-HT3 blockade. The high score of 0.987 is a model output only.

The Tourette syndrome prediction (rank 2, score 97.96%) is much more plausible. 5-HT3 receptors modulate dopaminergic and serotonergic circuits in cortico-striatal pathways involved in tics and OCD-spectrum symptoms. Early human studies exist, but there is no Phase 3 confirmation in the data provided. Trichotillomania (rank 3) shares this serotonergic hypothesis but has no supporting studies.

## Clinical Trial Evidence

**NSIAD (rank 1):** Currently no related clinical trials registered.

**Tourette syndrome (rank 2, for reference):**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03239210](https://clinicaltrials.gov/study/NCT03239210) | Phase 4 | Completed | 110 | Randomized, placebo-controlled test of 24 mg/day ondansetron for 4 weeks in OCD and tic disorders, with MRI and symptom assessments. Outcome data are not included in the pack and must be verified. |

## Literature Evidence

**NSIAD (rank 1):** Currently no related literature available.

**Tourette syndrome (rank 2, for reference):**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39876680](https://pubmed.ncbi.nlm.nih.gov/39876680/) | 2025 | RCT | Am J Psychiatry | 4 weeks of high-dose ondansetron vs placebo for sensory phenomena and brain connectivity in OCD and tic disorders. Results are not shown in the excerpt. |
| [15816793](https://pubmed.ncbi.nlm.nih.gov/15816793/) | 2005 | RCT | J Clin Psychiatry | 3-week randomized, double-blind, placebo-controlled study of ondansetron in Tourette's disorder. Results are not shown in the excerpt. |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Review | Medicine | Narrative review of Phase III and IV pharmacological trials in Tourette syndrome. |
| [11474424](https://pubmed.ncbi.nlm.nih.gov/11474424/) | 2001 | Review | CNS Drug Reviews | Ondansetron and its applications in CNS-related disorders. |
| [21183132](https://pubmed.ncbi.nlm.nih.gov/21183132/) | 2010 | Review | Semin Pediatr Neurol | Review of RCTs of drugs for Tourette syndrome and stereotypies in autism. |
| [10565805](https://pubmed.ncbi.nlm.nih.gov/10565805/) | 1999 | Open-label pilot | Int Clin Psychopharmacol | 6 men with haloperidol-resistant Tourette's syndrome treated with ondansetron. |
| [18184945](https://pubmed.ncbi.nlm.nih.gov/18184945/) | 2008 | Case report | J Child Neurol | A boy's tics improved on ondansetron and reappeared when the dose was reduced. |
| [16314763](https://pubmed.ncbi.nlm.nih.gov/16314763/) | 2005 | Genetic association | Psychiatr Genet | HTR3A and HTR3B gene variants were not found to be involved in Tourette syndrome. |

The literature retrieved for common cold and allergic urticaria concerns unrelated topics (chemotherapy neuropathy, food allergy) and gives no support for those predictions.

## Singapore Market Information

Approved indication text is not available for these registrations. Five of 16 are shown.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15558P | ONRON 8 Solution for Injection or Infusion 2 mg/ml | Injection, solution | Intas Pharmaceuticals |
| SIN15742P | Ondansetron B. Braun Solution for Injection or Infusion 2 mg/ml | Injection, solution | B. Braun Melsungen AG |
| SIN16791P | Prezinton Solution for Injection 4 mg/2ml | Injection, solution | PT Ferron Par Pharmaceuticals |
| SIN15004P | Ondavell Film-Coated Tablet 8 mg | Tablet, film coated | PT Novell Pharmaceutical Laboratories |
| SIN05133P | Zofran Tablet 8 mg | Tablet, film coated | Aspen Bad Oldesloe GmbH |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold** (for NSIAD, the rank-1 prediction)

**Rationale:**
The NSIAD prediction has no trials, no literature and no plausible mechanism, so it is a model prediction only (L5). The score should not be treated as evidence. The personality-disorder entries (ranks 4–7) share an identical score of 0.9716, which suggests a graph-propagation artifact rather than a disease-specific signal. Tourette syndrome (L2) is worth pursuing as a research question, but its evidence is a Phase 4 trial and early RCTs, not Phase 3 confirmation.

**To proceed, the following is needed:**
- Retrieve HSA package insert warnings and contraindications, which currently block safety screening
- Obtain mechanism-of-action data from DrugBank
- Retrieve the primary-endpoint results of NCT03239210 and the two Tourette RCTs (PMIDs 39876680 and 15816793) to decide whether Tourette syndrome should advance
- Confirm route compatibility for each candidate indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

