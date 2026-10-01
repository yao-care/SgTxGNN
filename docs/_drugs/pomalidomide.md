---
layout: default
title: Pomalidomide
parent: Low Evidence (L5)
nav_order: 798
evidence_level: L5
indication_count: 10
---

# Pomalidomide
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

# Pomalidomide: From Relapsed/Refractory Multiple Myeloma to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Pomalidomide is an oral immunomodulatory drug already marketed in Singapore for relapsed/refractory multiple myeloma.
The TxGNN model predicts it may also be useful for **indolent plasma cell myeloma** (the smoldering subtype), with **1 clinical trial** and **2 publications** currently supporting this direction.
The evidence covers myeloma in general, not the indolent subtype specifically, so this is best viewed as a subtype extension rather than true repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relapsed/refractory multiple myeloma (the HSA licence records contain no indication text) |
| Predicted New Indication | Indolent plasma cell myeloma |
| TxGNN Prediction Score | 94.0% |
| Evidence Level | L2 (one completed Phase 2 trial, but single-arm and not randomized) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Pomalidomide binds cereblon, a protein that tags other proteins for degradation. This leads to degradation of the transcription factors Ikaros and Aiolos. The result is a direct anti-myeloma effect plus immune stimulation. The drug is already used in relapsed/refractory multiple myeloma, so its activity against malignant plasma cells is established.

Indolent (smoldering) myeloma is an earlier stage of the same plasma cell disease. The same mechanism could apply, so a high model score is plausible. However, the available trial enrolled relapsed/refractory patients, and it is unclear whether the findings carry over to an early-stage, asymptomatic population. That population has a different risk-benefit balance, since it is typically observed rather than treated.

Detailed mechanism data were not retrieved from DrugBank. The mechanism described here comes from the evidence analysis.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02046915](https://clinicaltrials.gov/study/NCT02046915) | Phase 2 | Completed | 60 | Open-label, single-arm multicenter study of pomalidomide plus dexamethasone with response-adapted cyclophosphamide in relapsed myeloma. It aimed to improve efficacy while limiting myelosuppression. Relevance grade B: it supports the drug–myeloma link, not necessarily the indolent subtype. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21181954](https://pubmed.ncbi.nlm.nih.gov/21181954/) | 2011 | Review | American Journal of Hematology | Overview of multiple myeloma diagnosis, risk stratification and management. Myeloma accounts for about 10% of haematologic malignancies. |
| [22180161](https://pubmed.ncbi.nlm.nih.gov/22180161/) | 2012 | Review | American Journal of Hematology | 2012 update of the same myeloma management review. |

Both are general myeloma reviews and do not test pomalidomide in the indolent subtype.

## Singapore Market Information

Five of the eight registrations are shown. The licence records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN14713P | POMALYST CAPSULE 1MG | Capsule | Celgene International Sarl |
| SIN14714P | POMALYST CAPSULE 2MG | Capsule | Celgene International Sarl |
| SIN16983P | POMAGEN CAPSULES 1MG | Capsule | Lotus Pharmaceutical Co., Ltd. Nantou Plant |
| SIN16984P | POMAGEN CAPSULES 2MG | Capsule | Lotus Pharmaceutical Co., Ltd. Nantou Plant |
| SIN16985P | POMAGEN CAPSULES 3MG | Capsule | Lotus Pharmaceutical Co., Ltd. Nantou Plant |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunomodulatory agent (thalidomide analogue), not a conventional cytotoxic |
| Myelosuppression Risk | Relevant: the trial summary highlights myelosuppression as a key toxicity concern in combination regimens |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential; other items per the package insert |
| Handling Protection | As a thalidomide analogue, follow the package insert's pregnancy-prevention and handling requirements |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial and a well-understood mechanism support activity in myeloma, and the drug is already marketed in Singapore. However, the trial was single-arm, it enrolled relapsed/refractory patients rather than indolent disease, and no safety data have been reviewed yet.

**To proceed, the following is needed:**
- Confirmation of the exact disease subtype and target population (indolent or smoldering versus relapsed/refractory)
- Singapore package insert warnings and contraindications (currently blocking the safety screening)
- Documented original indications and mechanism-of-action data
- Evidence specific to early-stage or smoldering myeloma, ideally randomized

The other nine predictions have low prediction scores and little or no evidence. The melanoma-related ones (ranks 2–6) have only indirect preclinical support. None of these is recommended for advancement at this time.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

