---
layout: default
title: Dulaglutide
parent: Low Evidence (L5)
nav_order: 353
evidence_level: L5
indication_count: 10
---

# Dulaglutide
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

# Dulaglutide: From Type 2 Diabetes to Opsismodysplasia

## One-Sentence Summary

Dulaglutide is a once-weekly injectable GLP-1 receptor agonist, used for type 2 diabetes (the Singapore registration record does not state the indication, so this comes from the drug's known class use).
The TxGNN model predicts it may be effective for **opsismodysplasia**, a rare skeletal disorder.
There are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus (from known drug use; not stated in the Singapore licence records) |
| Predicted New Indication | Opsismodysplasia |
| TxGNN Prediction Score | 97.05% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known class pharmacology, dulaglutide is a GLP-1 receptor agonist. It enhances glucose-dependent insulin secretion, slows gastric emptying and reduces appetite. Its efficacy in type 2 diabetes is established, but nothing in these mechanisms addresses a skeletal disorder.

**This prediction is not biologically reasonable on current information.** Opsismodysplasia is a rare skeletal dysplasia linked to INPPL1, with impaired growth plate ossification. There is no plausible pathway from GLP-1 receptor signalling to this defect. The high score most likely reflects proximity in the knowledge graph rather than real biology.

The other top predictions show the same pattern:
- **Stiff person spectrum (focal stiff limb syndrome, classic stiff person syndrome):** the link likely comes from anti-GAD65 autoimmunity co-occurring with diabetes. That is comorbidity, not evidence of treatment benefit.
- **Localized lipodystrophies (drug-induced, centrifugal, pressure-induced, idiopathic):** these likely cluster together in the graph. Dulaglutide is itself an injectable, and further fat loss would be undesirable.
- **Pancreatic agenesis:** dulaglutide needs existing beta cells to act, and these are largely absent in this condition.
- **Thiamine-responsive dysfunction syndrome and autoimmune oophoritis:** the support is weak or speculative, and there are no clinical data.

All ten predicted indications are at evidence level L5 with a Hold recommendation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14968P | TRULICITY INJECTION 0.75MG/0.5ML | Injection, solution | Not listed in the record |
| SIN14967P | TRULICITY INJECTION 1.5MG/0.5ML | Injection, solution | Not listed in the record |

Both products are made by Eli Lilly and Company, with Vetter Pharma-Fertigung as the manufacturing site. The only available route is injection.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical, registry or literature support and no plausible mechanism. The high TxGNN score most likely reflects knowledge-graph artifacts, not a genuine treatment signal.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently missing and blocks any safety screening
- Detailed mechanism of action data from DrugBank
- Preclinical or mechanistic evidence linking GLP-1 receptor signalling to INPPL1-related growth plate defects
- Review by a rare skeletal disease specialist to decide whether this candidate is worth pursuing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

