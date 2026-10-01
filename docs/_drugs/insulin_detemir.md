---
layout: default
title: Insulin Detemir
parent: High Evidence (L1-L2)
nav_order: 531
evidence_level: L1
indication_count: 10
---

# Insulin Detemir
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Insulin Detemir: From Diabetes Mellitus to Type 1 Diabetes Mellitus

## One-Sentence Summary

Insulin detemir (Levemir) is a long-acting basal insulin analogue used for diabetes mellitus. The Singapore licence records do not state the approved indication text.
The TxGNN model ranks **type 1 diabetes mellitus** first, but this is an already-established use of the drug, not a new repurposing finding.
The prediction is backed by **50 retrieved clinical trials** (several are detemir head-to-head Phase 3 RCTs) and **19 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Type 1 diabetes mellitus |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Proceed with Guardrails |

The Original Indication row is omitted because both Singapore licence records have empty indication text.

---

## Why is This Prediction Reasonable?

Insulin detemir is acylated with a 14-carbon fatty acid. This lets it bind reversibly to albumin after subcutaneous injection, which slows absorption and gives a prolonged, consistent effect of up to 24 hours. It binds the insulin receptor and replaces the insulin that is missing in type 1 diabetes. Structured mechanism-of-action data is not available in the Evidence Pack, so this description comes from the published reviews.

The high score (0.998) reflects a well-established indication rather than a novel signal. Detemir is used as basal insulin in both type 1 and type 2 diabetes, so type 1 diabetes is a labelled use. The report should not present it as a new discovery.

The other nine predictions are not credible new uses:
- **Pancreatic agenesis** (rank 7): insulin replacement is plausible, but no trial or literature evidence was retrieved.
- **Autoimmune oophoritis, stiff person syndrome, focal stiff limb syndrome, thiamine-responsive dysfunction syndrome:** these likely reflect comorbidity with diabetes or autoimmune conditions in the knowledge graph, not a therapeutic effect.
- **Opsismodysplasia:** the link is theoretical only.
- **Drug-induced localized lipodystrophy, centrifugal lipodystrophy, pressure-induced localized lipoatrophy:** the first two mainly reflect a known injection-site adverse effect, and the third is a similar fat-loss phenotype. They should be treated as safety signals, not treatment benefits.

All nine have no clinical evidence (L5) and are on Hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00184665](https://clinicaltrials.gov/study/NCT00184665) | Phase 3 | Completed | 501 | 2-year comparison of detemir vs NPH insulin in type 1 diabetes (HbA1c, hypoglycaemia, weight) |
| [NCT00474045](https://clinicaltrials.gov/study/NCT00474045) | Phase 3 | Completed | 470 | Detemir vs NPH, with aspart as mealtime insulin, in pregnant women with type 1 diabetes |
| [NCT01697657](https://clinicaltrials.gov/study/NCT01697657) | Phase 3 | Completed | 131 | Crossover comparison of hypoglycaemia frequency, detemir vs NPH, in well-controlled type 1 diabetes |
| [NCT00487240](https://clinicaltrials.gov/study/NCT00487240) | Phase 3 | Completed | 387 | Insulin lispro protamine vs detemir as basal insulin in type 1 diabetes |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | Completed | 362 | Insulin degludec/aspart vs detemir plus mealtime aspart in children and adolescents with type 1 diabetes |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | Completed | 520 | Detemir once vs twice daily in a basal-bolus regimen in type 1 diabetes |
| [NCT00841087](https://clinicaltrials.gov/study/NCT00841087) | Phase 2 | Completed | 65 | 6-week exploratory safety trial of degludec vs detemir, with emphasis on hypoglycaemia, in type 1 diabetes |
| [NCT00738153](https://clinicaltrials.gov/study/NCT00738153) | N/A (observational) | Completed | 798 | Real-world efficacy and serious adverse drug reactions of Levemir in type 1 and 2 diabetes |
| [NCT00655044](https://clinicaltrials.gov/study/NCT00655044) | N/A (observational) | Completed | 3,637 | Serious adverse drug reactions of Levemir in routine practice |
| [NCT00509925](https://clinicaltrials.gov/study/NCT00509925) | Phase 4 | Terminated | 23 | Energy expenditure, detemir vs NPH, in type 1 diabetes (small; ended early) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT trial: degludec vs detemir, each with aspart, in pregnant women with type 1 diabetes (non-inferiority) |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | Systematic review / meta-analysis | Pol Arch Med Wewn | Detemir vs NPH in type 1 diabetes; earlier studies did not all confirm a glycaemic benefit |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | Network meta-analysis | Value Health | Relative efficacy and safety of basal insulin regimens in adults with type 1 diabetes |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Systematic review / meta-analysis | Clin Ther | Degludec vs glargine and detemir in type 1 and 2 diabetes |
| [23110609](https://pubmed.ncbi.nlm.nih.gov/23110609/) | 2012 | Review | Drugs | Detemir is a basal insulin analogue for type 1 and 2 diabetes; less within-patient variability than NPH |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Albumin binding gives a prolonged, more consistent effect and less variability than NPH |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Detemir can reduce hypoglycaemia risk, especially nocturnal, in type 1 and 2 diabetes |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | Detemir offers effective basal options with a lower hypoglycaemia rate |
| [37290466](https://pubmed.ncbi.nlm.nih.gov/37290466/) | 2023 | Review | Lancet Diabetes Endocrinol | Update on managing type 1 diabetes in pregnancy, including pharmacological treatment |
| [18454569](https://pubmed.ncbi.nlm.nih.gov/18454569/) | 2008 | Review | Paediatr Drugs | Insulin analogues, including detemir, in children and adolescents with type 1 diabetes |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN13115P | LEVEMIR® FLEXPEN® 100U/ML, 3ML | Injection, solution | Novo Nordisk A/S (and affiliated production sites) |
| SIN15515P | LEVEMIR® PENFILL® 100 U/ML | Injection, solution | Novo Nordisk A/S (Bagsværd) (and affiliated production sites) |

Approved indication text is not stated in either licence record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least two completed Phase 3 RCTs compare detemir with NPH or other basal insulins in type 1 diabetes, which meets L1. The drug is marketed in Singapore, and type 1 diabetes is a labelled use rather than a repurposing.

**To proceed, the following is needed:**
- Obtain the HSA package insert to confirm the approved indications and to fill the missing warnings and contraindications. This is a blocking gap for safety screening.
- Confirm the label status of type 1 diabetes against the local regulatory record, and do not present it as a new repurposing finding.
- Add a hypoglycaemia monitoring plan, and watch for injection-site lipodystrophy (predicted ranks 8–10 are most likely adverse-effect signals).
- Add structured mechanism-of-action data from DrugBank.
- Keep the other nine predictions on Hold unless supporting evidence, such as case reports for pancreatic agenesis, is curated.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

