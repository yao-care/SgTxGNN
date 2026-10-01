---
layout: default
title: Ulipristal
parent: Low Evidence (L5)
nav_order: 1029
evidence_level: L5
indication_count: 10
---

# Ulipristal
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

# Ulipristal: From Emergency Contraception to Rheumatoid Arthritis

## One-Sentence Summary

Ulipristal is a selective progesterone receptor modulator, marketed in Singapore as ELLA 30 mg tablets (emergency contraception).
The TxGNN model predicts it may be effective for **rheumatoid arthritis**, but this prediction rests on the model score alone.
Only **1 clinical trial** was found, and it is unrelated to the drug. There are **no publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Emergency contraception (the HSA record has no indication text; this is based on the known use of ELLA 30 mg) |
| Predicted New Indication | Rheumatoid arthritis |
| TxGNN Prediction Score | 90.31% (model rank 34,482) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Ulipristal is a selective progesterone receptor modulator with some anti-glucocorticoid activity. Sex-hormone and glucocorticoid signaling both influence immune regulation, which gives a loose, hypothesis-level link to rheumatoid arthritis (RA).

Currently, detailed mechanism of action data is not available in the Evidence Pack. No RA-specific mechanism or data support the link, and the relationship between the original use (a reproductive-hormone indication) and an autoimmune joint disease is weak. Long-term ulipristal use also carries a hepatotoxicity signal, which is a concern for a chronic indication like RA.

The other nine top predictions (including tendinitis, fibromyalgia, Glanzmann thrombasthenia and several rare congenital syndromes) are also L5 with a Hold recommendation. Most have no plausible mechanism and appear to be knowledge-graph artifacts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04300465](https://clinicaltrials.gov/study/NCT04300465) | N/A | Unknown | 64 | A 12-week community lifestyle program (exercise, education, cardiovascular risk optimisation) in chronic disease patients. It does not test ulipristal and gives no efficacy or safety evidence for RA (relevance grade C). |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13979P | ELLA TABLET 30MG (manufacturer: CENEXI) | Tablet (oral) | Not stated in the registration record |

## Safety Considerations

- **Hepatotoxicity**: Long-term ulipristal use carries a hepatotoxicity signal, which matters for a chronic indication such as RA.

Please refer to the package insert for warnings, contraindications and drug interaction information. No interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score. No relevant trials or publications exist, the mechanistic link is speculative, and the hepatotoxicity signal argues against chronic use.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (blocking for safety screening)
- Detailed mechanism of action data (for example, via the DrugBank API)
- Preclinical or mechanistic evidence for progesterone receptor or glucocorticoid-receptor modulation in RA
- A long-term hepatic safety assessment for chronic dosing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

