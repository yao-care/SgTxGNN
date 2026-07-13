---
layout: default
title: Flecainide
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 10
---

# Flecainide
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

# Flecainide: From Atrial Fibrillation to Stroke Disorder

## One-Sentence Summary

Flecainide is a Class IC antiarrhythmic drug widely used internationally for the treatment of atrial fibrillation (AF), paroxysmal supraventricular tachycardia, and ventricular arrhythmias in patients without structural heart disease.
The TxGNN model predicts it may be effective for **Stroke Disorder**,
with **multiple completed large-scale clinical trials** (including the landmark EAST-AFNET 4 trial, n=2,789) and **20 publications** currently supporting this direction through an AF-mediated stroke prevention pathway.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atrial fibrillation, paroxysmal supraventricular tachycardia (not registered in Singapore; based on international approved use) |
| Predicted New Indication | Stroke Disorder |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flecainide is a Class IC antiarrhythmic agent that works by blocking cardiac voltage-gated sodium channels (Nav1.5), slowing impulse conduction throughout both atrial and ventricular myocardium. This electrophysiological action makes it effective at converting atrial fibrillation (AF) to sinus rhythm and maintaining normal rhythm — a strategy known as "rhythm control." Although detailed MOA data was not returned from the DrugBank query in this pipeline, Flecainide's sodium channel blocking mechanism is extensively documented in the clinical literature and forms the mechanistic backbone of the TxGNN prediction.

The connection between AF and stroke is one of the most robust associations in cardiovascular medicine. AF accounts for approximately 15–20% of all ischemic strokes through a cardioembolic mechanism: chaotic atrial contractions allow blood to pool in the left atrial appendage, promoting thrombus formation that can embolize to cerebral vessels. By restoring and maintaining sinus rhythm, Flecainide indirectly but powerfully reduces this embolic risk. This is an **indirect repurposing pathway**: Flecainide does not target cerebrovascular pathology or coagulation directly, but acts upstream by eliminating the arrhythmia that drives stroke.

