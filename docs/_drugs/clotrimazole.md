---
layout: default
title: Clotrimazole
parent: Medium Evidence (L3-L4)
nav_order: 270
evidence_level: L4
indication_count: 10
---

# Clotrimazole
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

# Clotrimazole: From Topical Antifungal Use to Acne

## One-Sentence Summary

Clotrimazole is an azole antifungal, sold in Singapore as vaginal tablets, creams and ear drops, and the registration records do not state its approved indications.
The TxGNN model predicts it may be effective for **acne**, but only **1 clinical trial** (suspended, testing a triple combination) and **no publications** support this direction.
The high model score is not backed by clinical data, so this prediction is not ready to act on.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (clotrimazole is used as a topical antifungal) |
| Predicted New Indication | Acne |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the drug record. Clotrimazole is an imidazole antifungal that inhibits fungal lanosterol 14-alpha-demethylase (CYP51). This depletes ergosterol and disrupts the fungal cell membrane. It is well established for Candida and dermatophyte infections. It may also have minor antibacterial or anti-inflammatory activity.

The link to acne is indirect. Acne vulgaris is driven by sebum, follicular blockage, *Cutibacterium acnes* and inflammation, not primarily by fungi. The only trial tests a fixed-dose combination of beclometasone, gentamicin and clotrimazole. The steroid and the antibiotic could account for any benefit, so clotrimazole's contribution cannot be separated out. The likely rationale is a mixed or secondary infection component, not acne pathogenesis.

The TxGNN score of 99.86% reflects graph-based association and should not be read as clinical proof.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Compared a beclometasone 0.025% + gentamicin 0.1% + clotrimazole 1% cream (Glenmark) in contaminated dermatosis with bilateral symmetrical lesions. No results reported. The trial's actual target population is unclear from the truncated title. |

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Shown below are 5 of the 20 registrations. The record does not give approved indication text for any of them.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03395P | CANDID-V6 Vaginal Tablet 100 mg | Tablet | Not stated in record |
| SIN16407P | COVEE Cream 1% w/w | Cream | Not stated in record |
| SIN06398P | Clotrimazole Cream 1% w/w | Cream | Not stated in record |
| SIN00175P | COTREN Vaginal Tablets 500 mg | Tablet | Not stated in record |
| SIN04573P | CANDID Ear Drops 1% | Solution | Not stated in record |

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting trial is a suspended, unreported study of a triple combination, so clotrimazole's own effect on acne cannot be assessed. The mechanism (antifungal CYP51 inhibition) does not address acne pathology, and no publications support the link.

Other predictions for this drug are much stronger and are likely established uses. Vulvovaginitis (L1, Proceed with Guardrails) and superficial mycosis (L2, Proceed with Guardrails) have completed Phase 3/4 trials and comparative studies. They should be checked against the labelled indications, since the registration records here give no indication text.

**To proceed, the following is needed:**
- Details of NCT01244256: target population, reason for suspension and any results
- Monotherapy clotrimazole data in acne, from clinical or mechanistic studies
- The Singapore package insert (HSA), for approved indications, warnings and contraindications
- Detailed mechanism of action data from DrugBank
- Confirmation of the drug's original indications, which are missing from the record
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

