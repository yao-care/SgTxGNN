---
layout: default
title: Amisulpride
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 10
---

# Amisulpride
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

# Amisulpride: From Unregistered Status to Schizophrenia Treatment in Singapore

## One-Sentence Summary

Amisulpride is a second-generation atypical antipsychotic of the substituted benzamide class, approved for schizophrenia in the European Union, Australia, and numerous other countries, but currently not registered in Singapore.
The TxGNN model predicts it may be effective for **Schizophrenia** — effectively validating its well-established global evidence base in the Singapore context —
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Singapore registration (drug not currently marketed in Singapore) |
| Predicted New Indication | Schizophrenia |
| TxGNN Prediction Score | 96.05% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Amisulpride is a highly selective dopamine receptor antagonist with a unique dual-dose mechanism of action. At higher doses (400–1,200 mg/day), it preferentially blocks postsynaptic D2/D3 receptors in the mesolimbic system, suppressing dopaminergic hyperactivity and alleviating positive symptoms such as hallucinations and delusions. At lower doses (50–300 mg/day), it preferentially blocks presynaptic D2/D3 autoreceptors, thereby disinhibiting dopamine release in the prefrontal cortex and improving negative symptoms — including blunted affect, social withdrawal, and avolition. Additionally, amisulpride exhibits 5-HT7 receptor antagonism, which further contributes to improvement of negative and affective symptoms. This mechanistic versatility distinguishes amisulpride from many other second-generation antipsychotics that rely primarily on broad 5-HT2A/D2 antagonism.

The dopamine hyperactivity hypothesis of schizophrenia — particularly excess mesolimbic D2 receptor stimulation — directly aligns with amisulpride's postsynaptic D2/D3 blocking mechanism. Its selective dopaminergic profile also affords a generally more favourable metabolic side-effect burden compared to agents such as clozapine or olanzapine, which is clinically meaningful for long-term maintenance therapy. The drug's ability to address both positive and negative symptom domains within a single agent represents a meaningful clinical advantage.

