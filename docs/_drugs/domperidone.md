---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Domperidone
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

# Domperidone: From Nausea & Vomiting to Headache Disorder

## One-Sentence Summary

Domperidone is a peripherally selective dopamine D2 receptor antagonist, widely used as an antiemetic and prokinetic agent for nausea, vomiting, and gastric motility disorders.
The TxGNN model predicts it may be effective for **Headache Disorder** (particularly migraine), the highest-evidence prediction among the top 10 candidates,
with **0 clinical trials** and **20 publications** currently supporting this direction.

> **Note on prediction ranking**: TxGNN's top-ranked prediction by score is *nephrogenic syndrome of inappropriate antidiuresis* (NSIAD, score 99.08%), but this has no supporting clinical evidence and a mechanistic rationale that is directionally inconsistent with treatment goals (Hold). The **headache disorder** prediction (score 96.72%), while ranked 4th by model score, carries L3 evidence and a *Proceed with Guardrails* recommendation — making it the primary focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Nausea, vomiting, and gastric motility disorders (antiemetic/prokinetic) |
| Predicted New Indication | Headache Disorder (Migraine) |
| TxGNN Prediction Score | 96.72% |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Domperidone is a dopamine D2 receptor antagonist that acts primarily at the chemoreceptor trigger zone (CTZ) and the upper gastrointestinal tract. Unlike metoclopramide, it is peripherally selective with minimal CNS penetration, which limits extrapyramidal side effects while preserving both antiemetic and prokinetic activity.

Migraine attacks are frequently accompanied by nausea, vomiting, and gastric stasis — pathophysiological features that domperidone is mechanistically well-positioned to address. During a migraine attack, delayed gastric emptying significantly impairs oral absorption of analgesics and triptans. By restoring normal gastric motility, domperidone acts as a pharmacokinetic enhancer for co-administered acute migraine medications. This "adjunct role" is recognised in multiple major guidelines, including the Canadian Headache Society (2013) and European treatment recommendations, and is directly supported by an RCT comparing domperidone + paracetamol (Domperamol) to sumatriptan 50 mg in moderate-to-severe migraine.

Beyond its symptomatic role, emerging 2024 evidence (Karsan & Goadsby, *CNS Drugs*) proposes that dopaminergic activation during the premonitory phase is a key migraine trigger mechanism. Blocking D2 receptors in this pre-headache window may prevent the cascade from progressing to full attack — an early-intervention hypothesis that positions domperidone not merely as an adjunct, but potentially as a disease-modifying agent when administered in the prodrome. The mechanistic link is rated **moderate-to-strong**.

---

## Clinical Trial Evidence

