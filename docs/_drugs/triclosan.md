---
layout: default
title: Triclosan
parent: Low Evidence (L5)
nav_order: 1012
evidence_level: L5
indication_count: 10
---

# Triclosan
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

# Triclosan: From Antibacterial Agent to Acne

## One-Sentence Summary

Triclosan is a broad-spectrum antibacterial agent. In Singapore it is registered in one topical lotion product (QV Flare Up Bath Oil), and no approved indication text is recorded for that product.
The TxGNN model predicts it may be useful for **acne**, but the supplied evidence contains **no triclosan-specific clinical trials and no triclosan-specific publications** for this indication.
This is a mechanism-plausible hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 97.38% |
| Evidence Level | L5 (model prediction only; the pack labels it L4, but no preclinical or mechanism studies were supplied) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. Based on general pharmacology, triclosan inhibits bacterial enoyl-ACP reductase (FabI), an enzyme in bacterial fatty-acid synthesis. This gives it broad antibacterial activity.

Acne involves *Cutibacterium acnes* colonisation of the pilosebaceous unit. An agent that suppresses skin bacteria could plausibly reduce this component, which is why the model's prediction is biologically reasonable. However, the evidence supplied does not contain triclosan-specific acne data, so the link remains theoretical. Acne also has non-bacterial drivers, such as sebum production, follicular keratinisation and inflammation, which an antibacterial alone would not address.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00907257](https://clinicaltrials.gov/study/NCT00907257) | Phase 4 | Completed | 247 | Compared two tretinoin gel (RETIN-A MICRO 0.04%) plus 5% benzoyl peroxide wash regimens for facial acne vulgaris. Triclosan is not involved, so this is not evidence for the drug. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30176066](https://pubmed.ncbi.nlm.nih.gov/30176066/) | 2019 | Systematic review | J Eur Acad Dermatol Venereol | HS ALLIANCE treatment recommendations for hidradenitis suppurativa/acne inversa. This is a different condition from acne vulgaris and is not specific to triclosan. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11468P | QV FLARE UP BATH OIL (EGO Pharmaceuticals) | Lotion | Not stated in the record |

## Safety Considerations

- **Drug Interactions**: No interaction records were found.
- **Endocrine and thyroid signal**: The supplied literature (10 of the 15 listed publications were provided) discusses triclosan as a potential endocrine disruptor. Evidence includes reduced thyroxine in rats (PMID 29462796) and reviews of reproductive, cardiovascular and thyroid effects (PMID 36232730). A critical review concludes human studies show no evidence that personal-care-product exposure affects the thyroid system (PMID 24897554). Human data are mixed, include a randomised intervention in pregnancy (PMID 28939492), and need careful interpretation.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 97.38% model score is not backed by any triclosan-specific trial or publication. The only trial found tested a different drug. Long-term endocrine-safety concerns for triclosan are also unresolved. The other nine predicted indications are either unsupported or, for thyroid gland disease, reflect a safety signal rather than a therapeutic one.

**To proceed, the following is needed:**
- The HSA package insert, to confirm warnings, contraindications and the approved indication
- Mechanism-of-action data from DrugBank
- Triclosan-specific in vitro or clinical data against *C. acnes* or in acne
- A review of the thyroid and endocrine safety literature in the context of repeated topical use
- A route and formulation compatibility assessment for acne
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

