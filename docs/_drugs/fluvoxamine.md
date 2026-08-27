---
layout: default
title: Fluvoxamine
parent: 僅模型預測 (L5)
nav_order: 444
evidence_level: L5
indication_count: 10
---

# Fluvoxamine
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

Using the drug-repurposing report format directly (this is a content-generation task, not one that maps to a coding/ops skill), I reviewed the full Evidence Pack before drafting. One judgment call worth flagging up front: `predicted_indications[0]` (schizotypal personality disorder) is explicitly annotated in its own `repurposing_rationale` as likely knowledge-graph noise (no causal literature, scoring = L5/Hold) — same for ranks 2–4 and 7–9 (schizoid/paranoid/dependent/narcissistic personality disorder, benign paroxysmal torticollis). Mechanically reporting on rank #1 would produce a misleading "evaluation," so I built the report around the strongest, most defensible candidate in the pack — **Anxiety Disorder** (rank 5, L1 evidence, "Proceed with Guardrails") — and noted the discarded low-evidence candidates transparently rather than silently dropping them.

---

# Fluvoxamine: From Obsessive-Compulsive Disorder/Depression to Anxiety Disorder

## One-Sentence Summary

Fluvoxamine is a selective serotonin reuptake inhibitor (SSRI) originally developed and approved for **depression** and **obsessive-compulsive disorder (OCD)**. The TxGNN model's top-ranked prediction for this drug (schizotypal personality disorder, score 99.997%) is flagged in the underlying evidence review as likely knowledge-graph noise with no causal support, so this report instead evaluates the strongest, evidence-backed candidate among the ten TxGNN outputs: **Anxiety Disorder**, supported by **43 clinical trials** and **20 publications**, including Cochrane-level meta-analyses and a completed Phase 3 pediatric RCT.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obsessive-Compulsive Disorder / Depression (established via literature in this Evidence Pack; no Singapore-specific label text is available) |
| Predicted New Indication | Anxiety Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed formal mechanism-of-action documentation is not available in this Evidence Pack (DrugBank MOA field is a data gap). However, the literature evidence collected alongside the predictions consistently and repeatedly describes fluvoxamine as a potent, specific 5-HT (serotonin) reuptake inhibitor (e.g., PMID 3096686, PMID 10872178), first studied in depression in the late 1970s and approved for OCD in the US in 1994 and in roughly 30 other countries since. Serotonergic reuptake inhibition is also the accepted core pharmacological mechanism underlying efficacy across the broader anxiety-disorder spectrum (generalized anxiety disorder, social anxiety disorder, panic disorder with/without agoraphobia).

