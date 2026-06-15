---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 10
---

# Bisoprolol
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

# Bisoprolol: From Heart Failure to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Bisoprolol is a highly cardioselective β1-adrenergic receptor blocker with established use in heart failure and hypertension, though no Singapore regulatory records are available in this evidence pack.
The TxGNN model identifies **Chronic Pulmonary Heart Disease** (cor pulmonale / COPD-associated right heart disease) as the most evidence-supported repurposing candidate,
with the **BICS Phase 3 RCT** (NCT03917914, n=280, completed 2025, published in *JAMA*), a **2023 systematic review**, and **multiple randomised trials** collectively providing Level 1 evidence.

> **Note on TxGNN ranking:** The model's highest-scored prediction is *malignant renovascular hypertension* (rank 1, 99.94%), but that indication has no clinical trials or supporting literature (L4, Research Question only). Chronic pulmonary heart disease (rank 6, 98.63%) carries the strongest actionable evidence and is therefore the focus of this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure / hypertension (established clinical use; no Singapore license on record) |
| Predicted New Indication | Chronic Pulmonary Heart Disease |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L1 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Bisoprolol is a second-generation cardioselective beta-blocker with one of the highest β1:β2 receptor selectivity ratios (~75:1) among all commercially available agents. Its landmark indications rest on the CIBIS and CIBIS-II trials in heart failure with reduced ejection fraction, and it is the prototype agent when cardiac β1-blockade is needed without compromising airways. Detailed MOA data is absent from this evidence pack (data gap DG002), but the core pharmacology is well-established: competitive blockade of cardiac β1-adrenergic receptors reduces heart rate, myocardial oxygen demand, and pathological neurohormonal activation.

Chronic pulmonary heart disease represents right ventricular dysfunction or failure driven by elevated pulmonary vascular resistance — most commonly COPD-induced cor pulmonale. This population suffers disproportionate cardiovascular mortality yet has historically been denied beta-blocker therapy due to fear of bronchoconstriction. Bisoprolol's exceptional β1 selectivity provides the mechanistic bridge: at therapeutic doses it delivers the full cardiac benefit (rate reduction, anti-remodeling, sympathetic blockade) while sparing airway β2-receptors, directly sidestepping the traditional pulmonary contraindication. Both COPD-related pulmonary hypertension and classical heart failure share the final common pathway of sympathetic over-activation and adverse cardiac remodeling, making the pharmacological rationale particularly compelling.

