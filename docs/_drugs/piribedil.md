---
layout: default
title: Piribedil
parent: 僅模型預測 (L5)
nav_order: 791
evidence_level: L5
indication_count: 10
---

# Piribedil
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

# Piribedil: From Parkinson's Disease to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Piribedil is a D2/D3 dopamine receptor agonist established in other markets for Parkinson's disease treatment (detailed original-indication data not present in this evidence pack).
The TxGNN model's top prediction is **Retinal Dystrophy with or without Extraocular Anomalies**,
but this is supported by **0 clinical trials** and **15 publications**, none of which mention Piribedil or a dopaminergic mechanism relevant to this eye disease — the evidence is essentially model-score-only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (based on known pharmacological classification as D2/D3 dopamine agonist; not formally recorded in Singapore regulatory data, as the drug is unmarketed here) |
| Predicted New Indication | Retinal dystrophy with or without extraocular anomalies |
| TxGNN Prediction Score | 99.34% |
| Evidence Level | L5 |
| Singapore Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack (flagged as a High-severity data gap). Based on general pharmacological knowledge referenced in the evidence pack's own analysis, Piribedil is a D2/D3 dopamine receptor agonist whose efficacy in Parkinson's disease is established in markets where it is registered.

For the top-ranked prediction, however, the evidence pack's own rationale is candid that **no known mechanistic link exists** between Piribedil's dopaminergic action and retinal dystrophy with extraocular anomalies. The 15 associated publications are general ophthalmology reviews and case reports on congenital eye/orbital conditions (e.g., congenital ptosis, orbital infections, congenital cranial dysinnervation disorders) — none discuss Piribedil, dopamine agonists, or a plausible biological pathway connecting the two. This appears to be a case of a high TxGNN embedding-similarity score without corroborating mechanistic or clinical support.

Notably, other lower-ranked predictions in this same batch are mechanistically far more coherent with Piribedil's known pharmacology — e.g., rank 2 ("paralysis agitans, juvenile, of Hunt," an old term for early-onset Parkinson's disease) and rank 5 ("juvenile onset Parkinson disease 19A") both align directly with dopamine agonist activity, even though they too currently lack clinical trial or literature support in this dataset.

---

## Clinical Trial Evidence

Currently no related clinical trials registered

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | Overview of orbital infections/cellulitis secondary to sinusitis; no drug relevance |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | Diagnostic approach to diplopia from ocular/neurologic/muscle causes; no drug relevance |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Congenital ptosis pathophysiology and levator muscle fibrosis; no drug relevance |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital lens shape anomalies and associated anterior segment dysgenesis; no drug relevance |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler syndrome vitreoretinal degeneration and associated anomalies; no drug relevance |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | Imaging classification of pediatric ocular pathologies including congenital lesions; no drug relevance |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Ther Adv Ophthalmol | Eye involvement across inherited metabolic disorders; no drug relevance |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | Two cases of unilateral cryptophthalmia with orbital/globe anomalies; no drug relevance |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | Isolated case of congenital trochlear-oculomotor synkinesis; no drug relevance |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optom Vis Sci | Case of congenital extraocular muscle fibrosis with synergistic divergence; no drug relevance |

**Note:** None of the above literature discusses Piribedil, dopamine agonists, or a mechanistic pathway connecting this drug class to retinal dystrophy/extraocular anomalies. These publications reflect general disease description rather than drug-disease evidence.

---

## Singapore Market Information

Piribedil is not currently marketed in Singapore — no product registrations or license records are present in the regulatory database (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information.

*(Note: this evidence pack flags a Blocking data gap — official warnings/contraindications from the regulatory label have not yet been retrieved — which must be resolved before any S1 safety review can proceed.)*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction has a high TxGNN score but is unsupported by any clinical trial evidence, and the associated literature is topically unrelated to Piribedil's dopaminergic mechanism. Combined with a Blocking data gap on safety/label information, there is insufficient basis to advance this candidate.

**To proceed, the following is needed:**
- Official TFDA/HSA label data (warnings, contraindications) to close the Blocking data gap (DG001)
- Confirmed mechanism of action (MOA) documentation (DG002)
- Targeted literature/mechanistic search specifically linking dopamine agonism to retinal dystrophy pathophysiology, or reconsideration of higher mechanistic-plausibility candidates in this batch (e.g., ranks 2 and 5, both related to early-onset Parkinsonism)
- Any preclinical or case-level evidence directly involving Piribedil in ophthalmologic indications, if it exists
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

