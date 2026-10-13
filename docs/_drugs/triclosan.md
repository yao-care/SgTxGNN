---
layout: default
title: Triclosan
parent: Medium Evidence (L3-L4)
nav_order: 1022
evidence_level: L4
indication_count: 10
---

# Triclosan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Triclosan: From an Unspecified Topical Antimicrobial Use to Acne

## One-Sentence Summary

Triclosan is a broad-spectrum antibacterial agent that is currently registered in Singapore as a single-ingredient lotion product (a bath oil), although no approved indication text is on record.
The TxGNN model predicts it may be effective for **acne**, but there are **0 clinical trials** and only **1 indirectly related publication** (a review about a different disease, hidradenitis suppurativa) supporting this direction.
The evidence is weak, and the high model score is not backed by direct clinical data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 97.38% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, triclosan is a broad-spectrum antibacterial that inhibits bacterial enoyl-acyl carrier protein reductase (FabI). It has activity against *Cutibacterium acnes* and *Staphylococcus* species.

Because bacterial colonisation contributes to acne, this gives a plausible but indirect link between the drug and the predicted indication. This is only a mechanistic hypothesis, however. The single publication retrieved concerns treatment frameworks for hidradenitis suppurativa (acne inversa), a different disease, and does not evaluate triclosan.

The high TxGNN score (97.38%) should therefore be read as a model signal, not as confirmation of clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acne.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30176066](https://pubmed.ncbi.nlm.nih.gov/30176066/) | 2019 | Systematic review | J Eur Acad Dermatol Venereol | Systematic review and consensus recommendations for hidradenitis suppurativa/acne inversa management. It does not evaluate triclosan and concerns a different disease, so it offers only indirect context. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11468P | QV FLARE UP BATH OIL | Lotion | Not stated |

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph (not from label text)**: The TxGNN knowledge graph links triclosan to contraindication edges for epilepsy, sudden cardiac arrest, heart conduction disease and respiratory failure. These are model-derived associations and should be verified against official labelling.
- **Thyroid and endocrine signals from the literature**: Studies reviewed for the thyroid-related prediction examine triclosan as an exposure that may disrupt thyroid hormone homeostasis. These include pregnancy cohorts, a toothpaste-use study and animal work showing reduced thyroid hormone levels. They indicate a potential safety concern, not a therapeutic benefit.
- **Drug interactions**: No interaction records were found.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction rests on a plausible antibacterial mechanism but has no direct clinical trial or literature support. The only retrieved publication addresses a different disease. In addition, the local registration lacks indication and label safety data, and triclosan carries endocrine/thyroid safety signals in the literature.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Mechanism of action data confirmed from DrugBank
- Direct evidence of triclosan efficacy in acne (clinical trials or relevant studies)
- A formal safety assessment addressing the thyroid and endocrine-disruption signals
- Confirmation of the approved indication and route of use for the registered Singapore product

---

## Other Predicted Indications (Brief Notes)

Other predictions were also reviewed, and none currently supports advancing:

- **Scalp dermatosis (score 94.15%, L4, Hold)**: One retrospective safety study (NCT05105139, n=90) of Sebryl/Sebryl Plus products in seborrheic dermatitis and scalp psoriasis. It does not confirm triclosan as the active ingredient and did not assess efficacy.
- **Thyroid gland disease (score 88.04%, L4, Hold)**: The literature treats triclosan as a potential thyroid disruptor, not a treatment. This is a safety concern and argues against repurposing.
- **Familial adrenal hypoplasia with absent pituitary LH, PAGOD syndrome, elevated plasma zinc, primary release disorder of platelets, pseudo-von Willebrand disease, multiple endocrine neoplasia, familial pityriasis rubra pilaris (all L5, Hold)**: Prediction-only signals with no plausible mechanism or supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

