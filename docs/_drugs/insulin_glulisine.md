---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
---

# Insulin Glulisine
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

# Insulin Glulisine: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin glulisine (Apidra) is a rapid-acting human insulin analogue approved globally for prandial glycaemic control in patients with diabetes mellitus; it is not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus (T1DM)** — importantly, this constitutes a **validation prediction** that confirms the drug's primary established indication worldwide rather than identifying a genuinely novel repurposing opportunity.
With **50 clinical trials** and **19 publications** identified, the evidence base is exceptionally robust at **Evidence Level L1**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; globally approved for diabetes mellitus (prandial glycaemic control) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack's structured fields. Based on well-established pharmacological knowledge, insulin glulisine is a rapid-acting human insulin analogue (brand name: Apidra, Sanofi). It incorporates two amino acid substitutions in the B chain — asparagine at position B3 is replaced by lysine, and lysine at position B29 is replaced by glutamic acid — which reduces insulin self-association and accelerates subcutaneous absorption compared to regular human insulin, producing an onset of action within approximately 15 minutes and a duration of approximately 4 hours.

Type 1 Diabetes Mellitus is characterised by autoimmune destruction of pancreatic β-cells, resulting in absolute insulin deficiency. External insulin replacement is the cornerstone of T1DM management. Insulin glulisine's rapid onset and short duration of action precisely mimic physiological prandial insulin secretion, making it biologically ideal for managing postprandial glycaemic excursions in T1DM patients across all age groups, including paediatric populations.

