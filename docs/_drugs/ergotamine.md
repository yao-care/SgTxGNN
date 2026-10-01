---
layout: default
title: Ergotamine
parent: Medium Evidence (L3-L4)
nav_order: 390
evidence_level: L4
indication_count: 10
---

# Ergotamine
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

# Ergotamine: From Acute Migraine to Migraine with Brainstem Aura

## One-Sentence Summary

Ergotamine is an ergot alkaloid used for the acute treatment of migraine and cluster headache. The TxGNN model predicts it may be effective for **migraine with brainstem aura**, but only **1 clinical trial** (of a different drug, topiramate) and **20 publications** were retrieved, and none address ergotamine in this subtype. The literature also points to a safety concern: ergot products are conventionally cautioned against in brainstem-type aura.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acute migraine (from the literature; the Singapore licence text is blank) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 98.93% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

DrugBank mechanism data is not available in the Evidence Pack. The literature describes ergotamine as highly potent at the 5-HT1B and 5-HT1D receptors (PMID 12558771). These receptors mediate cranial vasoconstriction and inhibit release of pain-related neuropeptides. Ergotamine also acts on adrenergic and dopaminergic receptors. Migraine with brainstem aura is a subtype of migraine, so the model's high score reflects the drug's network proximity to migraine.

The prediction is weak for this specific subtype, for three reasons:

- No evidence in the pack is specific to brainstem aura.
- A report on dihydroergotamine (a close relative) states that it is currently contraindicated in hemiplegic and basilar-type migraine (PMID 20533960).
- Vasoconstrictor drugs raise concern in aura patients because migraine is an independent stroke risk factor (PMID 16097850).

In short, the target is plausible, but the safety signal argues against use.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01799590](https://clinicaltrials.gov/study/NCT01799590) | Phase 2 | Completed | 296 | Long-term safety and efficacy of topiramate (a preventive drug) in Japanese migraine patients. It does not involve ergotamine and does not address brainstem aura (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society update on the evidence for acute migraine drugs. General context, not subtype-specific. |
| [20533960](https://pubmed.ncbi.nlm.nih.gov/20533960/) | 2010 | Clinical report | Headache | Dihydroergotamine in migraine with posterior fossa symptoms. It notes the drug is currently contraindicated in hemiplegic and basilar-type migraine. |
| [16097850](https://pubmed.ncbi.nlm.nih.gov/16097850/) | 2005 | Review | CNS Drugs | Migraine is an independent risk factor for stroke, with implications for migraine treatment. |
| [25841032](https://pubmed.ncbi.nlm.nih.gov/25841032/) | 2015 | Cohort / analysis | Neurology | Examines whether acute treatment outcome differs in migraine with aura versus without aura, using sumatriptan. |
| [25841027](https://pubmed.ncbi.nlm.nih.gov/25841027/) | 2015 | Cohort / analysis | Neurology | Asks whether aura informs migraine severity and treatment response (no abstract available). |
| [1602293](https://pubmed.ncbi.nlm.nih.gov/1602293/) | 1992 | Double-blind crossover trial | J Intern Med | Ergotamine 2 mg suppository versus ketoprofen 100 mg in migraine **without** aura (50 patients). Ketoprofen was found more efficacious. |
| [31213753](https://pubmed.ncbi.nlm.nih.gov/31213753/) | 2018 | Double-blind comparative trial | Hippokratia | Ergotamine-based five-component combination versus sumatriptan in migraine **without** aura. |
| [22211870](https://pubmed.ncbi.nlm.nih.gov/22211870/) | 2012 | Review | Headache | Rescue therapy with triptans, dihydroergotamine and magnesium in emergency and headache clinic settings. |
| [19006559](https://pubmed.ncbi.nlm.nih.gov/19006559/) | 2008 | Review | Headache | Neurogenic basis of migraine. Vasoconstriction may not be the most important mechanism of ergotamines and triptans. |
| [20187861](https://pubmed.ncbi.nlm.nih.gov/20187861/) | 2010 | Review | Expert Rev Neurother | Management of sporadic and familial hemiplegic migraine, a related aura subtype. Clinical trials have not been conducted. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11746P | CAFFOX TABLET (manufacturer: T O Pharma Co Ltd) | Tablet (oral) | Not listed in the source data |

## Safety Considerations

The package insert data (warnings and contraindications) is not available. Please refer to the package insert for safety information.

The following signals come from the retrieved literature and should not be read as label content:

- **Brainstem/hemiplegic aura**: the dihydroergotamine report (PMID 20533960) states that the drug is currently contraindicated in hemiplegic and basilar-type migraine.
- **Vascular risk**: migraine is an independent stroke risk factor (PMID 16097850). Ergotamine side effects reported in the literature include myocardial infarction, limb ischaemia and fibrotic changes (PMID 8825693).
- **Medication-overuse headache**: ergotamine overuse is a recognised cause of chronic daily headache (PMID 41039192).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only supporting signal is the model score. No trial or paper tests ergotamine in brainstem aura, and the available safety literature argues against vasoconstrictor use in this subtype. Ergotamine is already used for migraine generally, so this is not a strong repurposing signal.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap). Confirm whether brainstem or hemiplegic aura is a labelled contraindication.
- DrugBank mechanism-of-action data.
- Any subtype-specific clinical data on ergotamine in brainstem aura, plus a stroke and vascular risk assessment.

Other predicted indications in the pack:
- **Trigeminal autonomic cephalalgia (cluster headache)**: has historical ergotamine use and reviews but no controlled trial (L3, research question).
- **SUNCT**: shows a negative signal, since dihydroergotamine exacerbated attacks (PMID 25667300).
- **Remaining predictions**: L4–L5 evidence only.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

