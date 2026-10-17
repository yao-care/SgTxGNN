---
layout: default
title: Cyclizine
parent: Low Evidence (L5)
nav_order: 284
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cyclizine: predicted new indication Allergic urticaria (evidence level L5). Approved use: Motion sickness, allergic rhinitis, vasomotor rhinitis, pharyngitis…"
monitor_inn: "Cyclizine"
predicted_indications: ["allergic urticaria", "nasal cavity disease", "cold urticaria", "rosacea conjunctivitis", "headache disorder", "trigeminal autonomic cephalalgia", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
---

# Cyclizine
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

# Cyclizine: From Motion Sickness and Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cyclizine is a first-generation antihistamine with anticholinergic activity, originally used for motion sickness and upper-airway and eye allergic conditions such as allergic rhinitis and conjunctivitis.
The TxGNN model predicts it may be effective for **allergic urticaria**,
but currently there are **0 clinical trials** and **no directly relevant publications** supporting this direction, so the prediction is based on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Motion sickness, allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, conjunctivitis (atopic, papillary, vernal), nasopharyngitis (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Allergic urticaria |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from the data compiled for this report. Based on known information, cyclizine belongs to the first-generation H1 antihistamine class with anticholinergic properties. Its efficacy in allergic rhinitis and conjunctivitis is established, and mechanistically it may be applicable to histamine-mediated skin conditions.

Allergic urticaria is driven largely by histamine release, and H1 blockade is the standard symptomatic approach. This is the same pathway that underlies cyclizine's existing allergic indications, so the prediction is biologically plausible.

There are important caveats. The score of 99.98% is a computational prediction only, and no cyclizine-specific studies for urticaria were found. Current practice generally favours second-generation antihistamines over sedating first-generation agents like cyclizine because of better tolerability.

Other predictions in the top 10 are less compelling:
- **Rhinitis, acute laryngopharyngitis, nasal cavity disease**: these overlap with existing labelled indications, so they are not true repurposing opportunities.
- **Cold urticaria**: the mechanism is plausible, but second-generation agents are preferred.
- **Rosacea conjunctivitis, recalcitrant atopic dermatitis, atopic IgE responsiveness**: the mechanistic link is weak or speculative.
- **Trigeminal autonomic cephalalgia**: there is no clear mechanistic rationale.
- **Headache disorder**: an antiemetic adjunct role for nausea in migraine is plausible, but see the literature section below.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature is available for the top prediction (allergic urticaria). Two publications were returned for the sixth-ranked prediction, headache disorder, but they are indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3926322](https://pubmed.ncbi.nlm.nih.gov/3926322/) | 1985 | RCT | Cephalalgia | Randomised trial (114 patients) comparing naproxen sodium with an ergotamine combination for acute migraine attacks. The ergotamine product contained 50 mg cyclizine, but cyclizine was not evaluated on its own. |
| [20420788](https://pubmed.ncbi.nlm.nih.gov/20420788/) | 2010 | Cohort (database analysis) | Int J Clin Pharmacol Ther | Pharmacy database analysis of migraine prescribing patterns and cost, focusing on triptans. Does not appear to evaluate cyclizine. |

Neither publication directly supports cyclizine for headache disorder, and this judgement is based on titles and abstracts only.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15193P | NAUSICALM TABLET 50MG | Tablet | Not stated in the compiled records |
| SIN15353P | NAUSICALM TABLET 50MG (PHARMACY ONLY) | Tablet | Not stated in the compiled records |

Both licences are valid single-ingredient oral tablets.

---

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: The TxGNN knowledge graph links cyclizine to contraindication with the following conditions, which should be verified against the package insert:
  - Cardiovascular: hypertension, hypotension, coronary artery disease, myocardial infarction, atherosclerosis
  - Neurological: epilepsy
  - Renal and urinary: kidney disease, benign prostatic hyperplasia, pyoureter
  - Hepatic, biliary and pancreatic: liver disease, gallbladder disease, pancreatitis
  - Gastrointestinal: peptic ulcer disease, inflammatory bowel disease, *Clostridium difficile* colitis, necrotizing enterocolitis
  - Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, adrenocortical insufficiency, hypothyroidism
  - Haematological: hemoglobinopathy
  - Ocular: ocular hypertension
- **Drug Interactions**: 100 interactions were recorded. Examples shown:
  - **Major**: potassium citrate, potassium chloride
  - **Moderate**: anticholinergics (atropine, hyoscyamine, scopolamine, glycopyrronium, dicyclomine, trospium, propantheline), opioids and related agents (morphine, opium, loperamide, eluxadoline), cannabinoids (dronabinol, nabilone), and gastrointestinal motility agents (metoclopramide, prucalopride)

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The H1-blockade mechanism makes allergic urticaria plausible, but the prediction rests on a computational score alone with no cyclizine-specific trials or literature (Evidence Level L5). Second-generation antihistamines are already preferred for urticaria, and the long list of knowledge-graph contraindications and interactions calls for caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA (currently a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A systematic search for cyclizine-specific studies in urticaria, including comparison against second-generation antihistamines
- A risk-benefit assessment of sedation and anticholinergic effects compared with current standard therapy
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

