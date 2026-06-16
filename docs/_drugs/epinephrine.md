---
layout: default
title: Epinephrine
parent: 僅模型預測 (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Epinephrine
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

# Epinephrine: From Anaphylaxis & Bronchospasm to Obstructive Lung Disease

## One-Sentence Summary

Epinephrine (adrenaline) is a naturally occurring catecholamine and cornerstone emergency medication, classically used for anaphylaxis, cardiac arrest, and acute severe bronchospasm; it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Obstructive Lung Disease** (particularly acute bronchiolitis in infants),
with **2 Cochrane systematic reviews**, **1 pivotal Phase 3 RCT (n=864)**, and **multiple completed RCTs** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anaphylaxis; acute severe bronchospasm (no Singapore registration on record) |
| Predicted New Indication | Obstructive Lung Disease (Bronchiolitis) |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Epinephrine acts simultaneously on two classes of adrenergic receptors, giving it a dual advantage in managing acute airway obstruction. Stimulation of **β2-adrenergic receptors** on bronchial smooth muscle causes rapid bronchodilation, while activation of **α1-adrenergic receptors** on mucosal blood vessels induces vasoconstriction, reducing submucosal edema and secretion. This combined mechanism directly addresses the two dominant pathophysiological processes — bronchospasm and mucosal swelling — that underlie obstructive lung disease.

In infant bronchiolitis, the most clinically studied obstructive lung disease subtype in this context, the airway is compromised by viral-induced inflammation (typically RSV or parainfluenza), mucus plugging, and mucosal congestion. Unlike selective β2-agonists such as salbutamol, nebulized epinephrine's additional α1 activity targets mucosal congestion specifically, explaining its superior short-term efficacy observed in multiple head-to-head trials. The drug has been used in this setting for several decades, and its therapeutic role is reflected in emergency paediatric protocols internationally.

The TxGNN prediction score of 99.71% is therefore mechanistically well-grounded. Two Cochrane systematic reviews confirm consistent short-term clinical benefit, and a recently completed large Phase 3 RCT (n=864) further validates the therapeutic direction. While epinephrine's effect in bronchiolitis is symptom-directed rather than disease-modifying, its role as an acute first-line intervention is well established and the mechanistic rationale for the TxGNN prediction is clear.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03567473](https://clinicaltrials.gov/study/NCT03567473) | Phase 3 | Completed | 864 | Multicentre Phase 3 RCT: inhaled epinephrine + oral dexamethasone vs. double placebo in infants with bronchiolitis presenting to ED; primary endpoint was hospitalization rate at 7 days — highest-quality pivotal trial for this indication |
| [NCT03614273](https://clinicaltrials.gov/study/NCT03614273) | N/A | Completed | 60 | RCT directly comparing nebulized 3% hypertonic saline vs. nebulized adrenaline in bronchiolitis; also assessed non-responders to initial therapy to guide stepwise management |
| [NCT01834820](https://clinicaltrials.gov/study/NCT01834820) | Phase 4 | Completed | 120 | Pilot RCT of triple therapy (epinephrine + dexamethasone + hypertonic saline) in infant bronchiolitis; measured impact on hospital admission rate |
| [NCT02586961](https://clinicaltrials.gov/study/NCT02586961) | Phase 2/3 | Terminated | 195 | Multicentre RCT: nebulized adrenaline + high-dose oral betamethasone in bronchiolitis at paediatric ED; designed to confirm reduction in hospitalization rate |
| [NCT00622817](https://clinicaltrials.gov/study/NCT00622817) | N/A | Completed | 65 | Double-blind RCT: adrenaline inhalation vs. xylometazoline HCl nasal drops for bronchiolitis; tested hypothesis of equivalent efficacy |
| [NCT01705964](https://clinicaltrials.gov/study/NCT01705964) | Phase 4 | Completed | 49 | RCT: intramuscular epinephrine 1:1000 as adjunct to inhaled β2-agonists in children with severe acute asthma exacerbation in ED |
| [NCT00114478](https://clinicaltrials.gov/study/NCT00114478) | N/A | Unknown | 600 | Head-to-head comparison of epinephrine vs. albuterol for bronchiolitis; one of the largest enrolment trials for this question |
| [NCT01255709](https://clinicaltrials.gov/study/NCT01255709) | Phase 2 | Completed | 24 | Pharmacokinetic crossover study of epinephrine HFA-MDI inhaler (E004) using deuterium-labelled tracer to distinguish exogenous from endogenous epinephrine |
| [NCT01143051](https://clinicaltrials.gov/study/NCT01143051) | Phase 1/2 | Completed | 24 | PK and safety evaluation of inhaled epinephrine HFA aerosol (E004) under augmented dosing in healthy volunteers; supports inhaled route characterisation |
| [NCT01216553](https://clinicaltrials.gov/study/NCT01216553) | Phase 4 | Unknown | 135 | Matched case-control study of home oxygen therapy with nebulized epinephrine (0.1% in bromhexine) or hypertonic saline for outpatient bronchiolitis management |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21678340](https://pubmed.ncbi.nlm.nih.gov/21678340/) | 2011 | Cochrane SR / Meta-analysis | Cochrane Database Syst Rev | Comprehensive systematic review and meta-analysis of epinephrine for acute bronchiolitis; demonstrated short-term improvement in clinical severity scores vs. placebo |
| [14974006](https://pubmed.ncbi.nlm.nih.gov/14974006/) | 2004 | Cochrane SR | Cochrane Database Syst Rev | Earlier Cochrane review confirming modest short-term clinical benefit of epinephrine as bronchodilator in mild-to-moderate bronchiolitis |
| [21486501](https://pubmed.ncbi.nlm.nih.gov/21486501/) | 2011 | Clinical Review | BMJ Clinical Evidence | Evidence-based management overview of bronchiolitis in infants; epinephrine assessed among bronchodilators for hospital and outpatient settings |
| [30488718](https://pubmed.ncbi.nlm.nih.gov/30488718/) | 2019 | Review | Expert Rev Respir Med | Decade-long review of therapeutic strategies for paediatric bronchiolitis; racemic epinephrine, systemic corticosteroids, hypertonic saline, and high-flow oxygen compared |
| [19444115](https://pubmed.ncbi.nlm.nih.gov/19444115/) | 2009 | Review | Curr Opin Pediatrics | Updated review of all epinephrine applications in paediatric emergencies, including bronchiolitis, croup, and anaphylaxis; highlights dosing and route considerations |
| [19135584](https://pubmed.ncbi.nlm.nih.gov/19135584/) | 2009 | Review | Pediatr Clin North Am | Mechanistic and clinical evidence for nebulized adrenaline in acute bronchiolitis and croup; discusses symptom-relief role vs. disease modification |
| [4606289](https://pubmed.ncbi.nlm.nih.gov/4606289/) | 1974 | Clinical Study | Clin Pharmacol Ther | Comparative study of bronchodilator effects of terbutaline vs. epinephrine in patients with obstructive lung disease; early mechanistic evidence |
| [19450362](https://pubmed.ncbi.nlm.nih.gov/19450362/) | 2007 | Clinical Review | BMJ Clinical Evidence | Bronchiolitis evidence review; evaluates epinephrine alongside supportive therapies; discusses limitations of bronchodilator use in outpatient setting |
| [6777857](https://pubmed.ncbi.nlm.nih.gov/6777857/) | 1980 | Cohort Study | Scand J Clin Lab Invest | Elevated plasma noradrenaline in chronic obstructive lung disease patients; inverse correlation with arterial oxygen saturation, supporting catecholamine involvement in disease physiology |
| [30856157](https://pubmed.ncbi.nlm.nih.gov/30856157/) | 2019 | Drug Review | Med Letter Drugs Ther | OTC re-approval of Primatene Mist (epinephrine HFA inhaler) by FDA for mild intermittent asthma bronchospasm; regulatory milestone for inhaled epinephrine formulations |

---

## Singapore Market Information

Epinephrine currently has **no registered products** in Singapore (HSA). There are no licence entries to display. This represents a critical regulatory gap that must be addressed before any structured repurposing programme can proceed.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two Cochrane systematic reviews and a completed Phase 3 multicentre RCT (n=864) together establish L1-level evidence that inhaled/nebulized epinephrine provides meaningful short-term clinical benefit in obstructive lung disease (particularly infant bronchiolitis), with a clear and well-characterized adrenergic mechanism of action. The TxGNN prediction is strongly supported by clinical and mechanistic evidence. However, epinephrine carries no Singapore registration, and complete safety, contraindication, and drug interaction data for the local regulatory context has not been assembled.

**To proceed, the following is needed:**
- HSA registration pathway assessment for epinephrine nebulizer solution and/or HFA-MDI inhaler formulations
- Full safety profile documentation: retrieve TFDA, EMA, and FDA-approved package inserts to extract warnings, contraindications, and monitoring requirements
- Drug-drug interaction data (DrugBank API query; particular attention to MAO inhibitors, β-blockers, tricyclic antidepressants, and halogenated anaesthetics)
- Formal target population definition: acute infant bronchiolitis vs. broader obstructive lung disease spectrum
- Safety monitoring plan for high-risk subgroups (premature neonates, infants with congenital heart disease, patients with arrhythmia risk)
- Formulation strategy: determine whether existing international nebulizer solutions or the newly re-approved HFA-MDI (Primatene Mist) format is appropriate for the Singapore context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

