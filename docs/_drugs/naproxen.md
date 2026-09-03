---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 691
evidence_level: L5
indication_count: 10
---

# Naproxen
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

# Naproxen: From Pain and Inflammation to Inflammatory Spondylopathy

## One-Sentence Summary

Naproxen is a long-established non-selective COX-1/COX-2 inhibitor NSAID used for pain and inflammation in rheumatic conditions such as osteoarthritis and rheumatoid arthritis. Among 10 TxGNN-predicted indications for this drug, **Inflammatory Spondylopathy** (including ankylosing spondylitis / axial spondyloarthritis) stands out as the only candidate backed by substantial real-world evidence — **9 clinical trials** and **19 publications** — while the other 9 candidates (e.g. brachydactyly-syndactyly syndrome, Kummell disease) are pure model-similarity artifacts with no supporting data and are flagged Hold. This report focuses on the evidence-supported candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Singapore (no HSA license on file); as an NSAID, naproxen is established for pain and inflammation in rheumatic diseases (osteoarthritis, rheumatoid arthritis) |
| Predicted New Indication | Inflammatory Spondylopathy (incl. Ankylosing Spondylitis / Axial Spondyloarthritis) |
| TxGNN Prediction Score | 98.58% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Naproxen is a non-selective COX-1/COX-2 inhibitor that suppresses prostaglandin synthesis, giving it analgesic, antipyretic, and anti-inflammatory activity. This mechanism is directly applicable to inflammatory spondylopathy: NSAIDs as a class are the established first-line pharmacologic treatment for axial spondyloarthritis and ankylosing spondylitis, used to control axial pain, stiffness, and inflammation.

Unlike the other 9 TxGNN-predicted indications for naproxen in this evidence pack — which are rare structural/genetic skeletal syndromes (e.g., brachydactyly-syndactyly syndrome, acromesomelic dysplasia, Kummell disease) with no inflammatory component and therefore no plausible mechanistic link to a COX inhibitor — inflammatory spondylopathy is mechanistically coherent and already reflected in real-world clinical practice. In this sense, the "repurposing" signal here is less a novel discovery and more a confirmation that TxGNN's embedding correctly recovers an already-established use, which strengthens rather than weakens its credibility as a positive control.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01298531](https://clinicaltrials.gov/study/NCT01298531) | Phase 4 | Completed | 90 | Double-blind, placebo-controlled study of the NSAID-sparing effect of etanercept vs placebo in axial spondyloarthritis; directly evaluates NSAID (naproxen-class) treatment in this population |
| [NCT01511926](https://clinicaltrials.gov/study/NCT01511926) | N/A | Completed | 2000 | Retrospective study of Vimovo™ (naproxen + esomeprazole) prescribing patterns in OA/RA/AS patients at GI risk |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials comparing COX-2 selective vs non-selective NSAIDs for individualized anti-inflammatory therapy in axial spondyloarthritis |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | TNF inhibitor dose-adjustment trial in stable ankylosing spondylitis (background/comparator context) |
| [NCT02355236](https://clinicaltrials.gov/study/NCT02355236) | Phase 4 | Unknown | 106 | Naxozol (naproxen/esomeprazole) vs celecoxib for GI protection and pain relief in OA/RA/AS |
| [NCT01208207](https://clinicaltrials.gov/study/NCT01208207) | Phase 3 | Completed | 1015 | Etoricoxib vs naproxen for spinal pain intensity in ankylosing spondylitis over 6 weeks |
| [NCT00367211](https://clinicaltrials.gov/study/NCT00367211) | Phase 3 | Completed | 400 | Gastric ulcer incidence with naproxen vs comparator in NSAID-associated ulcer risk population |
| [NCT02293681](https://clinicaltrials.gov/study/NCT02293681) | N/A | Terminated | 76 | Infliximab vs conventional therapy (incl. NSAIDs) in AS patients with hip involvement |
| [NCT00844805](https://clinicaltrials.gov/study/NCT00844805) | Phase 3 | Completed | 158 | Infliximab + naproxen vs placebo + naproxen in early active axial spondyloarthritis, ASAS partial remission endpoint |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368727](https://pubmed.ncbi.nlm.nih.gov/24368727/) | 2014 | RCT | Journal of Thrombosis and Thrombolysis | Safety/tolerability of naproxen/esomeprazole with concomitant low-dose aspirin, pooled from 5 Phase III studies |
| [27015283](https://pubmed.ncbi.nlm.nih.gov/27015283/) | 2016 | Cohort | Arthritis & Rheumatology | Infliximab + naproxen vs naproxen alone: course of inflammatory/fatty MRI lesions in early axial spondyloarthritis |
| [39315555](https://pubmed.ncbi.nlm.nih.gov/39315555/) | 2024 | Cohort | Reumatismo | Liver and kidney function in ankylosing spondylitis patients on long-term NSAID therapy |
| [40500963](https://pubmed.ncbi.nlm.nih.gov/40500963/) | 2025 | Review | Pain Management | Narrative review comparing radiofrequency ablation and naproxen in axial spondyloarthritis management |
| [2202585](https://pubmed.ncbi.nlm.nih.gov/2202585/) | 1990 | Review | Drugs | Reappraisal of naproxen pharmacology and therapeutic use in rheumatic diseases and pain states |
| [387372](https://pubmed.ncbi.nlm.nih.gov/387372/) | 1979 | Review | Drugs | Comprehensive review of naproxen's pharmacological properties and use in rheumatic disease |
| [21329403](https://pubmed.ncbi.nlm.nih.gov/21329403/) | 2011 | Review | Drugs & Aging | Naproxen/esomeprazole fixed-dose combination for arthritic symptoms and gastric ulcer risk reduction |
| [1173774](https://pubmed.ncbi.nlm.nih.gov/1173774/) | 1975 | Review | Arzneimittel-Forschung | Foundational chemistry and pharmacology of naproxen, developed for rheumatoid arthritis, OA, gout, and ankylosing spondylitis |
| [22258995](https://pubmed.ncbi.nlm.nih.gov/22258995/) | 2012 | Review | Cochrane Database of Systematic Reviews | Pain management for inflammatory arthritis (incl. AS) with GI/liver comorbidity, covering NSAID use |
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Review | BMB Reports | Compares NSAIDs (selective vs non-selective COX inhibition) for bone progression inhibition in spondyloarthritis |

---

## Singapore Market Information

Naproxen currently has **no HSA registration on file** (Market Status: Not Marketed, 0 licenses). No product-level authorization or approved indication text is available for the Singapore market at this time.

---

## Safety Considerations

Formal safety data for this evidence pack could not be retrieved: key warnings, contraindications, and drug-drug interaction (DDI) records are all unavailable (DDI query returned no results). This corresponds to a flagged **Blocking** data gap (DG001 – HSA/TFDA label warnings and contraindications), which currently prevents a formal safety pre-assessment. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Inflammatory spondylopathy is the only one of naproxen's 10 TxGNN-predicted indications supported by substantive evidence (L1: multiple completed Phase 3/4 trials and naproxen-specific reviews), and it aligns with NSAIDs' already-established first-line role in axial spondyloarthritis/ankylosing spondylitis — this is a mechanistically sound, low-novelty-risk repurposing signal rather than a speculative one.

**To proceed, the following is needed:**
- HSA/TFDA package insert data — key warnings and contraindications (blocking gap, DG001)
- Confirmed mechanism of action detail from DrugBank (DG002)
- A Singapore market-entry or registration pathway, since naproxen currently has zero HSA licenses on file
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

