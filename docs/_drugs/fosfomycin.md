---
layout: default
title: Fosfomycin
parent: Low Evidence (L5)
nav_order: 453
evidence_level: L5
indication_count: 8
monitor_inn: "Fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "pyelitis"]
last_modified_at: 2026-10-28
description: "Fosfomycin: predicted new indication Uterine inflammatory disease (evidence level L5). Approved use: Urinary tract infection"
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fosfomycin: From Urinary Tract Infection to Uterine Inflammatory Disease
{: .text-alpha }

## One-Sentence Summary

Fosfomycin is an antibiotic. The TxGNN model (deep learning) predicts it may help with **uterine inflammatory disease** (score 0.9998), but the support is thin. There are **2 registered clinical trials**, both general pediatric pharmacokinetic studies, and **1 publication**, which is about cystitis rather than uterine disease. This prediction rests mainly on the model score, which may reflect similarities the model learned between related diseases, not biological evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (a relation recorded in the knowledge graph; the local licence record gives no approved indication text) |
| Predicted New Indication | Uterine inflammatory disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Licences | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not included in the data compiled for this report. Fosfomycin is generally known to inhibit MurA (UDP-N-acetylglucosamine enolpyruvyl transferase). This blocks an early step of bacterial cell wall (peptidoglycan) synthesis and gives broad activity against Gram-negative and Gram-positive urinary pathogens.

Uterine inflammatory conditions such as endometritis or pelvic inflammatory disease are often bacterial. A drug with broad antibacterial activity could therefore plausibly act on them. This is a mechanistic guess only. No cited study tests fosfomycin for endometritis or pelvic inflammatory disease. The only linked paper concerns cystitis, which is a urinary condition and not uterine disease.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pharmacokinetics of understudied drugs given to children as standard of care. Not specific to uterine inflammatory disease, and no efficacy data. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | Multi-drug pharmacokinetic, pharmacodynamic and safety platform study in children and young adults. Not indication-specific, and no efficacy data. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohort | J Obstet Gynaecol | Compared acute cystitis symptoms and bacteriuria in women with endometriosis who took dienogest or combined oral contraceptives after laparoscopic surgery. It does not evaluate fosfomycin as a treatment for uterine inflammatory disease. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11013P | MONUROL SACHET 3 g/sachet (Zambon Switzerland Ltd) | Granule, for suspension | Not stated in the licence record |

## Safety Considerations

- **Contraindication relations in the knowledge graph** (not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, and perinatal necrotizing enterocolitis.
- **Drug Interactions** (3 found):
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The model score is very high, but no cited study directly examines fosfomycin in uterine inflammatory disease. The two trials are general pediatric pharmacokinetic studies, and the single paper concerns cystitis. The mechanism is plausible, but there is no clinical evidence for this indication, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical or microbiological studies of fosfomycin in endometritis or pelvic inflammatory disease, covering pathogen coverage and tissue penetration in the genital tract
- Package insert warnings and contraindications from the Singapore Health Sciences Authority (HSA) record, and the approved indication text for the local licence
- Detailed mechanism-of-action data
- A review of whether the available dosage form and route suit the target condition
- Comparison against standard regimens for uterine infections
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

