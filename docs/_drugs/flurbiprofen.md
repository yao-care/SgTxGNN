---
layout: default
title: Flurbiprofen
parent: Low Evidence (L5)
nav_order: 441
evidence_level: L5
indication_count: 10
---

# Flurbiprofen
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

# Flurbiprofen: From NSAID Pain Relief to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Flurbiprofen is a non-steroidal anti-inflammatory drug (NSAID). In Singapore it is registered as a throat lozenge, a throat spray and a pain-relief patch.
The TxGNN model ranks **acromesomelic dysplasia, Hunter-Thompson type** first, but **no clinical trials and no publications** support this prediction, and it is most likely a knowledge-graph artifact.
Among the top 10 predictions, only **ankylosing spondylitis** (rank 8) has real evidence, with **about 20 publications**, including several randomized double-blind trials.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (registered products are a sore-throat lozenge, a throat spray and a pain patch) |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From general pharmacology, flurbiprofen is a non-selective COX-1/COX-2 inhibitor that reduces prostaglandin-mediated pain and inflammation.

For the top-ranked prediction, the mechanistic case is weak. Acromesomelic dysplasia, Hunter-Thompson type, is a genetic skeletal dysplasia caused by defects in the CDMP1/GDF5 pathway. COX inhibition does not correct that defect, and the high score most likely reflects shared skeletal-phenotype nodes in the knowledge graph rather than a real pharmacological link.

The picture is different for ankylosing spondylitis. This condition responds to NSAIDs as a class, so flurbiprofen's use there is class-consistent symptom relief rather than a novel mechanism. It is the only predicted indication in this pack with a credible evidence base.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked prediction, or for any of the 10 predicted indications.

## Literature Evidence

Currently no related literature available for the top-ranked prediction.

Literature exists only for the rank 8 prediction, **ankylosing spondylitis**, so it is shown below as the strongest lead:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3963018](https://pubmed.ncbi.nlm.nih.gov/3963018/) | 1986 | RCT (double-blind) | Am J Med | 57 patients, 26 weeks: flurbiprofen 200 mg/day controlled pain and symptoms, comparable to indomethacin |
| [3963017](https://pubmed.ncbi.nlm.nih.gov/3963017/) | 1986 | RCT (double-blind) | Am J Med | 90 patients, 26 weeks: flurbiprofen 200 mg/day as effective as phenylbutazone 300 mg/day |
| [71969](https://pubmed.ncbi.nlm.nih.gov/71969/) | 1977 | RCT (double-blind) | Curr Med Res Opin | 26 patients, 6 weeks: flurbiprofen and indomethacin equally effective for pain and tenderness |
| [329422](https://pubmed.ncbi.nlm.nih.gov/329422/) | 1977 | RCT (double-blind) | South Med J | Same design and 26-patient cohort as PMID 71969, apparently a duplicate report |
| [324773](https://pubmed.ncbi.nlm.nih.gov/324773/) | 1977 | RCT (double-blind) | Eur J Clin Pharmacol | 27 patients, 6 weeks: flurbiprofen and phenylbutazone equally effective; the patient/investigator preference for phenylbutazone was not significant |
| [4611579](https://pubmed.ncbi.nlm.nih.gov/4611579/) | 1974 | Double-blind crossover | Br Med J | 35 patients, 4 weeks: flurbiprofen 150 mg/day was well tolerated, with efficacy approaching phenylbutazone |
| [7003449](https://pubmed.ncbi.nlm.nih.gov/7003449/) | 1980 | Double-blind crossover | N Z Med J | 30 patients: flurbiprofen 200 mg/day and naproxen 750 mg/day both effective; side effects were more frequent with flurbiprofen |
| [4595274](https://pubmed.ncbi.nlm.nih.gov/4595274/) | 1974 | Double-blind crossover | Ann Rheum Dis | Flurbiprofen compared with indomethacin and placebo (no abstract available) |
| [3963024](https://pubmed.ncbi.nlm.nih.gov/3963024/) | 1986 | Pooled safety analysis | Am J Med | 1,677 patients across nine Phase III trials (ankylosing spondylitis, osteoarthritis, rheumatoid arthritis): no clinically significant liver or kidney effects reported in the abstract |
| [391529](https://pubmed.ncbi.nlm.nih.gov/391529/) | 1979 | Review | Drugs | Flurbiprofen is comparable to other NSAIDs in rheumatic diseases, including ankylosing spondylitis |

All of these studies are small and 27 to 50 years old. They compare flurbiprofen with older NSAIDs, not with modern standards of care or biologics.

## Other Predicted Indications (Ranks 2-10)

| Rank | Predicted Indication | Score | Evidence Level | Decision | Note |
|------|------|------|------|------|------|
| 2 | Brachydactyly-syndactyly syndrome | 99.99% | L5 | Hold | Congenital malformation, no mechanistic rationale |
| 3 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.99% | L5 | Hold | Ultra-rare developmental syndrome, no plausible link |
| 4 | Brachyolmia-amelogenesis imperfecta syndrome | 99.99% | L5 | Hold | Only symptomatic pain relief is conceivable |
| 5 | Myosclerosis | 99.98% | L5 | Hold | Speculative link, no evidence |
| 6 | Brachyolmia | 99.98% | L5 | Hold | Genetic spinal dysplasia, no evidence |
| 7 | Spondyloarthropathy, susceptibility to | 99.97% | L5 | Hold | Genetic susceptibility entity, not a treatable condition |
| 8 | **Ankylosing spondylitis** | 99.97% | **L2** | **Proceed with Guardrails** | Multiple comparative trials of flurbiprofen |
| 9 | Pseudoachondroplasia | 99.96% | L5 | Hold | At most symptomatic joint-pain relief |
| 10 | Hypermobility of coccyx | 99.95% | L5 | Hold | Analgesic rationale plausible, no evidence |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14364P | Strepsils MaxPro Honey and Lemon lozenges 8.75mg | Lozenge | Not provided in registry data |
| SIN15370P | Strepsils Max Pro Direct Spray 8.75mg per dose | Spray | Not provided in registry data |
| SIN12090P | Acustop Cataplasma Plaster 40 mg/sheet | Patch | Not provided in registry data |

All three local products are topical or local-use forms. The ankylosing spondylitis trials used oral flurbiprofen at 100-200 mg/day, so none of the locally registered products matches the studied route. Route compatibility is still pending.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, acromesomelic dysplasia, Hunter-Thompson type, has no clinical or literature support and no plausible mechanism, so it should not be pursued. The only credible lead in the top 10 is ankylosing spondylitis. It is a class-consistent NSAID use supported by several older comparative trials (evidence level L2), but the safety data and registered forms are not yet sufficient to move it forward.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For ankylosing spondylitis: a check of the current guidelines and a route/dose feasibility review, since the local products are not oral forms
- Removal or deprioritization of the rank 1-7 and rank 9 predictions, which look like knowledge-graph artifacts

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

