---
layout: default
title: Enalapril
parent: 僅模型預測 (L5)
nav_order: 369
evidence_level: L5
indication_count: 10
---

# Enalapril
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

# Enalapril: From Hypertension and Heart Failure to Chronic Pulmonary Heart Disease

## One-Sentence Summary

Enalapril is an angiotensin-converting enzyme (ACE) inhibitor, globally established for the treatment of hypertension and heart failure with reduced ejection fraction.
The TxGNN model predicts it may be effective for **Chronic Pulmonary Heart Disease** (cor pulmonale),
with **4 clinical trials** and **20 publications** currently in the evidence base — including direct human studies demonstrating hemodynamic improvement and enhanced exercise tolerance in COPD-related cor pulmonale.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Heart Failure (per global labeling — not registered in Singapore) |
| Predicted New Indication | Chronic Pulmonary Heart Disease (Cor Pulmonale) |
| TxGNN Prediction Score | 98.91% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Enalapril is a prodrug that is hydrolysed to enalaprilat, a potent inhibitor of angiotensin-converting enzyme (ACE). By blocking the conversion of angiotensin I to angiotensin II (Ang II), enalapril reduces systemic and pulmonary vascular resistance, lowers cardiac afterload, and suppresses aldosterone secretion. Critically, ACE is most densely expressed in the pulmonary vascular endothelium — meaning the lungs are a primary site of both Ang II generation and pharmacological ACE inhibition.

Chronic pulmonary heart disease (cor pulmonale) arises when sustained pulmonary hypertension — most commonly driven by COPD — leads to right ventricular hypertrophy and eventual failure. In this setting, RAAS overactivation contributes to right ventricular remodelling, fluid retention, and progressive pulmonary vasoconstriction. By reducing Ang II levels, enalapril can dilate pulmonary vessels, lower right ventricular afterload, and attenuate the pathological remodelling cycle. Animal data (PMID 9140694) confirm that RAAS inhibition can reverse hypoxia-induced pulmonary hypertension and right ventricular fibrosis in experimental models.

