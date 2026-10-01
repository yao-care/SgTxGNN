---
layout: default
title: Artesunate
parent: Low Evidence (L5)
nav_order: 110
evidence_level: L5
indication_count: 10
---

# Artesunate
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

# Artesunate: From Antiparasitic Use to Acne (Disease)

## One-Sentence Summary

Artesunate is an artemisinin-derivative antiparasitic, and it is marketed in Singapore as an injectable powder. The TxGNN model predicts it may be effective for **acne (disease)**, but this is a computational signal only. There are **0 clinical trials** and **0 publications** supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Singapore license data (drug is an antiparasitic artemisinin derivative) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 79.21% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Artesunate is an artemisinin-class antiparasitic. The Singapore license record does not state an approved indication, so the link between its original use and acne cannot be assessed from the supplied data.

The only mechanistic idea is that artesunate is reported to have general anti-inflammatory activity, which could relate to inflammatory skin disease. This was not verified against the supplied data. No mechanism can be tied to acne at this stage, and the prediction rests on the TxGNN score alone.

The other top predictions show the same limits. The mastocytosis entities (ranks 2, 3 and 5) cluster together, which suggests a shared knowledge-graph neighborhood signal rather than independent support. Diffuse cutaneous leishmaniasis (rank 6, score 66.16%) has the most coherent biology, since it is a protozoal disease and artesunate is an antiparasitic. That point is also unverified and needs a targeted literature search.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN17135P | Artesunate Amivas Powder and Solvent for Solution for Injection 110mg/vial | Injection, powder, for solution |

The manufacturer is Dalton Chemical Laboratories Inc. (operating as Dalton Pharma Services). Only an injectable form is registered, and no topical form is registered.

## Safety Considerations

Please refer to the package insert for safety information. The drug interaction query returned no records.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The acne prediction is model output only (L5), with no trials, no literature and no verified mechanism. The only registered product is an injectable, so route compatibility with a skin indication is also unresolved.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on artesunate in acne and inflammatory skin disease
- A route compatibility assessment (injectable only vs. any topical or oral need)
- A separate literature check on artesunate against *Leishmania*, since diffuse cutaneous leishmaniasis (rank 6) is flagged as a research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

