---
layout: default
title: Nifedipine
parent: Medium Evidence (L3-L4)
nav_order: 704
evidence_level: L4
indication_count: 10
---

# Nifedipine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Nifedipine: From Cardiovascular Use to Migraine with Brainstem Aura

## One-Sentence Summary

Nifedipine is a calcium channel blocker with 11 Singapore registrations, and is generally known as a cardiovascular drug.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but there are **0 clinical trials** and only **2 general migraine publications (1992)** for this subtype.
One of those publications is a double-blind trial in which nifedipine did not help acute migraine attacks, so the prediction rests mainly on model scoring.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records (nifedipine is generally known as a cardiovascular drug) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 92.63% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Nifedipine is an L-type calcium channel blocker. The proposed link to migraine is the same as for calcium channel blockers in general: reducing cerebral vasoconstriction and calcium-dependent neuronal excitability. This comes from the literature, not from the provided drug record.

Migraine with brainstem aura is a subtype of migraine. The two retrieved papers (both 1992) address migraine broadly, not this subtype, so the evidence is indirect. The high TxGNN score most likely reflects the parent migraine association in the knowledge graph.

The signals are mixed. A double-blind study found nifedipine was not useful for acute attacks of migraine with aura, and a review concluded that its preventive effect in migraine is not firmly demonstrated. Mechanistic plausibility exists, but there is no evidence for this specific subtype.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1423566](https://pubmed.ncbi.nlm.nih.gov/1423566/) | 1992 | RCT (double-blind) | Cephalalgia | Nifedipine or vehicle for six acute attacks of migraine with aura. Both administration modes increased headache intensity versus vehicle. The authors concluded nifedipine is not useful as an abortive treatment. Not specific to the brainstem aura subtype. |
| [1353873](https://pubmed.ncbi.nlm.nih.gov/1353873/) | 1992 | Review | Pathologie-biologie | Review of controlled studies of calcium antagonists (verapamil, diltiazem, nifedipine) for migraine prevention. Effectiveness cannot be considered firmly demonstrated, given trial design problems. |

## Singapore Market Information

The registration records provided do not include approved indication text. 5 of the 11 registrations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11117P | DEPIN-E RETARD TABLETS 20 mg | Tablet | — |
| SIN08776P | AA PHARMA NIFEDIPINE CAPSULE 10MG | Capsule | — |
| SIN11671P | NIFEDIPINE LA TABLET 30 mg | Tablet, film coated | — |
| SIN07710P | ADALAT LA 30 TABLET 30 mg | Tablet, film coated | — |
| SIN07228P | NIFELAT TABLET 10 mg | Tablet, film coated | — |

## Safety Considerations

- **Drug Interactions**: The interaction query returned no results.
- **Headache signal from related literature**: Papers retrieved for the parent indication (migraine disorder) point to a tolerability concern.
  - Nifedipine is among the drugs most frequently reported with headache in WHO monitoring data (PMID 2759851).
  - In a placebo-controlled crossover trial in classic migraine, side effects occurred in 54% of nifedipine patients versus 8% on placebo (PMID 2644581).
  - In an open-label comparison with propranolol, 45% of nifedipine patients withdrew, mainly for side effects (PMID 2654067).
  - Headache as an adverse effect of a vasodilator is a particular concern in a migraine population.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no trials and no subtype-specific literature. The only controlled study retrieved (a 1992 trial in migraine with aura) was negative for acute treatment, and related studies report frequent side effects, including headache.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (currently blocking the safety screening)
- Mechanism of action data from DrugBank
- Full-text review of the 2025 systematic review on calcium channel blockers in migraine (PMID 40580307), and of the small crossover RCTs retrieved for the parent indication
- Evaluation of the parent indication "migraine disorder" (rank 2), which has 1 completed Phase-N/A pediatric pharmacokinetic study, 1 Phase 2 trial with unconfirmed migraine relevance, and several small RCTs, and is a more realistic research target than this subtype
- Subtype-specific evidence for brainstem aura, if any exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

