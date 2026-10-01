---
layout: default
title: Indomethacin
parent: Low Evidence (L5)
nav_order: 526
evidence_level: L5
indication_count: 10
---

# Indomethacin
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

# Indomethacin: From an NSAID (Original Indication Not Recorded) to Brachydactyly-Syndactyly Syndrome

## One-Sentence Summary

Indomethacin is a marketed non-selective COX inhibitor (an NSAID), but the source data does not record its approved indications.
The TxGNN model's top prediction is **brachydactyly-syndactyly syndrome**, a congenital limb malformation, with a very high score of 99.97%.
This prediction has **0 clinical trials** and **0 publications** behind it, so it is a graph-based signal only. Among the other predictions, **juvenile idiopathic arthritis (JIA)** is the only one with meaningful literature support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the licence records contain no indication text) |
| Predicted New Indication | Brachydactyly-syndactyly syndrome |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Indomethacin is known to be a non-selective COX-1/COX-2 inhibitor. It reduces prostaglandin-mediated inflammation and pain.

For brachydactyly-syndactyly syndrome, the review found **no plausible mechanistic link**. It is a congenital limb malformation, and COX inhibition has no known relevance to its development. The high TxGNN score reflects graph proximity only. It is not supported by any trial or publication, so it should be treated as a model artefact rather than a lead.

The same is true of most other top-ranked predictions: colobomatous microphthalmia-rhizomelic dysplasia syndrome, Hunter-Thompson acromesomelic dysplasia, WHIM syndrome, brachyolmia and brachyolmia-amelogenesis imperfecta syndrome. All are rare genetic disorders with no COX-dependent mechanism.

The mechanistically plausible candidates are the inflammatory arthritis predictions. Juvenile idiopathic arthritis is the strongest of these (rank 8, score 99.84%, evidence level L3). NSAIDs are a recognised symptomatic therapy in JIA. Note that this would be established symptomatic care, not a novel disease-modifying repurposing claim.

## Clinical Trial Evidence

Currently no related clinical trials registered for brachydactyly-syndactyly syndrome. No trials were retrieved for any of the other nine predicted indications either.

## Literature Evidence

Currently no related literature available for brachydactyly-syndactyly syndrome.

The only indication with substantial literature is the rank 8 prediction, **juvenile idiopathic arthritis**. The table below lists its most relevant publications. Only titles and abstract excerpts were reviewed, and none is a phase-labelled trial.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [362571](https://pubmed.ncbi.nlm.nih.gov/362571/) | 1978 | RCT | S Afr Med J | Double-blind crossover of ketoprofen vs indomethacin in 30 children with juvenile chronic arthritis. Both were safe and effective, and indomethacin was the preferred drug. |
| [1379157](https://pubmed.ncbi.nlm.nih.gov/1379157/) | 1992 | Review | Drugs | Pharmacological management of juvenile rheumatoid arthritis. Lists indomethacin among the NSAIDs used. |
| [28418334](https://pubmed.ncbi.nlm.nih.gov/28418334/) | 2017 | Review | Balkan Med J | General overview of JIA subtypes, clinical features and treatment. |
| [22573189](https://pubmed.ncbi.nlm.nih.gov/22573189/) | 2012 | Review | Swiss Med Wkly | Review of systemic-onset JIA (Still's disease). |
| [8422565](https://pubmed.ncbi.nlm.nih.gov/8422565/) | 1993 | Not classified | Br J Rheumatol | NSAIDs in paediatric rheumatic disease. Salicylates and indomethacin are used for systemic JCA fever. For joint symptoms they are no more effective than other NSAIDs, but more toxic. |
| [1884567](https://pubmed.ncbi.nlm.nih.gov/1884567/) | 1991 | Not classified | Clin Pharmacokinet | Pharmacokinetics of drugs used in juvenile arthritis. |
| [5632159](https://pubmed.ncbi.nlm.nih.gov/5632159/) | 1967 | Not classified | Arzneimittel-Forschung | Long-term indomethacin therapy in juvenile rheumatoid arthritis and Still's disease (no abstract available). |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05375P | INDO CAPSULES 25 mg | Capsule | Not listed in the retrieved record |
| SIN08624P | INDOMEN CAPSULE 25 mg | Capsule | Not listed in the retrieved record |
| SIN09699P | HD-METHACIN CAPSULE 25 mg | Capsule | Not listed in the retrieved record |

All three products are oral capsules.

## Safety Considerations

Please refer to the package insert for safety information. No drug-interaction records were found in the data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, brachydactyly-syndactyly syndrome, rests on a model score alone. It has no trials, no literature and no plausible mechanism. Indomethacin's use in JIA is real but is established symptomatic NSAID care. It is not a new repurposing opportunity and is supported only by dated, mostly comparative literature.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications and approved indications). This is a blocking gap for safety screening.
- Mechanism of action data from DrugBank.
- Full-text review of the JIA literature, especially the 1978 RCT, to confirm efficacy and safety in children.
- If JIA is pursued, a check of whether it already falls within the approved Singapore indications, to avoid counting existing use as repurposing.
- Route compatibility and similarity-to-original assessments, which are currently pending.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

