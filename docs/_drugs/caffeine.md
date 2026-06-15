---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# Caffeine: From Analgesic Adjuvant to Hypnic Headache

## One-Sentence Summary

Caffeine is the world's most widely consumed psychoactive compound, established pharmaceutically as a CNS stimulant, analgesic adjuvant, and neonatal respiratory stimulant for apnea of prematurity.
The TxGNN model identified **10 candidate repurposing indications** spanning neurological, vascular, and ENT domains; the most actionable finding is **Hypnic Headache** (rank 9 by TxGNN score), where caffeine is already cited as the **preferred first-line therapy** in headache specialist guidelines, supported by **L3 evidence** from 19 publications including multiple independent case series reviews.
The highest-ranked TxGNN prediction — Nasal Cavity Disease (score 99.91%) — carries only L5 evidence and a Hold recommendation due to absence of clinical trial data and lack of direct therapeutic rationale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Analgesic adjuvant; CNS stimulant; neonatal apnea of prematurity (no standalone HSA registration) |
| Primary Actionable Prediction | Hypnic Headache (rank 9 by TxGNN score; highest evidence level in pack) |
| Top TxGNN Score Prediction | Nasal Cavity Disease (rank 1; score 99.91%; L5) |
| TxGNN Prediction Score (Hypnic Headache) | 99.17% |
| Evidence Level | **L3** (Hypnic Headache) |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Proceed with Guardrails** |

---

## All Predicted Indications at a Glance

| Rank | Indication | TxGNN Score | Evidence | Decision | Notes |
|------|------------|-------------|----------|----------|-------|
| 1 | Nasal Cavity Disease | 99.91% | L5 | Hold | Nasal route = delivery path, not therapeutic target |
| 2 | Thrombotic Disease | 99.90% | L4 | Research Question | PCSK9 inhibition + anti-platelet mechanism; conflicting epidemiology |
| 3 | Acute Laryngopharyngitis | 99.89% | L5 | Hold | No supporting literature; infection/allergy aetiology |
| 4 | Papillary Conjunctivitis | 99.79% | L5 | Hold | No supporting literature; mechanical/immune aetiology |
| 5 | Neuralgia | 99.34% | L4 | Research Question | Animal models support trigeminal pain adjuvant role; human data absent |
| 6 | Glossodynia | 99.26% | L5 | Hold | No literature; caffeine may exacerbate burning mouth syndrome |
| 7 | Coccygodynia | 99.22% | L5 | Hold | Structural/post-traumatic pain; caffeine lacks targeted mechanism |
| 8 | Trigeminal Autonomic Cephalalgia | 99.21% | L4 | Research Question | A2A antagonism may modulate hypothalamic-trigeminal pathway |
| **9** | **Hypnic Headache ★** | **99.17%** | **L3** | **Proceed with Guardrails** | **First-line therapy in expert guidelines; strong mechanistic basis** |
| 10 | Vein Disease | 99.06% | L4 | Research Question | Indirect vascular effects via adenosine/renin-angiotensin axis; broad label |

★ Primary report focus — highest evidence level across all 10 predictions.

---

## Why is This Prediction Reasonable?

Caffeine is a competitive, non-selective antagonist of adenosine receptors (A1, A2A, A2B subtypes). Adenosine accumulates during wakefulness and drives sleep pressure; blockade of adenosine signalling maintains CNS arousal, increases dopaminergic and noradrenergic neurotransmission, and produces cerebrovascular vasoconstriction. At higher concentrations, caffeine additionally inhibits cyclic nucleotide phosphodiesterases (PDE), amplifying cAMP-mediated intracellular signalling. These mechanisms make caffeine one of the most pharmacologically active dietary compounds in neurological contexts.

Hypnic headache is a rare primary headache disorder — occurring exclusively during sleep, predominantly in patients over 50 — that awakens patients 1–3 times per night at consistent times, with attacks lasting 15–180 minutes. The dorsomedial hypothalamus is proposed as the primary generator, and both REM and NREM sleep phases have been confirmed as attack triggers by polysomnographic recording. Caffeine's pharmacological profile directly addresses this pathophysiology through three converging mechanisms: (1) **A2A receptor blockade** disrupts the sleep-phase adenosine accumulation that likely initiates nocturnal attacks; (2) **vasoconstriction** counteracts the cerebrovascular dilation characteristic of hypnic headache episodes; (3) **CNS excitatory arousal** raises the threshold for sleep-onset attack initiation, preventing recurrence without requiring pharmacological sedation reversal.

This mechanistic alignment is corroborated by consistent, independently replicated clinical observations across case series totalling hundreds of patients and is reflected in formal treatment guideline language. Bedtime caffeine (40–60 mg — approximately one cup of strong coffee) is explicitly endorsed as the **preferred first-line treatment** in specialist headache literature, on par with melatonin and indomethacin, with a favourable tolerability profile in the predominantly elderly patient population affected. The biological rationale is strong and coherent; the primary gap is the absence of a randomised controlled trial, which reflects the ultra-rare disease prevalence rather than any safety or efficacy signal of concern.

---

## Clinical Trial Evidence

Currently no clinical trials specifically testing caffeine for Hypnic Headache are registered on ClinicalTrials.gov or ICTRP.

