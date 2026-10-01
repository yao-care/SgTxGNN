---
layout: default
title: Panitumumab
parent: Low Evidence (L5)
nav_order: 752
evidence_level: L5
indication_count: 10
---

# Panitumumab
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

# Panitumumab: From an Anti-EGFR Oncology Antibody to Drug-Induced Osteoporosis

## One-Sentence Summary

Panitumumab is an anti-EGFR monoclonal antibody marketed in Singapore as Vectibix, and the registration record supplied does not list its approved indication.
The TxGNN model predicts it may be relevant to **drug-induced osteoporosis**, but there are **0 clinical trials** and **0 publications** supporting this direction.
This is a model-only hypothesis (Evidence Level L5) and should be treated as such.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not listed in the registration record supplied |
| Predicted New Indication | Drug-induced osteoporosis |
| TxGNN Prediction Score | 99.13% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Panitumumab is an anti-EGFR monoclonal antibody. Detailed mechanism-of-action data is not available in the source record, so the mechanistic analysis is limited.

EGFR signalling has been discussed in the context of bone remodelling. Nothing in the supplied data shows which direction the effect goes, and EGFR blockade could plausibly be neutral or even harmful to bone. The link between the original use and this new indication therefore rests only on a TxGNN graph prediction (score 0.991), and is speculative.

The other top-ranked predictions are diabetic retinopathy (including severe non-proliferative disease) and several cataract subtypes, all with scores around 0.988 to 0.990. Several cataract entries share identical scores, which suggests a shared graph-derived signal rather than disease-specific evidence. None has supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN14498P | Vectibix Concentrate for Solution for Infusion 100 mg/vial | Infusion, solution concentrate | Not listed in the registration record |

The manufacturer is Amgen Manufacturing Limited LLC. The only registered route is injectable.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-EGFR monoclonal antibody) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Electrolytes, especially magnesium and calcium (anti-EGFR antibodies are known to cause hypomagnesemia); other items per the package insert |
| Handling Protection | Please refer to the package insert and local institutional handling policy |

## Safety Considerations

- **Electrolyte disturbance (caution flag):** Anti-EGFR antibodies are known to cause hypomagnesemia. This could be counterproductive in bone-related conditions and in cataract subtypes secondary to hypocalcaemia. It is a caution and not evidence of benefit.
- **Systemic use in new populations:** Panitumumab is a systemic oncology antibody, and its safety in patients with diabetic eye disease, cataract or osteoporosis has not been assessed.

Please refer to the package insert for complete safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a TxGNN score, with no clinical trials, no literature, and no established mechanism. The direction of EGFR blockade on bone is unclear and may be harmful, and the safety profile of a systemic oncology antibody in these populations is unassessed.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indication), which is currently blocking safety screening
- Mechanism-of-action data from DrugBank
- A literature review of EGFR signalling in bone remodelling to establish the direction of effect
- Preclinical or mechanistic evidence for the predicted indication
- A risk-benefit assessment of systemic anti-EGFR therapy in non-oncology populations

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

