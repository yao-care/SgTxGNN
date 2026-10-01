---
layout: default
title: Dactinomycin
parent: Low Evidence (L5)
nav_order: 294
evidence_level: L5
indication_count: 10
---

# Dactinomycin
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

# Dactinomycin: From Cancer Chemotherapy to Relapsing-Remitting Multiple Sclerosis

## One-Sentence Summary

Dactinomycin is a cytotoxic anticancer antibiotic, and the literature in this pack shows it used in combination regimens for paediatric sarcomas and Wilms tumour.
The TxGNN model predicts it may be effective for **relapsing-remitting multiple sclerosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore label data (see Singapore Market Information) |
| Predicted New Indication | Relapsing-remitting multiple sclerosis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Dactinomycin is known to intercalate into DNA and inhibit transcription. Mechanistically, this could suppress rapidly dividing immune cells and produce broad immunosuppression.

This is a weak rationale. Dactinomycin is a highly cytotoxic agent with a narrow therapeutic index. Multiple sclerosis is a chronic, non-oncologic disease for which approved disease-modifying therapies already exist. The risk-benefit balance is therefore unfavourable.

The high score (99.58%) most likely reflects proximity in the knowledge graph to other cytotoxic or immunosuppressive drugs, not a real therapeutic signal. There are no trials, publications or preclinical studies linking dactinomycin to multiple sclerosis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN10989P | K. U. DACTINOMYCIN FOR INJECTION 0.5 mg/vial | Injection, powder, for solution | Korea United Pharmaceutical Inc |

The registration record contains no approved indication text. The only route available is injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anticancer antibiotic, DNA intercalator) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Haematological parameters (CBC with differential) and liver function; hepatic veno-occlusive disease has been reported in the literature retrieved for this drug |
| Handling Protection | Must follow cytotoxic drug handling regulations |

The rows above marked "Please refer to the package insert" have no source data in this Evidence Pack.

## Safety Considerations

Please refer to the package insert for safety information.

The literature retrieved for other candidate indications documents hepatic veno-occlusive disease and hepatopathy after dactinomycin-containing regimens (vincristine, dactinomycin, cyclophosphamide). This is a serious concern in any hepatobiliary or immune-mediated setting. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a model prediction only (L5), with no trials or literature. Dactinomycin's cytotoxicity and narrow therapeutic index make it a poor fit for a chronic non-oncologic disease that already has approved disease-modifying therapies.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking data gap, so the case cannot proceed to safety screening without it)
- Mechanism of action data from DrugBank
- Any preclinical or clinical signal for dactinomycin in multiple sclerosis or autoimmune demyelination

**Note on other predictions in this pack:** Several oncology predictions are much better supported, all in rhabdomyosarcoma (RMS) settings. Parameningeal embryonal RMS (rank 5) is the strongest, at L1 with a suggested "Proceed with Guardrails". It is supported by VAC-regimen (vincristine, dactinomycin, cyclophosphamide) studies from the Children's Oncology Group and the Intergroup Rhabdomyosarcoma Study. Those results are probably already standard of care rather than true repurposing, so they should be confirmed against the labelled indication wording. Evidence for the other rhabdomyosarcoma sites, liver sarcoma and head and neck cancer is limited to case reports, reviews and cohort studies, and evidence for T-cell leukemia is limited to in vitro work.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

