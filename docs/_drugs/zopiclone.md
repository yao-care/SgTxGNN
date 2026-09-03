---
layout: default
title: Zopiclone
parent: 僅模型預測 (L5)
nav_order: 1080
evidence_level: L5
indication_count: 10
---

# Zopiclone
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

# Zopiclone: From Insomnia to Sleep Disorder, Initiating and Maintaining Sleep

## One-Sentence Summary

> Zopiclone is a widely used Z-drug hypnotic, and although its original indication is not formally documented in this evidence pack, it is well established as a short-term treatment for insomnia.
> The TxGNN model predicts it may be effective for **Sleep Disorder, Initiating and Maintaining Sleep** — which is essentially the same clinical entity as insomnia — with **1 clinical trial** (not yet recruiting) and **20 publications** currently supporting this direction.
> Because the "new" indication largely overlaps with the drug's known real-world use, this should be read as a confirmation of existing pharmacology rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not formally recorded in this evidence pack (no Singapore license text available); commonly known real-world use is short-term insomnia treatment |
| Predicted New Indication | Sleep Disorder, Initiating and Maintaining Sleep |
| TxGNN Prediction Score | 98.83% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (marked as a data gap). Based on known pharmacological class information reflected in the rationale for related candidates, Zopiclone belongs to the "Z-drug" (cyclopyrrolone) class of non-benzodiazepine hypnotics, acting as a GABA-A receptor positive allosteric modulator to promote sedation and sleep onset.

The predicted new indication — "sleep disorder, initiating and maintaining sleep" — is clinically synonymous with insomnia, which is Zopiclone's established therapeutic use. This means the TxGNN knowledge graph has essentially re-identified the drug's known indication rather than surfacing a novel repurposing opportunity. The mechanistic plausibility is therefore very high, but the value of this prediction lies in validating model behavior rather than uncovering new clinical use.

Supporting literature consistently places Z-drugs (including zopiclone) within major systematic reviews, network meta-analyses, and clinical practice guidelines for insomnia pharmacotherapy, reinforcing that the association is well-grounded in existing evidence — even though it does not represent a true "repurposing" case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06928766](https://clinicaltrials.gov/study/NCT06928766) | Phase 2 | Not Yet Recruiting | 15 | Evaluates eszopiclone and lemborexant (not zopiclone itself) in patients with obstructive sleep apnoea and comorbid insomnia (COMISA) who have a low arousal threshold; relevant as class-level evidence for Z-drugs in difficulty maintaining/initiating sleep |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30303519](https://pubmed.ncbi.nlm.nih.gov/30303519/) | 2018 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | Reviews efficacy/safety of eszopiclone (Z-drug class relative of zopiclone) for insomnia |
| [35843245](https://pubmed.ncbi.nlm.nih.gov/35843245/) | 2022 | Systematic Review / NMA | Lancet | Compares pharmacological interventions, including Z-drugs, for acute and long-term insomnia management |
| [36947394](https://pubmed.ncbi.nlm.nih.gov/36947394/) | 2023 | Systematic Review / NMA (153 RCTs) | Drugs | Ranks insomnia drug classes by effectiveness, safety, and tolerability |
| [36701954](https://pubmed.ncbi.nlm.nih.gov/36701954/) | 2023 | Systematic Review / NMA | Sleep Medicine Reviews | Evaluates efficacy and tolerability of 20 insomnia drugs across placebo-controlled and head-to-head trials |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | Clinical Practice Guideline | J Clin Sleep Med (AASM) | AASM guideline on pharmacologic treatment of chronic insomnia, covering individual drugs including Z-drugs |
| [39923608](https://pubmed.ncbi.nlm.nih.gov/39923608/) | 2025 | Expert Consensus / Guideline | Sleep Medicine | European consensus on switching/deprescribing hypnotics; explicitly lists zopiclone among GABAergic Z-drugs |
| [38551874](https://pubmed.ncbi.nlm.nih.gov/38551874/) | 2024 | Review | La Revue du praticien | Discusses zopiclone directly as a first-line pharmacotherapy for sleep initiation in chronic insomnia |
| [29487083](https://pubmed.ncbi.nlm.nih.gov/29487083/) | 2018 | Review | Pharmacological Reviews | Reviews Z-drugs (including zopiclone) alongside newer non-GABAergic insomnia treatments |
| [34121443](https://pubmed.ncbi.nlm.nih.gov/34121443/) | 2021 | Systematic Review / NMA | J Manag Care Spec Pharm | Network meta-analysis comparing lemborexant with other insomnia treatments, including Z-drugs |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs & Aging | Recommendations for pharmacological management of insomnia in elderly patients |

---

## Singapore Market Information

Zopiclone is currently not marketed in Singapore, and no registration records are available in the evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The predicted indication overlaps substantially with Zopiclone's known real-world use as an insomnia treatment, so this is not a genuine novel repurposing signal; more importantly, a **blocking data gap** exists on local (TFDA/HSA-equivalent) label warnings and contraindications, which prevents completion of the initial safety assessment (S1), and the drug is not currently marketed in Singapore.

**To proceed, the following is needed:**
- TFDA/HSA package insert warnings and contraindications (DG001, blocking)
- Confirmed mechanism of action data from DrugBank (DG002)
- Clarification of whether this candidate should be reclassified as "existing indication confirmation" rather than a repurposing candidate
- If repurposing value is still sought, prioritize the lower-ranked candidates with genuinely novel mechanistic hypotheses (e.g., restless legs syndrome, rank 8) over this one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

