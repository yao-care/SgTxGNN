---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
---

# Insulin Degludec
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

# Insulin Degludec: From Type 2 Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin degludec (Tresiba®) is an ultra-long-acting second-generation basal insulin analogue approved in the EU, USA, Japan, and multiple other markets for the treatment of diabetes mellitus, though it currently holds **no regulatory registration in Singapore**.
The TxGNN model predicts it is highly effective for **Type 1 Diabetes Mellitus (T1DM)**, a finding reinforced by **multiple completed Phase 3 randomised controlled trials** and **20 publications** directly evaluating degludec in this population.
With a prediction score of **99.44%** and an independently determined evidence level of **L1**, this candidate represents one of the most evidence-rich predictions in the dataset — the primary barrier to clinical use is local regulatory status, not evidence sufficiency.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; approved in other markets for Type 1 and Type 2 diabetes mellitus |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database record for insulin degludec. Based on well-established pharmacological knowledge, insulin degludec is an ultra-long-acting basal insulin analogue engineered through fatty acid side-chain conjugation to human insulin. Following subcutaneous injection, it self-assembles into soluble multi-hexamer complexes that form a stable subcutaneous depot, from which insulin monomers are continuously released into the systemic circulation. This mechanism confers a flat, peakless pharmacodynamic profile with a duration of action exceeding 42 hours and substantially reduced within-patient day-to-day variability compared to first-generation basal insulins such as glargine and detemir.

Type 1 Diabetes Mellitus is characterised by autoimmune destruction of pancreatic β-cells, resulting in absolute endogenous insulin deficiency. Insulin degludec directly addresses this core pathophysiology: after release from the subcutaneous depot, it binds the insulin receptor (IR), activating the PI3K/Akt and MAPK signalling cascades to restore glucose uptake in muscle and adipose tissue while suppressing hepatic gluconeogenesis — precisely mimicking the physiological role of the missing endogenous basal insulin. This is a first-in-class mechanistic match.

