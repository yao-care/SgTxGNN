---
layout: default
title: Somatostatin
parent: Low Evidence (L5)
nav_order: 928
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Somatostatin: predicted new indication Amenorrhea (evidence level L5). Approved use: Not available"
---

# Somatostatin
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

# Somatostatin: From an Unspecified Approved Indication to Amenorrhea

## One-Sentence Summary

Somatostatin is a hypothalamic peptide hormone that is registered in Singapore as an injectable product, but the approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **amenorrhea** (score 98.6%), but there are **no clinical trials** and only **literature that mostly describes pituitary tumours in which amenorrhea is a symptom**, so the prediction rests almost entirely on the model.
Among the top 10 predictions, **multiple endocrine neoplasia (MEN)** has the strongest supporting evidence (1 Phase 3 trial and relevant reviews), and it is discussed below as an alternative lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the approved indication text in the Singapore licence is blank) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 98.64% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, somatostatin is a natural neuropeptide that inhibits the release of growth hormone and several other hormones, and its analogues act on pituitary and neuroendocrine tumours through somatostatin receptors (mainly SSTR2 and SSTR5).

The link to amenorrhea is weak. The retrieved publications concern pituitary adenomas (growth hormone-, ACTH- and prolactin-secreting), in which amenorrhea appears as a downstream symptom of hormone excess or hypogonadism. Somatostatin-type drugs may help in these tumours by suppressing the hormone excess, but any benefit would be indirect and specific to the cause. It would not be a treatment for amenorrhea itself. The high TxGNN score is most likely driven by the drug's network proximity to pituitary disease.

For context, the other top-ranked predictions look similar or weaker:
- **Multiple endocrine neoplasia (rank 5):** the most biologically plausible, because MEN1-associated neuroendocrine tumours commonly express somatostatin receptors, and somatostatin analogues are established for symptom and tumour control in neuroendocrine tumours. Evidence level L4.
- **HER2-positive breast carcinoma (rank 9) and pulmonary hypertension (rank 7):** only preclinical or indirect evidence (L4). The animal data for pulmonary hypertension are inconsistent.
- **Hypogonadotropic hypogonadism (rank 4):** somatostatin would be expected to suppress, not restore, gonadotropin function.
- **Ranks 2, 3, 6, 8 and 10** (Leydig cell hypoplasia, 46,XY disorder of sex development, mycotic corneal ulcer, kyphoscoliotic heart disease, homozygous familial hypercholesterolemia): prediction only, with no trials, no literature and no plausible mechanism.

## Clinical Trial Evidence

For amenorrhea, there are currently no related clinical trials registered.

For reference, the closest trial in the wider prediction list is for multiple endocrine neoplasia:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02705651](https://clinicaltrials.gov/study/NCT02705651) | Phase 3 | Unknown | 180 | Randomised study of somatostatin analogues versus no treatment in non-functioning pancreatic neuroendocrine tumours in MEN1. No results available, and the intervention arm should be verified. |

## Literature Evidence

The publications retrieved for amenorrhea are reviews and case reports about pituitary tumours. None test somatostatin as a treatment for amenorrhea.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28170483](https://pubmed.ncbi.nlm.nih.gov/28170483/) | 2017 | Review | JAMA | Diagnosis and treatment of pituitary adenomas, which can cause hormone excess or mass effects |
| [15765032](https://pubmed.ncbi.nlm.nih.gov/15765032/) | 2004 | Review | Minerva Endocrinol | Prolactin-secreting pituitary tumours cause amenorrhea-galactorrhea in women |
| [15578985](https://pubmed.ncbi.nlm.nih.gov/15578985/) | 2004 | Review | Curr Drug Targets Immune Endocr Metabol Disord | Treatment of Cushing's syndrome, of which amenorrhea is one feature |
| [17644863](https://pubmed.ncbi.nlm.nih.gov/17644863/) | 2002 | Review | Eat Weight Disord | GH/IGF-I axis changes in anorexia nervosa, which include amenorrhea |
| [6277529](https://pubmed.ncbi.nlm.nih.gov/6277529/) | 1981 | Review | Clin Biochem | Control of anterior pituitary hormone release by hypothalamic factors |
| [24683483](https://pubmed.ncbi.nlm.nih.gov/24683483/) | 2014 | Case report | Endocrinol Diabetes Metab Case Rep | GH-secreting macroadenoma with secondary amenorrhoea |
| [41687635](https://pubmed.ncbi.nlm.nih.gov/41687635/) | 2025 | Case report | Georgian Med News | Late diagnosis of acromegaly in a somatoprolactinoma, with early amenorrhea |
| [21814887](https://pubmed.ncbi.nlm.nih.gov/21814887/) | 2012 | Case report | Pituitary | MEN1A presenting with amenorrhea and galactorrhea |
| [34158336](https://pubmed.ncbi.nlm.nih.gov/34158336/) | 2021 | Case report | BMJ Case Rep | Cushing disease with secondary amenorrhoea in an adolescent |
| [1400888](https://pubmed.ncbi.nlm.nih.gov/1400888/) | 1992 | Other | J Clin Endocrinol Metab | Atypical McCune-Albright syndrome with GH-prolactin adenoma, treated with SMS 201-995 (octreotide) plus bromocriptine |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06135P | STILAMIN 3000 FOR INJECTION 3 mg/ampoule | Injection, powder, for solution | Not available |

## Safety Considerations

Please refer to the package insert for safety information.

Note that no drug interaction records were found, and no contraindication data from the knowledge graph were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The amenorrhea prediction is supported only by the model score and by literature in which amenorrhea is a symptom of pituitary tumours. No trial tests somatostatin for amenorrhea, and no direct mechanism is apparent (L5). The more promising direction is neuroendocrine tumours in multiple endocrine neoplasia (L4, with one Phase 3 trial of unconfirmed intervention), which could be pursued as a separate research question.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications from the Singapore regulator, to allow safety screening
- Mechanism of action data
- Verification of the intervention arm and results of NCT02705651 before considering an upgrade of the multiple endocrine neoplasia lead
- For amenorrhea, evidence of a direct therapeutic effect (for example, a cause-specific study in hormone-secreting pituitary tumours) rather than symptom-level associations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

