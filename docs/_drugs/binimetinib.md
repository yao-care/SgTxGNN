---
layout: default
title: Binimetinib
parent: Low Evidence (L5)
nav_order: 161
evidence_level: L5
indication_count: 10
---

# Binimetinib
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

# Binimetinib: From BRAF V600-Mutant Melanoma to Choroideremia

## One-Sentence Summary

Binimetinib is an oral MEK1/2 inhibitor, used together with encorafenib for BRAF V600-mutant melanoma. The TxGNN model predicts it may be effective for **choroideremia**, an X-linked inherited retinal degeneration. There are **0 clinical trials** and **0 publications** for this indication, so the score of 98.6% is a graph-based prediction only and has no supporting studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | BRAF V600-mutant melanoma (inferred from the mechanism and trial notes; the Singapore license text was blank) |
| Predicted New Indication | Choroideremia |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank in this dataset. The mechanistic notes identify binimetinib as a MEK1/2 inhibitor that acts downstream of BRAF and NRAS in the MAPK pathway. Combined with encorafenib, it is an established regimen for BRAF V600-mutant melanoma.

This mechanism does not plausibly connect to choroideremia. The disease is caused by loss of CHM/REP1 function, and no MAPK-driven mechanism has been established for it. The high TxGNN score most likely reflects network proximity in the knowledge graph, not biology. It should not be read as a signal of efficacy.

The model's other top predictions are melanoma subtypes, and these are much better supported:
- **Non-cutaneous melanoma** (rank 2, 98.60%): 40 registered trials, of which 10 were provided. Evidence level is L2 and the recommendation is "Proceed with Guardrails". Most of the trials enrol melanoma broadly, and non-cutaneous enrolment is unconfirmed.
- **Mucosal melanoma** and **acral lentiginous melanoma**: L2, "Research Question". BRAF V600 mutations are less frequent in these subtypes, so benefit is limited to the BRAF- or NRAS-mutant subset.
- **Six other subtypes** (epithelioid cell, eyelid, scrotum, lentigo maligna, CDK4-linked and superficial spreading melanoma): L4–L5, "Hold". They have no subtype-specific efficacy evidence, only class-level plausibility.

These melanoma predictions largely restate the original indication, so they are not new repurposing opportunities.

## Clinical Trial Evidence

Currently no related clinical trials registered for choroideremia.

## Literature Evidence

Currently no related literature available for choroideremia.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16826P | MEKTOVI FILM-COATED TABLET 15MG | Tablet, film coated | Not stated in the data provided |

Manufacturer: ALMAC Pharma Services Limited; Pierre Fabre Médicament Production (PFMP) (primary and secondary packager). Route: oral.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (MEK1/2 inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

Please refer to the package insert for safety information. The HSA package insert has not been retrieved, and no drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Choroideremia has no registered trials and no literature, and its mechanism (CHM/REP1 loss) has no established link to MEK inhibition. The prediction rests on the model score alone, so it does not justify further investment.

**To proceed, the following is needed:**
- Preclinical evidence that MAPK/MEK signalling contributes to choroideremia pathology
- Retrieval and review of the HSA package insert to complete the safety screen
- Mechanism of action data from DrugBank
- Assessment of route feasibility for an ocular indication, since only an oral tablet is registered
- For the melanoma-subtype predictions: confirmation that the mapped trials enrolled non-cutaneous, mucosal or acral patients, and review of the remaining 30 trials not provided
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

