---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
---

# Dronedarone
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

# Dronedarone: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Dronedarone (Multaq®) is a Class III multichannel antiarrhythmic agent, internationally approved for reducing cardiovascular hospitalisation and death in patients with paroxysmal or persistent atrial fibrillation (AF) or atrial flutter.
The TxGNN model predicts it may be effective for **Stroke Disorder**, with **19 clinical trials** and **20 publications** currently supporting this direction — including the landmark ATHENA Phase 3 RCT demonstrating a 34% relative risk reduction in stroke/TIA.
Evidence has been scored at **L1**, making this one of the best-supported repurposing candidates in this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial Fibrillation / Atrial Flutter (internationally approved; no Singapore registration on record) |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Dronedarone is a non-iodinated benzofuran derivative and multichannel ion channel blocker that inhibits sodium (INa), rapid and slow potassium (IKr, IKs), L-type calcium (ICaL), and funny current (If) channels. This combined electrophysiological blockade slows ventricular rate during AF episodes and promotes restoration and maintenance of sinus rhythm, reducing overall AF burden. Although detailed MOA data is not yet available from the Singapore regulatory database, dronedarone's pharmacological profile is extensively characterised in the international clinical literature, including well-powered Phase 3 trials.

The mechanistic link between AF rhythm control and stroke prevention is direct and biologically well-grounded: AF generates turbulent, stagnant blood flow within the left atrial appendage, promoting thrombus formation and subsequent cardioembolic stroke — accounting for approximately 20–25% of all ischaemic strokes. By restoring and sustaining sinus rhythm, dronedarone reduces both the duration and frequency of conditions that favour left atrial thrombus formation. The ATHENA Phase 3 RCT demonstrated a 34% relative risk reduction in stroke/TIA (p=0.027) in patients with paroxysmal or persistent AF. Importantly, a mechanistic study (PMID 28992468, Zafar et al. 2017) further demonstrated that dronedarone exerts direct anticoagulant and antiplatelet effects that are independent of its antiarrhythmic action — providing a secondary, rhythm-independent pathway for stroke prevention.

