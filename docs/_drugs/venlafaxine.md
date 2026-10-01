---
layout: default
title: Venlafaxine
parent: Low Evidence (L5)
nav_order: 1052
evidence_level: L5
indication_count: 10
---

# Venlafaxine
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

# Venlafaxine: From Major Depressive Disorder to Ohdo Syndrome and Variants

## One-Sentence Summary

Venlafaxine is a serotonin-norepinephrine reuptake inhibitor (SNRI) antidepressant, used mainly for major depressive disorder. The TxGNN model ranks **Ohdo syndrome and variants** as its top new-indication prediction. There are **0 clinical trials** and **0 publications** supporting it, so it is most likely a knowledge-graph artifact.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major depressive disorder (the Singapore registration records do not state an indication text) |
| Predicted New Indication | Ohdo syndrome and variants |
| TxGNN Prediction Score | 95.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Venlafaxine blocks the reuptake of serotonin and norepinephrine. This mechanism supports its use in depression, and in anxiety-related disorders such as panic disorder and obsessive-compulsive disorder. Detailed mechanism-of-action data is not available in the Evidence Pack beyond this class-level description.

Ohdo syndrome is a rare genetic developmental disorder, usually linked to KAT6B. It involves structural and intellectual-disability features, not a monoaminergic deficit. No plausible mechanistic link to venlafaxine's pharmacology was identified. The high score (0.959) most likely reflects proximity in the knowledge graph, not pharmacology. The same applies to the closely related entry "blepharophimosis - intellectual disability syndrome, Ohdo type" (rank 3, score 93.79%).

Treat this prediction as a model output with no clinical or literature support.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11435P | EFEXOR XR CAPSULE 75 mg | Capsule | Not stated in records |
| SIN15038P | VENLEX XR CAPSULES 75MG | Capsule, extended release | Not stated in records |
| SIN15039P | VENLEX FORTE XR CAPSULES 150MG | Capsule, extended release | Not stated in records |
| SIN15521P | DEPREVIX MODIFIED RELEASE HARD CAPSULE 150MG | Capsule, delayed release | Not stated in records |
| SIN15520P | DEPREVIX MODIFIED RELEASE HARD CAPSULE 75MG | Capsule, delayed release | Not stated in records |

All products are oral formulations. Two further registrations (7 in total) are not listed here.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials, no publications, and no plausible mechanism. The only support is a high model score, which is not enough to justify further investment in this indication.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are required before any safety screening
- Detailed mechanism-of-action data from DrugBank
- A credible mechanistic hypothesis linking SNRI pharmacology to KAT6B-related disorders, followed by preclinical support

**Other predictions in this Evidence Pack have more support and may be worth reviewing first:**

| Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|------|------|------|
| Melancholia | 88.81% | L2 | Proceed with Guardrails (a subtype within the existing depression indication, not true repurposing) |
| Agoraphobia | 85.25% | L2 | Proceed with Guardrails (strongest when co-occurring with panic disorder; standalone evidence is limited) |
| Dysthymic disorder | 89.14% | L3 | Research Question (open-label studies and a class-level meta-analysis, no venlafaxine-specific RCT) |
| Obsessive-compulsive disorder | 87.34% | L3 | Research Question (mostly open-label and case-level evidence, no confirmed venlafaxine RCT) |

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

