---
layout: default
title: Urokinase
parent: Low Evidence (L5)
nav_order: 1045
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Urokinase: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Pulmonary embolism"
monitor_inn: "Urokinase"
predicted_indications: ["primary release disorder of platelets", "Glanzmann thrombasthenia", "pseudo-von Willebrand disease", "thrombotic thrombocytopenic purpura", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "Scott syndrome", "Ledderhose disease", "palmar fibromatosis", "infantile digital fibromatosis"]
---

# Urokinase
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

# Urokinase: From Pulmonary Embolism to Primary Release Disorder of Platelets

## One-Sentence Summary

Urokinase is a fibrinolytic (clot-dissolving) drug originally used for pulmonary embolism.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but there are **0 clinical trials** and only **3 loosely related publications**, none of which supports this use.
This prediction rests on the model score alone, and the mechanism argues against it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 98.63% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, urokinase is a plasminogen activator. It converts plasminogen to plasmin, which breaks down fibrin clots, and this is why it is used in pulmonary embolism.

Primary release disorder of platelets is a defect of platelet function (granule secretion), not an excess of fibrin clot. Thrombolysis does not address this underlying defect, and a fibrinolytic would be expected to increase bleeding risk. The high score (98.63%) is a network-based prediction and most likely reflects the closeness of platelet and coagulation pathways in the knowledge graph rather than real therapeutic benefit.

The retrieved publications concern cholesterol crystal embolism, coronary thrombosis, and plasma uPA levels in leukaemia. None of them supports this indication.

**Other predicted indications:**
- **Thrombotic thrombocytopenic purpura (TTP)** is the only prediction with a plausible mechanistic rationale (evidence level L4, "Research Question"). Two case reports from the early 1980s describe urokinase use, and preclinical work supports targeted thrombolysis. However, one study suggests plasmin may inactivate ADAMTS13, which could worsen the disease. No trials are registered, and standard care (plasma exchange, immunosuppression, caplacizumab, recombinant ADAMTS13) is well established.
- **Glanzmann thrombasthenia, pseudo-von Willebrand disease, constitutional thrombocytopenia, collagen receptor defects and Scott syndrome** are bleeding disorders. A fibrinolytic is expected to aggravate bleeding in these conditions, and there is no supporting evidence.
- **Ledderhose disease, palmar fibromatosis and infantile digital fibromatosis** are fibrotic conditions. A link through plasmin-mediated matrix remodelling is only speculative, and there is no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32089086](https://pubmed.ncbi.nlm.nih.gov/32089086/) | 2020 | Review | Circulation Research | Cholesterol crystal embolism pathophysiology and therapeutic targets; not specific to this indication |
| [9173723](https://pubmed.ncbi.nlm.nih.gov/9173723/) | 1997 | Review | Zeitschrift fur Kardiologie | Role of coronary thrombosis in chronic myocardial ischaemia; not specific to this indication |
| [1414164](https://pubmed.ncbi.nlm.nih.gov/1414164/) | 1992 | Cohort | Acta Haematologica | High plasma uPA levels in acute non-lymphoblastic leukaemia; not specific to this indication |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11140P | UROKINASE-GREEN CROSS INJ. 60,000 iu/vial | Powder for solution for injection | Not stated in the data compiled for this report |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified, and 20 are listed in the data compiled for this report. Many involve agents that raise bleeding risk. Examples:
  - **Major**: abciximab, apixaban, betrixaban, bivalirudin, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetan, tositumomab (I-131)
  - **Moderate**: acetylsalicylic acid, ibuprofen, ketorolac, celecoxib, diclofenac (topical), aminocaproic acid, omega-3 fatty acids, ginger, fenfluramine, sibutramine

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone, with no registered trials and no supporting literature. Urokinase dissolves clots, whereas platelet release disorders are defects of platelet function, so a fibrinolytic is mechanistically unlikely to help and may increase bleeding.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are currently missing and block safety screening
- Detailed mechanism of action data (MOA)
- Any clinical or mechanistic evidence for urokinase in platelet release disorders, which is unlikely to exist given the mechanism
- If a thrombolytic repurposing direction is pursued, TTP (L4, "Research Question") is the more plausible candidate. It would need mechanistic work on the plasmin–ADAMTS13 concern and controlled data before any clinical consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

