---
layout: default
title: Idarubicin
parent: Low Evidence (L5)
nav_order: 512
evidence_level: L5
indication_count: 10
---

# Idarubicin
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

# Idarubicin: From Cytotoxic Anthracycline Chemotherapy to Bulbar Polio

## One-Sentence Summary

Idarubicin is a cytotoxic anthracycline chemotherapy injection that is marketed in Singapore as ZAVEDOS.
The TxGNN model predicts it may be effective for **bulbar polio**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
This looks like a graph artifact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Idarubicin is an anthracycline that intercalates into DNA and inhibits topoisomerase II, which kills rapidly dividing cells.

This mechanism gives no plausible link to bulbar polio, which is an infection of motor neurons by poliovirus. Idarubicin has no known antiviral or neuroprotective action, and polio is prevented by vaccination. The high score (97.05%) most likely reflects proximity in the knowledge graph rather than real biology, so this prediction is not considered reasonable.

Other predictions for this drug are more coherent. The most notable are ganglioneuroblastoma (score 78.4%), where anthracyclines are part of multi-agent neuroblastoma regimens, and retroperitoneal neoplasm (77.4%). Both still need idarubicin-specific evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN12455P | ZAVEDOS Solution for Injection 10 mg/10 ml | Injection |
| SIN12456P | ZAVEDOS Solution for Injection 5 mg/5 ml | Injection |

Both products are made by Bridgewest Perth Pharma Pty Ltd and Zydus Hospira Oncology Private Limited.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline; DNA intercalator and topoisomerase II inhibitor) |
| Myelosuppression Risk | High (anthracyclines are myelosuppressive) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function; cardiac function assessment is also typical for anthracyclines |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone, with no trials or literature, and there is no credible mechanism linking a cytotoxic anthracycline to poliovirus infection. Using a myelosuppressive, cardiotoxic drug for this condition would carry risk without a plausible benefit.

**To proceed, the following is needed:**
- The approved indications and safety information from the HSA package insert, which are missing from the Singapore records
- Mechanism of action data from DrugBank
- A shift in focus to the more biologically plausible predictions (ganglioneuroblastoma, retroperitoneal neoplasm), starting with a literature search for idarubicin-specific data
- Remapping of the obsolete "Hodgkin's granuloma" term to current Hodgkin lymphoma before any evidence search

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

