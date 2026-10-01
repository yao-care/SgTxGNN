---
layout: default
title: Acyclovir
parent: Low Evidence (L5)
nav_order: 37
evidence_level: L5
indication_count: 10
---

# Acyclovir
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

# Acyclovir: From Antiviral Therapy to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Acyclovir is an antiviral drug that is currently marketed in Singapore under 20 registrations.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**, but the prediction rests on model score alone: there are **0 clinical trials** and **2 publications**, and neither publication evaluates acyclovir.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records supplied |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.67% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Acyclovir is an antiviral that acts through thymidine-kinase-dependent activation, so it is expected to work against viruses that carry their own thymidine kinase, such as herpesviruses.

Punctate epithelial keratoconjunctivitis has several causes. A herpetic cause would fit acyclovir's mechanism, but nothing in the retrieved evidence shows that. An adenoviral cause would not fit, because adenoviruses lack a viral thymidine kinase.

The two retrieved papers concern drug-induced corneal lipidosis in AIDS patients and microsporidial keratoconjunctivitis. Microsporidia are not herpesviruses, so acyclovir has no mechanistic rationale there. The high graph score is therefore not backed by clinical or mechanistic evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7825685](https://pubmed.ncbi.nlm.nih.gov/7825685/) | 1995 | Case series | American Journal of Ophthalmology | Two AIDS patients treated for opportunistic infections developed drug-induced corneal lipidosis. Acyclovir is not evaluated. |
| [21934222](https://pubmed.ncbi.nlm.nih.gov/21934222/) | 2011 | Case series | Indian Journal of Pathology & Microbiology | Characteristics of microsporidial keratoconjunctivitis in an eastern Indian cohort. Acyclovir is not evaluated. |

## Singapore Market Information

Approved indication text is not provided for these licences. Five of the 20 registrations are shown.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN09298P | VILERM TABLET 400 mg | Tablet |
| SIN10307P | APO-ACYCLOVIR TABLET 400 mg | Tablet |
| SIN09377P | ACYCLOVIR 800 STADA TABLET 800 mg | Tablet |
| SIN08761P | MEDOVIR 200 TABLET 200 mg | Tablet, film coated |
| SIN08641P | ZORAL CREAM 5% | Cream |

Across all registrations the listed forms are oral, cream, suspension and injectable. No ophthalmic form appears in the data, so route compatibility with an eye indication is unconfirmed.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support is a graph-model score. There are no trials, and the two retrieved papers do not test acyclovir. The mechanism is plausible only if the cause is herpetic, which the evidence does not show.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications
- Mechanism of action data from DrugBank
- Evidence tying acyclovir to a specific cause of punctate epithelial keratoconjunctivitis (for example, herpetic), ideally from controlled studies
- Confirmation of a suitable ophthalmic route or formulation
- A separate review of the rank 2 prediction, common wart. It has L2 evidence and six registered trials of intralesional acyclovir, all small (40–92 participants).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

