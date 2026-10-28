---
layout: default
title: Felypressin
parent: Low Evidence (L5)
nav_order: 421
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Felypressin: predicted new indication Drug-induced osteoporosis (evidence level L5). Approved use: Not recorded in the registration data"
monitor_inn: "Felypressin"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "esotropia", "diabetic retinopathy", "chondroid hamartoma", "ductal or ductular proliferation", "bronchial adenomas/carcinoids childhood", "non-seminomatous lesion", "tumor of testis and paratestis", "pre-malignant neoplasm"]
---

# Felypressin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Felypressin: From Local Dental Anaesthesia Adjunct (Indication Text Not Recorded) to Drug-Induced Osteoporosis
{: .text-alpha }

## One-Sentence Summary

Felypressin is a synthetic vasopressin analogue, marketed in Singapore as an injection (CITANEST OCTAPRESSIN), although the registered indication text is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no mechanistic or clinical support.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, felypressin is a synthetic vasopressin analogue that acts mainly as a V1a receptor agonist, producing vasoconstriction. It is used alongside local dental anaesthetics, where it prolongs the anaesthetic effect and reduces bleeding at the injection site.

No established pathway links felypressin to bone remodelling or to glucocorticoid-induced bone loss. The high TxGNN score (0.9980) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. In practice, this prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern: none has clinical evidence, and several have tied scores (for example, 0.9919 for four unrelated terms), which suggests non-specific, ontology-level predictions. Two diabetic retinopathy predictions also raise a theoretical safety concern, because vasoconstriction could worsen retinal ischaemia.

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
| SIN06175P | CITANEST OCTAPRESSIN INJECTION | Injection | Not recorded |

Manufacturer: Astra Pharmaceuticals Pty Ltd. This is the only registration, and it is a valid single-ingredient product.

---

## Safety Considerations

Please refer to the package insert for safety information.

As a vasoconstrictor, felypressin carries a theoretical concern for retinal perfusion if considered for diabetic retinopathy. This is an inference from its pharmacology, not an established finding.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence. There are no clinical trials or publications, no identified mechanistic link, and the package insert safety data have not been reviewed. The evidence level is L5.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website
- Mechanism of action data (for example, from DrugBank)
- The approved indication text for the Singapore registration
- A literature and trial search for a plausible biological link between V1a signalling and bone metabolism
- Route and formulation compatibility assessment, since only an injectable dental product is registered
- Review of the other predicted indications (for example, diabetic retinopathy) only if a credible mechanism and safety rationale emerge
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

