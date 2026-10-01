---
layout: default
title: Bisoprolol
parent: Low Evidence (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Bisoprolol
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

# Bisoprolol: From Its Established Cardiovascular Use to Malignant Renovascular Hypertension

## One-Sentence Summary

Bisoprolol is a beta-blocker that is currently marketed in Singapore, and the record supplied here does not state its approved indication text.
The TxGNN model predicts it may be effective for **malignant renovascular hypertension**,
but **0 clinical trials** and **0 publications** currently support this specific prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Malignant renovascular hypertension |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Bisoprolol is a cardioselective beta-1 blocker. Beta-1 blockade lowers renin release, and renin-driven blood pressure elevation is central to renovascular hypertension. This makes the prediction mechanistically plausible, but only in a generic way.

The prediction should be read with caution for three reasons:
- Malignant hypertension is a hypertensive emergency, usually managed with parenteral agents, and no trial or publication supports bisoprolol in this setting.
- The original-indication and mechanism fields are empty in the input, so the link cannot be checked against approved-use data.
- The closely related prediction, malignant hypertensive renal disease, has an identical score (99.94%). This suggests both come from the same ontology neighbourhood rather than independent signals. A high graph score is not clinical evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

There are 20 registrations in total. Five main ones are listed below. The approved indication text is not provided in the record.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16300P | BISODAC 2.5 Film-Coated Tablets 2.5MG | Tablet, film coated |
| SIN11349P | CONCOR Tablet 2.5 mg | Tablet, film coated |
| SIN15804P | BLOKBIS Tablet 2.5MG | Tablet |
| SIN15866P | BISOZEN Film Coated Tablet 5MG | Tablet, film coated |
| SIN15865P | BISOZEN Film Coated Tablet 10MG | Tablet, film coated |

All listed products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information. No interaction records were found in the supplied data.

Candidate-specific concerns noted in the evidence pack:
- **Pulmonary hypertension**: beta-blockers are generally used with caution because of the risk of reduced right ventricular output.
- **Prinzmetal (vasospastic) angina**: beta-blockade may leave alpha-mediated coronary vasoconstriction unopposed.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is supported only by a model score, with no trials, no literature and no verified mechanism. Bisoprolol is not established therapy for hypertensive emergencies.

**Other predicted indications, for context:**

| Predicted Indication | Score | Evidence Level | Status |
|------|------|------|------|
| Chronic pulmonary heart disease | 98.63% | L4 | Research question |
| Prinzmetal angina | 94.42% | L4 | Hold |
| Cerebrovascular disorder | 68.13% | L4 | Hold |
| Other entries (malignant hypertensive renal disease, two pulmonary hypertension entries, Braddock syndrome, obsolete ischemic stroke susceptibility, brain stem infarction) | 68.17%–99.94% | L5 | Hold |

- **Chronic pulmonary heart disease** is the most promising secondary candidate. It has 16 trials and 20 publications, but all are indirect, mostly in COPD or heart failure with COPD. This includes a completed Phase 3 RCT in COPD ([NCT03917914](https://clinicaltrials.gov/study/NCT03917914), n=280). No trial enrols patients with the target disease itself.
- **Prinzmetal angina** has one Phase 4 trial ([NCT05294887](https://clinicaltrials.gov/study/NCT05294887), n=132, status unknown, no results). It is not confirmed that bisoprolol is an arm or that vasospastic angina is the population.
- **Cerebrovascular disorder** has only animal studies (PMIDs 33106920, 23441690).
- The 20 publications retrieved for the pulmonary hypertension due to lung disease/hypoxia entry cover general hypoxia biology. They are a keyword-matching artifact and do not count as evidence.

**To proceed, the following is needed:**
- The Singapore package insert (HSA) with warnings and contraindications, and confirmation of the approved indications
- Detailed mechanism of action data (MOA) from DrugBank
- A review of the COPD trial outcomes and safety data (e.g., PMIDs 38762800, 40386836) to judge whether chronic pulmonary heart disease deserves advancement
- The NCT05294887 protocol and arms, to confirm bisoprolol's role and the population
- Mapping of the obsolete stroke-susceptibility term to a current concept before any evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

