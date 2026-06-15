---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 402
evidence_level: L5
indication_count: 10
---

# Ivabradine
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

# Ivabradine: From Chronic Heart Failure to Pulmonary Hypertension

## One-Sentence Summary

Ivabradine is a selective HCN4 channel inhibitor originally indicated for chronic heart failure with reduced ejection fraction and stable angina, reducing heart rate through sinoatrial If current blockade without suppressing cardiac contractility.
Among the TxGNN model's top 10 predictions, **Pulmonary Hypertension** (rank 7, score 98.50%) stands out as the most clinically relevant candidate, supported by **3 clinical trial registrations** and **20 publications** — including direct animal and clinical observational evidence for right ventricular function improvement.
Notably, the top 6 TxGNN computational predictions (ranks 1–6, largely hair and dental malformation syndromes) are assessed as mechanistic false positives due to absent pathophysiological links to the If channel; the pulmonary hypertension signal is the most actionable finding in this evidence pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic heart failure with reduced ejection fraction (HFrEF); stable angina |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 98.50% (Rank 7 of 17,080 diseases) |
| Evidence Level | L3 |
| Singapore Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ivabradine selectively inhibits the If ("funny current") channel — encoded by the HCN4 subunit — in the sinoatrial node. This reduces spontaneous pacemaker depolarisation, lowering heart rate in a dose-dependent manner without any negative inotropic effect. Unlike beta-blockers, ivabradine does not reduce cardiac contractility or blood pressure, making it theoretically attractive in conditions where heart rate reduction is beneficial but further haemodynamic depression must be avoided.

In pulmonary hypertension (PH), the right ventricle faces chronically elevated afterload from increased pulmonary vascular resistance. The compensatory tachycardia that develops shortens diastolic filling time and amplifies right ventricular oxygen demand, creating a vicious cycle of worsening right heart function. Ivabradine's selective heart rate reduction would theoretically restore diastolic filling time, reduce right ventricular wall tension and myocardial oxygen demand, and slow the progression of right ventricular remodelling — without the cardiac output penalties that make beta-blockers poorly tolerated in advanced PH.

Two independent rat model studies (monocrotaline-induced PH and SU5416/hypoxia-induced PH) confirm that ivabradine reduces right ventricular fibrosis and improves biventricular function, with mechanistic evidence pointing to downregulation of the TGF-β/Smad fibrotic pathway. Multiple small clinical studies and case series in humans — including patients with systemic sclerosis–associated PAH and COPD-associated pulmonary hypertension — report functional improvements with ivabradine therapy. The presence of HCN channel expression in pulmonary vascular smooth muscle cells further raises the hypothesis of direct vasodilatory effects, though this remains unconfirmed in humans.

---

## Clinical Trial Evidence

