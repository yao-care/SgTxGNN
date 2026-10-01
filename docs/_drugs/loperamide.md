---
layout: default
title: Loperamide
parent: Low Evidence (L5)
nav_order: 606
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a peripheral opioid antidiarrheal that slows gut motility and reduces secretion, and it is marketed in Singapore mainly as capsules and syrup.
The TxGNN model predicts it may be effective for **acute contagious conjunctivitis** with a very high score (99.97%), but **no clinical trials and no publications** support this prediction.
The score most likely reflects proximity in the knowledge graph rather than a pharmacological rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Diarrhea (antidiarrheal use; the registry extract gives no indication text) |
| Predicted New Indication | Acute contagious conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 10 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Loperamide is known as a peripheral mu-opioid receptor agonist that acts on gut motility and secretion, and its efficacy in diarrhea is well established.

There is no plausible mechanistic link between a gut-acting opioid antidiarrheal and infection or inflammation of the ocular surface. The high score (rank 878 in the model output) is most likely explained by neighborhood proximity to other conjunctivitis nodes in the knowledge graph. The same pattern appears in the sibling predictions (pseudomembranous, chronic follicular, parasitic, serous conjunctivitis and others), which share identical or near-identical scores.

## Clinical Trial Evidence

Currently no related clinical trials registered for acute contagious conjunctivitis.

For reference, the broader "conjunctivitis" prediction matched two azithromycin trachoma trials (NCT04185402 and NCT06289647). Loperamide is not an intervention in either, so they provide no evidence for this drug.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN05587P | VACONTIL CAPSULE 2 mg | Capsule |
| SIN06525P | LORPA SYRUP 1mg/5ml | Syrup |
| SIN05595P | LOPERAX CAPSULE 2 mg | Capsule |
| SIN06212P | IMODIUM CAPSULE 2 mg | Capsule |
| SIN16450P | ABYDIUM CAPSULES 2MG | Capsule |

Only 5 of the 10 registrations are shown. No topical or ophthalmic formulation is registered, so the available forms (oral capsule and syrup) do not match the route needed for an ocular indication.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. It is very likely a graph artifact, and there is no reason to spend resources on it.

**To proceed, the following is needed:**
- A pharmacological rationale for a gut-acting opioid in conjunctival disease, and detailed mechanism of action data
- Any preclinical or clinical study of loperamide in conjunctivitis
- The HSA package insert warnings and contraindications for a safety screen
- A suitable ocular formulation, since none is registered in Singapore

**Other predictions in the pack:**
- **Gastroduodenitis** is the only one with a literature signal: a 1986 non-English clinical report of Imodium in peptic ulcer and chronic gastroduodenitis. Its design and outcomes are unconfirmed, so it is worth verifying as a research question.
- **Amebic dysentery** points to a safety concern rather than a benefit: a case report links heavy loperamide use to fulminant amoebic colitis. It is not a viable candidate.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

