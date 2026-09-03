---
layout: default
title: Norepinephrine
parent: 僅模型預測 (L5)
nav_order: 713
evidence_level: L5
indication_count: 10
---

# Norepinephrine
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

# Norepinephrine: From Vasopressor Support in Acute Hypotension/Shock to Obstructive Lung Disease

## One-Sentence Summary

Norepinephrine (DB00368) is a catecholamine best known clinically as a vasopressor used to support blood pressure in acute hypotension and shock states; detailed original-indication and mechanism-of-action data are not available in this evidence pack, and the drug is currently **not marketed in Singapore**. The TxGNN model's top-ranked prediction is that it may be relevant to **Obstructive Lung Disease**, but this is supported only by **17 clinical trials** (none testing norepinephrine as a treatment for this indication) and **19 publications**, most of which describe norepinephrine as a disease biomarker rather than a therapeutic agent.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in Singapore registration data (drug not marketed); internationally, norepinephrine is used as a vasopressor for acute hypotension and shock |
| Predicted New Indication | Obstructive Lung Disease |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism-of-action data for norepinephrine is not available in this evidence pack. Based on general pharmacological knowledge, norepinephrine is an endogenous catecholamine and a potent non-selective α1/α2- and β1-adrenergic receptor agonist, clinically used to raise blood pressure via vasoconstriction and increased cardiac contractility. Its intrinsic β2 (bronchodilator) activity is weak, which is the key mechanistic limitation for any extrapolation to obstructive airway disease.

The rationale linking norepinephrine to obstructive lung disease is indirect: the autonomic nervous system, including noradrenergic signaling, is known to participate in airway caliber regulation, and patients with COPD and asthma show altered plasma catecholamine levels correlated with hypoxemia and hemodynamic status. However, the available literature and trials largely characterize norepinephrine as a **disease-state biomarker** (elevated in hypoxemic, hemodynamically compromised COPD patients) rather than demonstrating any therapeutic benefit of administering norepinephrine to treat obstructive lung disease.

