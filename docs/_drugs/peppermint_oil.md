---
layout: default
title: Peppermint Oil
parent: Low Evidence (L5)
nav_order: 778
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "Peppermint oil"
predicted_indications: ["leprosy", "pneumocystosis", "coronary artery disease", "myocardial ischemia", "echinococcus granulosus infectious disease", "polyp of vocal cord", "uterine polyp", "polyp of middle ear", "cardiovascular disease", "polyp of frontal sinus"]
description: "Peppermint Oil: predicted new indication Leprosy (evidence level L5)."
---

# Peppermint Oil
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

## Peppermint Oil: From an Oral Enteric-Coated Capsule to Leprosy (Predicted)
{: .text-alpha }

## One-Sentence Summary

Peppermint oil is marketed in Singapore as an enteric-coated oral capsule, but no approved indication is recorded for it in the registration data.
The TxGNN model predicts it may be effective for **leprosy**, with a very high score.
However, there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Peppermint oil is a plant-derived oil rich in menthol, and it is registered in Singapore as a single-ingredient oral product. The registration record does not state an approved indication, so the link between an "original indication" and leprosy cannot be drawn from the available data.

The high score (0.9980) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No mechanistic link to leprosy has been established. Laboratory antimicrobial activity of essential oils does not show efficacy against *Mycobacterium leprae*. This prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered for leprosy.

## Literature Evidence

Currently no related literature available for leprosy.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13034P | COLPERMIN CAPSULE 187mg | Capsule, enteric coated (oral) | Not stated in the registration record |

The product is a single-ingredient, currently valid registration. It is manufactured by Tillotts Pharma AG, with the capsule coating step also handled by SwissCo Services AG.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no supporting trials, no literature, and no plausible mechanism in the available data. It is a computational signal only (L5).

**Other predictions:** Among the other top-ranked predictions, only **cardiovascular disease** (TxGNN score 0.9913) has supporting human evidence (L3, "Research Question"):
- One completed trial, [NCT05561543](https://clinicaltrials.gov/study/NCT05561543), tested peppermint oil on cardiometabolic outcomes in mild-to-moderate hypertension. It is small (40 participants) and has no assigned phase.
- A placebo-controlled randomized trial report ([PMID 42024666](https://pubmed.ncbi.nlm.nih.gov/42024666/), PLoS One, 2026) and its protocol ([PMID 40333716](https://pubmed.ncbi.nlm.nih.gov/40333716/), 2025) cover the same question.
- These results rely on surrogate endpoints and are not confirmatory. If the team wants to pursue a direction with evidence, this one is a better candidate than leprosy.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, because safety screening cannot start without them
- Mechanism of action data, retrievable from DrugBank
- For leprosy: any preclinical or clinical evidence showing activity against *M. leprae*; without it, the prediction should stay on hold
- For cardiovascular disease: the full results of the hypertension trial, and a larger confirmatory study if the signal holds
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

