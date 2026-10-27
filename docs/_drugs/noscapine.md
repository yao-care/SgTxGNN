---
layout: default
title: Noscapine
parent: Low Evidence (L5)
nav_order: 726
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Noscapine: predicted new indication Scalp dermatosis (evidence level L5). Approved use: Cough"
monitor_inn: "Noscapine"
predicted_indications: ["scalp dermatosis", "renin-angiotensin-aldosterone system-blocker-induced angioedema", "rheumatoid arthritis", "atopic eczema", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "nephrotic syndrome", "brachydactyly-syndactyly syndrome", "eye disease", "autoimmune hemolytic anemia", "recurrent idiopathic neuroretinitis"]
---

# Noscapine
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

## Noscapine: From Cough Suppression to Scalp Dermatosis
{: .text-alpha }

## One-Sentence Summary

Noscapine is an antitussive (cough suppressant) marketed in Singapore as a single-ingredient cough syrup and lozenge.
The TxGNN model predicts it may be effective for **scalp dermatosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction, so it rests on computational prediction alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cough (antitussive use; the registered indication text is blank in the licence records) |
| Predicted New Indication | Scalp dermatosis |
| TxGNN Prediction Score | 98.52% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Noscapine is generally known as an antitussive acting through sigma-receptors, and it also has tubulin-binding, antimitotic properties. However, nothing in the compiled data connects these properties to scalp dermatosis.

The link between a symptomatic cough medicine and a skin condition of the scalp is not obvious. The high TxGNN score is a computational prediction, likely reflecting proximity in the knowledge graph rather than a demonstrated biological relationship. Further biological rationale would be needed before this prediction can be considered credible.

Other predicted indications were also reviewed, and all share the same evidence level (L5):

| Rank | Predicted Indication | Score | Evidence |
|------|------|------|------|
| 2 | RAAS-blocker-induced angioedema | 98.44% | No trials or literature |
| 3 | Rheumatoid arthritis | 97.13% | No trials or literature |
| 4 | Atopic eczema | 96.20% | No trials or literature |
| 5 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 95.57% | No trials or literature |
| 6 | Nephrotic syndrome | 95.41% | No trials or literature |
| 7 | Brachydactyly-syndactyly syndrome | 95.37% | No trials or literature |
| 8 | Eye disease | 95.19% | 2 publications, neither providing clinical evidence |
| 9 | Autoimmune haemolytic anaemia | 95.05% | No trials or literature |
| 10 | Recurrent idiopathic neuroretinitis | 95.04% | No trials or literature |

For eye disease, a 1999 review discusses sigma-receptors in cough, gastrointestinal and retinal function. This offers only a hypothetical mechanistic link. The other retrieved paper is a 1962 antitussive comparison and is not relevant to eye disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top predicted indication (scalp dermatosis). The only publications retrieved relate to the rank 8 prediction (eye disease):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10562963](https://pubmed.ncbi.nlm.nih.gov/10562963/) | 1999 | Review | Nihon Yakurigaku Zasshi | Overview of sigma-receptor roles in cough reflex, gastrointestinal and retinal function; sigma-receptor ligands reduced cough in a dose-dependent manner |
| [13864787](https://pubmed.ncbi.nlm.nih.gov/13864787/) | 1962 | Experimental/Preclinical | Praxis | Double-blind comparison of the antitussive effects of noscapine hydrochloride and dihydrocodeine bitartrate; not relevant to eye disease |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09666P | TONIN COUGH SYRUP S | Syrup | Not stated in the licence record |
| SIN04537P | NEW TONIN TROCHE L | Lozenge | Not stated in the licence record |

Both licences are valid single-ingredient products from Sato Pharmaceutical Co Ltd.

---

## Safety Considerations

Please refer to the package insert for safety information.

The knowledge graph (not label text) links noscapine to contraindication edges for the following conditions. These are not confirmed label contraindications and should be verified against the package insert:

- **Cardiovascular:** hypertension, myocardial infarction, coronary thrombosis, pulmonary oedema, cor pulmonale
- **Endocrine and metabolic:** hypothyroidism, myxoedema, congenital hypothyroidism, hyperthyroidism, Graves disease, thyrotoxicosis, diabetes mellitus, diabetic ketoacidosis
- **Hepatic, gastrointestinal and other:** liver disease, gallbladder disease, peptic ulcer disease, epilepsy, substance abuse/dependence, haemoglobinopathy, multiple organ dysfunction syndrome, cystic fibrosis

No drug interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for scalp dermatosis is supported only by a model score, with no clinical trials, no publications and no identified mechanistic link. Label safety data are also missing, so the evidence is insufficient to advance.

**To proceed, the following is needed:**
- Mechanism of action data for noscapine, and a plausible biological rationale linking it to scalp dermatosis
- Preclinical or clinical evidence (literature and trial searches targeted at the predicted indication)
- Package insert warnings and contraindications from HSA, to allow safety screening
- Route compatibility assessment, since the available oral forms (syrup, lozenge) may not suit a scalp condition
- Review of the knowledge-graph contraindication signals against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