Amisulpride has been approved for schizophrenia in the European Union (marketed as Solian®), Australia, and numerous other markets for over two decades. A landmark 2013 Lancet network meta-analysis encompassing 212 trials and 43,049 patients ranked amisulpride among the most efficacious antipsychotics for overall schizophrenia outcomes. The high TxGNN prediction score (96.05%) reflects the robust mechanistic and clinical alignment between this drug and this indication, and the primary barrier to Singapore market access is regulatory — not evidentiary.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01105481](https://clinicaltrials.gov/study/NCT01105481) | Phase 4 | Completed | 273 | 14-week double-blind RCT of amisulpride augmentation therapy in clozapine-resistant schizophrenia; results (PMID 36253804) demonstrated significant improvement in psychopathology and cognitive performance versus placebo |
| [NCT04528095](https://clinicaltrials.gov/study/NCT04528095) | Phase 3 | Unknown | 162 | Sequential multiple-assignment RCT (SMART) comparing antipsychotic regimens including amisulpride in treatment-resistant schizophrenia; status requires follow-up for published outcomes |
| [NCT03510325](https://clinicaltrials.gov/study/NCT03510325) | Phase 3 | Completed | 762 | SMART design RCT evaluating antipsychotics including amisulpride for first-episode schizophrenia in real-world settings; assessed efficacy, adverse reactions, and pharmacoeconomics |
| [NCT01609153](https://clinicaltrials.gov/study/NCT01609153) | Phase 4 | Completed | 328 | COMBINE trial: double-blind RCT assessing whether olanzapine + amisulpride combination is superior to either monotherapy in acutely ill patients (results published in Lancet Psychiatry 2022) |
| [NCT01248195](https://clinicaltrials.gov/study/NCT01248195) | Phase 4 | Completed | 479 | OPTiMiSE study: optimising and individualising treatment in schizophrenia across Europe, with amisulpride as a primary first-line comparator arm |
| [NCT03451734](https://clinicaltrials.gov/study/NCT03451734) | N/A | Completed | 2,000 | Large multicentre Chinese observational study across 20 hospitals randomising first-episode schizophrenia patients to amisulpride or other second-generation antipsychotics over 8 weeks |
| [NCT05633108](https://clinicaltrials.gov/study/NCT05633108) | N/A | Completed | 579,728 | French national health insurance database study evaluating antipsychotic monotherapy versus polypharmacy (including amisulpride) on time to psychiatric rehospitalisation across psychotic disorders |
| [NCT01446328](https://clinicaltrials.gov/study/NCT01446328) | Phase 4 | Completed | 151 | Bergen Psychosis Project 2: independent, pragmatic head-to-head comparison of amisulpride, aripiprazole, and olanzapine with 12-month follow-up; assessed symptoms, side effects, and cognition |
| [NCT01795183](https://clinicaltrials.gov/study/NCT01795183) | Phase 4 | Completed | 316 | Prospective, open-label, multicentre study evaluating effectiveness and safety of amisulpride specifically in Chinese patients with schizophrenia — directly relevant to the Singapore population |
| [NCT00245674](https://clinicaltrials.gov/study/NCT00245674) | Phase 4 | Completed | 300 | Solian oral solution study: observing antipsychotic effect and safety profile of amisulpride solution during the first days of an acute schizophrenic episode |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23810019](https://pubmed.ncbi.nlm.nih.gov/23810019/) | 2013 | Network Meta-Analysis | Lancet | Leucht et al.: Among 15 antipsychotics across 212 trials (N=43,049), amisulpride ranked among the most efficacious agents for overall schizophrenia outcomes; established as first-tier treatment |
| [36253804](https://pubmed.ncbi.nlm.nih.gov/36253804/) | 2022 | RCT | Military Medical Research | 12-week double-blind RCT (n=273): amisulpride augmentation significantly improved PANSS scores and cognitive function in patients with clozapine-resistant treatment-refractory schizophrenia |
| [35276079](https://pubmed.ncbi.nlm.nih.gov/35276079/) | 2022 | RCT | Lancet Psychiatry | COMBINE trial (n=328): combination of amisulpride plus olanzapine demonstrated superior outcomes versus either monotherapy in acutely ill schizophrenia patients, informing polypharmacy practice |
| [39002529](https://pubmed.ncbi.nlm.nih.gov/39002529/) | 2024 | RCT | Schizophrenia Research | BeSt InTro substudy (n=126): compared remission rates across amisulpride, aripiprazole, and olanzapine; amisulpride showed competitive remission rates, supporting its use as a first-line SGA |
| [33069317](https://pubmed.ncbi.nlm.nih.gov/33069317/) | 2020 | Pragmatic RCT | Lancet Psychiatry | BeSt InTro trial: first independent, rater-blind, pragmatic head-to-head trial of amisulpride vs aripiprazole vs olanzapine; amisulpride demonstrated competitive efficacy and safety over 12 months |
| [30115598](https://pubmed.ncbi.nlm.nih.gov/30115598/) | 2018 | RCT | Lancet Psychiatry | OPTiMiSE three-phase switching study: amisulpride as first-line agent achieved symptomatic remission in approximately 47% of first-episode schizophrenia patients at 10 weeks |
| [29368205](https://pubmed.ncbi.nlm.nih.gov/29368205/) | 2018 | Systematic Review | Eur Arch Psychiatry Clin Neurosci | Antipsychotics for predominant or prominent negative symptoms: amisulpride identified as one of the most efficacious options for this clinically challenging symptom domain |
| [30185173](https://pubmed.ncbi.nlm.nih.gov/30185173/) | 2018 | Meta-Analysis | BMC Psychiatry | Amisulpride vs olanzapine for schizophrenia in China (systematic review + meta-analysis): comparable efficacy with more favourable metabolic profile for amisulpride; cost-minimisation analysis supports amisulpride |
| [36368055](https://pubmed.ncbi.nlm.nih.gov/36368055/) | 2022 | Review | Expert Opinion on Pharmacotherapy | Update on novel antipsychotics and strategies for treatment-resistant schizophrenia; amisulpride augmentation (particularly add-on to clozapine) reviewed as a clinically supported strategy |
| [12685918](https://pubmed.ncbi.nlm.nih.gov/12685918/) | 2002 | Review | Int Clinical Psychopharmacology | Seminal review establishing the mechanistic rationale for amisulpride's dual-dose dopaminergic effects; addresses dosage optimisation for positive versus negative symptom targets |

---

## Singapore Market Information

Amisulpride currently holds **no approved product registrations** with the Health Sciences Authority (HSA) of Singapore. The drug is not available as a locally licensed medicinal product. There are no authorisation numbers, approved dosage forms, or registered indications on record.

Clinicians wishing to prescribe amisulpride in Singapore would need to access it through the HSA Special Access Route (SAR) or similar regulatory pathway pending formal product registration.

---

## Safety Considerations

Please refer to the package insert for safety information. Formal TFDA/HSA-specific warnings, contraindications, and drug–drug interaction data were not available in this evidence pack.

Based on the established pharmacological profile of amisulpride as a selective D2/D3 antagonist, the following clinically important safety considerations are known from the approved EU/Australian prescribing information and published literature:

- **Hyperprolactinaemia**: Class effect of D2 receptor blockade; may manifest as galactorrhoea, amenorrhoea, or sexual dysfunction — monitor prolactin in long-term users
- **QTc prolongation**: Amisulpride carries dose-dependent QTc-prolonging effects; baseline and periodic ECG monitoring is recommended, particularly at higher doses and in patients with cardiac risk factors
- **Extrapyramidal symptoms (EPS)**: Risk is lower than first-generation antipsychotics but increases with dose; akathisia and parkinsonism may occur
- **Metabolic profile**: Generally more favourable than clozapine or olanzapine, with lower risk of weight gain and dyslipidaemia — an advantage for long-term schizophrenia management

For definitive prescribing guidance, consult the approved EU Summary of Product Characteristics (SmPC) or Australian Product Information for Solian®.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Amisulpride has robust Level 1 evidence for schizophrenia — supported by multiple completed Phase 3 and Phase 4 RCTs, a landmark Lancet network meta-analysis, regulatory approval in the EU and Australia, and over two decades of post-marketing real-world data. The primary barrier to Singapore use is the absence of local HSA registration, not a lack of clinical evidence.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate a New Drug Application (NDA) to HSA or utilise the Special Access Route (SAR) for immediate clinical access while registration is pursued
- **Complete safety documentation**: Obtain full prescribing information from an approved jurisdiction (EU SmPC or Australian PI); assess TFDA/HSA-specific requirements for warnings and contraindications
- **Drug–drug interaction assessment**: Compile the DDI profile (particularly for QTc-prolonging co-medications common in Singapore's patient population) before routine prescribing
- **Local population data**: Consider a local post-marketing surveillance plan given the Asian population context (PK differences in CYP450 metabolism may warrant dose-adjustment guidance)
- **Cardiac safety protocol**: Establish institutional ECG monitoring protocols given amisulpride's known QTc-prolongation risk
- **Pharmacoeconomic evaluation**: Benchmark cost-effectiveness against currently available antipsychotics in Singapore to support formulary inclusion decisions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