The EAST-AFNET 4 trial (NCT01288352, n=2,789, completed) was the pivotal study establishing early rhythm control as a stroke prevention strategy in AF patients. A dedicated sub-analysis (PMID 38702961, *Europace* 2024) specifically examined sodium channel blockers — including Flecainide and propafenone — within EAST-AFNET 4 and confirmed their long-term safety and efficacy for early rhythm control. Additionally, NCT05213104 (*Assessment of Flecainide to Lower the PFO Closure Risk of Atrial Arrhythmia*) represents a Phase 3 trial that directly tests Flecainide in patients with cryptogenic stroke who underwent patent foramen ovale (PFO) closure — a cerebrovascular procedure — making this the most direct linkage between Flecainide and stroke disorder in current evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | Completed | 2,789 | EAST-AFNET 4: Early structured rhythm control (including Flecainide and catheter ablation) vs usual care in AF patients. Rhythm control group showed significant reduction in stroke and cardiovascular death composite endpoint. |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | Completed | 2,204 | CABANA trial: Catheter ablation vs antiarrhythmic drug therapy (Flecainide as one option) for AF. Primary composite endpoint included all-cause mortality and stroke. |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | Not Yet Recruiting | 1,746 | EAST-STROKE trial: Early comprehensive rhythm control therapy (including Flecainide) in patients with **acute ischemic stroke and AF** vs usual care. Directly targets stroke patients with AF. |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | Active, Not Recruiting | 484 | Global multicenter RCT: Pulsed field ablation vs antiarrhythmic drugs (including Flecainide) as first-line treatment for persistent AF. Cerebrovascular/neurological outcomes tracked. |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | Completed | 245 | STOP AF: Cryoablation vs antiarrhythmic drug therapy (Flecainide, propafenone, or sotalol) after drug failure in paroxysmal AF. |
| [NCT02459574](https://clinicaltrials.gov/study/NCT02459574) | N/A | Completed | 321 | Catheter ablation vs antiarrhythmic drugs (including Flecainide) for recurrent AF. Stroke listed as secondary endpoint. Streamlined daycase ablation showed superior reduction in hospital episodes. |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | Active, Not Recruiting | 186 | **Directly tests Flecainide** to lower risk of atrial arrhythmia after PFO closure in cryptogenic stroke patients. PFO closure is a stroke prevention procedure; Flecainide is the sole investigational drug. |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | Unknown | 70 | Direct head-to-head comparison of Vernakalant vs **Flecainide** on atrial contractility after cardioversion. Reduced atrial contractility post-cardioversion is associated with increased stroke risk. |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | Not Yet Recruiting | 100 | SAVE STROKE Phase II: AF ablation vs routine medication (Flecainide rhythm control arm) in patients with **new-onset AF at the time of stroke**. Neurological outcomes are the primary endpoint. |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | Not Yet Recruiting | 988 | RECASTE trial: Flecainide vs standard rhythm-control drugs (sotalol or amiodarone) in patients with AF and **stable coronary artery disease**, directly evaluating Flecainide safety in higher-risk cardiovascular patients. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT Sub-analysis (EAST-AFNET 4) | *Europace* | Long-term sodium channel blocker (SCB) therapy — including **Flecainide** — for early rhythm control in AF is safe and effective. SCB users in EAST-AFNET 4 showed no excess proarrhythmic risk vs non-SCB users and shared the stroke reduction benefit of early rhythm control. |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT (indirect) | *Journal of Clinical Medicine* | Multicenter RCT comparing carvedilol vs **Flecainide** for idiopathic PVCs from ventricular outflow tract. Provides direct pharmacodynamic data on Flecainide's antiarrhythmic efficacy in a randomized setting. |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Review | *Nature Reviews Disease Primers* | Comprehensive primer on AF epidemiology and management. Highlights stroke as the most feared complication of AF (risk ×5 vs general population) and summarises evidence for rhythm control drugs including Flecainide in reducing stroke risk. |
| [25430048](https://pubmed.ncbi.nlm.nih.gov/25430048/) | 2014 | Evidence Synthesis | *BMJ Clinical Evidence* | Systematic evidence synthesis on acute AF management. Establishes Flecainide as a first-line pharmacological cardioversion agent, with stroke risk as a core outcome consideration. |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | Cohort (Pharmacoepidemiology) | *Journal of Atrial Fibrillation* | Real-world US cohort (n=10,455) examining stroke and cardiovascular event risks across antiarrhythmic drugs including Flecainide. Provides comparative stroke outcome data in the clinical setting. |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | Cohort (Multinational) | *BMC Medicine* | Multinational cohort studying concomitant use of DOACs and antiarrhythmic drugs (including Flecainide) in non-valvular AF. Evaluates stroke outcomes and bleeding risk under combined rhythm control and anticoagulation strategies. |
| [30067936](https://pubmed.ncbi.nlm.nih.gov/30067936/) | 2018 | Clinical Practice Guidelines | *Medical Journal of Australia* | Australian national AF guidelines (National Heart Foundation & CSANZ). Positions Flecainide as a first-line rhythm control option in AF without structural heart disease, with stroke prevention as a core management goal. |
| [21718559](https://pubmed.ncbi.nlm.nih.gov/21718559/) | 2011 | Evidence Synthesis | *BMJ Clinical Evidence* | BMJ evidence synthesis on acute AF management. Outlines that acute AF increases stroke and heart failure risk; Flecainide cited for cardioversion in patients without structural heart disease. |
| [39077579](https://pubmed.ncbi.nlm.nih.gov/39077579/) | 2023 | Review | *Reviews in Cardiovascular Medicine* | Management of AF during pregnancy, with Flecainide mentioned as a treatment option. Highlights thromboembolism risk management in a complex clinical scenario. |
| [27884575](https://pubmed.ncbi.nlm.nih.gov/27884575/) | 2017 | Case Report | *The Journal of Emergency Medicine* | Flecainide overdose unmasked a Brugada ECG pattern in an AF patient. Documents the proarrhythmic risk of sodium channel blockade at supratherapeutic levels — key safety signal relevant to monitoring. |

---

## Singapore Market Information

Flecainide is currently **not registered in Singapore**. There are no active Health Sciences Authority (HSA) product authorizations on record. This is a market access gap that would need to be addressed before any clinical deployment in the Singapore setting.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Critical Safety Signal from Evidence Analysis:** Although formal TFDA/HSA package insert data was not available in this pipeline, the clinical trial and literature evidence identifies two important safety boundaries:
> - **Structural Heart Disease Contraindication:** Flecainide is contraindicated in patients with post-myocardial infarction or significant structural heart disease (the CAST trial demonstrated increased mortality in this population). Candidate patients must be carefully screened.
> - **Sick Sinus Syndrome (SSS) Contraindication:** TxGNN rank 3 prediction flagged SSS as a potential indication — however, SSS is a **known contraindication** to Flecainide (Nav1.5 blockade may worsen sinus node conduction and cause bradycardia or sinus arrest). This prediction should not be pursued.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic link between Flecainide (AF rhythm control via Nav1.5 blockade) and stroke prevention (via reduction of AF-mediated cardioembolism) is biologically well-grounded and supported by a completed Phase 4 large-scale RCT (EAST-AFNET 4, n=2,789) along with an ongoing Phase 3 trial directly administering Flecainide in cryptogenic stroke patients post-PFO closure (NCT05213104, n=186). The evidence base justifies advancement to the next evaluation stage, but only within a carefully defined patient population.

**To proceed, the following is needed:**

- **Formal MOA documentation:** Retrieve full DrugBank and TFDA package insert data to document the sodium channel blocking mechanism and complete contraindication profile
- **Patient selection criteria:** Limit repurposing target population to AF patients **without structural heart disease, without sick sinus syndrome, and without bundle branch block** — the safety boundaries from the CAST trial must be encoded as hard exclusion criteria
- **Singapore market access pathway:** Flecainide is not registered in Singapore; a parallel market authorization application or compassionate use pathway would be required before clinical deployment
- **Anticoagulation co-treatment protocol:** The stroke prevention benefit operates in conjunction with appropriate anticoagulation (e.g., DOACs). A combined Flecainide + DOAC protocol document is needed, informed by PMID 41152878 on drug interaction risks
- **QRS monitoring plan:** A cardiac monitoring protocol for QRS widening and proarrhythmia signals must be established prior to any expanded use
- **Clarification on EAST-STROKE trial (NCT05293080):** This Phase 3 trial (n=1,746, starting 2024) is the most direct evidence pending — its results upon completion may elevate this from L2 to L1 evidence, warranting a re-evaluation of the decision stage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

