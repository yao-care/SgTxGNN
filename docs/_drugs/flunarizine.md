---
layout: default
title: Flunarizine
parent: Low Evidence (L5)
nav_order: 439
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Flunarizine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not stated in the licence records (both approved indication fields ar…"
monitor_inn: "Flunarizine"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "atrophoderma vermiculata", "ulerythema ophryogenesis", "common cold", "insomnia (disease)"]
---

# Flunarizine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Flunarizine: From Unspecified Registered Indication to Migraine Disorder

## One-Sentence Summary

> Flunarizine is a calcium channel blocker with antihistaminic activity. The Singapore licence records compiled for this report do not state an approved indication.
> The TxGNN model predicts it may be effective for **migraine disorder**, which is already its established use as a migraine prophylactic in many countries, and so is an on-label use rather than true repurposing.
> Currently **14 clinical trials** and **20 publications** are listed for this direction, but most trials are comparator or indirect studies, and the completed trials do not clearly demonstrate efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the licence records (both approved indication fields are empty) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 (as assigned in the data compiled for this report; see the note in the clinical trial section) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Based on the pharmacology compiled for this report, flunarizine is a selective calcium entry blocker with antihistaminic activity. It acts on T-type calcium channels (Cav3.1, Cav3.2, Cav3.3) and the D2 receptor. It is thought to reduce cortical spreading depression and neuronal hyperexcitability, both of which underlie migraine.

The record lists no original indication, so the migraine link comes from marketed use elsewhere rather than from the source record. Pharmacology data describe its main clinical use as migraine prophylaxis in a large number of countries. It is not FDA-approved. A 2023 European Headache Federation meta-analysis describes it as a repurposed first- or second-line migraine preventive.

Several related predictions (migraine with brainstem aura, headache disorder, susceptibility labels) fall in the same disease family. They mostly rest on migraine evidence rather than data specific to those entries.

## Clinical Trial Evidence

The first 10 of the 14 registered trials are shown below. None is a completed Phase 3 trial, and no results are reported in the data compiled. The L1 grade therefore looks generous. The supporting literature (meta-analyses, guidelines) is stronger than the registered trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not yet recruiting | 460 | PREMI: primary-care comparison of amitriptyline, flunarizine, topiramate and propranolol for migraine prevention |
| [NCT07655700](https://clinicaltrials.gov/study/NCT07655700) | Phase 4 | Not yet recruiting | 177 | Propranolol vs flunarizine vs combination for migraine prophylaxis |
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Flunarizine 10 mg/day vs topiramate 50 mg/day for chronic migraine prophylaxis |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | NA | Completed | 120 | Greater occipital nerve block vs topiramate vs flunarizine in episodic migraine |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | NA | Unknown | 84 | Flunarizine vs amitriptyline for migraine prophylaxis |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | NA | Recruiting | 44 | Flunarizine vs propranolol in children aged 8-15 (PedMIDAS) |
| [NCT07751497](https://clinicaltrials.gov/study/NCT07751497) | Phase 2 | Not yet recruiting | 400 | Rimegepant vs flunarizine non-inferiority in vestibular migraine prevention |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Active, not recruiting | 60 | Pulsed radiofrequency vs calcium channel blockers in childhood migraine |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Pharmacokinetic interaction of flunarizine and topiramate (safety/DDI, not efficacy) |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | Not yet recruiting | 60 | Fu's subcutaneous needling vs flunarizine in migraine without aura |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37723437](https://pubmed.ncbi.nlm.nih.gov/37723437/) | 2023 | Meta-analysis | J Headache Pain | EHF systematic review and meta-analysis rating the evidence for flunarizine, a repurposed first- or second-line migraine preventive |
| [42673583](https://pubmed.ncbi.nlm.nih.gov/42673583/) | 2026 | Systematic review / guideline | Headache | AAN/AHS systematic review of pharmacologic migraine prevention in adults |
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | Systematic review | Health Technol Assess | Preventive drugs for chronic migraine, with economic modelling |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | Network meta-analysis | JAMA Netw Open | Efficacy and safety of preventive medications in pediatric migraine |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | Guideline | Neurology | AAN/AHS update on pharmacologic prevention of pediatric migraine |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | Meta-analysis | J Assoc Physicians India | Amitriptyline vs propranolol and flunarizine for migraine prophylaxis |
| [37073858](https://pubmed.ncbi.nlm.nih.gov/37073858/) | 2023 | Systematic review | Cochrane Database Syst Rev | Pharmacological prophylaxis of vestibular migraine |
| [1393843](https://pubmed.ncbi.nlm.nih.gov/1393843/) | 1992 | RCT | Can J Neurol Sci | Double-blind trial of flunarizine 10 mg daily vs propranolol in 94 patients; both reduced migraine frequency |
| [1889980](https://pubmed.ncbi.nlm.nih.gov/1889980/) | 1991 | Review | Headache | Minireview: controlled studies, including placebo-controlled ones, establish flunarizine efficacy in migraine prophylaxis |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | Clinical study | Acta Neurol Scand | Flunarizine plus supraorbital neurostimulation vs either alone for migraine prophylaxis |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08250P | FORKNOW TABLET 10 mg | Tablet | Not stated in the licence record |
| SIN09449P | POLI-FLUNARIN CAPSULE 5 mg | Capsule | Not stated in the licence record |

## Safety Considerations

Please refer to the package insert for safety information.

The following is limited to the drug-target data compiled for this report; no drug-drug interaction records were returned. Flunarizine acts on the D2 receptor and on the Cav3.1, Cav3.2 and Cav3.3 calcium channels.

Related literature notes the following, which should be confirmed against the package insert:
- Extrapyramidal disturbances and depression are known side effects with chronic use.
- A pharmacokinetic study with topiramate has been registered (NCT00752466), but its results are not available in the data compiled.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Migraine prophylaxis is flunarizine's established use in many countries, and meta-analyses and guidelines support it. The registered trials are mostly comparator or ongoing studies without reported results. The Singapore licences list no approved indication, and no package insert safety data are available.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- The approved indication wording for the two Singapore licences
- Confirmation of the mechanism of action from DrugBank
- Reported results from completed head-to-head trials (e.g., NCT02639598, NCT03712917)
- A safety monitoring plan for depression and extrapyramidal symptoms, especially in elderly and pediatric patients

**Other predicted indications:**
- Headache disorder: Proceed with Guardrails, but it largely overlaps with migraine.
- Migraine with brainstem aura, migraine susceptibility and trigeminal autonomic cephalalgia: research questions only (L4), with no registered trials. For trigeminal autonomic cephalalgia the support is case reports only.
- Nephrogenic syndrome of inappropriate antidiuresis, atrophoderma vermiculata, ulerythema ophryogenesis, common cold and insomnia: Hold. These are prediction-only signals with no supporting evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

