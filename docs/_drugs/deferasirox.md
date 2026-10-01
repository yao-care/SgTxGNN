---
layout: default
title: Deferasirox
parent: Medium Evidence (L3-L4)
nav_order: 305
evidence_level: L4
indication_count: 10
---

# Deferasirox
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

# Deferasirox: From Iron Chelation to HIV Infectious Disease

## One-Sentence Summary

Deferasirox is an oral iron chelator. The registration data supplied does not state its approved indication.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **0 clinical trials** and only **2 publications**, one preclinical and one general review.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (deferasirox is an iron chelator) |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.40% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, deferasirox is an iron chelator, and mechanistically its iron-binding activity may be relevant to iron-dependent viral processes.

The only supporting link is a 2021 preclinical study (PMID 34550543). It shows that iron in endolysosomes affects HIV-1 Tat-mediated LTR transactivation, by changing Tat oligomerization and β-catenin expression. This suggests iron homeostasis can influence HIV-1 biology. It does not show that deferasirox itself has anti-HIV activity, and no clinical data exist.

The other top predictions show a similar pattern. Chronic hepatitis C (rank 2) has only indirect iron-overload literature from thalassemia populations. Beta-thalassemia (rank 8) and pyruvate kinase deficiency (rank 10) fit iron chelation well biologically, but have no supporting studies in this dataset. Beta-thalassemia is likely close to the drug's known use, so its status should be checked against regulatory labelling. Several other predictions are obsolete ontology terms, animal-only diseases (simian and feline immunodeficiency) or have no rationale, and should not be pursued.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | Preclinical mechanistic study | Journal of Neurovirology | Endolysosomal iron restricts Tat-mediated HIV-1 LTR transactivation by increasing Tat oligomerization and β-catenin expression |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Review | Journal of the American Pharmacists Association | New drug overview covering deferasirox; not HIV-specific |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17174P | DESROXIA Film-Coated Tablets 90MG | Film-coated tablet | Not stated in registration data |
| SIN17173P | DESROXIA Film-Coated Tablets 360MG | Film-coated tablet | Not stated in registration data |
| SIN17088P | FERASIRO Film Coated Tablet 90MG | Film-coated tablet | Not stated in registration data |
| SIN15215P | JADENU Film Coated Tablet 360MG | Film-coated tablet | Not stated in registration data |
| SIN15213P | JADENU Film Coated Tablet 90MG | Film-coated tablet | Not stated in registration data |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a high model score but rests on one indirect preclinical study and no clinical trials (L4). The original indication and safety data are also missing from the record, so it cannot advance beyond a research question.

**To proceed, the following is needed:**
- Download and parse the HSA package insert to obtain approved indications, warnings and contraindications
- Obtain mechanism of action data from DrugBank
- Confirm the known approved indication, so genuine repurposing candidates can be told apart from labelled uses such as iron overload in thalassemia
- Direct evidence of deferasirox anti-HIV activity, for example in vitro antiviral assays, before any clinical consideration
- Remap obsolete ontology terms, such as the familial combined hyperlipidemia prediction, to current terms before any review
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

