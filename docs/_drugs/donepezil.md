---
layout: default
title: Donepezil
parent: Low Evidence (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Donepezil
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

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is a reversible acetylcholinesterase inhibitor, widely used for Alzheimer's disease. The TxGNN model predicts it may be effective for **psychogenic movement disorders**, but **no clinical trials and no publications** were retrieved for this prediction. It is a model-only signal (Evidence Level L5).

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Psychogenic movement disorders |
| TxGNN Prediction Score | 99.23% (rank 8,800) |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 13 |
| Recommended Decision | Hold |

The Singapore records supplied carry no approved-indication text, so no original indication is listed in the table. The title uses Alzheimer's disease as the drug's well-established use, which the supplied literature describes as the standard therapy for cholinesterase inhibitors.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the dataset. Donepezil is a reversible acetylcholinesterase inhibitor. Its efficacy in Alzheimer's disease is established, and cholinergic signalling is involved in basal ganglia circuits, so a role in movement disorders is conceivable.

For psychogenic (functional) movement disorders, however, no established mechanistic rationale exists in the supplied data. The high score should be read with caution. All top-10 predictions for this drug fall within a narrow band of 0.98 to 0.99, so the score alone does not separate strong candidates from weak ones. Increased cholinergic tone can also worsen tremor and extrapyramidal symptoms, so the direction of effect is unclear.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications with Evidence

Some lower-ranked predictions have more supporting evidence than the top-ranked one. All rows below are research questions at best, and none is supported by a registered trial or RCT.

| Rank | Predicted Indication | Score | Evidence Level | Recommendation | Evidence Summary |
|------|------|------|------|------|------|
| 2 | Chronic tic disorder | 99.19% | L3 | Research Question | An 18-week open-label pediatric study ([18343255](https://pubmed.ncbi.nlm.nih.gov/18343255/), 2008, Clin Ther) in children with tics and ADHD, plus a case report ([10440471](https://pubmed.ncbi.nlm.nih.gov/10440471/)) and a commentary ([16986157](https://pubmed.ncbi.nlm.nih.gov/16986157/)). Mouse head-twitch studies ([14643839](https://pubmed.ncbi.nlm.nih.gov/14643839/), [16045972](https://pubmed.ncbi.nlm.nih.gov/16045972/)) suggest serotonergic effects. |
| 10 | Glaucoma | 98.28% | L3 | Research Question | A pilot study in normal-tension glaucoma ([20415624](https://pubmed.ncbi.nlm.nih.gov/20415624/), 2010) on cerebral and optic nerve head blood flow, and a rat retinal neuroprotection study ([20197638](https://pubmed.ncbi.nlm.nih.gov/20197638/)). |
| 8 | Lingual-facial-buccal dyskinesia | 99.02% | L4 | Research Question | Mostly a short report ([15689723](https://pubmed.ncbi.nlm.nih.gov/15689723/)) and drug-class Cochrane reviews ([29553158](https://pubmed.ncbi.nlm.nih.gov/29553158/), [12137608](https://pubmed.ncbi.nlm.nih.gov/12137608/)). One case of donepezil-induced jaw tremor ([18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/)) points the other way. |
| 4 | Extrapyramidal and movement disease | 99.16% | L4 | Hold | Mixed evidence. A 2025 systematic review ([40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/)) points to movement disorders as an adverse effect of cholinesterase inhibitors. A small tardive-movement report ([15669896](https://pubmed.ncbi.nlm.nih.gov/15669896/)) suggests benefit. |
| 3, 5, 7, 9 | Primary orthostatic tremor, benign shuddering attacks, benign paroxysmal tonic upgaze of childhood with ataxia, acute intermittent porphyria | 98.75–99.17% | L5 | Hold | Prediction only. No trials or literature. |
| 6 | Tremor-nystagmus-duodenal ulcer syndrome | 99.15% | L5 | Hold | The only retrieved paper ([41362004](https://pubmed.ncbi.nlm.nih.gov/41362004/)) concerns Behçet disease and is likely a keyword mismatch. |

## Singapore Market Information

Donepezil has 13 registrations in Singapore. The five listed below are the main ones; none of the records supplied includes approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN13645P | Aricept Evess 5mg orodispersible tablet | Orally disintegrating tablet | Bushu Pharmaceuticals Ltd. |
| SIN15565P | Jubdozil film coated tablet 5mg | Film-coated tablet | Jubilant Generics Limited |
| SIN16006P | Alzer 10 (donepezil hydrochloride tablets USP 10 mg) | Film-coated tablet | Hetero Labs Limited |
| SIN15251P | Torpezil tablets 10 mg | Film-coated tablet | Torrent Pharmaceuticals Ltd |
| SIN14389P | Dopezil tablets 10mg | Film-coated tablet | Sun Pharmaceutical Industries Limited |

All listed products are oral formulations.

## Safety Considerations

Please refer to the package insert for safety information. No warnings, contraindications, or drug interaction records were available in the evidence pack.

The retrieved literature raises signals relevant to the predicted uses:
- **Movement-related adverse effects**: A 2025 systematic review ([40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/)) and a case report of donepezil-induced jaw tremor ([18321753](https://pubmed.ncbi.nlm.nih.gov/18321753/)) suggest cholinesterase inhibitors can cause or worsen movement disorders. A pharmacovigilance study ([24127392](https://pubmed.ncbi.nlm.nih.gov/24127392/)) examined Pisa syndrome.
- **Ocular**: A case report describes angle-closure glaucoma after donepezil discontinuation ([16127117](https://pubmed.ncbi.nlm.nih.gov/16127117/)).
- **Pediatric use**: Any use in children (for example, for tics) would need a controlled design and safety monitoring.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction, psychogenic movement disorders, is supported only by the model score. No trials or publications were retrieved, no mechanistic rationale is evident, and the literature for related movement disorders includes a possible harm signal. The 99.23% score does not distinguish it from other predictions in the same narrow score band.

**To proceed, the following is needed:**
- Mechanism of action data (for example, from DrugBank), to assess a link to functional movement disorders
- Package insert warnings and contraindications from HSA, which are currently missing
- A targeted literature and trial search for psychogenic movement disorders
- If resources are limited, consider prioritising chronic tic disorder and glaucoma (both L3), each starting with a controlled study design and a full review of the retrieved records

*This report is for research reference only and does not constitute medical advice. Predicted repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

