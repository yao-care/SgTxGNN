---
layout: default
title: Caffeine
parent: Low Evidence (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From Approved Use (Indication Not Recorded in Registration Data) to Nasal Cavity Disease

## One-Sentence Summary

Caffeine is a widely used stimulant that appears in 20 Singapore registrations, including infusion, capsule and tablet products, but none of the records list an approved indication.
The TxGNN model predicts it may be effective for **nasal cavity disease**, with a very high score (99.91%).
There are **0 clinical trials** and **3 publications** on this prediction, and none of them tests caffeine as a treatment for a nasal disease, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified in the registration data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L4 (preclinical and mechanism-level evidence only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. From general pharmacology, caffeine is an adenosine receptor antagonist and a phosphodiesterase (PDE) inhibitor. Adenosine signalling occurs in airway and mucosal tissue, and bitter taste receptors are expressed in nasal and airway epithelium. That gives a possible but only indirect pharmacological link to nasal disease.

The retrieved literature does not show that this link has been tested. The only nasal-related study is a formulation paper on a caffeine nasal gel designed to improve cognition after sleep deprivation. That study uses the nose as a delivery route, not as a disease target. The very high TxGNN score reflects proximity in the knowledge graph, not clinical support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bitter taste receptors are found in several tissues, including the nasal cavity and lungs. This offers a possible pharmacological link to airway epithelium but does not address caffeine treatment. |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Formulation / preclinical | Current Drug Delivery | A thermo-sensitive nasal in situ gel of caffeine to improve cognition after sleep deprivation. It is a drug-delivery study, not treatment of a nasal disease. |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Animal study | Cancer Research | Black tea and caffeine reduced lung tumours in rats given a tobacco-specific carcinogen. It concerns lung cancer prevention and is not relevant to nasal disease. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16929P | GENCEBOK SOLUTION FOR INFUSION 10MG/ML | Infusion, solution | Not specified in the registration data |
| SIN08055P | SEMOR PAIN AND FEVER RELIEF CAPSULES | Capsule | Not specified in the registration data |
| SIN14766P | PANADOL EXTRA WITH OPTIZORB CAPLETS 500mg/65mg | Tablet | Not specified in the registration data |
| SIN03369P | FONGTIT 600 CAPSULE | Capsule | Not specified in the registration data |
| SIN11746P | CAFFOX TABLET | Tablet | Not specified in the registration data |

The listed registrations cover infusion, oral capsule and oral tablet forms. None is a nasal product, so a nasal route would need a new formulation.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only for practical purposes. There are no trials, and the retrieved papers are a delivery-formulation study, a receptor review and an unrelated rat lung study. No mechanism specific to nasal disease has been shown. Existing Singapore products are not in a nasal dosage form.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from the HSA website, which are currently missing and block safety screening.
- Detailed mechanism of action data (for example from DrugBank).
- The approved indications for the Singapore registrations.
- Preclinical or clinical evidence of caffeine in a specific nasal condition (for example allergic rhinitis or chronic rhinosinusitis), since "nasal cavity disease" is too broad to act on.
- A route compatibility assessment for a nasal formulation.

Among the other TxGNN predictions for caffeine, hypnic headache has the stronger signal (L3, review-level evidence). It may be a better candidate to pursue than nasal cavity disease.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

