---
layout: default
title: Butylscopolamine
parent: Medium Evidence (L3-L4)
nav_order: 187
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Butylscopolamine: predicted new indication Irritable bowel syndrome (evidence level L3). Approved use: Not stated in the registration data compiled for this report (general…"
monitor_inn: "Butylscopolamine"
predicted_indications: ["irritable bowel syndrome", "cauda equina syndrome", "neurocirculatory asthenia", "obsolete neurogenic bladder (disease)", "autonomic nervous system disease", "open-angle glaucoma", "primary hereditary glaucoma", "dysautonomia", "migraine disorder", "migraine with brainstem aura"]
---

# Butylscopolamine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

## Butylscopolamine: From Gastrointestinal Spasm to Irritable Bowel Syndrome
{: .text-alpha }

## One-Sentence Summary

Butylscopolamine (hyoscine butylbromide) is a peripherally acting antimuscarinic antispasmodic that is already marketed in Singapore for smooth muscle spasm. The TxGNN model predicts it may be effective for **irritable bowel syndrome (IBS)**. Current support is limited: **no registered clinical trials** and **one narrative review** (2025), plus one drug-utilization study that gives no efficacy evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data compiled for this report (general pharmacology: gastrointestinal spasm) |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, butylscopolamine is a peripherally acting antimuscarinic that relaxes gastrointestinal smooth muscle. Its quaternary ammonium structure limits penetration into the central nervous system.

Abdominal pain and cramping are the main symptoms of IBS, and antispasmodics are a standard treatment option for them. A 2025 review (PMID 40237755) discusses hyoscine butylbromide specifically for IBS and notes that Russian and international guidelines regard it as an effective antispasmodic. Because the drug is already used for gastrointestinal spasm, this prediction is close to an existing use rather than true repurposing.

This rationale rests on general pharmacology and a narrative review. Trial-level data have not been verified.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40237755](https://pubmed.ncbi.nlm.nih.gov/40237755/) | 2025 | Review | Terapevticheskii arkhiv | Reviews IBS therapy with hyoscine butylbromide. Guidelines list antispasmodics for abdominal pain, the main IBS symptom, and regard hyoscine butylbromide as effective. |
| [20065398](https://pubmed.ncbi.nlm.nih.gov/20065398/) | 1996 | Drug utilization/economic study | Laeknabladid | Study of drug use and costs for IBS in Iceland compared with other Nordic countries. Provides no efficacy evidence. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN10096P | COPAN INJECTION 20 mg/ml | Injection | Not listed |
| SIN03553P | HYOSCINE BUTYLBROMIDE TABLET 10 mg | Tablet, film coated | Not listed |
| SIN03082P | SPASMOLIV TABLET 10 mg | Tablet, film coated | Not listed |
| SIN03574P | BUSCOPAN TABLET 10 mg | Tablet, sugar coated | Not listed |
| SIN02575P | DHACOPAN TABLET 10 mg | Tablet, film coated | Not listed |

A sixth authorization, SIN03683P (COSPAN INJ. 20 mg/ml, injection), is also valid. All 6 registrations are valid single-ingredient products.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanism is plausible and the drug is already marketed in Singapore for a closely related use. Evidence is limited to a narrative review with no registered trials, so confidence in IBS-specific efficacy is moderate.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Mechanism of action data from DrugBank
- The approved indication text for each Singapore registration, to confirm the original indication
- Randomized controlled trial or systematic review data on hyoscine butylbromide in IBS, since the review's trial-level content has not been verified
- Confirmation of oral dosage forms for IBS use

## Other Predicted Indications (All on Hold)

The other nine predicted indications have no clinical trials and no supporting evidence. All are rated L5, and the recommendation for each is **Hold**.

| Predicted Indication | TxGNN Score | Comment |
|------|------|------|
| Cauda equina syndrome | 98.75% | No direct mechanistic rationale. It is a compressive neurosurgical emergency. |
| Neurocirculatory asthenia | 98.28% | Speculative. Anticholinergic effects such as tachycardia could worsen symptoms. |
| Obsolete neurogenic bladder (disease) | 97.92% | Antimuscarinics are an established class for this use, but no butylscopolamine-specific evidence was supplied. The disease term is obsolete and needs mapping to a current ontology term. Urinary retention is a risk. |
| Autonomic nervous system disease | 96.93% | Term is broad. The two supplied papers (a colitis animal model and an observational peptic ulcer study) do not support a therapeutic link. |
| Open-angle glaucoma | 96.71% | Not supported mechanistically. Antimuscarinics raise an intraocular pressure safety concern. |
| Primary hereditary glaucoma | 96.48% | No plausible rationale, with the same intraocular pressure concern. |
| Dysautonomia | 96.30% | The only paper is observational and does not test butylscopolamine. Anticholinergic effects could worsen some presentations. |
| Migraine disorder | 95.97% | No clear mechanism, and poor CNS penetration weakens the rationale. |
| Migraine with brainstem aura | 95.68% | No supporting mechanism. A peripherally restricted antimuscarinic is unlikely to act on brainstem aura. |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