Because norepinephrine lacks meaningful β2-agonist activity, and no identified trial administers it as a bronchodilator or COPD/asthma therapy, this connection should be interpreted as a knowledge-graph-level association reflecting shared physiological pathways (sympathetic/adrenergic regulation of the airway and vasculature) rather than a validated treatment hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02360865](https://clinicaltrials.gov/study/NCT02360865) | NA | Completed | 18 | Investigated endothelial dysfunction and muscle sympathetic nerve activity as mechanisms of exercise intolerance in COPD. |
| [NCT01536587](https://clinicaltrials.gov/study/NCT01536587) | Phase 4 | Completed | 32 | Assessed whether inhaled salmeterol reduces sympathetic (adrenergic) activity via microneurography in COPD GOLD II/III patients. |
| [NCT01219738](https://clinicaltrials.gov/study/NCT01219738) | NA | Completed | 20 | Examined non-genomic glucocorticoid (budesonide) effects on adrenergic agonist transport in airway vascular smooth muscle, involving endogenous norepinephrine signaling. |
| [NCT00834509](https://clinicaltrials.gov/study/NCT00834509) | N/A | Completed | 181 | Explored blood/urine biomarkers for diagnosing obstructive sleep apnea; not a norepinephrine intervention trial. |
| [NCT02564406](https://clinicaltrials.gov/study/NCT02564406) | NA | Completed | 35 | Assessed extracorporeal CO2 removal in COPD patients with hypercapnic respiratory failure who declined intubation. |
| [NCT04280497](https://clinicaltrials.gov/study/NCT04280497) | NA | Recruiting | 1800 | Compared corticosteroid therapy vs. placebo in sepsis, with vasopressor use (potentially including norepinephrine) as part of a composite endpoint. |
| [NCT07332442](https://clinicaltrials.gov/study/NCT07332442) | Phase 3 | Not yet recruiting | 250 | Testing whether arousal threshold modification affects CPAP adherence in obstructive sleep apnea; no norepinephrine arm. |
| [NCT02627378](https://clinicaltrials.gov/study/NCT02627378) | Phase 1 | Completed | 35 | ECMO support for MERS-CoV-induced respiratory failure; vasopressors used as supportive, not primary, therapy. |
| [NCT05664204](https://clinicaltrials.gov/study/NCT05664204) | NA | Recruiting | 200 | Evaluating intraoperative ECMO strategy during lung transplantation to reduce need for mechanical ventilation. |
| [NCT04234217](https://clinicaltrials.gov/study/NCT04234217) | NA | Recruiting | 300 | Investigating mechanisms linking sleep apnea to prediabetes development. |

**None of the above trials tests norepinephrine as a treatment for obstructive lung disease** — its appearance is limited to mechanistic/supportive-care contexts.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29030339](https://pubmed.ncbi.nlm.nih.gov/29030339/) | 2018 | Cohort | Am J Physiol Heart Circ Physiol | Found impaired muscle α-adrenergic responsiveness (blunted functional sympatholysis) during exercise in COPD, using tyramine-evoked norepinephrine release. |
| [9009625](https://pubmed.ncbi.nlm.nih.gov/9009625/) | 1996 | Cohort | Monaldi Arch Chest Dis | Measured plasma noradrenaline and other hormones during right heart catheterization in COPD patients. |
| [2048831](https://pubmed.ncbi.nlm.nih.gov/2048831/) | 1991 | Review | Am Rev Respir Dis | Reviewed autonomic (cholinergic/noradrenergic) control of airway caliber in asthma and COPD. |
| [1617386](https://pubmed.ncbi.nlm.nih.gov/1617386/) | 1992 | Review | Br Med Bull | Described sympathetic (noradrenaline/NPY) constriction of tracheobronchial vasculature. |
| [11099681](https://pubmed.ncbi.nlm.nih.gov/11099681/) | 2000 | Review | Am J Med | Investigated hypoxemia, hypercapnia, and cardiovascular hormones including norepinephrine as mechanisms of hypertension in COPD with acute respiratory failure. |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Pending | Scand J Clin Lab Invest | Reported elevated plasma noradrenaline in chronic obstructive lung disease, inversely correlated with arterial oxygen saturation. |
| [3420304](https://pubmed.ncbi.nlm.nih.gov/3420304/) | 1988 | Pending | Respiration | Assessed hemodynamic effects of dopamine/L-dopa in pulmonary hypertension secondary to COPD. |
| [3332227](https://pubmed.ncbi.nlm.nih.gov/3332227/) | 1987 | Pending | Crit Care Clin | Reviewed catecholamine (norepinephrine, epinephrine, dopamine) release and vasoregulation in critical illness. |
| [35870527](https://pubmed.ncbi.nlm.nih.gov/35870527/) | 2022 | Pending | Environ Pollut | Panel study linking short-term air pollution exposure to neuroendocrine (HPA/SAM axis) stress hormone dysregulation in COPD patients. |
| [24486056](https://pubmed.ncbi.nlm.nih.gov/24486056/) | 2014 | Pending | Semin Immunol | Reviewed neuroendocrine-immune interactions, including sympathetic regulation of inflammation. |

**All identified literature characterizes norepinephrine as a physiological/disease-state marker in obstructive lung disease, not as a studied therapeutic agent.**

---

## Singapore Market Information

Norepinephrine is currently **not marketed in Singapore** — no product registrations (SIN numbers) or approved indication text are available in this evidence pack.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but the supporting evidence is entirely mechanistic/observational (Evidence Level L4) — no clinical trial or publication tests norepinephrine as a treatment for obstructive lung disease, and its pharmacology (weak β2 activity) does not support a bronchodilator role. Combined with the drug's unmarketed status in Singapore and missing safety/MOA data, this candidate does not meet the bar to advance.

**To proceed, the following is needed:**
- Package insert warnings/contraindications (currently a blocking data gap)
- Confirmed mechanism-of-action data from DrugBank or equivalent source (currently a high-severity data gap)
- Direct interventional evidence evaluating norepinephrine (or adrenergic modulation more broadly) in COPD/obstructive lung disease patients, rather than observational biomarker studies
- Note: among the other candidates in this evidence pack, **anaphylaxis** (rank 8, Evidence Level L3, decision stage S2, recommendation "Proceed with Guardrails") has a substantially stronger and more clinically established rationale — norepinephrine is already used as a second-line/adjunct vasopressor in refractory anaphylactic shock — and may warrant separate, prioritized evaluation.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

