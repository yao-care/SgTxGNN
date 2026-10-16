---
layout: default
title: Galcanezumab
parent: Low Evidence (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Galcanezumab: predicted new indication Heparin cofactor 2 deficiency (evidence level L5). Approved use: Migraine disorder"
---

# Galcanezumab
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

# Galcanezumab: From Migraine to Heparin Cofactor 2 Deficiency

## One-Sentence Summary

Galcanezumab (Emgality) is an injectable monoclonal antibody originally used to prevent migraine.
The TxGNN model predicts it may be effective for **heparin cofactor 2 deficiency**, but there are **0 clinical trials** and **0 publications** supporting this direction.
The high prediction score is most likely a network-prediction artifact rather than a real therapeutic signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder (the registration records for Singapore do not state indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Heparin cofactor 2 deficiency |
| TxGNN Prediction Score | 99.50% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, galcanezumab is a humanized monoclonal antibody that neutralizes calcitonin gene-related peptide (CGRP), a key mediator in migraine. Its efficacy in migraine prevention is well established.

Heparin cofactor 2 deficiency is a hereditary coagulation-inhibitor disorder involving impaired regulation of thrombin. There is no plausible mechanistic link between CGRP blockade and thrombin regulation. The very high TxGNN score most likely reflects patterns in the knowledge graph rather than biology. No trials or publications support the prediction.

Note that the same drug's prediction list also includes several other coagulation-related conditions (antithrombin deficiency type 2, factor V excess, thrombophilia, and others). These share the same lack of mechanistic support and look like a clustering artifact in the model.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15919P | EMGALITY Solution for Injection in Pre-filled Pen 120 mg/mL | Injection, solution | — |
| SIN16063P | EMGALITY Solution for Injection in Pre-filled Syringe 100 mg/mL | Injection, solution | — |

Both licenses are valid single-ingredient products from Eli Lilly and Company. The registration data compiled for this report do not include the approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature, and no plausible mechanistic link between CGRP neutralization and heparin cofactor 2 deficiency. Evidence is at L5 (model prediction only), so the drug should not be advanced for this indication.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis connecting CGRP signalling to heparin cofactor 2 or thrombin regulation, supported by preclinical data
- Mechanism of action (MOA) data to be added to the drug record
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Review of other predictions for this drug. The prediction for **migraine with brainstem aura** (score 98.33%) has the strongest support, at evidence level L3. It is essentially an extension within the approved migraine indication rather than true repurposing, and it carries a glaucoma risk signal for CGRP inhibitors that warrants safety monitoring.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

