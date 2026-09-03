---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 657
evidence_level: L5
indication_count: 10
---

# Methylphenidate
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

# Methylphenidate: From ADHD to Specific Developmental Disorder (Childhood Apraxia of Speech)

## One-Sentence Summary

Methylphenidate is a central nervous system stimulant currently used as first-line pharmacological treatment for Attention-Deficit/Hyperactivity Disorder (ADHD), as repeatedly documented across the evidence base collected for this candidate.
Among the 10 TxGNN-predicted indications reviewed for this drug, **Specific Developmental Disorder** is the only one supported by direct, completed clinical trial evidence — including a Phase 2 RCT testing methylphenidate specifically in childhood apraxia of speech — backed by **16 clinical trials** and **18 publications**.
Several higher-scoring TxGNN predictions (e.g. faciodigitogenital syndrome at 99.998%, chondromyxoid fibroma at 99.99%) were screened out and flagged as likely knowledge-graph embedding noise, since they carry **zero** supporting trials or literature and no plausible mechanistic link to methylphenidate's pharmacology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Attention-Deficit/Hyperactivity Disorder (ADHD) — referenced consistently in trial and literature evidence as methylphenidate's established core indication |
| Predicted New Indication | Specific Developmental Disorder (lead evidenced subtype: Childhood Apraxia of Speech) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, a formal DrugBank-sourced mechanism-of-action (MOA) record is not available for methylphenidate in this evidence pack. Based on the clinical trial and literature evidence collected, methylphenidate is understood to act as a dopamine transporter (DAT) / norepinephrine transporter (NET) reuptake inhibitor — a psychostimulant mechanism that underlies its established efficacy in ADHD, itself a neurodevelopmental disorder affecting attention, impulse control, and executive function.

"Specific developmental disorder" and ADHD both fall within the broader neurodevelopmental disorder spectrum, so a mechanistic extension from ADHD to other developmental-disorder subtypes is biologically plausible. This is not purely theoretical: **NCT05185583**, a completed, double-blind, placebo-controlled, randomized Phase 2 crossover trial, directly tested methylphenidate in children with childhood apraxia of speech (CAS) — a specific developmental disorder — for its effect on speech intelligibility. This is the strongest single piece of evidence in the entire candidate set and is what elevates this indication to Evidence Level L2 / decision stage S2, versus most other TxGNN top-ranked predictions for this drug.

