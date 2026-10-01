---
layout: default
title: Ramucirumab
parent: Low Evidence (L5)
nav_order: 842
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: From Gastric Cancer to Uterine Ligament Adenocarcinoma

## One-Sentence Summary

Ramucirumab is a VEGFR-2 antibody used in gastric and gastroesophageal junction adenocarcinoma.
The TxGNN model predicts it may be effective for **uterine ligament adenocarcinoma**,
but **0 clinical trials** and **0 publications** currently support this direction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gastric / gastroesophageal junction adenocarcinoma (general pharmacology knowledge; the Singapore registration text does not state an indication) |
| Predicted New Indication | Uterine ligament adenocarcinoma |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the supplied record. Based on general pharmacology, ramucirumab is a monoclonal antibody that blocks VEGFR-2 and thereby inhibits VEGF-driven tumour angiogenesis. Its efficacy in gastric and gastroesophageal junction adenocarcinoma is established, and mechanistically it may be applicable to other adenocarcinomas that depend on angiogenesis.

Uterine ligament adenocarcinoma is an extremely rare gynaecologic tumour. No disease-specific data on VEGFR-2 dependence were provided, so the link is plausible but unsupported.

The model's other top predictions all fall in the same cluster of gynaecologic adenocarcinomas, with scores of about 99.94% to 99.95%:
- endocervical carcinoma
- adenoid cystic carcinoma of the cervix
- several uterine ligament histologies (serous, endometrioid, clear cell, mucinous)
- rare cervical variants (signet ring, glassy cell, intestinal-type mucinous)

The most reasonable of these is cervical cancer. The VEGF-A antibody bevacizumab has Phase 3 data there, but this is class-level, indirect evidence and not specific to ramucirumab. For the signet ring and intestinal-type variants, there is only a loose histologic analogy to gastrointestinal adenocarcinoma, which does not establish activity at the cervical site.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15036P | CYRAMZA Concentrate for Solution for Infusion 500mg/50ml | Injection, solution, concentrate | Not stated in the registration record |
| SIN15035P | CYRAMZA Concentrate for Solution for Infusion 100mg/10ml | Injection, solution, concentrate | Not stated in the registration record |

Both products are manufactured by Eli Lilly and Company (with Lilly France-Fegersheim).

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGFR-2 monoclonal antibody), not a conventional cytotoxic |
| Myelosuppression Risk | Low as a single agent; haematological toxicity is mainly driven by combined chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC, blood pressure, urine protein, signs of bleeding or thromboembolism; please refer to the package insert warnings and precautions |
| Handling Protection | Follow institutional hazardous drug handling policy; please refer to the package insert |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high (99.95%), but it rests on the model alone. There are no clinical trials or publications for ramucirumab in this indication, and the evidence level is L5. The safety information is also incomplete.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data, for example from the DrugBank API
- A targeted search for trials and literature on ramucirumab in cervical and gynaecologic adenocarcinomas, starting with cervical cancer
- Route compatibility and similarity-to-original assessments, both still pending
- Preclinical or early-phase evidence of VEGFR-2 dependence in the target histology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

