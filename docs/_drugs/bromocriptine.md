---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From Parkinson's Disease / Hyperprolactinemia to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Bromocriptine is a semisynthetic ergot alkaloid and dopamine D2/D3 receptor agonist, with internationally established indications including Parkinson's disease, hyperprolactinemia, and type 2 diabetes mellitus, though it is not currently marketed in Singapore.
The TxGNN model's highest-ranked novel prediction is **Congenital Disorder of Glycosylation with Defective Fucosylation** (score 99.83%), with **no clinical trials** and **no publications** directly supporting this specific direction.
Among all 10 predictions reviewed in this pack, **Retinal Dystrophy with or without Extraocular Anomalies** (rank 3) carries the most plausible mechanistic basis with pre-clinical drug repurposing evidence, while **Schizophrenia** (rank 9) has the largest evidence base (3 clinical trials, 20 publications) but is complicated by a documented signal that Bromocriptine can itself induce psychotic symptoms.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease, hyperprolactinemia, type 2 diabetes mellitus (internationally established; no Singapore registration) |
| Predicted New Indication | Congenital Disorder of Glycosylation with Defective Fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Singapore Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Mechanism of action data for Bromocriptine is not available in this Evidence Pack; the following draws on established pharmacological literature. Bromocriptine acts principally as a partial agonist at dopamine D2 and D3 receptors in the pituitary, striatum, and hypothalamus. Pituitary D2 agonism suppresses prolactin secretion, underpinning its use in hyperprolactinemia and prolactin-secreting adenomas. Striatal D2/D3 activation compensates for dopamine deficiency in the nigrostriatal pathway, providing symptomatic benefit in Parkinson's disease. A distinct mechanism — modulation of hypothalamic circadian signalling and sympathetic nervous system tone via D2 receptors — supports its FDA-approved use for type 2 diabetes mellitus (brand name Cycloset). Bromocriptine therefore operates at the intersection of neuroendocrine and metabolic regulation, with no established cytotoxic activity.

Congenital Disorders of Glycosylation with Defective Fucosylation are rare inherited metabolic diseases affecting the biosynthesis of fucosylated glycoproteins. The best-characterised subtype is CDG-IIc (Leukocyte Adhesion Deficiency Type II, LAD-II), caused by loss-of-function mutations in *SLC35C1*, which encodes the Golgi GDP-fucose transporter. Clinical features include recurrent bacterial infections due to absent selectin ligands, intellectual disability, short stature, and distinctive facies. Partial phenotypic rescue with exogenous fucose supplementation is possible in some patients.

The mechanistic link between Bromocriptine's dopamine receptor pharmacology and CDG fucosylation defects is highly speculative and currently lacks any experimental or clinical basis. Dopamine D2/D3 receptor agonism has no established pathway to enhance GDP-fucose synthesis, transport into the Golgi, or incorporation into glycoproteins. The TxGNN model's high prediction score most likely reflects indirect topological proximity within the disease–gene–drug knowledge graph rather than a direct pharmacological mechanism. This prediction is classified L5 (model prediction only) and requires foundational pre-clinical validation before any resources are committed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Congenital Disorder of Glycosylation with Defective Fucosylation.

---

## Literature Evidence

Currently no related literature available for Congenital Disorder of Glycosylation with Defective Fucosylation.

---

## Singapore Market Information

Bromocriptine is not currently registered in Singapore. No product authorizations are on record in this dataset.

For reference, bromocriptine is marketed internationally under brand names including **Parlodel** (Novartis) and **Cycloset** (Salix Pharmaceuticals), with approved indications spanning Parkinson's disease, hyperprolactinemia, acromegaly, and type 2 diabetes mellitus. Any future Singapore registration pathway should reference these international reference products.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings and contraindications data are not available in this Evidence Pack; prescribers should consult the manufacturer's current prescribing information and the Health Sciences Authority (HSA) Therapeutic Products guidance.

**Notable safety signal relevant to CNS repurposing:** Clinical literature associated with the Schizophrenia prediction (rank 9, PMID 8120934) documents a case where low-dose bromocriptine induced schizophrenia-like psychosis in a patient without prior psychiatric history; symptoms resolved fully on discontinuation. This is consistent with the known risk of dopamine agonists precipitating or exacerbating psychotic symptoms via mesolimbic D2 hyperstimulation, and is a critical safety consideration for any proposed CNS repurposing of this drug.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN prediction — Congenital Disorder of Glycosylation with Defective Fucosylation — is a pure model prediction (L5) with no clinical, pre-clinical, or mechanistic supporting evidence, and the proposed dopaminergic–glycosylation axis lacks any established biological basis.

**To proceed, the following is needed:**

- **MOA data (DrugBank API):** Retrieve the full receptor binding profile, pharmacodynamics, target affinities (D1, D2, D3, serotonin 5-HT2C, adrenergic), and pharmacokinetics to enable a proper mechanistic plausibility screen
- **Pre-clinical mechanistic validation:** Cell-based assays in CDG patient-derived fibroblasts or equivalent models testing whether D2 receptor agonism or downstream cAMP/PKA pathway modulation affects GDP-fucose transport or fucosylation capacity
- **Singapore regulatory pathway:** Confirm whether any compassionate-use, clinical trial importation, or foreign reference product (Parlodel/Cycloset) registration route is applicable before committing to development activities
- **Prioritise Retinal Dystrophy (rank 3, L4):** Commission a dedicated evaluation; PMID 39009597 (Nature Communications, 2024) reports mutation-agnostic pre-clinical efficacy for a systems pharmacology combination including bromocriptine in inherited retinopathy models — this is the most immediately actionable signal in this pack
- **Evaluate Schizophrenia signal (rank 9, L3) with full safety risk stratification:** The available literature indicates Bromocriptine acts on negative symptoms as a D2 agonist adjunct, but the same mechanism carries documented psychosis-induction risk; a benefit–risk analysis for adjunctive use in treatment-resistant negative symptoms requires a separate safety-focused evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

