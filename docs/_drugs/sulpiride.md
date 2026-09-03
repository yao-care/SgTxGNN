---
layout: default
title: Sulpiride
parent: 僅模型預測 (L5)
nav_order: 933
evidence_level: L5
indication_count: 10
---

# Sulpiride
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

# Sulpiride: From an Unconfirmed Original Indication to a Predicted Role in Retinal Dystrophy

## One-Sentence Summary

> Sulpiride's original indication could not be determined from available regulatory data — the drug is **not currently marketed in Taiwan** and no approved indication text is on file.
> The TxGNN model predicts a possible link to **Retinal Dystrophy with or without Extraocular Anomalies**,
> but this is supported by **0 clinical trials** and **no drug-specific literature** — all 15 retrieved publications discuss the disease in general terms without mentioning Sulpiride.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available — drug is unlicensed in Taiwan, no original indication data on file |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Taiwan Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for Sulpiride (flagged as a **Blocking-severity data gap**). Based on general pharmacological class knowledge, Sulpiride is known as a **D2/D3 dopamine receptor antagonist**, a class typically used for psychiatric indications (e.g., schizophrenia, depression) and, in some markets, functional gastrointestinal or vestibular disorders.

Retinal dystrophy with or without extraocular anomalies is a heterogeneous group of **inherited retinal degeneration disorders**, generally driven by genetic mutations affecting photoreceptor structure or function. There is **no established pharmacological or mechanistic pathway** connecting dopaminergic receptor antagonism to the genetic/developmental processes underlying retinal dystrophy. The retrieved literature (see below) discusses orbital and ocular motility conditions in general clinical terms and does not reference Sulpiride, dopamine receptors, or any pharmacological intervention for retinal dystrophy.

Given the absence of a biologically plausible mechanism and the complete lack of drug-specific supporting evidence, this prediction should be treated as a **high-confidence but low-plausibility algorithmic signal**, warranting no further action without independent biological validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

⚠️ **Caveat:** The following publications were retrieved because they discuss the predicted disease (or closely related ocular/orbital conditions). **None of them mention Sulpiride**, and their relevance to this specific drug-disease pairing has not been confirmed (`relevance: pending` in source data). They are listed for transparency, not as supporting evidence.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging features of pediatric ocular pathologies, including congenital/developmental lesions |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and associated developmental abnormalities |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Review | Int J Molecular Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (genetic dysinnervation disorder) |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Therapeutic Advances in Ophthalmology | Eye involvement (including retina, extraocular muscles) in inherited metabolic disorders |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | Neuroradiology | Neuroradiological evaluation of ophthalmoplegia |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocular Vision Ocular Motility | Congenital Cranial Dysinnervation Disorders overview |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Review | Am J Ophthalmology | Pathogenesis/treatment of maculopathy with cavitary optic disc anomalies |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuro-Ophthalmology | Case of congenital trochlear-oculomotor synkinesis |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monatsbl Augenheilkd | Review of congenital ptosis, levator muscle dystrophy/fibrosis |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Seminars in Neurology | Clinical approach to diplopia (ocular/neurologic/muscular causes) |

---

## Singapore/Taiwan Market Information

Sulpiride is **not currently marketed in Taiwan** — no license or authorization records are on file (`total_licenses: 0`), so no product/indication table is available.

---

## Safety Considerations

Please refer to the package insert for safety information. No TFDA warnings, contraindications, or drug interaction data are currently on file for Sulpiride (this is flagged as a **Blocking-severity data gap** — TFDA package insert has not yet been retrieved and parsed).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Despite a very high TxGNN score (99.95%), there is no mechanistic plausibility, no clinical trial evidence, and no drug-specific literature connecting Sulpiride to retinal dystrophy. Combined with the Blocking-severity safety data gap (no TFDA label data) and the drug's unmarketed status in Taiwan, this candidate cannot proceed past S0. The remaining 9 predicted indications for Sulpiride in this evidence pack show the same pattern — L5 evidence, no supporting trials/literature, and Hold recommendations — reinforcing that these are likely algorithmic artifacts rather than genuine repurposing signals.

**To proceed, the following is needed:**
- TFDA package insert (warnings, contraindications) — currently Blocking gap (DG001)
- Confirmed mechanism of action from DrugBank — currently High-severity gap (DG002)
- Original indication data (Sulpiride's approved use elsewhere) to establish a baseline for mechanistic comparison
- Drug-specific literature search (Sulpiride + retinal dystrophy / dopamine + retinal degeneration) to confirm or rule out biological plausibility before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

