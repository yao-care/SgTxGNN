---
layout: default
title: Zopiclone
parent: Low Evidence (L5)
nav_order: 1080
evidence_level: L5
indication_count: 10
---

# Zopiclone
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

# Zopiclone: Predicted Indication — Sleep Disorder (Initiating and Maintaining Sleep)

## One-Sentence Summary

Zopiclone is a hypnotic (sleep medicine) already marketed in Singapore under 3 registrations, although the registration records supplied here do not state an approved indication.
The TxGNN model predicts it is effective for **sleep disorder, initiating and maintaining sleep** (insomnia), with **1 clinical trial** (of the related drug eszopiclone, not yet recruiting) and **20 publications**, mostly general insomnia reviews and meta-analyses.
This is closer to confirming a probable existing use than to true repurposing.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Sleep disorder, initiating and maintaining sleep |
| TxGNN Prediction Score | 98.83% |
| Evidence Level | L3 (see note below) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Proceed with Guardrails |

**Evidence level note:** The upstream pack graded this L2. The only trial listed is Phase 2, has not started recruiting and tests eszopiclone, so it does not meet the L2 rule (one completed Phase 2/3 RCT). The support here is systematic reviews, network meta-analyses and guidelines, which fits L3.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. From general pharmacology, zopiclone is a cyclopyrrolone ("Z-drug") hypnotic. It is a positive allosteric modulator at the benzodiazepine site of the GABA-A receptor, which shortens the time to fall asleep and helps sleep continuity.

The original indication is not recorded: the original-indication field and all three Singapore licence texts are empty. Insomnia is very likely zopiclone's established labelled use. The label should be checked against the HSA record before this is treated as a new indication. Guidelines and reviews in the data (AASM 2017, a European 2025 consensus, network meta-analyses) list zopiclone among the recommended Z-drug hypnotics.

Nine other predicted diseases were also generated. These include encephalopathy, agoraphobia, prion disease and restless legs syndrome. They have no trials or only indirect literature, no plausible mechanistic link, and are all rated Hold. They are not pursued here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not yet recruiting | 15 | Eszopiclone (the active S-enantiomer of zopiclone) vs lemborexant vs placebo in obstructive sleep apnoea with a low arousal threshold and difficulty falling or staying asleep. No results yet. Related drug, narrow subgroup. |

No Phase 3 RCT of zopiclone itself is listed.

---

## Literature Evidence

Of 20 publications supplied, the 10 most relevant are shown. Most address insomnia drugs generally rather than zopiclone alone.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Network meta-analysis (153 RCTs) | Drugs | Compares effectiveness, safety and tolerability of insomnia drugs by class and individual drug |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Network meta-analysis | Lancet | Comparative effectiveness of drug treatments for acute and long-term insomnia in adults |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Systematic review / NMA | Sleep Med Rev | Ranks 20 insomnia drugs on sleep latency, awake time and tolerability in placebo-controlled or head-to-head RCTs |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical practice guideline | J Clin Sleep Med | AASM recommendations for pharmacologic treatment of chronic insomnia, drug by drug |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Expert consensus guideline | Sleep Med | European guidance on switching or deprescribing hypnotics. Lists zopiclone among recommended Z-drugs, with CBT-I as first line |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | Systematic review / meta-analysis of RCTs | Psychiatry Clin Neurosci | Sleep medicines (including Z-drugs) added to antidepressants for depression with insomnia |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacol Rev | Z-drugs (including zopiclone) are approved for insomnia but carry cognitive impairment, tolerance, falls and dependence risks |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | Pharmacological management of insomnia in the elderly |
| [38551874](https://pubmed.ncbi.nlm.nih.gov/38551874/) | 2024 | Review | Rev Prat | Zopiclone and zolpidem, taken at the right time and dose, promote sleep onset with fewer harms than long-acting benzodiazepines |
| [30303519](https://pubmed.ncbi.nlm.nih.gov/30303519/) | 2018 | Cochrane review | Cochrane Database Syst Rev | Eszopiclone for insomnia (related drug) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN05047P | IMOVANE TABLET 7.5 mg (Opella Healthcare International SAS) | Film-coated tablet |
| SIN09355P | APO-ZOPICLONE TABLET 7.5 mg (Apotex Inc) | Film-coated tablet |
| SIN11416P | ZOPICLONE TABLET 7.5 mg (Dragenopharm Apotheker Püschl GmbH & Co KG) | Tablet |

All products are oral. The approved indication text is blank in the supplied records, so no indication column is shown.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the interaction query.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Zopiclone is marketed in Singapore, and guidelines and network meta-analyses support Z-drugs for insomnia, so the main prediction is credible and probably matches existing use. However, no zopiclone-specific Phase 3 RCT is in the data, the one listed trial concerns eszopiclone and has not started, and safety data are missing.

**To proceed, the following is needed:**
- Download and review the HSA package insert for warnings, contraindications and the approved indication. This is currently a blocking gap.
- Confirm whether insomnia is already on the Singapore label, which would make this a label confirmation rather than a new indication.
- Obtain mechanism of action data from DrugBank.
- Apply use guardrails: short duration of use, monitoring for next-day impairment, dependence and falls (especially in older adults), and avoiding combination with other CNS depressants.

*This report is for research reference only and does not constitute medical advice. Predicted candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

