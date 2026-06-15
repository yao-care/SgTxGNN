---
layout: default
title: Bromazepam
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Bromazepam
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

# Bromazepam: From Anxiety Disorders to Migraine Disorder

## One-Sentence Summary

Bromazepam is a 1,4-benzodiazepine positive allosteric modulator of GABA-A receptors, historically prescribed across multiple countries as an anxiolytic for generalised anxiety disorder and related conditions.
The TxGNN model predicts it may be effective for **Migraine Disorder** (rank 1, prediction score 99.06%), though the single identified clinical trial carries **negative directional relevance** and no supporting literature exists for this indication.
Notably, the sixth-ranked prediction — **anxiety** — is supported by multiple placebo-controlled RCTs directly studying bromazepam and achieves an L2 evidence level, making it the most actionable finding in this analysis despite being bromazepam's historically established use.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anxiety disorders (generalised anxiety; known pharmacological use — not registered in Singapore) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L4 — no direct supportive clinical data for migraine |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bromazepam is a member of the 1,4-benzodiazepine class that enhances inhibitory neurotransmission by potentiating GABA-A receptor chloride conductance. Although detailed MOA data was not retrieved in this evidence pack, the pharmacology of the class is well-established: bromazepam shows preferential activity at α2- and α3-containing GABA-A receptor subtypes, which are associated with anxiolytic and muscle-relaxant effects, while displaying lower α1 selectivity compared to z-drugs such as zolpidem. The broad GABAergic inhibition it produces underlies its anxiolytic, sedative, muscle relaxant, and anticonvulsant properties.

The mechanistic link between bromazepam and migraine is indirect and contentious. Benzodiazepines can provide adjunctive sedation and anxiolysis that may reduce acute migraine distress, and GABAergic modulation has been explored peripherally in headache research. However, the core pathophysiology of migraine — cortical spreading depression (CSD), trigeminovascular system activation, and calcitonin gene-related peptide (CGRP) release — is not addressed by GABA-A modulation. There is no established pharmacodynamic pathway from bromazepam's mechanism to any recognised acute or prophylactic anti-migraine effect.

Critically, the one clinical trial retrieved (NCT04410536) studied **medication overuse headache (MOH) withdrawal** using a behavioural home-based programme. In this context, bromazepam is likely one of the **overused substances being withdrawn**, not the therapeutic agent. This creates a directional paradox: the available clinical evidence suggests bromazepam may **contribute to** MOH rather than treat migraine, making the TxGNN rank-1 prediction almost certainly an artefact of knowledge graph co-occurrence within the neurological domain rather than a true therapeutic signal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT04410536](https://clinicaltrials.gov/study/NCT04410536) | Phase 4 | Completed | 25 | Home-withdrawal programme combined with behavioural therapy for medication overuse headache (MOH) during the COVID-19 emergency; followed patients at one year for relapse rates. Bromazepam is likely one of the overused medications being discontinued — **directional relevance is negative** for repurposing as a migraine treatment. |

---

## Literature Evidence

Currently no related literature available for bromazepam in migraine disorder.

---

## Singapore Market Information

Bromazepam is **not registered** in Singapore. No HSA product authorisations are on record.

---

## Safety Considerations

Formal safety data from Singapore/HSA-approved labelling was not retrieved in this evidence pack. Based on the established pharmacology of the benzodiazepine class and available pharmacokinetic literature, the following is known:

- **Key Warnings (class-based):** Physical and psychological dependence with prolonged use; withdrawal syndrome on abrupt discontinuation (seizures, rebound anxiety); CNS and respiratory depression, particularly in combination with opioids, alcohol, or other CNS depressants; impaired psychomotor performance and cognitive function; risk of medication overuse headache with chronic use in headache patients
- **Contraindications (class-based):** Myasthenia gravis; severe respiratory insufficiency; obstructive sleep apnoea syndrome; severe hepatic impairment; acute narrow-angle glaucoma
- **Drug Interactions:** CYP3A4 inhibitors (e.g. itraconazole) significantly increase bromazepam plasma concentrations and pharmacodynamic effects, as documented in a controlled pharmacokinetic study (PMID [14517708](https://pubmed.ncbi.nlm.nih.gov/14517708/)); additive CNS depression with alcohol and sedatives

> For complete and Singapore-specific safety information, please refer to the applicable package insert and HSA regulatory guidance.

---

## Conclusion and Next Steps

**Decision: Hold** *(for migraine disorder as a repurposing target)*

**Rationale:**
No mechanistic pathway links bromazepam's GABA-A modulation to migraine pathophysiology, and the only clinical trial identified suggests an inverse relationship — bromazepam may be a cause of medication overuse headache rather than a treatment. Development for this indication is not recommended at this stage.

---

**Important secondary finding — Anxiety (Rank 6, L2 evidence):**

Although anxiety is bromazepam's historically established indication rather than a novel repurposing target, TxGNN independently identified it with multiple supporting placebo-controlled RCTs that **directly studied bromazepam**:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6132936](https://pubmed.ncbi.nlm.nih.gov/6132936/) | 1983 | RCT (placebo-controlled) | J Clin Psychopharmacology | Bromazepam 18 mg/day significantly superior to diazepam and placebo in generalised anxiety disorder over 4 weeks; greater efficacy on somatic anxiety subscale |
| [2880459](https://pubmed.ncbi.nlm.nih.gov/2880459/) | 1986 | RCT (placebo-controlled) | Acta Psychiatrica Scandinavica | Bromazepam and lorazepam both superior to placebo in 60 outpatients with GAD; bromazepam associated with less mood depression than lorazepam |
| [1969172](https://pubmed.ncbi.nlm.nih.gov/1969172/) | 1990 | RCT (multicentre) | Psychopharmacology | Bromazepam significantly superior to placebo and non-inferior to chlorprothixene in 245 GAD patients; Hamilton Anxiety reduction median 12 points |
| [13969](https://pubmed.ncbi.nlm.nih.gov/13969/) | 1977 | RCT (active-comparator) | Diseases of the Nervous System | Bromazepam 23.8 mg/day vs. amitriptyline and placebo in anxiety-depressive neurosis; bromazepam showed early and sustained improvement on BPRS and Hamilton scales |
| [710](https://pubmed.ncbi.nlm.nih.gov/710/) | 1975 | RCT | Psychopharmacologia | Controlled crossover study of bromazepam cognitive and sedative effects; characterised bromazepam's CNS pharmacodynamic profile |

---

**To proceed with any further evaluation, the following is needed:**

1. **Regulatory gap closure:** Retrieve TFDA/HSA package insert for complete warnings and contraindications (Data Gap DG001 — currently Blocking)
2. **MOA documentation:** Retrieve DrugBank API data for bromazepam receptor binding profile, including GABA-A subunit selectivity data (Data Gap DG002)
3. **For insomnia (Rank 3, L4):** This is mechanistically plausible (GABA-A α1 sedation pathway), but bromazepam has lower α1 selectivity than approved z-drugs; a direct comparative RCT vs. zolpidem or zopiclone is needed before clinical consideration
4. **For alcohol withdrawal delirium (Rank 7, L4):** Class-effect extrapolation from standard BZDs (diazepam, chlordiazepoxide) is scientifically plausible given identical mechanism; direct bromazepam AWS trial data required to establish dosing and safety equivalence
5. **For migraine:** Not recommended for further development; clinicians managing migraine patients should specifically assess for bromazepam overuse as a potential contributor to MOH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

