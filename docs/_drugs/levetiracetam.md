---
layout: default
title: Levetiracetam
parent: Medium Evidence (L3-L4)
nav_order: 593
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Levetiracetam: predicted new indication Visual epilepsy (evidence level L4). Approved use: Partial epilepsy"
monitor_inn: "Levetiracetam"
predicted_indications: ["beta-ketothiolase deficiency"]
---

# Levetiracetam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Levetiracetam: From Partial Epilepsy to Visual Epilepsy

## One-Sentence Summary

Levetiracetam is an antiseizure medication, originally used for partial (focal) epilepsy.
The TxGNN model predicts it may be effective for **visual epilepsy** (seizures triggered by visual stimuli), but there are **0 registered clinical trials** and no publications specific to this condition.
The retrieved **20 publications** cover general seizure populations only, so the evidence is indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Partial epilepsy (taken from the knowledge-graph indication record; the Singapore licence records contain no indication text) |
| Predicted New Indication | Visual epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Published literature describes levetiracetam as binding synaptic vesicle protein 2A (SV2A), which alters neurotransmitter release and reduces seizure frequency. Its efficacy in partial epilepsy is established, and it is widely used as an antiseizure medication.

Visual epilepsy is a reflex (photosensitive) epilepsy, in which seizures are triggered by a specific visual stimulus. Partial epilepsy and reflex epilepsies share a hyperexcitable-network basis. A drug that dampens excessive synaptic release could therefore plausibly reduce stimulus-triggered seizures.

However, the retrieved literature concerns neonatal, post-stroke and neurocritical-care seizures, not visually triggered seizures. The high TxGNN score mainly reflects similarity to the parent indication and should not be read as proof of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below studies visual epilepsy directly.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | Levetiracetam vs phenobarbital for neonatal seizures (indirect) |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | RCT (Phase 3) | The Lancet Neurology | Prophylactic levetiracetam to prevent early seizures after intracerebral haemorrhage (PEACH) |
| [38678766](https://pubmed.ncbi.nlm.nih.gov/38678766/) | 2024 | RCT (open-label) | Seizure | Phenytoin vs levetiracetam for acute symptomatic seizures in children with acute encephalitis syndrome |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Meta-analysis | Neurocritical Care | Levetiracetam for seizure prophylaxis in neurocritical care |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Network meta-analysis | Neurology | Comparison of antiseizure medications in poststroke seizures |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Meta-analysis | Epilepsy & Behavior | Levetiracetam for myoclonic seizures in idiopathic generalized epilepsy |
| [39899098](https://pubmed.ncbi.nlm.nih.gov/39899098/) | 2025 | Review | Continuum | Management of first seizures, cluster seizures and status epilepticus |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Overview of levetiracetam's approved uses in epilepsy |
| [12915343](https://pubmed.ncbi.nlm.nih.gov/12915343/) | 2003 | Review | Epileptic Disorders | Favourable safety profile of levetiracetam as add-on therapy for partial-onset seizures |
| [29287214](https://pubmed.ncbi.nlm.nih.gov/29287214/) | 2018 | Preclinical | Epilepsy & Behavior | Brivaracetam shows fewer behavioural side effects than levetiracetam in a model; both act on SV2A |

## Singapore Market Information

Twenty licences are valid; the five main ones are shown below. No approved indication text is recorded for these licences.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11686P | Keppra Tablet 500 mg | Film-coated tablet | — |
| SIN13730P | Keppra Concentrate for Solution for Infusion 100 mg/ml | Infusion concentrate | — |
| SIN14905P | Levetiracetam Sandoz Film Coated Tablets 500 mg | Film-coated tablet | — |
| SIN16254P | Intiracetam Oral Solution 100 mg/ml | Oral solution | — |
| SIN16250P | Levipil Levetiracetam Injection USP 100 mg/ml | Injection | — |

Oral, intravenous and oral-solution forms are all available.

## Safety Considerations

- **Contraindication signals (knowledge-graph data, not label text)**: The knowledge graph links levetiracetam to anxiety and other mental disorders (psychotic, schizoaffective and dysthymic disorders), kidney disease, liver disease, gallbladder disease, and blood-cell disorders (neutropenia, agranulocytosis, leukopenia, pancytopenia). These need verification against the package insert.
- **Drug interactions**: 100 interacting drugs were recorded. The moderate-level ones include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide and sibutramine, which are mainly additive central nervous system effects. Several others, such as pantoprazole, omeprazole, metformin and vancomycin, have an unclassified interaction level.
- **Reported adverse effects in the literature**: behavioural changes, hyponatraemia (PMID 28755154) and, rarely, gingival hyperplasia (PMID 35848684). A preclinical study also examined cochlear effects (PMID 34903423).

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Visual epilepsy has no registered trials and no disease-specific publications, so the evidence is indirect (L4). The high TxGNN score alone does not justify advancing.

Among the other predictions in the same data set, **status epilepticus** has far stronger support. It has several completed Phase 3 trials, including a 478-patient randomized comparison of levetiracetam, fosphenytoin and valproate, and the published ESETT trial (PMID 31774955). It is rated L1 and "Proceed with Guardrails", and it would be a better candidate to prioritise.

**To proceed, the following is needed:**
- Disease-specific evidence for levetiracetam in photosensitive or visually triggered epilepsy (e.g. photoparoxysmal EEG response studies, case series)
- Package insert warnings and contraindications from the Singapore regulator (HSA)
- Mechanism of action data confirmed from a primary source
- Comparison with established first-line options for photosensitive epilepsy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

