---
layout: default
title: Aminophylline
parent: Medium Evidence (L3-L4)
nav_order: 88
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Aminophylline: predicted new indication Migraine disorder (evidence level L4). Approved use: Not recorded in the Singapore license data"
monitor_inn: "Aminophylline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
---

# Aminophylline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Aminophylline: From Respiratory Airway Disease (Label Indication Not Recorded) to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Aminophylline is a methylxanthine drug (a theophylline salt) that is registered in Singapore as an injection, although the approved indication text is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 registered clinical trials** and only **4 publications** (one narrative review, two case reports and one old headache review) supporting this direction.
The evidence is early-stage and should be treated as a research question, not as proof of efficacy.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore license data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L4 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Aminophylline is generally known as a non-selective adenosine receptor antagonist and phosphodiesterase inhibitor. Adenosine signalling is implicated in migraine, including trigeminovascular activation and cerebral vasodilation.

Supporting this, a case report describes a hemiplegic migraine episode triggered by regadenoson, an adenosine A2A receptor agonist. Blocking adenosine could therefore plausibly reduce migraine. A 2023 narrative article proposes that migraine may involve impaired brain energy metabolism with high adenosine levels, and that aminophylline may relieve pain, particularly post-dural headache.

This reasoning is hypothesis-level. The available literature is limited to a narrative article, case reports and an old review, with no controlled trials.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | Pain Management | Proposes that migraine involves high adenosine and impaired brain energy metabolism; aminophylline, an adenosine antagonist, may relieve pain, especially post-dural headache |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | J Nucl Cardiol | Hemiplegic migraine triggered by regadenoson (adenosine A2A agonist); methylxanthines such as aminophylline can reverse its adverse effects |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case report | Can J Cardiol | Syndrome X with "myocardial migraine" attributed to excessive adenosine effect |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | Aggiornamenti Clinicoterapeutici | Historical review of headaches (no abstract available) |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03471P | Aminophylline Injection 0.25 g/10 ml (Atlantic Laboratories Corpn Ltd) | Injection | Not recorded |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction database. Examples include:
  - **Major**: bupropion
  - **Moderate**: famotidine, ranitidine, cimetidine, nizatidine, doxycycline, tetracycline, minocycline, clarithromycin, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - **Minor**: lansoprazole
- **Other safety notes from the prediction review**: In Prinzmetal angina, aminophylline termination of dipyridamole stress has been reported to trigger coronary vasospasm. Methylxanthines may also worsen thyrotoxic symptoms such as tremor. Both are theoretical concerns relevant to patient selection.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The migraine prediction has a high model score and a plausible adenosine-antagonism mechanism. However, there are no registered trials, and the literature consists of one narrative article, case reports and an old review. The package insert warnings and contraindications and the approved indication are also missing, so safety screening cannot be completed.

**To proceed, the following is needed:**
- Singapore package insert (warnings, contraindications, approved indication) from the HSA website
- Detailed mechanism of action data from DrugBank
- A systematic literature review, then a pilot or Phase 2 study in migraine (including post-dural headache)
- A safety plan for the major interaction (bupropion), seizure risk and cardiovascular risk, and for the narrow therapeutic window of methylxanthines

### Other Predicted Indications (Brief Note)

- **Pulmonary hypertension (score 0.9923, L3):** One completed Phase 1 safety and interaction study with ambrisentan (NCT01530464, n=18) and several small, mostly old, haemodynamic studies. No Phase 2/3 RCT. It is the next most-supported prediction after migraine.
- **Migraine with brainstem aura, migraine susceptibility, atrophoderma vermiculata, ulerythema ophryogenesis, sciatic neuropathy, kyphoscoliotic heart disease:** Prediction only, or irrelevant or preclinical literature. Hold.
- **Prinzmetal angina and hyperthyroidism:** The literature suggests possible harm rather than benefit. Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

