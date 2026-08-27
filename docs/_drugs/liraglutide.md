---
layout: default
title: Liraglutide
parent: 僅模型預測 (L5)
nav_order: 599
evidence_level: L5
indication_count: 10
---

# Liraglutide
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

# Liraglutide: From Type 2 Diabetes to Type 1 Diabetes Mellitus

## One-Sentence Summary

Liraglutide is a long-acting GLP-1 receptor agonist approved globally for Type 2 Diabetes Mellitus and obesity management (marketed as Victoza® and Saxenda®), though not currently registered in Singapore.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus** as an adjunct to insulin therapy,
with **50 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 Diabetes Mellitus / Obesity (global approvals; not registered in Singapore per HSA registry) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 92.27% |
| Evidence Level | L1 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Liraglutide is a GLP-1 receptor agonist that mimics endogenous GLP-1, stimulating glucose-dependent insulin secretion, suppressing post-meal glucagon release, delaying gastric emptying, and reducing appetite through central nervous system pathways. Although its primary global approval targets Type 2 Diabetes (where some residual β-cell function remains) and obesity, its mechanisms extend meaningfully into the biology of Type 1 Diabetes. Detailed MOA data from the Singapore HSA package insert is not yet available; the following is drawn from published clinical pharmacology.

In Type 1 Diabetes, patients depend entirely on exogenous insulin due to autoimmune β-cell destruction. Liraglutide offers multiple complementary benefits in this setting: (1) preserving residual β-cell function and prolonging the honeymoon period in newly diagnosed patients (PMID 39192527, NewLira RCT); (2) glucose-dependently suppressing glucagon, blunting post-prandial spikes and reducing bolus insulin requirements; (3) delaying gastric emptying to flatten post-meal glucose excursions; (4) promoting weight loss and lowering insulin resistance, which is increasingly relevant as overweight/obesity rates rise among T1DM patients; and (5) providing cardiovascular protection through mechanisms consistent with the landmark LEADER trial.

