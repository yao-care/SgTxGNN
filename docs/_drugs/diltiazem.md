---
layout: default
title: Diltiazem
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
---

# Diltiazem
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

# Diltiazem: From Cardiac Arrhythmia & Hypertension to Cerebrovascular Disorder

## One-Sentence Summary

Diltiazem is a non-dihydropyridine calcium channel blocker (CCB) widely used for rate control in atrial fibrillation, hypertension, and angina pectoris.
The TxGNN model's top-ranked prediction uses obsolete ontology terminology; the highest-ranked clinically meaningful indication is **Cerebrovascular Disorder** (rank #4, TxGNN score 97.63%), supported by **6 clinical trials** and **20 publications**.
However, most evidence is indirect — primarily through Diltiazem's role in atrial fibrillation management and its pharmacokinetic interactions with anticoagulants — and targeted direct evidence for cerebrovascular treatment remains limited.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial fibrillation (rate control), hypertension, angina pectoris |
| Predicted New Indication | Cerebrovascular Disorder |
| TxGNN Prediction Score | 97.63% |
| Evidence Level | L3 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data was not retrieved from the database. Based on well-established pharmacological knowledge, Diltiazem belongs to the non-dihydropyridine CCB class. It blocks L-type voltage-gated calcium channels in cardiac and vascular smooth muscle cells, producing vasodilation, heart rate reduction, decreased myocardial contractility, and slowed atrioventricular conduction. These properties underpin its primary clinical uses: rate control in atrial fibrillation, management of hypertension, and treatment of chronic stable angina.

The mechanistic case for cerebrovascular applications is built on multiple indirect pathways. Atrial fibrillation is the leading cause of cardioembolic stroke, and Diltiazem's heart rate control function indirectly reduces cardioembolic risk. Beyond that, L-type calcium channel blockade in cerebrovascular smooth muscle can relieve vasospasm and improve cerebral perfusion — a mechanism directly examined in a 1985 primate model of chronic cerebrovascular spasm (PMID: 2416213) and in a cat middle cerebral artery occlusion model (PMID: 4056906). The landmark NORDIL trial (*Lancet* 2000; PMID: 10972367), a Phase 3 RCT in 10,881 hypertensive patients, provided the broadest population-level data, showing numerically lower fatal and non-fatal stroke rates in the Diltiazem arm compared to diuretics and beta-blockers.

