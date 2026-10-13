---
layout: default
title: Tedizolid Phosphate
parent: Low Evidence (L5)
nav_order: 958
evidence_level: L5
indication_count: 10
---

# Tedizolid Phosphate
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

# Tedizolid Phosphate: From Skin Infection to Post-Infectious Syndrome

## One-Sentence Summary

Tedizolid phosphate was originally used to treat infection-related skin disease.
The TxGNN model predicts it may be effective for **post-infectious syndrome**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Skin disease caused by infection (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Post-infectious syndrome |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, tedizolid is an oxazolidinone antibacterial. It inhibits bacterial protein synthesis by binding the 23S rRNA of the 50S ribosomal subunit, and it is active against Gram-positive organisms. Its efficacy in infection-related skin disease is the basis for its original use.

The link to the predicted indication is weak. Post-infectious syndromes are generally immune-mediated sequelae that appear after the pathogen has been cleared, so an antibacterial offers no clear mechanistic rationale. The high score (0.994) most likely reflects the model's association between "infection" concepts and anti-infective drugs, not a demonstrated biological mechanism. A plausible role would exist only if a persistent Gram-positive trigger were identified.

**Other predictions in the top 10** (all L5, all Hold):

| Rank | Predicted Disease | Score | Comment |
|------|------|------|------|
| 2 | Post-bacterial disorder | 99.42% | Vague category that overlaps with post-infectious syndrome |
| 3 | Postinfectious vasculitis | 99.42% | Immune-complex mediated, so an antibacterial would not address the pathology |
| 4 | Infective urethral stricture | 99.38% | Fibrotic and anatomical, with surgery as the primary treatment. Many urethral pathogens are Gram-negative |
| 5 | Chagas cardiomyopathy | 99.37% | Protozoal cause, with no established antiprotozoal activity |
| 6 | Infection-related haemolytic uraemic syndrome | 99.36% | Usually Shiga toxin-producing *E. coli*, so there is no activity, and antibiotics may increase toxin release (potentially unsafe) |
| 7 | Otitis externa | 99.33% | Plausible for *S. aureus*, but *Pseudomonas aeruginosa* is not covered. Topical agents are standard |
| 8 | Conjunctivitis | 99.00% | MRSA is covered in vitro, but an ophthalmic formulation would be needed |
| 9 | Infectious otitis interna | 98.58% | Inner ear penetration is unknown |
| 10 | Infectious otitis media | 97.65% | *H. influenzae* and *M. catarrhalis* are not covered, and paediatric data are limited |

Among these, **otitis externa** and **conjunctivitis** are the most biologically plausible, because they involve Gram-positive pathogens related to the approved skin infection indication. Neither has supporting data.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14851P | SIVEXTRO Lyophilized Powder for Solution for Infusion 200 mg per vial | Injection, powder, lyophilized, for solution | Not stated in the licence records |
| SIN14850P | SIVEXTRO Film-Coated Tablet 200 mg | Tablet, film coated | Not stated in the licence records |

Both licences are valid, single-ingredient products. Injectable and oral routes are available.

## Safety Considerations

- **Knowledge-graph contraindication signals** (not label text): neutropenia and agranulocytosis. Haematological monitoring would be prudent in any new use.
- **Drug Interactions**: No interaction records were found in the data compiled for this report.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5), with no clinical trials or publications. Post-infectious syndromes are mainly immune-mediated, so the mechanistic link to an antibacterial is weak. Some alternative predictions (e.g. infection-related HUS) carry potential safety concerns.

**To proceed, the following is needed:**
- Mechanism of action data and the package insert warnings and contraindications
- A clear definition of the target condition, and evidence of a persistent Gram-positive trigger if one is claimed
- Preclinical or in vitro data supporting any new use
- If pursuing a more plausible candidate (otitis externa or conjunctivitis), a review of the pathogen spectrum, formulation (topical or ophthalmic) and tissue penetration
- A haematological safety assessment, given the neutropenia and agranulocytosis signals
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

