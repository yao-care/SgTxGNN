---
layout: default
title: Rabeprazole
parent: Low Evidence (L5)
nav_order: 837
evidence_level: L5
indication_count: 10
---

# Rabeprazole
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

# Rabeprazole: From Acid-Related Gastric Disorders to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor (PPI) used to suppress gastric acid. Its registered indication text is not recorded in the data supplied, so "acid-related gastric disorders" here is inferred from the drug class and the published literature.
The TxGNN model predicts it may be useful in **Smouldering Systemic Mastocytosis**, but this rests on the model score alone, with **0 clinical trials** and **0 publications** retrieved.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data (acid-related gastric disorders, inferred from drug class and literature) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rabeprazole belongs to the PPI class. Its efficacy in acid-related gastric disease is well established in the literature, and it may be applicable to mast-cell-driven acid-related symptoms.

The most plausible link is symptomatic. In systemic mastocytosis, mast cells release histamine, which can drive gastric acid hypersecretion. PPIs are used to control the resulting reflux, gastritis and ulcer symptoms. This would be supportive care, not treatment of the mastocytosis itself, and rabeprazole would not be expected to change the course of the disease.

The high score probably reflects how close the mastocytosis nodes sit to acid-related disease nodes in the knowledge graph, not any direct evidence. The same pattern appears for the neighbouring prediction, lymphadenopathic mastocytosis with eosinophilia (99.35%), which also has no supporting studies.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14910P | Acilesol Gastro-Resistant Tablet 20mg | Tablet, enteric coated | Not listed in the data |
| SIN15259P | Bepraz Gastro Resistant Tablets 20mg | Tablet, delayed release | Not listed in the data |
| SIN15260P | Bepraz Gastro Resistant Tablets 10mg | Tablet, delayed release | Not listed in the data |
| SIN14319P | Rabeprazole Sandoz Gastro Resistant Tablet 20mg | Tablet, enteric coated | Not listed in the data |

All four products are oral tablets.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or literature behind it, and the only mechanistic argument is symptomatic acid control. That would not be disease-modifying in smouldering systemic mastocytosis.

**To proceed, the following is needed:**
- Download and parse the HSA package insert (warnings, contraindications, registered indications). Its absence blocks safety screening.
- Retrieve the mechanism of action from DrugBank.
- Run a targeted literature search on PPI use for GI symptoms in systemic mastocytosis to see whether the supportive-care role is documented.
- Confirm the registered indications of the four Singapore products.
- Review the other predictions in this pack before choosing a lead candidate. Active peptic ulcer disease (98.74%) and gastric ulcer (97.83%) both reach L1 evidence with a "Proceed with Guardrails" recommendation. They are likely existing PPI uses rather than true repurposing, so the labeling should be confirmed first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