A critical caveat tempers this picture: Diltiazem is a moderate inhibitor of both CYP3A4 and P-glycoprotein. In patients who require concurrent anticoagulation for AF-related stroke prevention — using DOACs such as rivaroxaban or apixaban — Diltiazem significantly elevates DOAC plasma concentrations and may increase major bleeding risk. This pharmacokinetic interaction is well-documented across multiple 2022–2026 cohort studies and a 2026 meta-analysis (PMID: 40326046), creating a complex risk-benefit trade-off that makes Diltiazem a double-edged agent in the cerebrovascular disease setting.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05838664](https://clinicaltrials.gov/study/NCT05838664) | N/A | Completed | 2,140,403 | Large retrospective French registry (2016–2020) comparing stroke, major bleeding, and mortality in AF patients on vs. off oral anticoagulants; provides real-world context for cerebrovascular risk in the AF–Diltiazem population |
| [NCT01176565](https://clinicaltrials.gov/study/NCT01176565) | Phase 3 | Terminated | 1,000 | ATACH-II: intensive BP reduction in acute intracerebral hemorrhage primarily using nicardipine; provides CCB-class context for acute cerebrovascular event management; terminated early due to futility |
| [NCT03529149](https://clinicaltrials.gov/study/NCT03529149) | Phase 4 | Unknown | 90 | TCD-guided blood pressure control after endovascular thrombectomy for ischemic stroke; Diltiazem may be a candidate antihypertensive; evaluates cerebral blood flow optimisation in post-stroke care |
| [NCT06175663](https://clinicaltrials.gov/study/NCT06175663) | N/A | Unknown | 130 | Observational MRI study assessing early brain structural changes in midlife hypertension; relevant to understanding Diltiazem's antihypertensive role in cerebral small vessel disease prevention |
| [NCT02922452](https://clinicaltrials.gov/study/NCT02922452) | Phase 1 | Completed | 16 | PK/DDI study evaluating Diltiazem's effect on BMS-986141 pharmacokinetics; provides quantitative data on CYP3A4-mediated drug level elevation relevant to DOAC co-prescription safety |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not Yet Recruiting | 100 | SAVE STROKE Phase II: AF catheter ablation vs. rate-control medication in patients with new-onset AF at time of stroke; Diltiazem likely included as rate-control comparator; no data yet available |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10972367](https://pubmed.ncbi.nlm.nih.gov/10972367/) | 2000 | RCT | *Lancet* | NORDIL trial: Diltiazem vs. diuretics/beta-blockers in hypertension; comparable combined cardiovascular endpoints; fatal and non-fatal stroke numerically favoured Diltiazem arm |
| [40326046](https://pubmed.ncbi.nlm.nih.gov/40326046/) | 2026 | Meta-analysis | *Ann Pharmacother* | Diltiazem/verapamil co-prescribed with DOACs: contradictory findings across real-world studies; overall signal toward increased bleeding risk requiring clinical vigilance |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Retrospective Cohort | *BMC Medicine* | Multinational cohort in non-valvular AF: antiarrhythmic drugs including diltiazem co-administered with DOACs; quantified stroke prevention vs. bleeding risk trade-off across healthcare systems |
| [37791408](https://pubmed.ncbi.nlm.nih.gov/37791408/) | 2023 | Retrospective Cohort | *Eur Heart J CVP* | Nationwide cohort: P-gp/CYP3A4 inhibitors including diltiazem with NOACs in AF; clinically relevant pharmacokinetic interactions affecting stroke and bleeding outcomes |
| [36149579](https://pubmed.ncbi.nlm.nih.gov/36149579/) | 2023 | Retrospective Cohort | *J Interv Card Electrophysiol* | Diltiazem + DOAC co-prescription in AF: characterised major bleeding risk arising from CYP3A4/P-gp-mediated DDI |
| [35861836](https://pubmed.ncbi.nlm.nih.gov/35861836/) | 2022 | Retrospective Cohort | *J Am Heart Assoc* | Diltiazem with DOACs in 4,544 AF patients: bleeding risk stratified by kidney function; moderate CYP3A4 inhibition increases DOAC exposure, particularly in impaired renal function |
| [2416213](https://pubmed.ncbi.nlm.nih.gov/2416213/) | 1985 | Animal Study | *Am J Cardiol* | Primate model of chronic cerebrovascular spasm (5 days post-haemorrhage): Diltiazem assessed for protection of cerebral arterial structure and function; provides direct mechanistic evidence for cerebrovascular vasodilation |
| [4056906](https://pubmed.ncbi.nlm.nih.gov/4056906/) | 1985 | Animal Study | *J Neurosurg* | Cat MCA occlusion model: IV Diltiazem infusion (0.1–1.0 µg/kg/min) initiated 2 hours before stroke onset; evaluated neuroprotective potential compared to verapamil in acute ischemic stroke |
| [8204245](https://pubmed.ncbi.nlm.nih.gov/8204245/) | 1994 | Clinical Study | *J Clin Anesthesia* | Diltiazem 5 mg bolus vs. nicardipine 1 mg during cerebral aneurysm surgery for subarachnoid haemorrhage: compared effects on internal carotid artery flow velocity and local cerebral blood flow under isoflurane anaesthesia |
| [17309423](https://pubmed.ncbi.nlm.nih.gov/17309423/) | 2007 | Review | *Med J Australia* | Atrial fibrillation management: Diltiazem and verapamil cited as superior to digoxin for exercise heart rate control; supports AF rate-control strategy for reducing cardioembolic cerebrovascular events |

---

## Singapore Market Information

Diltiazem currently has **no active product registrations** with the Singapore Health Sciences Authority (HSA). No license entries are available in the Singapore regulatory database.

---

## Safety Considerations

- **Drug Interactions (from literature)**: Diltiazem is a moderate CYP3A4 and P-glycoprotein inhibitor. Co-administration with DOACs (rivaroxaban, apixaban) significantly increases DOAC plasma concentrations and elevates major bleeding risk — particularly critical in AF patients using anticoagulation for stroke prevention. Multiple large real-world studies (2022–2026) and a meta-analysis have confirmed this DDI as clinically significant. Co-prescription with simvastatin may increase myopathy and rhabdomyolysis risk via CYP3A4 inhibition (PMID: 17304269); a case of fatal intracranial haemorrhage with supratherapeutic INR was reported following a statin switch in a patient on both diltiazem and warfarin.

For complete warnings and contraindications, please refer to the relevant product package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Diltiazem's mechanistic plausibility for cerebrovascular protection is supported by its established AF rate-control function, antihypertensive effects, and preclinical evidence of direct cerebrovascular vasodilation — but no dedicated clinical trial has evaluated Diltiazem as a primary treatment for cerebrovascular disorder. The available evidence is predominantly indirect (AF management, antihypertensive cohorts), evidence level is L3, and the drug's significant DDI risk with DOACs — the mainstay of stroke prevention in AF — creates a complex and potentially hazardous co-prescription scenario. Its absence from the Singapore market further limits immediate clinical deployment.

**To proceed, the following is needed:**
- Retrieval of the full DrugBank MOA record and package insert (complete warnings, contraindications, and DDI profile)
- Singapore HSA regulatory pathway assessment for new registration or research use authorisation
- A prospective clinical trial specifically designed to evaluate Diltiazem's direct effects on cerebrovascular outcomes, independent of AF or hypertension endpoints
- Quantitative DDI risk modelling for Diltiazem + DOAC co-administration in cerebrovascular patients, stratified by renal function
- Alignment with current clinical practice guidelines (ACC/AHA, ESC, Singapore MOH) on CCB use in cerebrovascular disease management before any protocol development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