> This is expected for ultra-rare primary headache disorders: the population prevalence is insufficient to power conventional parallel-group RCTs at standard sites. Evidence development in this area has proceeded exclusively through case series aggregation and expert review — a pattern consistent across all accepted treatments for this condition (melatonin, indomethacin, lithium).

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [22072057](https://pubmed.ncbi.nlm.nih.gov/22072057/) | 2012 | Treatment Review | Curr Treat Options Neurol | **Caffeine explicitly identified as the preferable first-line therapy** for both acute treatment (cup of coffee at headache awakening) and prophylaxis of hypnic headache; discusses dose and timing guidance |
| [31075680](https://pubmed.ncbi.nlm.nih.gov/31075680/) | 2019 | Case series review (n=348) | J Neurol Sci | Largest systematic case review spanning 1988–2018 (348 published cases); caffeine consistently among the most frequently reported effective treatments |
| [25231430](https://pubmed.ncbi.nlm.nih.gov/25231430/) | 2014 | Case series / Review | Headache | Clinical features, therapeutic options, and outcomes in hypnic headache; caffeine described as a cornerstone management strategy |
| [24942086](https://pubmed.ncbi.nlm.nih.gov/24942086/) | 2014 | Narrative Review | Cephalalgia | Reviews ICHD-3β diagnostic criteria and treatment evidence; caffeine featured as standard therapeutic approach alongside melatonin |
| [23832130](https://pubmed.ncbi.nlm.nih.gov/23832130/) | 2013 | Review | Cephalalgia | Pathophysiology and treatment of hypnic headache; caffeine's arousal-promoting mechanism discussed in relation to REM sleep-linked attacks |
| [12654950](https://pubmed.ncbi.nlm.nih.gov/12654950/) | 2003 | Case series review (n=71) | Neurology | Foundational 71-case analysis establishing caffeine as an effective, well-tolerated treatment option in the predominantly elderly patient population |
| [23728805](https://pubmed.ncbi.nlm.nih.gov/23728805/) | 2013 | Annual Review | Curr Pain Headache Rep | Reviews 2012 publications on hypnic headache including documented pharmacological and non-pharmacological treatment successes |
| [15111685](https://pubmed.ncbi.nlm.nih.gov/15111685/) | 2004 | PSG Clinical Study | Neurology | Polysomnographic evidence that attacks arise directly from both REM and NREM sleep — supports caffeine's sleep-phase adenosine antagonism as the mechanism of attack prevention |
| [33974014](https://pubmed.ncbi.nlm.nih.gov/33974014/) | 2021 | Review | JAMA | Comprehensive headache management review in JAMA establishing caffeine's established role across rare primary headache syndromes |
| [35574653](https://pubmed.ncbi.nlm.nih.gov/35574653/) | 2023 | Review | Crit Rev Food Sci Nutr | Comprehensive caffeine health effects review; covers neurological effects including sleep architecture modulation, headache, and arousal thresholds |

---

## Singapore Market Information

Caffeine is not currently registered as a standalone pharmaceutical product in Singapore. No HSA product authorisations were identified in this evidence pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | — | — | No registrations on record |

**Note:** Caffeine is ubiquitously present as an active ingredient in combination analgesic OTC products and as a dietary component in beverages globally, but does not appear as a registered standalone pharmaceutical in this dataset. For the hypnic headache indication, the clinically relevant administration route (40–60 mg caffeine at bedtime via dietary intake or OTC analgesic) may not require formal drug registration — however, this requires confirmation with HSA if any therapeutic claim is to be made.

---

## Safety Considerations

Formal safety data — including key warnings, contraindications, and drug-drug interactions — were not available in this evidence pack. Please refer to the package insert for comprehensive safety information.

Clinical considerations specific to the **hypnic headache** target population:

- **Cardiovascular monitoring**: Hypnic headache predominantly affects patients over 50; caffeine-induced heart rate increase and transient blood pressure elevation warrant cardiovascular baseline screening in this demographic
- **Caffeine withdrawal**: Regular bedtime caffeine use may lead to rebound/withdrawal headache on cessation — patient counselling on gradual dose tapering is recommended
- **Sleep architecture impact**: While bedtime caffeine at low doses (40–60 mg) disrupts pathological sleep-triggered headaches, dose minimisation is advised to avoid chronic sleep quality degradation
- **Drug interactions**: Caffeine is a CYP1A2 substrate; co-administration with CYP1A2 inhibitors (e.g., fluvoxamine, ciprofloxacin) may increase caffeine exposure — formal DDI review needed

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Caffeine for hypnic headache represents an unusual case where the repurposing target already has recognised clinical use supported by consistent case series observations and explicit first-line treatment endorsement in specialist headache guidelines — the TxGNN model correctly identified a pharmacologically sound and clinically validated signal. The primary gap is not efficacy uncertainty but the absence of a formal RCT, which is structurally difficult given disease rarity.

**To proceed, the following is needed:**

- **RCT design**: Initiate a small prospective crossover trial (n=30–50) comparing bedtime caffeine (40–60 mg) vs. melatonin vs. placebo in ICHD-confirmed hypnic headache patients — this would establish Level 1 or Level 2 evidence and enable formal indication labelling
- **HSA regulatory pathway**: Consult HSA to clarify whether a new drug application is required or whether physician prescribing guidance / existing combination product label amendments are sufficient for this indication
- **MOA documentation**: Retrieve formal DrugBank adenosine receptor antagonist data (currently marked as a data gap in this pack) to support any regulatory mechanistic submissions
- **Full safety review**: Obtain TFDA/HSA package insert warnings and conduct a formal DDI risk assessment; priority concerns are CYP1A2 interactions and cardiovascular risk in the elderly target population
- **Secondary indication follow-up**: Thrombotic disease, neuralgia, and trigeminal autonomic cephalalgia (all L4, Research Question) warrant targeted mechanistic literature reviews before any clinical feasibility assessment is initiated
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

