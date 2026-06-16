---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 354
evidence_level: L5
indication_count: 10
---

# Duloxetine
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

# Duloxetine: From Major Depressive Disorder to Obsessive-Compulsive Disorder

## One-Sentence Summary

Duloxetine is a serotonin-norepinephrine reuptake inhibitor (SNRI) approved globally for major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, fibromyalgia, and chronic musculoskeletal pain. The TxGNN model predicts it may be effective for **Obsessive-Compulsive Disorder (OCD)** — the highest-ranked prediction with substantive clinical evidence — with **5 clinical trials** (including 1 completed Phase 4 trial directly targeting OCD and 1 double-blind RCT) and **20 publications** currently supporting this direction. Duloxetine is not currently registered in Singapore, and the evidence base, while promising, falls short of a powered Phase 3 standard.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Major depressive disorder, generalized anxiety disorder, diabetic peripheral neuropathic pain, fibromyalgia, chronic musculoskeletal pain (globally approved; no Singapore HSA registration found) |
| Predicted New Indication | Obsessive-Compulsive Disorder (OCD) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not returned by the DrugBank query in this Evidence Pack. Based on information embedded in the retrieved literature, duloxetine is a **dual serotonin and norepinephrine reuptake inhibitor (SNRI)**: it simultaneously blocks the reuptake transporters for both 5-HT and NE, raising synaptic concentrations of both monoamines. This dual action distinguishes it from pure SSRIs, which act only on the serotonin transporter.

The connection to OCD is mechanistically sound. OCD pathophysiology centres on hyperactivation of the **cortico-striato-thalamo-cortical (CSTC) circuit**, driven in large part by serotonergic dysregulation. SSRIs — which share duloxetine's serotonergic mechanism — are the established first-line pharmacotherapy for OCD and are effective in approximately 40–60% of patients. For the remaining treatment-resistant cases, the additional noradrenergic component of duloxetine offers a rational augmentation strategy: NE modulation may further dampen pathological CSTC hyperactivity through prefrontal top-down control circuits.

Critically, this prediction is not purely theoretical. A completed Phase 4 trial (NCT00464698) directly evaluated duloxetine in OCD patients; a double-blind placebo-controlled augmentation trial (PMID 27811556) produced positive signals in treatment-resistant OCD; and a series of open-label studies and case reports have documented clinically meaningful responses. The convergence of a plausible mechanism and multiple, independently published clinical data points places OCD in a meaningfully different category from the other high-ranking TxGNN predictions in this pack (most of which are L5 with zero supporting evidence).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | Completed | 20 | The only registered trial with duloxetine efficacy for OCD as its primary objective. Completed over ~8 years; provides direct proof-of-concept data despite modest sample size |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | Completed | 26 | OCD medication response prediction study; duloxetine included as a third-arm treatment option alongside clomipramine and escitalopram for patients who had previously tried standard agents; provides comparative efficacy signal |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | Unknown | 8,800 | Large individual patient data meta-analysis of antidepressant efficacy across anxiety disorders; broad scope covers OCD-relevant populations and offers high-level indirect supporting context |

> Trials NCT05930912 (ASD psychoanalysis, n=1) and NCT01944657 (TMS for depression, withdrawn, n=0) were retrieved by the query but are not relevant to OCD and are excluded.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | Double-blind RCT (augmentation) | J Clin Psychopharmacol | Duloxetine augmentation in treatment-resistant OCD; double-blind controlled design; positive efficacy signal in patients who failed SRI monotherapy |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-review | Frontiers in Psychiatry | Systematic meta-review of antidepressants (including SNRIs) in children and adolescents across ADHD, anxiety, OCD, MDD; assesses efficacy, tolerability, and suicidality risk |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | OCD shows reduced antidepressant and placebo response relative to other anxiety disorders; essential context for setting realistic efficacy expectations when repurposing duloxetine |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label Trial | Int J Neuropsychopharmacol | Open-label investigation of duloxetine efficacy in DSM-IV OCD; exploratory but provides direct clinical experience data |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Systematic Review | Frontiers in Psychiatry | Systematic review of duloxetine use in psychiatric disorders beyond approved indications; dedicated coverage of OCD evidence base and dose considerations |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | Case Report | Cureus | Supratherapeutic duloxetine combined with CBT for severe treatment-resistant OCD with comorbid MDD in a 42-year-old male; sustained symptom improvement documented after over a decade of treatment failure |
| [22567604](https://pubmed.ncbi.nlm.nih.gov/22567604/) | 2012 | Case Report | Innov Clin Neurosci | Suprathreshold duloxetine for comorbid treatment-resistant OCD, anorexia nervosa binge-purging type, and depression; raises hypothesis that dose escalation may matter in complex comorbidity |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case Series | J Psychopharmacol | Switching from SRIs to duloxetine in resistant OCD patients; case series documenting clinical outcomes and tolerability of the transition strategy |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical Review | J Clin Psychiatry | Critical review of SNRI antiobsessional properties (venlafaxine and clomipramine as comparators); foundational literature establishing the theoretical rationale for duloxetine in OCD |
| [17632660](https://pubmed.ncbi.nlm.nih.gov/17632660/) | 2007 | Case Report | Prim Care Companion J Clin Psychiatry | First published case of OCD responding to duloxetine; early clinical signal predating the formal trial programme |

---

## Singapore Market Information

Duloxetine currently has **no product registrations** with the Health Sciences Authority (HSA) of Singapore. The drug is not marketed and has no active licenses in Singapore. Any clinical use would require either HSA market authorization or a Special Access Route (SAR) application before proceeding.

---

## Safety Considerations

Please refer to the package insert for safety information. Safety data (key warnings, contraindications, and drug-drug interactions) were not returned in this Evidence Pack due to query gaps and should be obtained directly from the prescribing information before any clinical decision is made.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
OCD has a biologically coherent mechanistic link to duloxetine's SNRI profile, and the evidence base — one completed Phase 4 trial, one double-blind augmentation RCT, one open-label trial, and a series of independently published case reports and reviews — represents the most substantive clinical foundation among all 10 TxGNN-predicted indications in this pack. However, the largest dedicated trial enrolled only 20 patients, the RCT focused on augmentation in treatment-resistant cases rather than first-line monotherapy, and duloxetine is not registered in Singapore. Proceeding requires defined guardrails rather than immediate clinical adoption.

**To proceed, the following is needed:**

- **Safety data gap resolution**: Obtain full prescribing information (package insert) to extract key warnings, contraindications, and drug-drug interactions — this is currently a blocking gap
- **MOA confirmation**: Query DrugBank API for the formal mechanism of action entry (DB00476) to support regulatory submissions
- **Singapore HSA pathway**: Evaluate HSA registration requirements or Special Access Route eligibility, as the drug has zero existing licenses in Singapore
- **Trial design**: Commission a powered Phase 2 randomised controlled trial (estimated n ≥ 80–120) focused on either treatment-naive OCD or treatment-resistant OCD (augmentation strategy appears particularly promising based on PMID 27811556)
- **Patient stratification**: Define target population clearly — evidence suggests augmentation in SRI-resistant patients may be the highest-yield entry point
- **Dose-finding**: Existing case reports suggest supratherapeutic dosing may be relevant in resistant cases; a formal dose-finding component should be considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

