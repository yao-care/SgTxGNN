---
layout: default
title: Pemigatinib
parent: Low Evidence (L5)
nav_order: 765
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: From FGFR-Targeted Cancer Therapy to Multiple Endocrine Neoplasia

## One-Sentence Summary

Pemigatinib is an oral, selective FGFR1-3 inhibitor marketed in Singapore as Pemazyre tablets.
The TxGNN model predicts it may be effective for **multiple endocrine neoplasia (MEN)**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records |
| Predicted New Indication | Multiple endocrine neoplasia |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Pemigatinib is a selective inhibitor of FGFR1, FGFR2 and FGFR3. Detailed mechanism-of-action data is not available in the source data. The FGFR-inhibitor description comes from the mechanistic assessment in the Evidence Pack.

The link to the predicted indication is weak. MEN syndromes are driven mainly by MEN1 and RET alterations, and no direct FGFR-driven mechanism is established for them. The high score (0.997, model rank 4529) is a statistical output of the knowledge graph. It has not been confirmed by any trial, publication or preclinical study.

Other high-scoring predictions for this drug raise further doubts about the model output:
- **Veterinary diseases** (infectious bovine rhinotracheitis, malignant catarrhal fever) are likely knowledge-graph artifacts and are not human indications.
- **Three overlapping ALS entries** should be read as a single signal. FGF signalling is generally neurotrophic, so FGFR inhibition could be neutral or harmful.
- **Amenorrhea** appears to have the opposite direction of effect. FGFR1 signalling supports GnRH neuron development, so FGFR inhibition is more likely to disturb the reproductive axis than to treat amenorrhea.
- **HER2-positive breast carcinoma** is the only prediction with a plausible mechanism, because FGFR pathway alterations have been discussed as resistance or co-drivers. The one retrieved paper is a general kinase-inhibitor review with no pemigatinib efficacy data, so this remains a research question.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN17042P | PEMAZYRE TABLETS 4.5 MG | Tablet | Lonza Tampa LLC |
| SIN17043P | PEMAZYRE TABLETS 9 MG | Tablet | Lonza Tampa LLC |
| SIN17044P | PEMAZYRE TABLETS 13.5 MG | Tablet | Lonza Tampa LLC |

The registration records do not include approved indication text. All three products are oral tablets.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

The classification is inferred from the drug class. The Evidence Pack contains no DrugBank toxicity data.

---

## Safety Considerations

Please refer to the package insert for safety information.

The drug-interaction query returned no records. This means no data was found, not that no interactions exist.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.71% TxGNN score for multiple endocrine neoplasia is not supported by any trial, publication or established mechanism. MEN is driven mainly by MEN1 and RET, not FGFR. The evidence level is L5 (model prediction only), and the safety package is incomplete.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence linking FGFR signalling to MEN pathology
- Mechanism of action data from DrugBank
- HSA package insert warnings and contraindications, which block safety screening
- Approved indication text for the Singapore registrations
- Separate follow-up on HER2-positive breast carcinoma (FGFR as a resistance pathway) as a more plausible research question

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

