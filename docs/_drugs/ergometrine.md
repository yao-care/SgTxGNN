---
layout: default
title: Ergometrine
parent: Low Evidence (L5)
nav_order: 389
evidence_level: L5
indication_count: 10
---

# Ergometrine
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

# Ergometrine: From Uterotonic Use to Hypertrichosis

## One-Sentence Summary

Ergometrine is an ergot alkaloid used as a uterotonic (a drug that contracts the uterus) and vasoconstrictor. The TxGNN model predicts it may be effective for **hypertrichosis**, but **no clinical trials and no publications** support this prediction. It is a model output only, with no pharmacological rationale behind it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record (drug class: uterotonic) |
| Predicted New Indication | Hypertrichosis (disease) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Ergometrine is known to act as an alpha-adrenergic and 5-HT2 receptor agonist. It contracts uterine muscle and constricts blood vessels, which is why it is used as a uterotonic.

No plausible link connects these actions to hypertrichosis, which is excessive hair growth. Hypertrichosis has no vasoconstrictor-related mechanism that ergometrine could correct. The high TxGNN score (99.96%) reflects a knowledge-graph pattern, not a demonstrated biological rationale. This prediction should be treated as unsupported.

For context, the same run produced 9 other predictions. Only **migraine disorder** (rank 7) has usable literature, at evidence level L3. It is discussed in the conclusion.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03588P | SYNTOMETRINE INJECTION (Panpharma GmbH) | Injection | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information.

Ergometrine's vasoconstrictor action carries a known risk of vasospasm. The retrieved literature on other candidate indications includes reports of coronary vasospasm and raised pulmonary pressure with related ergot drugs. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. It has no trials, no literature, and no mechanistic link between ergometrine and hypertrichosis, so it does not justify further investment. Package insert safety data is also still missing.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indication), which blocks any safety screening
- Mechanism of action data from DrugBank
- A mechanistic rationale for hypertrichosis, without which the prediction should not advance
- Consider redirecting the review to **migraine disorder** (rank 7, L3). Evidence there comes mostly from the analog methylergonovine (small, non-randomized studies), not ergometrine itself. It would need a safety and analog-equivalence review first, given the vasospasm risk.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