It is also worth noting, for triage transparency, that several other TxGNN predictions scored higher than this one but carried no supporting evidence at all (faciodigitogenital syndrome, chondromyxoid fibroma, benign paroxysmal torticollis of infancy) and were judged embedding artifacts. Two other candidates — trichotillomania and insomnia — actually showed evidence pointing in the **opposite** direction: literature described methylphenidate as *inducing or aggravating* these conditions as an adverse effect, not treating them, and both were correctly held back. This underscores why raw TxGNN score alone should never be used as a decision criterion without evidence triage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05185583](https://clinicaltrials.gov/study/NCT05185583) | Phase 2 | Completed | 18 | Double-blind, randomized, placebo-controlled crossover trial testing methylphenidate's effect on speech intelligibility in children (6–12y) with childhood apraxia of speech — the direct evidence anchor for this indication. |
| [NCT05974241](https://clinicaltrials.gov/study/NCT05974241) | Phase 4 | Completed | 36 | Evaluated methylphenidate and aripiprazole for irritability in children with ADHD and emotion dysregulation; relevant comorbid population but not a direct developmental-disorder endpoint. |
| [NCT01363544](https://clinicaltrials.gov/study/NCT01363544) | Phase 2/3 | Completed | 112 | Combined exercise and neurofeedback intervention with pharmacological (stimulant) treatment for ADHD core symptoms and cortical regulation. |
| [NCT04647500](https://clinicaltrials.gov/study/NCT04647500) | N/A | Completed | 45 | Studied dopaminergic modulation via methylphenidate on memory and executive processes in 22q11.2 deletion syndrome, a neurogenetic developmental condition with 35–45% ADHD comorbidity. |
| [NCT00573859](https://clinicaltrials.gov/study/NCT00573859) | Phase 1/2 | Completed | 27 | Examined reinforcing/stimulant mechanisms in adult ADHD, relevant to methylphenidate's dopaminergic action but not a direct developmental-disorder treatment trial. |

*Note: 11 additional registered trials in this category (e.g. NCT01470261, NCT01577277, NCT04815278, NCT04841122, NCT05635318, and several unassessed "pending relevance" trials) were reviewed but screened out as low relevance — largely large observational/registry studies, diet interventions, or unrelated acute-care studies where methylphenidate was incidental rather than the primary intervention for this indication.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8719499](https://pubmed.ncbi.nlm.nih.gov/8719499/) | 1996 | Cohort | Clinical EEG (electroencephalography) | QEEG-based discriminant functions distinguished children with specific developmental learning disorders from ADD/ADHD populations and predicted differential stimulant response, directly relevant to this disease category. |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Cohort/Longitudinal MRI | Prog Neuropsychopharmacol Biol Psychiatry | Age-dependent effects of cumulative methylphenidate exposure on brain structure and symptom amelioration in youth with ADHD (N=89 ADHD, N=91 controls). |
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Cohort/Imaging (PET) | Psychiatry Clin Neurosci | Longitudinal dual-tracer PET study showing extended-release methylphenidate modulates DAT and NET binding in adults with ADHD. |
| [20483462](https://pubmed.ncbi.nlm.nih.gov/20483462/) | 2010 | Cohort | Psychiatry Research | EEG coherence differences distinguished good versus poor methylphenidate responders in children with combined-type ADHD. |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Review | Neuropharmacology | Review of ADHD neurobiology, including genetic basis and structural brain differences relevant to stimulant treatment mechanisms. |
| [19487194](https://pubmed.ncbi.nlm.nih.gov/19487194/) | 2009 | Review | Philos Trans R Soc Lond B | Describes ADHD impulsiveness as a timing disturbance with neurocognitive abnormalities normalized by methylphenidate. |
| [36688969](https://pubmed.ncbi.nlm.nih.gov/36688969/) | 2024 | Cohort | Eur Child Adolesc Psychiatry | First study of methylphenidate's effects on objectively measured graphomotor (handwriting) movements in children with ADHD. |
| [25989180](https://pubmed.ncbi.nlm.nih.gov/25989180/) | 2015 | Genetic/Pharmacogenetic | Genes Brain Behav | LPHN3 gene variants linked to ADHD susceptibility and methylphenidate pharmacogenetic response. |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Review | Clin EEG Neurosci | Review of quantitative EEG use in childhood ADHD and learning disabilities, supporting personalized-medicine framing for stimulant response. |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Review | J Atten Disord | Reviews evolution of methylphenidate mechanism-of-action research across adult and juvenile brain studies. |

---

## Singapore Market Information

Methylphenidate currently has **no marketing authorization registered** in the Singapore regulatory dataset used for this evaluation (market status: 未上市 / Not Marketed; 0 registrations on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Key warnings, contraindications, and drug-drug interaction data were not available in this evidence pack — the DDI query for methylphenidate returned no results, and this is flagged as a Blocking-severity data gap (DG001) requiring the Singapore HSA product insert before any safety pre-screening can proceed.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed, double-blind, placebo-controlled Phase 2 RCT (NCT05185583) directly tested methylphenidate in a specific developmental disorder subtype (childhood apraxia of speech), supported by a substantial body of ADHD neuropharmacology literature justifying mechanistic extrapolation across developmental-disorder subtypes. However, the pivotal trial's enrollment is small (N=18) and targets a narrow subtype rather than the full "specific developmental disorder" category, so the evidence supports cautious, guarded progression rather than unconditional advancement.

**To proceed, the following is needed:**
- HSA (Singapore) product insert / warnings and contraindications data to close the Blocking data gap (DG001) before any safety pre-screening
- Confirmed mechanism-of-action data from DrugBank (DG002) to strengthen the mechanistic rationale
- A completed, adequately powered drug-drug interaction (DDI) review, since the current DDI query returned no results
- Clarification of the precise target sub-indication (childhood apraxia of speech vs. the broader "specific developmental disorder" ICD grouping) before any regulatory engagement
- A larger confirmatory trial beyond the N=18 pilot to validate efficacy before considering formal indication-seeking activity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

