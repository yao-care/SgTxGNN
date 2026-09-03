---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 814
evidence_level: L5
indication_count: 10
---

# Prednisone
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

# Prednisone: From Broad-Spectrum Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

> Prednisone is a well-established systemic glucocorticoid; detailed original-indication data was not available in this dataset, but it is broadly used across inflammatory and autoimmune conditions.
> The TxGNN model predicts it may be effective for **Alopecia Areata**,
> with **32 clinical trials** and **21 publications** currently linked in the evidence pool, though only a small subset directly studies prednisone in this disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not documented in current regulatory dataset (no Singapore license records available) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on known pharmacology, prednisone is a broad-spectrum systemic glucocorticoid whose efficacy across a wide range of inflammatory and autoimmune conditions is well established; this class-level mechanism may reasonably extend to alopecia areata.

Alopecia areata is a T-cell-mediated autoimmune disease in which cytotoxic T cells attack the immune-privileged hair follicle. Prednisone, as a systemic glucocorticoid, broadly suppresses T-cell activation and key pro-inflammatory cytokines (IFN-γ, IL-15), which directly maps onto the underlying disease mechanism. This is not a novel discovery — systemic corticosteroids have been used off-label for alopecia areata for decades, particularly in acute or diffuse presentations, even though it has never been a formally approved indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | RCT testing methotrexate alone vs. methotrexate + low-dose prednisone vs. placebo in severe alopecia areata (pelade grave); directly evaluates prednisone's role as adjunct therapy. |
| [NCT03843125](https://clinicaltrials.gov/study/NCT03843125) | Phase 3 | Terminated | 1147 | Long-term safety/efficacy study of baricitinib in an autoimmune indication linked to alopecia areata via shared immune-modulation pathway; trial terminated, drug is not prednisone. |

*Note: The broader knowledge-graph evidence pool also surfaced numerous SLE, lupus nephritis, and oncology trials involving prednisone as a background therapy; these were excluded here as they do not directly evidence a prednisone–alopecia areata relationship.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | JAMA Dermatology | 2-step double-blind RCT: methotrexate alone vs. methotrexate + low-dose prednisone in alopecia areata totalis/universalis. |
| [38650498](https://pubmed.ncbi.nlm.nih.gov/38650498/) | 2024 | Cohort | Ital J Dermatol Venereol | Real-world Italian cohort of hospitalized alopecia areata patients, characterizing treatment patterns including corticosteroid use. |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Cohort/Follow-up | Archives of Dermatology | Follow-up of 18 alopecia areata patients treated with alternate-day prednisone; initial response but limited long-term benefit and notable steroid side effects. |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort | Dermatology (Basel) | Efficacy/safety of methotrexate combined with low-to-moderate dose corticosteroids in severe alopecia areata. |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case series | Clin Exp Dermatol | 8-case series showing major improvement in very severe alopecia areata with baricitinib + low-dose corticosteroids. |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | Archives of Dermatology | Review of alopecia areata therapies including corticosteroids, discussing efficacy, safety, and mechanism. |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Clinical study | Ann Dermatol Venereol | Evaluation of once-monthly oral pulsed prednisone for alopecia areata. |
| [9732014](https://pubmed.ncbi.nlm.nih.gov/9732014/) | 1998 | Clinical study | Int J Dermatol | Severe alopecia areata treated with systemic corticosteroids, demonstrated as an effective option. |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Clinical/immunopathologic study | J Am Acad Dermatol | Systemic cyclosporine + low-dose prednisone in chronic severe alopecia areata with immunopathologic evaluation. |
| [911178](https://pubmed.ncbi.nlm.nih.gov/911178/) | 1977 | Clinical study | Archives of Dermatology | Prednisone therapy for alopecia areata. |

---

## Singapore Market Information

Currently no registration records available — this drug/formulation has no listed authorizations in the Singapore regulatory dataset (market status: **Not Marketed**, total registrations: **0**).

---

## Safety Considerations

Please refer to the package insert for safety information. No structured warnings, contraindications, or drug-interaction data were available in this evidence pack; the underlying TFDA/HSA label warning and contraindication data gap (DG001) is flagged as **Blocking** for progression to formal safety review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between systemic glucocorticoid action and alopecia areata's T-cell-mediated pathology is well established, and decades of off-label clinical use (Phase 3 RCT, multiple cohort studies) support plausibility — corresponding to Evidence Level L2. However, this is not a formally approved indication, and critical safety documentation is missing.

**To proceed, the following is needed:**
- Resolve DG001 (Blocking): obtain HSA/TFDA-equivalent package insert warnings and contraindications before any S1 safety evaluation
- Resolve DG002: obtain formal DrugBank MOA data to strengthen mechanistic rationale documentation
- Confirm Singapore market/registration pathway, since the drug currently has zero local registrations
- Distinguish prednisone-specific evidence from broader corticosteroid-class evidence (e.g., baricitinib trials) when finalizing the clinical evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

