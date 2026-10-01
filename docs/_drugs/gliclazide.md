---
layout: default
title: Gliclazide
parent: Low Evidence (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Gliclazide
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

# Gliclazide: From Type 2 Diabetes to Classic Stiff Person Syndrome

## One-Sentence Summary

Gliclazide is a sulfonylurea that stimulates insulin release, and it is used to treat type 2 diabetes. This use comes from the drug's class, because the Singapore licence text provided does not state an indication.
The TxGNN model predicts it may be effective for **classic stiff person syndrome**, with a high graph score of 97.96%.
There are currently **0 clinical trials** and **0 publications** supporting this direction, so this is a model prediction only and the mechanistic link looks weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (based on drug class; the Singapore licence text provided is empty) |
| Predicted New Indication | Classic stiff person syndrome |
| TxGNN Prediction Score | 97.96% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 17 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack. Based on general pharmacology, gliclazide blocks the K-ATP channel (SUR1/Kir6.2) on pancreatic beta cells. This closes the channel and triggers insulin secretion. The drug has no known effect on GABAergic or spinal inhibitory pathways, which are the systems involved in stiff person syndrome.

The most likely reason for the prediction is an indirect association in the knowledge graph. Stiff person syndrome is linked to anti-GAD65 autoimmunity, and it often co-occurs with type 1 diabetes. This is a comorbidity relationship, not a therapeutic target. The related entry "focal stiff limb syndrome" has exactly the same score (97.96%). The two entries therefore look like near-duplicate nodes and should not be counted as independent signals.

**Conclusion:** the high score reflects graph proximity, not pharmacological plausibility. Nothing in the data supports a clinical benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

There are 17 registrations in total. The first 5 are listed below. All are oral tablets, and the approved-indication text is blank in the data provided.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN08529P | Glyclazide Tablet 80 mg | Tablet | Sam Chun Dang Pharm Co Ltd |
| SIN13468P | Apo-Gliclazide Tablet 80 mg | Tablet | Apotex Inc. |
| SIN09350P | Sun-Glizide Tablet 80 mg | Tablet | Sunward Pharmaceutical Private Limited |
| SIN11662P | Melicron Tablet 80 mg | Tablet, film coated | Xepa-Soul Pattinson (Malaysia) Sdn Bhd |
| SIN14258P | Apo-Gliclazide MR Tablet 30 mg | Tablet, extended release | Apotex Inc. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical or preclinical support (L5), and no plausible mechanism links a K-ATP channel blocker to stiff person syndrome. The high score most likely comes from a diabetes and GAD-autoimmunity association in the graph.

**Other predicted candidates (all L5, no trials or literature):**

| Rank | Predicted Indication | Score | Recommendation | Assessment |
|------|------|------|------|------|
| 2 | Focal stiff limb syndrome | 97.96% | Hold | Same weak link as rank 1; near-duplicate node |
| 3 | Thiamine-responsive dysfunction syndrome | 97.79% | Research Question | Most plausible candidate. It involves diabetes from beta-cell dysfunction (SLC19A2 defect), so a secretagogue could be relevant to the diabetic component only, not to the anemia or deafness |
| 4 | Opsismodysplasia | 97.72% | Hold | No mechanistic connection; likely a graph artifact |
| 5 | Pancreatic agenesis | 96.64% | Hold | Gliclazide needs functional beta cells, so it is unlikely to work |
| 6–9 | Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic) | 95.93–96.43% | Hold | No action on adipocyte biology; likely a lipodystrophy cluster effect |
| 10 | Autoimmune oophoritis | 88.15% | Hold | Likely an autoimmune polyglandular syndrome association; no clinical support |

**To proceed, the following is needed:**
- The Singapore package insert (HSA warnings and contraindications), which is currently missing and blocks safety screening.
- Detailed mechanism of action data from DrugBank.
- A targeted literature search for thiamine-responsive dysfunction syndrome (rank 3), for example reported sulfonylurea responses in diabetes linked to thiamine-responsive megaloblastic anemia (TRMA), before any further staging.
- No further work is recommended for the stiff person syndrome entries unless new mechanistic or clinical evidence emerges.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