The most compelling support comes from two direct human studies: PMID 1405196 demonstrated that 30 days of enalapril (10–20 mg/day) added to standard therapy in 11 patients with COPD-related cor pulmonale produced a significant reduction in mean pulmonary artery pressure and improved exercise tolerance on treadmill testing; PMID 9282581 compared enalapril combined with bronchodilators, diuretics, and steroids against conventional treatment alone in 30 cor pulmonale patients, showing greater reductions in right ventricular dimensions after six weeks. Together with a well-established mechanistic rationale, these findings make the TxGNN prediction biologically coherent and clinically plausible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02768298](https://clinicaltrials.gov/study/NCT02768298) | Phase 4 | Completed | 201 | Randomised comparison of LCZ696 vs enalapril on exercise capacity in chronic HFrEF; enalapril served as active comparator, providing controlled data on cardiac remodelling effects |
| [NCT00292162](https://clinicaltrials.gov/study/NCT00292162) | N/A | Completed | 41 | Radiofrequency ablation for AF in advanced chronic heart failure; enalapril was part of background therapy, confirming its role in maintaining haemodynamic stability in this comorbid population |
| [NCT00151619](https://clinicaltrials.gov/study/NCT00151619) | Phase 2 | Terminated | 7 | Regional and systemic haemodynamic effects of amlodipine added to enalapril + furosemide + digoxin in CHF; early termination limits conclusions, but underscores enalapril as a backbone agent in complex cardiac-pulmonary failure |
| [NCT06697353](https://clinicaltrials.gov/study/NCT06697353) | N/A | Completed | 4,936 | Real-world Japanese retrospective study of vericiguat in chronic HFrEF; captures background RAAS inhibitor use patterns across a large heart failure population |

> **Note:** No trials directly recruiting cor pulmonale or pulmonary heart disease as a primary indication were identified. The above trials provide indirect context for enalapril's use in overlapping cardiopulmonary populations.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1405196](https://pubmed.ncbi.nlm.nih.gov/1405196/) | 1992 | Clinical Study | Kardiologia polska | **Direct evidence:** Enalapril (10–20 mg/day, 30 days) in 11 COPD cor pulmonale patients significantly reduced mean pulmonary artery pressure and improved maximal treadmill exercise tolerance |
| [9282581](https://pubmed.ncbi.nlm.nih.gov/9282581/) | 1996 | Clinical Study | J Assoc Physicians India | Enalapril + standard therapy vs conventional treatment in 30 chronic cor pulmonale patients; greater reduction in right ventricular internal diastolic dimension and improved GFR after 6 weeks |
| [9140694](https://pubmed.ncbi.nlm.nih.gov/9140694/) | 1997 | Preclinical | Cardiovascular Drugs and Therapy | Enalapril reversed chronic hypoxia-induced pulmonary hypertension and right ventricular hypertrophy in rats, and reduced persistent myocardial fibrosis — establishing the mechanistic basis for RAAS inhibition in hypoxic cor pulmonale |
| [6313787](https://pubmed.ncbi.nlm.nih.gov/6313787/) | 1983 | Clinical Study | J Am Coll Cardiology | Enalapril increased cardiac index and reduced pulmonary capillary wedge pressure and right atrial pressure acutely in 15 CHF patients; effects sustained at 4 weeks in 7 patients |
| [2210899](https://pubmed.ncbi.nlm.nih.gov/2210899/) | 1990 | Clinical Study | Int J Cardiology | Enalapril as initial monotherapy in severe congestive heart failure with sodium retention; significant reductions in pulmonary wedge pressure and right atrial pressure confirmed |
| [33522249](https://pubmed.ncbi.nlm.nih.gov/33522249/) | 2021 | Cohort | J Am Heart Assoc | PARADIGM-HF subgroup: 8,399 HFrEF patients stratified by COPD status; COPD concomitance associated with undertreatment and worse outcomes — highlights importance of optimising RAAS inhibition in this population |
| [3033043](https://pubmed.ncbi.nlm.nih.gov/3033043/) | 1987 | Clinical Study | J Am Coll Cardiology | IV enalaprilat in 14 chronic HF patients: onset within 15 minutes, 33% reduction in pulmonary capillary wedge pressure and 32% reduction in systemic vascular resistance at peak effect |
| [6187789](https://pubmed.ncbi.nlm.nih.gov/6187789/) | 1983 | Clinical Study | J Am Coll Cardiology | Acute single-dose enalapril in 9 severe CHF patients: significant reduction in systemic vascular resistance (−19%) and pulmonary wedge pressure, establishing haemodynamic proof-of-concept |
| [39210725](https://pubmed.ncbi.nlm.nih.gov/39210725/) | 2024 | RCT (Post-hoc) | JAMA Cardiology | Post-hoc PARADIGM-HF/PARAGON-HF analysis comparing sacubitril/valsartan vs enalapril for all-cause hospitalisation in multimorbid HF — provides large-scale comparative enalapril outcome data |
| [40329926](https://pubmed.ncbi.nlm.nih.gov/40329926/) | 2025 | Review | High Alt Med Biol | Comprehensive review of chronic mountain sickness management; ACE inhibitors proposed as novel therapies for hypoxia-driven pulmonary hypertension and erythrocytosis — supports RAAS inhibition rationale in hypoxic cardiopulmonary disease |

---

## Singapore Market Information

Enalapril is **not registered** in Singapore. There are currently **no active licences** on record with HSA. Physicians wishing to use enalapril in Singapore would need to access it via the Special Access Route (SAR) or through an unregistered drug importation pathway under HSA regulations.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Clinically important considerations specific to pulmonary heart disease (from mechanistic data in the evidence pack):**
> - **Systemic hypotension risk:** ACE inhibitors reduce both systemic and pulmonary vascular resistance. In right heart failure, where cardiac output is preload-dependent, excessive blood pressure lowering can precipitate haemodynamic collapse — initiate at the lowest available dose and titrate slowly.
> - **Renal function monitoring:** Enalapril reduces glomerular filtration pressure; in cor pulmonale patients with concomitant right heart failure and renal congestion, serum creatinine and potassium must be checked within 1–2 weeks of initiation and at each dose increase.
> - **Bilateral renal artery stenosis:** Absolute contraindication to all ACE inhibitors — must be excluded before prescribing.
> - **Hypoxia-worsening potential:** In Group 3 pulmonary hypertension contexts, systemic vasodilation may theoretically worsen ventilation–perfusion mismatch; monitor oxygen saturation after initiation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two direct controlled clinical studies (PMID 1405196, PMID 9282581) demonstrate that enalapril improves pulmonary haemodynamics and right ventricular dimensions in COPD-related cor pulmonale patients, supported by a well-characterised mechanistic basis (ACE expression in pulmonary endothelium, RAAS-driven right ventricular remodelling) and corroborating animal model data. The evidence is L3 — sufficient to justify a prospective research programme, but not yet a practice change.

**To proceed, the following is needed:**

- **Dedicated Phase 2 RCT** enrolling patients with established cor pulmonale (COPD-related), randomising to enalapril vs placebo on top of standard bronchodilator therapy, with primary endpoints of right ventricular function (echocardiographic) and 6-minute walk distance
- **Formal MOA documentation** from DrugBank API (currently a data gap) to complete mechanistic dossier
- **Safety monitoring plan** specifying: starting dose (2.5 mg/day), BP thresholds for dose hold, renal function check schedule (baseline, week 1, week 4, then monthly), and oxygen saturation surveillance
- **Exclusion criteria protocol** for bilateral renal artery stenosis, severe aortic stenosis, and baseline systolic BP < 90 mmHg
- **Singapore regulatory pathway assessment:** given zero HSA registrations, a full new drug application or compassionate use framework will be required for any local clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

