---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 770
evidence_level: L5
indication_count: 10
---

# Perampanel
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

# Perampanel: From Epilepsy to Visual Epilepsy

## One-Sentence Summary

Perampanel (DrugBank DB08883) is a selective, non-competitive AMPA-receptor antagonist used globally as an antiseizure medication for focal-onset and primary generalized tonic-clonic seizures. The TxGNN model predicts it may be effective for **Visual Epilepsy** (a photosensitive/visually-induced reflex seizure subtype), with **3 clinical trials** and **19 publications** currently returned as supporting evidence — though none of them specifically studies the visually-induced subtype.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy — focal-onset and primary generalized tonic-clonic seizures (per literature evidence in this pack; drug is not currently registered in Singapore) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

DrugBank's structured mechanism-of-action field for Perampanel is currently a data gap. However, the literature evidence collected in this pack consistently and independently describes Perampanel as a selective, non-competitive antagonist of AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) glutamate receptors — the first antiepileptic drug approved with this mechanism, used in over 35 countries as adjunctive (and in some jurisdictions monotherapy) treatment for focal-onset seizures, with or without secondary generalization, and for primary generalized tonic-clonic seizures.

Visual epilepsy (photosensitive/visually-induced epilepsy) is a reflex epilepsy subtype in which visual stimuli trigger excessive, synchronized cortical discharge originating in the occipital cortex, propagating through AMPA-receptor-mediated excitatory glutamatergic transmission. Since Perampanel's core mechanism is blockade of postsynaptic AMPA-receptor excitation, there is a plausible mechanistic rationale for it dampening the photoparoxysmal response that characterizes this seizure subtype.

That said, the mechanistic link here is theoretical rather than demonstrated. All 3 clinical trials and the great majority of the 19 publications returned for this indication study Perampanel in general epilepsy populations (partial-onset seizures, EEG/cognition effects, neurophysiology testing) rather than in patients with confirmed visual/photic seizure triggers. No trial in this evidence pack was designed around photic stimulation or photoparoxysmal EEG response as an endpoint.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Phase 2 | Completed | 18 | Tolerability, safety and pharmacokinetics of E2007 (perampanel) in epileptic patients with partial and generalised seizures; general population, not visually-induced subtype. |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Phase 4 | Completed | 30 | Effects of perampanel on cognition and EEG in patients with epilepsy; not designed around photic/visual seizure triggers. |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Phase 4 | Completed | 12 | Effects of perampanel on neurophysiology tests (EEG, SEP, BAEP, visual evoked potential) in healthy subjects; explores VEP as a physiological measure, not a visual-epilepsy treatment trial. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematic Review | Brain & Development | Efficacy, tolerability and safety of perampanel in children/adolescents with epilepsy — general population meta-analysis. |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Practice Guideline | Neurology | AAN/AES updated guideline on efficacy/tolerability of newer antiepileptic drugs for new-onset epilepsy. |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Review | Epilepsy & Behavior | Perampanel monotherapy for epilepsy: clinical trial and real-world evidence; confirms AMPA-antagonist mechanism and approved FOS/GTCS indications. |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Review | Expert Opinion on Drug Discovery | Discovery and development of perampanel; first approved AMPA-receptor antagonist antiepileptic, approved in 35+ countries. |
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Pending | Seizure | Systematic review/meta-analysis of RCTs on efficacy and safety of perampanel in epilepsy (general focal/GTC seizure populations). |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Pending | Journal of Neurology | Network meta-analysis of antiseizure medications (incl. perampanel) for idiopathic generalized epilepsies. |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Pending | Neurology | Perampanel efficacy/tolerability with enzyme-inducing AEDs, pooled from 3 Phase 3 trials. |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Pending | BMJ | Management of epilepsy during pregnancy and lactation; general ASM safety context, not subtype-specific. |
| [27935018](https://pubmed.ncbi.nlm.nih.gov/27935018/) | 2017 | Pending | Developmental Medicine & Child Neurology | Tolerability and efficacy of perampanel in children with refractory epilepsy. |
| [37329172](https://pubmed.ncbi.nlm.nih.gov/37329172/) | 2023 | Pending | Annals of Clinical and Translational Neurology | Efficacy of perampanel in pediatric epilepsy with known/presumed genetic etiology. |

None of the 19 returned publications specifically addresses visually-induced/photosensitive epilepsy; all evidence is drawn from general epilepsy populations and extrapolated by mechanism.

---

## Singapore Market Information

Perampanel currently has **0 registered authorizations** in Singapore (`market_status: 未上市` / Not Marketed). No license records, product names, dosage forms, or approved indication text are available from the regulatory data source for this drug.

---

## Safety Considerations

Please refer to the package insert for safety information. (Key warnings, contraindications, and drug-drug interaction data are all marked as data gaps in this evidence pack — notably flagged as a **Blocking** gap (DG001: TFDA/HSA label warnings & contraindications), which prevents completion of the S1 safety pre-screen.)

---

## Conclusion and Next Steps

**Decision: Research Question**

**Rationale:**
The TxGNN score is very high (99.92%) and there is a strong general body of evidence for Perampanel's efficacy and mechanism in epilepsy broadly, but no trial or publication in this pack specifically studies the visually-induced/photosensitive seizure subtype — the mechanistic link remains theoretical (evidence level L4). The drug is also unregistered in Singapore and safety documentation is currently blocked.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001, Blocking — required before any S1 safety screen)
- Confirmed DrugBank mechanism-of-action record (DG002)
- Subtype-specific evidence: trials or case series using photic stimulation / photoparoxysmal EEG response as an endpoint
- Singapore registration pathway assessment, given current "Not Marketed" status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