Anxiety disorders and OCD/depression sit on a closely related, overlapping neurobiological axis, and both are already commonly treated with SSRIs in clinical practice. Fluvoxamine specifically has decades of trial history in this space: it carries an FDA-approved indication for social anxiety disorder in some markets, and pediatric fluvoxamine trials (e.g., the NIMH-sponsored RUPP Anxiety Treatment Study) were run explicitly because "fluvoxamine has been successfully used to treat OCD... anxiety disorders other than OCD... may respond to fluvoxamine" (per NCT00000389's own trial rationale). This makes the TxGNN prediction mechanistically coherent rather than speculative — unlike several other candidates in this same evidence pack (schizotypal, schizoid, paranoid, dependent, and narcissistic personality disorder, and benign paroxysmal torticollis of infancy), which returned only incidental comorbidity case reports or no evidence at all, and are explicitly annotated in the source data as probable false-positive/noise predictions with no mechanistic basis — these were excluded from further evaluation.

Two other TxGNN candidates in this pack — **Agoraphobia** and **Endogenous Depression** — also reached L1 evidence status via the same SSRI/anxiolytic-antidepressant mechanism and could be evaluated as parallel or follow-on repurposing targets using largely the same evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000389](https://clinicaltrials.gov/study/NCT00000389) | Phase 3 | Completed | N/A | RUPP pediatric anxiety treatment study directly evaluating fluvoxamine for GAD, social phobia, and separation anxiety in youth |
| [NCT00655174](https://clinicaltrials.gov/study/NCT00655174) | Phase 3 | Completed | 108 | Double-blind, placebo-controlled RCT of fluvoxamine vs. sertraline for aggression, obsessive symptoms, and anxiety in childhood autism |
| [NCT00854919](https://clinicaltrials.gov/study/NCT00854919) | Phase 4 | Completed | 46 | Long-term effectiveness/safety of atypical antipsychotic augmentation in SSRI (including fluvoxamine)-refractory OCD/anxiety-spectrum patients |
| [NCT00012584](https://clinicaltrials.gov/study/NCT00012584) | N/A (pilot) | Completed | 120 | NIMH pilot study of fluvoxamine (an SSRI with antianxiety effects) combined with stimulant medication in youths with comorbid ADHD and anxiety disorders |
| [NCT02043197](https://clinicaltrials.gov/study/NCT02043197) | N/A (observational) | Completed | 300 | Post-marketing observational program (FRIENDS) describing Fevarin® (fluvoxamine) effects on anxiety and depression severity in neurological-disorder patients |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29995828](https://pubmed.ncbi.nlm.nih.gov/29995828/) | 2018 | Meta-analysis | Medicine | Confirms efficacy and acceptable tolerability of fluvoxamine in social anxiety disorder (SAD) |
| [18408531](https://pubmed.ncbi.nlm.nih.gov/18408531/) | 2008 | Systematic review / network meta-analysis | International Clinical Psychopharmacology | Comparative efficacy of second-generation antidepressants, including fluvoxamine, in SAD |
| [19198698](https://pubmed.ncbi.nlm.nih.gov/19198698/) | 2008 | RCT (3 pooled trials) | Drugs of Today | Three 12-week double-blind, multicenter, placebo-controlled RCTs demonstrate efficacy of controlled-release fluvoxamine in OCD and SAD |
| [16573847](https://pubmed.ncbi.nlm.nih.gov/16573847/) | 2007 | RCT | Int J Neuropsychopharmacology | Randomized, double-blind, placebo-controlled trial confirms fluvoxamine efficacy for generalized social anxiety disorder in Japanese patients |
| [2109498](https://pubmed.ncbi.nlm.nih.gov/2109498/) | 1990 | RCT | Acta Psychiatrica Scandinavica | Multicentre double-blind RCT: fluvoxamine comparable to lorazepam for mixed anxiety and depression in general practice |
| [22030083](https://pubmed.ncbi.nlm.nih.gov/22030083/) | 2011 | Review | BMJ Clinical Evidence | Overview of generalized anxiety disorder (GAD) epidemiology and evidence base for SSRI treatment |
| [11825104](https://pubmed.ncbi.nlm.nih.gov/11825104/) | 2002 | Review | CNS Drugs | Review of fluvoxamine use in pediatric/adolescent anxiety disorders; supports dosing up to 300 mg/day in adolescents |
| [11706925](https://pubmed.ncbi.nlm.nih.gov/11706925/) | 2001 | Review | Paediatric Drugs | Reviews fluvoxamine's therapeutic potential for anxiety disorders in children and adolescents |
| [9184625](https://pubmed.ncbi.nlm.nih.gov/9184625/) | 1997 | Review | Journal of Clinical Psychiatry | Establishes fluvoxamine's anti-obsessional/anxiolytic efficacy via serotonin reuptake inhibition |
| [25728382](https://pubmed.ncbi.nlm.nih.gov/25728382/) | 2015 | Review | Expert Opinion on Drug Metabolism & Toxicology | Pharmacokinetic evaluation supporting fluvoxamine's role in anxiety-disorder treatment, based on 30 years of clinical experience |

---

## Singapore Market Information

Fluvoxamine currently has **0 product registrations** in Singapore, with a market status of **Not Marketed**. No HSA license records were found for this drug in the Evidence Pack. This means formal local registration/import authorization — not just clinical evidence — would be a prerequisite before fluvoxamine could be used for any indication (original or repurposed) within Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Structured safety fields — key warnings, contraindications, and drug-drug interactions — returned no data in this Evidence Pack; the DDI query itself came back "not found." This is flagged as a Blocking data gap (DG001) in the source data, since it prevents formal S1 safety pre-screening.)*

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The Anxiety Disorder indication is backed by L1-tier evidence — Cochrane/meta-analysis-level literature and a completed Phase 3 pediatric RCT — consistent with fluvoxamine's well-established SSRI mechanism, making it the most credible repurposing candidate in this evidence pack. However, the drug is currently unregistered in Singapore and lacks formal safety labeling data, so guardrails are required before any clinical deployment.

**To proceed, the following is needed:**
- Official prescribing information (warnings/contraindications) for Singapore or a comparable regulator — currently missing and blocking formal safety screening (DG001)
- A documented mechanism-of-action reference (e.g., from DrugBank) to support formal pharmacological review (DG002)
- Initiation of the HSA registration pathway, since fluvoxamine currently holds zero product licenses in Singapore
- No further action on the TxGNN-flagged personality-disorder and infantile-torticollis predictions (ranks 1–4, 7–9) — these lack any credible clinical or mechanistic evidence and are recommended for Hold/exclusion
- Optional: parallel evaluation of **Agoraphobia** and **Endogenous Depression**, both of which also reached L1 evidence status via the same SSRI mechanism and could extend this repurposing case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

