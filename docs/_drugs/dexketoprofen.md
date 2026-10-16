---
layout: default
title: Dexketoprofen
parent: Low Evidence (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dexketoprofen: predicted new indication Tendinitis (evidence level L5). Approved use: Not stated in the Singapore registration record"
monitor_inn: "Dexketoprofen"
predicted_indications: ["tendinitis", "fibromyalgia", "myositis fibrosa", "idiopathic granulomatous myositis", "rheumatoid arthritis", "migraine disorder", "headache disorder", "migraine with brainstem aura", "exostosis", "congenital hypotrichosis milia"]
---

# Dexketoprofen
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

# Dexketoprofen: From Acute Pain to Tendinitis

## One-Sentence Summary

Dexketoprofen is a non-steroidal anti-inflammatory drug (NSAID) generally used for short-term relief of mild to moderate acute pain.
The TxGNN model predicts it may be effective for **tendinitis**, but there are **0 clinical trials** and only **1 indirect publication** (a study of general musculoskeletal pain) supporting this specific direction.
Note that the same model output shows much stronger evidence for **migraine** (see the conclusion).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record; generally used for acute mild to moderate pain |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 (no tendinitis-specific study; one indirect study in related musculoskeletal pain) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known pharmacology, dexketoprofen is the active S-(+) form of ketoprofen and acts as a non-selective COX-1/COX-2 inhibitor. Its efficacy in acute pain is established, and mechanistically it may be applicable to tendinitis.

Prostaglandin-driven inflammation and pain are involved in tendon disorders, so an NSAID is a plausible treatment. However, the only supporting paper is an emergency department trial in non-traumatic musculoskeletal pain in general, where tendinitis is mentioned as one possible cause. The link to tendinitis is therefore indirect and unproven.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/) | 2019 | RCT | Am J Emerg Med | Compared IV dexketoprofen with paracetamol for non-traumatic musculoskeletal pain in the emergency department. Tendinitis is cited as one possible cause, but the study is not specific to tendinitis. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12650P | KETESSE TABLET 25 mg | Film-coated tablet (oral) | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
For tendinitis, support is limited to a model prediction plus one indirect study in general musculoskeletal pain, with no tendinitis-specific trials. This is a research question, not a ready candidate.

**To proceed, the following is needed:**
- Tendinitis-specific clinical studies, such as an RCT of oral dexketoprofen against another NSAID or placebo
- Mechanism of action (MOA) data
- The registered indication text and safety information (warnings, contraindications) from the HSA package insert
- Confirmation of route and formulation. The only registered product in Singapore is an oral tablet, while the supporting study used an intravenous form.

**Note on a better-supported candidate:** Among the other predictions for this drug, **migraine** has much stronger evidence: 5 clinical trials (mostly Phase 4, in emergency department acute migraine, including a placebo-controlled trial of 224 patients), a meta-analysis of randomized trials, and several RCTs. This is rated L1 and **Proceed with Guardrails**. Headache disorder also rates L1, but its supporting trials are almost all in migraine. Evaluating migraine first is recommended. Fibromyalgia, rheumatoid arthritis, myositis fibrosa, idiopathic granulomatous myositis, exostosis and congenital hypotrichosis milia are model predictions only (L5) and should stay on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

