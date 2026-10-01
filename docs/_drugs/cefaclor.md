---
layout: default
title: Cefaclor
parent: Low Evidence (L5)
nav_order: 217
evidence_level: L5
indication_count: 10
---

# Cefaclor
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

# Cefaclor: From Bacterial Infections to Hyperamylasemia

## One-Sentence Summary

Cefaclor is an oral second-generation cephalosporin antibiotic. Its approved indication text is not stated in the Singapore registration records, so "bacterial infections" is the general class use.
The TxGNN model ranks **hyperamylasemia** as its top prediction, but there are **0 clinical trials** and **0 publications** supporting it, and no plausible mechanism.
This looks like a graph artifact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records (cefaclor is a cephalosporin antibacterial) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 97.70% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Cefaclor is a beta-lactam antibiotic that inhibits bacterial penicillin-binding proteins and cell-wall synthesis.

That mechanism has no known effect on amylase metabolism. Hyperamylasemia is a laboratory finding with varied causes, not a bacterial disease, so an antibacterial has no clear therapeutic role. The high TxGNN score is most likely a graph artifact.

The same pattern applies to most of the other top-ranked predictions. Several are hematologic or immunoglobulin-related disorders with no mechanistic link (see "Other Predicted Indications" below).

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications Worth Noting

Among the top 10 predictions, only one has any supporting evidence.

**Gonococcal urethritis (rank 3, score 97.48%, Evidence Level L3, "Research Question")**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [121455](https://pubmed.ncbi.nlm.nih.gov/121455/) | 1979 | Clinical study | Postgrad Med J | Controlled trial in 40 men with uncomplicated gonococcal urethritis, using a 1 g cefaclor loading dose |
| [116373](https://pubmed.ncbi.nlm.nih.gov/116373/) | 1979 | Randomized trial | Sex Transm Dis | Cefaclor 2, 3 or 4 g daily for 3 days, with or without probenecid, in men with culture-confirmed infection |
| [6225482](https://pubmed.ncbi.nlm.nih.gov/6225482/) | 1983 | Comparative study | Br J Vener Dis | 400 men randomized to four regimens. Cure rate was 98.9% with spectinomycin, 95.8% with cefaclor 3 g plus probenecid, and 89.6% with cefaclor 3 g alone |
| [6400040](https://pubmed.ncbi.nlm.nih.gov/6400040/) | 1984 | Clinical study | Med J Malaysia | Single-dose oral cefaclor in men with uncomplicated gonococcal urethritis |
| [9582471](https://pubmed.ncbi.nlm.nih.gov/9582471/) | 1997 | Clinical study | Genitourin Med | Reassessed in vivo and in vitro efficacy of cefaclor for uncomplicated gonococcal infection in the developing world |

The studies are old and no registered trials exist. Current gonorrhea guidelines favor injectable ceftriaxone because of rising resistance to oral cephalosporins. This is an antibacterial use rather than true repurposing.

**Other predictions with no evidence (all L5, Hold):**
- **Mechanistically contradicted:** Ureaplasma urethritis. Ureaplasma lacks a cell wall, so beta-lactams are intrinsically ineffective.
- **Partial plausibility only:** uterine inflammatory disease (only if bacterial, and cefaclor lacks reliable anaerobic and chlamydial coverage) and xanthogranulomatous pyelonephritis (mainly surgical, antibiotics only adjunctive).
- **No mechanistic link:**
  - polyclonal hyperviscosity syndrome
  - congenital analbuminemia
  - premalignant hematological system disease
  - monoclonal gammopathy
- **Opposite safety signal:** blood group incompatibility. Cephalosporins can cause drug-induced immune hemolytic anemia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09294P | CLEANCEF CAPSULE 250 mg | Capsule | Not stated in the registration record |
| SIN11733P | SOFICLOR FOR ORAL SUSPENSION 125 mg/5 ml | Granule, for suspension | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

- **Drug Interactions**: No interaction records were found in the queried source.
- **Hemolysis signal**: Cephalosporins are known to cause drug-induced immune hemolytic anemia. This matters for any blood-related indication.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hyperamylasemia, has no trials, no literature and no plausible mechanism, so the high TxGNN score is not credible. The only indication with any evidence is gonococcal urethritis. That is an old, antibacterial-type use with limited relevance today.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indications). This blocks safety screening.
- Mechanism of action data from DrugBank.
- For gonococcal urethritis only: current local susceptibility data and comparison against present guideline regimens.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

