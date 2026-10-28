---
layout: default
title: Propylthiouracil
parent: Medium Evidence (L3-L4)
nav_order: 837
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Propylthiouracil"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
description: "Propylthiouracil: predicted new indication Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (evidence level L4). Approved use: Not recorded in the local data"
---

# Propylthiouracil
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Propylthiouracil: Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta
{: .text-alpha }

## One-Sentence Summary

Propylthiouracil (PTU) is an antithyroid drug originally used for hyperthyroidism, Graves' disease, thyrotoxicosis and thyroid crisis.
The TxGNN model's top-ranked prediction is **resistance to thyroid hormone due to a THRB mutation**, but there are **no clinical trials** and only **4 publications** (case reports and mouse models), and none show a therapeutic benefit.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta |
| TxGNN Prediction Score | 0.9966 |
| Evidence Level | L4 (rank 1); the highest-ranked evidence is L1 for autoimmune thyroid disease (rank 5), which is largely an on-label overlap |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold (rank 1); Proceed with Guardrails for autoimmune thyroid disease (rank 5) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on established pharmacology, PTU inhibits thyroid peroxidase, which reduces thyroid hormone synthesis, and also reduces peripheral conversion of T4 to T3. This makes it directly relevant to states of true thyroid hormone excess.

For the top-ranked prediction, the rationale is weak. In resistance to thyroid hormone (THRB mutation), tissues are insensitive to hormone and levels are already elevated. Lowering them further with an antithyroid drug could raise TSH and drive goiter or thyroid hyperplasia. Consistent with this, the retrieved case reports describe patients whose goiter enlarged during PTU treatment. The high TxGNN score probably reflects network proximity to thyroid hormone biology, not a validated treatment rationale.

Among the other predictions, only a few have a plausible link:
- **Neonatal thyrotoxicosis** is mechanistically relevant, but the literature concerns maternal treatment in pregnancy. PTU's liver toxicity limits direct use in neonates.
- **Hyperthyroxinemia, Hashimoto thyroiditis and Prinzmetal angina** are relevant only when true thyrotoxicosis is present.

---

## Clinical Trial Evidence

For the top-ranked prediction (resistance to thyroid hormone), currently no related clinical trials are registered.


| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05118542](https://clinicaltrials.gov/study/NCT05118542) | Phase 3 | Completed | 36 | PTU vs methimazole in Graves' disease; effect on early atherosclerosis markers |
| [NCT03066076](https://clinicaltrials.gov/study/NCT03066076) | Phase 3 | Unknown | 60 | Total thyroidectomy vs thionamides in Graves' ophthalmopathy |
| [NCT01056419](https://clinicaltrials.gov/study/NCT01056419) | Phase 4 | Unknown | 40 | Early total thyroidectomy vs antithyroid drugs in Graves' orbitopathy |
| [NCT03433352](https://clinicaltrials.gov/study/NCT03433352) | N/A | Unknown | 90 | Gut microbiota and methimazole response in Graves' disease (observational) |
| [NCT03447093](https://clinicaltrials.gov/study/NCT03447093) | N/A | Unknown | 120 | Oral microbiota in autoimmune thyroiditis (observational, no PTU intervention) |

---

## Literature Evidence

Publications for the top-ranked prediction (resistance to thyroid hormone):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case report | Clin Endocrinol | Neonatal thyrotoxicosis and maternal infertility in a family with a TRβ mutation (M313T) |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case report | Endocr J | Thai woman with a de novo TRβ mutation; goiter enlarged after 9 months of PTU given for presumed thyrotoxicosis |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Mouse model | Endocrinology | Role of TSH in thyroid carcinoma in TRβ-mutant mice |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Mouse model | Oncogene | Thyroid hormone activates tumour cell proliferation in a mouse model of follicular thyroid carcinoma |


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30283735](https://pubmed.ncbi.nlm.nih.gov/30283735/) | 2018 | Guideline | Eur Thyroid J | European Thyroid Association guideline for Graves' hyperthyroidism |
| [32929476](https://pubmed.ncbi.nlm.nih.gov/32929476/) | 2020 | Review | J Clin Endocrinol Metab | Update on management of Graves' thyroidal and extrathyroidal disease |
| [26321810](https://pubmed.ncbi.nlm.nih.gov/26321810/) | 2015 | Review (adverse effects) | Indian J Crit Care Med | PTU-induced autoimmune disease |
| [24622372](https://pubmed.ncbi.nlm.nih.gov/24622372/) | 2013 | Review | Lancet Diabetes Endocrinol | Hyperthyroidism in pregnancy |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00772P | PROPYLTHIOURACIL TABLETS BP 50 mg | Tablet | Not stated in the licence record |
| SIN11695P | PROPYL TABLET 50 mg | Tablet | Not stated in the licence record |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: thrombocytopenia, leukopenia, pancytopenia, agranulocytosis, neutropenia (including congenital forms), hypothyroidism, myxedema, congenital hypothyroidism, hyperbilirubinemia, Gilbert syndrome, drug-induced liver injury, and interstitial lung disease.
- **Drug Interactions**: 83 interactions were identified. Notable ones include:
  - Major: deferiprone.
  - Moderate: warfarin, dicoumarol, theophylline, aminophylline, oxtriphylline, naltrexone, macimorelin, radioactive iodine (I-131, I-123).
- **Additional points from the literature**: PTU carries a risk of severe liver injury (it is reserved for first-trimester pregnancy or methimazole intolerance), and of ANCA-associated vasculitis and PTU-induced autoimmune disease. Liver function monitoring is needed.

Please refer to the package insert for the full warnings and contraindications, as these were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold** (for the top-ranked prediction, resistance to thyroid hormone)

**Rationale:**
- The high TxGNN score is not supported by evidence. There are no trials, the literature is limited to case reports and mouse models, and PTU may worsen goiter in this condition by raising TSH.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which block the safety screening.
- Mechanism of action data (for example from DrugBank).
- For other predictions: any direct clinical or mechanistic evidence before further consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