Currently no related clinical trials registered on ClinicalTrials.gov or ICTRP for this drug-indication pair.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [11191009](https://pubmed.ncbi.nlm.nih.gov/11191009/) | 2000 | RCT | *Current Medical Research and Opinion* | Domperidone + paracetamol (Domperamol) vs sumatriptan 50 mg in moderate-to-severe migraine (n=120, UK primary care); comparable efficacy and tolerability |
| [27837002](https://pubmed.ncbi.nlm.nih.gov/27837002/) | 2016 | Prospective Safety Study | *Neurology* | Safety evaluation of domperidone for nausea management during dihydroergotamine (DHE) infusion in refractory headache; favourable safety profile reported |
| [33409110](https://pubmed.ncbi.nlm.nih.gov/33409110/) | 2020 | Prospective Observational | *Cureus* | Real-world headache management study from tertiary care; documents domperidone use in clinical migraine practice with disability assessment (MIDAS, VAS, HIT-6) |
| [23968886](https://pubmed.ncbi.nlm.nih.gov/23968886/) | 2013 | Clinical Guideline | *Canadian Journal of Neurological Sciences* | Canadian Headache Society acute migraine guideline; explicitly includes domperidone as a recommended antiemetic adjunct for episodic migraine |
| [38822165](https://pubmed.ncbi.nlm.nih.gov/38822165/) | 2024 | Review | *CNS Drugs* | Premonitory phase intervention in migraine; D2 antagonists (including domperidone) proposed as early-window treatment to prevent progression to headache onset |
| [9876882](https://pubmed.ncbi.nlm.nih.gov/9876882/) | 1998 | Review | *Cephalalgia* | Pathophysiology of emesis in migraine; benzamide D2 antagonists (domperidone, metoclopramide) identified as central to antiemetic and prokinetic strategy in migraine |
| [10494007](https://pubmed.ncbi.nlm.nih.gov/10494007/) | 1999 | Review | *Canadian Journal of Clinical Pharmacology* | Migraine-associated nausea; domperidone's prokinetic action shown to improve GI absorption of analgesics and triptans during attack |
| [8749241](https://pubmed.ncbi.nlm.nih.gov/8749241/) | 1995 | Review | *Cephalalgia* | Analgesics and NSAIDs in acute migraine; domperidone 20 mg orally recommended as antiemetic adjunct to enhance drug resorption |
| [25877672](https://pubmed.ncbi.nlm.nih.gov/25877672/) | 2015 | Review | *Headache* | Comprehensive review of acute migraine treatment in adults; prokinetic antiemetics including domperidone cited as validated adjunct strategy |
| [11200800](https://pubmed.ncbi.nlm.nih.gov/11200800/) | 2000 | Review | *Functional Neurology* | Physiopharmacology of emesis and GI motility in migraine; details the mechanism by which domperidone restores retrograde GI contractions and improves drug delivery |

---

## Singapore Market Information

Domperidone (DB01184) is **not currently registered** with the Health Sciences Authority (HSA) of Singapore. No marketing authorisations were found in the HSA licensing database.

Practitioners should refer to EMA (European Medicines Agency) or Health Canada safety communications for current approved indications, warnings, and contraindication guidance, as domperidone is approved in multiple other jurisdictions (EU, Canada, Japan, Taiwan, among others).

---

## Safety Considerations

Detailed TFDA/HSA package insert warnings and contraindications are not available in this Evidence Pack. Based on the published literature and known regulatory signals:

- **QT Prolongation Risk**: Domperidone is a known QT-prolonging agent. The EMA and Health Canada have issued safety communications limiting use to the lowest effective dose and shortest duration, particularly in patients aged >60 years or receiving doses >30 mg/day.
- **Cardiac Risk**: Observational studies have associated domperidone with increased risk of serious ventricular arrhythmia and sudden cardiac death, especially in combination with other QT-prolonging drugs (macrolide antibiotics, azole antifungals, HIV protease inhibitors).
- **Hyperprolactinaemia**: As a D2 antagonist, domperidone elevates prolactin levels; prolonged use may cause galactorrhoea, amenorrhoea, and gynaecomastia.

> Please refer to the EMA Public Assessment Report and package insert for complete safety information pending HSA regulatory review.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Domperidone has a well-characterised mechanistic basis and guideline-supported role in migraine management, backed by L3 evidence including one RCT (Domperamol vs sumatriptan) and multiple treatment guidelines; however, cardiac safety concerns (QT prolongation) and the absence of HSA registration in Singapore require a structured guardrail framework before any clinical deployment.

**To proceed, the following is needed:**

- **HSA registration pathway**: Assess feasibility of HSA new drug application or off-label use framework in Singapore for migraine indication
- **Cardiac safety review**: Mandatory QT-interval assessment protocol for any study design; exclude patients on concomitant QT-prolonging agents
- **Randomised controlled trial**: Current RCT evidence (Domperamol, 2000) is underpowered and dated; a modern confirmatory trial with triptan comparator is needed
- **MOA documentation**: Retrieve complete mechanism of action data from DrugBank (DG002) to support regulatory submission
- **TFDA/HSA package insert**: Obtain and parse approved package insert for full contraindication and warning list (DG001, currently blocking S1 safety screening)
- **Drug interaction profile**: Characterise DDI risk with co-prescribed migraine agents (triptans, ergotamines, NSAIDs) before any combination therapy study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

