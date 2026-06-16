---
layout: default
title: Clotrimazole
parent: 僅模型預測 (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Clotrimazole
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

# Clotrimazole: From Candidiasis / Dermatophytosis to Acne

## One-Sentence Summary

Clotrimazole is a synthetic broad-spectrum imidazole antifungal, globally established as a first-line topical treatment for candidiasis and dermatophytosis, though it is currently not registered in Singapore.
The TxGNN model ranks **Acne (disease)** as its top repurposing prediction with a score of 99.86%, yet this is supported by only **1 clinical trial** (currently suspended) and **no published literature** directly evaluating Clotrimazole for acne.
Given the fundamental mismatch between Clotrimazole's antifungal mechanism and acne's predominantly bacterial and inflammatory pathophysiology, the current evidence base is insufficient to support further development in this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally used for candidiasis (vulvovaginal, oropharyngeal), tinea pedis, tinea corporis, and other superficial fungal infections |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Clotrimazole is a synthetic imidazole antifungal that inhibits the fungal cytochrome P450 enzyme CYP51 (lanosterol 14α-demethylase), thereby blocking ergosterol biosynthesis and disrupting the fungal cell membrane. This mechanism is highly specific to organisms that depend on ergosterol as a structural membrane component — primarily fungi and some protozoa.

Acne vulgaris, by contrast, is a multifactorial disease driven primarily by *Cutibacterium acnes* (a Gram-positive anaerobic bacterium), excess sebum production, follicular hyperkeratinization, and a cascade of host inflammatory responses mediated by innate immunity. None of these pathological drivers are directly addressed by ergosterol synthesis inhibition, and *C. acnes* does not possess a CYP51-dependent ergosterol pathway.

The only mechanistic bridge that could be constructed is indirect: in cases of pityrosporum folliculitis (a *Malassezia*-associated acneiform eruption that is frequently misdiagnosed as acne vulgaris), antifungal treatment including azoles may be appropriate and effective. However, this represents a distinct clinical entity from acne vulgaris itself. Without any supporting literature or completed trials, this mechanistic link remains entirely hypothetical, and the TxGNN prediction here is most likely capturing broad dermatological co-occurrence patterns rather than a true pharmacological relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Evaluated a three-drug combination (Clotrimazole 1% + Gentamicin 0.1% + Beclomethasone 0.025%) topical cream in patients with contaminated dermatosis presenting bilateral symmetrical lesions. The trial was suspended before completion, and because Clotrimazole was only one component of a fixed-dose combination, its independent contribution to any anti-acne effect cannot be determined from this study. |

---

## Literature Evidence

Currently no related literature is available directly evaluating Clotrimazole for acne.

---

## Singapore Market Information

Clotrimazole has **no registered products** in Singapore. No authorization numbers, product names, dosage forms, or approved indications are on record with HSA.

---

## Safety Considerations

Please refer to the package insert for safety information. (Safety warnings, contraindications, and drug interaction data were not available in this Evidence Pack.)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for Clotrimazole in acne is absent — its antifungal CYP51-inhibition mechanism does not address the bacterial (*C. acnes*) and inflammatory drivers of acne vulgaris — and the sole identified clinical trial was suspended before yielding interpretable data within a combination product design that precludes attributing any effect to Clotrimazole alone.

**To proceed, the following would be needed:**
- A clearly defined mechanistic hypothesis: if the target is *Malassezia*-associated pityrosporum folliculitis rather than true acne vulgaris, this distinction must be made explicit and the indication reframed accordingly
- Preclinical or mechanistic studies demonstrating any direct activity against *C. acnes*, sebaceous gland regulation, or anti-inflammatory effects relevant to acne pathogenesis
- At least one completed, prospective clinical study with Clotrimazole as a monotherapy or well-characterized component in a dermatologist-diagnosed acne population
- Full safety profile review, including retrieval of the TFDA / HSA package insert data currently unavailable in this pack

> **Note:** While acne ranks first by TxGNN prediction score, the second-ranked indication — **vulvovaginitis** — carries substantially stronger evidence (Evidence Level **L1**, ≥3 completed Phase 3/4 RCTs with Clotrimazole as the primary intervention, recommendation: **Proceed with Guardrails**). Reviewers may wish to prioritize the vulvovaginitis assessment for near-term regulatory and market access planning in Singapore.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

