---
layout: default
title: Phenytoin
parent: Low Evidence (L5)
nav_order: 790
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy"
---

# Phenytoin
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

# Phenytoin: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenytoin is a long-established antiseizure drug, originally used for epilepsy, including generalized tonic-clonic seizures, partial seizures, status epilepticus and Lennox-Gastaut syndrome.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm** (score 99.99%), but there are **no registered clinical trials** and only **2 loosely related publications**, neither of which addresses a neoplasm.
The prediction is most likely an artifact of the knowledge graph's link to trigeminal neuralgia, so the evidence is essentially model prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (the approved indication text in the Singapore licences is blank; the original indications come from the knowledge graph) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Phenytoin is generally known as an antiseizure drug that blocks voltage-gated sodium channels, which reduces repetitive high-frequency neuronal firing. This general pharmacology is not drawn from the compiled data, so it should be verified.

The link between epilepsy and a trigeminal nerve neoplasm is weak. The retrieved literature concerns trigeminal neuralgia (a pain syndrome) and Sturge-Weber syndrome, not tumours. Sodium channel blockade might relieve neoplasm-associated neuropathic pain or seizures, but that would be symptomatic relief, not an anti-tumour effect. The prediction is probably explained by the ontology's proximity to trigeminal neuralgia, where phenytoin has genuine, though second-line, use.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Overview of medical and surgical treatments for trigeminal neuralgia; concerns a pain syndrome, not a neoplasm |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | An Esp Pediatr | Experience with 14 cases of Sturge-Weber syndrome (clinical features, course, treatment response); not about neoplasm |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09208P | DILANTIN CAPSULE 100 mg | Capsule | Not stated in the compiled data |
| SIN13114P | Dilantin 125 (Phenytoin Oral Suspension, USP) 125mg/5ml | Suspension | Not stated in the compiled data |
| SIN16560P | PHARMANIAGA PHENYTOIN SODIUM SOLUTION FOR INJECTION 250MG/5ML | Injection, solution | Not stated in the compiled data |
| SIN08183P | DBL PHENYTOIN INJECTION BP 50 mg/ml | Injection | Not stated in the compiled data |
| SIN06056P | DILANTIN CAPSULE 30 mg | Capsule | Not stated in the compiled data |

All five licences are valid single-ingredient products, covering oral and injectable routes.

---

## Safety Considerations

**Contraindication signals from the knowledge graph** (these are graph-derived associations, not package insert text):
- Cardiac: long QT syndrome (including familial), torsades de pointes
- Liver: liver failure, liver disease, hepatic coma, hepatic encephalopathy, gallbladder disease
- Kidney: kidney disease
- Blood: thrombocytopenia, neutropenia, agranulocytosis
- Metabolic: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, porphyria and other porphyrin metabolism diseases
- Autoimmune: systemic lupus erythematosus (including paediatric)
- Other: hypotensive disorder, anxiety and neurotic disorders, dysthymic disorder, substance abuse/dependence, sleep apnea syndromes, congenital central hypoventilation syndrome

**Drug Interactions:** 100 interactions were found. The 20 shown in the data are mostly Moderate, with one Minor (acetylsalicylic acid). Moderate-level examples include:
- Antidiabetic drugs: acarbose, metformin, pioglitazone, alogliptin, albiglutide
- Acid suppressants: omeprazole, famotidine, ranitidine
- Corticosteroids: dexamethasone, hydrocortisone, betamethasone, triamcinolone
- Others: doxycycline, metronidazole, bupropion, aprepitant, morphine, cholecalciferol, calcifediol

Literature reports also describe phenytoin-related thrombocytopenia, hyperglycemia/diabetic ketoacidosis, and the EMPACT syndrome (erythema multiforme with cranial radiation), which matters for patients with brain tumours.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The score is very high, but there are no clinical trials, no neoplasm-specific literature, and no mechanistic basis for an anti-tumour effect. The prediction looks like a knowledge-graph artifact. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data (MOA)
- Package insert warnings and contraindications from the HSA
- Any evidence of phenytoin anti-tumour activity in trigeminal nerve tumours (none found so far)

---

## Other Predicted Indications Worth Noting

The other predictions offer a more credible path than the top-ranked one:

| Rank | Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 9 | Trigeminal neuralgia | 99.97% | L4 | Most clinically credible. Phenytoin acts on the same sodium channel mechanism as carbamazepine (first-line). Evidence includes IV phenytoin retrospective cohorts (PMID 32981076, PMID 35469475) and a Cochrane review on neuropathic pain (PMID 22592741). Guidelines favour carbamazepine/oxcarbazepine, so it is at best second-line or rescue. Suggested as a research question. |
| 2 | Micturition-induced seizures | 99.98% | L4 | Mechanistically compatible; only indirect case-report support, no specific trials. Research question. |
| 3, 8 | Startle epilepsy, reading seizures | 99.98%, 99.97% | L4 | Case reports only; the drug-specific clinical report for startle epilepsy favours lamotrigine. Hold. |
| 4–7 | Audiogenic, eating, orgasm-induced, thinking seizures | 99.98% | L5 | Mostly animal or unrelated literature. Hold. |
| 10 | Beta-ketothiolase deficiency | 99.95% | L5 | No mechanistic rationale or literature. Hold. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

