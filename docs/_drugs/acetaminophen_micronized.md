---
noindex: true
sitemap: false
layout: default
title: Acetaminophen Micronized
parent: Low Evidence (L5)
nav_order: 30
evidence_level: L5
indication_count: 0
last_modified_at: 2026-11-12
predicted_indications: []
---

# Acetaminophen Micronized
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **0** 
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

## Acetaminophen Micronized: Insufficient Data for Repurposing Prediction
{: .text-alpha }

---

## One-Sentence Summary

Acetaminophen Micronized is a particle-size-reduced formulation of the well-known analgesic and antipyretic acetaminophen (paracetamol), commonly used for mild-to-moderate pain relief and fever reduction.
The TxGNN model returned **no predicted new indications** for this compound, likely due to the absence of a matched DrugBank ID for the micronized formulation variant.
Without a TxGNN score or supporting evidence, a formal repurposing evaluation cannot proceed at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic / Antipyretic (general pharmaceutical knowledge; no TFDA registration data available) |
| Predicted New Indication | None — TxGNN returned no predictions |
| TxGNN Prediction Score | N/A |
| Evidence Level | L5 (model prediction only — not applicable; no prediction generated) |
| Singapore Market Status | Marketed (valid licences: 101 of 101) |
| Number of Registrations | 101 (valid: 101) |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

No TxGNN repurposing prediction is available for this entry. The pipeline query log shows that a DrugBank lookup was attempted and returned one result (`result_count: 1`), but no `drugbank_id` was successfully mapped into the candidate record. Without a valid DrugBank identifier, TxGNN cannot traverse the knowledge graph to generate disease associations.

Acetaminophen (INN: paracetamol) is one of the most widely used over-the-counter analgesics globally, with a well-characterised mechanism involving cyclooxygenase inhibition in the central nervous system and modulation of the endocannabinoid system. The "micronized" designation refers to a pharmaceutical particle-size reduction process intended to improve dissolution rate and bioavailability — it is the same active moiety, not a distinct chemical entity.

To unlock TxGNN predictions, the canonical DrugBank entry for acetaminophen (DB00316) should be explicitly linked to this candidate before re-running the prediction pipeline.

<!-- review:begin sg-lic-20261106-acetaminophen_micronized-1 -->

> **Review correction (2026-11-06)**: Originally stated: "This drug is currently **not registered** in Singapore under the Health Sciences Authority (HSA). No license records are available." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 101 registrations for this drug, 101 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-acetaminophen_micronized-1 -->

---

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN05323P | PROGESIC TABLET 500 mg | TABLET | Valid |
| SIN05328P | PANAMOL TABLETS 500 mg | TABLET | Valid |
| SIN05471P | BIOGESIC TABLET 500 mg | TABLET | Valid |
| SIN05559P | PANAMOL FORTE SUSPENSION 250 mg/5 ml | SUSPENSION | Valid |
| SIN05565P | PARMOL 250 SUSPENSION 250 mg/5 ml | SUSPENSION | Valid |

Showing 5 of 101 HSA registrations.

<!-- licenses:end -->

---

## Safety Considerations

Please refer to the package insert for safety information. No DDI records, contraindications, or key warnings were retrieved during the current data collection cycle.

> Until this document is retrieved and parsed, a formal safety profile cannot be constructed.

<!-- review:begin sg-lic-20261106-acetaminophen_micronized-2 -->

> **Review correction (2026-11-06)**: Originally stated: "> **Note for reviewers:** The TFDA package insert (仿單) was flagged as a blocking data gap (DG001). Until this document is retrieved and parsed, a formal safety profile cannot be constructed." Removed: leftover template text about Taiwan's TFDA, which does not apply to this Singapore page. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-acetaminophen_micronized-2 -->

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The absence of TxGNN predictions, a missing DrugBank ID linkage mean there is no actionable repurposing signal to evaluate at this time. The underlying active ingredient (acetaminophen) is well-characterised, but this specific formulation variant has not been processed through the full pipeline.

<!-- review:begin sg-lic-20261106-acetaminophen_micronized-3 -->

> **Review correction (2026-11-06)**: Originally stated: "The absence of TxGNN predictions, a missing DrugBank ID linkage, and zero Singapore regulatory registrations mean there is no actionable repurposing signal to evaluate at this time." Removed: it conflicted with the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 101 registrations for this drug, 101 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-acetaminophen_micronized-3 -->

**To proceed, the following is needed:**

1. **Resolve DrugBank ID mapping** — Explicitly assign DrugBank ID `DB00316` (acetaminophen) to this candidate and re-run the TxGNN prediction pipeline (`scripts/run_kg_prediction.py`)
3. **Confirm formulation intent** — Clarify whether "micronized" is being evaluated as a standalone entity or as a formulation variant of standard acetaminophen; this determines whether a separate evidence collection run is warranted
4. **Re-run evidence collection** — After DrugBank ID is resolved, re-run ClinicalTrials.gov and PubMed collectors to populate the evidence pack
5. **HSA registration check** — Verify whether any acetaminophen micronized products are under pending HSA registration or are covered under existing acetaminophen monograph approvals in Singapore

<!-- review:begin sg-lic-20261106-acetaminophen_micronized-4 -->

> **Review correction (2026-11-06)**: Originally stated: "**Resolve DrugBank ID mapping** — Explicitly assign DrugBank ID `DB00316` (acetaminophen) to this candidate and re-run the TxGNN prediction pipeline (`scripts/run_kg_prediction.py`) / **Retrieve TFDA package insert** — Download and parse the TFDA 仿單 PDF to populate key warnings, contraindications, and MOA fields (Data Gap DG001, severity: Blocking)" Removed: leftover template text about Taiwan's TFDA, which does not apply to this Singapore page. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-acetaminophen_micronized-4 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "This drug is currently **not registered** in Singapore under the Health Sciences Authority (HSA). No license records are available" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "**Note for reviewers:** The TFDA package insert (仿單) was flagged as a blocking data gap (DG001)" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "and zero Singapore regulatory registrations" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |
| 2026-11-06 | Removed: "2. **Retrieve TFDA package insert** — Download and parse the TFDA 仿單 PDF to populate key warnings, contraindications, and MOA fields (Data G" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

