---
layout: default
title: Polatuzumab Vedotin
parent: Low Evidence (L5)
nav_order: 795
evidence_level: L5
indication_count: 10
---

# Polatuzumab Vedotin
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

# Polatuzumab vedotin: From B-Cell Lymphoma to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Polatuzumab vedotin is an anti-CD79b antibody-drug conjugate (ADC) with an MMAE payload, used in B-cell lymphoma.
The TxGNN model predicts it may be effective for **HER2-positive breast carcinoma**,
but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data (lymphoma use noted in the mechanism analysis) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. Based on known information, polatuzumab vedotin is an antibody-drug conjugate that delivers MMAE, a microtubule inhibitor, to cells expressing CD79b.

The mechanistic link to breast cancer is weak. CD79b is a B-cell-restricted antigen and is not a recognized target in breast carcinoma. Polatuzumab does not bind HER2, although other HER2-directed ADCs already exist. The high score (0.993) most likely reflects graph proximity to other ADCs or cytotoxic payloads, not a target-based rationale.

The other nine predictions were also reviewed: other breast cancer subtypes, drug-induced osteoporosis, acne, and three hereditary coagulation disorders. None has a plausible mechanism, and none has trials or supporting literature. Several share identical scores, which points to graph-neighborhood artifacts rather than independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

The 19 publications retrieved for the related prediction "breast tumor luminal A or B" were false-positive matches. The search term "B" pulled in B-cell biology, B-cell lymphoma and hepatitis B vaccine papers. None addresses polatuzumab vedotin in breast cancer.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16345P | POLIVY 30 mg powder for concentrate for solution for infusion | Lyophilized powder for injection | F. Hoffmann-La Roche AG |
| SIN16007P | POLIVY 140 mg powder for concentrate for solution for infusion | Lyophilized powder for injection | BSP Pharmaceuticals S.p.A (Primary Packager) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy: antibody-drug conjugate with a cytotoxic microtubule-inhibitor payload (MMAE) |
| Myelosuppression Risk | Myelosuppression is a known toxicity; please refer to the package insert for severity grading |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count; neurological assessment for neuropathy; liver and renal function |
| Handling Protection | Please refer to the package insert; follow institutional cytotoxic drug handling procedures given the MMAE payload |

## Safety Considerations

Known toxicities of this drug include neuropathy and myelosuppression. No drug interaction records were found. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5). There are no trials or relevant literature, and the target (CD79b) is not expressed in breast carcinoma. The high TxGNN score is not supported by any biological rationale.

**To proceed, the following is needed:**
- Evidence of target expression (CD79b or an alternative) in HER2-positive breast tumors
- Preclinical data showing activity in HER2-positive breast cancer models
- Mechanism of action data from DrugBank
- HSA package insert warnings and contraindications for safety screening
- Comparison against existing HER2-directed ADCs to show a differentiated rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