A critical safety boundary must be understood upfront: the PALLAS Phase 3 trial (NCT01151137, n=3,236) was terminated early due to excess mortality and heart failure hospitalisation in patients with **permanent** AF. This trial establishes a hard population boundary — dronedarone's benefit-risk profile is strictly confined to **paroxysmal or persistent AF with preserved ventricular function**. Any clinical application of this repurposing indication must codify this boundary in patient selection criteria.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | Completed | 339 | Pragmatic RCT of early dronedarone vs. usual care in first-detected AF; evaluates composite cardiovascular outcomes including stroke — the most direct completed prospective trial for this repurposing indication |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | Terminated | 3,236 | PALLAS trial: dronedarone vs. placebo in permanent AF with stroke and cardiovascular death as primary endpoints; terminated early due to increased heart failure hospitalisation and all-cause mortality — defines the contraindicated population and establishes the key safety guardrail |
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4: early structured rhythm control (dronedarone as an allowed antiarrhythmic) vs. usual care in AF; stroke/TIA is a pre-specified key secondary endpoint — landmark trial demonstrating benefit of early rhythm control strategy |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | Not Yet Recruiting | 1,898 | Multicenter prospective study of dronedarone for early AF rhythm control; evaluates efficacy, safety, and quality of life with stroke-related endpoints; expected completion December 2028 |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | Observational | Completed | 1,015 | Real-world comparative effectiveness of dronedarone vs. other antiarrhythmics across Germany, Spain, Italy, and USA; stroke outcome is among the comparative endpoints |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | Unknown | 100 | Amiodarone vs. dronedarone post-cardioversion for sinus rhythm maintenance; indirectly evaluates stroke risk through rhythm control outcomes |
| [NCT03993119](https://clinicaltrials.gov/study/NCT03993119) | Observational | Completed | 500 | Cross-sectional study of NOAC management in elderly NVAF patients for stroke prevention; characterises dronedarone drug interactions affecting anticoagulation efficacy |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA trial: catheter ablation vs. antiarrhythmic drugs (including dronedarone) for AF; stroke is a safety secondary endpoint across a large, diverse AF population |
| [NCT02294955](https://clinicaltrials.gov/study/NCT02294955) | N/A | Unknown | 152 | CAPTAF: catheter ablation vs. optimised pharmacological therapy (dronedarone as an option) in symptomatic AF; evaluates rhythm control strategies with stroke as a secondary measure |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, Not Recruiting | 484 | Pulsed field ablation vs. antiarrhythmic drugs (including dronedarone) as first-line treatment for persistent AF; ongoing with stroke-related safety endpoints |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT Post-hoc Analysis | Clin Res Cardiol | Long-term safety and efficacy of amiodarone and dronedarone for early rhythm control in EAST-AFNET 4; provides updated outcome data for both drugs in a large AF population |
| [40295782](https://pubmed.ncbi.nlm.nih.gov/40295782/) | 2025 | RCT Post-hoc Analysis | Europace | Post-hoc ATHENA analysis using EAST-AFNET 4 inclusion criteria; confirms dronedarone improves cardiovascular outcomes — including stroke — in early AF patients with cardiovascular comorbidities |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | Systematic Review/Meta-analysis | Cochrane Database Syst Rev | Cochrane review of antiarrhythmics for sinus rhythm maintenance after cardioversion of AF; comprehensive evidence synthesis on dronedarone's effects on mortality and clinical outcomes |
| [20396635](https://pubmed.ncbi.nlm.nih.gov/20396635/) | 2010 | RCT Subanalysis (ATHENA) | Clin Interv Aging | Direct analysis of dronedarone's impact on stroke reduction in the ATHENA trial data; quantifies stroke and TIA risk reduction in AF/AFL patients |
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | Systematic Review & Meta-analysis | Am J Cardiovasc Drugs | Systematic review and meta-analysis of dronedarone's effect on stroke incidence in paroxysmal/persistent AF across randomised trials; supports a significant reduction in stroke risk |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | Mechanistic/Clinical Study | Atherosclerosis | Dronedarone exhibits direct anticoagulant and antiplatelet effects independent of its antiarrhythmic action — provides a second mechanistic pathway for stroke prevention beyond rhythm control alone |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Observational Cohort | J Atrial Fibrillation | Real-world analysis of stroke, heart failure, interstitial lung disease, and liver injury risks with dronedarone vs. other antiarrhythmics in US clinical practice (n=10,455 patients) |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | Clinical Study (ATHENA Post-hoc) | Eur J Heart Failure | Dronedarone in AF with HFpEF and HFmrEF; evaluates cardiovascular outcomes in the preserved/mildly reduced ejection fraction population — defines the eligible patient group |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | Retrospective Cohort | Circ Arrhythm Electrophysiol | Dronedarone vs. sotalol in antiarrhythmic drug-naive veterans with AF; large VA database analysis of comparative effectiveness and safety including stroke outcomes |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review/Approval Analysis | Vasc Health Risk Manag | Dronedarone FDA approval and efficacy for AF/atrial flutter; reviews ATHENA data showing reductions in all-cause mortality and cardiovascular hospitalisation, and a post-hoc decrease in stroke risk |

---

## Singapore Market Information

Dronedarone is currently **not registered** in Singapore. No active HSA licences are on record.

> Dronedarone is marketed internationally as Multaq® 400 mg film-coated tablets (approved in the USA since 2009 and in the EU for paroxysmal/persistent AF or atrial flutter). Any clinical use in Singapore would require a Special Access Route (SAR) application to the Health Sciences Authority prior to procurement or prescribing.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical Safety Signal from Clinical Evidence:** The PALLAS Phase 3 trial (NCT01151137) was terminated early due to significantly increased mortality and heart failure hospitalisation in patients with **permanent atrial fibrillation**. International regulatory authorities (FDA, EMA) have issued black-box–equivalent warnings contraindicting dronedarone in: (1) **permanent AF**, (2) **symptomatic heart failure with recent decompensation or NYHA Class IV**, and (3) **sick sinus syndrome or second/third-degree AV block without a functioning permanent pacemaker**. These are non-negotiable population exclusions for any clinical application of this repurposing indication.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The ATHENA Phase 3 RCT — corroborated by two 2025 post-hoc analyses, a Cochrane systematic review, multiple completed Phase 4 trials, and mechanistic evidence of direct antithrombotic effects — provides L1-level evidence that dronedarone reduces stroke and TIA risk in patients with paroxysmal or persistent AF. The evidence base is mature and consistent. However, the PALLAS trial's early termination establishes irreversible safety boundaries that must be enforced through strict patient selection before any clinical application proceeds.

**To proceed, the following is needed:**
- **Singapore regulatory pathway:** Assess eligibility for HSA Special Access Route or initiate new drug application
- **MOA documentation:** Retrieve full DrugBank pharmacology entry to complete mechanistic analysis (Data Gap DG002)
- **Package insert review:** Download and parse international label (FDA/EMA) to formally document contraindications and key warnings (Data Gap DG001)
- **Patient selection protocol:** Restrict use strictly to paroxysmal or persistent AF with preserved left ventricular function (LVEF ≥35%), excluding permanent AF, decompensated heart failure, and patients without pacemaker cover for sick sinus syndrome
- **Cardiac monitoring plan:** Baseline and follow-up 12-lead ECG, liver function tests (LFTs at 1, 3, 6 months), pulmonary function, and renal function
- **Drug interaction management plan:** Address P-glycoprotein inhibition by dronedarone (increases plasma levels of digoxin and certain DOACs including rivaroxaban); dose adjustment protocols required for co-administration
- **Local clinical consultation:** Engage Singapore cardiologists to assess unmet clinical need and feasibility of trial or compassionate use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

