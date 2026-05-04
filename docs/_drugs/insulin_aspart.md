---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 10
---

# Insulin Aspart
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

# Insulin Aspart: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin aspart (NovoLog®/NovoRapid®) is a rapid-acting human insulin analogue established globally for the management of blood glucose in patients with diabetes mellitus, though it is currently unregistered in Singapore.
The TxGNN model predicts it may be effective for **Type 1 Diabetes Mellitus (T1DM)**, with **50 clinical trials** and **20 publications** currently supporting this direction — reflecting one of the most evidence-rich therapeutic relationships in diabetes pharmacology.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore (no approved indication on record) |
| Predicted New Indication | Type 1 Diabetes Mellitus |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L1 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Insulin aspart is a rapid-acting human insulin analogue produced by substituting the amino acid proline at position B28 with aspartic acid (B28 Pro→Asp). This single structural modification reduces the tendency for insulin molecules to self-aggregate into hexamers, enabling faster subcutaneous absorption compared with regular human insulin. After injection, insulin aspart begins acting within 10–20 minutes, reaches peak plasma concentration at approximately 60 minutes, and more closely mirrors the physiological postprandial insulin secretion pattern seen in healthy individuals — a profile particularly well-suited for mealtime bolus dosing.

In Type 1 Diabetes Mellitus, autoimmune destruction of pancreatic β-cells results in the complete and permanent loss of endogenous insulin secretion. Insulin replacement is therefore not merely beneficial — it is life-sustaining. Insulin aspart's pharmacokinetic profile makes it ideally suited for both multiple daily injection (MDI) regimens and continuous subcutaneous insulin infusion (CSII) via insulin pump, directly addressing the postprandial hyperglycaemia that characterises T1DM and contributes to long-term microvascular and macrovascular complications.

