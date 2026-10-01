---
layout: default
title: Acetaminophen
parent: Low Evidence (L5)
nav_order: 29
evidence_level: L5
indication_count: 10
---

# Acetaminophen
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

# Acetaminophen: From Analgesic Use to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen is a widely marketed central analgesic, and its label indication text is not available in the source data.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, with a score of 99.15%.
There are **no clinical trials** and **19 publications** on this direction, all on migraine in general rather than this subtype, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registry data (all retrieved licenses have empty indication text) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 (indirect: general migraine literature only, nothing specific to this subtype) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in DrugBank for this record. From general pharmacology, acetaminophen is a central analgesic. It is thought to act through COX inhibition in the central nervous system and through serotonergic and endocannabinoid pathways. That profile makes it a plausible option for headache pain.

The literature supports acetaminophen, mostly in combination products, for acute migraine in general. It is also cited as first-line symptomatic treatment for headache in pregnancy. However, none of the retrieved publications addresses brainstem aura specifically. The high TxGNN score (0.99) is most likely driven by the parent "migraine" node in the knowledge graph rather than by subtype-specific evidence.

The comparison with the drug's currently approved indication could not be made, because label indication text is missing. Whether migraine is already covered by existing Singapore labels is therefore unverified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT (three double-blind, placebo-controlled trials) | Arch Neurol | Assessed the acetaminophen + aspirin + caffeine combination for relieving migraine headache pain |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT (pooled analysis of 3 trials) | Clin Ther | Same combination studied in menstruation-associated versus non-menstrual migraine |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | RCT (combination product) | Headache | Compared isometheptene/dichloralphenazone/acetaminophen with sumatriptan in mild-to-moderate migraine, with or without aura |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society update on evidence for acute migraine drug therapies |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Status migrainosus, a complication of migraine with or without aura |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurol Clin | Headache in pregnancy; acetaminophen is described as first-line symptomatic treatment |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | Abortive and preventive migraine therapies in pregnancy |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Migraine in pregnancy and breastfeeding, and treatment approach |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurol Int | Acute migraine treatment; notes acetaminophen among non-prescription options |
| [9556832](https://pubmed.ncbi.nlm.nih.gov/9556832/) | 1998 | Review | Schweiz Med Wochenschr | Migraine drug treatment, from mechanisms of action to contraindications |

The RCTs above test combination products, not acetaminophen alone. They also enrolled general migraine populations, not brainstem aura specifically.

## Singapore Market Information

Five of the 20 registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16479P | PANADOL MINI CAPS CAPSULE 500MG | Capsule | Not listed in registry data |
| SIN11299P | PARACIL TABLETS 500 mg | Tablet | Not listed in registry data |
| SIN14871P | PARASUSTAIN SUSTAINED RELEASE TABLETS 665MG | Film-coated extended-release tablet | Not listed in registry data |
| SIN14699P | PANADOL WITH OPTIZORB CAPLET 500MG | Film-coated tablet | Not listed in registry data |
| SIN11120P | PRITAMOL SUPPOSITORIES 125 mg | Suppository | Not listed in registry data |

Other registered forms include suspension, powder and intravenous infusion solution.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on general migraine evidence, and none of it is specific to brainstem aura. No clinical trial evaluates acetaminophen for this subtype. Safety data and label indications are also missing.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently a blocking gap for safety screening)
- Label indication text, to check whether migraine is already an approved use in Singapore
- Mechanism of action data from DrugBank
- Subtype-specific evidence, or a clinical judgement that general migraine evidence can be extended to brainstem aura

**Note on other predictions in this pack:** Among the lower-ranked predictions, **sciatic neuropathy** has the strongest direct evidence (L2). It has two Phase 4 randomized trials of IV paracetamol in emergency-department sciatica (NCT02504996, NCT02777320) and one RCT (PMID 26938140). These are symptom-focused rather than disease-modifying, and a review title in the pack suggests analgesic efficacy in sciatica is contested; that review's findings were not verified here. This candidate may warrant its own evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

