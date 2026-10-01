---
layout: default
title: Atenolol
parent: Low Evidence (L5)
nav_order: 116
evidence_level: L5
indication_count: 10
---

# Atenolol
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

# Atenolol: From Original Label Indication (Not Documented) to Posterolateral Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-blocker marketed in Singapore under 17 registrations, but the Evidence Pack does not record its original approved indication.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, but **0 clinical trials** and **0 publications** support this specific indication.
The prediction is a graph-based signal only, so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% (model rank 2482) |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Atenolol is a beta-1 selective blocker. Blocking beta-1 receptors lowers heart rate and contractility and reduces myocardial oxygen demand. That is a plausible fit for ischaemia after a heart attack.

The Singapore licence records list no approved indication text, so we cannot tell whether myocardial infarction (MI) is already on the label. If it is, this is a label confirmation rather than true repurposing. The current label should be checked first.

The score of 99.87% reflects the model's graph association, not clinical proof. Posterolateral MI is also one of several closely related MI subtypes that received identical scores (posteroinferior, septal). This suggests the model is predicting an MI-class association rather than a subtype-specific effect.

## Clinical Trial Evidence

Currently no related clinical trials registered for posterolateral myocardial infarction.

One trial found for a neighbouring prediction gives background only:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03278509](https://clinicaltrials.gov/study/NCT03278509) | Phase 4 | Active, not recruiting | 5000 | REDUCE-SWEDEHEART tests whether long-term oral beta-blocker therapy after MI with preserved ejection fraction reduces death or new MI. It is not atenolol-specific, and it addresses whether beta-blockers should continue, not their efficacy in posterolateral MI. |

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

Two records were found for sibling MI predictions. Both are indirect and dated:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | RCT (single-blind, crossover; small) | La Revue de médecine interne | Atenolol 200 mg vs diltiazem 240 mg in 23 patients about 4 weeks after posteroinferior or anterior MI with residual ischaemia, assessed by computerised exercise test. This is an anti-ischaemic comparison, not an outcome trial. |
| [7257500](https://pubmed.ncbi.nlm.nih.gov/7257500/) | 1981 | Cohort (diagnostic imaging) | Zeitschrift für Kardiologie | Thallium-201 stress scintigraphy in 14 patients with coronary artery disease after atenolol 5 mg IV. It is an imaging study, not a therapeutic outcome study. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN10278P | PRENOLOL TABLET 100 mg | Tablet, film coated | Berlin Pharmaceutical Industry Co Ltd |
| SIN07538P | TENOL TABLET 50 mg | Tablet | Sunward Pharmaceutical Private Limited / Sunward Pharmaceutical Sdn Bhd |
| SIN07161P | VASCOTEN 50 TABLET 50 mg | Tablet | Medochemie Ltd |
| SIN02344P | TENOLOL TABLET 100 mg | Tablet, film coated | Ipca Laboratories Ltd |
| SIN10391P | NORMATEN TABLET 100 mg | Tablet, film coated | Xepa-Soul Pattinson (Malaysia) Sdn Bhd |

The pack lists 17 registrations in total, and only these 5 are shown. All are oral. Approved indication text is blank in the records provided.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the query.

One class-level caution applies to this prediction. Beta-blockade in patients with acute or decompensated cardiac dysfunction needs careful assessment. This is general beta-blocker knowledge, not data from the pack.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or literature for this indication. The two indirect MI-related papers are small and dated (1981 and 1985). The original indication is also undocumented, so we cannot tell whether this is repurposing or an existing use.

**To proceed, the following is needed:**
- HSA package insert (warnings, contraindications, approved indications). This is the blocking gap, and it also settles whether MI is already labelled
- Detailed mechanism of action data (e.g. from DrugBank)
- A targeted literature search for atenolol in acute or post-MI populations, including secondary prevention trials and reviews
- Confirmation of the current evidence for long-term beta-blocker use after MI, including the REDUCE-SWEDEHEART results when available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

