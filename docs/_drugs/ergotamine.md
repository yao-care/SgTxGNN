---
layout: default
title: Ergotamine
parent: 僅模型預測 (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Ergotamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Ergotamine: From Migraine and Cluster Headache to Migraine with Brainstem Aura

## One-Sentence Summary

Ergotamine is one of the oldest migraine-specific therapies, historically used for over a century in the acute treatment of migraine and cluster headache.
The TxGNN model predicts it may be effective for **Migraine with Brainstem Aura**,
with **1 clinical trial** and **20 publications** currently supporting this direction — though the clinical literature raises significant safety concerns specific to this subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Migraine and cluster headache (historical use; no Singapore regulatory record) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 98.93% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on published clinical literature, Ergotamine is an ergot alkaloid that acts as a potent agonist at 5-HT1B and 5-HT1D receptors, causing constriction of cranial blood vessels and inhibiting release of vasoactive neuropeptides — including CGRP and substance P — from perivascular trigeminal nerve endings. It also exhibits partial alpha-adrenergic agonist activity, providing additional vasoconstrictive effects. This pharmacological profile has been extensively documented across decades of clinical experience (Silberstein & McCrory, *Headache*, 2003; PMID 12558771).

Migraine with brainstem aura (formerly known as "basilar-type migraine") involves the same fundamental trigeminovascular pathway as common migraine, which explains why TxGNN assigns an extremely high prediction score of 98.93%. The model correctly identifies mechanistic overlap between ergotamine's antimigraine mechanism and this specific subtype.

However, a critical clinical distinction must be acknowledged: migraine with brainstem aura involves dysfunction of the basilar artery and posterior circulation. Ergotamine's potent vasoconstrictive mechanism — the very source of its efficacy in common migraine — could worsen posterior circulation ischemia in these patients. A key piece of literature (PMID 20533960, Whyte et al., *Headache*, 2010) directly addresses this concern, noting that dihydroergotamine (DHE, ergotamine's close structural analogue) "is currently contraindicated in patients with hemiplegic migraine and basilar-type migraine." Most contemporary headache society guidelines extend this caution to ergotamine itself, classifying brainstem aura as a contraindication rather than a supported indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01799590](https://clinicaltrials.gov/study/NCT01799590) | Phase 2 | Completed | 296 | Safety and efficacy of **topiramate** (not ergotamine) in migraine prevention; provides disease context only — not directly relevant to this evaluation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [1602293](https://pubmed.ncbi.nlm.nih.gov/1602293/) | 1992 | RCT | *Journal of Internal Medicine* | Double-blind, placebo-controlled crossover RCT comparing ketoprofen vs **ergotamine** (2 mg suppository) in acute migraine without aura (n=50); ketoprofen found more efficacious |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Systematic Evidence Assessment | *Headache* | American Headache Society updated evidence assessment of acute migraine pharmacotherapies; positions ergotamine within the treatment ladder |
| [20533960](https://pubmed.ncbi.nlm.nih.gov/20533960/) | 2010 | Clinical Review | *Headache* | **Directly relevant:** DHE use in migraine with posterior fossa symptoms; confirms DHE (ergotamine analogue) is contraindicated in basilar-type migraine — the exact subtype predicted here |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Review | *Headache* | Rescue therapy in acute migraine with triptans, DHE, and magnesium in emergency and outpatient settings |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Clinical Study | *Neurology* | Reduced efficacy of sumatriptan (5-HT1B/1D agonist, same class as ergotamine) in migraine **with aura** vs without aura — implies class effect limitations in aura subtypes |
| [25841027](https://pubmed.ncbi.nlm.nih.gov/25841027/) | 2015 | Cohort/Clinical Study | *Neurology* | Whether aura presence informs migraine severity and treatment response; relevant to understanding brainstem aura subtype behavior |
| [16097850](https://pubmed.ncbi.nlm.nih.gov/16097850/) | 2005 | Cohort Study | *CNS Drugs* | Stroke risk in migraine with aura patients; ergotamine's vasoconstrictive properties may compound this risk in posterior circulation variants |
| [8536293](https://pubmed.ncbi.nlm.nih.gov/8536293/) | 1995 | Critical Review | *Cephalalgia* | Sumatriptan mechanism in migraine and cluster headache; parallel review of 5-HT1 agonist class including ergotamine analogues |
| [9009471](https://pubmed.ncbi.nlm.nih.gov/9009471/) | 1997 | Clinical Review | *Headache* | AAN advisory committee guidance on dosing and appropriate use of ergotamine tartrate and DHE across migraine subtypes |
| [19006559](https://pubmed.ncbi.nlm.nih.gov/19006559/) | 2008 | Review | *Headache* | Neurogenic basis of migraine; discusses ergotamine/triptans as vasoactive agents whose primary benefit may be neurogenic rather than purely vascular |

---

## Safety Considerations

**Note based on literature evidence (formal package insert data not available for this evaluation):**

- **Vasoconstrictive risk in posterior circulation:** Ergotamine's alpha-adrenergic and 5-HT1B agonism causes significant cranial vasoconstriction. In migraine with brainstem aura, where the basilar and posterior cerebral arteries are already functionally compromised, this effect may precipitate or worsen ischemia.
- **Medication overuse headache:** Chronic or frequent use of ergotamine is a well-documented cause of rebound/transformation headache, sometimes converting episodic migraine to chronic daily headache (PMID 2259318; PMID 41039192).
- **Peripheral and coronary vasospasm:** Ergotamine carries known risks of peripheral limb ischemia and, rarely, coronary vasospasm with chronic use (PMID 8825693).
- **Contraindication signal:** The literature consistently flags basilar-type / brainstem aura migraine as a contraindication for ergotamine-class drugs (PMID 20533960).

Please refer to the official package insert for the complete list of warnings, contraindications, and drug interactions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the TxGNN model's high confidence score (98.93%), which reflects legitimate mechanistic overlap between ergotamine's antimigraine pharmacology and migraine with brainstem aura, published clinical evidence consistently identifies this specific subtype as a **contraindication** — not a supported indication — for ergotamine and its structural analogues. The evidence level (L3) derives entirely from general migraine literature, not brainstem-aura-specific efficacy data.

**To proceed, the following is needed:**

- Retrieve formal MOA data from DrugBank to complete the mechanistic profile (currently a data gap per DG002)
- Obtain the official product package insert to confirm contraindication language for brainstem aura migraine (currently a blocking data gap per DG001)
- Conduct a targeted systematic review specifically examining ergotamine or DHE outcomes in basilar-type / brainstem aura migraine patients
- Consult current International Headache Society and American Headache Society guidelines to determine whether any subpopulation might be eligible
- Consider formally reclassifying this TxGNN prediction as a **negative repurposing signal** (mechanistically plausible but clinically contraindicated), and instead direct attention to **Rank 2 (Headache Disorder, L1 evidence, "Proceed with Guardrails")** and **Rank 7 (Trigeminal Autonomic Cephalalgia, L2 evidence)** as higher-priority repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

