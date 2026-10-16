---
layout: default
title: Estradiol Valerate
parent: Low Evidence (L5)
nav_order: 403
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Estradiol Valerate: predicted new indication Symptomatic form of fragile X syndrome in female carriers (evidence level L5). Approved use: Primary ovarian failure"
---

# Estradiol Valerate
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

# Estradiol Valerate: From Primary Ovarian Failure to Symptomatic Fragile X Syndrome in Female Carriers

## One-Sentence Summary

Estradiol valerate is an oral estrogen, originally used to treat primary ovarian failure.
The TxGNN model predicts it may be effective for **symptomatic form of fragile X syndrome in female carriers**, but **no clinical trials and no publications** were found for this specific prediction.
The prediction currently rests on model output and a plausible mechanistic link alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Primary ovarian failure (the Singapore licence records contain no indication text) |
| Predicted New Indication | Symptomatic form of fragile X syndrome in female carriers |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, estradiol valerate is an ester prodrug of estradiol, used as estrogen replacement. Its efficacy in primary ovarian failure rests on correcting a low-estrogen state, and mechanistically it may be applicable to other conditions that share this feature.

Female carriers of an FMR1 premutation can develop fragile X-associated primary ovarian insufficiency (FXPOI). This overlaps with the original indication, so estrogen replacement is plausible for the low-estrogen part of the condition. It would not be expected to treat other features of fragile X carrier syndrome. The high TxGNN score is a prediction only, with no supporting studies retrieved.

Other top-ranked predictions follow a similar pattern. Blepharophimosis-epicanthus inversus-ptosis (BPES), including the 3q23 rearrangement form, involves FOXL2-related ovarian insufficiency. Estrogen could address only the ovarian component, not the eyelid malformation. Anovulation and ovarian dysfunction are the only predictions with any retrieved evidence, and that evidence is mostly indirect (see below). Several predictions (partial trisomy/tetrasomy of chromosome arms 5p, 12p and 18p) show no clear mechanistic link, and the scores likely reflect knowledge-graph proximity to gonadal phenotypes.

## Clinical Trial Evidence

Currently no related clinical trials are registered for the top predicted indication.

For the lower-ranked prediction of **anovulation** (rank 7), one trial was found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02186782](https://clinicaltrials.gov/study/NCT02186782) | Phase 4 | Unknown | 600 | Randomised trial of clomiphene citrate plus estradiol versus clomiphene alone for ovulation induction in infertile women. No results were provided. |

## Literature Evidence

Currently no related literature is available for the top predicted indication.

For the lower-ranked predictions (anovulation and ovarian dysfunction), the literature is mostly preclinical. Estradiol valerate is widely used to *induce* polycystic-ovary-like conditions in animals, which describes the drug causing ovarian dysfunction rather than treating it. The most relevant items are:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36063826](https://pubmed.ncbi.nlm.nih.gov/36063826/) | 2022 | Randomised trial | Gynecol Endocrinol | Compared estradiol valerate at 4, 6 and 9 mg/day on endometrial estrogen receptor expression and ovarian function in women with unexplained recurrent abortion. |
| [1472813](https://pubmed.ncbi.nlm.nih.gov/1472813/) | 1992 | Clinical study | J Assist Reprod Genet | In an oocyte donation programme for women with ovarian failure, oral estradiol valerate 6 mg daily plus progesterone was used for hormonal replacement. |
| [33749482](https://pubmed.ncbi.nlm.nih.gov/33749482/) | 2021 | Clinical study | Gynecol Endocrinol | Estradiol valerate/nomegestrol acetate combination in ovarian endometrioma and deep infiltrating endometriosis. This is a different combination product, so relevance is indirect. |
| [9024224](https://pubmed.ncbi.nlm.nih.gov/9024224/) | 1997 | Clinical study | J Clin Endocrinol Metab | Effects of hormone replacement with estradiol valerate plus cyproterone acetate or medroxyprogesterone acetate on nitric oxide levels in postmenopausal women. |
| [40774400](https://pubmed.ncbi.nlm.nih.gov/40774400/) | 2025 | Review | J Steroid Biochem Mol Biol | Review of induction agents used in animal models of polycystic ovary syndrome. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04456P | PROGYNOVA TABLET 2 mg | Tablet, sugar coated | Not stated in the licence record |
| SIN04778P | PROGYLUTON TABLET | Tablet, sugar coated | Not stated in the licence record |

Both are valid single-ingredient oral products from Bayer Weimar GmbH und Co. KG.

## Safety Considerations

The knowledge graph lists the following conditions as contraindications for this drug. These come from graph data, not from label text, so they should be confirmed against the package insert:

- **Cardiovascular and metabolic:** hypertension, congestive heart failure, diabetes mellitus, diabetic ketoacidosis, hypertriglyceridemia, hypercalcemia (including humoral hypercalcemia of malignancy)
- **Hepatic, renal and biliary:** liver disease, kidney disease, gallbladder disease
- **Neurological and psychiatric:** epilepsy, anxiety disorder, neurotic disorder, dysthymic disorder
- **Porphyrias:** inherited porphyria, porphyrin metabolism disease, porphyria
- **Endocrine and autoimmune:** hypothyroidism (including myxedema and congenital hypothyroidism), systemic lupus erythematosus (including paediatric)
- **Respiratory:** asthma (intrinsic and allergic)
- **Other:** benign prostatic hyperplasia, gynecomastia, breast hypertrophy, pyoureter

No drug interaction records were found. Please refer to the package insert for warnings and complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials or publications behind it (Level L5), and the high TxGNN score is a model output only. The mechanistic link through fragile X-associated primary ovarian insufficiency is plausible but covers only the low-estrogen component. The only registered trial (anovulation, Phase 4, status unknown, no results) concerns a lower-ranked prediction. Most of the supporting literature uses estradiol valerate to cause ovarian dysfunction in animals rather than treat it. Package insert warnings and contraindications are also unavailable, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, to enable safety screening
- Mechanism of action data from DrugBank
- A targeted literature search on estrogen replacement in FXPOI and FMR1 premutation carriers
- Clarification of the approved indication text for the two Singapore licences
- Results or a status update for NCT02186782 if anovulation is pursued as an alternative direction
- Route and formulation compatibility assessment for the proposed indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

