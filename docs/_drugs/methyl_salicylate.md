---
layout: default
title: Methyl Salicylate
parent: Low Evidence (L5)
nav_order: 661
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Methyl Salicylate: predicted new indication Gout (evidence level L5). Approved use: Not specified"
monitor_inn: "Methyl salicylate"
predicted_indications: ["gout", "bronchitis", "exostosis", "congestive heart failure", "osteoarthritis susceptibility", "osteoarthritis", "acute pulmonary heart disease", "pseudoachondroplasia", "rheumatoid arthritis", "exostoses, multiple,"]
---

# Methyl Salicylate
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

# Methyl Salicylate: From an Unspecified Topical Indication to Gout

## One-Sentence Summary

Methyl salicylate is a topical salicylate counter-irritant. It is registered in Singapore as a lotion, but no approved indication text was recorded.
The TxGNN model ranks **gout** as its top predicted new indication, with **no registered clinical trials** and only **1 publication**, which is a plant biology study unrelated to gout in humans.
This prediction is model-based only. The better-supported alternative among the top 10 predictions is osteoarthritis (symptomatic topical use), but the evidence there is also limited and partly indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not specified (the approved indication text on the Singapore licence is blank) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 98.86% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methyl salicylate is a salicylate that is hydrolysed to salicylic acid after dermal absorption. Salicylic acid inhibits COX enzymes and has anti-inflammatory activity, so in principle it could relieve inflammatory pain such as gouty inflammation.

However, the single publication retrieved for gout (PMID 26042139) is a study of volatile compounds in grapevine and has no bearing on human gout. The high TxGNN score therefore reflects a knowledge-graph association only, with no clinical support.

For context, the other nine top predictions are also weak. Osteoarthritis (rank 6) and rheumatoid arthritis (rank 9) are biologically plausible for symptomatic relief, but their evidence is mostly indirect or preclinical. Several predictions (exostosis, pseudoachondroplasia, multiple exostoses, acute pulmonary heart disease) have no evidence or plausible mechanism. For congestive heart failure, salicylates and NSAIDs may cause fluid retention and worsen the condition, so the direction of effect is potentially harmful.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26042139](https://pubmed.ncbi.nlm.nih.gov/26042139/) | 2015 | Plant biology (not clinical) | Frontiers in Plant Science | Volatile compounds as markers of defence elicitation in grapevine. Not relevant to gout. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN08677P | Robinson Ringworm and Whitespot Lotion | Lotion | Not recorded |

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** The TxGNN knowledge graph links methyl salicylate with contraindications in the following conditions. These are not drawn from the package insert and should be verified against it:
  - Liver and kidney disease, including liver failure
  - Gastrointestinal disease, such as gastritis, active peptic ulcer disease, gastroesophageal reflux disease and esophagitis
  - Bleeding and blood disorders, such as blood coagulation disease, haemophilia, anaemia and thrombocytopenic purpura
  - Cardiovascular disease, including heart disease, heart conduction disease and sudden cardiac arrest
  - Respiratory failure
  - Diabetes mellitus and diabetic ketoacidosis
  - Thyroid disease, such as hyperthyroidism, thyrotoxicosis and Graves disease
  - Epilepsy
  - Skin conditions, such as skin disease, actinic keratosis and seborrheic keratosis
  - Others: gallbladder disease, pyoureter and nasal cavity polyp
- **Drug interactions:** No interaction records were found. One review (PMID 8672833) discusses warfarin–NSAID interactions, which is a class-level concern for salicylates.

For label-based warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The gout prediction rests entirely on the model score. No trials exist, and the only retrieved paper is unrelated plant research. Salicylate anti-inflammatory activity makes a symptomatic benefit conceivable, but nothing supports it.

**To proceed, the following is needed:**
- The package insert for the Singapore product, to confirm approved indications, warnings and contraindications
- Mechanism of action data from DrugBank
- A targeted literature search on topical salicylates in gout, with human clinical data
- Consideration of osteoarthritis (symptomatic topical use) as a more evidence-supported research question than gout. It currently sits at L3 with limited, partly indirect evidence.
- Confirmation that the route of administration (topical lotion) suits the target condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

