---
layout: default
title: Ocrelizumab
parent: Low Evidence (L5)
nav_order: 722
evidence_level: L5
indication_count: 10
---

# Ocrelizumab
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

# Ocrelizumab: From Multiple Sclerosis to HER2-Positive Breast Carcinoma

## One-Sentence Summary

Ocrelizumab is an anti-CD20 antibody that depletes B cells and is marketed in Singapore as OCREVUS. The registration record does not state its approved indication; multiple sclerosis is inferred from the pack's safety notes. The TxGNN model ranks **HER2-positive breast carcinoma** as its top new prediction, but there are **0 clinical trials** and **0 publications** supporting it, so this is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Multiple sclerosis (inferred from the pack's safety notes; the registration text is blank) |
| Predicted New Indication | HER2 positive breast carcinoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Ocrelizumab is known to be an anti-CD20 antibody that depletes B cells.

The mechanistic case for breast cancer is weak. Breast carcinoma cells do not express CD20, so the drug has no direct target on the tumour. The only speculative link is an indirect one, through tumour-infiltrating B cells in the HER2-positive microenvironment, and nothing in this pack supports it. The high score is more likely a knowledge-graph artifact from shared breast-cancer neighbours than independent evidence.

The nine lower-ranked predictions share this profile:
- **Other breast cancer subtypes** (progesterone-receptor positive, progesterone-receptor negative, normal breast-like, luminal A/B): no supporting trials or literature. The first two share an identical score (0.99813), which suggests an inherited graph signal.
- **Benign neoplasms** (tongue, hypopharynx, buccal mucosa): no biological rationale for anti-CD20 therapy.
- **Neural-crest and nerve-sheath tumours** (cervical neuroblastoma, jugular foramen schwannoma): these tumours do not express CD20, so there is no mechanistic basis.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for HER2-positive breast carcinoma.

The 19 papers retrieved for the luminal A/B prediction (rank 4) are false positives from keyword matching on "B". They cover B-cell biology, hepatitis B vaccines and B-cell lymphoma, and none addresses ocrelizumab or breast cancer. They were not counted as evidence.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16871P | OCREVUS CONCENTRATE FOR SOLUTION FOR INFUSION 300MG/10ML | Injection, solution, concentrate |

Manufacturer: Roche Diagnostics GmbH & F. Hoffmann-La Roche Ltd. The only available route is injectable.

## Safety Considerations

- **Key Warnings**: The label carries a malignancy warning. In MS trials, breast cancer was numerically more frequent in treated patients. This argues against a therapeutic benefit in breast cancer without new evidence.
- **Drug Interactions**: No interaction records were found.

Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no trials or relevant literature. The tumour cells lack the drug's target (CD20), and the drug's own malignancy warning points in the opposite direction.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications. The pack flags this as a blocking gap that prevents safety screening.
- Mechanism of action data from DrugBank.
- Evidence that tumour-infiltrating B cells in HER2-positive breast cancer are a valid target for B-cell depletion.
- Any preclinical or clinical study of anti-CD20 therapy in breast cancer.

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

