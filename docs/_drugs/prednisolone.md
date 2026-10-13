---
layout: default
title: Prednisolone
parent: High Evidence (L1-L2)
nav_order: 821
evidence_level: L2
indication_count: 10
---

# Prednisolone
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Prednisolone: From Autoimmune Disease to Alopecia Areata

## One-Sentence Summary

Prednisolone is a glucocorticoid originally used for autoimmune and inflammatory conditions such as Crohn disease, adrenocortical insufficiency and acute lymphoblastic leukaemia.
The TxGNN model predicts it may be effective for **alopecia areata**, with **0 registered clinical trials** and **20 publications** (including one RCT, a network meta-analysis and several reviews) currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune disease (the Singapore licence records list no approved indication text; this is taken from the knowledge-graph indication list, which also includes Crohn disease, adrenocortical insufficiency and acute lymphoblastic leukaemia) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, prednisolone is a glucocorticoid that suppresses T-cell activation and the production of pro-inflammatory cytokines.

Alopecia areata is an autoimmune disease in which T cells attack hair follicles and the follicle's immune privilege collapses. This matches the autoimmune use for which prednisolone is already established. One study in the literature also reports that oral pulse steroids alter serum and tissue TNF-α levels in alopecia areata, which suggests a plausible mechanism.

There are limits. Hair loss often returns after the drug is withdrawn, and long-term steroid use causes cumulative toxicity. Pulse or short-course dosing is therefore the usual approach.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | J Am Acad Dermatol | Placebo-controlled trial of oral pulse prednisolone in alopecia areata; earlier pulse-steroid studies were neither randomised nor placebo-controlled |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network meta-analysis | Cochrane Database Syst Rev | Compares treatments for alopecia areata, including immunosuppressants, hair growth stimulants and contact immunotherapy |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic review | Australas J Dermatol | Reviews randomised evidence for systemic treatments in alopecia areata, totalis and universalis; efficacy evidence is variable |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | Reviews efficacy, relapse rates, side effects and prognostic factors of corticosteroid pulse therapy |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | Reviews dosing regimens and side effects of pulse corticosteroids in children; regimens are not well established |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Cohort/Case series | Dermato-endocrinology | Medium-dose prednisolone pulse therapy; effective in early stages but significant side effects led to discontinuation |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Cohort/Case series | J Dtsch Dermatol Ges | Sequential high- then low-dose steroids for severe childhood disease; relapse after stopping is inevitable |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Cohort study | Dermatol Ther | Oral pulse plus topical corticosteroids in 65 children with severe disease, with long-term follow-up |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | Retrospective study | J Eur Acad Dermatol Venereol | Continuation rates of steroid-sparing agents (azathioprine, methotrexate, cyclosporine) in 138 patients with chronic disease |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Mechanistic study | J Cosmet Dermatol | Oral pulse steroids alter serum and tissue TNF-α levels, a possible mechanism of action |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN04845P | PRELONE SYRUP 3 mg/5 ml | Syrup | Not stated in the compiled data |
| SIN04190P | XEPASONE TABLET 5 mg | Tablet | Not stated in the compiled data |
| SIN04237P | PREDNISOLONE TABLET 5 mg | Tablet | Not stated in the compiled data |
| SIN04726P | PREDNISOLONE TABLET 5 mg | Tablet | Not stated in the compiled data |
| SIN07771P | YSP PREDNISOLONE TABLET 5 mg | Tablet | Not stated in the compiled data |

There are 10 valid single-ingredient licences in total, in tablet and syrup forms.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (not taken from label text): hypertension, epilepsy, hyperglycaemia, congestive heart failure, herpes simplex virus keratitis, measles, porphyria, urea cycle disorders (e.g. citrullinemia, hyperargininemia), and hypopituitarism or pituitary deficiency states.
- **Drug Interactions**: 100 interactions were found. Examples:
  - Major: adalimumab.
  - Moderate: ibuprofen, ketorolac, nifedipine, acarbose, acetazolamide, isotretinoin, ethinylestradiol, zidovudine, aldesleukin, alemtuzumab.
  - Minor: salbutamol, formoterol.
- **Literature-reported concerns**: relapse after withdrawal, side effects leading to treatment discontinuation, and cumulative steroid toxicity with long-term use.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alopecia areata is an autoimmune disease, and the mechanism fits prednisolone. Supporting evidence includes one placebo-controlled RCT, a Cochrane network meta-analysis, a systematic review and several reviews of pulse therapy. No clinical trials are registered, relapse after withdrawal is common, and cumulative steroid toxicity limits long-term use, so use should be restricted to pulse or short-course regimens.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently missing and blocking safety screening)
- Mechanism of action data from DrugBank
- A defined pulse-dosing protocol with relapse monitoring and a steroid-sparing plan
- Safety review for patients with hypertension, diabetes or hyperglycaemia, epilepsy, heart failure or active infection
- Review of the interaction with adalimumab and other major interactions

## Other Predicted Indications (Brief Note)

- **Idiopathic steroid-sensitive nephrotic syndrome** (L1, Proceed with Guardrails): prednisolone is already first-line therapy for childhood steroid-sensitive nephrotic syndrome, supported by Cochrane-level evidence and RCT data. This is effectively an established use rather than a novel repurposing. Several retrieved articles concern steroid-resistant disease and are less relevant.
- **Alopecia mucinosa, Quinquaud's folliculitis decalvans, alopecia antibody deficiency** (L4, Hold): only indirect or weak case-level evidence for prednisolone itself.
- **Telogen effluvium, hereditary hypotrichosis with recurrent skin vesicles, alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome, atrichia with papular lesions, prolapse of lacrimal gland** (L5, Hold): model prediction only, with no trials or literature.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

