---
layout: default
title: Anidulafungin
parent: Low Evidence (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Anidulafungin: predicted new indication Impetigo (evidence level L5). Approved use: Esophageal candidiasis, candidemia"
monitor_inn: "Anidulafungin"
predicted_indications: ["impetigo", "malignant pleural mesothelioma", "staphylococcal scalded skin syndrome", "pleural empyema (disease)", "malignant visceral pleura tumor", "bullous impetigo", "malignant epithelioid mesothelioma", "sarcomatoid mesothelioma", "hordeolum", "Clostridium infectious disease"]
---

# Anidulafungin
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

# Anidulafungin: From Esophageal Candidiasis to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal, originally used to treat esophageal candidiasis and candidemia.
The TxGNN model predicts it may be effective for **impetigo** (score 98.9%), but **no clinical trials and no publications** currently support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Anidulafungin belongs to the echinocandin class, which inhibits beta-(1,3)-D-glucan synthase, an enzyme needed for the fungal cell wall. Its efficacy against invasive *Candida* infections is established.

Impetigo is a skin infection caused mainly by *Staphylococcus aureus* and *Streptococcus pyogenes*. These are bacteria with no beta-glucan cell wall, and anidulafungin has no antibacterial activity. **No plausible mechanistic link was identified**, so the high TxGNN score should be read as a computational association only, not as pharmacological support.

Other top-ranked predictions show the same pattern. Bullous impetigo, staphylococcal scalded skin syndrome, hordeolum and Clostridium infections are bacterial. Several mesothelioma subtypes would require an unknown off-target anti-tumour effect. Pleural empyema is the only prediction with a related publication, a pharmacokinetic study of drug penetration into pleural fluid. It shows distribution, not efficacy, and most empyema is bacterial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for impetigo.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN16803P | Anidulafungin Fresenius Kabi Powder for Concentrate for Solution for Infusion 100mg/vial | Injection, powder, lyophilized, for solution | Not stated in the data |
| SIN13585P | Eraxis 100mg For Injection | Injection, powder, lyophilized, for solution | Not stated in the data |
| SIN16106P | Anidaccord 100 Powder for Concentrate for Solution for Infusion 100 mg | Injection, powder, for solution | Not stated in the data |

All three are single-ingredient, valid registrations, and all are injectable. An intravenous-only product is a practical limitation for a superficial skin infection such as impetigo.

## Safety Considerations

- **Disease associations in the knowledge graph**: liver disease and gallbladder disease are flagged as contraindication-related. These come from a knowledge graph, not from label text, and should be verified against the package insert.
- **Drug Interactions**: One interaction is recorded, with **cyclosporine** (Minor severity).

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for impetigo is supported only by the model score. There are no clinical trials or publications, and the causative organisms are bacteria that anidulafungin does not target. The same holds for the other top-ranked predictions, none of which has efficacy evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are a blocking gap for safety screening
- Mechanism of action data from DrugBank
- Any in vitro or in vivo evidence of activity against the relevant pathogens, or a credible off-target mechanism
- Assessment of route compatibility, since only intravenous products are registered in Singapore
- Reconsideration of the target indication. If repurposing is pursued, pleural empyema, the only prediction with related literature, could be explored for fungal causes, starting with efficacy data beyond pharmacokinetics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

