---
layout: default
title: Enalaprilat
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 10
---

# Enalaprilat
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

# Enalaprilat: From Acute Heart Failure to Acute Pulmonary Heart Disease

## One-Sentence Summary

Enalaprilat is the active intravenous form of enalapril and the only IV-available ACE inhibitor, used in acute care settings to manage hypertensive emergencies and acute decompensated heart failure.
The TxGNN model predicts it may be effective for **Acute Pulmonary Heart Disease** (rank #3, score 98.3%), with **6 clinical trials** and **13 publications** currently supporting this direction — including 1 directly relevant completed Phase 3 trial and 2 RCTs specifically using IV enalaprilat.
Note: while primary hereditary glaucoma ranked #1 in TxGNN predictions (score 99.1%), that indication carries zero clinical or preclinical evidence; acute pulmonary heart disease is the highest-ranked prediction with substantive, actionable evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute decompensated heart failure; hypertensive emergency (intravenous administration) |
| Predicted New Indication | Acute Pulmonary Heart Disease (TxGNN Rank #3) |
| TxGNN Prediction Score | 98.32% |
| Evidence Level | L2 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data is not available in this Evidence Pack. However, Enalaprilat is well-characterised pharmacologically as the active diacid metabolite of enalapril. It inhibits angiotensin-converting enzyme (ACE), blocking the conversion of angiotensin I to the potent vasoconstrictor angiotensin II. The downstream effects are rapid and clinically significant: systemic vascular resistance (afterload) falls, venous capacitance increases (reducing preload), and aldosterone secretion is suppressed, collectively lowering cardiac filling pressures. IV administration produces haemodynamic onset within 15 minutes and effects lasting up to 6 hours — a profile uniquely suited to acute inpatient scenarios where oral therapy is not feasible.

In acute pulmonary heart disease, sudden-onset right ventricular dysfunction is driven by elevated pulmonary vascular resistance and acute volume and pressure overload. This is mechanistically analogous to the acute decompensated heart failure settings where enalaprilat has direct RCT-level evidence (Annane et al., *Circulation* 1996). Importantly, ACE is abundantly expressed on pulmonary capillary endothelium (PCEB-ACE), making the pulmonary vasculature an anatomically specific target for enalaprilat's action — a biological rationale formally characterised in human studies (PMID 11836639). The TxGNN prediction therefore traces a coherent mechanistic chain: IV ACE inhibition → rapid reduction in pulmonary vascular resistance and cardiac afterload → improved right and left ventricular haemodynamics → resolution of acute pulmonary congestion.

The biological overlap between acute pulmonary heart disease and acute cardiogenic pulmonary oedema — both characterised by elevated filling pressures and neurohormonal activation — further supports mechanistic transferability. The S2 decision stage and "Proceed with Guardrails" recommendation reflect this moderate-to-strong mechanistic fit, tempered by the small sample sizes in direct enalaprilat trials and the absence of a large, dedicated trial specifically enrolling acute pulmonary heart disease patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00741156](https://clinicaltrials.gov/study/NCT00741156) | Phase 3 | Completed | 12 | Directly used IV enalaprilat to assess acute effects on systemic, pulmonary, and cerebral blood flow in post-bidirectional cavopulmonary connection patients; the most directly relevant completed Phase 3 RCT for this drug |
| [NCT04591210](https://clinicaltrials.gov/study/NCT04591210) | Phase 3 | Completed | 372 | International RCT of ACEi/ARB in COVID-19 patients to reduce ICU admission, ventilator requirement, and mortality; provides Phase 3 class-level evidence for ACE inhibitors in acute cardiopulmonary disease |
| [NCT04191681](https://clinicaltrials.gov/study/NCT04191681) | Phase 4 | Recruiting | 50 | Sacubitril-valsartan (ARNI) vs. standard oral vasodilator post-LVAD implantation; provides design reference for pulmonary haemodynamic endpoints in device-supported acute heart failure |
| [NCT05487261](https://clinicaltrials.gov/study/NCT05487261) | Phase 4 | Unknown | 260 | Sacubitril-valsartan effect on right heart catheterisation parameters including pulmonary artery pressure in HFrEF with post-capillary pulmonary hypertension; indirect reference for pulmonary vascular endpoint design |
| [NCT03650205](https://clinicaltrials.gov/study/NCT03650205) | N/A | Unknown | 160 | Ivabradine for anthracycline-induced cardiotoxicity; enalapril cited as cardioprotective comparator — background clinical context only |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | Recruiting | 20,000 | REMAP-CAP: large adaptive platform trial in ICU patients with community-acquired pneumonia and COVID-19; broad cardiopulmonary evidence generation platform, indirect relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [8822986](https://pubmed.ncbi.nlm.nih.gov/8822986/) | 1996 | RCT | Circulation | Placebo-controlled double-blind RCT of IV enalaprilat (1 mg, 2-hour infusion) in acute cardiogenic pulmonary oedema; demonstrated significant clinical efficacy with acceptable renal safety profile |
| [10393397](https://pubmed.ncbi.nlm.nih.gov/10393397/) | 1999 | RCT | Cardiology | Bolus vs. continuous low-dose IV enalaprilat (0.004 mg/kg) in 20 CHF patients with acute refractory decompensation; both regimens improved haemodynamics and systemic oxygenation, with dose-optimisation insights |
| [8205829](https://pubmed.ncbi.nlm.nih.gov/8205829/) | 1994 | Prospective Series | Critical Care Medicine | IV enalaprilat infusion in critically ill patients with intractable heart failure post-MI; documented acute haemodynamic improvement in ICU setting |
| [8383028](https://pubmed.ncbi.nlm.nih.gov/8383028/) | 1993 | Prospective Cohort | Clinical Cardiology | IV enalaprilat (1.25 mg) in 20 severe CHF patients with mitral regurgitation; significantly reduced systemic vascular resistance and improved stroke volume within 1 hour |
| [7994817](https://pubmed.ncbi.nlm.nih.gov/7994817/) | 1994 | Clinical Study | Circulation | Characterised angiotensinergic vs. non-angiotensinergic components of IV ACE inhibition haemodynamics in chronic heart failure; mechanistic basis for effect magnitude |
| [11836639](https://pubmed.ncbi.nlm.nih.gov/11836639/) | 2002 | Clinical Study | Int J Mol Med | Assayed pulmonary capillary endothelium-bound ACE (PCEB-ACE) activity in humans; establishes anatomical and biological basis for enalaprilat's pulmonary vascular selectivity |
| [7722147](https://pubmed.ncbi.nlm.nih.gov/7722147/) | 1995 | Clinical Study | JACC | Examined low-dose aspirin interaction with enalaprilat's cardiorenal haemodynamic effects in a canine severe heart failure model; identified relevant drug interaction affecting efficacy |
| [8205828](https://pubmed.ncbi.nlm.nih.gov/8205828/) | 1994 | Clinical Study | Critical Care Medicine | Characterised cardiopulmonary haemodynamic actions of IV enalaprilat in hypertensive trauma patients; extends safety and efficacy data to non-cardiac acute disease populations |
| [9704248](https://pubmed.ncbi.nlm.nih.gov/9704248/) | 1998 | Review | Drug Safety | Comparative tolerability profile of hypertensive crisis treatments; positions IV enalaprilat's safety relative to nitroprusside, labetalol, and other acute antihypertensives |
| [39799613](https://pubmed.ncbi.nlm.nih.gov/39799613/) | 2025 | Review | Am J Emergency Medicine | Current emergency medicine approach to sympathetic crashing acute pulmonary oedema (SCAPE); provides contemporary clinical context where IV vasoactive agents are first-line interventions |

---

## Singapore Market Information

Enalaprilat is not currently registered or marketed in Singapore. No Health Sciences Authority (HSA) product licences are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial (NCT00741156) directly evaluated IV enalaprilat's acute pulmonary and systemic haemodynamic effects, and a placebo-controlled RCT published in *Circulation* (1996) demonstrated efficacy and tolerability of IV enalaprilat in acute cardiogenic pulmonary oedema — a closely related phenotype. The drug's rapid IV onset, established haemodynamic profile, and mechanistic alignment with acute pulmonary-cardiac disease (ACE inhibition reducing afterload and preload) support moving forward, but formal large-scale evidence specifically in acute pulmonary heart disease remains limited.

**To proceed, the following is needed:**
- Obtain and review the official product monograph / package insert to document contraindications and warnings (currently a blocking data gap, DG001)
- Retrieve detailed pharmacokinetic and mechanism of action data from DrugBank (currently a high-severity data gap, DG002)
- Design a prospective pilot study specifically enrolling acute pulmonary heart disease patients with pre-specified pulmonary haemodynamic endpoints (e.g., pulmonary artery pressure, right ventricular stroke work index, and PVR)
- Evaluate Singapore regulatory pathway: Enalaprilat carries no HSA registration; import approval or investigational product authorisation under a clinical trial would be required before clinical use
- Implement mandatory renal function monitoring protocol — Enalaprilat accumulates significantly in chronic renal failure (PMID 11881130), necessitating close surveillance of serum creatinine and potassium in acute settings
- Assess drug interaction risk with concurrent agents common in this population (diuretics: hypotension risk; potassium-sparing diuretics or supplements: hyperkalemia risk)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

