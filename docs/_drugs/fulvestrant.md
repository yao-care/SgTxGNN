---
layout: default
title: Fulvestrant
parent: Medium Evidence (L3-L4)
nav_order: 458
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Fulvestrant: predicted new indication HIV infectious disease (evidence level L4). Approved use: Not stated in the licence data compiled for this report"
monitor_inn: "Fulvestrant"
predicted_indications: ["HIV infectious disease", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "rheumatoid arthritis", "acne (disease)", "brachydactyly-syndactyly syndrome", "hemoglobinopathy", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
---

# Fulvestrant
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Fulvestrant: From Its Licensed Breast Cancer Use to HIV Infectious Disease

## One-Sentence Summary

Fulvestrant is an estrogen receptor antagonist and degrader that is marketed in Singapore as an injectable. The data compiled for this report do not include the approved-indication text for its licences.
The TxGNN model predicts it may be effective for **HIV infectious disease**, but there are **0 clinical trials** and only **2 publications** (one of them on a different virus), so the prediction rests on early laboratory evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence data compiled for this report |
| Predicted New Indication | HIV infectious disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fulvestrant is generally known as an estrogen receptor alpha (ERα) antagonist and degrader. Its trials in the compiled data are in hormone receptor-positive, HER2-negative advanced breast cancer, so that is presumably its established use. The licence records themselves list no indication text.

The link to HIV is indirect. ERα is expressed in CD4+ T cells and appears to influence HIV transcription and latency. A 2026 laboratory study (JCI Insight) examined how ERα ligands, including fulvestrant, and HIV latency-reversing agents interact in these cells. Fulvestrant could plausibly influence latency reversal, but this is preclinical work only. No human data exist.

Other high-scoring predictions have even weaker support. Simian immunodeficiency virus infection and feline AIDS appear to come from similarity to HIV in the knowledge graph. Multiple endocrine neoplasia appears to come from shared endocrine disease ontology, because the linked trials are all in breast cancer, not in that condition.

## Clinical Trial Evidence

Currently no related clinical trials registered for HIV infectious disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Preclinical / in vitro | JCI Insight | Studied the effect of estrogen, fulvestrant and HIV latency-reversing agents on ERα in CD4+ T cells. It supports a mechanistic link between ER signaling and HIV latency. |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Multi-cohort omics analysis | Research Square | Concerns HTLV-1-associated myelopathy, a different retroviral disease, not HIV. Only indirectly relevant. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13216P | Faslodex Solution For Injection 250 mg/5ml | Injection, solution | Not listed |
| SIN16154P | Fulvestrant-Teva Solution For Injection 250mg/5ml | Injection, solution | Not listed |
| SIN16152P | Fulvestrant Sandoz Solution For Injection In Prefilled-Syringe 250mg/5ml | Injection, solution | Not listed |
| SIN16163P | Femcord Solution For Injection 250 mg/5 ml | Injection, solution | Not listed |
| SIN16780P | Fulvestrant-AFT Solution For Injection In Prefilled-Syringe 250mg/5ml | Injection, solution | Not listed |

Three further licences are valid (SIN17045P, SIN16848P, SIN16893P). All 8 are single-ingredient products, and none is cancelled.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Endocrine therapy (estrogen receptor antagonist and degrader), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions. Because the knowledge graph flags thrombocytopenia, blood coagulation disease and liver disease, a blood count, coagulation status and liver function are reasonable to consider. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links, not label text): liver disease, gallbladder disease, thrombocytopenia, blood coagulation disease.
- **Drug Interactions**: 92 potential interactions were recorded, all with an unclassified severity level. Examples include warfarin, metformin, simvastatin, prednisone, dexamethasone, omeprazole, pantoprazole, morphine, ondansetron and bupropion. Warfarin deserves attention given the coagulation signal.

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The HIV prediction has a high model score but only one indirect laboratory study supporting it and no clinical trials. The evidence level is L4. The data compiled for this report also lack approved-indication text and label safety information, which blocks safety screening.

**To proceed, the following is needed:**
- The HSA package insert (indication, warnings and contraindications)
- Mechanism of action data from DrugBank
- Further preclinical work showing whether fulvestrant promotes or suppresses HIV latency reversal in CD4+ T cells, and in which direction
- A rationale for anti-estrogen therapy in people living with HIV, including interactions with antiretroviral regimens
- An assessment of the safety of long-term estrogen blockade in this population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

