---
layout: default
title: Povidone-Iodine
parent: Low Evidence (L5)
nav_order: 815
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Povidone-Iodine: predicted new indication Plasmodium falciparum malaria (evidence level L5). Approved use: The registration record does not state an approved indication. The on…"
---

# Povidone-Iodine
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

# Povidone-iodine: From Topical Antisepsis (Sore Throat Spray) to Plasmodium falciparum Malaria

## One-Sentence Summary

Povidone-iodine is a broad-spectrum topical antiseptic. In Singapore it is registered as a sore throat spray.
The TxGNN model predicts it may be effective for **Plasmodium falciparum malaria**, but **no clinical trials and no publications** support this prediction, so it is a computational signal only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | The registration record does not state an approved indication. The only registered product is a sore throat spray (topical antiseptic use). |
| Predicted New Indication | Plasmodium falciparum malaria |
| TxGNN Prediction Score | 88.33% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, povidone-iodine is a broad-spectrum topical antiseptic. It releases free iodine, which oxidizes microbial components and kills bacteria, fungi and viruses on contact.

This does not translate well to malaria. *P. falciparum* is a blood-stage parasite that lives inside red blood cells. Treating it requires a drug that reaches the bloodstream at safe concentrations. Povidone-iodine has no established systemic antiplasmodial activity and is not suited to systemic use. The high TxGNN score most likely reflects network similarity in the knowledge graph (it is a general anti-infective) and not a biological rationale. The mechanistic link is therefore weak.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15313P | Betadine Sore Throat Spray 0.45% w/v (Mundipharma Pharmaceuticals Ltd) | Spray | Not stated in the registration record |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug–disease links in the model's knowledge graph, not taken from product label text): epilepsy, liver disease, gallbladder disease, respiratory failure, atrioventricular block / heart block (including atrioventricular dissociation). These should be verified against the official product information.

Please refer to the package insert for warnings, contraindications and drug interaction information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score, with no trials or publications. The drug is a topical antiseptic with no known systemic antimalarial mechanism, so it is poorly suited to a blood-stage parasite.

**To proceed, the following is needed:**
- Laboratory evidence of antiplasmodial activity at concentrations that are safe in humans
- Mechanism of action data and a credible systemic delivery route
- Package insert warnings and contraindications, so that safety can be screened

**Note on other predictions in the same analysis:** Several lower-ranked predictions have more supporting evidence than malaria and may merit separate evaluation.
- **Appendicitis (L2):** a Phase 2 randomized pilot trial (NCT02664220, 100 children, dilute povidone-iodine irrigation in perforated appendicitis) and supporting studies. The results are encouraging but come from pilot-scale studies. A larger Phase 3 trial is needed.
- **Pneumonia (L2):** mostly COVID-19 nasal and oral antiseptic trials with viral-load endpoints. The evidence is indirect, and meta-analyses exist for ventilator-associated pneumonia prevention.
- **Peritonitis (L3):** animal studies and a case report of sclerosing encapsulating peritonitis after intraperitoneal use raise a serious safety concern.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

