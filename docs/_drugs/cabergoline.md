---
layout: default
title: Cabergoline
parent: Medium Evidence (L3-L4)
nav_order: 189
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Cabergoline: predicted new indication Pituitary adenocarcinoma (evidence level L4). Approved use: Hyperprolactinemia, including prolactin-producing pituitary tumours"
monitor_inn: "Cabergoline"
predicted_indications: ["pituitary adenocarcinoma (disease)", "progeria-short stature-pigmented nevi syndrome", "pituitary cancer", "cerebral palsy, spastic quadriplegic", "glaucoma", "progeroid syndrome, Petty type", "psychogenic movement disorders", "kleptomania", "primary orthostatic tremor", "multiple fibroadenoma of the breast"]
---

# Cabergoline
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

# Cabergoline: From Hyperprolactinemia to Pituitary Adenocarcinoma

## One-Sentence Summary

Cabergoline is a dopamine agonist originally used to treat hyperprolactinemia and prolactin-producing pituitary tumours.
The TxGNN model predicts it may be effective for **pituitary adenocarcinoma**, but this specific prediction is supported by **0 clinical trials** and only **3 case reports or loosely related papers**.
Stronger evidence exists for a closely related prediction, "pituitary cancer", but that evidence concerns mostly benign adenomas (see the conclusion).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperprolactinemia, including prolactin-producing pituitary tumours (the Singapore licence text is blank, so this comes from the knowledge-graph indication list) |
| Predicted New Indication | Pituitary adenocarcinoma |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Cabergoline is, however, a well-known D2 dopamine receptor agonist. D2 stimulation suppresses prolactin and, in some tumours, ACTH secretion. It can also shrink tumours that express D2 receptors.

Hyperprolactinemia and prolactin-secreting pituitary tumours are the original indications. A pituitary carcinoma arises from the same tissue, so a graph-based model links the two. The mechanistic argument is that D2 receptors are expressed on some pituitary tumour cells.

The direct evidence is thin, however. The only clearly relevant paper is a case report of long-term octreotide or cabergoline use in ectopic ACTH hypersecretion. The other two retrieved papers do not study cabergoline treatment of pituitary carcinoma. The prediction is therefore mostly a model signal with limited supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered for this exact predicted indication.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | Case report | Endocrine Practice | Describes the corticotropin response to long-term octreotide or cabergoline in a patient with ectopic ACTH secretion after adrenalectomy. This is the only directly relevant report. |
| [33569966](https://pubmed.ncbi.nlm.nih.gov/33569966/) | 2021 | Case report | Revista Española de Enfermedades Digestivas | A patient with a pituitary adenoma on cabergoline was found to have duodenal lymphangiectasia as the first sign of pancreatic adenocarcinoma. It does not address cabergoline efficacy. |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | Case report | Medicine | Multiple endocrine neoplasia (MEN1) with an atypical course and a variant of uncertain significance. It does not address cabergoline treatment of pituitary carcinoma. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09545P | DOSTINEX TABLET 0.5 mg (Pfizer Italia S.r.l.) | Tablet | — (not stated in the data compiled) |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: liver disease, gallbladder disease, heart valve disease, pulmonary fibrosis (including postinflammatory pulmonary fibrosis), IgG4-related retroperitoneal fibrosis, and pre-eclampsia (including severe pre-eclampsia).
- **Drug Interactions**: 60 interactions were identified.
  - **Major**: lorcaserin and clarithromycin.
  - **Moderate**: metoclopramide.
  - The remaining entries are of unclassified severity (examples: pantoprazole, omeprazole, metformin, simvastatin, prednisone).
- **Safety signals in the retrieved literature (from other predicted indications)**:
  - Impulse control disorders (pathological gambling, compulsive shopping, hypersexuality) have been reported repeatedly in patients on cabergoline.
  - Cardiac valve disease is a debated risk, mainly at high doses.
  - A case of bilateral angle-closure glaucoma has been reported.

Please refer to the package insert for the official warnings, as these were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For pituitary adenocarcinoma specifically, there are no registered clinical trials and the literature consists of three case reports, only one of which is relevant. The prediction currently rests mainly on the model score and a plausible D2-receptor mechanism.

A closely related prediction in the same data, "pituitary cancer", has a stronger evidence base. It includes completed Phase 3 trials of cabergoline in corticotroph pituitary tumours (NCT00889525) and in residual non-functioning pituitary adenoma (NCT03271918, n=140). That evidence, however, concerns benign adenomas rather than true metastatic pituitary carcinoma. It should be assessed as a separate question and not treated as support for the carcinoma prediction.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA), especially D2 receptor expression in pituitary carcinoma.
- Clinical data in confirmed pituitary carcinoma or aggressive tumours, such as case series or prospective studies.
- The package insert warnings and contraindications from HSA, which are currently missing.
- A safety monitoring plan covering echocardiographic valve surveillance, impulse control disorder screening, and the major drug interactions.
- A clear decision on whether to pursue the benign-adenoma indications (corticotroph tumours, non-functioning adenoma) separately, since those have more mature evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