The TxGNN prediction score of 99.44% reflects this near-perfect mechanistic alignment. Multiple large Phase 3 and Phase 4 randomised controlled trials have directly enrolled T1DM patients and used degludec either as the investigational drug or as the active comparator benchmark, affirming that the model's prediction is fully consistent with globally established clinical practice. The outstanding question in Singapore is not whether the drug works, but rather how to navigate its absence from the local regulatory register.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | Completed | 692 | Multicenter RCT comparing once-weekly insulin efsitora alfa vs. once-daily degludec in T1DM on MDI therapy; degludec serves as the gold-standard active comparator |
| [NCT02034513](https://clinicaltrials.gov/study/NCT02034513) | Phase 3 | Completed | 501 | SWITCH 1: randomised double-blind crossover trial comparing degludec vs. insulin glargine both combined with insulin aspart in T1DM adults; confirms degludec non-inferiority with hypoglycaemia benefits |
| [NCT03214367](https://clinicaltrials.gov/study/NCT03214367) | Phase 3 | Completed | 1,392 | PRONTO-T1D: large RCT evaluating fast-acting insulin aspart in combination with either degludec or glargine in T1DM; directly validates degludec in basal-bolus regimens |
| [NCT03328845](https://clinicaltrials.gov/study/NCT03328845) | Phase 4 | Completed | 300 | INEOX: 4-year Phase 4 trial comparing oxidative stress parameters across current insulin analogues including degludec in T1DM; robust sample size with long follow-up |
| [NCT02738151](https://clinicaltrials.gov/study/NCT02738151) | Phase 4 | Completed | 929 | 24-week multicentre open-label RCT comparing Toujeo® (glargine U300) vs. Tresiba® (degludec) in insulin-naive T2DM; largest head-to-head post-marketing study demonstrating non-inferiority in HbA1c with comparable hypoglycaemia |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A | Completed | 1,262 | European 3-year non-interventional real-world study of degludec (Tresiba®) safety and effectiveness across both T1DM and T2DM populations |
| [NCT02192450](https://clinicaltrials.gov/study/NCT02192450) | Phase 4 | Completed | 149 | Evaluates whether degludec reduces symptomatic nocturnal hypoglycaemia vs. glargine specifically in T1DM patients with high risk of severe nocturnal events |
| [NCT00841087](https://clinicaltrials.gov/study/NCT00841087) | Phase 2 | Completed | 65 | Japanese Phase 2 exploratory safety study of degludec vs. insulin detemir in a basal-bolus regimen in T1DM; initial hypoglycaemia safety confirmation in the Asian population |
| [NCT00612040](https://clinicaltrials.gov/study/NCT00612040) | Phase 2 | Completed | 178 | Treat-to-target 3-arm trial comparing two degludec formulations vs. glargine with insulin aspart in T1DM; early efficacy and safety confirmation across European, US, and Oceanian sites |
| [NCT03463564](https://clinicaltrials.gov/study/NCT03463564) | Phase 4 | Recruiting | 150 | METRO: insulin pump vs. MDI (incorporating degludec as basal option) in adolescents with T1DM transitioning from paediatric to adult care; ongoing real-world relevance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6: once-weekly icodec vs. once-daily degludec in T1DM basal-bolus therapy; degludec used as benchmark, confirming its well-characterised efficacy and safety profile |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT (Phase 3) | Lancet | QWINT-5: once-weekly efsitora alfa vs. degludec in T1DM; Phase 3 non-inferiority RCT further validating degludec as the current clinical standard for once-daily basal therapy |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT: multinational open-label non-inferiority RCT comparing degludec vs. insulin detemir in pregnant women with T1DM; supports safety and efficacy in high-risk obstetric population |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic Review / Meta-analysis | Clinical Therapeutics | Comprehensive meta-analysis of degludec vs. glargine and detemir in T1DM and T2DM; confirms comparable HbA1c reduction with consistent benefit in nocturnal hypoglycaemia reduction |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Systematic Review | Value in Health | Network meta-analysis of basal insulin regimens in T1DM adults; positions degludec within the treatment landscape for relative efficacy and safety decision-making |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes & Metabolism | Narrative review of degludec in T1DM and T2DM based on RCT and observational data; highlights consistent nocturnal hypoglycaemia reduction and improved fasting plasma glucose control |
| [36106652](https://pubmed.ncbi.nlm.nih.gov/36106652/) | 2023 | Study Design Paper | Diabetes Obes Metab | Rationale and design of the ONWARDS 1–6 clinical programme; degludec is the active comparator across multiple T1DM and T2DM trials, underscoring its role as the current reference standard |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Clinical Review | Lancet Diabetes Endocrinol | Update on T1DM management in pregnancy, including evidence for degludec use; discusses technology integration and pharmacological choices in this specialist population |
| [23890782](https://pubmed.ncbi.nlm.nih.gov/23890782/) | 2014 | Pharmacology Review | Endocrinologia y Nutricion | Foundational review of degludec's ultra-long-acting multi-hexamer mechanism and early Phase 2/3 evidence in both T1DM and T2DM; establishes pharmacological rationale |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Clinical Review | Vascular Health Risk Mgmt | Review of insulin degludec and degludec/aspart co-formulation (IDegAsp) for T1DM and T2DM; discusses achieving glycaemic targets and managing hypoglycaemia risk with combination basal-bolus strategies |

---

## Singapore Market Information

Insulin degludec currently has **no regulatory registrations with the Health Sciences Authority (HSA) of Singapore** (total licences: 0). The drug is commercially available in the European Union, United States, Japan, Korea, India, and numerous other markets under the brand names **Tresiba®** (insulin degludec injection) and **Ryzodeg®** (insulin degludec/insulin aspart co-formulation), both with approved indications for diabetes mellitus in adults and, in several jurisdictions, children and adolescents. Its absence from the Singapore market represents a regulatory gap rather than a clinical evidence gap.

---

## Safety Considerations

Please refer to the package insert (Tresiba® SmPC or USPI) for full safety information, including hypoglycaemia risk, injection site reactions, fluid retention, and weight gain. Key clinical monitoring considerations for insulin therapy (blood glucose, HbA1c, renal function, hypoglycaemia events) should follow standard insulin management protocols.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin degludec for Type 1 Diabetes Mellitus is supported by the highest level of clinical evidence (L1), with multiple completed Phase 3 RCTs and Phase 4 real-world studies confirming its efficacy and safety across both T1DM and T2DM populations globally. The TxGNN prediction score of 99.44% is mechanistically justified: the drug directly replaces the absolute insulin deficiency that defines T1DM. The sole barrier in Singapore is the absence of local HSA registration.

**To proceed, the following is needed:**
- **Regulatory submission**: Initiate HSA registration via the abridged or verification pathway, referencing existing EU EMA approval (Tresiba®) or US FDA approval as the reference dossier
- **Full prescribing information review**: Obtain the complete Summary of Product Characteristics (SmPC) or USPI to document all warnings, contraindications, special populations (pregnancy, paediatrics, renal/hepatic impairment), and drug interactions — this resolves the current data gaps (DG001, DG002)
- **Formulary positioning assessment**: Evaluate clinical differentiation vs. currently available basal insulins in Singapore (glargine U100, glargine U300, insulin detemir) with focus on nocturnal hypoglycaemia reduction and dosing flexibility
- **Cold-chain and device readiness**: Confirm supply chain, pen device availability, and compatible glucose monitoring system integration for the local healthcare setting
- **Local clinical advisory**: Engage the Singapore endocrinology/diabetes specialist community for consensus on patient selection criteria and prescribing guidelines for T1DM management
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

