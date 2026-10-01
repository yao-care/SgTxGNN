---
layout: default
title: Sumatriptan
parent: Medium Evidence (L3-L4)
nav_order: 935
evidence_level: L4
indication_count: 10
---

# Sumatriptan
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

# Sumatriptan: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Sumatriptan is a 5-HT1B/1D agonist, marketed in Singapore for acute migraine. The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**, a subtype of the condition it already treats. Currently **0 clinical trials** and **18 publications** (mostly reviews, none specific to this subtype) are linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine (the HSA records provided carry no indication text, so this comes from the pack's rationale) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism data is not recorded in the drug entry. The pack's rationale describes sumatriptan as a 5-HT1B/1D agonist. Its antimigraine action is attributed to constriction of cranial blood vessels and inhibition of trigeminal neuropeptide release, including CGRP.

Migraine with brainstem aura is a subtype of migraine with aura. This is therefore an extension within the existing use, not true repurposing. The very high score (99.74%) most likely reflects the disease's closeness to migraine in the knowledge graph. It does not show that sumatriptan works or is safe in this subtype.

There is also a safety concern. Vasoconstrictive triptans are conventionally cautioned against in basilar/brainstem-aura and hemiplegic migraine. The older literature on triptans in basilar migraine is a review of case experience, not a controlled trial. A 2015 *Neurology* paper reports reduced sumatriptan efficacy in migraine with aura compared with migraine without aura.

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific subtype.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1313746](https://pubmed.ncbi.nlm.nih.gov/1313746/) | 1992 | RCT (per abstract) | Cephalalgia | Double-blind, placebo-controlled trial of oral sumatriptan 200 mg in acute migraine with aura. The abstract is truncated and gives no results. |
| [23657930](https://pubmed.ncbi.nlm.nih.gov/23657930/) | 2014 | RCT | Phytother Res | 100 patients with migraine without aura received ginger or sumatriptan. Sumatriptan is the comparator, and the population is not aura. |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society update on the evidence for acute migraine drugs. General, not subtype-specific. |
| [11903526](https://pubmed.ncbi.nlm.nih.gov/11903526/) | 2001 | Review | Headache | Reports on triptan use in basilar migraine and migraine with prolonged aura. This is the most directly relevant item, but the abstract is only one line. |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Study (type not classified) | Neurology | Asks whether acute treatment outcomes differ between migraine with aura and without aura. The title reports reduced sumatriptan efficacy with aura. |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handb Clin Neurol | Status migrainosus as a complication of migraine with or without aura. |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Treatment options for menstrual migraine. |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Migraine treatment approaches in pregnancy and breastfeeding. |
| [8559405](https://pubmed.ncbi.nlm.nih.gov/8559405/) | 1996 | Commentary (type not classified) | Neurology | Subcutaneous sumatriptan and the migraine aura. No abstract available. |
| [39391443](https://pubmed.ncbi.nlm.nih.gov/39391443/) | 2024 | Case report | Cureus | Migraine with aura accompanied by myoclonus. Not drug-specific. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN06744P | Imigran Injection 6 mg/0.5 ml | Injection |
| SIN13667P | Sumatran Tablet 50 mg | Tablet |
| SIN17179P | Sumason Tablets 50 mg | Tablet, film coated |
| SIN08419P | Imigran Tablet 50 mg | Tablet, film coated |

Approved indication text was not provided for any of these licenses.

## Safety Considerations

- **Clinical caution (from the pack's rationale)**: Triptans are conventionally cautioned against in basilar/brainstem-aura and hemiplegic migraine. Cardiovascular safety, including acute myocardial infarction, is a known concern in the sumatriptan literature.

No warnings, contraindications or drug interaction data were available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials exist for this subtype, and the supporting literature is general migraine reviews. Triptans carry a conventional caution in brainstem-aura migraine, so the 99.74% score cannot be read as support for use.

**To proceed, the following is needed:**
- The package insert warnings and contraindications from HSA (currently a blocking gap)
- Mechanism of action data from DrugBank
- Subtype-specific clinical or safety evidence for brainstem aura migraine
- A cardiovascular and neurological risk screening plan

**Related candidates from the same pack:**
- **Headache disorder**: L1, Proceed with Guardrails. Phase 3 trials NCT00387881 and NCT00573170 appear to be Treximet (sumatriptan/naproxen) studies. The interventions need confirming, and this is largely an on-label use.
- **Trigeminal autonomic cephalalgia**: L2, Proceed with Guardrails. Cluster headache studies include NCT00356603 and NCT00399243, with no confirmed Phase 3 RCT.
- **Sciatic neuropathy**: L4, Research Question. The only evidence is a rat study of vincristine-induced neuropathy.
- **Remaining candidates**: Held at L5 (prediction only).
  - Atrophoderma vermiculata
  - Ulerythema ophryogenesis
  - Tendinitis
  - Obsolete vascular headache (an obsolete term that should be merged with the headache and migraine entries)
  - Idiopathic granulomatous myositis
  - Myositis fibrosa

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

