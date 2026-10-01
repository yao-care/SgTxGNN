---
layout: default
title: Fludrocortisone
parent: Low Evidence (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Fludrocortisone
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

# Fludrocortisone: From Adrenocortical Insufficiency to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Fludrocortisone is an oral corticosteroid, mainly a mineralocorticoid. The Singapore registration record does not state an approved indication, but it is generally used to treat adrenocortical insufficiency such as Addison's disease.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma (CTCL)** with a very high score, but there are **0 clinical trials** and only **1 publication** (a 1967 paper whose title mentions neither fludrocortisone nor CTCL).
This prediction rests on the model alone and has no supporting studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the HSA record; generally adrenocortical insufficiency (Addison's disease) |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, fludrocortisone is a synthetic corticosteroid with strong mineralocorticoid activity and weak glucocorticoid activity. Its established use is replacing adrenal hormones and supporting blood pressure and salt balance.

The only conceivable link to CTCL is a class effect. Glucocorticoids can suppress T-cell-driven skin inflammation, and topical or systemic steroids are sometimes used as supportive care in skin lymphomas. However, fludrocortisone's glucocorticoid activity is weak, and it is not an established CTCL therapy. The very high score (99.58%) most likely reflects proximity in the knowledge graph rather than a demonstrated biological mechanism.

The other high-ranking predictions (cystic teratoma, dermoid cysts, exostosis and broad orbital or eye categories) also have no plausible pharmacological rationale, which suggests a graph-neighbourhood artifact. The one exception is **eye disease** (rank 6). It has early ocular research: a 2021 preclinical study of fludrocortisone in retinal degeneration and a 2022 Phase 1B safety study of intravitreal fludrocortisone acetate in geographic atrophy. That direction is separate from the CTCL prediction, and it uses a different route from the oral tablet registered in Singapore.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6028675](https://pubmed.ncbi.nlm.nih.gov/6028675/) | 1967 | Case report / historical (unverified from title) | Archives of Dermatology | "Pathergic granulomatosis." No abstract is available, and the title mentions neither fludrocortisone nor CTCL, so a link to this prediction is unconfirmed. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10680P | FLORINEF TABLET 0.1 mg (Haupt Pharma Amareg GmbH) | Tablet (oral) | Not listed in the record |

---

## Safety Considerations

Please refer to the package insert for safety information.

No drug-interaction records were found for fludrocortisone in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5). There are no registered trials, and the single citation is a 1967 paper with no abstract and no visible link to fludrocortisone or CTCL. Fludrocortisone is not an established CTCL treatment, and its glucocorticoid activity is weak.

**To proceed, the following is needed:**
- The HSA package insert, to obtain the approved indication, warnings and contraindications. Safety screening cannot proceed without it.
- Mechanism of action data from DrugBank.
- Full-text review of PMID 6028675 to check whether fludrocortisone and CTCL are actually discussed.
- A targeted search of trial registries and literature for corticosteroids or mineralocorticoids in CTCL.
- Separately, consider a focused review of the retinal (geographic atrophy) evidence, which is the only prediction with early clinical data. It would need a route other than the registered oral tablet.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

