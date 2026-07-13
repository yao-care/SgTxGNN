---
layout: default
title: Flupentixol
parent: 僅模型預測 (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Flupentixol
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

# Flupentixol: From Psychosis to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Flupentixol is a thioxanthene-class dopamine D1/D2 receptor antagonist used internationally for schizophrenia and depression, with no registered products in Singapore.
The TxGNN model predicts it may be effective for **retinal dystrophy with or without extraocular anomalies**, with **0 clinical trials** and **15 publications** retrieved — none of which directly study Flupentixol for this indication.
The mechanistic rationale is considered weak, and overall evidence is insufficient to support advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Singapore; used internationally for schizophrenia and depression |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Singapore Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Flupentixol is a thioxanthene derivative that blocks dopamine D1 and D2 receptors. It is widely used internationally for the treatment of schizophrenia and depressive episodes. Detailed mechanistic data was not available in the current Evidence Pack; based on its pharmacological class, its primary action is central dopaminergic blockade.

The proposed mechanistic link rests on the fact that dopamine is endogenously present in retinal amacrine cells, where it participates in photoadaptation and light-dark circuit regulation. This is the biological thread the TxGNN model appears to have captured. However, retinal dystrophies — such as those caused by mutations in *RPGR*, *CRB1*, and *PRPF31* — are hereditary degenerative diseases whose pathology is driven at the genetic level, not by dopamine dysregulation. Blocking D1/D2 receptors offers no established mechanism for slowing or reversing genetically-driven photoreceptor degeneration. The mechanistic link is speculative and considered weak by current scientific standards.

The 15 publications retrieved cover general ocular conditions (orbital infections, ptosis, congenital fibrosis of extraocular muscles, ophthalmoplegia) and appear to have been identified based on keyword overlap with "extraocular anomalies." None examine Flupentixol in the context of retinal dystrophy. Combined with zero clinical trials, the evidentiary picture for this repurposing direction is very limited.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ **Important caveat:** The publications below were retrieved by keyword matching with "retinal dystrophy with or without extraocular anomalies." **None of these studies directly examine Flupentixol for this indication.** They are listed for transparency; their relevance to this repurposing hypothesis is indirect at best.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Original Study | Int J Mol Sci | Congenital fibrosis of extraocular muscles (CFEOM) caused by KIF21A/TUBB3 mutations; optic nerve and retinal abnormalities may co-occur, suggesting dysinnervation extends beyond the oculomotor system |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and imaging features of paediatric ocular pathologies including congenital/developmental lesions, persistent fetal vasculature, and Coats disease |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Ther Adv Ophthalmol | Eye involvement in inherited metabolic disorders; abnormalities can affect cornea, lens, retina, distal optic pathway, and extraocular muscles |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | Congenital anomalies of crystalline lens shape, beginning from 22nd day of gestation; associations with anterior segment dysgenesis |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | Neuroradiology | Neuroradiological and clinical features in ophthalmoplegia; efficient neuroradiological evaluation assists differential diagnosis and treatment |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Original Study | Am J Ophthalmol | Proposed unified theory for pathogenesis of maculopathy associated with cavitary optic disc anomalies and rational approach to treatment |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocul Vis Ocul Motil | Congenital cranial dysinnervation disorders (CCDDs): primary defect of cranial nucleus/nerve development; significant limitations of ocular motility |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuro-Ophthalmol | Isolated trochlear-oculomotor synkinesis in a healthy 6-year-old boy; proposed pathophysiology of congenital cranial dysinnervation |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Review | Klin Monbl Augenheilkd | Simple congenital ptosis characterised by fatty dystrophy and fibrosis of levator muscle; associated with refractive errors and binocular vision disturbances |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case Series/Review | Doc Ophthalmol | Wagner-Stickler syndrome complex: phenotypic variability including myopia, cataract, optically empty vitreous, and retinal detachment with poor surgical prognosis |

---

## Singapore Market Information

Flupentixol has **no registered products in Singapore**. There are no approved licences on record, and the drug is currently not marketed locally.

---

## Safety Considerations

Please refer to the package insert for safety information. No Singapore regulatory labelling data (including warnings or contraindications) was available for this review, and no drug–drug interaction data was retrieved from the DDI database.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN score (99.99%), the mechanistic link between dopamine D1/D2 antagonism and hereditary retinal dystrophy is weak — these diseases are driven by genetic mutations in photoreceptor-maintenance pathways, not dopaminergic signalling. There are zero clinical trials and zero directly relevant publications. Flupentixol is also not marketed in Singapore, making local regulatory and safety data unavailable.

**To proceed, the following is needed:**
- Detailed mechanism of action data (MOA) retrieved from DrugBank API (flagged as a current data gap)
- Singapore or international regulatory labelling, including black-box warnings and contraindications
- Preclinical studies demonstrating that dopamine receptor modulation has any measurable effect in genetic retinal dystrophy animal models (e.g., *rd10*, *rho*-mutant mice)
- A biologically plausible hypothesis connecting D1/D2 antagonism to photoreceptor survival or circuit preservation in specific genetic subtypes
- Expert ophthalmological and clinical pharmacology review before any further investment in this direction

---

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

