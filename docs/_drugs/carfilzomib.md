---
layout: default
title: Carfilzomib
parent: Low Evidence (L5)
nav_order: 212
evidence_level: L5
indication_count: 10
---

# Carfilzomib
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

# Carfilzomib: From Multiple Myeloma to CMM7 (Hereditary Cutaneous Melanoma Subtype)

## One-Sentence Summary

Carfilzomib is a proteasome inhibitor marketed in Singapore as Kyprolis, and is generally used for relapsed/refractory multiple myeloma. The TxGNN model predicts it may be effective for **CMM7**, which appears to be a hereditary cutaneous melanoma subtype. There are **0 clinical trials** and **0 publications** supporting this specific prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records provided; generally relapsed/refractory multiple myeloma |
| Predicted New Indication | CMM7 |
| TxGNN Prediction Score | 99.37% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Carfilzomib is an irreversible proteasome inhibitor. Its efficacy in multiple myeloma is established, and proteasome inhibition causes proteotoxic stress and apoptosis in tumour cells. In principle, this could apply to other cancers.

The high score for CMM7 most likely reflects graph proximity to other melanoma nodes in the knowledge graph. It does not reflect a known biological link. No established connection exists between proteasome inhibition and this hereditary subtype, and no trials or publications were found. The prediction should be treated as a hypothesis only.

Melanoma in general has weak indirect support. One in vitro study reported enhanced apoptosis in mouse B16-F1 melanoma cells when carfilzomib was combined with bortezomib. There are no human efficacy data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15184P | KYPROLIS Powder for Solution for Infusion 60 mg/vial | Injection, powder, lyophilized, for solution |
| SIN15414P | KYPROLIS Powder for Solution for Infusion 30 mg/vial | Injection, powder, lyophilized, for solution |

The approved indication text was not included in the licence records provided.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (proteasome inhibitor) |
| Myelosuppression Risk | Present, including neutropenia; please refer to the package insert for details |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC (with differential) at minimum; please refer to the package insert for the full list |
| Handling Protection | Follow the institution's cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The CMM7 prediction has no clinical trials, no literature and no mechanistic support. The model score alone is not enough to justify further investment. The Singapore package insert safety data have not been obtained yet.

For context, other predictions in this run have better support:
- **Myeloid leukemia** is the best-supported new indication (L3). It has a completed Phase 1 carfilzomib trial in relapsed/refractory AML and ALL (NCT01137747, n=18) and supporting preclinical work.
- **Indolent plasma cell myeloma** has strong mechanistic plausibility but no indication-specific trial in the data.
- **Melanoma** has only preclinical evidence.

**To proceed, the following is needed:**
- Singapore package insert (approved indication, warnings and contraindications)
- Detailed mechanism of action data (MOA), for example from DrugBank
- Any preclinical or clinical data specific to CMM7 or hereditary melanoma; if none emerges, redirect effort to the myeloid leukemia or indolent myeloma candidates

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

