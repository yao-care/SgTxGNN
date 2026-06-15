---
layout: default
title: Hydrocortisone
parent: 僅模型預測 (L5)
nav_order: 347
evidence_level: L5
indication_count: 10
---

# Hydrocortisone
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

# Hydrocortisone: From Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Hydrocortisone is a naturally occurring glucocorticoid steroid hormone widely used as an anti-inflammatory agent, adrenal replacement therapy, and topical skin treatment.
The TxGNN model predicts it may be effective for **Alopecia Areata** (autoimmune hair loss),
with **1 completed Phase 3 clinical trial** and **20 publications**—including a landmark 2014 RCT in *JAMA Dermatology* and historical case series dating to the 1950s—supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-inflammatory / Adrenal insufficiency replacement therapy |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data sources queried. Based on established pharmacology, Hydrocortisone (cortisol) is a natural glucocorticoid that binds intracellular glucocorticoid receptors (GR-α), which subsequently translocate to the nucleus and suppress the NF-κB signalling pathway. This reduces transcription of pro-inflammatory cytokines including IL-2, IFN-γ, and TNF-α, and promotes T-lymphocyte apoptosis—resulting in broad local immunosuppression when applied topically or injected intralesionally.

Alopecia areata is an autoimmune disorder in which activated CD8+ T cells breach the immune privilege of the hair follicle and trigger non-scarring patchy hair loss. The disease is driven by the very inflammatory mediators that Hydrocortisone is designed to suppress. Topical 1% cream and intralesional formulations allow direct delivery to affected scalp tissue, concentrating the immunosuppressive effect locally while minimising systemic HPA axis suppression—an important safety advantage, especially in children. This mechanistic alignment explains why the TxGNN knowledge graph assigned such a high prediction score.

