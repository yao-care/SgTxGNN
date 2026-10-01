---
layout: default
title: Prednisolone
parent: Medium Evidence (L3-L4)
nav_order: 812
evidence_level: L3
indication_count: 10
---

# Prednisolone
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Prednisolone: From Systemic Corticosteroid Therapy to Alopecia Areata

## One-Sentence Summary

Prednisolone is an oral corticosteroid with anti-inflammatory and immunosuppressive activity, and the Singapore registration records provide no approved-indication text for it.
The TxGNN model predicts it may be effective for **alopecia areata**.
Of 17 retrieved trials, only **3 relate to alopecia**: a needle-free steroid injection comparison, an oral pulse methylprednisolone study and a tofacitinib study in which some participants also received prednisolone.
There are **20 publications**, including systematic reviews and pulse-steroid cohort studies, but no Phase 3 RCT of prednisolone in this condition.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for prednisolone is not available in this evidence pack. Based on known pharmacology, glucocorticoids suppress T-cell-mediated inflammation.

Alopecia areata is an autoimmune disease in which T cells attack the hair follicle. Suppressing this attack and helping restore follicular immune privilege is biologically plausible. One mechanistic study (PMID 30294905) reports that oral pulse steroids alter serum and tissue TNF-α levels in alopecia areata, which fits this idea.

Clinical support for prednisolone itself is limited. It comes mainly from pulse-dose cohort studies and reviews of systemic corticosteroids. A placebo-controlled trial of oral pulse prednisolone exists (PMID 15692475), but this report does not have its results.

## Clinical Trial Evidence

Only trials related to alopecia are listed. The other retrieved trials, mostly in systemic lupus erythematosus, do not concern this drug–disease pair.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Higher-dose, more frequent oral pulse methylprednisolone (a related corticosteroid) in severe alopecia areata |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A (observational) | Completed | 296 | Tofacitinib safety and effectiveness in alopecia, given with or without adjuvant prednisolone |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | Unknown | 20 | Needle-free Dermojet vs standard syringe for steroid injection in alopecia areata; not an oral prednisolone trial |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Compares treatments for alopecia areata, including immunosuppressants, hair growth stimulants and contact immunotherapy |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic review | Australas J Dermatol | Reviews the evidence for systemic treatments in alopecia areata, totalis and universalis |
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | Placebo-controlled trial | J Am Acad Dermatol | Oral pulse prednisolone vs placebo; earlier pulse-steroid studies had not been randomized or placebo-controlled |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Reviews efficacy, relapse rates, side effects and response predictors of pulse corticosteroids |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | Reviews pulse-dose corticosteroid regimens and side effects in children |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Cohort | Dermato-endocrinology | Medium-dose prednisolone pulse therapy; systemic prednisolone appears effective in early stages, but significant side effects can lead to discontinuation |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohort | J Dtsch Dermatol Ges | Sequential high- then low-dose systemic corticosteroids in severe childhood alopecia areata |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective cohort | Dermatol Ther | Methylprednisolone alone vs with methotrexate in 26 patients with extensive alopecia areata |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Retrospective study | J Eur Acad Dermatol Venereol | Continuation rates of steroid-sparing agents in 138 patients with chronic alopecia areata |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Mechanistic study | J Cosmet Dermatol | Changes in TNF-α levels as a possible mechanism of oral pulse steroids |

## Singapore Market Information

Showing 5 of 10 registrations.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN04845P | PRELONE SYRUP 3 mg/5 ml | Syrup |
| SIN04190P | XEPASONE TABLET 5 mg | Tablet |
| SIN04237P | PREDNISOLONE TABLET 5 mg (Beacons Pharmaceuticals) | Tablet |
| SIN04726P | PREDNISOLONE TABLET 5 mg (Atlantic Laboratories) | Tablet |
| SIN07771P | YSP PREDNISOLONE TABLET 5 mg | Tablet |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The biological rationale is plausible and the literature includes reviews and pulse-steroid cohorts. However, no Phase 3 RCT of prednisolone in alopecia areata was identified, and the evidence level is L3. The package insert warnings and contraindications are also missing, which blocks the safety screening step.

**To proceed, the following is needed:**
- Download and parse the HSA package insert for warnings and contraindications (blocking)
- Mechanism-of-action data from DrugBank
- Full-text review of the placebo-controlled pulse prednisolone trial (PMID 15692475)
- A plan for known guardrails if pursued:
  - Relapse after discontinuation is common.
  - Systemic steroid toxicity limits long-term use.
  - Approved JAK inhibitors are comparators to consider.

*Note on other predictions:* The other nine predicted indications have little or no supporting evidence. The exception is idiopathic steroid-sensitive nephrotic syndrome, where prednisolone is already standard first-line therapy and is not a true repurposing candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