A critical contextual note: TxGNN's top-ranked prediction for insulin glulisine is T1DM — **its primary globally approved indication**. This TxGNN result represents model validation rather than drug repurposing. The practical implication for Singapore is that a well-evidenced, internationally established therapy currently lacks local registration, representing a potential access gap for T1DM patients who require rapid-acting prandial insulin coverage.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | Completed | 68 | Multicentre study directly evaluating efficacy and safety of insulin glulisine in T1DM patients also using insulin glargine as basal; assessed HbA1c change, insulin dosing, and patient satisfaction |
| [NCT03328845](https://clinicaltrials.gov/study/NCT03328845) | Phase 4 | Completed | 300 | Compared the influence of different rapid-acting insulin analogues (including glulisine) on oxidative stress parameters in T1DM patients; high relevance, large sample, completed |
| [NCT01204593](https://clinicaltrials.gov/study/NCT01204593) | Phase 4 | Completed | 206 | Multinational non-comparative study of glargine once-daily + glulisine three times-daily in T1DM patients previously uncontrolled on any insulin regimen; primary endpoint HbA1c change at week 24 |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | Completed | 142 | Multicentre, non-randomised Phase 3 evaluating efficacy (HbA1c change) and safety of insulin glulisine in T1DM over 26 weeks; insulin glargine used as basal component |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | Completed | 59 | Multinational randomised controlled trial comparing safety of insulin glulisine vs insulin aspart in continuous subcutaneous insulin infusion (CSII) in T1DM; assessed catheter occlusions, HbA1c, and hypoglycaemia rates |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | Completed | 485 | Randomised, parallel-group study comparing efficacy and safety of insulin glulisine to insulin lispro in T1DM and T2DM patients using insulin glargine as basal; 12-week HbA1c primary endpoint |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | Completed | 319 | Open-label randomised trial comparing inhaled insulin Afrezza vs rapid-acting insulin analogues (including glulisine) combined with basal insulin in paediatric T1DM and T2DM over 26 weeks |
| [NCT00174668](https://clinicaltrials.gov/study/NCT00174668) | Phase 3 | Completed | 311 | Multinational open randomised trial demonstrating superior efficacy of an intensified insulin glulisine + glargine regimen over a conventional two-injection regimen in poorly controlled diabetes |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Phase 3 | Completed | 26 | Randomised double-blind placebo-controlled study of dapagliflozin as adjunct to liraglutide and insulin (including rapid-acting) in T1DM; examined glycaemic control, variability reduction, and weight outcomes |
| [NCT04124302](https://clinicaltrials.gov/study/NCT04124302) | Phase 4 | Completed | 76 | Compared two insulin dose calculation approaches on postprandial glycaemia after mixed meals in children with T1DM; relevant to rapid-acting insulin optimisation in paediatric T1DM |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative RCT | Acta Diabetologica | Described T1DM population using glulisine vs lispro/aspart for CSII therapy; evaluated relative effectiveness on HbA1c, fasting glucose, dose requirements, and rates of hypoglycaemia and diabetic ketoacidosis |
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Hormone and Metabolic Research | Multinational, multicentre, randomised, parallel-group trial (n=683) comparing glulisine to lispro in adult T1DM; demonstrated comparable glycaemic efficacy and a similar safety profile |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | Clinical Study | Pediatrics International | Evaluated efficacy and safety of insulin glulisine for CSII in 20 children with T1DM over 1 year; showed significant improvement in postprandial glucose after breakfast and dinner, with no increase in hypoglycaemic events |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Systematic Review | Drugs | Comprehensive systematic review of insulin glulisine for glycaemic management in adults, adolescents, and children; concluded it is effective and broadly comparable to other rapid-acting analogues with a favourable tolerability profile |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | PK/PD Study | Clinical Pharmacokinetics | Detailed pharmacokinetic and pharmacodynamic characterisation of insulin glulisine; documented faster absorption, earlier peak, and shorter duration of action compared to regular human insulin |
| [19216625](https://pubmed.ncbi.nlm.nih.gov/19216625/) | 2009 | Review | Expert Opinion on Biological Therapy | Reviewed optimisation of basal/bolus therapy using insulin glulisine; discussed its role in physiologically mirroring prandial insulin secretion and implications for early insulin initiation strategies |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Review | Drugs of Today | Reviewed rapid-acting insulin analogues (including glulisine) in T1DM children and adolescents; compared pharmacokinetic profiles, clinical outcomes, and approval status across paediatric age groups |
| [17703632](https://pubmed.ncbi.nlm.nih.gov/17703632/) | 2007 | Review | Vascular Health and Risk Management | Reviewed strategies for combining insulins including glulisine for optimal glycaemic control in T1DM and T2DM; discussed pharmacokinetic limitations of conventional insulins and the advantages of rapid-acting analogues |
| [16193096](https://pubmed.ncbi.nlm.nih.gov/16193096/) | 2005 | Drug Review | Drugs of Today | Early drug profile of insulin glulisine; characterised its rapid-action pharmacokinetic profile, pre- and post-meal dosing flexibility, and potential advantages over conventional insulin therapy in clinical diabetes management |
| [35650058](https://pubmed.ncbi.nlm.nih.gov/35650058/) | 2022 | Case Report | Japanese Journal of Geriatrics | Case of an 82-year-old T1DM patient with chronic heart failure: switching from insulin degludec to glulisine improved nocturnal hypoglycaemia and ventricular arrhythmia; illustrates the importance of insulin selection in complex comorbid T1DM |

---

## Singapore Market Information

Insulin glulisine is currently **not registered** in Singapore. There are no active or historical product licences on record with the Health Sciences Authority (HSA).

Globally, insulin glulisine is marketed under the brand name **Apidra** (Sanofi-Aventis) and holds regulatory approvals from major agencies, including:
- **US FDA** (approved 2004) — for improvement of glycaemic control in adults with T1DM and T2DM
- **European Medicines Agency (EMA)** — approved for adults, adolescents, and children ≥6 years with T1DM or T2DM
- **Health Canada** and multiple other national regulators

There is no Singapore-equivalent product licence to tabulate at this time.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
This TxGNN result validates insulin glulisine's primary globally approved indication (T1DM) at Evidence Level L1, supported by multiple completed Phase 3 and Phase 4 randomised trials; however, the drug is entirely absent from the Singapore market, creating a potential access gap for T1DM patients who require rapid-acting prandial insulin analogues.

**To proceed, the following is needed:**
- Initiate or verify an HSA registration pathway for Singapore; assess whether a reference product dossier (US FDA/EMA approval) can be leveraged for expedited review
- Obtain and review the full prescribing information (package insert) to document official warnings, contraindications, and drug-drug interactions for local labelling
- Confirm cold-chain supply logistics, storage infrastructure, and distributor agreements for insulin products in Singapore
- Review the Ministry of Health (MOH) Singapore clinical practice guidelines for T1DM to confirm that insulin glulisine aligns with current national standards of care
- Develop a pharmacovigilance and post-market safety monitoring plan, with particular attention to hypoglycaemia risk in local patient populations
- Explore health technology assessment (HTA) requirements, including cost-effectiveness data relative to alternative rapid-acting insulins already registered in Singapore (e.g., insulin aspart, insulin lispro)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

