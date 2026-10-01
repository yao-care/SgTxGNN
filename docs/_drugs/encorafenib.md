---
layout: default
title: Encorafenib
parent: Low Evidence (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Encorafenib
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

# Encorafenib: From BRAF-Mutant Cancers to Choroideremia

## One-Sentence Summary

Encorafenib is an oral BRAF V600 kinase inhibitor used in BRAF-mutant cancers such as melanoma and colorectal cancer, and it is marketed in Singapore.
The TxGNN model ranks **choroideremia**, an inherited retinal degeneration, as its top predicted new indication.
There are **no clinical trials and no publications** supporting this prediction, so it should be treated as an unsupported model output.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration text. The trial record points to BRAF V600-mutant melanoma and colorectal cancer. |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 97.10% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the dossier. Based on the known drug class, encorafenib inhibits BRAF V600 kinase. It is used where the MAPK pathway is over-activated by a BRAF mutation, as in BRAF-mutant melanoma.

Choroideremia is different. It is an X-linked retinal degeneration caused by loss of CHM/REP1 function and is not driven by BRAF/MAPK hyperactivation. The high score (0.971) most likely reflects graph-topology artifacts, such as shared ocular or pigmentation-related neighbours in the knowledge graph.

Retinal toxicity is a known class concern for MAPK-pathway inhibitors. Any use in an already degenerating retina would therefore need a strong safety rationale, which is currently absent.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16824P | BRAFTOVI HARD CAPSULE 75MG | Capsule |
| SIN16825P | BRAFTOVI HARD CAPSULE 50MG | Capsule |

The approved-indication text is blank in both registration records. Both products are oral capsules.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (BRAF kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Ophthalmic examination (class concern for MAPK inhibitors) and dermatologic surveillance (secondary skin neoplasms reported in case reports). Please refer to the package insert for laboratory monitoring. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Ocular toxicity**: Retinal toxicity is a recognized class concern for MAPK-pathway inhibitors. This is especially relevant when the proposed indication is itself a retinal degeneration.
- **Secondary skin neoplasms**: Case reports in the wider evidence set describe new melanomas or nevi appearing during BRAF inhibitor therapy, including PMID 40878071 (encorafenib plus cetuximab). These reports come from other indications, not from choroideremia.

Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Choroideremia has no trials, no literature and no plausible BRAF/MAPK mechanism, so the 97.10% score is likely a graph artifact. The known retinal class toxicity adds a specific safety concern.

Other predictions carry more evidence, but they are extensions of the melanoma use rather than true repurposing. Non-cutaneous melanoma (score 96.55%) and acral lentiginous melanoma (score 95.59%) each have Phase 2 trials and are rated L2, "Research Question". Their trials have no results available, and BRAF V600 mutations are uncommon in mucosal, uveal and acral disease. If a candidate is taken forward, these would be better choices than choroideremia.

**To proceed, the following is needed:**
- The HSA package insert, to establish warnings, contraindications and the registered indications
- Detailed mechanism-of-action data (MOA)
- A biological rationale and retinal safety assessment before any retinal-disease use is considered
- For the melanoma subtypes: registry verification of trial populations and BRAF V600 status, and any available results

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

