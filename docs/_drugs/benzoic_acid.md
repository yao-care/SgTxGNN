---
layout: default
title: Benzoic Acid
parent: Low Evidence (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Benzoic Acid
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

# Benzoic Acid: From Topical Skin Preparations to Bronchitis

## One-Sentence Summary

Benzoic acid is registered in Singapore only as an ingredient in topical skin products (ointments and a solution). The registration data states no approved indication, but the product names refer to ringworm and tinea. The TxGNN model predicts it may be effective for **bronchitis**, but there are **0 clinical trials** and only **2 publications** on file, and neither publication studies benzoic acid. This is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data. Product names suggest topical skin infections (ringworm, tinea) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available, and no original indication is on file. Based on the registered products, benzoic acid is used in topical preparations named for ringworm and tinea. It is a commonly known antifungal and preservative ingredient in such products. No mechanistic link to bronchitis has been established.

The 99.98% score is a knowledge-graph embedding output only. The two retrieved papers do not support it:
- One reviews repaglinide, a benzoic acid derivative, in type 2 diabetes.
- The other tests a soluble epoxide hydrolase inhibitor in a smoke-induced COPD model.

Route compatibility is also a concern. All registered products are topical (ointment, solution), while bronchitis would normally require systemic or inhaled delivery. This has not been assessed.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | Drugs | Review of repaglinide, a benzoic acid derivative, in type 2 diabetes. Not about benzoic acid or bronchitis |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | Preclinical | Am J Respir Cell Mol Biol | Soluble epoxide hydrolase inhibitor in a smoke-induced COPD model. Bronchitis is only mentioned as a COPD component. Benzoic acid is not studied |

Neither paper provides direct evidence for benzoic acid in bronchitis.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09544P | Robinson Ringworm & Whitespot Ointment | Ointment | Not stated in registration data |
| SIN08773P | Tinea Skin Solution (Three Leg Brand) | Solution | Not stated in registration data |
| SIN09830P | Saw Hong Choon Skin Ointment | Ointment | Not stated in registration data |
| SIN04418P | Nixoderm Ointment | Ointment | Not stated in registration data |
| SIN16547P | Veelanz's Ointment | Ointment | Not stated in registration data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no trials, and the retrieved literature does not study benzoic acid. The registered topical products also do not match a respiratory indication.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications, which are required before any safety screening
- Mechanism of action data (for example, from the DrugBank API)
- Direct studies of benzoic acid in bronchitis or airway inflammation models
- An assessment of whether a suitable delivery route exists, since only topical forms are registered
- A review of the other predictions. Diabetic retinopathy (L4) has the most indirect context, but it relies only on benzoic acid derivatives (repaglinide, synthetic retinoids), not benzoic acid itself. It would need a direct test in retinal models before it counts as evidence.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

