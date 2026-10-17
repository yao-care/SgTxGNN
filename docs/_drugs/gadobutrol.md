---
layout: default
title: Gadobutrol
parent: Low Evidence (L5)
nav_order: 462
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Gadobutrol: predicted new indication Benign prostatic hyperplasia (evidence level L5). Approved use: Not stated in the Singapore licence text (the drug is an MRI contrast…"
monitor_inn: "Gadobutrol"
predicted_indications: ["benign prostatic hyperplasia (disease)", "peripheral arterial disease", "cauda equina syndrome", "peripheral vascular disease", "strongyloidiasis", "prostate calculus", "obsolete neurogenic bladder (disease)", "iritis (disease)", "hypertrichosis (disease)", "disease of orbital region"]
---

# Gadobutrol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Gadobutrol: From MRI Contrast Imaging to Peripheral Arterial Disease (Diagnostic Use)

## One-Sentence Summary

Gadobutrol is a gadolinium-based MRI contrast agent, marketed in Singapore as Gadovist, and used for diagnostic imaging rather than treatment.
The TxGNN model's top-ranked prediction is benign prostatic hyperplasia, but this has no supporting evidence. The best-supported direction is **peripheral arterial disease**, as a diagnostic (contrast-enhanced MR angiography) use, with **1 clinical trial** and **13 publications** compiled for this report.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore licence text (the drug is an MRI contrast agent) |
| Predicted New Indication | Benign prostatic hyperplasia (TxGNN rank 1); peripheral arterial disease (rank 2) is the best-supported alternative |
| TxGNN Prediction Score | 83.24% (benign prostatic hyperplasia); 76.72% (peripheral arterial disease) |
| Evidence Level | L5 (benign prostatic hyperplasia); L1 (peripheral arterial disease, diagnostic comparative studies) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold (benign prostatic hyperplasia); Proceed with Guardrails (peripheral arterial disease, diagnostic use only) |

**Note:** The highest-scoring prediction is not the one with evidence. Because the rank-1 prediction has no trials or literature, the sections below focus on peripheral arterial disease (rank 2), which is the first prediction with real supporting studies. The related prediction of peripheral vascular disease (rank 4) draws on largely the same studies.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the data compiled for this report. Based on known information, gadobutrol is an extracellular gadolinium-based contrast agent. Its paramagnetic gadolinium chelate shortens T1 relaxation time, which brightens blood vessels on MRI. It has no known pharmacological target and is not a therapeutic.

For peripheral arterial disease, the "indication" is therefore diagnostic: contrast-enhanced MR angiography (CE-MRA) to detect narrowing or blockage of leg and pelvic arteries. The 1.0 M formulation gives a compact contrast bolus with high T1 relaxivity, which supports high-quality angiography, including moving-table and time-resolved techniques. This explains why many imaging studies have used gadobutrol in this setting. It is not a therapeutic repurposing.

The other predictions are not supported. Benign prostatic hyperplasia, cauda equina syndrome, strongyloidiasis, prostate calculus, neurogenic bladder (an obsolete ontology term), iritis, hypertrichosis and orbital disease have no trials or literature. For each, the model score most likely reflects network-proximity artefacts in the knowledge graph rather than real biology.

---

## Clinical Trial Evidence

(For peripheral arterial disease)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01026389](https://clinicaltrials.gov/study/NCT01026389) | Phase 4 | Completed | 189 | Dotarem-enhanced MRA compared with Gadovist (gadobutrol)-enhanced MRA for diagnosing abdominal or lower-limb arterial disease. Gadobutrol served as the comparator. |

No clinical trials were registered for the other nine predicted indications.

---

## Literature Evidence

(For peripheral arterial disease and peripheral vascular disease)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26001243](https://pubmed.ncbi.nlm.nih.gov/26001243/) | 2015 | RCT | AJR Am J Roentgenol | Large randomized noninferiority comparison of gadoterate vs gadobutrol for 3 T MRA in peripheral arterial occlusive disease, with DSA as the reference |
| [22848033](https://pubmed.ncbi.nlm.nih.gov/22848033/) | 2012 | RCT | J Magn Reson Imaging | Randomized, crossover, double-blind comparison of 0.5 M gadoterate and 1.0 M gadobutrol for peripheral MRA at 3 T |
| [18504760](https://pubmed.ncbi.nlm.nih.gov/18504760/) | 2008 | RCT | J Magn Reson Imaging | Prospective randomized trial comparing 1.0 M gadobutrol with 0.5 M gadoterate in three-station lower-limb CE-MRA |
| [12928960](https://pubmed.ncbi.nlm.nih.gov/12928960/) | 2003 | Prospective multicentre study | Eur Radiol | 203 patients; gadobutrol moving-table MRA compared with intra-arterial DSA, blinded readers |
| [23188773](https://pubmed.ncbi.nlm.nih.gov/23188773/) | 2013 | Prospective diagnostic accuracy study | J Magn Reson Imaging | Multi-station high-resolution CE-MRA compared with DSA in the lower extremity |
| [21031523](https://pubmed.ncbi.nlm.nih.gov/21031523/) | 2010 | Prospective comparative study | J Magn Reson Imaging | Gadobenate dimeglumine 0.5 M vs gadobutrol 1.0 M in run-off MRA: image quality and diagnostic accuracy |
| [24893292](https://pubmed.ncbi.nlm.nih.gov/24893292/) | 2014 | Comparative clinical study | PLoS One | Gadoterate vs gadobutrol at equimolar doses for time-resolved 3 T MRA of the calf |
| [12928957](https://pubmed.ncbi.nlm.nih.gov/12928957/) | 2003 | Safety study | Eur Radiol | Safety of 1.0 M gadobutrol in CE-MRA across 435 patients in three multicentre trials |
| [15280530](https://pubmed.ncbi.nlm.nih.gov/15280530/) | 2004 | Randomized clinical study | Nephrol Dial Transplant | Gadobutrol vs iodinated contrast (iohexol) for angiography in patients with reduced renal function; renal function assessed after exposure |
| [15149986](https://pubmed.ncbi.nlm.nih.gov/15149986/) | 2004 | Clinical study | AJR Am J Roentgenol | Whole-body 3D MRA with gadobutrol in 51 patients compared with DSA |

Further studies (for example PMIDs 19652610, 24156379 and 12677513) address the same imaging question. The compiled data also include one swine-model study (PMID 22543971).

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12399P | GADOVIST INJECTION 1.0 mmol/ml (Bayer AG) | Injection | Not stated in the data compiled |
| SIN13807P | GADOVIST 1MMOL/ML PREFILLED SYRINGE 5.0 ML (Bayer AG) | Injection | Not stated in the data compiled |

Both licences are valid single-ingredient products, given by injection.

---

## Safety Considerations

- **Drug Interactions:** 25 interactions were identified in total (source: DDInter). The 20 listed in the data compiled for this report are all rated Moderate, and all are beta-blockers: acebutolol, atenolol, betaxolol (including ophthalmic), bisoprolol, carteolol (including ophthalmic), carvedilol, esmolol, labetalol, levobunolol (ophthalmic), metipranolol (ophthalmic), metoprolol, nadolol, nebivolol, pindolol, propranolol, sotalol and timolol (including ophthalmic).
- **Gadolinium class precautions (from the study data and standard class knowledge, not label text):** renal function screening is advisable before use, with attention to the risk of nephrogenic systemic fibrosis (NSF) in severe renal impairment and to gadolinium retention.

For warnings and contraindications, please refer to the package insert, as this information was not available for this report.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails (peripheral arterial disease / peripheral vascular disease, diagnostic use only). Hold (all other predictions, including benign prostatic hyperplasia).**

**Rationale:**
- Peripheral arterial disease has a completed Phase 4 trial and several randomized comparative studies of gadobutrol-enhanced MRA (L1). However, this grade reflects diagnostic comparisons, not therapeutic Phase 3 RCTs, and gadobutrol already serves as a standard MRA contrast agent. This is a diagnostic use rather than a new treatment.
- The remaining eight predictions, including the top-ranked benign prostatic hyperplasia (83.24%), have no trials, no literature and no plausible mechanism (L5). They look like model artefacts.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking safety data gap)
- The approved indication text for both Singapore licences, to confirm whether MR angiography is already covered
- Mechanism of action data (a data gap, although the contrast mechanism is well understood)
- Confirmation of renal function screening and gadolinium safety procedures for angiography use
- No further work is suggested for the L5 predictions unless new evidence appears
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

