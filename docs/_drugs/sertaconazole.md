---
layout: default
title: Sertaconazole
parent: Medium Evidence (L3-L4)
nav_order: 899
evidence_level: L4
indication_count: 10
---

# Sertaconazole
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

# Sertaconazole: From Topical Azole Antifungal to Dermatophytosis of the Groin and Perianal Area

## One-Sentence Summary

Sertaconazole is a topical imidazole antifungal, marketed in Singapore as a 2% cream and a 300 mg vaginal suppository. The TxGNN model predicts it may be effective for **dermatophytosis of the groin and perianal area**, but this prediction currently has **0 clinical trials** and **0 publications** registered for this exact indication. Trials in the neighbouring indication, tinea corporis, exist (see Literature Evidence).

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Dermatophytosis of groin and perianal area |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

The Singapore registration records contain no approved indication text, and the pack lists no original indications, so the original indication row is omitted.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the dataset. Based on general pharmacology and published reviews, sertaconazole is an imidazole antifungal that inhibits ergosterol synthesis (lanosterol 14-alpha-demethylase). At higher concentrations it may also disrupt fungal membranes through its benzothiophene ring. Ergosterol is essential to fungal cell membranes, so this mechanism should apply to dermatophytes at any skin site.

The groin and perianal area is a skin site for dermatophyte infection (tinea cruris and related forms). A 2009 review (PMID 19275277) reports sertaconazole is indicated in the EU for dermatophytosis, including tinea cruris. This suggests the prediction may reflect an existing use rather than true repurposing, though the missing original-indication data prevents confirming this.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for this specific indication.

For context, the adjacent indication **tinea corporis** has randomized comparative trials of sertaconazole. Two of them also enrolled patients with tinea cruris:
- [24249898](https://pubmed.ncbi.nlm.nih.gov/24249898/): vs terbinafine 1% cream in tinea corporis and tinea cruris (2013).
- [28066103](https://pubmed.ncbi.nlm.nih.gov/28066103/): vs terbinafine in localized dermatophytosis (tinea corporis or cruris) (2016).

These are indirect evidence. They were not retrieved for the groin and perianal indication, and no trial phase is labelled in the data.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10933P | ZALAIN CREAM 2% | Cream (topical) | Not stated in registration data |
| SIN11905P | ZALAIN VAGINAL SUPPOSITORY 300 mg | Suppository | Not stated in registration data |

Only the cream is a skin formulation. The vaginal suppository is not relevant to groin or perianal skin infection.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This indication rests on the model prediction and general pharmacology alone, with no trials or literature retrieved (L4). Safety data, including the package insert, is missing and is flagged as a blocking gap. The adjacent tinea corporis indication has stronger evidence (L1) and is a better candidate to advance first.

**To proceed, the following is needed:**
- HSA package insert (warnings and contraindications), which blocks safety screening
- The approved indication text for the Singapore cream (SIN10933P), to confirm whether tinea cruris is already on-label
- Mechanism-of-action data from DrugBank
- A targeted search for tinea cruris and perianal dermatophytosis trials
- Route compatibility review (topical cream use on groin and perianal skin)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

