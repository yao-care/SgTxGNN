---
layout: default
title: Flecainide
parent: Medium Evidence (L3-L4)
nav_order: 434
evidence_level: L3
indication_count: 10
last_modified_at: 2026-10-14
description: "Flecainide: predicted new indication Stroke disorder (evidence level L3). Approved use: Atrial fibrillation"
monitor_inn: "Flecainide"
predicted_indications: ["stroke disorder", "obsolete susceptibility to ischemic stroke", "sick sinus syndrome 2, autosomal dominant", "ABri amyloidosis", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "duodenal obstruction", "cerebrovascular disorder", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Flecainide
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

## Flecainide: From Atrial Fibrillation to Stroke Disorder
{: .text-alpha }

## One-Sentence Summary

Flecainide is a Class 1C sodium channel blocker, originally used to maintain normal heart rhythm in atrial fibrillation.
The TxGNN model predicts it may be useful for **stroke disorder**, but the link is indirect (via rhythm control), supported by **1 Phase 3 clinical trial** (arrhythmia endpoint, not stroke) and **20 publications**, mostly on atrial fibrillation management.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atrial fibrillation (the registration records compiled for Singapore contain no approved-indication text) |
| Predicted New Indication | Stroke disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (research question; guardrails needed if explored) |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, flecainide is a Class 1C sodium channel blocker. Its efficacy in maintaining rhythm control in atrial fibrillation is established, and any benefit in stroke would be indirect.

Atrial fibrillation is a major cause of cardioembolic stroke. If flecainide helps maintain sinus rhythm, it could in theory lower stroke risk in selected patients. The one Phase 3 trial (NCT05213104) tests flecainide for preventing atrial arrhythmia after patent foramen ovale (PFO) closure in patients with prior cryptogenic stroke. Its primary endpoint is arrhythmia, not recurrent stroke.

The very high TxGNN score reflects closeness to atrial fibrillation in the knowledge network. It is not clinical evidence of efficacy in stroke. Class 1C agents are also restricted in structural and ischaemic heart disease, which is common in stroke populations.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, not recruiting | 186 | Flecainide to lower atrial arrhythmia risk after PFO closure in a cryptogenic-stroke-related population. Endpoint is arrhythmia, so evidence for stroke prevention is indirect. No results reported yet. Estimated completion: September 2026. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | Cohort | Europace | Safety and efficacy of long-term sodium channel blocker (flecainide/propafenone) early rhythm control in EAST-AFNET 4 |
| [38551548](https://pubmed.ncbi.nlm.nih.gov/38551548/) | 2024 | Cohort | JACC Clin Electrophysiol | Class 1C drugs for PVC suppression in nonischaemic cardiomyopathy with ICDs |
| [41954064](https://pubmed.ncbi.nlm.nih.gov/41954064/) | 2026 | Not classified | J Am Heart Assoc | Long-term outcomes of Class 1C antiarrhythmics in atrial fibrillation |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | Randomised pilot study | J Clin Med | Carvedilol vs flecainide for idiopathic outflow-tract PVCs (not stroke-related) |
| [37676022](https://pubmed.ncbi.nlm.nih.gov/37676022/) | 2024 | Review | J Cardiovasc Electrophysiol | Role of antiarrhythmic drugs in PVC-induced cardiomyopathy |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Review | BMJ Clin Evid | Acute-onset atrial fibrillation; notes increased stroke and heart failure risk |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Review | J Manag Care Pharm | Pharmacologic management of atrial fibrillation |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Retrospective cohort | J Atr Fibrillation | Cardiovascular events and stroke with dronedarone vs amiodarone and other antiarrhythmics |
| [8199770](https://pubmed.ncbi.nlm.nih.gov/8199770/) | 1994 | Review | Heart Dis Stroke | Value and danger of flecainide; best suited to patients without structural heart disease |
| [8729366](https://pubmed.ncbi.nlm.nih.gov/8729366/) | 1995 | Clinical study | Arch Mal Coeur Vaiss | Atrial electrophysiological study with IV flecainide in 38 patients with unexplained ischaemic cerebrovascular events |

Most publications address atrial fibrillation or PVC management. None demonstrates that flecainide reduces stroke.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN01726P | TAMBOCOR TABLET 100 mg | Tablet | Not available |
| SIN16823P | JAMP FLECAINIDE ACETATE TABLETS USP 100 MG | Tablet | Not available |

## Safety Considerations

- **Contraindication-related signals (from a knowledge graph, not label text)**: Kidney disease, liver disease, gallbladder disease, potassium deficiency, myocardial infarction and coronary thrombosis, haemoglobinopathy, atrioventricular block, and sick sinus syndrome (including the familial form).
- **Proarrhythmic risk**: A published case report describes a Brugada pattern after flecainide overdose. Class 1C agents are generally restricted to patients without structural or ischaemic heart disease.
- **Drug Interactions**: 100 interactions were identified. Major-level ones include **dolasetron** and **eliglustat**. Moderate-level ones include famotidine, cimetidine, loperamide, bupropion, clarithromycin, levofloxacin, lorcaserin, palonosetron, trospium, and several laxatives or bowel-preparation agents (bisacodyl, picosulfuric acid, lactulose, lactitol, sodium sulfate, polyethylene glycol). Minor-level ones include ascorbic acid, potassium citrate, and metronidazole.

Please refer to the package insert for full safety information. The Singapore package insert warnings and contraindications were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial (Phase 3, active, not recruiting) targets arrhythmia after PFO closure, not stroke, and the literature is dominated by atrial fibrillation reviews and cohorts. The high TxGNN score reflects network proximity to atrial fibrillation, not stroke evidence. Stroke populations often have structural or ischaemic heart disease, where Class 1C agents are a safety concern. This remains a research question.

**To proceed, the following is needed:**
- Results from NCT05213104, including any stroke or thromboembolic outcomes
- Direct evidence on stroke outcomes with flecainide-based rhythm control, ideally from randomised or well-controlled cohort studies
- The Singapore package insert (warnings, contraindications, approved indications)
- Detailed mechanism of action data
- A patient-selection plan excluding structural and ischaemic heart disease, with ECG monitoring and review of interacting drugs (especially dolasetron and eliglustat)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

