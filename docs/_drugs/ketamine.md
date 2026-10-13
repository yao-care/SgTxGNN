---
layout: default
title: Ketamine
parent: Low Evidence (L5)
nav_order: 565
evidence_level: L5
indication_count: 10
---

# Ketamine
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

# Ketamine: From Anaesthesia/Analgesia to Headache Disorder

## One-Sentence Summary

Ketamine is an injectable NMDA-receptor-blocking drug that is registered in Singapore as two single-ingredient injection products. The approved indication text is not available in the data compiled for this report.
The TxGNN model predicts it may be effective for **headache disorder**, with **8 clinical trials** and **19 publications** retrieved for this prediction.
Several of these trials are small, and the key Phase 3 trial is still recruiting.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L1 per the scoring in the data compiled for this report. Note that only one Phase 3 trial has completed, so this level may be overstated. |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ketamine is an NMDA receptor antagonist. Detailed mechanism-of-action data from DrugBank are not available in the data compiled for this report, so the following is based on the mechanistic assessment in the prediction record.

Glutamate signalling, cortical spreading depolarization and central sensitization all contribute to headache pathophysiology. Blocking NMDA receptors is therefore a plausible way to relieve pain and migraine. Ketamine is already used in anaesthesia and pain medicine, and it has been tested in emergency department headache and in refractory chronic headache.

Related predictions on the same drug support this direction. Migraine disorder (L1, Proceed with Guardrails) shares most of the same trials. Trigeminal autonomic cephalalgia, including cluster headache, has open-label and case-series signals. Some other predictions, such as the common cold, ADHD, Tourette syndrome and psychotic disorder, have no credible support or even suggest harm. They should not be pursued.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead: multicentre, placebo-controlled RCT of high-dose IV ketamine (1 mg/kg/h for 6 hours) in chronic daily headache. No results yet. |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK: intranasal ketamine vs standard care for acute headache in the emergency department |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | Low-dose ketamine vs prochlorperazine (Compazine) for headache in the emergency department, double-blind |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Completed | 93 | Single infusion of ketamine plus magnesium sulfate in refractory chronic cluster headache (combination, so ketamine's own effect is hard to isolate) |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac in tension-type headache |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | Not specified | Completed | 34 | Placebo-controlled trial of sub-dissociative ketamine in acute migraine-type headache in the emergency department |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept study of intranasal ketamine in chronic cluster headache |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine plus aspirin vs rimegepant in emergency department headache (too small to be informative) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society update on parenteral drug treatment of acute migraine in the emergency department |
| [34703891](https://pubmed.ncbi.nlm.nih.gov/34703891/) | 2021 | Systematic review | J Dent Anesth Pain Med | Efficacy of ketamine in migraine and other primary headaches vs placebo and active comparators |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective cohort | Front Neurol | Efficacy, duration and safety of inpatient IV lidocaine and ketamine infusions in headache disorders |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Drug treatment of cluster headache, including acute and preventive options |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Systematic review/meta-analysis | J Neurol | Preventive treatment of refractory chronic cluster headache |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Ketamine mentioned as a possible adjuvant in trigeminal neuralgia |
| [32189074](https://pubmed.ncbi.nlm.nih.gov/32189074/) | 2020 | Review | Curr Neurol Neurosci Rep | Emergency department and inpatient management of headache in adults |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Curr Neurol Neurosci Rep | Emergency department and inpatient management of headache in children and adolescents |

Other retrieved papers concern ketamine in depression, and they say little about headache.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05966P | Ketamine Hydrochloride Injection USP (PANPHARMA GmbH) | Injection | Not stated in the licence record |
| SIN15402P | Ketamine Hameln Injection 50 mg/ml (Siegfried Hameln GmbH) | Injection, solution | Not stated in the licence record |

Both are single-ingredient products with valid status. Only injectable forms are registered, so the intranasal and oral routes studied in some trials have no local product.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension and hypertensive disorders, stroke and cerebrovascular disorders, myocardial infarction, coronary artery disease and myocardial ischaemia, intracranial hypertension and pseudotumor cerebri, ocular hypertension, respiratory failure, hyperthyroidism and Graves disease, delirium, substance abuse/dependence, and hemoglobinopathy.
- **Drug interactions:** 100 interactions were recorded. The moderate-level ones include opioids (morphine, opium, diphenoxylate), cannabinoids (dronabinol, nabilone), metoclopramide, and sympathomimetic or stimulant drugs (ephedrine, phentermine, sibutramine, fenfluramine, isometheptene, topical epinephrine). Several others, such as atropine, omeprazole and ondansetron, have an unknown severity level.
- **Other points from the retrieved literature:** ketamine causes psychotomimetic effects and has abuse and dependence potential.

Please refer to the package insert for official warnings, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Ketamine has a plausible NMDA-related mechanism and several randomized trials in headache, including an ED-based Phase 3 trial (THINK) that has completed. Most trials are small, and the multicentre Phase 3 trial (KetHead) is still recruiting with no results. The cardiovascular and cerebrovascular contraindication signals and the abuse potential call for tight patient selection.

**To proceed, the following is needed:**
- Results of NCT05306899 (KetHead) and NCT03081416 (THINK), with a check of the L1 evidence level
- Package insert warnings and contraindications from the Singapore Health Sciences Authority (HSA), as the safety screening cannot be completed without them
- Mechanism-of-action data from DrugBank
- A decision on route and formulation, since the registered products are injectable only
- A monitoring plan for blood pressure, cardiovascular risk, dissociative effects and abuse potential
- Prioritising migraine and cluster headache over other predicted indications. The common cold, ADHD, Tourette syndrome, psychotic disorder and trichotillomania should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

