---
layout: default
title: Eplerenone
parent: 僅模型預測 (L5)
nav_order: 381
evidence_level: L5
indication_count: 10
---

# Eplerenone
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

# Eplerenone: From Heart Failure to Pulmonary Hypertension with Unclear Multifactorial Mechanism

## One-Sentence Summary

Eplerenone is a selective mineralocorticoid receptor antagonist (MRA) with established clinical use in chronic heart failure with reduced ejection fraction (HFrEF) and post-myocardial infarction heart failure.
The TxGNN model's top prediction is **pulmonary hypertension with unclear multifactorial mechanism** (score 99.50%), however this top-ranked indication has **no supporting clinical trials or publications** (Evidence Level: L5).
Across all 10 evaluated predictions, the most evidence-backed candidate is **Chronic Pulmonary Heart Disease (Cor Pulmonale)** (Rank 6), supported by **6 clinical trials** and **4 directly relevant publications** (Evidence Level: L3); two additional cerebrovascular indications (Ranks 9–10) show promising preclinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure (post-MI; HFrEF NYHA Class II–IV) and hypertension — inferred from clinical trial evidence; formal indication text not available in this evidence pack |
| Predicted New Indication (Rank 1) | Pulmonary Hypertension with Unclear Multifactorial Mechanism |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 (Rank 1 prediction); L3 for Chronic Pulmonary Heart Disease (Rank 6) |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Rank 1) / Research Question (Ranks 6, 9, 10) |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known clinical information, Eplerenone is a selective mineralocorticoid receptor (MR) antagonist — it blocks aldosterone binding at the MR, thereby inhibiting sodium retention, aldosterone-driven cardiac fibrosis, and vascular remodeling. Its efficacy in heart failure has been definitively proven: the landmark EMPHASIS-HF trial (NCT00232180, n=2,743) demonstrated a 37% relative risk reduction in the composite of cardiovascular death or heart failure hospitalization in HFrEF patients (NYHA Class II, EF ≤35%), and mechanistically may be applicable to pulmonary vascular disease via the same anti-fibrotic axis.

For the top-ranked prediction — pulmonary hypertension with unclear multifactorial mechanism — the rationale is theoretically plausible: aldosterone can promote pulmonary vascular smooth muscle proliferation and perivascular fibrosis through MR activation. However, by definition, this disease category has an unclarified pathogenesis, meaning it is unknown whether the aldosterone-MR axis is a primary driver. The high TxGNN score most likely reflects shared cardiovascular comorbidity node patterns in the knowledge graph rather than direct mechanistic support, and should not be interpreted as clinical evidence.

The most clinically grounded prediction is **Chronic Pulmonary Heart Disease / Cor Pulmonale (Rank 6)**. A 2018 animal study (PMID 29499691) directly showed that Eplerenone significantly attenuates pulmonary *vascular* remodeling — specifically fibrosis — in a rat pulmonary arterial hypertension model, though it did not improve right ventricular remodeling. A critical counterpoint (PMID 24067600) found no benefit of Eplerenone combined with losartan in an isolated right ventricular failure model, signaling that the well-established benefits in left-sided HF may not translate to predominantly right-sided failure — the dominant pathology in advanced Cor Pulmonale. This mechanistic contradiction is the central unresolved question for this indication.

---

## Clinical Trial Evidence

