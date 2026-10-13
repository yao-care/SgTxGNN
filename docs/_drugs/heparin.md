---
layout: default
title: Heparin
parent: Low Evidence (L5)
nav_order: 496
evidence_level: L5
indication_count: 10
---

# Heparin
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

# Heparin: From Pulmonary Embolism and Disseminated Intravascular Coagulation to Thrombophilia due to Protein C Deficiency

## One-Sentence Summary

Heparin is an injectable anticoagulant, originally used for pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency (autosomal recessive)**,
but **no clinical trials and no publications** were found for this indication, so the prediction rests on model output and mechanistic reasoning alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans (the Singapore licence records contain no approved indication text) |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, heparin enhances antithrombin activity and thereby inhibits thrombin and factor Xa. This offsets a hypercoagulable state.

Protein C deficiency removes a key natural brake on coagulation, leaving patients prone to thrombosis. Its severe form can cause purpura fulminans, which is already among heparin's original indications. This overlap is the main reason the prediction is plausible.

This is a mechanistic hypothesis only. No trial or publication was found to confirm it for this condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00720P | Heparin Injection 1,000 iu/ml (Vianex S.A.) | Injection | Not stated |
| SIN11035P | Hanlim Heparin Sodium Injection 25,000 iu/5 ml | Injection | Not stated |
| SIN00714P | Heparin Injection 5,000 iu/ml (Vianex S.A.) | Injection | Not stated |
| SIN01768P | DBL Heparin Sodium Injection BP (Porcine) 1,000 iu/ml | Injection | Not stated |
| SIN01766P | DBL Heparin Sodium Injection BP (Porcine) 5,000 iu/ml | Injection | Not stated |

A sixth licence, SIN12253P (Heparinised Saline Injection 10 iu/ml, B. Braun), is also valid. All six licences are for single-ingredient injectable products.

## Safety Considerations

**Contraindications flagged in the knowledge graph (not from label text):**
liver failure, thrombocytopenia (including heparin-induced thrombocytopenia), blood coagulation disorders (including hemophilia and antithrombin III deficiency), platelet function defects (Glanzmann thrombasthenia), intracranial or intracerebral hemorrhage, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease, biliary tract disease and obstructive jaundice, infective endocarditis, placental abruption, osteoporosis, and several retinal diseases (diabetic and hypertensive retinopathy, retinitis).

**Drug interactions:** 100 interactions were identified. The listed ones include moderate-level interactions with acetylsalicylic acid and with antidiabetic agents (chlorpropamide, glimepiride, glipizide, glyburide, tolbutamide, tolazamide, acetohexamide, repaglinide, nateglinide), as well as with fenfluramine, dexfenfluramine and sibutramine. Interactions with levocarnitine, mannitol, calcitriol, vitamin A, pantoprazole, mesalazine and doxycycline are of unknown severity.

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is biologically plausible, because protein C deficiency is a hypercoagulable state and heparin is already used in purpura fulminans. However, there is no clinical trial or literature support, so the evidence level is L5 (model prediction only). The safety screening cannot proceed without the package insert data.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A targeted literature search on heparin in protein C deficiency and neonatal purpura fulminans, and a clinical trial registry search
- Route compatibility and similarity-to-original-indication assessments, which are still pending

**Other predicted indications reviewed (all currently Hold, except as noted):**

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|---|---|---|---|---|
| 2 | Primary release disorder of platelets | 99.06% | L4 | No mechanistic rationale for heparin; the literature is only thematically adjacent; bleeding risk could increase |
| 3 | Pseudo-von Willebrand disease | 98.65% | L5 | No clear rationale, likely a graph artifact, possible bleeding risk |
| 4 | Atypical hemolytic-uremic syndrome with thrombomodulin anomaly | 96.74% | L5 | Plausible but unvalidated; standard of care is complement inhibition |
| 5 | Painful neuropathy | 96.13% | L4 | Only preclinical HMGB1 papers; the one trial (NCT00445328) compares dalteparin with heparin for VTE prevention and is not relevant |
| 6 | Retinal telangiectasia | 94.88% | L5 | No mechanistic link |
| 7 | Retinal microaneurysm | 94.52% | L5 | Speculative; risk of retinal hemorrhage |
| 8 | Arteriosclerotic retinopathy | 94.52% | L5 | Speculative; shares its score with retinal microaneurysm |
| 9 | Vertebral artery occlusion | 94.22% | L4 | Indirect evidence only; flagged as a research question (S1). Trial [NCT01980316](https://clinicaltrials.gov/study/NCT01980316) is a completed Phase 4 study (n=114) of argatroban, not heparin. The [CADISS RCT (PMID 30801621)](https://pubmed.ncbi.nlm.nih.gov/30801621/) found no clear difference between antiplatelet and anticoagulant therapy in cervical artery dissection |
| 10 | Breast fibrocystic disease | 93.20% | L5 | No credible mechanistic link |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

