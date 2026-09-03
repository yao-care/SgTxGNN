---
layout: default
title: Paroxetine
parent: 僅模型預測 (L5)
nav_order: 757
evidence_level: L5
indication_count: 10
---

# Paroxetine
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

Using no additional tools — this is a direct content-generation task from the provided Evidence Pack; I'll write the report following the specified template, prioritizing the evidence pack's own risk-flagging (the pipeline explicitly marks the top TxGNN-ranked "Ohdo syndrome" hit as likely embedding noise) over blindly using rank 1.

---

# Paroxetine: From SSRI Antidepressant Use to Agoraphobia (Panic Disorder)

## One-Sentence Summary

Paroxetine (DrugBank DB00715) is a selective serotonin reuptake inhibitor (SSRI) whose established therapeutic domain is depression and anxiety-spectrum disorders. Among TxGNN's ten candidate indications, the best-evidenced signal is **Agoraphobia (Panic Disorder)**, supported by **4 clinical trials** (all Grade A, Phase 3/4, completed) and **20 publications**. This is worth flagging plainly: the model's single *highest-scoring* candidate, "Ohdo syndrome and variants," is explicitly labeled by the evidence pipeline itself as likely embedding-similarity noise (a "paroxysmal"/"paroxetine" string artifact), not a genuine repurposing signal — so the headline result here reflects the strongest real evidence in the pack, not the top raw TxGNN score.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in this evidence pack (no Singapore license text — drug is unregistered locally); Paroxetine is broadly established as an SSRI antidepressant/anxiolytic |
| Predicted New Indication | Agoraphobia (Panic Disorder) |
| TxGNN Prediction Score | 97.76% |
| Evidence Level | L1 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in this evidence pack (flagged as a High-severity data gap, DG002). Based on general pharmacological knowledge, paroxetine is a phenylpiperidine-class SSRI that selectively inhibits presynaptic serotonin reuptake, increasing synaptic 5-HT availability, with minimal affinity for adrenergic, dopaminergic, histaminergic, or cholinergic receptors.

Agoraphobia most commonly presents as a component of panic disorder, which is driven by dysregulated serotonergic modulation of amygdala-centered fear circuitry. This is not a mechanistically distant "new" indication — paroxetine is already one of the first SSRIs approved internationally specifically for panic disorder with agoraphobia, so the TxGNN signal here largely reconfirms an existing, clinically validated use rather than proposing a novel therapeutic hypothesis.

By contrast, several other high-scoring candidates in this pack (Ohdo syndrome and its variant "blepharophimosis–intellectual disability syndrome, Ohdo type," benign paroxysmal torticollis of infancy, and several personality disorders) have **no supporting clinical trials or literature**, and the pipeline's own rationale attributes them to knowledge-graph embedding proximity or lexical similarity rather than biological plausibility.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02852577](https://clinicaltrials.gov/study/NCT02852577) | Phase 4 | Completed | 120 | Long-term, naturalistic RCT of clonazepam vs. paroxetine in panic disorder with/without agoraphobia; evaluated short-term, long-term, and post-treatment efficacy |
| [NCT00677352](https://clinicaltrials.gov/study/NCT00677352) | Phase 4 | Completed | 321 | Multicenter double-blind RCT comparing sertraline vs. paroxetine for efficacy and safety in panic disorder |
| [NCT00540098](https://clinicaltrials.gov/study/NCT00540098) | Phase 4 | Completed | 75 | RCT of paroxetine vs. placebo combined with aerobic exercise or relaxation training for panic disorder |
| [NCT00000368](https://clinicaltrials.gov/study/NCT00000368) | Phase 3 | Completed | 379 | Long-term treatment strategy trial evaluating maintenance CBT with/without medication for panic disorder |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Network meta-analysis of pharmacological treatments for panic disorder in adults |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12-week placebo-controlled comparison of paroxetine, clomipramine, and cognitive therapy for panic disorder with/without agoraphobia |
| [15669886](https://pubmed.ncbi.nlm.nih.gov/15669886/) | 2005 | RCT | J Clin Psychiatry | Efficacy and tolerability of controlled-release paroxetine in panic disorder |
| [11110016](https://pubmed.ncbi.nlm.nih.gov/11110016/) | 2000 | Review | Int Clin Psychopharmacol | Review of SSRIs (paroxetine among others) in panic disorder and agoraphobia treatment |
| [23338224](https://pubmed.ncbi.nlm.nih.gov/23338224/) | 1997 | Review | CNS Drugs | Pharmacology and therapeutic potential of paroxetine in panic disorder management |
| [12877016](https://pubmed.ncbi.nlm.nih.gov/12877016/) | 2003 | Review | Ryoikibetsu Shokogun Shirizu | Panic disorder and agoraphobia overview |
| [15089103](https://pubmed.ncbi.nlm.nih.gov/15089103/) | 2004 | Review | CNS Drugs | Controlled-release paroxetine efficacy across MDD, social anxiety, PMDD |
| [26400133](https://pubmed.ncbi.nlm.nih.gov/26400133/) | 2015 | Cohort | Psychiatria Danubina | Ghrelin and lipid levels in panic disorder with/without agoraphobia, pre/post treatment |
| [39295933](https://pubmed.ncbi.nlm.nih.gov/39295933/) | 2024 | Case Report | Front Pharmacol | CYP2D6 phenoconversion in protracted paroxetine intoxication |
| [29875534](https://pubmed.ncbi.nlm.nih.gov/29875534/) | 2018 | Case Report/Review | Indian J Psychol Med | Bowel and bladder anxiety as a possible agoraphobia variant |

## Singapore Market Information

Paroxetine currently has **no HSA registration on file** in this evidence pack (`market_status`: 未上市, `total_licenses`: 0). No authorization records, product names, or approved indication text are available to summarize.

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug-drug interaction data were retrievable in this evidence pack (DDI query: not found). This is recorded as a **Blocking** data gap (DG001) — TFDA/HSA label warnings and contraindications must be obtained before this candidate can enter a formal safety pre-assessment (S1).

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (evidence-stage assessment only — see safety caveat below)

**Rationale:**
- Agoraphobia/panic disorder is supported by L1-tier evidence (4 completed Phase 3/4 RCTs, all Grade A relevance, plus 20 supporting publications), and mechanistically this reflects paroxetine's core SSRI action rather than a speculative new mechanism.
- However, this evidence-level assessment is independent of the drug-level safety data gap (DG001), which is Blocking severity — the two should not be conflated when finalizing a go/no-go decision.

**To proceed, the following is needed:**
- TFDA/HSA package insert (warnings, contraindications) — Blocking gap, required before S1 safety pre-assessment
- Detailed mechanism-of-action documentation from DrugBank (High-severity gap)
- Drug-drug interaction profile (current query returned no results)
- Singapore regulatory pathway assessment, since paroxetine is not currently registered/marketed locally
- Clarification on whether "Agoraphobia" as a repurposing target is distinct enough from paroxetine's existing internationally-approved panic disorder indication to warrant a repurposing submission versus a standard new-registration pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

