---
layout: default
title: Aprepitant
parent: Low Evidence (L5)
nav_order: 105
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-20
description: "Aprepitant: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not available"
monitor_inn: "Aprepitant"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "hypertrichosis (disease)", "pulmonary hypertension", "leprosy", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "kyphoscoliotic heart disease", "syndrome with a Dandy-Walker malformation as major feature", "subarachnoid hemorrhage (disease)", "isolated genetic hair shaft abnormality"]
---

# Aprepitant
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

## Aprepitant: From Chemotherapy-Related Nausea and Vomiting to Nephrogenic Syndrome of Inappropriate Antidiuresis
{: .text-alpha }

## One-Sentence Summary

Aprepitant is an NK1 receptor antagonist and is marketed in Singapore as an oral capsule. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 relevant publications** supporting this direction. This is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the Singapore licence records) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aprepitant: "Aprepitant is a selective high-affinity antagonist of human substance P/neurokinin 1 (NK 1 ) receptors. Aprepitant has little or no affinity for serotonin (5-HT 3 ), dopamine, and corticosteroid receptors. Aprepitant has been shown in animal models to inhibit emesis induced by cytotoxic chemotherapeutic agents, such as cisplatin, via central actions." ([DailyMed: Cinvanti (aprepitant) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c218d3a-a508-4abc-9ed8-a6e8e191d1b4), label version 2026-04-01; accessed 2026-11-19.) Aprepitant is known to be a substance P/neurokinin-1 (NK1) receptor antagonist, and it penetrates the central nervous system.

NSIAD is caused by a gain-of-function change in the vasopressin V2 receptor, which leads to water retention and low blood sodium. No established link connects NK1 antagonism to this V2 receptor mechanism. The only argument is speculative: substance P might modulate water balance through the vasopressin axis, and no data supports it.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The prediction should be treated as a hypothesis only.

Other high-ranking predictions have the same limitation. Hypertrichosis, leprosy, pulmonary hypertension, subarachnoid haemorrhage and several rare congenital disorders were also predicted, and none has supporting trials or relevant literature. Subarachnoid haemorrhage and pulmonary hypertension have only weak, indirect preclinical hypotheses involving substance P/NK1 signalling.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for nephrogenic syndrome of inappropriate antidiuresis.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN12369P | EMEND CAPSULE 80 mg | CAPSULE | Valid |
| SIN12371P | EMEND TRI-PACK CAPSULE | CAPSULE | Valid |
| SIN16363P | INAPITANT TRI-PACK CAPSULE | CAPSULE | Valid |

<!-- licenses:end -->

All licences are valid products, and none is cancelled. The only route of administration is oral.

<!-- review:begin sg-lic-20261106-aprepitant-1 -->

> **Review correction (2026-11-24)**: Originally stated: "All three licences are valid single-ingredient products, and none is cancelled." Removed: it described the products as single-ingredient or combination products in a way that did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-aprepitant-1 -->

## Safety Considerations

- **Contraindications (model signal, not label text)**: The TxGNN model (deep learning) indicates a contraindication association with **liver failure**. This may reflect similarities the model learned between related diseases, not biological evidence. This should be verified against the official package insert.
- **Drug Interactions**: The interaction query returned 100 records, and the first 20 are in the data compiled for this report. Several are rated **Major**:
  - Fentanyl
  - Alfentanil
  - Acalabrutinib

  Examples rated **Moderate** include paclitaxel, abemaciclib, nifedipine, ibuprofen, hydrocortisone, fluvoxamine, fosphenytoin, gefitinib, rabeprazole, lidocaine and levonorgestrel. Dolutegravir is rated Minor. Aprepitant is metabolised through CYP3A4, which is a likely reason for many of these interactions. A full interaction review would be needed before any new use.

Warnings and contraindications from the package insert are not available. Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence level is L5. There are no clinical trials and no relevant literature. There is also no plausible mechanistic link between NK1 antagonism and the V2 receptor gain-of-function that causes NSIAD. Package insert safety data are also missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website, to enable safety screening
- Mechanism of action data from DrugBank, and a mechanistic assessment of any substance P and vasopressin link
- Approved indication text for the Singapore licences, to confirm the original indication
- Preclinical or literature evidence showing NK1 antagonism affects water balance or V2 receptor signalling
- A review of the major drug interactions (opioids, CYP3A4-related drugs) and of the liver failure signal for the target population
- Route compatibility and similarity-to-original assessments, which are still pending

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "single-ingredient" | Corrected (revised 2026-11-24; earlier version kept in the record) | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Cinvanti (aprepitant) prescribing information, Heron Therapeutics, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4c218d3a-a508-4abc-9ed8-a6e8e191d1b4) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

