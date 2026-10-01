---
layout: default
title: Dobutamine
parent: Low Evidence (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
---

# Dobutamine
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

# Dobutamine: From Intravenous Inotropic Support to Alopecia

## One-Sentence Summary

Dobutamine is a beta-1 adrenergic inotrope given by injection for cardiac support. The TxGNN model predicts it may be effective for **alopecia**, but **0 clinical trials** and only **2 off-topic case reports** exist for this indication, and neither supports it. The prediction rests on the model score alone and is not backed by any evidence.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Alopecia |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data and the registered original indication are not available in the Evidence Pack. Based on known pharmacology, dobutamine is a beta-1 adrenergic agonist used as an intravenous inotrope. It has no known effect on hair follicle biology.

The high score (0.9985) is most likely a knowledge-graph artifact. Dobutamine probably shares graph neighbors with cardiovascular drugs such as minoxidil. Minoxidil is a vasodilator known for its hair-growth effect, and that link does not carry over to dobutamine. Because the original mechanism and indications are missing, the prediction cannot be cross-checked.

The other top predictions show the same pattern:
- **Hair disorders:** hypotrichosis simplex of the scalp, congenital hypotrichosis milia, diffuse alopecia areata and hypertrichosis. All are prediction-only, with no trials or literature.
- **Glaucoma:** beta-adrenergic signaling touches aqueous humor dynamics, but an intravenous inotrope has no established pressure-lowering role.
- **Raynaud disease:** vasodilation is theoretically relevant, but no therapeutic data exist.
- **Headache and migraine:** the retrieved literature describes headache as an adverse effect of inotropes, and the one migraine paper is a preclinical study that does not confirm dobutamine was tested.

All of these are Level L5 with a Hold recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered for alopecia.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | Case report (veterinary) | Journal of Veterinary Cardiology | A cat with heart failure after minoxidil intoxication received dobutamine for hypotension. This is not evidence for treating alopecia. |
| [17505274](https://pubmed.ncbi.nlm.nih.gov/17505274/) | 2007 | Case report | Pediatric Emergency Care | Acute colchicine poisoning in a child, with hair loss as a recovery-phase feature. Dobutamine is not evaluated as a treatment. |

Both papers mention alopecia-related settings only incidentally, and neither tests dobutamine for hair loss.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN08702P | DOBUTAMINE INJECTION 12.5 mg/ml | Injection | Hospira, Inc. |

The registry entry does not provide approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no supportive literature and no plausible mechanistic link. Dobutamine is also a systemically active intravenous inotrope, which makes hemodynamic risk a concern for any non-cardiac use. The high TxGNN score alone does not justify further investment.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action and original indication data from DrugBank
- Evidence of a specific mechanistic link between beta-1 agonism and hair follicle biology
- Confirmation of whether a topical route is feasible, since an injectable-only product is unlikely to suit a dermatologic use
- Re-review of the migraine preclinical paper's abstract only if that indication is reconsidered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

