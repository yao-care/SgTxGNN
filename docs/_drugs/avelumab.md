---
layout: default
title: Avelumab
parent: Low Evidence (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Avelumab
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

# Avelumab: From Cutaneous Neuroendocrine Carcinoma to Human Herpesvirus 8-Related Tumor

## One-Sentence Summary

Avelumab was originally used to treat cutaneous neuroendocrine carcinoma (Merkel cell carcinoma).
The TxGNN model predicts it may be effective for **human herpesvirus 8-related tumor**,
but **no clinical trials and no publications** were found in the data compiled for this report, so the prediction rests on the model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Cutaneous neuroendocrine carcinoma (taken from the knowledge-graph indication record; the Singapore licence has no indication text) |
| Predicted New Indication | Human herpesvirus 8-related tumor |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Avelumab is known to be an immune checkpoint inhibitor that blocks PD-L1. This is general background and not drawn from the compiled data.

Human herpesvirus 8 (HHV-8)-related tumors, such as Kaposi sarcoma, are virus-driven and may express PD-L1. Blocking PD-L1 is therefore biologically plausible. Merkel cell carcinoma is also a virus-associated tumor in many cases, which may partly explain the model's link between the two. However, no trials or literature were provided to test this idea, so it remains a hypothesis.

### Other Predictions in the Top 10

All ten predictions have scores above 99.9% and none has clinical trial or literature support. They differ greatly in plausibility:

| Rank | Predicted Disease | Score | Assessment |
|------|------|------|------|
| 1 | Human herpesvirus 8-related tumor | 99.97% | Plausible (virus-driven, may express PD-L1); no evidence |
| 2 | Middle ear neuroendocrine tumor | 99.97% | Extrapolated from another neuroendocrine tumor; uncertain |
| 3 | Malignant cutaneous granular cell skin tumor | 99.97% | Only shares the cutaneous tumor context; no checkpoint rationale |
| 4 | Ectomesenchymoma | 99.97% | No clear mechanistic rationale |
| 5 | Adenosine deaminase deficiency | 99.95% | Metabolic immunodeficiency; likely a model artifact |
| 6 | Reticular dysgenesis | 99.94% | No plausible link; likely a model artifact |
| 7 | Immunoerythromyeloid hypoplasia | 99.94% | No evident link; likely a model artifact |
| 8 | Non-severe combined immunodeficiency | 99.92% | No rationale; immune-related adverse events are a safety concern |
| 9 | Prostatic urethra urothelial carcinoma | 99.92% | Better grounded: avelumab is approved as maintenance therapy for urothelial carcinoma; site-specific evidence needed |
| 10 | Kidney pelvis sarcomatoid transitional cell carcinoma | 99.91% | Better grounded: upper-tract urothelial variant, often PD-L1 positive; variant-specific evidence needed |

Ranks 9 and 10 (the urothelial carcinoma subsites) are the best-grounded candidates and are marked "Research Question", meaning a targeted search is warranted. Ranks 5 to 8 are immunodeficiencies, where the high scores most likely reflect network proximity rather than real biology.

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
| SIN15672P | BAVENCIO Concentrate for Solution for Infusion 200mg/10mL (MERCK SERONO SA) | Injection, solution, concentrate | Not stated in the data compiled for this report |

This is the only licence on record, and it is a valid single-ingredient product. It is an injectable form.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Immunotherapy (PD-L1 inhibitor), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: Three Major-level interactions were identified, all with immunomodulatory agents:
  - Lenalidomide
  - Pomalidomide
  - Thalidomide

For warnings and contraindications, please refer to the package insert. The package insert has not yet been retrieved.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for human herpesvirus 8-related tumor is based only on the TxGNN model score (L5), with no registered trials or publications. Several other top predictions, especially the immunodeficiency diseases, appear to be model artifacts.

**To proceed, the following is needed:**
- Retrieve the HSA package insert to obtain warnings, contraindications and the approved indication (currently a blocking gap for safety screening)
- Obtain mechanism of action data from DrugBank
- Search for trials and literature on avelumab in HHV-8-related tumors, such as Kaposi sarcoma
- Run targeted searches for the urothelial carcinoma subsites (prostatic urethra, kidney pelvis sarcomatoid), which are the best-grounded alternatives
- Assess route compatibility and similarity to the original indication, both currently pending
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

