---
layout: default
title: Flavoxate
parent: Low Evidence (L5)
nav_order: 429
evidence_level: L5
indication_count: 10
---

# Flavoxate
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

# Flavoxate: From Urinary Tract Spasm to ADHD, Inattentive Type

## One-Sentence Summary

Flavoxate is a smooth muscle relaxant with antimuscarinic and PDE-inhibitory properties, marketed in Singapore as an oral tablet. The registration records do not state its approved indication, so the "urinary tract spasm" label in this report is inferred from its pharmacology.
The TxGNN model ranks **attention deficit hyperactivity disorder, inattentive type** as its top prediction, but there are **0 clinical trials** and **0 publications** supporting it, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract spasm (inferred from pharmacology; the approved indication text is blank in all 4 registrations) |
| Predicted New Indication | Attention deficit hyperactivity disorder, inattentive type |
| TxGNN Prediction Score | 99.75% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Flavoxate is generally described as a smooth muscle relaxant with antimuscarinic and PDE-inhibitory activity. It has no recognised dopaminergic or noradrenergic activity, which are the pathways relevant to ADHD.

**No plausible mechanistic link to ADHD was identified.** The high score (0.997) most likely reflects graph proximity in the knowledge graph rather than biology. The same pattern appears in two other predictions: "attention deficit-hyperactivity disorder" (rank 4, essentially a duplicate) and "specific developmental disorder" (rank 3). All three appear to share one graph artifact.

The remaining top-10 predictions differ in plausibility:

| Rank | Predicted Indication | Score | Mechanistic Plausibility |
|------|------|------|------|
| 6 | Neurogenic bladder | 99.13% | **Most coherent.** Antimuscarinic and smooth muscle relaxant effects on the detrusor fit bladder overactivity and spasm. |
| 2 | Irritable bowel syndrome | 99.74% | Plausible but unverified. Consistent with antispasmodic therapy. |
| 5 | Cauda equina syndrome | 99.27% | Indirect. Could ease bladder symptoms only, not the underlying compression. |
| 7 | Gastroduodenitis | 99.12% | Weak. Flavoxate is not an established GI agent. |
| 8 | Peptic ulcer disease | 99.10% | Weak. Antimuscarinic adjuncts have been superseded by acid suppression. |
| 9 | Pharyngitis | 98.90% | No plausible link. |
| 10 | Chondromyxoid fibroma | 98.89% | No plausible link. Likely a graph artifact. |

Any literature review should start with neurogenic bladder, not ADHD.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN12299P | LAVOXEN TABLET 200 mg | Tablet, film coated | Dae Han New Pharm. Co. Ltd. |
| SIN09677P | CLEANXATE TAB 200 mg | Tablet, sugar coated | Sam Chun Dang Pharm Co Ltd |
| SIN16400P | URIPAX FILM COATED TABLET 200MG | Tablet, film coated | Y.S.P. Industries (M) Sdn. Bhd. |
| SIN12007P | URISPAS 200 TABLET 200 mg | Tablet, film coated | Recordati Industria Chimica e Farmaceutica SpA |

All four products are oral tablets. The approved indication text is not included in the registration records.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked prediction (ADHD, inattentive type) has only a model score behind it. It has no clinical or literature support and no plausible mechanistic link to flavoxate's pharmacology. The high score is likely a graph artifact.

**To proceed, the following is needed:**
- The Singapore package insert (warnings, contraindications and approved indication), which is required before any safety screening
- Detailed mechanism of action data, for example from DrugBank
- A targeted literature and trial search for neurogenic bladder and irritable bowel syndrome, the more plausible predictions, before any further work on ADHD
- Confirmation of the original approved indication, so the original-to-new indication relationship can be assessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

