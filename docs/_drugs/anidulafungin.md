---
layout: default
title: Anidulafungin
parent: Low Evidence (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Anidulafungin: From Fungal Infection to Impetigo

## One-Sentence Summary

Anidulafungin is an echinocandin antifungal that inhibits fungal beta-1,3-D-glucan synthase. The TxGNN model predicts it may be effective for **impetigo** (score 98.85%), but there are currently **0 clinical trials** and **0 publications** supporting this direction. Impetigo is a bacterial infection, and anidulafungin has no known antibacterial activity, so this looks like a model artifact rather than a real repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore licence data. The known class use is antifungal (Candida infections), which I have not verified against the label. |
| Predicted New Indication | Impetigo |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known class pharmacology, anidulafungin is an echinocandin that blocks fungal beta-1,3-D-glucan synthase, a key enzyme in building the fungal cell wall. It is active against Candida.

Impetigo is caused by *Staphylococcus aureus* or *Streptococcus pyogenes*. Bacteria have no glucan cell wall, so the drug's target does not exist in the causative organisms. No plausible mechanistic link between the original use and the predicted one was found, and the prediction is unsupported by biology.

A high TxGNN score reflects proximity in the knowledge graph, not proof of efficacy. Here, the score alone should not be read as a signal worth pursuing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN13585P | Eraxis 100mg For Injection | Lyophilized powder for injection | Pharmacia and Upjohn Company LLC |
| SIN16106P | ANIDACCORD 100 Powder for Concentrate for Solution for Infusion 100 mg | Powder for injection | SIA Pharmidea / Laboratorios Alcalá Farma, S.L. |
| SIN16803P | Anidulafungin Fresenius Kabi Powder for Concentrate for Solution for Infusion 100mg/vial | Lyophilized powder for injection | Mefar Ilac Sanayii A.S. |

All three products are injectables. The approved indication text is not recorded in the data received.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5) with no trials or literature. The drug's known target is absent in the bacteria that cause impetigo, so there is no mechanistic basis for pursuing it. The other top-10 predictions (mesothelioma cluster, staphylococcal scalded skin syndrome, bullous impetigo, hordeolum, *Clostridium* infection) also lack a mechanistic rationale, and each is rated Hold. The only exception is pleural empyema. It is rated L4 as a research question, based on a 2018 PK study showing some pleural fluid penetration in critically ill patients. That study shows exposure, not efficacy, and any plausible role is limited to fungal empyema.

**To proceed, the following is needed:**
- Any evidence of antibacterial or anti-inflammatory activity against *S. aureus* or *S. pyogenes*, which is unlikely given the drug's class
- Approved indication text and package insert safety information (warnings, contraindications) from the HSA
- DrugBank mechanism of action data
- If a lead is wanted from this drug's predictions, a separate assessment of fungal pleural empyema is the more defensible candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

