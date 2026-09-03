---
layout: default
title: Rasagiline
parent: 僅模型預測 (L5)
nav_order: 846
evidence_level: L5
indication_count: 10
---

# Rasagiline
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

# Rasagiline: From Parkinson's Disease to Lewy Body Dementia

## One-Sentence Summary

Rasagiline is a selective MAO-B inhibitor used for Parkinson's disease. Across ten TxGNN-predicted indications, most are mechanistically implausible (e.g. inherited metabolic disorders, retinal dystrophy) with zero supporting evidence, but **Lewy Body Dementia** stands out as the only candidate with a partial evidence trail — **1 withdrawn clinical trial** and **12 publications**, though none directly confirm efficacy in this population. This drug is currently not marketed in Singapore.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (per DrugBank; no Singapore approved indication text available) |
| Predicted New Indication | Lewy Body Dementia |
| TxGNN Prediction Score | 98.83% |
| Evidence Level | L4 |
| Singapore Market Status | 未上市 (Not marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this Evidence Pack (marked as a Blocking data gap). Based on known pharmacology, rasagiline is a selective, irreversible MAO-B inhibitor approved for Parkinson's disease, where it reduces dopamine breakdown and has demonstrated neuroprotective/anti-apoptotic properties in preclinical models via its propargylamine structure.

Lewy Body Dementia (LBD) shares core pathology with Parkinson's disease — both are synucleinopathies driven by α-synuclein accumulation, with overlapping dopaminergic and cholinergic degeneration. This provides a plausible theoretical rationale for TxGNN's high prediction score (98.83%, rank 11,851). Mechanistic literature supports this link: α-synuclein has been shown to directly bind and stimulate MAO-B activity, triggering downstream neurodegenerative cascades relevant to both PD and LBD (PMID 29769405).

However, the only clinical trial identified (NCT05611372) was designed for prodromal Parkinson's disease — not LBD — and was **withdrawn with zero enrollment**, producing no data. The literature is dominated by mechanistic/preclinical studies and studies of related compounds (e.g. ladostigil) rather than direct clinical evidence in LBD patients. The single trial with human data (PMID 33614888) was conducted in Alzheimer's disease, not LBD. This is a biologically plausible but clinically unproven hypothesis.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05611372](https://clinicaltrials.gov/study/NCT05611372) | Phase 2/3 | Withdrawn | 0 | Designed to test whether 1 year of rasagiline reduces progression from prodromal REM sleep behavior disorder to Parkinson's disease. Not targeted at LBD; withdrawn before enrollment, no data generated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33614888](https://pubmed.ncbi.nlm.nih.gov/33614888/) | 2021 | Phase II RCT (Alzheimer's, not LBD) | Alzheimer's & Dementia (NY) | Rasagiline 1mg/day for 24 weeks evaluated for effects on brain glucose metabolism, cognition, and tau in mild-moderate AD — proof-of-concept, not LBD-specific. |
| [36232361](https://pubmed.ncbi.nlm.nih.gov/36232361/) | 2022 | Review (Mechanistic) | Int J Mol Sci | Reviews neuroprotective function of MAO-B inhibitors (rasagiline, selegiline) across synucleinopathies including PD, dementia with Lewy bodies, and MSA. |
| [38412454](https://pubmed.ncbi.nlm.nih.gov/38412454/) | 2024 | Review/Drug Design | Archiv der Pharmazie | Describes hybrid molecules combining neflamapimod and rasagiline pharmacophores specifically targeting LBD, citing rasagiline's neuroprotective propargylamine scaffold. |
| [29769405](https://pubmed.ncbi.nlm.nih.gov/29769405/) | 2018 | Preclinical/Mechanistic | The EMBO Journal | α-Synuclein directly binds and stimulates MAO-B activity, triggering AEP activation and dopaminergic neurodegeneration relevant to PD/LBD pathology. |
| [20555137](https://pubmed.ncbi.nlm.nih.gov/20555137/) | 2010 | Preclinical/Mechanistic | J Alzheimer's Disease | Propargylamine MAO-B inhibitors (selegiline, rasagiline) modulate amyloid precursor protein processing via MAPK/PKC pathways. |
| [29549278](https://pubmed.ncbi.nlm.nih.gov/29549278/) | 2018 | Cohort (Imaging) | Scientific Reports | Tau-PET imaging study comparing PD, PD-dementia, and DLB retention patterns; not a rasagiline intervention study. |
| [38988416](https://pubmed.ncbi.nlm.nih.gov/38988416/) | 2024 | Cohort (Biomarker) | Alzheimer's & Dementia (NY) | Biomarker analysis from the rasagiline AD trial cohort; not LBD-specific. |
| [17197368](https://pubmed.ncbi.nlm.nih.gov/17197368/) | 2006 | Review | Neurotoxicity Research | Discusses ladostigil, a multifunctional drug combining rasagiline's neuroprotective pharmacophore with cholinesterase inhibition, for dementia/Parkinsonism comorbidity. |
| [16086033](https://pubmed.ncbi.nlm.nih.gov/16086033/) | 2005 | Preclinical | Br J Pharmacology | Neurochemical/behavioral effects of ladostigil (rasagiline-derived compound) in rat models. |
| [12697291](https://pubmed.ncbi.nlm.nih.gov/12697291/) | 2003 | Preclinical | Neuroscience Letters | Anti-apoptotic action of rasagiline-derived TV3326 compound, developed to protect neurons in Alzheimer's and Lewy body disease. |

Two additional records ([16935943](https://pubmed.ncbi.nlm.nih.gov/16935943/), [16175158](https://pubmed.ncbi.nlm.nih.gov/16175158/)) were retrieved but are either unclassified or general PD reviews with limited direct relevance to LBD.

---

## Singapore Market Information

This drug is not currently registered in Singapore (0 licenses on file).

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this evidence pack (flagged as a Blocking data gap — TFDA label warnings/contraindications must be sourced before any safety evaluation can proceed).

---

## Other Predicted Indications (Screened Out)

Nine of the ten predicted indications for rasagiline had **no supporting clinical trials or literature** and are mechanistically unrelated to MAO-B inhibition (e.g. transaldolase deficiency, fructose-1,6-bisphosphatase deficiency, congenital glycosylation disorders, polymicrogyria syndromes, Rasmussen encephalitis, myelitis). These are classified as L5 (model prediction only) and are not viable repurposing candidates. One indication — "paralysis agitans, juvenile, of Hunt" (an archaic term for juvenile-onset Parkinsonism) — shares the same pathophysiology as the approved indication but has no direct trial/literature evidence for the juvenile population specifically. Retinal dystrophy literature hits (PMID 9416661 and others) are search noise — unrelated ophthalmology topics with no rasagiline connection.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The strongest candidate (Lewy Body Dementia) has a plausible shared-pathology rationale but zero direct clinical evidence — its only relevant trial was withdrawn with no enrollment, and no completed trial has tested rasagiline specifically in LBD patients. Combined with the Blocking data gap on TFDA safety labeling, this candidate cannot proceed past a research-hypothesis stage.

**To proceed, the following is needed:**
- TFDA/regulatory label data (warnings, contraindications) to clear the Blocking safety gap
- Detailed mechanism of action documentation from DrugBank
- A dedicated, adequately powered clinical trial of rasagiline in confirmed LBD patients (not PD or AD surrogates)
- Confirmation of Singapore market status/import pathway, since the drug is currently unregistered here
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

