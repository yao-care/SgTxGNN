---
layout: default
title: Betahistine
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Betahistine
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

# Betahistine: From Ménière's Disease to Peripheral Vertigo in Singapore

## One-Sentence Summary

Betahistine is a histamine analogue (H1 receptor weak agonist / H3 receptor potent antagonist) approved in over 40 countries — including the EU, UK, Japan, and Taiwan — for Ménière's disease and vestibular vertigo, but not currently registered in Singapore.
The TxGNN model identifies **Peripheral Vertigo** and related vestibular conditions as the most clinically actionable repurposing targets in the Singapore context, with prediction scores consistently above 97%.
The evidence base for peripheral vertigo includes **2 completed clinical trials directly involving betahistine** (including one Phase 2 RCT), **2 Cochrane systematic reviews**, and over **20 publications** — supporting an evidence level of **L2** and a **Proceed with Guardrails** recommendation.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ménière's disease / vestibular vertigo (approved in EU, UK, Japan, Taiwan; not registered in Singapore) |
| Predicted New Indication | Peripheral Vertigo |
| TxGNN Prediction Score | 98.07% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence pack. Based on the published literature, betahistine is a structural analogue of histamine with two complementary pharmacological actions: (1) a weak agonist effect at peripheral H1 receptors, promoting vasodilation of the microvasculature in the cochlear stria vascularis; and (2) a potent inverse agonist effect at presynaptic H3 autoreceptors in the vestibular nuclei and inner ear vasculature — increasing local histamine turnover and suppressing abnormal firing in the deafferented vestibular nucleus. Together, these actions improve cochlear microcirculation and accelerate central vestibular compensation after peripheral inner-ear injury.

Peripheral vertigo encompasses the most prevalent vestibular disorders — Ménière's disease (endolymphatic hydrops), vestibular neuritis (acute unilateral deafferentation), and benign paroxysmal positional vertigo (BPPV with residual compensatory dysregulation) — each of which involves disrupted cochlear microcirculation, vestibular nuclear imbalance, or impaired compensation. These are precisely the three points of betahistine's pharmacological action, explaining its decades of clinical use across Europe and Asia and its endorsement in the European Position Statement on Ménière's Disease diagnosis and treatment (PMID 30256205).

