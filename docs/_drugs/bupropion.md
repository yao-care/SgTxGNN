---
layout: default
title: Bupropion
parent: High Evidence (L1-L2)
nav_order: 183
evidence_level: L2
indication_count: 10
---

# Bupropion
{: .fs-9 }

Evidence Level: **L2** | Predicted Indications: **10** 
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

# Bupropion: From Its Registered Use to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Bupropion is marketed in Singapore in two products, WELLBUTRIN SR and CONTRAVE. The registry extract does not record an approved indication for either.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, with **8 matched clinical trials** (1 completed Phase 3 placebo-controlled RCT) and **no supporting publications** in the pack.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. Bupropion is generally understood to inhibit dopamine and norepinephrine reuptake. This is general pharmacology, not data from the pack.

ADHD is commonly explained by a catecholaminergic deficit, and established ADHD medicines act on the same dopamine and norepinephrine pathways. That overlap is the main reason the prediction is plausible. The very high TxGNN score is consistent with this, but it does not replace clinical evidence.

A related prediction, ADHD inattentive type, has no trials or literature of its own and only inherits support from the parent ADHD entry.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00048360](https://clinicaltrials.gov/study/NCT00048360) | Phase 3 | Completed | 162 | 8-week, multicenter, randomized, double-blind, placebo-controlled trial of extended-release bupropion (300-450 mg/day) in adults with ADHD |
| [NCT00936299](https://clinicaltrials.gov/study/NCT00936299) | Phase 4 | Completed | 105 | Bupropion for ADHD in adolescents with substance use disorder |
| [NCT01270555](https://clinicaltrials.gov/study/NCT01270555) | NA | Completed | 32 | Open study of bupropion SR for adult ADHD with recent or current substance use disorders |
| [NCT00061087](https://clinicaltrials.gov/study/NCT00061087) | Phase 2/3 | Completed | 115 | Treatment of adult ADHD in methadone patients (the intervention is not stated, so the link to bupropion is unconfirmed) |
| [NCT00000268](https://clinicaltrials.gov/study/NCT00000268) | NA | Completed | 32 | Cocaine abuse with ADHD (the drug is not confirmed from the title) |
| [NCT04553263](https://clinicaltrials.gov/study/NCT04553263) | Early Phase 1 | Withdrawn | 0 | Relapse prevention in stimulant use disorder with or without ADHD (bupropion and bupropion/naltrexone); no participants enrolled |
| [NCT03326128](https://clinicaltrials.gov/study/NCT03326128) | Phase 2 | Terminated | 12 | High-dose bupropion for smoking cessation (not ADHD) |
| [NCT00330434](https://clinicaltrials.gov/study/NCT00330434) | NA | Withdrawn | 0 | CYP2B6 induction and polymorphism study (pharmacokinetic, not ADHD efficacy) |

The strongest evidence is NCT00048360, a completed Phase 3 placebo-controlled RCT of bupropion in adult ADHD. The other supportive trials are small, open-label, or in comorbid substance-use populations. The last three rows are listed for completeness and do not support efficacy.

---

## Literature Evidence

Currently no related literature available for ADHD.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10983P | WELLBUTRIN SR TABLETS 150 mg | Tablet, film coated | Not recorded in the registry extract |
| SIN16411P | CONTRAVE PROLONGED RELEASE TABLET 8MG/90MG | Tablet, film coated, extended release | Not recorded in the registry extract |

Both products are oral. CONTRAVE is a bupropion/naltrexone combination.

---

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug-interaction records were found in the supplied data.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
One completed Phase 3 placebo-controlled RCT and several smaller studies support bupropion in ADHD, giving evidence level L2. There is no supporting literature, the mechanism data is missing, and safety information has not been reviewed. The other nine predictions (including the ADHD inattentive subtype) have little or no evidence and should stay on Hold.

**To proceed, the following is needed:**
- Obtain and review the HSA package insert for warnings and contraindications. This is a blocking gap.
- Obtain mechanism-of-action data, for example from DrugBank.
- Confirm the results and full design of NCT00048360, and confirm the intervention in NCT00061087.
- Search for published papers on bupropion in ADHD, which the pack does not contain.
- Set safety guardrails for pediatric use and for patients with substance use disorders.
- Confirm the approved indications of the two Singapore licences.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

