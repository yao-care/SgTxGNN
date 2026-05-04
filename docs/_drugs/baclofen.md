---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Baclofen
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

# Baclofen: From Muscle Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist widely used internationally for muscle spasticity in multiple sclerosis and spinal cord injury, though it is **not currently registered in Singapore**.
The TxGNN model ranks **attention deficit-hyperactivity disorder (ADHD)** as the top predicted new indication (score 99.32%), yet the supporting evidence consists entirely of indirect publications with no registered clinical trials.
In this 10-indication panel, **nicotine dependence (rank 2)** carries the strongest clinical signal — 3 Phase 2 trials and 20 publications — and is the primary actionable candidate; ADHD itself remains at the hypothesis stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Muscle spasticity (MS, spinal cord injury) — not registered in Singapore |
| Predicted New Indication | Attention deficit-hyperactivity disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (ADHD) / Proceed with Guardrails (Nicotine Dependence) |

---

## Full Prediction Summary

| Rank | Disease | TxGNN Score | Trials | Literature | Evidence | Decision |
|------|---------|-------------|--------|-----------|----------|----------|
| 1 | Attention deficit-hyperactivity disorder | 99.32% | 0 | 10 | L4 | Hold |
| 2 | Nicotine dependence | 99.19% | 3 | 20 | L3 | Proceed with Guardrails |
| 3 | ADHD, inattentive type | 98.89% | 0 | 0 | L5 | Hold |
| 4 | Myofascial pain syndrome | 98.87% | 1 relevant* | 4 | L3 | Research Question |
| 5 | Faciodigitogenital syndrome | 98.78% | 0 | 0 | L5 | Hold ⚠️ Likely false positive |
| 6 | Trigeminal nerve neoplasm | 98.70% | 0 | 2† | L4 | Hold ⚠️ ICD mismatch |
| 7 | Methemoglobinemia | 98.33% | 0 | 1 | L5 | Hold ⚠️ Likely false positive |
| 8 | Chondromyxoid fibroma | 98.15% | 0 | 0 | L5 | Hold ⚠️ Likely false positive |
| 9 | Methemoglobinemia, alpha type | 97.97% | 0 | 0 | L5 | Hold ⚠️ Likely false positive |
| 10 | Specific developmental disorder | 97.95% | 1 relevant‡ | 2 | L4 | Hold |

\* NCT07442786 (tDCS for alcohol use disorder) is a data mismatch and excluded; only NCT05617118 is relevant.
† Both publications describe trigeminal **neuralgia** (pain disorder), not trigeminal nerve **neoplasm** — probable ICD coding error in the knowledge graph.
‡ NCT04618978 (spinal cord injury/sleep study) is unrelated; only NCT03682978 (arbaclofen in ASD) is potentially relevant.

> **Quality note**: Ranks 5, 7, 8, and 9 have no known mechanistic connection between GABA-B agonism and the target pathology. These are assessed as TxGNN false positives arising from non-specific knowledge-graph neighbor propagation.

---

## Rank 1: ADHD — Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, baclofen is a GABA-B receptor agonist that reduces presynaptic neurotransmitter release by inhibiting voltage-gated calcium channels and activating inwardly-rectifying potassium channels, thereby suppressing excessive neuronal excitability across multiple circuits.

The theoretical case for ADHD rests on GABA-B receptor expression in the prefrontal cortex (PFC), the brain region most implicated in ADHD pathophysiology. PFC governs executive function, working memory, and inhibitory control — precisely the domains disrupted in ADHD. GABAergic modulation could theoretically stabilize dopaminergic and noradrenergic transmission in these circuits. One animal study (PMID 21300040) directly administered baclofen to spontaneously hypertensive rats (a validated ADHD model) and observed altered EEG activity in the frontal cortex and hippocampus, providing a mechanistic foothold.

However, the critical weakness is that ADHD and Tourette syndrome frequently co-occur (30–50% comorbidity), and the majority of retrieved publications concern TS management rather than direct ADHD treatment. No paper directly randomises ADHD patients to baclofen. The prediction therefore remains at the level of a theoretically plausible hypothesis requiring prospective human data before further development.

---

## Clinical Trial Evidence (ADHD, Rank 1)

Currently no related clinical trials registered for baclofen in ADHD.

---