The TxGNN knowledge graph prediction captures the well-established biological relationship between betahistine's histaminergic targets and vestibular disease network nodes. Since betahistine is not registered in Singapore, its approved vestibular indications from comparable regulatory jurisdictions (EMA, PMDA) represent a genuine market access opportunity backed by substantial clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03908567](https://clinicaltrials.gov/study/NCT03908567) | Phase 2 | Completed | 124 | AM-125 (intranasal betahistine, Auris Medical) vs placebo for acute peripheral vertigo after vestibular schwannoma neurosurgery — highest-grade direct RCT evidence for betahistine in acute peripheral vertigo |
| [NCT01759251](https://clinicaltrials.gov/study/NCT01759251) | N/A (Post-marketing) | Completed | 309 | Betahistine dihydrochloride (Betaserc®) real-world observational study in vestibular vertigo outpatients; assessed effectiveness and symptom course after treatment discontinuation in Russia and Ukraine |
| [NCT07203248](https://clinicaltrials.gov/study/NCT07203248) | N/A | Not Yet Recruiting | 2,000 | CGRP-targeted therapy for vestibular migraine in Chinese patients — vestibular disease context; does not involve betahistine directly |
| [NCT06001047](https://clinicaltrials.gov/study/NCT06001047) | N/A | Recruiting | 120 | Head acupuncture for residual dizziness post-BPPV canalith repositioning — BPPV disease context; does not involve betahistine directly |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27327415](https://pubmed.ncbi.nlm.nih.gov/27327415/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Betahistine vs placebo for vertigo of multiple causes — reviewed efficacy via improved inner ear blood flow; currently the authoritative systematic review on betahistine for vertigo |
| [36827524](https://pubmed.ncbi.nlm.nih.gov/36827524/) | 2023 | Cochrane Systematic Review | Cochrane Database Syst Rev | Systemic pharmacological interventions for Ménière's disease — evaluated betahistine, diuretics, antivirals, and corticosteroids across controlled trials |
| [26797774](https://pubmed.ncbi.nlm.nih.gov/26797774/) | 2016 | Phase 3 RCT | BMJ | BEMED trial: long-term multicentre double-blind RCT comparing betahistine 16 mg t.i.d., 48 mg t.i.d., and placebo for vertigo attack frequency in Ménière's disease |
| [23778722](https://pubmed.ncbi.nlm.nih.gov/23778722/) | 2014 | Meta-analysis | Eur Arch Otorhinolaryngol | Meta-analysis of 12 double-blind, randomised, placebo-controlled studies with betahistine in vestibular vertigo and Ménière's disease; odds ratio favoured betahistine for overall treatment response |
| [40070497](https://pubmed.ncbi.nlm.nih.gov/40070497/) | 2025 | Systematic Review / Meta-analysis | World J Otorhinolaryngol Head Neck Surg | Betahistine as add-on to Epley manoeuvre for BPPV residual dizziness — systematic review and meta-analysis confirming adjunctive betahistine benefit |
| [30256205](https://pubmed.ncbi.nlm.nih.gov/30256205/) | 2018 | Clinical Guideline | J Int Adv Otol | European Position Statement on Ménière's Disease diagnosis and treatment — betahistine endorsed as the primary pharmacological treatment option |
| [26245698](https://pubmed.ncbi.nlm.nih.gov/26245698/) | 2015 | Clinical Review | Acta Otolaryngol | Clinical studies and meta-analyses demonstrate betahistine efficacy and safety for Ménière's disease, BPPV, vestibular neuronitis, and other peripheral vertigo types |
| [39525524](https://pubmed.ncbi.nlm.nih.gov/39525524/) | 2024 | Mechanistic Study | Laryngoscope Investig Otolaryngol | Betahistine modulates pro-inflammatory cytokine expression in autoimmune inner ear disease and Ménière's disease patients — novel immunomodulatory dimension of H1/H3 activity |
| [26998036](https://pubmed.ncbi.nlm.nih.gov/26998036/) | 2016 | Meta-analysis | Exp Ther Med | Meta-analysis of puerarin combined with betahistine for vertebrobasilar ischaemia vertigo across 6 RCTs — betahistine as active comparator and combination partner |
| [32530417](https://pubmed.ncbi.nlm.nih.gov/32530417/) | 2020 | Narrative Review | Dtsch Arztebl Int | Updated evidence on diagnosis, pathophysiology, genetics, and treatment of peripheral, central, and functional vestibular vertigo syndromes |

---

## Singapore Market Information

Betahistine is currently **not registered in Singapore**. No product authorisations are on record with the Health Sciences Authority (HSA).

For reference, the drug is commercially available internationally under brand names including **Serc®** and **Betaserc®** (BGP Pharma / Abbott) with the following approved indications in comparable jurisdictions:

| Jurisdiction | Approved Indication |
|---|---|
| European Union (EMA) | Ménière's syndrome: vertigo, tinnitus, and hearing loss |
| United Kingdom (MHRA) | Ménière's disease |
| Japan (PMDA) | Ménière's disease; vertigo associated with vertebrobasilar insufficiency |
| Taiwan (TFDA) | Ménière's disease and vestibular vertigo (multiple registered products) |

---

## All Predicted Indications — Multi-Indication Overview

This evidence pack covers 10 TxGNN predictions for betahistine. The three actionable indications (L2 evidence, Proceed with Guardrails) are all peripheral vestibular disorders, fully consistent with betahistine's global pharmacological profile.

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation |
|------|-----------|------------|---------------|----------------|
| 1 | Restless Legs Syndrome | 98.51% | L5 | Hold |
| 2 | Active Cochleovestibular Ménière Disease | 98.34% | L4 | Research Question |
| **3** | **Active Vestibular Ménière Disease** | **98.34%** | **L2** | **Proceed with Guardrails** |
| 4 | Active Cochlear Ménière Disease | 98.34% | L3 | Research Question |
| 5 | Otosclerosis | 98.19% | L4 | Hold |
| **6** | **Peripheral Vertigo** | **98.07%** | **L2** | **Proceed with Guardrails** |
| 7 | Age-Related Hearing Impairment | 97.93% | L5 | Hold |
| **8** | **Vertigo, Benign Recurrent / BPPV** | **97.78%** | **L2** | **Proceed with Guardrails** |
| 9 | Autosomal Recessive Hyperinsulinism (Kir6.2) | 97.77% | L5 | Hold |
| 10 | Hyperinsulinemic Hypoglycaemia, Familial | 97.32% | L5 | Hold |

**Actionable cluster (ranks 3, 6, 8):** All three are peripheral vestibular disorders directly addressable by betahistine's established mechanism. Peripheral Vertigo (rank 6) is the broadest indication and the recommended primary registration target, as it encompasses both Ménière's disease and BPPV subtypes.

**Research Question cluster (ranks 2, 4):** Cochleovestibular and cochlear Ménière subtypes share mechanistic overlap with the vestibular subtype but lack specific clinical trials; suitable for investigator-initiated studies or as secondary endpoints in a broader Ménière's registration dossier.

**Hold cluster (ranks 1, 5, 7, 9, 10):** No supporting clinical evidence exists for these indications. Restless Legs Syndrome and the metabolic indications (Kir6.2 hyperinsulinism, familial hyperinsulinemic hypoglycaemia) are speculative knowledge-graph topology predictions without pharmacological rationale in betahistine's mechanism. Otosclerosis involves bone remodelling pathology unrelated to histaminergic action; betahistine may offer indirect symptom relief for associated vestibular symptoms but has no effect on the core disease.

---

## Safety Considerations

Please refer to the package insert for safety information. No drug-drug interaction data was available from the DDI query. No specific warnings or contraindications were returned from the Singapore regulatory database (drug not registered).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Betahistine has one of the strongest evidence bases in vestibular pharmacotherapy — supported by two Cochrane systematic reviews, a landmark Phase 3 RCT (BEMED trial), a 12-trial meta-analysis, and an international clinical guideline (European Position Statement) — all specifically for peripheral vestibular indications. Singapore's non-registration represents a market access gap, not an evidence gap; comparable regulatory jurisdictions have approved betahistine for these exact indications for decades.

**To proceed, the following is needed:**

- **HSA regulatory pathway assessment:** Determine whether abridged registration (referencing the EMA-approved Serc® SmPC) or a full new drug application is required; confirm no previous withdrawn registration exists
- **Complete safety dossier:** Obtain the full Summary of Product Characteristics (SmPC) for betahistine to document warnings, contraindications (e.g., phaeochromocytoma), and known drug interactions for Singapore prescribers
- **MOA data gap closure:** Complete DrugBank API query for DB06698 to formally document the H1 agonist / H3 antagonist mechanism in the submission dossier
- **Manufacturing / MAH partner identification:** Identify a registered manufacturer or marketing authorisation holder willing to file in Singapore (Serc® or equivalent)
- **Pharmacoeconomic analysis:** Assess cost-effectiveness vs currently available vertigo agents in Singapore (prochlorperazine, dimenhydrinate, cinnarizine/dimenhydrinate combination)
- **Post-registration pharmacovigilance plan:** Design a real-world data collection protocol for Singapore patients, with particular focus on Ménière's disease and BPPV subpopulations to generate local outcomes data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

