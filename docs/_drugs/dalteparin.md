---
layout: default
title: Dalteparin
parent: Low Evidence (L5)
nav_order: 298
evidence_level: L5
indication_count: 10
---

# Dalteparin
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

# Dalteparin: From Pulmonary Embolism and Purpura Fulminans to Protein C Deficiency Thrombophilia

## One-Sentence Summary

Dalteparin is a low-molecular-weight heparin (LMWH) originally used for pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be useful for **thrombophilia due to protein C deficiency (autosomal recessive)**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The support is the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans (from the TxGNN knowledge graph; the Singapore licence has no indication text) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, dalteparin is an LMWH that potentiates antithrombin and inhibits factor Xa, thereby reducing clot formation.

Protein C deficiency causes a strong tendency to clot, and its severe form presents as purpura fulminans, which is already among dalteparin's original indications in the knowledge graph. This overlap with the protein C pathway makes anticoagulation biologically plausible. Any use would be adjunctive only, because LMWH does not replace protein C.

The other predictions are weaker. For several (primary platelet release disorder, pseudo-von Willebrand disease, retinal telangiectasia, retinal microaneurysm, arteriosclerotic retinopathy), an anticoagulant would be expected to add bleeding risk rather than treat the disease, and the scores likely reflect network proximity in the knowledge graph. For atypical haemolytic-uraemic syndrome with thrombomodulin anomaly and thrombotic thrombocytopenic purpura, the rationale is peripheral because complement inhibitors or plasma-based therapy are the standard approach.

## Clinical Trial Evidence

Currently no clinical trials are registered for the top predicted indication.

Among the lower-ranked predictions, one trial was linked to painful neuropathy (rank 5), but it does not support that indication:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00445328](https://clinicaltrials.gov/study/NCT00445328) | Phase 4 | Terminated | 84 | Open-label comparison of dalteparin vs unfractionated heparin for VTE prevention in hospitalised acutely ill medical patients. It does not study painful neuropathy, so it is likely a mismatch, and early termination limits its value. |

## Literature Evidence

Currently no related literature is available for the top predicted indication.

The only publication linked to any prediction (rank 10, vertebral artery occlusion) is indirect preclinical work:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17011126](https://pubmed.ncbi.nlm.nih.gov/17011126/) | 2006 | Preclinical (rat) | Neuroscience Letters | Compared pentosan polysulphate with dalteparin in a rat model of ischaemia-related hippocampal neuronal death. It concerns neuroprotection in an ischaemia model, not vertebral artery occlusion in patients. |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05249P | FRAGMIN INJECTION 2500 iu/ml | Injection | Not stated in the available data |

The product is a single-ingredient injectable made by Pfizer Manufacturing Belgium NV, and its licence is valid.

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Knowledge-graph contraindications (not label text)**: The graph links dalteparin to contraindications in conditions with bleeding risk or coagulation abnormalities. These include heparin-induced thrombocytopenia, thrombocytopenia, haemophilia, blood coagulation disease, antithrombin III deficiency, intracranial and intracerebral haemorrhage, active peptic ulcer disease, liver failure, infective endocarditis, placental abruption, Glanzmann thrombasthenia and qualitative platelet defects. Others are retinal disease and retinopathies (diabetic, hypertensive), inflammatory bowel disease, ulcerative colitis, biliary tract disease, obstructive jaundice and osteoporosis.
- **Drug interactions**: The data compiled for this report list 100 interactions, of which the first 20 were provided. Major interactions include:
  - Antiplatelet and anticoagulant agents: acetylsalicylic acid, abciximab, fondaparinux
  - NSAIDs: ketorolac, ibuprofen
  - Others: acalabrutinib, deferasirox, trastuzumab emtansine, ibritumomab tiuxetan, tositumomab
  
  Moderate interactions include fenfluramine, dexfenfluramine, sibutramine, fluvoxamine, fosinopril, sugammadex and radioiodine agents. Together these mainly point to additive bleeding risk.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has a plausible mechanism, but no trials or publications support it, so the evidence is limited to the model score (L5). The package insert safety review is incomplete, and many of the lower-ranked predictions involve conditions where bleeding risk makes an anticoagulant a poor fit.

**To proceed, the following is needed:**
- The package insert from the HSA website, to complete the warnings and contraindications review
- Mechanism of action data (for example from DrugBank)
- A literature search on LMWH in protein C deficiency and purpura fulminans, including case series
- Expert clinical review of adjunctive use alongside protein C replacement
- Assessment of bleeding risk in the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

