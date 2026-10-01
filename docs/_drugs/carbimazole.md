---
layout: default
title: Carbimazole
parent: Low Evidence (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Carbimazole
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

# Carbimazole: From Antithyroid Therapy to Resistance to Thyroid Hormone (THRB Mutation)

## One-Sentence Summary

Carbimazole is an antithyroid drug that lowers thyroid hormone production, and it is marketed in Singapore.
The TxGNN model predicts it may be effective for **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTH-beta)**.
This prediction has **no clinical trials** and **1 publication** behind it, and that publication is a diagnostic case report, not treatment evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism (antithyroid use per the published literature; the HSA records contain no indication text) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the record. Carbimazole is known to act as an antithyroid drug that blocks thyroid peroxidase, and so reduces thyroid hormone synthesis. Its efficacy in thyroid overproduction states such as Graves' disease is well established.

The high score (0.997) is most likely a graph artifact from shared thyroid-axis nodes, and the mechanism does not fit RTH-beta. In RTH-beta the receptor is insensitive to thyroid hormone, and TSH and thyroid hormone levels are both raised. Blocking hormone synthesis could push TSH higher and enlarge the goitre. The single paper found (PMID 24165508) describes a man treated intermittently with carbimazole for about 10 years after a misdiagnosis of hyperthyroidism. It shows why the diagnosis matters, not that carbimazole helps. Carbimazole is potentially inappropriate for this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report | BMJ Case Reports | A young man with persistently high free T4 and non-suppressed TSH was treated intermittently with carbimazole for a decade before the picture was recognised as a diagnostic differential. It is not evidence of benefit. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06923P | Carbimazole 5 Tablet 5 mg (Remedica Ltd) | Film-coated tablet | Not recorded |
| SIN04453P | Carbimazole Tablet 5 mg (Sunward Pharmaceutical Private Limited) | Tablet | Not recorded |
| SIN04490P | Camazol Tablet 5 mg (Xepa-Soul Pattinson (Malaysia) Sdn Bhd) | Tablet | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. The one paper is a diagnostic case, and the mechanism argues against benefit, since further suppression of hormone synthesis may raise TSH and worsen goitre in RTH-beta.

Other predicted indications in the same pack look more promising:
- **Neonatal thyrotoxicosis** (L3): 20 publications, mostly reviews, case reports and small cohorts, with no registered trials.
- **Autoimmune thyroid disease** (L3): 4 registered trials and Graves' disease literature. This use is probably already labelled, so it may not be true repurposing. The evidence level could move to L1 if the carbimazole arm of NCT03303053 is confirmed.
- **Hashimoto thyroiditis** (L3): the literature includes a small placebo-controlled study, but it is a pilot-level signal.
- **Hyperthyroxinaemia** (L4): only case reports and reviews, and the indication would need narrowing to thyroid-overproduction causes.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- For RTH-beta, a specialist review of whether any rationale exists. Otherwise, redirect effort to the stronger candidates above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

