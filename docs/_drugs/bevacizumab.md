---
layout: default
title: Bevacizumab
parent: Low Evidence (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bevacizumab: predicted new indication Epiglottis neoplasm (evidence level L5). Approved use: Ovarian/peritoneal cancer, breast cancer, metastatic colon cancer…"
monitor_inn: "Bevacizumab"
predicted_indications: ["epiglottis neoplasm", "benign neoplasm of tongue", "tumor of testis and paratestis", "benign neoplasm of hypopharynx", "benign neoplasm of floor of mouth", "cervical neuroblastoma", "cystic neoplasm", "nasal cavity inverting papilloma", "mesenchymoma", "schwannoma of jugular foramen"]
---

# Bevacizumab
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

# Bevacizumab: From Ovarian, Breast, Colorectal and Brain Cancers to Epiglottis Neoplasm

## One-Sentence Summary

Bevacizumab is an anti-VEGF antibody originally used for several cancers, including ovarian/peritoneal, breast, metastatic colorectal and glioblastoma.
The TxGNN model predicts it may be effective for **epiglottis neoplasm**, but **no clinical trials and no publications** were found for this specific indication, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian/peritoneal cancer, breast cancer, metastatic colon cancer, glioblastoma (taken from the knowledge-graph indication list, because the Singapore licence records contain no indication text) |
| Predicted New Indication | Epiglottis neoplasm |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 9 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Bevacizumab neutralises VEGF-A, a key driver of tumour angiogenesis. Blocking it starves tumours of new blood supply. This mechanism is not tied to one tumour type, which is why the drug is used across many cancers. Detailed mechanism-of-action data were not available in the data compiled for this report, so this description is based on the drug's known class behaviour.

The epiglottis is part of the head and neck region, and head and neck tumours are often highly vascularised. Anti-VEGF therapy is therefore plausible for this site. However, the model's score of 99.90% is a computational prediction only. No studies specific to epiglottis neoplasm were retrieved. The link to the original indications is therefore a general mechanistic argument, not demonstrated clinical benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Bevacizumab has 9 valid single-ingredient registrations in Singapore, covering the originator and several biosimilars. All are concentrate for solution for infusion. Indication text was not recorded for these licences. The five main ones are listed below.

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN14097P | Avastin 400mg/16ml | Infusion, solution concentrate |
| SIN13065P | Avastin 100mg/4ml | Infusion, solution concentrate |
| SIN16287P | Zirabev 400 mg/16 ml | Infusion, solution concentrate |
| SIN16583P | Abevmy 25mg/ml | Injection, solution, concentrate |
| SIN16810P | Vegzelma 25 mg/ml | Infusion, solution concentrate |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (anti-VEGF-A monoclonal antibody), not a conventional cytotoxic agent |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions |
| Handling Protection | Please refer to the package insert warnings and precautions |

---

## Safety Considerations

- **Drug Interactions**: 22 interaction records were identified. Five are rated Major:
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Panitumumab
  - Sunitinib
  - Thalidomide

  The remaining records are mostly rated Moderate. They include bisphosphonates (e.g. alendronic acid, pamidronic acid), growth factors (filgrastim, pegfilgrastim, sargramostim), radiopharmaceuticals and others.

Warnings and contraindications from the package insert were not available in the data compiled for this report. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for epiglottis neoplasm has the highest model score in this list, but it has no clinical trials and no literature behind it (Evidence Level L5). The anti-angiogenic rationale is plausible but generic, and this is not enough to justify moving forward.

Among the other predicted indications, the only one with strong evidence is "cystic neoplasm" (L1, Proceed with Guardrails). That signal comes mainly from ovarian and peritoneal epithelial tumours, which largely overlap bevacizumab's existing indication, so it is not a true repurposing.

**To proceed, the following is needed:**
- Disease-specific evidence for epiglottis or laryngeal/head and neck tumours (preclinical data, case series or trials)
- Detailed mechanism of action data
- Package insert warnings and contraindications, to complete the safety screening
- Confirmation of the approved indication wording on the Singapore licences
- Safety review of the major interacting drugs, especially sunitinib and panitumumab, if combination use is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