## Literature Evidence (ADHD, Rank 1)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Efficacy of behavioural interventions, antipsychotics, and alpha agonists for tics in Tourette's syndrome (frequent ADHD comorbidity); baclofen not directly reviewed |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | Baclofen directly tested in SHR (ADHD model) and kainate-treated rats via intracerebroventricular EEG; altered frontal cortex and hippocampus oscillations observed |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurology | 450 Tourette/tic patients treated with baclofen ± botulinum toxin A; the only paper with direct baclofen clinical data in this literature set |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Narrative Review | Clinical Neuropharmacology | Mood stabilisers in ASD children/adolescents; addresses overlapping ADHD behavioural symptoms |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiology | Emerging treatments for Tourette syndrome including ADHD comorbidity management |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Clinical Review | Paediatric Drugs | TS clinical features and current management, noting ADHD as a leading comorbid condition |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | α2A-adrenergic stimulation in ventral hippocampus reduces impulsive decision-making — ADHD-relevant mechanism, no baclofen |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Anterior cingulate cortex and amygdala dissociable roles in effortful decision-making deficits seen in ADHD |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | Eur J Neuroscience | Habenula modulates monoaminergic neurotransmission and social play; neurodevelopmental relevance to ADHD |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical Commentary | L'Encéphale | Off-label methylphenidate prescribing in adult ADHD — pharmacotherapy landscape context only |

> ⚠️ **Important caveat**: Only PMID 10342599 reports any clinical baclofen use (in Tourette syndrome, not ADHD), and only PMID 21300040 directly tests baclofen in a validated ADHD animal model. The remaining 8 papers are tangential references. This literature set does **not** constitute evidence for baclofen efficacy in ADHD.

---

## Rank 2: Nicotine Dependence — The Best-Supported Prediction

### Why This Mechanism Works

Baclofen activates presynaptic GABA-B receptors on dopaminergic neurons in the ventral tegmental area (VTA), suppressing voltage-gated calcium channel activity and reducing nicotine-induced dopamine release in the nucleus accumbens. This directly blunts the mesolimbic reward signal that maintains nicotine addiction — weakening drug craving, conditioned cue reactivity, and physical withdrawal symptoms. The mechanism has been replicated across conditioned place preference, self-administration, and extinction-reinstatement animal paradigms, and a completed Phase 2 fMRI study confirmed attenuated brain responses to smoking cues in human smokers. This is the mechanistically clearest and clinically best-supported indication in the entire panel.

### Clinical Trial Evidence (Nicotine Dependence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | Completed | 44 | Perfusion fMRI with dopaminergic gene polymorphism analysis; evaluated baclofen's effect on brain activation to appetitive smoking cues; most rigorous design in this panel — full results needed |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Assessed baclofen for reduction of smoking urge, withdrawal, and reinforcement in moderate-to-heavy smokers; terminated early — reason requires clarification |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Randomised placebo-controlled trial of baclofen for nicotine abstinence (planned n=120); enrolled only 6 patients — effectively a failed trial with no statistical inference possible |