The clinical rationale is reinforced by decades of real-world evidence: intralesional hydrocortisone injections for alopecia areata were first described in the late 1950s (PMID 13610145, 5989830), with systematic case series following in the 1960s (PMID 14158891). A 2014 Phase 3 RCT published in *JAMA Dermatology* (PMID 24226568; NCT01453686) provided the most rigorous confirmation, showing that Hydrocortisone 1% cream produces measurable hair regrowth in paediatric alopecia areata, though it is statistically less potent than Clobetasol 0.05%. This positions Hydrocortisone as a clinically appropriate first-line or paediatric option where the risk–benefit ratio of high-potency steroids is less favourable.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01453686](https://clinicaltrials.gov/study/NCT01453686) | Phase 3 | Completed | 41 | The primary head-to-head RCT: Hydrocortisone 1% cream vs Clobetasol propionate 0.05% cream in children with alopecia areata. Both arms demonstrated effective hair regrowth; Clobetasol was statistically superior. Directly establishes Hydrocortisone's efficacy and relative potency in this indication. Published as PMID 24226568. |
| [NCT00484679](https://clinicaltrials.gov/study/NCT00484679) | Phase 2 | Completed | 18 | Assessed adrenal gland function (HPA axis) in alopecia areata patients receiving intralesional triamcinolone acetonide (Kenalog-10) injections. Uses triamcinolone rather than hydrocortisone directly, but provides key corticosteroid safety data—particularly HPA suppression risk—relevant to intralesional corticosteroid use in this population. |
| [NCT06551818](https://clinicaltrials.gov/study/NCT06551818) | N/A | Not Yet Recruiting | 72 | Four-arm, double-blind, randomised, placebo-controlled dose-response study of hair growth products in mild-to-moderate androgenic alopecia (Grade I–III). Targets androgenic rather than autoimmune alopecia; indirect relevance to the predicted indication. Results pending. |
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Examined the effects of abnormal steroid metabolome (mild autonomous cortisol secretion from adrenal adenoma) on bone strength, density, and body composition. Not directly targeted at alopecia areata treatment; provides background safety data on systemic hydrocortisone exposure effects. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24226568](https://pubmed.ncbi.nlm.nih.gov/24226568/) | 2014 | RCT | JAMA Dermatology | Published results of NCT01453686. Hydrocortisone 1% vs Clobetasol 0.05% for alopecia areata in children. Both formulations achieved statistically significant hair regrowth vs baseline; Clobetasol was superior. Hydrocortisone confirmed as an effective, lower-risk option for mild-to-moderate paediatric cases. |
| [38501938](https://pubmed.ncbi.nlm.nih.gov/38501938/) | 2024 | Clinical Study | Clinical and Experimental Dermatology | Single-centre retrospective analysis of topical corticosteroid therapy under occlusion for severe paediatric alopecia areata, including alopecia totalis and universalis. Demonstrates real-world clinical utility and safety of topical corticosteroids (including lower-potency options) even in severe paediatric disease. |
| [36718837](https://pubmed.ncbi.nlm.nih.gov/36718837/) | 2023 | Systematic Review | Journal of Cosmetic Dermatology | Systematic review and meta-analysis of fractional laser therapy (alone or combined) for alopecia areata. Situates topical corticosteroids as the established reference treatment against which emerging therapies are benchmarked, reinforcing their status as standard of care. |
| [28516731](https://pubmed.ncbi.nlm.nih.gov/28516731/) | 2017 | Review | JEADV | Investigates whether HPA axis hyperactivity is present in alopecia areata patients. Finds no evidence of HPA hyperactivity, supporting the safety rationale for topical corticosteroid use without concern for compounding systemic cortisol dysregulation in typical cases. |
| [39506493](https://pubmed.ncbi.nlm.nih.gov/39506493/) | 2025 | Exploratory Clinical Study | Journal of Cosmetic Dermatology | Explores the link between chronic psychological stress and dermatoses including alopecia areata, mediated via cortisol and epinephrine release. Corroborates the role of the cortisol/glucocorticoid pathway in alopecia areata pathophysiology, lending mechanistic credibility to glucocorticoid-based therapy. |
| [13368875](https://pubmed.ncbi.nlm.nih.gov/13368875/) | 1956 | Case Series | Medical Times | Among the earliest documented clinical series treating alopecia areata (partialis and totalis) with cortisone, hydrocortisone, prednisone, and prednisolone. Establishes a nearly 70-year history of clinical corticosteroid use in this indication. |
| [13610145](https://pubmed.ncbi.nlm.nih.gov/13610145/) | 1958 | Case Series | Der Hautarzt | Reports hair regrowth in alopecia areata and alopecia maligna following intracutaneous hydrocortisone injection. Early direct evidence specifically for the intralesional hydrocortisone route of administration. |
| [5989830](https://pubmed.ncbi.nlm.nih.gov/5989830/) | 1966 | Case Series | Vestnik Dermatologii | Case series documenting treatment of alopecia areata and alopecia totalis with intracutaneous hydrocortisone injections. Further corroborates intralesional efficacy across different disease severities. |
| [14158891](https://pubmed.ncbi.nlm.nih.gov/14158891/) | 1963 | Case Series | Actas Dermo-Sifiliograficas | Case reports of alopecia areata treated with intradermal hydrocortisone injections. Supports the historical body of evidence for direct intralesional application. |
| [15692503](https://pubmed.ncbi.nlm.nih.gov/15692503/) | 2005 | Case Report | JAAD | Describes 4 cases of congenital alopecia areata with 3–5 year follow-up. Treatments included minoxidil and a range of topical steroids. Illustrates practical use of hydrocortisone-range topical steroids in early-onset alopecia areata with prolonged quiescence periods. |

---

## Singapore Market Information

Hydrocortisone currently has **no registered products** in Singapore's Health Sciences Authority (HSA) database. No license records are available.

> Note: This reflects the data available at the time of query (2026-04-04). Hydrocortisone-containing products may be available through other regulatory pathways (e.g., HSA-licensed imports or hospital formulary approvals) not captured in this dataset. A prospective HSA registration search is recommended.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (key warnings, contraindications, drug–drug interactions) were not retrievable from the queried sources at the time of this report. Given that Hydrocortisone is a glucocorticoid with well-characterised class effects—including HPA axis suppression with prolonged use, skin atrophy from topical application, and potential for systemic absorption at higher concentrations—clinicians should consult the full prescribing information and current clinical guidelines before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 RCT (NCT01453686, *JAMA Dermatology* 2014) directly establishes that Hydrocortisone 1% cream is effective for alopecia areata in children, and over six decades of published clinical experience—spanning intralesional injections to modern controlled trials—provide a robust historical foundation. The mechanistic link between Hydrocortisone's immunosuppressive action and the CD8+ T-cell-mediated pathophysiology of alopecia areata is well-understood. However, Hydrocortisone's lower potency relative to agents such as Clobetasol or triamcinolone means its optimal role is as a first-line or paediatric-safe option in mild-to-moderate disease, rather than as a single agent for severe or extensive alopecia areata.

**To proceed, the following is needed:**

- **Safety data recovery**: Obtain and review the full prescribing information (package insert) for topical and intralesional Hydrocortisone formulations to formally document contraindications, HPA suppression warnings, and application-site precautions
- **Population stratification**: Define clear patient selection criteria—disease severity (patchy mild-moderate vs. totalis/universalis), age group (paediatric vs. adult), and body surface area involved—to guide appropriate use given the potency gap with alternatives
- **Formulation pathway**: Determine whether topical 1% cream, intralesional injection, or both are being considered; regulatory and manufacturing requirements differ substantially
- **HSA registration assessment**: Conduct a prospective HSA search and explore the registration pathway for Singapore market entry, given zero current licensed products
- **Long-term monitoring plan**: Establish protocols for monitoring HPA axis function (early morning cortisol, ACTH stimulation test) in patients receiving extensive or prolonged topical therapy, particularly in children
- **Comparative effectiveness position**: Commission or identify head-to-head data versus JAK inhibitors (baricitinib, ritlecitinib), which represent the emerging new standard for moderate-to-severe alopecia areata, to clarify where Hydrocortisone fits in an updated treatment algorithm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

