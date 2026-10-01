---
layout: default
title: Indacaterol
parent: Low Evidence (L5)
nav_order: 524
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From COPD to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is an ultra-long-acting inhaled beta-2 agonist bronchodilator, used in Singapore-registered combination inhalers for obstructive airway disease.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obstructive airway disease (COPD; asthma in triple-combination products). No indication text appears in the Singapore registration records provided |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the records. Indacaterol is a long-acting beta-2 agonist that relaxes airway smooth muscle through Gs/cAMP signalling. It is marketed in fixed-dose combinations with glycopyrronium and/or mometasone.

NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor (AVPR2), which leave the receptor constitutively active. Indacaterol acts on a different Gs-coupled receptor, and no established pathway connects beta-2 agonism to suppressing constitutive V2 receptor signalling. Its bronchodilator use has no clear link to a renal water-handling disorder.

The high score therefore reflects graph-based similarity in the TxGNN knowledge graph, not a demonstrated or plausible therapeutic mechanism. The link should be treated as speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

All five registrations are combination products containing indacaterol. The registration records provided do not state approved indications.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14539P | Ultibro Breezhaler Inhalation Powder Hard Capsule 110/50 mcg | Capsule | Not stated in the record |
| SIN16148P | Atectura Breezhaler Inhalation Powder, Hard Capsule 150/160 mcg | Powder, metered | Not stated in the record |
| SIN16149P | Atectura Breezhaler Inhalation Powder, Hard Capsule 150/80 mcg | Powder, metered | Not stated in the record |
| SIN16147P | Atectura Breezhaler Inhalation Powder, Hard Capsule 150/320 mcg | Powder, metered | Not stated in the record |
| SIN16153P | Enerzair Breezhaler Inhalation Powder, Hard Capsule 150/50/160 mcg | Powder, metered | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information. Warnings, contraindications and interaction data have not yet been obtained from the HSA package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The NSIAD prediction has no trials, no literature and no credible mechanism, so it rests on a graph score alone (Evidence Level L5). Safety data have not been retrieved, which blocks safety screening.

Among the other top-10 predictions, only "bronchial disease" has substantial evidence (multiple Phase 3 asthma trials and an RCT). That mostly reflects indacaterol's existing bronchodilator use rather than true repurposing, and the asthma evidence applies to the triple combination rather than to indacaterol alone.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website
- Mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking beta-2 agonism to V2 receptor signalling, if this direction is to be pursued
- Correction of the empty original-indication field so that existing labelled uses are separated from true repurposing candidates
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

