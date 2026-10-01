---
layout: default
title: Thiamine
parent: Medium Evidence (L3-L4)
nav_order: 971
evidence_level: L3
indication_count: 10
---

# Thiamine
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **10** 
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

# Thiamine: From Vitamin B1 Supplementation to Hyperthyroidism

## One-Sentence Summary

Thiamine (vitamin B1) is marketed in Singapore mainly in oral B-vitamin tablets and in injectable forms, but the registration data do not state an approved indication.
The TxGNN model predicts it may be useful for **hyperthyroidism**, with **1 clinical trial** (a 12-patient pilot) and **20 retrieved publications**.
These are mostly case reports of thiamine-deficiency complications, so the evidence supports correcting deficiency in hyperthyroid patients, not treating the thyroid disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration data (all approved indication texts are empty) |
| Predicted New Indication | Hyperthyroidism |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available. Thiamine is a cofactor for transketolase, pyruvate dehydrogenase and alpha-ketoglutarate dehydrogenase, which are central to carbohydrate energy metabolism.

Hyperthyroidism is a hypermetabolic state that increases thiamine use and can cause functional deficiency. The literature links this to Wernicke encephalopathy, often in pregnancy with hyperemesis, and to beriberi-like high-output heart failure. The plausible benefit is therefore preventing or treating deficiency-related complications in hyperthyroid patients.

There is no evidence that thiamine acts on thyroid hormone production or on the autoimmune process in Graves disease. The prediction should be read as "thiamine as supportive care in hyperthyroidism", not as a disease-modifying treatment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02767245](https://clinicaltrials.gov/study/NCT02767245) | N/A | Completed | 12 | Pilot study of thiamine supplementation to improve cardiovascular function in severe hyperthyroidism. It also assesses the prevalence of thiamine deficiency. Randomization and results are not shown in the input. |

---

## Literature Evidence

Of the 20 retrieved papers, 10 are listed below. One feline veterinary paper (PMID 40692342) and several unrelated or purely historical items are omitted. No RCTs or systematic reviews were found. Study types are taken from the classification where available, otherwise judged from the title or abstract.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [26567494](https://pubmed.ncbi.nlm.nih.gov/26567494/) | 2015 | Case report | Crit Care Nurs Clin North Am | Thyrotoxicosis and wet beriberi (severe thiamine deficiency) both cause high-output heart failure. |
| [32983708](https://pubmed.ncbi.nlm.nih.gov/32983708/) | 2020 | Case report | Cureus | Wernicke encephalopathy with transient gestational hyperthyroidism and hyperemesis gravidarum. |
| [18026802](https://pubmed.ncbi.nlm.nih.gov/18026802/) | 2008 | Case report | J Gen Intern Med | Wernicke encephalopathy in a thyrotoxic patient. |
| [36176825](https://pubmed.ncbi.nlm.nih.gov/36176825/) | 2022 | Case report | Cureus | Wernicke encephalopathy after persistent vomiting and weight loss in a patient started on methimazole. |
| [36593922](https://pubmed.ncbi.nlm.nih.gov/36593922/) | 2023 | Case report | Radiol Case Rep | Uncommon Wernicke presentation in a pregnant woman with pre-gestational hyperthyroidism. |
| [25148818](https://pubmed.ncbi.nlm.nih.gov/25148818/) | 2014 | Case report | Endocr Pract | Gestational thyrotoxicosis and hyperemesis gravidarum associated with Wernicke encephalopathy. |
| [34995426](https://pubmed.ncbi.nlm.nih.gov/34995426/) | 2021 | Case report | S D Med | Wernicke encephalopathy with visual disturbances in a Graves disease patient after sleeve gastrectomy. |
| [32934066](https://pubmed.ncbi.nlm.nih.gov/32934066/) | 2020 | Case report | Clin Med (Lond) | Pregnant woman with thyrotoxicosis, persistent vomiting and confusion; brain MRI showed symmetrical changes. |
| [22436368](https://pubmed.ncbi.nlm.nih.gov/22436368/) | 2013 | Not classified (no abstract) | Neurologia | Title: Wernicke encephalopathy secondary to hyperthyroidism and ingestion of thiaminase-rich products. |
| [13305517](https://pubmed.ncbi.nlm.nih.gov/13305517/) | 1955 | Clinical physiology study | Endocrinologia e scienza della costituzione | Urinary thiamine after intravenous cocarboxylase load in hyperthyroidism versus normal subjects. |

---

## Singapore Market Information

Singapore has 10 registrations in total. Five are shown below, all film-coated oral tablets. Injectable forms (injection; powder for solution) are also registered.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12077P | DANEURON TABLET | Tablet, film coated | Not stated in registration data |
| SIN10891P | NEURO-B TABLET | Tablet, film coated | Not stated in registration data |
| SIN07635P | VITAMIN B FORTE TABLET | Tablet, film coated | Not stated in registration data |
| SIN11606P | NEUROSANBE TABLET | Tablet, film coated | Not stated in registration data |
| SIN10260P | NUTRIHEALTH NEUROVIT FORTE TABLET | Tablet, film coated | Not stated in registration data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only trial is a 12-patient pilot with no results shown, and the literature is almost entirely case reports of deficiency complications. The package insert safety review (warnings and contraindications) has not been done and is a blocking data gap. The pack classifies this as a research question, not a treatment candidate.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking), plus the approved indications for the registered products
- Results and design details of NCT02767245 (randomization, thiamine deficiency prevalence, cardiovascular outcomes)
- Controlled data showing that thiamine improves outcomes in hyperthyroid patients, as opposed to correcting deficiency alone
- Mechanism-of-action data from DrugBank
- A defined target population, such as hyperthyroid patients with hyperemesis, malnutrition or high-output heart failure, where deficiency is most plausible

Among the other predictions, pulmonary hypertension (L3) has the strongest signal, but only in thiamine-deficiency-driven cases, mainly in infants. It is outside the scope of this report.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

