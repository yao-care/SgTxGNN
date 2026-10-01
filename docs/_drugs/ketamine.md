---
layout: default
title: Ketamine
parent: Medium Evidence (L3-L4)
nav_order: 560
evidence_level: L3
indication_count: 10
---

# Ketamine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Ketamine: From Anaesthesia to Headache Disorder

## One-Sentence Summary

Ketamine is an injectable drug marketed in Singapore, and it is generally known as an anaesthetic and analgesic agent. The registration records in this Evidence Pack do not state an approved indication.
The TxGNN model predicts it may be effective for **headache disorder**, and the pack links it to **39 registry hits**, of which only a handful are headache-specific, plus **20 retrieved publications**.
The evidence is mostly small, early-phase or observational work in migraine and cluster headache, so it supports a research question and not a treatment recommendation.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in DrugBank for this record. The mechanism below is inferred from the literature. Ketamine blocks NMDA-type glutamate receptors. Glutamate signalling and central sensitization are thought to contribute to several headache disorders, so blocking these receptors could plausibly reduce pain. Reviews also describe ketamine suppressing cortical spreading depolarization, a process linked to migraine aura.

"Headache disorder" is a broad umbrella term, so the real evidence sits with specific subtypes. The headache-specific clinical data are:
- a retrospective cohort of intravenous lidocaine and ketamine infusions;
- small trials in acute migraine and cluster headache;
- reviews.

Most other registry hits are perioperative pain or depression trials that matched only on pain-related terms. Subtype-level records in the same pack point the same way. There is a small placebo-controlled RCT of intranasal ketamine in migraine with prolonged aura. One ED trial was titled "Low-dose Ketamine Does Not Improve Migraine in the Emergency Department". The mechanistic case is therefore reasonable, but clinical benefit is unproven.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Recruiting | 90 | Single infusion of ketamine plus magnesium sulfate in refractory chronic cluster headache; no results yet |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | Multicentre placebo-controlled RCT of high-dose IV ketamine for chronic daily headache (KetHead); no results yet |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | Intranasal sub-dissociative ketamine vs standard care for primary headache in the ED (THINK); results not in pack |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | N/A | Completed | 34 | Placebo-controlled RCT of sub-dissociative ketamine for acute migraine-type headache in the ED |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | Low-dose ketamine vs prochlorperazine for ED headache (CHECK); results not in pack |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept intranasal ketamine in chronic cluster headache; open-label, uncontrolled |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs ketorolac for acute tension-type headache in the ED |
| [NCT06608277](https://clinicaltrials.gov/study/NCT06608277) | Phase 2 | Recruiting | 175 | Ketamine and/or stellate ganglion block for traumatic brain injury-associated headache and PTSD |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine plus aspirin vs rimegepant for acute headache in the ED; too small for inference |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective cohort | Front Neurol | Efficacy, duration and safety of inpatient IV lidocaine and ketamine infusions for headache disorders |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Drug treatment of cluster headache, covering acute and preventive options |
| [32189074](https://pubmed.ncbi.nlm.nih.gov/32189074/) | 2020 | Review | Curr Neurol Neurosci Rep | ED and inpatient management of headache in adults |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Curr Neurol Neurosci Rep | ED and inpatient management of headache in children and adolescents |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Trigeminal neuralgia pharmacotherapy; ketamine mentioned as a possible adjuvant |

The other retrieved publications are mainly about depression (ketamine and esketamine) or complex regional pain syndrome, so they do not bear on headache.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05966P | Ketamine Hydrochloride Injection USP | Injection | PANPHARMA GmbH |
| SIN15402P | Ketamine Hameln Injection 50 mg/ml | Injection, solution | Siegfried Hameln GmbH |

Approved indication text is not recorded for either licence. Both products are injectable only.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high and the NMDA-related mechanism is plausible. However, the headache-specific evidence is small, early-phase or observational, and the key Phase 3 trials are still recruiting. There is also no completed Phase 3 RCT, and safety data is missing from the pack. Ketamine is best treated as a research question, possibly a refractory or rescue option, and not a standard headache therapy.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which block any safety screening
- Detailed mechanism-of-action data from DrugBank
- Results from the ongoing and completed headache trials, especially NCT05306899, NCT04814381 and NCT03081416
- A specific target subtype (for example refractory chronic migraine or chronic cluster headache) in place of the broad "headache disorder" label
- A route and dosing review, since Singapore products are injectable while several trials use intranasal or oral ketamine
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

