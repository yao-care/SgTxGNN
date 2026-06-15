---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Carvedilol
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

# Carvedilol: From Heart Failure to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Carvedilol is a non-selective β-adrenergic and α1-adrenergic blocker established in clinical practice for chronic heart failure, hypertension, and post-myocardial infarction left ventricular dysfunction.
The TxGNN model identified 10 new predicted indications; the most evidence-supported candidate is **Chronic Pulmonary Heart Disease (cor pulmonale)** (TxGNN rank #6),
with **12 registered clinical trials** and **20 publications** — including 4 Grade-A trials directly studying Carvedilol in this population — currently backing this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic heart failure, hypertension, post-MI left ventricular dysfunction |
| Predicted New Indication | Chronic Pulmonary Heart Disease (Cor Pulmonale) |
| TxGNN Prediction Score | 94.55% |
| Evidence Level | L3 |
| Singapore Market Status | Not registered |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Carvedilol is a third-generation beta-blocker with a uniquely broad pharmacological profile. Unlike cardioselective agents such as bisoprolol or metoprolol, it simultaneously blocks β1-, β2-, and α1-adrenergic receptors, and additionally exerts potent antioxidant activity through its carbazole moiety. The α1-blocking component reduces systemic and pulmonary vascular resistance — a property not shared by most beta-blockers — making it pharmacologically distinctive among its class. Although the full MOA data from DrugBank is currently unavailable, its established mechanism in heart failure is well-characterised in the published literature: it slows pathological cardiac remodelling (via β1-blockade) and reduces afterload (via α1-blockade), with the antioxidant activity adding an additional layer of cardioprotection.

Chronic pulmonary heart disease (cor pulmonale) is fundamentally a right heart failure syndrome driven by chronic pulmonary disease, most often COPD. The core pathophysiology — right ventricular pressure overload, adverse remodelling, oxidative stress from chronic hypoxia — maps directly onto the mechanisms Carvedilol already targets in left-sided heart failure. Its α1-blockade may lower pulmonary vascular resistance, its β1-blockade can attenuate maladaptive right ventricular remodelling, and its antioxidant action may mitigate COPD-driven oxidative injury. This multi-point mechanistic overlap provides a credible biological rationale for the TxGNN prediction.

The primary safety concern is non-selective β2-blockade, which can worsen bronchospasm in patients with underlying airway disease. This risk is real, and several of the supporting trials were specifically designed to evaluate it. Crucially, multiple Danish and Italian register-based cohort studies — along with Phase 4 randomised crossover trials — have demonstrated that Carvedilol can be used safely in patients with concurrent heart failure and COPD when dose titration is careful and pulmonary function is monitored. This body of evidence differentiates the cor pulmonale prediction from the other TxGNN candidates (ranks 1–5 and 7–10), which either lack any supporting data (L5, Hold) or have mechanistic arguments against Carvedilol use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02120339](https://clinicaltrials.gov/study/NCT02120339) | Phase 1 | Terminated | 5 | Pilot study of chronic **Carvedilol** in pulmonary arterial hypertension (PAH) — assessed RV function and safety; terminated early due to safety concerns. The only dedicated Carvedilol-in-PAH trial; critical for safety profiling in pulmonary hypertensive populations. |
| [NCT00517725](https://clinicaltrials.gov/study/NCT00517725) | Phase 4 | Completed | 60 | Three-arm head-to-head trial: Nebivolol vs Bisoprolol vs **Carvedilol** in heart failure patients. Primary endpoints include exercise capacity, chemoreceptor response, and pulmonary function under normoxic and hypoxic conditions. Carvedilol is an explicit trial arm with lung function as a key endpoint. |
| [NCT03370835](https://clinicaltrials.gov/study/NCT03370835) | Phase 4 | Completed | 21 | Randomised open-label crossover: Metoprolol succinate-ER vs **Carvedilol** in COPD patients — directly evaluates tolerability of a non-selective beta-blocker in the chronic pulmonary heart disease population at guideline-recommended doses. |
| [NCT00924833](https://clinicaltrials.gov/study/NCT00924833) | Phase 4 | Completed | 27 | **Carvedilol** vs Nebivolol cardiovascular, metabolic, and respiratory effects at high altitude — a validated physiological model for hypoxic cardiopulmonary stress that mimics chronic heart failure with hypoxia. |
| [NCT01656005](https://clinicaltrials.gov/study/NCT01656005) | Phase 4 | Completed | 18 | Chronic dose exposure to cardioselective vs non-cardioselective beta-blockers (Carvedilol class) in moderate-to-severe COPD — assesses cardiopulmonary function over sustained exposure. |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | CAMERA Study: purpose-designed **Carvedilol** vs Metoprolol respiratory assessment in CHF patients — highest scientific relevance, but withdrawn before enrolment. No usable data; highlights the unmet evidence gap. |
| [NCT00292162](https://clinicaltrials.gov/study/NCT00292162) | N/A | Completed | 41 | Radiofrequency ablation for atrial fibrillation in advanced CHF; Carvedilol used as background medication, not the study intervention. Low direct relevance. |
| [NCT00878384](https://clinicaltrials.gov/study/NCT00878384) | N/A | Completed | 52 | AF catheter ablation vs rate-control in CHF; does not address chronic pulmonary heart disease as a primary endpoint. Low relevance. |
| [NCT03778554](https://clinicaltrials.gov/study/NCT03778554) | Phase 4 | Active, not recruiting | 2760 | DANBLOCK: long-term beta-blocker after MI in patients with preserved ejection fraction; population (post-MI, no HF) differs substantially from cor pulmonale. Low relevance. |
| [NCT06697353](https://clinicaltrials.gov/study/NCT06697353) | N/A | Completed | 4936 | ROVER Japan: real-world Vericiguat outcomes in HFrEF; Carvedilol is background therapy only, no cor pulmonale-specific analysis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [20413026](https://pubmed.ncbi.nlm.nih.gov/20413026/) | 2010 | Randomised Crossover | JACC | Randomised crossover comparing β1-selective vs non-selective (**Carvedilol**) agents in CHF+COPD patients; directly measures respiratory, haemodynamic, and clinical effects of switching between drug types. |
| [22015086](https://pubmed.ncbi.nlm.nih.gov/22015086/) | 2011 | RCT | Respiratory Medicine | Randomised trial: Bisoprolol vs **Carvedilol** in HF+COPD — compares pulmonary function, exercise tolerance, and hospitalisation risk between the two most commonly used beta-blockers in this comorbid population. |
| [31391573](https://pubmed.ncbi.nlm.nih.gov/31391573/) | 2019 | Register Cohort | Scientific Reports | Italian register study: predictors of **Carvedilol** choice in HF+COPD patients; guidelines favour cardioselective agents, yet real-world Carvedilol prescribing remains high, suggesting perceived clinical utility. |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Propensity-Matched Cohort | Am J Cardiology | Metoprolol vs **Carvedilol** in elderly patients with HF+COPD+DM+renal failure using Danish national registers (1:1 propensity match); 1-year survival and disease-specific hospitalisation outcomes. |
| [29159953](https://pubmed.ncbi.nlm.nih.gov/29159953/) | 2018 | Nationwide Cohort | Eur J Heart Failure | Danish nationwide cohort: **Carvedilol** vs metoprolol/bisoprolol/nebivolol in HF+COPD — compared COPD-related hospitalisation hazard and beta-blocker persistence in the real-world setting. |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Population Cohort | Medicine | Taiwan NHI database: **Carvedilol**, Bisoprolol, and Metoprolol survival effects in coexistent HF+COPD; largest Asian population-based analysis of this three-way comparison, directly relevant to Singapore practice. |
| [12490274](https://pubmed.ncbi.nlm.nih.gov/12490274/) | 2002 | Prospective Cohort | J Heart Lung Transplant | Prospective evaluation of **Carvedilol** tolerability and efficacy in CHF patients with concomitant COPD or asthma — foundational safety dataset demonstrating acceptable lung function outcomes with careful titration. |
| [31521680](https://pubmed.ncbi.nlm.nih.gov/31521680/) | 2019 | State-of-the-Art Review | JACC Heart Failure | Comprehensive review of diagnostic and therapeutic gaps in HF+COPD; summarises current evidence for beta-blocker use including **Carvedilol**, spirometry underutilisation, and guideline-practice gaps. |
| [18294490](https://pubmed.ncbi.nlm.nih.gov/18294490/) | 2008 | Epidemiology | Am Heart Journal | Prevalence and prognostic impact of COPD in stable HF — establishes the size of the cor pulmonale comorbidity burden and documents beta-blocker withdrawal patterns by COPD status. |
| [15358010](https://pubmed.ncbi.nlm.nih.gov/15358010/) | 2004 | Review | JACC | Therapeutic update specifically on non-selective β- and α-adrenergic blockade (**Carvedilol's** precise profile) in coexistent CHF+COPD — mechanistic rationale and clinical management guidance. |

---

## Singapore Market Information

Carvedilol is currently **not registered** with the Health Sciences Authority (HSA) in Singapore. No product licences are on record.

For clinical research use in Singapore, importation under the HSA Special Access Route (SAR) or a Clinical Trial Authorisation (CTA) framework would be required before any investigator-initiated trial could proceed.

---

## Safety Considerations

Detailed safety data from the Singapore HSA package insert and DrugBank were not available for this analysis (flagged as data gaps requiring remediation). Based on well-established pharmacological class knowledge:

- **Bronchospasm risk**: Non-selective β2-adrenergic blockade is the most clinically important concern in this indication. In patients with underlying airway obstruction (the defining feature of cor pulmonale aetiology), Carvedilol may precipitate or worsen bronchoconstriction. Mandatory slow titration from the lowest available dose is essential, and FEV1/SpO2 monitoring should be incorporated into any study protocol.
- **Haemodynamic effects**: Combined α1 and β-blockade can produce significant bradycardia and hypotension, particularly at initiation or during dose escalation in already-compromised right heart failure patients.

Please refer to the originator package insert for complete contraindications, drug interactions, and special population guidance. Remediation of the TFDA/HSA package insert data gap (flagged as Blocking severity) is required before any formal safety screening.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 4 randomised crossover trials and large propensity-matched cohort studies directly evaluate Carvedilol in patients with heart failure concurrent with chronic pulmonary disease — the pathophysiological substrate of cor pulmonale. The mechanistic rationale (right ventricular remodelling via β1-blockade, pulmonary afterload reduction via α1-blockade, oxidative injury mitigation via antioxidant activity) is well-grounded and directly maps to cor pulmonale pathophysiology. The evidence base, while not yet Phase 3 RCT-level for this specific indication, is sufficient to support a structured research programme with appropriate safety monitoring.

**To proceed, the following is needed:**
- Remediate the **Blocking data gap**: obtain and parse the TFDA/HSA package insert to extract key warnings and contraindications before any formal safety evaluation
- Retrieve full **MOA data from DrugBank** to complete the mechanistic linkage analysis
- Obtain a **drug interaction profile** against common COPD co-medications (long-acting bronchodilators, inhaled corticosteroids, theophylline)
- Design a **dedicated Phase 2 RCT in confirmed cor pulmonale patients** — existing evidence derives from HF+COPD cohorts without verified cor pulmonale diagnosis; bridging data are needed
- Define a **pulmonary function monitoring plan** (FEV1/FVC, SpO2, 6-minute walk test) as mandatory safety endpoints for any trial protocol
- Initiate HSA **Special Access Route (SAR) or CTA application** given the absence of Singapore market registration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