*The following trials are associated with **Chronic Pulmonary Heart Disease (Cor Pulmonale)** — Rank 6, the highest-evidence predicted indication. The Rank 1 prediction (pulmonary hypertension with unclear multifactorial mechanism) has no registered clinical trials. Trials are sorted by direct relevance to Eplerenone.*

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00232180](https://clinicaltrials.gov/study/NCT00232180) | Phase 3 | Completed | 2,743 | EMPHASIS-HF: Eplerenone vs. placebo in HFrEF (NYHA II, EF ≤35%). Significantly reduced composite of CV death or HF hospitalization (HR 0.63, p<0.001). Landmark efficacy data; indication is left-sided HF, but many patients carry secondary pulmonary hypertension — direct extrapolation to Cor Pulmonale requires caution. |
| [NCT01115855](https://clinicaltrials.gov/study/NCT01115855) | Phase 3 | Completed | 221 | Japanese CHF cohort: Eplerenone vs. placebo for CV mortality and HF hospitalization. Smaller regional study consistent with EMPHASIS-HF findings; indication is general HF, not Cor Pulmonale-specific. Supports ethnic generalizability. |
| [NCT07029503](https://clinicaltrials.gov/study/NCT07029503) | Phase 2 | Recruiting | 40 | SCARF-1: Eplerenone in HFrEF with severe CKD. Open-label pilot exploring feasibility and safety in cardiorenal syndrome — a population with significant hyperkalemia risk. Results will inform safety boundaries relevant to Cor Pulmonale patients with renal impairment. |
| [NCT02354352](https://clinicaltrials.gov/study/NCT02354352) | Phase 3 | Completed | 52 | Duchenne Muscular Dystrophy: spironolactone vs. eplerenone for cardiac and pulmonary function preservation. Genetic cardiomyopathy with distinct pathomechanism; limited external validity to Cor Pulmonale, but provides comparative MRA safety data. |
| [NCT05198791](https://clinicaltrials.gov/study/NCT05198791) | Phase 2 | Recruiting | 350 | MRA therapy in acute MI or myocardial injury patients with microvascular disease. Eplerenone is the primary intervention; cardiovascular microvascular endpoints — relevant to shared disease substrate with pulmonary vascular disease. |
| [NCT06697353](https://clinicaltrials.gov/study/NCT06697353) | N/A (Observational) | Completed | 4,936 | ROVER Japan: real-world outcomes with Vericiguat (sGC stimulator) in HFrEF. Study drug is not Eplerenone; provides epidemiological background on HFrEF population and co-occurring pulmonary complications. |

---

## Literature Evidence

*The following publications represent the most directly Eplerenone-relevant findings across Chronic Pulmonary Heart Disease (Rank 6) and Cerebrovascular Indications (Ranks 9–10). The 20 papers retrieved for Rank 2 (pulmonary hypertension owing to hypoxia) were reviewed and found to be general hypoxia biology literature with no direct Eplerenone content, and are excluded.*

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29499691](https://pubmed.ncbi.nlm.nih.gov/29499691/) | 2018 | Animal Study | BMC Pulmonary Medicine | Eplerenone significantly attenuates pulmonary **vascular** remodeling and fibrosis in a rat PAH model, but does not improve right ventricular remodeling. Key direct mechanistic support for pulmonary vascular indication; also identifies the RV as a critical evidence gap. |
| [24067600](https://pubmed.ncbi.nlm.nih.gov/24067600/) | 2013 | Animal Study | International Journal of Cardiology | Eplerenone + losartan shows **no benefit** in isolated experimental right ventricular failure model. Critical counterevidence: treatment approach established in left-sided HF does not appear to transfer to pressure-overloaded RV. |
| [32919912](https://pubmed.ncbi.nlm.nih.gov/32919912/) | 2020 | Cohort | JACC Heart Failure | TOPCAT trial sub-analysis: aldosterone antagonist therapy in HFpEF. Indirect class-level evidence for MRA benefit in heart failure spectrum with preserved EF. |
| [17475237](https://pubmed.ncbi.nlm.nih.gov/17475237/) | 2007 | Animal Study | European Journal of Pharmacology | Eplerenone pretreatment reduces infarct volume by ~25% in mouse middle cerebral artery occlusion (MCAO) model. Strongest **direct** animal evidence for Eplerenone in acute ischemic stroke neuroprotection. |
| [23316294](https://pubmed.ncbi.nlm.nih.gov/23316294/) | 2012 | Animal Study | Journal of the American Heart Association | Myeloid cell mineralocorticoid receptor mediates post-ischemic neuroinflammation in experimental stroke. MR blockade is neuroprotective in a model- and sex-dependent manner — highlights need for sex-stratified clinical trial design. |
| [17670862](https://pubmed.ncbi.nlm.nih.gov/17670862/) | 2007 | Animal Study | AJP Regulatory, Integrative and Comparative Physiology | MR antagonism reduces cerebral infarct size in male stroke-prone hypertensive rats but shows **no protective response in intact females**. Estrogen may modulate MR signaling — a critical sex-difference signal for future trial design. |
| [29622372](https://pubmed.ncbi.nlm.nih.gov/29622372/) | 2018 | Pilot Clinical Study | Journal of Stroke and Cerebrovascular Diseases | Eplerenone pilot study in hypertensive patients with unruptured cerebral aneurysms. Animal data showed MR blockade prevented aneurysm formation; this pilot evaluated growth/rupture prevention in humans. Provides the only Eplerenone-specific cerebrovascular clinical data. |
| [30118343](https://pubmed.ncbi.nlm.nih.gov/30118343/) | 2018 | Animal Study | AJP Heart and Circulatory Physiology | MR antagonism improves cerebral parenchymal arteriole dilation via TRPV4-dependent mechanism and prevents cognitive dysfunction in hypertension mouse model. Mechanistic pathway linking MR blockade to cerebral microvascular protection. |
| [15134822](https://pubmed.ncbi.nlm.nih.gov/15134822/) | 2004 | Review | Molecular and Cellular Endocrinology | Eplerenone organ protection: MR expression in heart, vasculature, and brain. Foundational review establishing extra-renal targets of aldosterone and the rationale for Eplerenone's cardiovascular and cerebrovascular protective roles. |
| [22717248](https://pubmed.ncbi.nlm.nih.gov/22717248/) | 2012 | Clinical Study | Canadian Journal of Cardiology | High plasma aldosterone is associated with progression of carotid plaque in humans; spironolactone/eplerenone (MRA) ameliorate adverse aldosterone vascular effects in animal models. Translational evidence linking aldosterone to human atherosclerosis and cerebrovascular risk. |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for future assessment:** Formal safety data (warnings, contraindications, drug-drug interactions) are not available in this evidence pack. Given Eplerenone's drug class, key safety areas to document include: hyperkalemia risk (particularly with ACE inhibitors, ARBs, potassium-sparing diuretics), contraindications in severe renal impairment (eGFR <30 mL/min), and use in patients with adrenal insufficiency. These should be retrieved from the TFDA package insert PDF prior to any clinical planning.

---

## Conclusion and Next Steps

### Rank 1 — Pulmonary Hypertension with Unclear Multifactorial Mechanism

**Decision: Hold**

**Rationale:**
No clinical trials or literature directly address Eplerenone in this disease category. The high TxGNN score reflects knowledge graph architecture, not clinical evidence. The disease category's "unclear multifactorial mechanism" designation means the primary pathogenic pathway is undefined, making targeted MR antagonism rationale speculative rather than evidence-based.

**To proceed, the following is needed:**
- Disease reclassification into a specific, actionable subtype (e.g., WHO Group 5 PH) before any evidence search is meaningful
- Proof-of-concept mechanistic studies establishing whether aldosterone-MR signaling is active in the intended patient population
- Full safety profile documentation (TFDA package insert, DrugBank MOA)

---

### Rank 6 — Chronic Pulmonary Heart Disease (Cor Pulmonale)

**Decision: Research Question**

**Rationale:**
One direct animal study demonstrates pulmonary vascular anti-remodeling effects (PMID 29499691), and two completed Phase 3 trials establish Eplerenone's efficacy in left-sided HF (NCT00232180, NCT01115855). However, PMID 24067600 provides a direct counterpoint showing no benefit in isolated RV failure — the core pathophysiology of advanced Cor Pulmonale — and no dedicated clinical trial for this indication exists.

**To proceed, the following is needed:**
- Dedicated animal studies in Cor Pulmonale models (not PAH-only or isolated RV pressure models)
- Biomarker studies measuring aldosterone activation and MR expression in Cor Pulmonale patients
- Safety profile specific to this population (COPD patients frequently co-prescribed bronchodilators, diuretics, and inhaled corticosteroids — DDI risk not yet assessed)
- Pilot RCT with pulmonary vascular resistance and RV function as co-primary endpoints

---

### Ranks 9–10 — Cerebrovascular Disorder / Cerebral Artery Occlusion

**Decision: Research Question**

**Rationale:**
Three convergent animal studies demonstrate MR blockade reduces ischemic brain injury volume (PMID 17475237), modulates post-stroke neuroinflammation (PMID 23316294), and improves cerebral microvascular function (PMID 30118343). A human pilot study in cerebral aneurysms (PMID 29622372) provides the only clinical signal. A critical sex-stratification finding — no protection in intact female rats (PMID 17670862) — must be addressed in any trial design.

**To proceed, the following is needed:**
- Human proof-of-concept RCT in hypertensive patients at high cerebrovascular risk, with sex-stratified analysis as a pre-specified subgroup
- Assessment of Eplerenone safety in patients receiving concurrent antiplatelet or anticoagulant therapy (standard in stroke prevention)
- Clarification of whether the MCAO model results (anterior circulation) are relevant to posterior circulation events such as brainstem infarction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

