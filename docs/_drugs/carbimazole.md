---
layout: default
title: Carbimazole
parent: Low Evidence (L5)
nav_order: 208
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Carbimazole: predicted new indication Resistance to thyroid hormone due to a mutation in thyroid hormone re… (evidence level L5). Approved use: Hyperthyroidism, Graves' disease, thyrotoxicosis"
monitor_inn: "Carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia", "Prinzmetal angina", "Hashimoto thyroiditis", "Raynaud disease", "migraine with brainstem aura", "kyphoscoliotic heart disease", "migraine disorder"]
---

# Carbimazole
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Carbimazole: From Hyperthyroidism to Resistance to Thyroid Hormone (Thyroid Hormone Receptor Beta Mutation)

## One-Sentence Summary

Carbimazole is an antithyroid drug (a prodrug of methimazole) originally used for hyperthyroidism, Graves' disease and thyrotoxicosis.
The TxGNN model's top-ranked prediction is **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta**, but the **0 clinical trials** and **1 case report** behind it do not support treatment, and the mechanism suggests possible harm.
Of the ten predictions, the best-supported are **neonatal thyrotoxicosis** and **autoimmune thyroid disease**, and both largely overlap with existing clinical use.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hyperthyroidism, Graves' disease, thyrotoxicosis (the Singapore licence records contain no indication text) |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, carbimazole is converted to methimazole, which inhibits thyroid peroxidase and lowers thyroid hormone synthesis. Its efficacy in hyperthyroidism is well established.

For the top-ranked prediction, the mechanism does not fit. In resistance to thyroid hormone (RTH-beta), the problem is receptor-level insensitivity, with elevated T4 and non-suppressed TSH. Lowering hormone production could raise TSH further and enlarge the goitre. The high score likely reflects network proximity to hyperthyroxinemia in the knowledge graph rather than a therapeutic basis. The one retrieved paper is a case report of a man treated intermittently with carbimazole for 10 years, with persistently elevated free T4 and non-suppressed TSH.

Other predictions fall into three groups:
- **Biologically plausible but not new:** neonatal thyrotoxicosis, hyperthyroxinemia and autoimmune thyroid disease (mainly Graves' disease). Thionamides are already used for these, so they are largely extensions of the approved use rather than true repurposing.
- **Weak or unsupported:** Hashimoto thyroiditis. Only a small 1980 study (20 patients) suggests carbimazole lowers thyroid antibodies, with no clinical benefit shown.
- **No evident link:** Prinzmetal angina, Raynaud disease, migraine (two forms) and kyphoscoliotic heart disease. These have no trials and no literature.

## Clinical Trial Evidence

No clinical trials are registered for the top-ranked prediction (RTH-beta). The only trials in the data relate to autoimmune thyroid disease (rank 5), and neither tests carbimazole for a new indication.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03303053](https://clinicaltrials.gov/study/NCT03303053) | Phase 3 | Unknown | 135 | Randomised study of cholestyramine or prednisolone added to standard antithyroid treatment (including carbimazole) in overt hyperthyroidism, aiming for faster control within 4 weeks. Informs context only. |
| [NCT00430547](https://clinicaltrials.gov/study/NCT00430547) | Not applicable | Completed | 60 | Study of thyroid-associated ophthalmopathy subtypes and orbital antibodies, comparing radioactive iodine with antithyroid medication in Graves' disease. No carbimazole intervention is evident. |

## Literature Evidence

Literature for the top-ranked prediction (RTH-beta) is limited to one case report. Key supporting papers for the more plausible predictions are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case report | BMJ Case Reports | RTH-beta presentation (elevated free T4, non-suppressed TSH) in a man treated intermittently with carbimazole for 10 years as "hyperthyroidism" |
| [24251220](https://pubmed.ncbi.nlm.nih.gov/24251220/) | 2013 | Review | Indian J Endocrinol Metab | Fetal and neonatal thyrotoxicosis, mostly from maternal TSH-receptor antibodies; mortality 12-20% |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Hyperthyroidism in pregnancy and outcomes for mother and child |
| [27978517](https://pubmed.ncbi.nlm.nih.gov/27978517/) | 2017 | Review | Horm Res Paediatr | Management of fetal and neonatal Graves' disease, with a diagnostic algorithm |
| [25952662](https://pubmed.ncbi.nlm.nih.gov/25952662/) | 2015 | Case report | Indian J Pediatr | Intrauterine carbimazole treatment of fetal hyperthyroidism in two siblings |
| [41191399](https://pubmed.ncbi.nlm.nih.gov/41191399/) | 2025 | Case report | Endocrinol Diabetes Metab Case Rep | Neonatal hypercalcaemia from transient thyrotoxicosis, responding to carbimazole |
| [12124735](https://pubmed.ncbi.nlm.nih.gov/12124735/) | 2002 | Case report | Am J Med Genet | Safety signal: choanal atresia after maternal carbimazole exposure (fourth published case) |
| [22394559](https://pubmed.ncbi.nlm.nih.gov/22394559/) | 2012 | Review | Lancet | Thionamides such as carbimazole or methimazole are the usual first-line treatment for thyrotoxicosis |
| [6247656](https://pubmed.ncbi.nlm.nih.gov/6247656/) | 1980 | Clinical/mechanistic study | N Engl J Med | Thyroid autoantibodies fell during carbimazole treatment independently of thyroxine changes, suggesting a direct effect on antibody synthesis |
| [6893563](https://pubmed.ncbi.nlm.nih.gov/6893563/) | 1980 | Clinical/mechanistic study | Br Med J | In 20 patients with Hashimoto's thyroiditis, microsomal antibody levels fell with carbimazole but thyroxine and TSH did not change |
| [24629864](https://pubmed.ncbi.nlm.nih.gov/24629864/) | 2014 | Review | Best Pract Res Clin Endocrinol Metab | Graves' disease in children; antithyroid drugs are first-line but only about 30% achieve remission |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN06923P | Carbimazole 5 mg Tablet (Remedica Ltd) | Tablet, film coated | Not recorded |
| SIN04453P | Carbimazole 5 mg Tablet (Sunward Pharmaceutical Private Limited) | Tablet | Not recorded |
| SIN04490P | Camazol 5 mg Tablet (Xepa-Soul Pattinson (Malaysia) Sdn Bhd) | Tablet | Not recorded |

All three licences are valid single-ingredient oral products.

## Safety Considerations

Please refer to the package insert for safety information.

Safety signals from the retrieved literature:
- A possible association between in-utero carbimazole exposure and choanal atresia (case reports).
- A case report of severe hypotension when amlodipine was added in a newborn on carbimazole and propranolol (an adverse event reported in that infant, not attributed to carbimazole alone).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (RTH-beta) has no trials, one case report, and a mechanism suggesting carbimazole could worsen TSH stimulation and goitre. The better-supported predictions (neonatal thyrotoxicosis, hyperthyroxinemia, autoimmune thyroid disease) largely overlap with existing thionamide use, so they are not true repurposing. They are best treated as research questions (L3-L4) rather than new development candidates. The remaining predictions have no supporting evidence.

**To proceed, the following is needed:**
- Safety information from the package insert (warnings and contraindications), which is currently missing
- Detailed mechanism of action data
- Approved indication text for the three Singapore licences
- For neonatal and fetal thyrotoxicosis: controlled data or guideline review, and a pregnancy and neonatal safety assessment, including the choanal atresia signal
- For RTH-beta: a clinical review to confirm that lowering thyroid hormone is not appropriate, and to rule out misdiagnosis as hyperthyroidism
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

