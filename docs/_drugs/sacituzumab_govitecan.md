---
layout: default
title: Sacituzumab Govitecan
parent: Low Evidence (L5)
nav_order: 881
evidence_level: L5
indication_count: 10
---

# Sacituzumab Govitecan
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

# Sacituzumab govitecan: From Oncology (Trop-2-Directed Cancer Therapy) to Drug-Induced Osteoporosis

## One-Sentence Summary

Sacituzumab govitecan is a Trop-2-directed antibody-drug conjugate with a topoisomerase I inhibitor payload (SN-38), used in oncology.
The TxGNN model predicts it may be effective for **drug-induced osteoporosis**, but there are currently **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only prediction with no mechanistic rationale, so it should be treated as a low-confidence signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record (the drug is a cancer therapy used in oncology) |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Sacituzumab govitecan is known to be a Trop-2-directed antibody-drug conjugate. It delivers SN-38, the active metabolite of irinotecan and a topoisomerase I inhibitor, to Trop-2-expressing tumour cells.

On the available information, **the prediction is not mechanistically supported**. Drug-induced osteoporosis is a chronic bone-metabolism condition. A cytotoxic, myelosuppressive agent is a poor fit for it, and cytotoxic therapy is itself associated with bone loss in some settings. The score of 0.998 appears to come from knowledge-graph proximity alone, with no trials or literature behind it.

The other nine predictions in the pack show the same pattern. They are diabetic retinopathy (severe nonproliferative and general) and several cataract subtypes. All are L5 with no evidence and no plausible link. The identical scores across the cataract subtypes (0.9855 and 0.9840) suggest score propagation within the graph rather than disease-specific signal.

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
| SIN16425P | TRODELVY POWDER FOR SOLUTION FOR INFUSION 180 MG/VIAL (BSP Pharmaceuticals S.p.A.) | Lyophilized powder for solution for injection (injectable) | Not listed in the registration record |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy: antibody-drug conjugate with a topoisomerase I inhibitor payload (SN-38) |
| Myelosuppression Risk | High (neutropenia is a key concern for this class; confirm against the package insert) |
| Emetogenicity Classification | Medium (based on general drug-class knowledge; confirm against the package insert) |
| Monitoring Items | CBC with differential (neutrophils in particular), diarrhoea and hydration status, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a knowledge-graph score alone (L5), with no trials, no literature and no plausible mechanism. The risk profile of a cytotoxic, myelosuppressive ADC is also unfavourable for a chronic non-malignant bone condition.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently a blocking gap for safety screening
- Mechanism of action data (for example from DrugBank) to support a mechanistic-link analysis
- Any preclinical or clinical evidence linking Trop-2 targeting or topoisomerase I inhibition to bone metabolism
- A benefit-risk justification for systemic cytotoxic exposure in a non-malignant indication

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

