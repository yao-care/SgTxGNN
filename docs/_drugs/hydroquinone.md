---
layout: default
title: Hydroquinone
parent: Medium Evidence (L3-L4)
nav_order: 508
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Hydroquinone: predicted new indication Seborrheic keratosis (evidence level L4). Approved use: Not stated in the Singapore licence record (hydroquinone is generally…"
monitor_inn: "Hydroquinone"
predicted_indications: ["seborrheic keratosis", "vulvar inverted follicular keratosis", "exanthem (disease)", "lichen disease", "seborrheic dermatitis", "vulvar squamous neoplasm", "annular atrophic lichen planus", "hypertrophic lichen planus", "lichen planus pigmentosus", "acrodermatitis chronica atrophicans"]
---

# Hydroquinone
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

# Hydroquinone: From Skin Hyperpigmentation (Topical Depigmenting Agent) to Seborrheic Keratosis

## One-Sentence Summary

Hydroquinone is a topical depigmenting agent that inhibits melanin production, and it is marketed in Singapore as a cream (TRI-LUMA CREAM). The TxGNN model predicts it may be useful for **seborrheic keratosis**, but this rests on **0 clinical trials** and **1 observational study** that is only indirectly relevant. Evidence is weak, and the prediction should be treated as a hypothesis to test, not an established benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence record (hydroquinone is generally used for skin hyperpigmentation such as melasma) |
| Predicted New Indication | Seborrheic keratosis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Hydroquinone is generally known to inhibit tyrosinase, the enzyme that drives melanin synthesis, and so it lightens pigmented skin.

Seborrheic keratosis is a benign overgrowth of epidermal cells that is often pigmented. A link therefore exists only through pigment reduction. Hydroquinone would not be expected to affect the growth of the lesion itself. The single supporting article is a prospective observational study of combination treatment for facial pigmentary disorders in Asian patients, which is only indirect evidence for this indication.

Most of the other top predictions have no plausible mechanism. Examples include seborrheic dermatitis, vulvar squamous neoplasm, and acrodermatitis chronica atrophicans, which look like prediction-only signals. The one partial exception is **lichen planus pigmentosus** (rank 9), which has a more plausible link through pigmentation. Its evidence is mixed, however (see Literature Evidence below).

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for seborrheic keratosis.

For reference, the only trial found among the other top-ranked predictions is below. It concerns the "exanthem" prediction (rank 3) and is not evidence for seborrheic keratosis:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02138539](https://clinicaltrials.gov/study/NCT02138539) | Phase 4 | Completed | 28 | Herbal de-pigmenting regimen vs hydroquinone, applied to opposite sides of the face, for mottled hyperpigmentation and melasma. Only tangentially relevant. |

---

## Literature Evidence

For seborrheic keratosis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | Cohort | J Plast Reconstr Aesthet Surg | Prospective observational study of a combination treatment algorithm for facial pigmentary disorders in Asian patients. Indirect evidence only. |

Selected publications for **lichen planus pigmentosus** (rank 9, the only other prediction with a plausible pigment-related link):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35151757](https://pubmed.ncbi.nlm.nih.gov/35151757/) | 2023 | Review | J Am Acad Dermatol | Pathogenesis and clinical features of common pigmentary disorders, including lichen planus pigmentosus |
| [21860153](https://pubmed.ncbi.nlm.nih.gov/21860153/) | 2011 | Review | Indian J Dermatol Venereol Leprol | Overview of facial melanoses in Indian patients, including lichen planus pigmentosus |
| [34567907](https://pubmed.ncbi.nlm.nih.gov/34567907/) | 2021 | Case report | Cureus | Unilateral lichen planus pigmentosus-inversus that did not respond to clobetasol and hydroquinone |
| [38954615](https://pubmed.ncbi.nlm.nih.gov/38954615/) | 2024 | Case report | J Drugs Dermatol | Facial hyperpigmentation in a skin-lightening cream user; hydroquinone is often linked to exogenous ochronosis, which complicated diagnosis |
| [36741605](https://pubmed.ncbi.nlm.nih.gov/36741605/) | 2023 | Case report | Cureus | Unilateral linear lichen planus pigmentosus that improved with isotretinoin |
| [41531723](https://pubmed.ncbi.nlm.nih.gov/41531723/) | 2025 | Case report | HCA Healthc J Med | Lichen planus pigmentosus inversus that responded to topical tacrolimus |

The evidence for lichen planus pigmentosus consists of reviews and case reports. It includes a report of **no response** to hydroquinone, so it does not support efficacy.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12607P | TRI-LUMA CREAM | Cream | Not recorded in the licence data |

Hydroquinone is currently available in Singapore only as a topical cream.

---

## Safety Considerations

- **Contraindications flagged by the knowledge graph** (drug-disease edges from the TxGNN knowledge graph, not from label text): sunburn, adrenocortical insufficiency, Addison disease, skin atrophy, telangiectasis, capillary disease, hereditary hemorrhagic telangiectasia, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease, atopic eczema, and dermatitis. These should be verified against the package insert.
- **Literature signal**: exogenous ochronosis (blue-black skin discoloration) is a known adverse effect of hydroquinone-containing skin-lightening products. It can also mimic the conditions being treated.
- **Drug interactions**: No interaction records were found.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.73%), but the supporting evidence is a single indirect observational study, with no clinical trials for seborrheic keratosis. Hydroquinone's pigment-lightening action does not address the growth of the lesion. Most other top predictions appear to be model artefacts. Evidence level is L4.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, and the licensed indication for TRI-LUMA CREAM
- Mechanism of action data (for example from DrugBank)
- Direct clinical evidence in seborrheic keratosis, such as a small controlled study
- If pursuing a pigment-related indication such as lichen planus pigmentosus, a focused review of efficacy and a plan to monitor for ochronosis and skin irritation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