It is important to note that from a global regulatory perspective, T1DM represents the primary established indication for insulin aspart rather than a novel repurposing target. The significance of this evaluation for Singapore lies in the fact that insulin aspart currently holds no product registration with the Health Sciences Authority (HSA). The TxGNN model's near-perfect prediction score, supported by L1-level clinical evidence, strongly supports initiating a regulatory market access pathway for Singapore.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00773279](https://clinicaltrials.gov/study/NCT00773279) | Phase 3 | Completed | 242 | Multicentre randomised crossover study comparing a new disposable pen (PDS290/FlexTouch®) vs FlexPen® for delivery of insulin detemir and insulin aspart in T1DM and T2DM; assessed glycaemic control, safety, and patient preference |
| [NCT00071448](https://clinicaltrials.gov/study/NCT00071448) | Phase 3 | Completed | 378 | Basal/bolus therapy with insulin aspart vs regular human insulin or insulin lispro + NPH in US paediatric T1DM patients; established efficacy and safety in children and adolescents |
| [NCT00095446](https://clinicaltrials.gov/study/NCT00095446) | Phase 4 | Completed | 513 | Large open-label study of insulin aspart vs insulin lispro in insulin pumps (CSII) under standard US clinical practice; evaluated postprandial control, safety, and patient acceptance |
| [NCT01278160](https://clinicaltrials.gov/study/NCT01278160) | Phase 4 | Completed | 179 | Extension trial comparing biphasic insulin aspart 30 twice daily with two different dosage-split regimens in Chinese T2DM patients not at HbA1c target (<7%) |
| [NCT00467649](https://clinicaltrials.gov/study/NCT00467649) | Phase 4 | Completed | 112 | Randomised open-label parallel-group study characterising basal insulin regimens intensified with either Symlin® or rapid-acting insulin aspart in insulin-naive or early-insulin T2DM |
| [NCT03977727](https://clinicaltrials.gov/study/NCT03977727) | Phase 3 | Completed | 40 | Exploratory crossover trial comparing faster-acting insulin aspart (Fiasp®) vs standard insulin aspart (NovoLog®) in the Medtronic MiniMed 670G closed-loop system in T1DM adults |
| [NCT01487382](https://clinicaltrials.gov/study/NCT01487382) | N/A (Post-marketing) | Completed | 241 | Japanese post-marketing special survey of NovoRapid® (insulin aspart) in paediatric T1DM and T2DM under real-world clinical conditions; collected safety and efficacy data |
| [NCT00645827](https://clinicaltrials.gov/study/NCT00645827) | N/A | Completed | 78 | RCT evaluating an Insulin Infusion Conversion Equation (IICE) to improve inpatient glycaemic control during the transition from IV insulin infusion to subcutaneous insulin aspart injections |
| [NCT01755416](https://clinicaltrials.gov/study/NCT01755416) | Phase 2 | Completed | 18 | Closed-loop device study with ePID algorithm assessing adjunctive liraglutide vs insulin aspart monotherapy for postprandial glucose excursions in T1DM; technical feasibility data |
| [NCT07076199](https://clinicaltrials.gov/study/NCT07076199) | Phase 3 | Recruiting | 877 | 26-week head-to-head study: once-weekly insulin icodec vs once-daily insulin glargine U100, both combined with insulin aspart as bolus, in T1DM adults; expected completion December 2026 |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | Systematic Review | Diabetes & Metabolism | Systematic review and meta-analysis comparing insulin aspart (IAsp) vs regular human insulin (RHI) and biphasic IAsp vs premixed human insulin across T1DM and T2DM; IAsp consistently associated with superior HbA1c reduction and postprandial glucose control |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | The Lancet | ONWARDS 6 trial: once-weekly insulin icodec vs once-daily insulin degludec, both in basal-bolus regimen with insulin aspart, in T1DM adults; aspart served as the standard bolus comparator demonstrating established efficacy |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | The Lancet Diabetes & Endocrinology | EXPECT trial: non-inferiority RCT of insulin degludec vs insulin detemir, both combined with insulin aspart, in pregnant women with T1DM across multiple countries; confirmed safety and efficacy of aspart-containing regimens in high-risk obstetric populations |
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT | Diabetes, Obesity & Metabolism | Double-blind crossover RCT comparing faster-acting insulin aspart vs standard insulin aspart in T1DM adults using non-automated insulin pump with continuous glucose monitoring; directly evaluated head-to-head efficacy and safety |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Systematic Review | Drugs | Foundational comprehensive review of insulin aspart across T1DM and T2DM: faster absorption than regular human insulin, significantly improved postprandial glucose, and comparable or superior HbA1c |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | The Lancet Diabetes & Endocrinology | Comprehensive review of T1DM management in pregnancy, including rapid-acting insulin analogues, CGM, and pump therapy; reinforces the central role of aspart-class insulins in achieving time-in-range targets |
| [29978361](https://pubmed.ncbi.nlm.nih.gov/29978361/) | 2019 | Review | Clinical Pharmacokinetics | Pharmacokinetic and pharmacodynamic overview of faster insulin aspart (Fiasp®) compared with standard aspart; earlier glucose-lowering onset, greater 20-minute effect, with comparable overall efficacy |
| [25143741](https://pubmed.ncbi.nlm.nih.gov/25143741/) | 2014 | Review | Vascular Health and Risk Management | Review of the insulin degludec/insulin aspart fixed-ratio combination in T1DM and T2DM; contextualises the role of the aspart component in providing prandial coverage within a basal-bolus framework |
| [18710361](https://pubmed.ncbi.nlm.nih.gov/18710361/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Evidence-based evaluation of biphasic insulin aspart 30 in T1DM; addressed pre- and postprandial hyperglycaemia as independent risk factors for complications |
| [15871555](https://pubmed.ncbi.nlm.nih.gov/15871555/) | 2003 | Review | Treatments in Endocrinology | Spotlight review on insulin aspart (NovoLog®/NovoRapid®) in T1DM and T2DM; immediate-premeal dosing yielded significantly lower mean HbA1c and improved postprandial glucose vs regular human insulin |

---

## Singapore Market Information

Insulin aspart is currently **not registered** in Singapore. There are no product licences on record with the Health Sciences Authority (HSA).

For reference, insulin aspart is widely approved internationally under the following brand names:

| Jurisdiction | Brand Name | Manufacturer | Approved Indications |
|-------------|-----------|-------------|---------------------|
| USA (FDA) | NovoLog® | Novo Nordisk | T1DM and T2DM in adults and paediatric patients ≥2 years |
| EU (EMA) | NovoRapid® | Novo Nordisk | T1DM and T2DM in adults, adolescents, and children ≥1 year |
| Japan (PMDA) | ノボラピッド® | Novo Nordisk | T1DM and T2DM |
| Multiple markets | Fiasp® | Novo Nordisk | Faster-acting formulation; T1DM and T2DM |

A regulatory submission to HSA under the new drug application pathway would be required before this product can be marketed in Singapore.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data including key warnings, contraindications, and drug interaction profile were not available in this Evidence Pack. This represents a **blocking data gap** that must be resolved before any clinical or regulatory decision can be made. The package insert (SmPC or prescribing information) from the originator (Novo Nordisk) should be reviewed as the primary source.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Insulin aspart for Type 1 Diabetes Mellitus carries the highest tier of clinical evidence (L1), supported by multiple completed Phase 3 and Phase 4 randomised trials, extensive real-world safety data, and a strong pharmacological rationale. The drug is registered and widely used in virtually all high-income markets globally. The primary barrier in Singapore is not clinical — it is regulatory. The absence of HSA registration prevents patient access to a therapy that is considered standard of care internationally for T1DM.

**To proceed, the following is needed:**

- **Regulatory submission to HSA:** Initiate a full New Drug Application (NDA) or abridged application (referencing approved markets such as FDA or EMA) through the Health Sciences Authority
- **Safety data package:** Obtain current prescribing information (SmPC/PI) to document key warnings, contraindications, and drug interactions — this is currently a blocking data gap
- **Mechanism of action documentation:** Source MOA details from DrugBank (DB01306) or the originator SmPC to support the mechanistic rationale section of the regulatory dossier
- **Cold chain logistics:** Confirm storage and distribution infrastructure in Singapore for insulin products (typically 2–8°C refrigeration)
- **Local clinical guideline alignment:** Review the Ministry of Health Singapore's clinical practice guidelines for diabetes mellitus to confirm that insulin aspart-based regimens are consistent with recommended treatment algorithms
- **Paediatric considerations:** Given the evidence base includes paediatric T1DM populations, confirm whether paediatric labelling is sought in the Singapore submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