The Phase 3 ADJUNCT ONE and ADJUNCT TWO trials (combined enrollment > 1,600 patients) directly established that liraglutide added to treat-to-target insulin reduces HbA1c and body weight in T1DM. However, both trials revealed a 3-fold increase in diabetic ketoacidosis (DKA) risk — the primary reason FDA declined to approve liraglutide for T1DM. This critical safety constraint does not negate the clinical signal, but mandates stringent DKA risk mitigation as a non-negotiable guardrail before any use in this population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02098395](https://clinicaltrials.gov/study/NCT02098395) | Phase 3 | Completed | 835 | ADJUNCT TWO: Multinational, multi-centre, placebo-controlled RCT evaluating liraglutide as insulin adjunct in T1DM across Africa, Europe and North America; demonstrated HbA1c reduction and weight loss alongside elevated DKA risk — the pivotal T1DM trial |
| [NCT05467514](https://clinicaltrials.gov/study/NCT05467514) | Phase 3 | Completed | 35 | Liraglutide 1.8 mg add-on to insulin over 6 months reduced carotid intima-media thickness and cardiovascular risk factors in T1DM patients; supports cardiovascular benefit as secondary endpoint |
| [NCT02473809](https://clinicaltrials.gov/study/NCT02473809) | Phase 4 | Completed | 60 | Directly evaluated liraglutide's effect on bone mass and bone cell function in T1DM (T1DM patients carry elevated fracture risk); addresses a clinically important safety and benefit dimension |
| [NCT01612468](https://clinicaltrials.gov/study/NCT01612468) | Phase 4 | Completed | 100 | Randomised double-blind placebo-controlled trial of liraglutide as add-on to insulin in poorly regulated T1DM; assessed HbA1c, body weight, and hypoglycaemia over 3 years |
| [NCT02518945](https://clinicaltrials.gov/study/NCT02518945) | Phase 3 | Completed | 26 | Examined additive effects of dapagliflozin + liraglutide in T1DM; demonstrated improved glycemic control, reduced glycemic variability, and lower insulin doses |
| [NCT02516657](https://clinicaltrials.gov/study/NCT02516657) | Phase 3 | Completed | 5 | Liraglutide effect on post-meal blood glucose, glucagon levels, mean weekly sugars, and insulin doses in adolescents with T1DM; paediatric safety signal data |
| [NCT01592279](https://clinicaltrials.gov/study/NCT01592279) | Phase 4 | Unknown | 124 | GLP-1 analogue in uncontrolled T1DM; evaluated low hypoglycaemia risk, glucagon inhibition, weight loss, and cardiovascular profile as advantages over sulfonylureas |
| [NCT06408532](https://clinicaltrials.gov/study/NCT06408532) | Phase 4 | Not Yet Recruiting | 256 | IDegLira (insulin degludec/liraglutide fixed combination) vs premixed insulin in patients failing prior therapy; reflects current real-world trajectory toward fixed-ratio liraglutide combinations |
| [NCT06387199](https://clinicaltrials.gov/study/NCT06387199) | Phase 2/3 | Recruiting | 26 | Semaglutide (same GLP-1RA class) in T1DM patients on closed-loop insulin therapy; aims to reduce carbohydrate counting burden — supports class-level T1DM applicability |
| [NCT06976619](https://clinicaltrials.gov/study/NCT06976619) | Phase 2 | Recruiting | 60 | Mechanistic study of GLP-1 receptor agonism on islet GLP-1 regulation in people with early T2DM and T1DM; provides insights into islet paracrine biology underlying GLP-1RA benefits |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27506222](https://pubmed.ncbi.nlm.nih.gov/27506222/) | 2016 | RCT | Diabetes Care | ADJUNCT ONE: Liraglutide added to treat-to-target insulin improved glycaemic control, reduced insulin requirements and body weight in T1DM; established foundational Phase 3 efficacy data |
| [33662334](https://pubmed.ncbi.nlm.nih.gov/33662334/) | 2021 | RCT | Lancet Diabetes & Endocrinology | Phase 2 double-blind RCT: anti-IL-21 antibody + liraglutide combination for β-cell preservation in recent-onset T1DM; novel immunomodulation + GLP-1RA approach |
| [39192527](https://pubmed.ncbi.nlm.nih.gov/39192527/) | 2024 | RCT | Diabetes, Obesity & Metabolism | NewLira study: liraglutide enhanced insulin secretion and prolonged the remission (honeymoon) period in newly diagnosed T1DM adults — direct evidence for β-cell preservation |
| [31203802](https://pubmed.ncbi.nlm.nih.gov/31203802/) | 2020 | Systematic Review / Meta-analysis | Current Diabetes Reviews | Pooled meta-analysis of all available RCTs on liraglutide as insulin adjunct in T1DM; provided precise effect estimates on HbA1c, weight, insulin dose, and hypoglycaemia |
| [37561012](https://pubmed.ncbi.nlm.nih.gov/37561012/) | 2023 | Review / Meta-analysis | J Clinical Endocrinology & Metabolism | Updated systematic review of GLP-1 analogues as adjunctive therapy in T1DM; highlighted obesity management gap and benefit-risk framework |
| [31612934](https://pubmed.ncbi.nlm.nih.gov/31612934/) | 2019 | Review | Am J Health-System Pharmacy | Comprehensive review of GLP-1 RA efficacy and safety evidence in T1DM; summarises clinical pharmacology rationale |
| [28304146](https://pubmed.ncbi.nlm.nih.gov/28304146/) | 2017 | Mechanistic Clinical Study | Diabetes, Obesity & Metabolism | Liraglutide acutely suppressed glucagon, lipolysis, and ketogenesis in T1DM — key mechanistic data explaining why DKA risk may be lower than with SGLT2 inhibitors |
| [34463425](https://pubmed.ncbi.nlm.nih.gov/34463425/) | 2021 | Post-hoc Analysis | Diabetes, Obesity & Metabolism | ADJUNCT ONE/TWO subgroup analysis: efficacy and safety of liraglutide in T1DM stratified by baseline HbA1c, BMI, and disease duration — guides patient selection |
| [26926662](https://pubmed.ncbi.nlm.nih.gov/26926662/) | 2016 | Review | Expert Opinion on Biological Therapy | Detailed review of liraglutide mechanism of action, efficacy, and safety as insulin add-on in T1DM; discusses glucose-dependent glucagon suppression and cardiovascular pleiotropic effects |
| [39717993](https://pubmed.ncbi.nlm.nih.gov/39717993/) | 2025 | Post-hoc Analysis | J Diabetes Science & Technology | Post-hoc of ADJUNCT ONE/TWO: identifies determinants of liraglutide treatment discontinuation in T1DM (mainly GI adverse effects); informs real-world adherence strategy |

---

## Singapore Market Information

No product licenses for liraglutide were found in the Singapore HSA registry at the time of this assessment (data cutoff: 2026-06-22).

> Liraglutide (Victoza® for T2DM, Saxenda® for obesity) is approved in the US, EU, Japan, and numerous other markets. If liraglutide is to be used in Singapore for any T1DM indication — whether under a clinical trial, compassionate use, or off-label framework — formal institutional review and HSA notification would be required given the absence of local registration.

---

## Safety Considerations

Package insert warnings and contraindications from the Singapore HSA are not available (data gap). Based on published evidence from the ADJUNCT clinical trial programme:

- **Diabetic Ketoacidosis (DKA)**: A 3-fold increase in DKA risk was observed in both ADJUNCT ONE and ADJUNCT TWO trials in T1DM patients. This was the primary basis for FDA's rejection of the T1DM indication. DKA occurred even in the absence of dramatic insulin dose reductions, suggesting a metabolic shift mechanism requiring active monitoring.
- **Insulin dose management**: Liraglutide reduces insulin requirements; inappropriate dose reductions may precipitate DKA before hyperglycaemia is evident ("euglycaemic DKA" risk).

Please refer to the current Victoza® / Saxenda® international package inserts and consult Novo Nordisk's Singapore medical affairs for full local safety information before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two large Phase 3 multinational RCTs (ADJUNCT ONE and ADJUNCT TWO, combined n > 1,600) provide L1 evidence that liraglutide as insulin adjunct improves HbA1c and body weight in T1DM, and the mechanistic basis — glucagon suppression, β-cell preservation, cardiovascular protection — is well-characterised across multiple RCTs and mechanistic studies. The evidence is sufficient to justify a structured programme, but the confirmed 3-fold DKA risk elevation makes this a conditional recommendation: proceed only with robust safety infrastructure in place.

**To proceed, the following is needed:**
- **DKA risk mitigation protocol**: Mandatory blood ketone monitoring thresholds (e.g., daily fasting ketone checks during dose titration), patient education on early DKA warning signs, and pre-defined insulin dose reduction guardrails
- **Patient selection criteria**: Focus on overweight/obese T1DM patients with elevated cardiovascular risk and suboptimal glycaemic control on insulin alone — the subgroup most likely to benefit per ADJUNCT subgroup analyses (PMID 34463425)
- **Regulatory and institutional pathway**: Since liraglutide is not HSA-registered in Singapore, any clinical use requires institutional ethics review, off-label informed consent, or a formal compassionate use / named-patient programme
- **Local safety data**: Obtain current Victoza®/Saxenda® Singapore-relevant safety documentation from Novo Nordisk; verify no local contraindications exist beyond the global label
- **Real-world monitoring plan**: Establish a structured ketone monitoring and adverse event reporting workflow integrated with the prescribing system before any clinical rollout
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