Two of the three identified trials directly involve ivabradine; the third (NCT04735354, studying sacubitril/valsartan in HFrEF) provides only indirect background context and is excluded below.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03650205](https://clinicaltrials.gov/study/NCT03650205) | N/A | Unknown | 160 | Ivabradine to prevent anthracycline-induced cardiotoxicity — assesses cardiac-protective effects via If channel inhibition; provides indirect safety and cardioprotection data for ivabradine under cardiac stress conditions |
| [NCT00757055](https://clinicaltrials.gov/study/NCT00757055) | Phase 2 | Withdrawn | 0 | Ivabradine in diastolic heart failure — withdrawn before enrolment (reason unknown); the stated rationale addresses heart rate reduction to improve impaired ventricular filling, mechanistically overlapping with the right heart failure pathophysiology seen in PH |

> **Evidence gap:** No dedicated clinical trial targeting ivabradine specifically for pulmonary hypertension has been registered on ClinicalTrials.gov or ICTRP. This is a critical gap for advancing this repurposing candidate.

---

## Literature Evidence

The following 10 publications are most directly relevant to ivabradine and pulmonary hypertension, prioritised by study type and direct drug–disease relevance:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [37742537](https://pubmed.ncbi.nlm.nih.gov/37742537/) | 2023 | Clinical Observational | Am J Cardiology | Prospective study (n not stated); ivabradine selectively lowers heart rate and significantly improves right ventricular systolic function in COPD patients with cor pulmonale and PH |
| [24556029](https://pubmed.ncbi.nlm.nih.gov/24556029/) | 2014 | Case Series | J Cardiac Failure | Functional improvements (6MWT, NYHA class) reported in PAH patients treated with ivabradine; early proof-of-concept signal in humans |
| [32915674](https://pubmed.ncbi.nlm.nih.gov/32915674/) | 2020 | Animal Study | Am J Resp Cell Mol Biol | Ivabradine (10 mg/kg/d) reduces RV fibrosis and improves RV function in MCT and SUHX rat PH models; anti-fibrotic mechanism via TGF-β/Smad pathway confirmed |
| [29146614](https://pubmed.ncbi.nlm.nih.gov/29146614/) | 2018 | Animal Study | Am J Physiol Heart Circ | HR reduction with ivabradine (vs carvedilol) improves biventricular mechanics, cardiac cycle timing, and interventricular interactions in monocrotaline-PAH rats |
| [22792738](https://pubmed.ncbi.nlm.nih.gov/22792738/) | 2012 | Small Clinical Study | Kardiologiia | Ivabradine (10 mg/day, 2 weeks) produces statistically significant reduction in pulmonary hypertension severity in COPD patients (n=60, controlled) |
| [23021874](https://pubmed.ncbi.nlm.nih.gov/23021874/) | 2012 | Case Series | Eur J Int Med | Ivabradine in systemic sclerosis–related PAH — reports clinical improvement in this high-risk subgroup |
| [22383181](https://pubmed.ncbi.nlm.nih.gov/22383181/) | 2012 | Case Series | Clin Res Cardiol | Ivabradine safe and well-tolerated in systemic sclerosis patients with PH; supports the feasibility of use alongside PH-specific therapies |
| [23389056](https://pubmed.ncbi.nlm.nih.gov/23389056/) | 2013 | Case Series | Clin Res Cardiol | Ivabradine in PAH — preliminary data suggesting potential to delay escalation to parenteral prostanoid therapy |
| [28701278](https://pubmed.ncbi.nlm.nih.gov/28701278/) | 2017 | Review | Eur J Int Med | Narrative review covering ACEi, ARB, beta-blockers, and ivabradine as supportive therapies in PH; discusses drug safety, tolerability, and interaction considerations |
| [32248556](https://pubmed.ncbi.nlm.nih.gov/32248556/) | 2020 | Scoping Review | Pharmacotherapy | Systematic scoping review of novel ivabradine uses beyond approved indications; pulmonary hypertension identified as one of the most evidence-supported off-label applications |

---

## Singapore Market Information

Ivabradine is currently **not registered** in Singapore. The HSA product license database returns zero registrations for this drug. There are no approved brand-name products, dosage forms, or indication-specific approvals on record.

This means any clinical use of ivabradine in Singapore would require special access (e.g., Special Access Route / Investigational New Drug pathway) and there is no locally available reference product or approved label to draw upon for safety benchmarking.

---

## Safety Considerations

Formal Singapore HSA package insert data are not available (drug is unregistered). Based on the international clinical literature present in this evidence pack and known pharmacology:

- **Key mechanism-based risk:** Dose-dependent bradycardia — the primary adverse effect; risk is amplified in patients with baseline low heart rate or those on concomitant rate-lowering agents
- **Visual disturbances:** Transient luminous phenomena (phosphenes) due to HCN1 channel expression in retinal photoreceptors; generally mild and reversible
- **CYP3A4 interactions:** Ivabradine is metabolised by CYP3A4; concomitant use with potent inhibitors (e.g., azole antifungals, macrolides) markedly increases plasma levels and bradycardia risk
- **Atrial fibrillation risk:** Noted in the SHIFT trial; ivabradine should be used with caution in patients at risk of AF
- **Contraindicated in:** Resting heart rate <60 bpm, severe hepatic impairment, sick sinus syndrome, sinoatrial block, and use with strong CYP3A4 inhibitors

For the specific PH patient population, drug interactions with ERA (endothelin receptor antagonists), PDE5 inhibitors, and prostanoids — the standard of care in PAH — require formal review before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic basis for ivabradine in pulmonary hypertension is well-grounded: selective heart rate reduction without negative inotropy addresses a key pathophysiological driver of right ventricular deterioration in PH. This rationale is reinforced by convergent evidence from two independent animal models and multiple small clinical studies, establishing ivabradine as a scientifically credible repurposing candidate at the observational/hypothesis-generating stage (L3). The absence of a completed Phase 2/3 RCT is the key evidence gap preventing a "Go" determination.

**To proceed, the following is needed:**

- **Regulatory:** Assess Singapore HSA Special Access Route eligibility; obtain international reference label (EMA/FDA) for full contraindication and safety profiling
- **Safety review:** Formal drug interaction assessment with standard PAH therapies (endothelin antagonists, PDE5 inhibitors, prostanoids)
- **MOA documentation:** Retrieve and document full HCN4 pharmacology from DrugBank (DG002 remediation) to support mechanistic narrative in any future IND submission
- **Clinical trial design:** Design a prospective RCT — recommended target population: PAH (Group 1) or COPD-associated PH (Group 3) with baseline HR ≥75 bpm; primary endpoint: right ventricular function (echocardiographic) or 6-minute walk distance
- **Local KOL consultation:** Engage Singapore pulmonary hypertension specialists to assess feasibility and patient availability for an investigator-initiated trial
- **Heart rate phenotyping:** Identify the PH patient subgroup most likely to benefit (tachycardic patients at rest, inadequately controlled with existing therapies)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

