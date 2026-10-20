---
layout: default
title: Indacaterol
parent: Low Evidence (L5)
nav_order: 528
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Indacaterol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the Singapore registration records"
monitor_inn: "Indacaterol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
---

# Indacaterol
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

# Indacaterol: From Obstructive Airway Disease to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is an ultra-long-acting inhaled beta2-agonist bronchodilator, registered in Singapore in several inhaler products.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but **no clinical trials and no publications** currently support this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records; indacaterol is a long-acting beta2-agonist bronchodilator used for obstructive airway disease |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data are not available in the data compiled for this report. Indacaterol is known to be an ultra-long-acting beta2-adrenergic agonist. It activates a Gs-coupled receptor and raises intracellular cAMP.

NSIAD is caused by gain-of-function variants in the vasopressin V2 receptor (AVPR2). The V2 receptor is also Gs-coupled and raises cAMP. This shared signalling pathway is the only conceivable link, and no direct connection between beta2-agonism and this disease has been established. Beta2-agonism would, if anything, be expected to add to cAMP signalling rather than counteract the overactive V2 receptor.

The high score therefore appears to be a network-level prediction without a supporting mechanism. The prediction is not mechanistically supported.

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
| SIN14539P | Ultibro Breezhaler Inhalation Powder Hard Capsule 110/50 mcg | Capsule | Not listed in the registration record |
| SIN16148P | Atectura Breezhaler Inhalation Powder, Hard Capsule 150/160 mcg | Powder, metered | Not listed in the registration record |
| SIN16149P | Atectura Breezhaler Inhalation Powder, Hard Capsule 150/80 mcg | Powder, metered | Not listed in the registration record |
| SIN16147P | Atectura Breezhaler Inhalation Powder, Hard Capsule 150/320 mcg | Powder, metered | Not listed in the registration record |
| SIN16153P | Enerzair Breezhaler Inhalation Powder, Hard Capsule 150/50/160 mcg | Powder, metered | Not listed in the registration record |

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** hypertension and hypertensive disorders, long QT syndrome (including familial), sudden cardiac arrest, heart conduction disease, coronary artery disease, epilepsy, hyperglycaemia, diabetes mellitus, diabetic ketoacidosis, potassium deficiency, and thyrotoxicosis, hyperthyroidism and Graves disease. These are consistent with the known cardiovascular, metabolic and hypokalaemic effects of beta2-agonists.
- **Drug interactions:** 100 interactions were identified. Examples:
  - **Moderate:** antidiabetic agents (acarbose, metformin, pioglitazone, alogliptin, saxagliptin, albiglutide, canagliflozin, dapagliflozin, chlorpropamide), epinephrine, isometheptene, famotidine and clarithromycin.
  - **Minor:** corticosteroids (hydrocortisone, dexamethasone, budesonide, beclomethasone, betamethasone, triamcinolone) and aprepitant.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NSIAD prediction has only a model score. There are no trials or publications, and no plausible mechanism has been identified. It should not be pursued further on current evidence.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis and preclinical data linking beta2-agonism to AVPR2-driven antidiuresis
- Detailed mechanism of action data and the indications and safety warnings from the Singapore package inserts

**Note on other predictions from the same analysis:**
- **Bronchial disease (rank 7, score 99.18%):** This prediction has the strongest evidence in this analysis (Evidence Level L1, "Proceed with Guardrails"). It is supported by several completed Phase 3 trials in asthma, including NCT02554786 (n=2,216), NCT00529529 (n=805) and NCT01079130 (n=511), and by the IRIDIUM RCT (PMID 32653074, *Lancet Respir Med*, 2020).
- **Caveat:** This is largely an existing drug class use rather than true repurposing. Stand-alone LABA use in asthma carries a safety concern, so use should be restricted to combinations with an inhaled corticosteroid.
- **Other predictions (ranks 2–6 and 8–10):** headache disorder, trigeminal autonomic cephalalgia, paratenonitis, calcific tendinitis, hypertrichosis, myositis, anaphylaxis and Ambras-type hypertrichosis. All have no supporting evidence and are rated "Hold".
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