### Literature Evidence (Nicotine Dependence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal Study | Psychopharmacology | Baclofen attenuates nicotine rewarding properties and physical withdrawal manifestations in rodents |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal Study | Eur Neuropsychopharmacology | Baclofen prevents drug-induced reinstatement of nicotine-seeking behaviour and conditioned place preference |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Animal Study | Prog Neuro-Psychopharmacology | Baclofen prevents mecamylamine-precipitated nicotine withdrawal and normalises α4β2 nicotinic receptor density in mice |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal Study | Neuroscience Letters | Baclofen reduces nicotine-induced conditioned place preference at 3 mg/kg; modest selectivity over general locomotion |
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Conference Abstract | Neuropsychopharmacology | Double-blind placebo-controlled RCT of baclofen for concurrent alcohol and nicotine dependence — direct human evidence, abstract only |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B receptors and positive allosteric modulators as therapeutic targets across substance use disorders |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for tobacco cessation — baclofen identified as investigational agent |
| [24654737](https://pubmed.ncbi.nlm.nih.gov/24654737/) | 2014 | Review | Expert Opin Emerging Drugs | 2014 update on emerging pharmacotherapies for tobacco dependence |
| [17338593](https://pubmed.ncbi.nlm.nih.gov/17338593/) | 2007 | Review | CNS Drugs | Pharmacotherapy for dual substance abuse including nicotine and alcohol — single-drug GABA strategies discussed |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review | Int Rev Neurobiology | Drug repurposing for alcohol use disorder — baclofen's GABA-B mechanism placed in broader addiction pharmacology context |

---

## Rank 4: Myofascial Pain Syndrome — Snapshot

**Evidence Level**: L3 | **Decision**: Research Question

Baclofen's GABA-B agonism inhibits spinal α-motor neuron activity, reducing excessive muscle tone and theoretically deactivating the trigger points that perpetuate myofascial pain cycles. A Russian clinical series (PMID 18577932; "baclosan" = baclofen's Russian brand name) directly administered baclofen to 20 dorsopathy patients with myofascial-tonic pain syndromes, demonstrating clinical benefit when added to standard physiotherapy. One clinical trial (NCT05617118) directly compares oral baclofen versus botulinum toxin A injection for pelvic myofascial pain syndrome (n=52, planned completion May 2024), but its current status is listed as "Unknown" — confirmation of completion and data retrieval are priority actions.

> ⚠️ NCT07442786 (tDCS for alcohol use disorder, n=312) was erroneously paired with this indication and has been excluded from this analysis.

---

## Singapore Market Information

Baclofen is **not currently registered in Singapore**. No product authorisations on file as of the data cutoff (2026-04-10).

> **Context**: In markets where baclofen is registered — the United States (FDA), European Union (EMA), Australia (TGA), United Kingdom (MHRA), and Japan (PMDA) — it is approved for spasticity treatment via oral tablets (10 mg, 20 mg) and intrathecal infusion for severe refractory cases. Any indication expansion in Singapore would first require completion of drug registration for the base indication.

---

## Safety Considerations

Safety data is not available in this Evidence Pack (Singapore package insert data not retrieved; DDI query returned no results).

> Please refer to the package insert for safety information. Based on published pharmacological literature, key safety considerations for baclofen include:
>
> - **CNS depression**: Sedation, dizziness, and muscle weakness — dose-dependent and particularly relevant in elderly patients
> - **Withdrawal risk**: Abrupt discontinuation can precipitate seizures, hallucinations, and hyperthermia — gradual dose tapering is mandatory
> - **Renal elimination**: Baclofen is primarily renally cleared; dose adjustment is essential in renal impairment
> - **Overdose**: High doses may cause respiratory depression and coma
>
> Formal DDI screening and retrieval of the complete product label are required before any clinical use assessment.

---

## Conclusion and Next Steps

### Rank 1 — ADHD

**Decision: Hold**

**Rationale:**
No clinical trials have tested baclofen in ADHD, and all 10 retrieved publications are indirect references (Tourette comorbidity literature, animal impulsivity models). The mechanistic hypothesis is plausible but unvalidated in human subjects. With Singapore registration also absent, the prerequisites for any clinical programme are not yet met.

**To proceed, the following is needed:**
- Design a proof-of-concept pilot study (n=20–40) testing baclofen in ADHD patients using validated rating scales (ADHD-RS, Conners)
- Generate direct preclinical data in ADHD models (SHR or DAT-knockdown rodents) specifically evaluating attentional and inhibitory outcomes with baclofen
- Resolve the MOA data gap via DrugBank API query (DG002)
- Initiate Singapore drug registration for baclofen (base indication: spasticity) as a prerequisite

---

### Rank 2 — Nicotine Dependence

**Decision: Proceed with Guardrails**

**Rationale:**
Nicotine dependence combines mechanistically coherent GABA-B receptor biology, robust multi-model animal validation, and one completed Phase 2 human trial. Two of three trials terminated early (one critically underpowered at n=6), limiting definitive conclusions, but the completed fMRI trial (NCT01821560) represents the highest-quality direct evidence in this panel. Singapore registration of baclofen remains the foundational prerequisite.

**To proceed, the following is needed:**
- Retrieve and critically appraise the full published results from NCT01821560 (completed 2017)
- Clarify early termination reasons for NCT00257894 (safety? funding? efficacy?) — this substantially affects the risk-benefit interpretation
- Conduct a formal systematic review and meta-analysis of baclofen for nicotine dependence (animal + human data)
- Pursue Singapore registration of baclofen for spasticity as a precondition for any off-label or expanded indication programme
- Design a powered Phase 2/3 RCT (target n ≥ 120) with pre-specified abstinence endpoints at 12 and 26 weeks

---

### Rank 4 — Myofascial Pain Syndrome

**Decision: Research Question**

**To proceed, the following is needed:**
- Confirm NCT05617118 completion status and retrieve primary endpoint results (oral baclofen vs. botulinum toxin A, n=52)
- Commission a targeted systematic review of muscle relaxants in myofascial pain syndrome, with baclofen as a focal agent
- Clarify the scope of the intended indication (localised pelvic vs. generalised myofascial pain) to define an appropriate development pathway
- Address Singapore registration gap (same prerequisite as above)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

