---
layout: default
title: Pregabalin
parent: Low Evidence (L5)
nav_order: 824
evidence_level: L5
indication_count: 6
last_modified_at: 2026-11-12
monitor_inn: "Pregabalin"
predicted_indications: ["tendinitis", "idiopathic granulomatous myositis", "myositis fibrosa", "inclusion body myositis", "migraine disorder", "migraine with brainstem aura"]
description: "Pregabalin: predicted new indication Tendinitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Pregabalin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Pregabalin: Tendinitis
{: .text-alpha }

## One-Sentence Summary

Pregabalin was originally used for anxiety disorder, fibromyalgia, myofascial pain syndrome and postherpetic neuralgia.
The TxGNN model predicts it may be effective for **tendinitis**, but **no clinical trials** and **no direct publications** currently support this specific use.
The literature found is only indirectly related, so this prediction rests mainly on the computational score.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Tendinitis |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 63 of 63) |
| Number of Registrations | 63 (valid: 63) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the compiled data. Pregabalin is known to bind the alpha2-delta subunit of voltage-gated calcium channels. This reduces the release of excitatory neurotransmitters, which may help the neuropathic or centrally sensitized components of pain.

Its original indications (fibromyalgia, myofascial pain, postherpetic neuralgia) are all chronic pain conditions. Tendinitis is a musculoskeletal pain condition, so the model may be picking up this shared pain pathway. Pregabalin could plausibly help where tendon pain has a nerve-related or centrally amplified component.

However, there is **no direct evidence in tendinitis**. The mechanistic link is a hypothesis, not a demonstrated effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of these publications studies pregabalin in tendinitis itself. All are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34052386](https://pubmed.ncbi.nlm.nih.gov/34052386/) | 2022 | RCT | Arthroscopy | Perioperative oral pregabalin gave postoperative pain scores equivalent to interscalene nerve block after arthroscopic rotator cuff repair. This is a surgical pain setting, not tendinitis. |
| [32839073](https://pubmed.ncbi.nlm.nih.gov/32839073/) | 2021 | Retrospective cohort | J Orthop Sci | Analgesic and opioid-sparing effect of pregabalin after rotator cuff repair. The abstract notes prior results on opioid sparing were conflicting. |
| [37051935](https://pubmed.ncbi.nlm.nih.gov/37051935/) | 2023 | Case report | Pain Pract | Posterior femoral cutaneous nerve impingement after a marathon, linked to hamstring tendonitis. Does not test pregabalin. |
| [41017607](https://pubmed.ncbi.nlm.nih.gov/41017607/) | 2025 | Case report | Praxis | Fluoroquinolone-associated disability after ciprofloxacin, including tendon problems. An adverse-effect report, not a treatment study. |
| [40818536](https://pubmed.ncbi.nlm.nih.gov/40818536/) | 2025 | Editorial | Arthroscopy | Piriformis syndrome diagnosis and treatment by sciatic neurolysis and piriformis tendon release. Not about pregabalin. |
| [39703364](https://pubmed.ncbi.nlm.nih.gov/39703364/) | 2024 | Preclinical | Adv Pharmacol Pharm Sci | A plant extract reduced vincristine-induced neuropathy in rats. Not about pregabalin or tendinitis. |

---

## Singapore Market Information

The licence records contain no approved indication text. Five examples:

<!-- review:begin sg-lic-20261106-pregabalin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Pregabalin has 20 valid single-ingredient licences in Singapore, all oral capsules. The licence records contain no approved indication text." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 63 registrations for this drug, 63 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-pregabalin-1 -->

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN13094P | Lyrica Capsule 25mg | CAPSULE | Valid |
| SIN13095P | Lyrica Capsule 50mg | CAPSULE | Valid |
| SIN13096P | Lyrica Capsule 75mg | CAPSULE | Valid |
| SIN13097P | Lyrica Capsule 150mg | CAPSULE | Valid |
| SIN13098P | Lyrica Capsule 100mg | CAPSULE | Valid |

Showing 5 of 63 HSA registrations.

<!-- licenses:end -->

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (from the TxGNN knowledge graph, not from label text): thrombocytopenia, angioedema (including hereditary, acquired and RAAS-blocker-induced forms), myopathy and muscle diseases (including rhabdomyolysis and familial periodic paralysis), impaired renal function, and atrioventricular block. The graph also lists anxiety disorder and related neurotic and dysthymic disorders, which is unexpected given pregabalin's original use and should be verified against the label.
- **Drug Interactions**: 100 interaction records were found; 20 were reviewed.
  - **Major**: morphine and liposomal morphine, which carry additive CNS and respiratory depression concerns.
  - **Moderate**: opioid and cannabinoid-type agents (opium, difenoxin, diphenoxylate, dronabinol, nabilone), metoclopramide, thiazolidinediones (pioglitazone, rosiglitazone, troglitazone), and sibutramine.
  - Several other interactions have unknown severity.

Please refer to the package insert for full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 0.9971 TxGNN score is a computational prediction only. No clinical trials exist for tendinitis, and the few publications found are indirect (post-surgical pain, case reports, an editorial, and a rat study). The mechanistic link through pain modulation is plausible but unproven.

**To proceed, the following is needed:**
- Clinical studies of pregabalin in tendinitis or tendinopathy, preferably randomized and placebo-controlled
- Detailed mechanism of action data
- Package insert warnings and contraindications for Singapore-registered products
- A defined patient population (for example, tendon pain with neuropathic or centrally sensitized features) and a safety plan covering sedation, dizziness, falls, renal dosing and opioid co-use

**Note:** Two other TxGNN predictions for pregabalin have much stronger supporting evidence than tendinitis. They may be better candidates to evaluate first.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Pregabalin has 20 valid single-ingredient licences in Singapore, all oral capsules" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

