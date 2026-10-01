---
layout: default
title: Celecoxib
parent: Low Evidence (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Arthritis and Pain Relief to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Celecoxib is a selective COX-2 inhibitor (NSAID) used for arthritis and pain.
The TxGNN model predicts it may be effective for **acromesomelic dysplasia, Hunter-Thompson type**, a rare genetic skeletal disorder.
This top-ranked prediction has **0 clinical trials** and **0 publications** supporting it, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records. Published reviews describe use in osteoarthritis, rheumatoid arthritis, ankylosing spondylitis and acute pain |
| Predicted New Indication | Acromesomelic dysplasia, Hunter-Thompson type |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Celecoxib is known as a selective COX-2 inhibitor. It reduces prostaglandin-driven inflammation and pain, and its efficacy in inflammatory arthritis is established.

Acromesomelic dysplasia, Hunter-Thompson type is a genetic skeletal dysplasia caused by the GDF5/CDMP1 pathway. It is not an inflammatory disease, and COX-2 inhibition does not act on this pathway. **No credible mechanistic link was found.** The high score most likely reflects proximity to other skeletal phenotypes in the knowledge graph, not a real pharmacological relationship.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16031P | COXIB-200 Capsules 200mg | Capsule | Not stated in record |
| SIN16253P | Synerrv Celecoxib Hard Capsules 100mg | Capsule | Not stated in record |
| SIN14560P | Celecoxib Sandoz Capsule 200mg | Capsule | Not stated in record |
| SIN15792P | Estacoxib Capsule 200mg | Capsule | Not stated in record |
| SIN11240P | Celebrex Capsules 100mg | Capsule | Not stated in record |

## Other Predicted Candidates Worth Noting

The rank-1 candidate has no support, but other predictions in this pack have more evidence:

| Rank | Predicted Indication | Score | Evidence Level | Decision | Comment |
|------|------|------|------|------|------|
| 9 | Inflammatory spondylopathy (axial spondyloarthritis / ankylosing spondylitis) | 99.80% | L1 | Proceed with Guardrails | Strongest candidate (details below) |
| 8 | RF-positive polyarticular juvenile idiopathic arthritis | 99.82% | L3 | Research Question | One registry paper on celecoxib safety in JIA. Efficacy in this subtype is not established |
| 3 | Rheumatoid vasculitis | 99.85% | L4 | Hold | Only a case report, which does not mention celecoxib. Standard care is immunosuppression |
| 5, 7 | Hypermobility of coccyx; rheumatoid nodulosis | 99.83%, 99.83% | L5 | Hold | Only generic symptom-relief plausibility |
| 1, 2, 4, 6, 10 | Genetic skeletal, connective tissue and immune disorders (including WHIM syndrome) | 99.80–99.88% | L5 | Hold | No credible mechanistic link |

**Rank 9 (axial spondyloarthritis) key evidence:**

| Trial | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | Celecoxib 200 mg QD or BID vs diclofenac over 12 weeks for symptomatic effect |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Celecoxib vs diclofenac SR in Chinese ankylosing spondylitis patients |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Two celecoxib doses vs diclofenac over 12 weeks |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Etanercept and celecoxib, alone or combined |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | Celecoxib added to golimumab vs golimumab alone, on spinal structural progression |

Supporting literature includes [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) (2025, meta-analysis, BMB Reports), which suggests celecoxib may inhibit bone progression in spondyloarthritis. It also includes [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) (2024, CONSUL trial analysis, Ann Rheum Dis), [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) (2017, RCT, imrecoxib vs celecoxib) and [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) (2025, cohort, cardiovascular and GI bleeding risk vs non-selective NSAIDs).

Only 10 of 19 trials and 10 of 20 papers were supplied for this candidate. Celecoxib may already be labeled for ankylosing spondylitis in some jurisdictions, so this may be an existing use rather than true repurposing. Verify against the Singapore label.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The rank-1 prediction (acromesomelic dysplasia, Hunter-Thompson type) has no trials, no literature and no plausible mechanism, and the high TxGNN score alone is not enough to justify further work.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications, approved indications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- For the rank-1 indication, any preclinical or mechanistic evidence linking COX-2 inhibition to the GDF5/CDMP1 pathway
- A separate evaluation of the axial spondyloarthritis candidate (rank 9), starting with a check of whether it is already a labeled use in Singapore
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