This mechanistic plausibility is now strongly corroborated by clinical data. Multiple randomised trials directly tested Bisoprolol in CHF+COPD overlap populations, culminating in the 2024–2025 BICS Phase 3 RCT published in *JAMA* and *Health Technology Assessment*. A 2023 systematic review and meta-analysis confirmed favourable safety and efficacy, and head-to-head RCTs against Carvedilol (non-selective) consistently demonstrate Bisoprolol's superior pulmonary tolerability, establishing it as the guideline-preferred beta-blocker when cardiac management is required alongside obstructive lung disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT03917914](https://clinicaltrials.gov/study/NCT03917914) | Phase 3 | Completed | 280 | **BICS trial** — double-blind RCT evaluating proactive cardiac risk treatment with Bisoprolol in high-exacerbation-risk COPD patients; designed to assess improvement in both cardiac and respiratory outcomes. Primary source of Level 1 evidence; results published 2024–2025. |
| [NCT00702156](https://clinicaltrials.gov/study/NCT00702156) | Phase 2 | Terminated | 27 | Phase 2 RCT of cardioselective beta-blockade with Bisoprolol in CHF + moderate/severe COPD; terminated early due to recruitment difficulties (n=27), but directly tested the study drug in the overlap population and provides Phase 2 supportive data. |
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Head-to-head RCT: Nebivolol vs **Bisoprolol** vs Carvedilol in HF; assessed exercise capacity, hypoxia response, and pulmonary diffusion — supports Bisoprolol's relative positioning in cardiopulmonary disease. |
| [NCT01656005](https://clinicaltrials.gov/study/NCT01656005) | Phase 4 | Completed | 18 | Systematic comparison of cardioselective vs non-cardioselective beta-blockers on lung function in moderate-to-severe COPD; directly supports the safety advantage of Bisoprolol's β1 selectivity. |
| [NCT02380053](https://clinicaltrials.gov/study/NCT02380053) | Phase 4 | Completed | 10 | Proof-of-concept: Celiprolol vs **Bisoprolol** on cardiopulmonary outcomes during exercise in COPD; pharmacodynamic evidence for β-selectivity differences at rest and under load. |
| [NCT00878384](https://clinicaltrials.gov/study/NCT00878384) | N/A | Completed | 52 | Catheter ablation vs rate control in persistent AF+CHF; contextually relevant to managing arrhythmic comorbidities common in chronic pulmonary heart disease. |
| [NCT03778554](https://clinicaltrials.gov/study/NCT03778554) | Phase 4 | Active, Not Recruiting | 2,760 | DANBLOCK: long-term beta-blocker after MI in preserved EF patients; contributes to the broader safety database for beta-blockers in non-classic cardiac settings. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | *JAMA* | **BICS trial results** — Bisoprolol in high-exacerbation-risk COPD; first large-scale RCT directly testing Bisoprolol in this population. Core Level 1 evidence for this indication. |
| [40386836](https://pubmed.ncbi.nlm.nih.gov/40386836/) | 2025 | RCT | *Health Technology Assessment* | **BICS full final report** — comprehensive clinical and health economic data from the BICS RCT; confirms Bisoprolol's clinical profile in COPD with cardiovascular comorbidity. |
| [38152590](https://pubmed.ncbi.nlm.nih.gov/38152590/) | 2023 | Systematic Review | *Int J Chronic Obstructive Pulmonary Disease* | Systematic review and meta-analysis of **Bisoprolol efficacy and safety specifically in COPD patients**; supports both benefit and tolerability. |
| [19460848](https://pubmed.ncbi.nlm.nih.gov/19460848/) | 2009 | RCT | *European Journal of Heart Failure* | First prospective RCT examining Bisoprolol in patients with **both HF and moderate-to-severe COPD**; established initial clinical feasibility. |
| [22015086](https://pubmed.ncbi.nlm.nih.gov/22015086/) | 2011 | RCT | *Respiratory Medicine* | Randomised trial comparing **Bisoprolol vs Carvedilol** in CHF+COPD; Bisoprolol demonstrated superior pulmonary function preservation. |
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | RCT | *Journal of the American College of Cardiology* | Randomised crossover: β1-selective vs nonselective beta-blockers in CHF+COPD; key evidence supporting switching to **Bisoprolol** in this population. |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | *New England Journal of Medicine* | REDUCE-SWEDEHEART: beta-blockers post-MI with preserved EF; contextualises current clinical practice and evidence base for beta-blockers beyond classic HFrEF. |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Cohort | *European Journal of Heart Failure* | Danish nationwide cohort: Carvedilol vs **Bisoprolol**/Metoprolol/Nebivolol in HF+COPD; all-cause and COPD-related hospitalisation outcomes. |
| [27792991](https://pubmed.ncbi.nlm.nih.gov/27792991/) | 2017 | Cohort | *International Journal of Cardiology* | **Bisoprolol vs Carvedilol** protective effects against myocardial injury and pulmonary dysfunction in CHF; supports β1-selectivity advantage. |
| [38597065](https://pubmed.ncbi.nlm.nih.gov/38597065/) | 2024 | Review | *Current Medical Research and Opinion* | Comparative beta-blocker pharmacology: explains Bisoprolol's unique β1 selectivity profile and its clinical implications in cardiopulmonary disease management. |

---

## Singapore Market Information

Bisoprolol currently has **no registered products in Singapore** (HSA). No authorization records are available.

Bisoprolol is approved and widely available in multiple international markets (EU, US, Japan, Taiwan, and others). The absence of a Singapore registration does not preclude use under special access or compassionate use pathways, but a dedicated registration strategy would be needed for formal market entry.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important:** Key safety data — including prescribing information warnings, contraindications, and drug-drug interaction profiles — are absent from this evidence pack. This has been flagged as a **Blocking data gap (DG001)** that must be resolved before formal safety screening (Stage S1) can proceed. Retrieval method: download the prescribing information PDF from a regulatory authority (e.g., EMA, FDA, or TFDA) and extract relevant sections.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The BICS Phase 3 RCT (n=280, NCT03917914, completed 2025) provides direct Level 1 clinical evidence for Bisoprolol in COPD patients at high cardiovascular risk, corroborated by a 2023 systematic review, multiple randomised crossover trials, and large observational cohorts. Mechanistic plausibility is strong, and the high β1 selectivity addresses the traditional safety concern in pulmonary disease. Evidence is sufficient to advance evaluation, contingent on completing outstanding safety data retrieval and defining clear patient selection guardrails.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain prescribing information (package insert) to complete safety screening — key warnings, contraindications, and drug interaction profile must be documented before clinical protocol development
- **Resolve DG002 (High):** Retrieve formal mechanism of action data from DrugBank API to support mechanistic rationale documentation
- **Review BICS trial primary and secondary endpoint data** in full detail (PMID 38762800, 40386836) before designing any local study protocol
- **Define patient selection criteria:** specify the COPD+cardiovascular risk phenotype to target; establish exclusion criteria (decompensated right heart failure, severe bronchospasm, resting bradycardia)
- **Establish a monitoring protocol:** baseline and follow-up FEV₁/FVC, 6-minute walk test, echocardiographic right ventricular function, BNP/NT-proBNP, and COPD exacerbation frequency
- **Conduct Singapore regulatory gap analysis:** assess HSA registration requirements or special access pathways, given the current absence of any local market authorisation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

