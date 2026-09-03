---
layout: default
title: Pramipexole
parent: 僅模型預測 (L5)
nav_order: 808
evidence_level: L5
indication_count: 10
---

# Pramipexole
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

# Pramipexole: From Dopaminergic Disorders to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

> Pramipexole is a non-ergot dopamine D2/D3 receptor agonist internationally established for Parkinson's Disease and Restless Legs Syndrome (no Singapore market registration exists for this evidence pack, so local approved-indication text is not available).
> TxGNN's top prediction is **Attention Deficit-Hyperactivity Disorder (ADHD)**, but on review the supporting clinical trial and literature evidence largely do **not** map cleanly onto ADHD — this is a low-confidence, hypothesis-generating signal rather than a validated repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available from Singapore regulatory data (drug not marketed locally). Internationally, Pramipexole is indicated for Parkinson's Disease and Restless Legs Syndrome. |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.998% (rank #111 among all candidates) |
| Evidence Level | L4 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in structured form. Based on known pharmacology, Pramipexole is a non-ergot D2/D3 dopamine receptor agonist with high selectivity for the D3 subtype, and its efficacy in dopaminergic-deficiency conditions such as Parkinson's Disease and Restless Legs Syndrome is well established.

ADHD pathophysiology has long been linked to underactive dopamine signalling in the prefrontal-striatal circuit, which offers a superficial mechanistic rationale for testing a dopamine agonist. However, this rationale is not fully consistent with how ADHD is conventionally treated: first-line agents (e.g., methylphenidate, amphetamines) act by inhibiting dopamine reuptake or promoting presynaptic dopamine release, whereas Pramipexole acts postsynaptically as a direct receptor agonist. The direction of pharmacological action is not the same, so the mechanistic link is theoretical rather than confirmed.

Critically, when the underlying evidence for this candidate was reviewed, almost none of it is actually about ADHD. The single linked clinical trial concerns Parkinson's Disease reward signalling (graded "C" relevance — likely a knowledge-graph mismatch), and the literature set is dominated by studies on Restless Legs Syndrome, Tourette's syndrome, case reports of ADHD as a comorbidity (not treatment target), and unrelated basic-science papers. Only one paper (PMID 34182128) directly discusses a plausible ADHD-relevant receptor mechanism (D4/α2A heteromerization), and it is preclinical, not clinical.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00558766](https://clinicaltrials.gov/study/NCT00558766) | N/A | Completed | 35 | Studied reward-related brain activity in Parkinson's Disease patients on dopaminergic therapy; **not an ADHD study** — flagged as likely knowledge-graph mismatch (relevance grade C). |

No clinical trial in this evidence set directly enrolled or evaluated ADHD patients.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [22407510](https://pubmed.ncbi.nlm.nih.gov/22407510/) | 2012 | RCT | Movement Disorders | Multicenter placebo-controlled trial of Pramipexole for **Tourette's syndrome**, not ADHD; tests dopamine-hypersensitivity hypothesis relevant to tic disorders. |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | Basic Science | Pharmacological Research | Preclinical receptor-heteromerization study (α2A adrenoceptor–D4 receptor variants) discussing relevance to ADHD and impulse-control disorders; most directly on-topic paper, but mechanistic/preclinical only. |
| [37342213](https://pubmed.ncbi.nlm.nih.gov/37342213/) | 2023 | Case Report | Frontiers in Pain Research | Case of chronic pain remission in a patient with comorbid ADHD treated with atomoxetine **plus** Pramipexole; ADHD present as comorbidity, not the treatment target. |
| [38649244](https://pubmed.ncbi.nlm.nih.gov/38649244/) | 2024 | Case Report | BMJ Case Reports | Hypokalaemia case in a patient with ADHD among other comorbidities, taking Pramipexole for an unrelated indication; incidental ADHD mention only. |
| [15540638](https://pubmed.ncbi.nlm.nih.gov/15540638/) | 2004 | Cohort | Dev Med Child Neurol | Periodic leg movements in children with sleep disturbance; Pramipexole discussed for sleep disorder, not ADHD. |
| [24079375](https://pubmed.ncbi.nlm.nih.gov/24079375/) | 2013 | Animal Model | Journal of Motor Behavior | Rat model exploring RLS/PLM-ADHD co-occurrence; no direct Pramipexole-ADHD efficacy data. |
| [19412489](https://pubmed.ncbi.nlm.nih.gov/19412489/) | 2006 | Review | Neuropsychiatr Dis Treat | Review of Pramipexole's "new use" in Restless Legs Syndrome; not ADHD. |
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue Neurologique | Review of Restless Legs Syndrome; not ADHD. |
| [24992083](https://pubmed.ncbi.nlm.nih.gov/24992083/) | 2014 | Cohort | Clinical Neuropharmacology | Compares piribedil vs. Pramipexole/ropinirole for daytime sleepiness in Parkinson's Disease; unrelated to ADHD. |

**Overall assessment:** Of the 9 literature items retrieved, only 1 is directly and substantively about ADHD mechanism (preclinical), and no clinical trial or clinical study evaluated Pramipexole as an ADHD treatment. This is consistent with the model's own annotation that this may be a knowledge-graph embedding artifact.

---

## Singapore Market Information

Pramipexole currently has no marketing authorization on record in this evidence pack (0 registrations, market status: not marketed). No product listing is available.

---

## Safety Considerations

Please refer to the package insert for safety information. Structured safety data (key warnings, contraindications, drug interactions) were not available in this evidence pack, and label-level safety data (TFDA warnings/contraindications) is flagged as a **blocking data gap** — this must be resolved before any safety evaluation (S1) can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale for Pramipexole in ADHD is theoretical and arguably contradicts the pharmacological direction of standard ADHD therapy (receptor agonism vs. reuptake inhibition/release), and the supporting clinical trial/literature evidence is almost entirely off-target (Parkinson's Disease, RLS, Tourette's, incidental comorbidity mentions) rather than ADHD-specific. Evidence Level L4 reflects mechanism-only support with no direct clinical validation for this indication.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain official label warnings/contraindications (source: regulatory agency) before any S1 safety screening
- Resolve high-priority data gap DG002: confirm structured mechanism of action via DrugBank API
- Identify and review a clinical trial or study that directly enrolls ADHD patients on Pramipexole (none currently exists in this evidence set)
- Note: within this same candidate list, **Schizophrenia (rank 9)** shows materially stronger evidence (L2, a completed Phase 3 RCT, a positive RCT in *J Clin Psychiatry* 2022, and a systematic review/meta-analysis) and may warrant separate, higher-priority evaluation if pursuing Pramipexole repurposing further.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

