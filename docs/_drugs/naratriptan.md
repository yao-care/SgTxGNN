---
layout: default
title: Naratriptan
parent: 僅模型預測 (L5)
nav_order: 692
evidence_level: L5
indication_count: 10
---

# Naratriptan
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

# Naratriptan: From Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Naratriptan is a selective 5-HT1B/1D receptor agonist (triptan) used internationally for the acute treatment of migraine. The TxGNN model predicts a very high association with **migraine with brainstem aura** (formerly basilar-type migraine), but this subtype is a well-recognized **contraindication category for triptans**, and none of the **19 supporting publications** actually study this specific subtype — the signal reflects general migraine efficacy, not evidence for this indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not on file for Singapore (no local license); internationally approved for acute treatment of migraine (with/without typical aura) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Naratriptan is a 5-HT1B/1D receptor agonist that relieves migraine by constricting intracranial (extracerebral) vessels and inhibiting trigeminovascular nociceptive signaling. This mechanism is well established for typical migraine, which is why the TxGNN model assigns an extremely high score (0.9998) to "migraine with brainstem aura" — the two conditions share the same broad diagnostic family and overlapping pathophysiology.

However, this is a case where mechanistic proximity works against, not for, repurposing. Migraine with brainstem aura (previously called basilar-type migraine) involves aura symptoms attributable to brainstem/posterior-circulation dysfunction, and triptans — including naratriptan — are conventionally listed as contraindicated or cautioned against in this subtype because their vasoconstrictive action is theorized to raise the risk of cerebral ischemia in a population where posterior-circulation vasospasm may already be part of the disease process. Patients with this diagnosis are routinely excluded from triptan clinical trials, which is consistent with the complete absence of clinical trial and disease-specific literature evidence in this evidence pack despite the strong general migraine literature base for naratriptan.

In short, the high score reflects the model picking up naratriptan's strong efficacy signal for migraine broadly, without being able to distinguish the safety-relevant boundary between typical migraine and the brainstem-aura subtype.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

*(0 trials found for "Naratriptan" + "migraine with brainstem aura"; all identified clinical trials in the literature relate to general or menstrual migraine, not this subtype.)*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972634](https://pubmed.ncbi.nlm.nih.gov/10972634/) | 2000 | RCT | Clinical Therapeutics | Randomized crossover trial comparing headache recurrence rates between naratriptan and sumatriptan in recurrence-prone migraine patients (general migraine, not brainstem-aura subtype) |
| [10961768](https://pubmed.ncbi.nlm.nih.gov/10961768/) | 2000 | RCT | Cephalalgia | Evaluated naratriptan given during the migraine prodrome to prevent headache onset |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review/Guideline | Headache | American Headache Society evidence assessment updating efficacy ratings for acute migraine pharmacotherapies, including triptans |
| [27910087](https://pubmed.ncbi.nlm.nih.gov/27910087/) | 2017 | Review | Headache | Review of treatment options for menstrual migraine, including triptan use |
| [25100506](https://pubmed.ncbi.nlm.nih.gov/25100506/) | 2014 | Review | Expert Opin Pharmacother | Updated review of hormonal causes, prophylaxis, and treatment strategies for menstrual migraine |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort | Neurology | Found reduced triptan (sumatriptan) efficacy in migraine with aura vs. without aura — relevant cautionary signal for aura subtypes generally |
| [12752749](https://pubmed.ncbi.nlm.nih.gov/12752749/) | 2003 | Cohort/Trial data | Headache | Demographic and clinical characterization of adolescents in the Glaxo Wellcome migraine trials database |
| [14511276](https://pubmed.ncbi.nlm.nih.gov/14511276/) | 2003 | Review/Case series | Headache | Discusses management of intractable migraine attacks using naratriptan |
| [22337860](https://pubmed.ncbi.nlm.nih.gov/22337860/) | 2013 | Review | Cephalalgia | Literature review on whether treating the migraine premonitory phase is a useful management strategy |
| [12498013](https://pubmed.ncbi.nlm.nih.gov/12498013/) | 2002 | Drug profile | Curr Opin Investig Drugs | Comparative pharmacology profile referencing naratriptan among 5-HT1B/1D agonists |

**None of the 19 identified publications specifically study naratriptan in migraine with brainstem aura** — all evidence pertains to general or menstrual migraine populations.

---

## Singapore Market Information

Naratriptan currently has no marketing authorization on file in Singapore (0 registrations; market status: not marketed).

---

## Safety Considerations

- **Key Warning (from mechanistic analysis, not formal labeling data)**: Triptans, including naratriptan, are conventionally contraindicated or cautioned against in migraine with brainstem aura due to theoretical cerebral ischemia risk from vasoconstriction acting on a posterior-circulation-implicated condition. This is the central reason this candidate is not being advanced despite its high TxGNN score.
- Formal Singapore label warnings, contraindications, and drug-drug interaction data are not currently on file for this product.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score reflects naratriptan's strong general migraine efficacy signal rather than evidence supporting use in migraine with brainstem aura specifically. This subtype is conventionally treated as a triptan contraindication/caution category, and no clinical trial or literature evidence addresses safety or efficacy in this population — patients with this diagnosis are typically excluded from triptan trials.

**To proceed, the following is needed:**
- Formal package insert/label data confirming naratriptan's contraindication status for basilar-type/brainstem-aura migraine (currently a blocking data gap — DG001)
- Confirmed DrugBank mechanism-of-action record (currently a data gap — DG002)
- Any future disease-specific safety data for triptans in this subtype before this candidate could be reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

