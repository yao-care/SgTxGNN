---
layout: default
title: Alglucosidase Alfa
parent: Low Evidence (L5)
nav_order: 64
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Alglucosidase Alfa: predicted new indication Adult polyglucosan body disease (evidence level L5). Approved use: Glycogen storage disease"
monitor_inn: "Alglucosidase alfa"
predicted_indications: ["adult polyglucosan body disease", "congenital entropion", "congenital ectropion", "congenital Horner syndrome (disease)", "ptosis-vocal cord paralysis syndrome", "camptodactyly, myopia, and fibrosis of the medial rectus muscle of eye", "epiblepharon", "ptosis-strabismus-ectopic pupils syndrome"]
---

# Alglucosidase Alfa
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Alglucosidase alfa: From Glycogen Storage Disease to Adult Polyglucosan Body Disease
{: .text-alpha }

## One-Sentence Summary

Alglucosidase alfa is a recombinant enzyme replacement therapy originally used for glycogen storage disease (Pompe disease).
The TxGNN model predicts it may be effective for **adult polyglucosan body disease**,
but **no clinical trials and no publications** currently support this direction, so it remains a computational prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Glycogen storage disease (the Singapore registration lists no indication text) |
| Predicted New Indication | Adult polyglucosan body disease |
| TxGNN Prediction Score | 0.9947 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, alglucosidase alfa is a recombinant human acid alpha-glucosidase (GAA). It breaks down glycogen inside lysosomes, and its efficacy in glycogen storage disease (Pompe disease) has been established.

Adult polyglucosan body disease (APBD) is caused by deficiency of the glycogen branching enzyme (GBE1). This leads to poorly branched, insoluble polyglucosan accumulating mainly in the cytosol of neurons and glia. At the substrate level the link is plausible, since polyglucosan is a glycogen-like polymer.

However, the mechanistic support is weak, for two reasons:
- The enzyme acts on lysosomal glycosidic bonds. It is not clear that it can reach cytosolic polyglucosan or degrade this abnormal structure.
- APBD is a neurological disease, and the recombinant enzyme has limited blood-brain barrier penetration.

The high TxGNN score (0.9947) is therefore best read as a signal from the shared "glycogen storage disease" category, not as proof of a specific mechanism.

**Other predictions in the top 10:** Seven further predictions (congenital entropion, congenital ectropion, congenital Horner syndrome, ptosis-vocal cord paralysis syndrome, camptodactyly-myopia-medial rectus fibrosis syndrome, epiblepharon, and ptosis-strabismus-ectopic pupils syndrome) are structural or developmental eye and neuromuscular conditions with no plausible link to glycogen metabolism. Their scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. All of them have evidence level L5 and no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13543P | Myozyme® (Alglucosidase alfa) 50mg Powder for Solution for Infusion | Injection, powder, lyophilized, for solution | Not stated in the registration data |

The product is a single-ingredient injectable (manufacturer: Genzyme Ireland Limited) with a valid status. There are no cancelled registrations.

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found, and no contraindicated diseases are recorded in the knowledge graph.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score. No trials or publications exist, the enzyme works in lysosomes while the target pathology is cytosolic, and blood-brain barrier penetration is limited. The lower-ranked predictions have even weaker or no mechanistic basis.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank, and the package insert warnings and contraindications from the HSA website
- Preclinical evidence on whether the enzyme can reach and degrade polyglucosan in neural tissue, including delivery across the blood-brain barrier
- A literature and trial search specific to APBD and glycogen storage disease type IV
- A route-of-administration and formulation feasibility assessment, since intravenous delivery may not reach the central nervous system
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

