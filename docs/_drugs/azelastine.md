---
layout: default
title: Azelastine
parent: Low Evidence (L5)
nav_order: 130
evidence_level: L5
indication_count: 10
---

# Azelastine
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

# Azelastine: From Allergic Rhinitis to Rosacea Conjunctivitis

## One-Sentence Summary

Azelastine is an antihistamine that is marketed in Singapore as nasal sprays, and the trials in this pack studied it in allergic rhinitis. The TxGNN model predicts it may be effective for **rosacea conjunctivitis**, but **0 clinical trials** and **0 publications** currently support this. It is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis (inferred: the HSA records supplied have no indication text, so this comes from the nasal spray products and the rhinitis trials in the pack) |
| Predicted New Indication | Rosacea conjunctivitis |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in DrugBank for this pack. Azelastine is known as an H1-receptor antagonist that also stabilises mast cells and inhibits mediator release. The high score most likely comes from the model's graph proximity to allergic conjunctivitis, where azelastine is well studied.

This link is weak for rosacea conjunctivitis. Ocular disease in rosacea is driven mainly by meibomian gland dysfunction and inflammation, not histamine. Antihistamine activity would therefore be expected to help at most with an allergic component or with symptoms, and no study confirms even that.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15255P | DYMISTA NASAL SPRAY (Cipla Limited) | Spray, metered | Not stated in the record |
| SIN15256P | SYNAZE NASAL SPRAY (Cipla Limited) | Spray, metered | Not stated in the record |

Both products are nasal sprays. No ophthalmic azelastine product appears in the Singapore records supplied.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and only a model score, and the mechanism does not fit rosacea-related ocular disease well. Singapore has only nasal spray products, so there is no matching route of administration.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Any clinical or preclinical evidence of azelastine in rosacea-associated ocular disease
- A route assessment, since ocular use would need an ophthalmic formulation that is not registered in Singapore

**Other predictions in this pack (for context):**
- **Conjunctivitis (rank 10, score 91.15%, L2, Proceed with Guardrails):** This has direct randomised evidence for topical azelastine in allergic conjunctivitis (PMIDs 12841925, 12841924, 12658084) and a Cochrane review (PMID 26028608). It is most likely an existing labeled use rather than a new finding. The claim should be limited to allergic conjunctivitis and the labeled ophthalmic indication confirmed.
- **Allergic urticaria (rank 2, score 96.23%, L4, Research Question):** The rationale is biologically strong, but all 10 trials listed are in allergic rhinitis, not urticaria.
- **Ranks 3 to 9 (other conjunctivitis subtypes):** All are L5 with no evidence, and several are infectious rather than histamine-driven.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

