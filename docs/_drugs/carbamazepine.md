---
layout: default
title: Carbamazepine
parent: Medium Evidence (L3-L4)
nav_order: 204
evidence_level: L4
indication_count: 10
---

# Carbamazepine
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Carbamazepine: From Epilepsy and Trigeminal Neuralgia to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Carbamazepine is a sodium-channel-blocking anticonvulsant, established for focal epilepsy and trigeminal neuralgia.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but the supporting evidence is weak: **1 clinical trial** (an unrelated MRI imaging study) and **20 publications** (mostly case reports about tumour-caused facial pain).
This prediction is most likely a disease-mapping artifact, not true antitumour activity.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the HSA licence data; established use is epilepsy and trigeminal neuralgia |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the evidence pack. Carbamazepine is known to be a voltage-gated sodium-channel blocker and a first-line drug for trigeminal neuralgia. It is not known to have antineoplastic activity.

The likely graph signal is symptom-level. Tumours of, or near, the trigeminal nerve (schwannoma, meningioma, lymphoma, melanoma of Meckel's cave, pituitary adenoma) often present as secondary trigeminal neuralgia. Patients are then commonly started on carbamazepine. The model has probably linked the drug to the tumour through this shared symptom.

The literature supports this reading. In several reports, carbamazepine gave only partial or temporary pain relief, or none, while the tumour kept growing. Examples are trigeminal nerve lymphoma, Meckel's cave melanoma and a cerebellopontine angle lipoma. At best, carbamazepine treats the pain of a tumour, not the tumour itself.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06853119](https://clinicaltrials.gov/study/NCT06853119) | N/A | Not yet recruiting | 120 | MRI study of brain network and structural changes in trigeminal neuralgia. It is not a carbamazepine intervention trial and does not involve neoplasm (relevance grade C). |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [36824641](https://pubmed.ncbi.nlm.nih.gov/36824641/) | 2022 | Review | Acta Clin Croat | Treatment options for trigeminal neuralgia. Notes that the pain can be caused by vascular compression or a tumour. |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Medical and surgical treatments for trigeminal neuralgia. |
| [3181365](https://pubmed.ncbi.nlm.nih.gov/3181365/) | 1988 | Preclinical (animal) | Exp Neurol | Intravenous carbamazepine inhibited spontaneous activity in experimental rat neuromas. This is a pain and nerve-firing effect, not an antitumour effect. |
| [30741017](https://pubmed.ncbi.nlm.nih.gov/30741017/) | 2023 | Case report | Br J Neurosurg | Primary lymphoma of the trigeminal nerve with facial pain. Carbamazepine did not improve symptoms. |
| [15235745](https://pubmed.ncbi.nlm.nih.gov/15235745/) | 2004 | Case report | Arq Neuropsiquiatr | Primary melanoma of Meckel's cave. Pain was not relieved by carbamazepine. |
| [25142539](https://pubmed.ncbi.nlm.nih.gov/25142539/) | 2014 | Case report | Rinsho Shinkeigaku | Lymphoma spreading along the trigeminal nerve. Initial improvement on carbamazepine, then loss of effect. |
| [25433061](https://pubmed.ncbi.nlm.nih.gov/25433061/) | 2014 | Case report | No Shinkei Geka | Cerebellopontine angle lipoma. Pain was not adequately controlled with carbamazepine because of side effects. |
| [9109911](https://pubmed.ncbi.nlm.nih.gov/9109911/) | 1997 | Case report | Neurology | Post-irradiation neuromyotonia in the facial and trigeminal distribution responded to carbamazepine. |
| [26768887](https://pubmed.ncbi.nlm.nih.gov/26768887/) | 2016 | Case report | Turk Neurosurg | Pituitary adenoma presenting as isolated trigeminal neuralgia. |
| [11286444](https://pubmed.ncbi.nlm.nih.gov/11286444/) | 2001 | Survey | Br J Oral Maxillofac Surg | Practice survey of trigeminal neuralgia investigation and carbamazepine monitoring among UK surgeons. |

No RCTs were found. All literature is reviews, case reports, a survey and one animal study.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN02388P | TEGRETOL CR 400 TABLET 400 mg | Film-coated tablet | Novartis Farma S.p.A. |
| SIN05735P | APO-CARBAMAZEPINE TABLET 200 mg | Tablet | Apotex Inc |
| SIN00352P | TEGRETOL 200 TABLET 200 mg | Tablet | Novartis Farma S.p.A. / Mipharm S.p.A. |
| SIN05583P | STORILAT 200 TABLET 200 mg | Tablet | Remedica Ltd |
| SIN02387P | TEGRETOL CR 200 TABLET 200 mg | Film-coated tablet | Novartis Farma S.p.A. |

Approved indication text is not recorded in the current data for these licences. A sixth registration exists in the total count but is not listed in the data provided.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is at L4. The only registered trial is an unrelated imaging study, and the literature consists of case reports showing that carbamazepine relieves tumour-related pain, at best, without acting on the tumour. There is no sign of antitumour activity, so this prediction should not be pursued as tumour repurposing.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are currently missing
- Approved indication text for the Singapore licences
- Mechanism of action data from DrugBank
- Confirmation that the prediction is a disease-mapping artifact, for example by checking whether the graph link comes from a neuralgia or epilepsy node
- Review of the other top predictions for carbamazepine. Ranks 2–8 (audiogenic, eating-induced, thinking-induced and reading seizures, startle epilepsy and others) are reflex-seizure types with L4–L5 evidence. They fall within its existing focal epilepsy use, so incremental repurposing value is low.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

