---
layout: default
title: Pibrentasvir
parent: Low Evidence (L5)
nav_order: 791
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Pibrentasvir: predicted new indication Hepatitis B virus infection (evidence level L5). Approved use: Chronic hepatitis C virus infection"
monitor_inn: "Pibrentasvir"
predicted_indications: ["hepatitis B virus infection", "HIV infectious disease", "hepatitis E virus infection", "hepatitis A virus infection", "hepatitis, viral, animal", "Omsk hemorrhagic fever", "Kyasanur forest disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Pibrentasvir
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Pibrentasvir: From Chronic Hepatitis C to Hepatitis B Virus Infection
{: .text-alpha }

## One-Sentence Summary

Pibrentasvir is an HCV NS5A inhibitor, originally used to treat chronic hepatitis C virus infection.
The TxGNN model predicts it may be effective for **hepatitis B virus infection**,
but **no clinical trials** and only **20 publications** (almost all about hepatitis C) are available, and none directly supports use against hepatitis B.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Chronic hepatitis C virus infection (the Singapore licence record contains no indication text; this comes from the original indication data) |
| Predicted New Indication | Hepatitis B virus infection |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, pibrentasvir is an NS5A inhibitor. It is used with glecaprevir (an NS3/4A protease inhibitor) in the fixed-dose combination marketed as Maviret/Mavyret. Its efficacy in hepatitis C is well established.

The mechanistic case for hepatitis B is weak. HBV has no NS5A protein. It is a DNA virus that replicates through reverse transcription and a cccDNA intermediate, which is very different from HCV replication. The high TxGNN score (0.9984) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No direct antiviral mechanism against HBV is supported.

The other top predictions show the same pattern (hepatitis A and E, HIV, tick-borne flaviviruses, and animal viral diseases). Each is either a family-level analogy or network proximity, and none has evidence of pibrentasvir activity.

## Clinical Trial Evidence

Currently no related clinical trials are registered for hepatitis B virus infection.

## Literature Evidence

No hepatitis B-specific studies of pibrentasvir were found. The publications retrieved are mainly hepatitis C papers matched through a broad "viral hepatitis" category. The most relevant are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31981264](https://pubmed.ncbi.nlm.nih.gov/31981264/) | 2020 | Cohort (retrospective) | Journal of Viral Hepatitis | Real-world data on glecaprevir/pibrentasvir in 108 Taiwanese HCV patients with CKD stage 4 or 5; HCV only |
| [37286314](https://pubmed.ncbi.nlm.nih.gov/37286314/) | 2023 | Cohort | BMJ Open | Real-life effectiveness and side effects of HCV treatment in prisons in Southern Taiwan |
| [30982721](https://pubmed.ncbi.nlm.nih.gov/30982721/) | 2019 | Review | Lancet Gastroenterol Hepatol | Direct-acting antivirals for HCV in children and adolescents |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | Pediatric viral hepatitis; notes that HBV treatment is far from curative, with no pibrentasvir data for HBV |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | Pharmacokinetic and pharmacodynamic considerations for HCV therapies |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | Retreatment of HCV patients after direct-acting antiviral failure |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | Diagnosis and treatment of chronic hepatitis C for primary care |
| [42127258](https://pubmed.ncbi.nlm.nih.gov/42127258/) | 2026 | Conference report | Top Antivir Med | CROI 2026 overview of viral hepatitis; general, with no pibrentasvir-specific HBV data |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15603P | MAVIRET FILM-COATED TABLET 100MG/40MG | Film-coated tablet (oral) | Indication text not recorded in the licence data |

## Cytotoxicity

Not applicable. Pibrentasvir is an antiviral, not an antineoplastic drug.

## Safety Considerations

Please refer to the package insert for safety information. No warning or contraindication text was available in the data compiled for this report, and no drug interaction records were found. The package insert from the Health Sciences Authority (HSA) still needs to be obtained and reviewed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score for hepatitis B is not backed by any clinical trial, hepatitis B-specific publication, or plausible mechanism. HBV lacks the NS5A target. Pibrentasvir's evidence is limited to its approved use in hepatitis C, so the prediction is best viewed as a TxGNN model (deep learning) artefact.

**To proceed, the following is needed:**
- In vitro antiviral activity data for pibrentasvir against HBV (replication and cccDNA assays), which is the minimum to justify any further work
- Mechanism of action data (MOA) from DrugBank
- HSA package insert warnings and contraindications for safety screening
- Review of HBV reactivation risk when direct-acting antivirals are used in HBV/HCV co-infected patients, which is a safety issue rather than a repurposing signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

