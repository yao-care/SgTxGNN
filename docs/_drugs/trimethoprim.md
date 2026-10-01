---
layout: default
title: Trimethoprim
parent: Low Evidence (L5)
nav_order: 1019
evidence_level: L5
indication_count: 10
---

# Trimethoprim
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

# Trimethoprim: From Antibacterial Use to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Trimethoprim is an antibacterial that inhibits bacterial dihydrofolate reductase (DHFR). It is marketed in Singapore mainly as a component of co-trimoxazole products.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (antibacterial agent) |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 12 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, trimethoprim is an antibacterial DHFR inhibitor. It is used in combination products such as co-trimoxazole and in topical polymyxin B/trimethoprim eye preparations.

The link to this indication is weak. Punctate epithelial keratoconjunctivitis is frequently viral (for example adenoviral) or non-infectious, so an antibacterial mechanism has no clear target. The high score appears to come from the knowledge-graph association between the drug and eye-surface conditions in general. It does not show that trimethoprim treats this disease.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

The record lists 12 authorizations. The five main ones are below. The records give no approved indication text.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN00508P | APO-SULFATRIM PEDIATRIC TABLET | Tablet |
| SIN00435P | APO-SULFATRIM TABLET | Tablet |
| SIN00526P | B.S. SUSPENSION | Suspension |
| SIN02183P | DBL SULFAMETHOXAZOLE 400MG AND TRIMETHOPRIM 80MG CONCENTRATE INJECTION BP | Injection |
| SIN00583P | CO-TRIMEXAZOLE SUSPENSION | Suspension |

The available forms are oral tablets, suspensions and injection. No ophthalmic product appears in the records provided.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction has only a model score, with no trials, no literature and no clear mechanistic link. The disease is often viral or non-infectious, which an antibacterial would not address.

**Other indications in the same prediction list:**
- **Conjunctivitis (rank 2)** has the strongest support in this pack. It is rated L2 and Proceed with Guardrails.
  - Evidence: a completed Phase 4 trial of polymyxin B/trimethoprim versus moxifloxacin ([NCT00581542](https://clinicaltrials.gov/study/NCT00581542), n=124) and a matching multicenter publication ([PMID 19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/)).
  - Caveats: the trial used a combination product, not trimethoprim alone. This may be an existing labeled use rather than true repurposing.
  - Guardrails: limit to bacterial etiology and consider local resistance.
- **Otitis externa (rank 8)** is rated L3 and treated as a research question only. The only direct human study is a 1993 oral cotrimoxazole trial, and Pseudomonas is often intrinsically resistant to trimethoprim.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap).
- Mechanism of action data from DrugBank.
- Original indication from the HSA licences, to judge whether any candidate is truly new.
- Route compatibility assessment. The Singapore licences list only oral and injectable forms, and ocular use would need a topical formulation.
- Direct human evidence for punctate epithelial keratoconjunctivitis. Without it, this indication should not advance.
- If conjunctivitis is pursued, a label check and the resistance guardrails above.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

