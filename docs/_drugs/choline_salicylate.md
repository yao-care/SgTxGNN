---
layout: default
title: Choline Salicylate
parent: Low Evidence (L5)
nav_order: 245
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Choline Salicylate: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the Singapore licence records"
monitor_inn: "Choline salicylate"
predicted_indications: ["Prinzmetal angina", "rheumatoid arthritis", "hypertensive disorder", "migraine disorder", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "malignant renovascular hypertension", "Raynaud disease", "pulmonary hypertension"]
---

# Choline Salicylate
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

## Choline Salicylate: From Topical Oral Pain Relief to Prinzmetal Angina
{: .text-alpha }

## One-Sentence Summary

Choline salicylate is a non-acetylated salicylate marketed in Singapore as topical gels. The TxGNN model's top prediction is **Prinzmetal angina**, but **no clinical trials and no publications** support this direction. The only prediction with any published literature is **rheumatoid arthritis** (3 historical reports from 1977–1980), which is the more credible repurposing candidate.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence records (all three licences list no approved indication text; products are oral/topical pain-relieving gels) |
| Predicted New Indication | Prinzmetal angina (top-ranked prediction); rheumatoid arthritis is the only prediction with literature support |
| TxGNN Prediction Score | 0.9984 |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | Marketed (valid licences: 3 of 3) |
| Number of Registrations | 3 (valid: 3) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, choline salicylate is a non-acetylated salicylate with cyclooxygenase (COX)-inhibitory, anti-inflammatory and analgesic activity.

For Prinzmetal angina, a plausible but unproven link is the effect of salicylates on prostanoid pathways involved in vasospasm. However, high-dose aspirin has been reported to potentially worsen vasospastic angina, so the rationale is uncertain. Non-acetylated salicylates also have minimal antiplatelet activity, which weakens the link further. The score of 0.9984 comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Among the other top-10 predictions, rheumatoid arthritis is the best fit mechanistically, because anti-inflammatory and analgesic activity is consistent with symptomatic control of inflammatory joint disease. The hypertension-related predictions (hypertensive disorder, malignant hypertensive renal disease, malignant renovascular hypertension) run against known salicylate and NSAID effects, which can raise blood pressure and reduce renal perfusion. Several pulmonary hypertension predictions share identical scores, suggesting one shared inference rather than independent signals.

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina or any of the other top-10 predicted indications.

## Literature Evidence

No literature was found for Prinzmetal angina. The only literature in the compiled data relates to the rank-2 prediction, rheumatoid arthritis:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [377958](https://pubmed.ncbi.nlm.nih.gov/377958/) | 1979 | Review | American Journal of Hospital Pharmacy | Review of antirheumatic drugs, including choline salicylate and choline magnesium salicylate among the salicylates |
| [897386](https://pubmed.ncbi.nlm.nih.gov/897386/) | 1977 | Clinical study (likely uncontrolled/observational) | Reumatologia | Usefulness of choline salicylate in children with rheumatoid arthritis (no abstract available) |
| [7188920](https://pubmed.ncbi.nlm.nih.gov/7188920/) | 1980 | Review/Clinical report | Fysiatricky a reumatologicky vestnik | Choline salicylate as an antirheumatic agent (no abstract available) |

These reports are old, low-tier and unregistered. They support symptomatic relief rather than disease modification, and none compares choline salicylate with current standards of care.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10428P | Soragel Antiseptic Pain Relieving Oral Gel | Gel | Not stated |
| SIN04948P | Ora-Sed Jel | Gel | Not stated |
| SIN04303P | Bonjela Gel | Gel | Not stated |

All three licences are valid single-ingredient products, and all are topical gels. Any systemic indication (such as rheumatoid arthritis or angina) would therefore need a different formulation or route.

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction databases. The first 20 reviewed include mostly Moderate-level and a few Minor-level interactions. Main groups:
  - **Corticosteroids** (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide): Moderate
  - **Sulfonylurea antidiabetics** (chlorpropamide, acetohexamide, glimepiride, glipizide, glyburide): Moderate
  - **Insulins** (human insulin, insulin aspart): Moderate
  - **Antacids and adsorbents** (aluminium hydroxide, calcium carbonate, activated charcoal): Moderate
  - **Fenfluramine and dexfenfluramine**: Moderate
  - **Proton pump inhibitors** (rabeprazole, dexlansoprazole): Minor
- **Class-level concerns relevant to the predictions**: Salicylates and NSAIDs can raise blood pressure, blunt antihypertensive therapy, and impair renal perfusion. This is a particular concern for the hypertension and renal predictions.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, Prinzmetal angina, rests on model score alone (L5), with no trials or literature, and the mechanistic rationale is doubtful because salicylates may worsen vasospasm. The rheumatoid arthritis prediction has limited historical support (L3) but is symptomatic only and is not compared with modern therapy. Only topical gel products are registered in Singapore.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- For rheumatoid arthritis: a structured literature review and comparison with current standard NSAID or DMARD therapy, plus a check of route and formulation compatibility (existing products are topical only)
- For Prinzmetal angina and the hypertension, renal and pulmonary hypertension predictions: no further work is recommended unless new supporting evidence emerges, given the safety and mechanistic concerns
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

