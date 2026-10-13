---
layout: default
title: Hydrocortisone Aceponate
parent: Low Evidence (L5)
nav_order: 505
evidence_level: L5
indication_count: 10
---

# Hydrocortisone Aceponate
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

# Hydrocortisone Aceponate: From Topical Corticosteroid Therapy to Gout

## One-Sentence Summary

Hydrocortisone aceponate is a topical corticosteroid, marketed in Singapore as a cream.
The TxGNN model predicts it may be effective for **gout** (top-ranked prediction), but **no clinical trials and no publications** currently support this direction.
The evidence is model prediction only, and the mechanistic link is weak for a topical formulation.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (topical corticosteroid cream) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 97.58% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, hydrocortisone aceponate is a topical corticosteroid diester with high local anti-inflammatory potency and low systemic exposure. Its efficacy in inflammatory skin conditions is established, and mechanistically it may be applicable to inflammatory conditions more broadly.

Systemic glucocorticoids do have a role in acute gout flares. However, a topical dermal formulation is unlikely to deliver meaningful anti-inflammatory effect in joints. The mechanistic link to gout is therefore weak for this formulation, and the high score should be read as a model output rather than a pharmacological rationale.

Other top-ranked predictions show the same pattern. Allergic and intrinsic asthma, Crohn's colitis and iris disease have class-level corticosteroid rationales but no established route for this dermal product. Exostosis, benign iris neoplasm and iris cancer have no recognised mechanism and likely reflect graph proximity. Two predictions are closer to the drug's dermal use: **seborrheic dermatitis** (rank 8, a research question based on class-level knowledge) and **primary cutaneous T-cell lymphoma** (rank 7, since topical corticosteroids are used as skin-directed therapy in early mycosis fungoides, though higher-potency agents are usually preferred).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top prediction (gout), currently no related literature available.

The only supporting item among the top 10 predictions is indirect, for allergic asthma (rank 2):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11817968](https://pubmed.ncbi.nlm.nih.gov/11817968/) | 2002 | Review | American Journal of Clinical Dermatology | Review of the pharmacology and use of new and established topical corticosteroids in dermatology; it does not address airway disease |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08555P | EFFICORT LIPOCREAM 0.127% | Cream | Not stated in records |
| SIN08556P | EFFICORT CREAM 0.127% | Cream | Not stated in records |

Both products are single-ingredient, currently valid, and manufactured by Lichtenheldt GmbH Pharmazeutische Fabrik. Only topical (cream) forms are registered.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests on the model score alone, with no trials or literature. A topical, locally potent, low-systemic-exposure corticosteroid is unlikely to act on joint inflammation, so the mechanistic link is weak.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Approved indication text for the two Singapore registrations
- Mechanism of action data (e.g., from DrugBank)
- A targeted literature review for the dermal predictions (seborrheic dermatitis, cutaneous T-cell lymphoma), which are more plausible than gout and could be prioritised as research questions
- Route and formulation compatibility assessment before any non-dermal indication is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

