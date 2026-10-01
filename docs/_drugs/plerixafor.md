---
layout: default
title: Plerixafor
parent: Low Evidence (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
---

# Plerixafor
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

# Plerixafor: From Stem Cell Mobilization to Indolent Plasma Cell Myeloma

## One-Sentence Summary

Plerixafor is an injectable drug marketed in Singapore, and its known use in myeloma is stem cell mobilization rather than treating the disease itself.
The TxGNN model predicts it may be effective for **indolent plasma cell myeloma**, with a very high score (99.97%).
However, **0 clinical trials** and **0 publications** support this specific prediction, so it is a model output only.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Indolent plasma cell myeloma |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, plerixafor blocks CXCR4, a chemokine receptor. CXCR4 and its ligand CXCL12 help plasma cells home to and stay in the bone marrow, so blocking this axis is biologically plausible for a plasma cell disease.

There is an important caveat. Plerixafor's established role in myeloma is mobilizing stem cells for collection, not treating the disease. The original indication and mechanism fields are missing from the input, so this link cannot be verified from the data provided.

**A better-supported direction appears in the same prediction list.** Myeloid leukemia (rank 7, TxGNN score 99.02%) has multiple Phase 1 and Phase 1/2 trials and about 20 publications. These trials test plerixafor with chemotherapy or hypomethylating agents in acute myeloid leukemia, and the input records them as supporting feasibility and safety. There is no randomized efficacy evidence there either, and several trials were terminated or withdrawn.

## Clinical Trial Evidence

Currently no related clinical trials registered

## Literature Evidence

Currently no related literature available

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN13894P | Mozobil Solution for Injection 20mg/ml | Injection, solution | Genzyme Corporation |
| SIN16879P | Pleristem Solution for Injection 20mg/ml | Injection, solution | Eugia Pharma Specialities Limited |
| SIN17147P | Plerixafor-AFT Solution for Injection 24 mg/1.2 mL | Injection, solution | Sichuan Huiyu Pharmaceutical Co., Ltd. |

The approved indication text is not recorded for any of these licences in the input.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for indolent plasma cell myeloma scores very high but has no trials or literature behind it (L5). The package insert data needed for safety screening is also missing. The mechanism is plausible, but plerixafor's known myeloma use is mobilization, not disease treatment.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (this blocks safety screening)
- Mechanism of action and original indication data from DrugBank
- Any indication-specific preclinical or clinical evidence for indolent plasma cell myeloma
- Consideration of the better-supported myeloid leukemia direction as a separate research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

