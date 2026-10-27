---
layout: default
title: Fondaparinux
parent: Low Evidence (L5)
nav_order: 451
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fondaparinux: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Pulmonary embolism"
monitor_inn: "Fondaparinux"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Ledderhose disease", "vertebral artery occlusion", "arteriosclerotic retinopathy", "retinal microaneurysm", "infantile digital fibromatosis", "palmar fibromatosis", "retinal telangiectasia"]
---

# Fondaparinux
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

## Fondaparinux: From Pulmonary Embolism to Primary Release Disorder of Platelets
{: .text-alpha }

## One-Sentence Summary

Fondaparinux is an injectable anticoagulant, originally used for pulmonary embolism (thromboembolic disease).
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and **1 publication** (unrelated to this indication) supporting this direction.
The prediction is computational only and is mechanistically implausible, because an anticoagulant would be expected to worsen a bleeding-type platelet disorder.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 93.06% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 4 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, fondaparinux is an indirect factor Xa inhibitor that acts through antithrombin III. Its efficacy in preventing and treating venous thromboembolism, including pulmonary embolism, is established.

Primary release disorder of platelets is a bleeding-type platelet function defect. Reducing coagulation would be expected to aggravate bleeding rather than treat the condition. The high TxGNN score therefore appears to reflect proximity between coagulation and platelet terms in the knowledge graph, not a genuine therapeutic relationship.

The other top predictions show the same pattern. Pseudo-von Willebrand disease and Glanzmann thrombasthenia are bleeding disorders where anticoagulation is likely harmful. Ledderhose disease, palmar fibromatosis and infantile digital fibromatosis are fibroproliferative disorders with no established link to factor Xa inhibition. Retinal conditions (arteriosclerotic retinopathy, retinal microaneurysm, retinal telangiectasia) carry intraocular bleeding concerns. Vertebral artery occlusion (L4, flagged as a research question) is the only prediction with a biologically plausible antithrombotic rationale. However, the evidence for venous disease does not transfer directly to arterial disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30018843](https://pubmed.ncbi.nlm.nih.gov/30018843/) | 2017 | Case report/Review | Journal of the Advanced Practitioner in Oncology | Case study of palliative chemotherapy and palliative care in a young patient with metastatic adenocarcinoma. It is unrelated to platelet release disorders or fondaparinux. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13587P | Arixtra Solution for Injection 5.0 mg/0.4 ml | Injection, solution | Not stated in the available data |
| SIN16809P | Diviti Solution for Injection in Pre-filled Syringe 2.5 mg/0.5 ml | Injection, solution | Not stated in the available data |
| SIN12059P | Arixtra Solution for Injection 2.5 mg/0.5 ml | Injection | Not stated in the available data |
| SIN13586P | Arixtra Solution for Injection 7.5 mg/0.6 ml | Injection, solution | Not stated in the available data |

All four are single-ingredient products with valid status. None are cancelled.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text)**: Fondaparinux is linked to contraindication in kidney disease, thrombocytopenia (including heparin-induced and immune thrombocytopenia), blood coagulation disease, anaemia, diabetic retinopathy, diabetic cataract, endocarditis and subacute bacterial endocarditis. Several of these overlap with the predicted bleeding-type indications, which reinforces the safety concern.
- **Drug Interactions**: 100 interactions were found. Major interactions include:
  - Antiplatelet and anti-inflammatory agents: acetylsalicylic acid, abciximab, ketorolac, ibuprofen
  - Other antithrombotic or platelet-active agents: anagrelide, antithrombin alfa, antithrombin III human
  - Other: deferasirox, acalabrutinib, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab

  Moderate interactions include fenfluramine, dexfenfluramine, sibutramine, sugammadex, ketorolac (ophthalmic) and radioiodine (I-131, I-123).

Please refer to the package insert for key warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone, with no trials and no relevant literature. An anticoagulant is mechanistically opposed to treating a bleeding-type platelet disorder, and the knowledge graph also lists related blood disorders as contraindications.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Singapore regulator (HSA), which are required for safety screening
- Detailed mechanism of action data
- Relevant mechanistic or preclinical evidence showing a plausible therapeutic link, if any exists
- Consideration of vertebral artery occlusion as a separate research question, since it is the only top prediction with a plausible antithrombotic rationale
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

