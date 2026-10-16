---
layout: default
title: Febuxostat
parent: Medium Evidence (L3-L4)
nav_order: 418
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Febuxostat: predicted new indication Hypouricemia, renal (evidence level L4). Approved use: Hyperuricemia"
---

# Febuxostat
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Febuxostat: From Hyperuricemia to Renal Hypouricemia

## One-Sentence Summary

Febuxostat is a xanthine oxidase inhibitor originally used to treat hyperuricemia (high blood uric acid).
The TxGNN model predicts it may be effective for **renal hypouricemia**, but this direction is supported by only **1 clinical trial of uncertain relevance** and **2 publications** (narrative review and case-level reports).
Mechanistically, lowering uric acid further in a condition already defined by low uric acid is counterintuitive, so this prediction should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperuricemia (the approved indication text is not available in the Singapore licence records; the original indication is taken from the knowledge graph) |
| Predicted New Indication | Hypouricemia, renal |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, febuxostat is a non-purine, selective xanthine oxidase inhibitor that reduces uric acid production. Its efficacy in hyperuricemia is established.

Renal hypouricemia is a condition where serum urate is already low, typically due to loss-of-function of urate transporters such as URAT1 or GLUT9. Further urate lowering is therefore mechanistically counterintuitive and could worsen the condition. The high TxGNN score likely reflects proximity to urate metabolism in the knowledge graph rather than true therapeutic benefit.

The only plausible link is a case-level report on using non-purine xanthine oxidoreductase inhibitors to prevent exercise-induced acute kidney injury in patients with renal hypouricemia. This is a preventive, hypothesis-level rationale and not treatment of hypouricemia itself.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Phase 4 | Unknown | 100 | Prospective controlled study of how uric acid control affects stone recurrence and renal function in patients with calculi and hyperuricemia. Its relevance to renal hypouricemia cannot be verified, so it is not direct evidence. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrative review of hypouricemia (serum urate < 2 mg/dL), covering its causes for practicing rheumatologists. |
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review (classified; reads as a case report) | Internal Medicine | A 16-year-old footballer with familial renal hypouricemia (URAT1 mutations) and recurrent exercise-induced acute kidney injury. Hydration alone failed as prophylaxis, and a xanthine oxidoreductase inhibitor, febuxostat, was considered as a preventive option. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14959P | FEBURIC® FILM COATED TABLETS 80MG | Tablet, film coated | Not stated in the licence record |
| SIN17054P | FEBUGOUT F.C. TABLETS 80MG | Tablet, film coated | Not stated in the licence record |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph relationships, not package insert text): stroke disorder, cerebrovascular disorder, ischemic stroke susceptibility, cerebral infarction, myocardial infarction, coronary thrombosis, and hemoglobinopathy.
- **Drug Interactions**: 22 interactions were recorded; 20 are listed in the data compiled for this report.
  - **Major**: mercaptopurine, azathioprine, leflunomide, teriflunomide.
  - **Moderate**: theophylline and related xanthines (dyphylline, aminophylline, oxtriphylline), methotrexate, naltrexone, tioguanine, clofarabine, epirubicin, trabectedin, brentuximab vedotin, asparaginase, pegaspargase, and interferon beta products.
- **Other**: Hepatic enzyme elevation is a recognized concern with febuxostat, and the mechanism notes advise caution in liver disease.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model scoring and hypothesis-level literature only. The one registered trial is of unclear relevance, and the proposed mechanism (further lowering urate in hypouricemia) runs against the disease biology. Cardiovascular and cerebrovascular contraindication signals add further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (a blocking gap for safety screening)
- Detailed mechanism of action data
- Prospective clinical evidence for the exercise-induced acute kidney injury prevention use in renal hypouricemia
- A risk assessment of cardiovascular and cerebrovascular safety in this population

---

*Other predictions in the data (lower priority):* Partial HPRT deficiency and Lesch-Nyhan syndrome are plausible as symptomatic urate control only, supported by case reports (evidence level L4, "Research Question"). The remaining predictions, including copper-associated cirrhosis, hepatoportal sclerosis, portal vein thrombosis, hepatopulmonary syndrome, hepatic porphyria, and phenylalanine metabolism disorder, have no clinical or literature support and no clear mechanism (evidence level L5, "Hold").
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

