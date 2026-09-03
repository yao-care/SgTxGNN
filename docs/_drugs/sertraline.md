---
layout: default
title: Sertraline
parent: 僅模型預測 (L5)
nav_order: 900
evidence_level: L5
indication_count: 10
---

# Sertraline
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

# Sertraline: From Major Depressive Disorder to Schizotypal Personality Disorder

## One-Sentence Summary

> Sertraline is a widely used SSRI, originally developed for major depressive disorder and subsequently approved for panic disorder, OCD, PTSD, and other anxiety-spectrum conditions.
> The TxGNN model predicts it may be relevant for **Schizotypal Personality Disorder**,
> but this signal is currently supported by only **1 small completed trial (n=8)** and **1 unrelated case report**, making it an early-stage research hypothesis rather than an established finding.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Major Depressive Disorder (per cited literature; no formal Singapore license record exists for this field — see Market Status below) |
| Predicted New Indication | Schizotypal Personality Disorder |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (flagged internally as "Research Question" — hypothesis-generating stage) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for sertraline is not available in this evidence pack (data gap, high severity). Based on known pharmacological information cited within the associated literature (PMID 12452737), sertraline is a naphthalenamine-derivative SSRI whose predominant action is inhibition of presynaptic serotonin reuptake at the synaptic cleft. It was initially marketed for major depressive disorder and later approved for panic disorder, OCD, and PTSD.

The predicted new indication, schizotypal personality disorder, sits on the schizophrenia spectrum and is characterized by attenuated positive and negative symptoms (odd beliefs, social anxiety, cognitive-perceptual distortions). The only supporting clinical trial (NCT00169988) tested sertraline in adolescents with *attenuated* positive/negative symptoms — a population conceptually adjacent to schizotypal presentations — providing a plausible, if indirect, mechanistic bridge between serotonergic modulation and thought-disorder-spectrum symptoms.

However, this mechanistic link remains theoretical. The trial enrolled only 8 participants with no phase designation, and the sole supporting literature record is a case report on an unrelated comorbidity (OCD and anorexia nervosa) that does not address schizotypal personality disorder at all. TxGNN's high confidence score likely reflects shared knowledge-graph connections among personality-disorder and mood/anxiety nodes rather than disease-specific efficacy evidence — a pattern also seen in several other lower-ranked candidates in this same prediction batch (e.g., schizoid, histrionic, and paranoid personality disorders), which show similarly high scores but essentially no relevant clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00169988](https://clinicaltrials.gov/study/NCT00169988) | NA | Completed | 8 | Compared sertraline alone vs. sertraline + risperidone in adolescents with attenuated positive/negative symptoms, assessing reduction in unusual thoughts, suspiciousness, and improvement in reasoning, memory, attention, and social skills. Directly relevant population but extremely small sample (n=8) limits statistical power. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37082034](https://pubmed.ncbi.nlm.nih.gov/37082034/) | 2021 | Case report | Postępy Psychiatrii i Neurologii | Describes diagnostic difficulty in a 14-year-old girl with comorbid OCD and anorexia nervosa; does not address schizotypal personality disorder directly and is of limited relevance to this prediction. |

---

## Singapore Market Information

Sertraline is currently **not marketed** in Singapore per the available regulatory dataset (0 registered licenses). No authorization records, product names, or approved-indication text are available to summarize.

---

## Safety Considerations

Please refer to the package insert for safety information.

Note: A TFDA/HSA label review (warnings and contraindications) is flagged as a **Blocking** data gap in this evidence pack — this must be resolved before any formal safety (S1) assessment can proceed for this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (schizotypal personality disorder) is supported by only one very small, non-phased completed trial (n=8) and one unrelated case report, placing it at evidence level L3 / decision stage S1 ("Research Question"). This is a hypothesis worth tracking, but not yet actionable.

**To proceed, the following is needed:**
- Detailed mechanism of action (MOA) data for sertraline (currently a data gap)
- TFDA/HSA product label (warnings, contraindications) — currently a **Blocking** data gap preventing any safety (S1) evaluation
- Larger, adequately powered trials specifically in schizotypal personality disorder or closely related attenuated-psychosis populations
- Literature directly evaluating sertraline's effect on schizotypal symptom domains (the current single reference is off-target)

**Additional context:** Several other candidates in this same prediction batch (agoraphobia/panic disorder, endogenous depression, major depressive disorder — ranks 6, 9, 10) carry the same TxGNN-style high scores but are supported by extensive Phase 3/4 RCT evidence (L1). These are not novel repurposing opportunities — they reflect sertraline's already well-established SSRI class indications, included here only because the original indication list in this dataset was empty. They should not be confused with genuinely new repurposing hypotheses like the schizotypal personality disorder signal discussed above.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

