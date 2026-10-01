---
layout: default
title: Vildagliptin
parent: Low Evidence (L5)
nav_order: 1057
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Vildagliptin is an oral DPP-4 inhibitor used to lower blood glucose in type 2 diabetes.
The TxGNN model ranks **focal stiff limb syndrome** as its top predicted new indication, but **no clinical trials and no publications** support it, so this is a graph-based prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (inferred from the drug class and trial records; the Singapore licence records carry no indication text) |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Vildagliptin is a DPP-4 inhibitor. It raises active GLP-1 and GIP and lowers glucagon during hyperglycaemia. Its efficacy in type 2 diabetes is established.

The review found no identifiable mechanistic link between DPP-4 inhibition and focal stiff limb syndrome. The score of 99.88% is identical to that of classic stiff person syndrome (rank 2 of the predictions). This suggests the two diseases share a neighbourhood in the knowledge graph rather than giving independent signals. A high score here should not be read as clinical plausibility.

The only speculative bridge is anti-GAD autoimmunity, which overlaps with autoimmune diabetes. That link is for the related stiff person syndrome, and no clinical data support it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN13407P | Galvus Tablet 50mg | Tablet |
| SIN13685P | Galvus Met Tablet 50mg/850mg | Film-coated tablet |
| SIN13684P | Galvus Met Tablet 50mg/1000mg | Film-coated tablet |
| SIN13952P | Galvus Met Tablet 50mg/500mg | Film-coated tablet |

All four products are oral. The manufacturers include Novartis sites. Approved indication text is not available in the record.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a knowledge-graph score. It has no trials, no literature and no plausible mechanism, and it shares its score with a neighbouring disease.

**To proceed, the following is needed:**
- The HSA package insert, to obtain warnings, contraindications and the approved indication text
- Mechanism of action data from DrugBank
- Any independent clinical or mechanistic evidence for stiff-limb or stiff-person syndromes

**Other candidates in this pack:**
- Ranks 2–9 are also L5 and Hold. Their mechanisms are implausible or speculative. The 5 papers retrieved for pancreatic agenesis are keyword matches on type 2 diabetes and DPP-4 pharmacology, not supporting evidence.
- **Type 1 diabetes mellitus (rank 10, score 99.37%)** is the only candidate with real evidence and was rated L2 and "Research Question". It should be evaluated as a separate report. The leading items are:
  - [NCT06021119](https://clinicaltrials.gov/study/NCT06021119): a completed Phase 3 trial (n=50) of vildagliptin add-on for iftar-related glycaemic excursions in T1D. It has a feasibility design with a surrogate endpoint, and randomisation and blinding are not confirmed.
  - [PMID 38057844](https://pubmed.ncbi.nlm.nih.gov/38057844/): the randomised trial publication matching the Phase 3 trial above.
  - [PMID 33124663](https://pubmed.ncbi.nlm.nih.gov/33124663/): a double-blind RCT of rapamycin plus vildagliptin in long-standing T1D. Its results are not in the supplied data and should be reviewed.
  - Most of the other registered trials are type 2 diabetes studies matched by drug name and are not T1D evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

