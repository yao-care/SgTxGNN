---
layout: default
title: Erdafitinib
parent: Low Evidence (L5)
nav_order: 386
evidence_level: L5
indication_count: 10
---

# Erdafitinib
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

# Erdafitinib: From Urothelial Carcinoma to Pulmonary Hypertension

## One-Sentence Summary

Erdafitinib is an oral FGFR kinase inhibitor, originally used to treat FGFR-altered urothelial carcinoma.
The TxGNN model predicts it may be effective for **pulmonary hypertension**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urothelial carcinoma with FGFR alterations (from general drug knowledge; the Singapore registration records contain no indication text) |
| Predicted New Indication | Pulmonary hypertension |
| TxGNN Prediction Score | 99.38% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. From general drug knowledge, erdafitinib is a pan-FGFR (FGFR1-4) tyrosine kinase inhibitor. Its efficacy in FGFR-driven urothelial cancer is established.

FGF/FGFR signalling has been implicated in pulmonary vascular remodelling, which is a core feature of pulmonary hypertension. This makes the link biologically plausible. However, there is no clinical or preclinical evidence for erdafitinib specifically. FGF signalling may also be protective in the pulmonary vasculature, so FGFR inhibition could be harmful rather than helpful. The high TxGNN score reflects knowledge-graph proximity, not proof of benefit.

Other top-ranked predictions are weaker:
- **Rheumatoid arthritis** (score 99.25%) is the only other candidate with any literature. That is a general review of FDA-approved kinase inhibitors with no RA-specific erdafitinib data (Evidence Level L4).
- **Amyotrophic lateral sclerosis** appears three times (ranks 5, 7 and 8). Rank 7 has a typo in the source data ("amyotrohpic"). These entries should be deduplicated, and no FGFR-related mechanism is known.
- **Kyphoscoliotic heart disease, amenorrhea, brachydactyly-syndactyly syndrome, axial spondylometaphyseal dysplasia and Mills syndrome** have no clear FGFR-mediated mechanism and no evidence. Several also raise safety concerns for FGFR blockade in developing bone.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15986P | BALVERSA Film-Coated Tablets 3 mg | Film-coated tablet | — |
| SIN15987P | BALVERSA Film-Coated Tablets 4 mg | Film-coated tablet | — |
| SIN15988P | BALVERSA Film-Coated Tablets 5 mg | Film-coated tablet | — |

All three are made by Janssen Cilag SpA and are oral products.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (FGFR kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Low (not a prominent feature of this class) |
| Emetogenicity Classification | Low |
| Monitoring Items | Serum phosphate, eye examinations, skin and nail changes, liver and renal function; please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

These entries come from general drug knowledge, not from the Evidence Pack.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone (Evidence Level L5), with no trials, no literature and no established mechanism for erdafitinib in pulmonary hypertension. FGFR signalling could be protective in the lung vasculature, so a therapeutic effect cannot be assumed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA. This is a blocking gap for safety screening.
- Mechanism-of-action data from DrugBank.
- Preclinical evidence (for example, pulmonary hypertension animal models) showing FGFR inhibition helps rather than harms.
- Normalisation of duplicate and misspelled disease entries (the ALS group) in the prediction output.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any clinical use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

