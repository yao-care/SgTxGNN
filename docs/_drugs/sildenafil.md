---
layout: default
title: Sildenafil
parent: Low Evidence (L5)
nav_order: 902
evidence_level: L5
indication_count: 10
---

# Sildenafil
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

# Sildenafil: From Erectile Dysfunction to Genetic Alopecia

## One-Sentence Summary

Sildenafil is an oral PDE5 inhibitor sold in Singapore under brands such as Viagra. The registration records supplied do not state its approved indication, so the "erectile dysfunction" in the title comes from general pharmacology, not the Evidence Pack. The TxGNN model ranks **Genetic Alopecia** as the best-supported of its 10 predictions, with **2 clinical trials** and **1 publication** behind it. The model's top-scoring predictions have no supporting evidence at all.

> **Note on scope:** The top-ranked prediction (Ambras-type hypertrichosis universalis congenita, 98.4%) has no trials or literature. This report therefore focuses on genetic alopecia, the only prediction with direct sildenafil evidence. All 10 predictions are summarised below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (general knowledge: erectile dysfunction) |
| Predicted New Indication | Genetic alopecia (model rank 9 of 10) |
| TxGNN Prediction Score | 75.03% |
| Evidence Level | L3 as scored in the pack; the supporting studies are small and early-phase, so this is borderline L3/L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. From general pharmacology (not from the pack), sildenafil inhibits PDE5 and raises intracellular cGMP, which causes vasodilation. Sildenafil is already marketed in Singapore as an oral drug.

The link to hair loss is plausible. The proposed mechanism is better blood flow around the hair follicle. A 2018 laboratory study (PMID 30292404) reported a hair-growth effect on human hair follicles. Two trials test topical sildenafil for hair loss, one in alopecia areata and one in male androgenetic alopecia. These are not exactly the "genetic alopecia" category the model predicted.

The evidence is small, early-phase and topical, so it does not yet show benefit.

**Other model predictions:** The other nine predictions are weak or unsupported:

| Rank | Predicted Indication | Score | Evidence |
|------|------|------|------|
| 1 | Ambras-type hypertrichosis universalis congenita | 98.4% | None. Sildenafil's hair-growth signal could worsen a hair-overgrowth disorder. |
| 2 | Malformation syndrome with odontal/periodontal component | 98.2% | Retrieved papers are generic periodontitis literature and do not involve sildenafil. They appear to be keyword noise. |
| 3 | Syndrome with Dandy-Walker malformation | 98.0% | None |
| 4 | Isolated genetic hair shaft abnormality | 97.9% | None |
| 5 | Hypertrichosis | 97.8% | One case report on glibenclamide in Cantú syndrome, not sildenafil |
| 6 | Homozygous familial hypercholesterolemia | 93.8% | None |
| 7 | Hypoalphalipoproteinemia | 90.1% | None |
| 8 | Familial isolated trichomegaly | 79.8% | None. Same worsening-direction concern as rank 1. |
| 10 | Obsolete patella aplasia, coxa vara, and tarsal synostosis | 70.0% | None. The disease entry is obsolete. |

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06527729](https://clinicaltrials.gov/study/NCT06527729) | Early Phase 1 | Completed | 28 | Randomized study of a sildenafil-loaded lipid nanocarrier in alopecia areata (an autoimmune alopecia). No results in the pack. |
| [NCT05369481](https://clinicaltrials.gov/study/NCT05369481) | Not applicable | Unknown | 50 | Topical sildenafil 2% vs topical minoxidil 5% in male androgenetic alopecia. No results in the pack. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30292404](https://pubmed.ncbi.nlm.nih.gov/30292404/) | 2018 | Preclinical (inferred from title; verify) | Biochem Biophys Res Commun | Examines the effect of sildenafil on human hair follicles, which was previously unknown. The supplied abstract is truncated and the results are not visible. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10805P | VIAGRA TABLET 50 mg | Film-coated tablet | Not stated in the record |
| SIN16024P | SILCAP® 50 CAPSULE 50MG | Capsule | Not stated in the record |
| SIN15090P | SILDENAFIL STADA® FILM COATED TABLET 100MG | Film-coated tablet | Not stated in the record |
| SIN14151P | Ernafil Tablet 100 mg | Film-coated tablet | Not stated in the record |
| SIN15367P | VIVIC TABLET 100MG | Film-coated tablet | Not stated in the record |

All listed products are oral. There are 20 registrations in total, and only 5 are shown.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Genetic alopecia has a plausible mechanism and two small early-phase topical trials, but no demonstrated benefit. The package-insert safety data needed for screening are missing. The highest-scoring predictions are unsupported and some may point in the wrong direction (worsening hypertrichosis).

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap)
- Mechanism of action data from DrugBank
- Results of NCT06527729 and NCT05369481, and a full read of PMID 30292404
- Confirmation of whether genetic alopecia is the right target (androgenetic vs alopecia areata) and whether a topical formulation is intended, since only oral forms are registered in Singapore
- Review of the direction of effect (benefit vs worsening) for the hypertrichosis-type predictions
- Removal of the keyword-matched periodontitis papers from the evidence set

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

