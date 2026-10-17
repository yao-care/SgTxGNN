---
layout: default
title: Tenecteplase
parent: Medium Evidence (L3-L4)
nav_order: 962
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Tenecteplase: predicted new indication Posterolateral myocardial infarction (evidence level L4). Approved use: Myocardial infarction…"
monitor_inn: "Tenecteplase"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "pyruvate kinase deficiency of red cells"]
---

# Tenecteplase
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **10** 
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

# Tenecteplase: From Myocardial Infarction to Posterolateral Myocardial Infarction

## One-Sentence Summary

Tenecteplase is a fibrin-specific clot-dissolving drug, originally used to treat myocardial infarction and coronary thrombosis.
The TxGNN model predicts it may be effective for **posterolateral myocardial infarction**, an anatomical subtype of the already-treated condition.
There are currently **0 clinical trials** and **0 publications** specific to this subtype, so the support is inferred from the parent indication and not from subtype-specific data.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myocardial infarction, coronary thrombosis (hemoglobinopathy is also listed in the knowledge graph). The Singapore licence text carries no approved indication wording. |
| Predicted New Indication | Posterolateral myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, tenecteplase is a fibrin-specific tissue plasminogen activator. It converts plasminogen to plasmin at the clot surface, which dissolves fibrin in blocked coronary arteries.

Posterolateral myocardial infarction is a regional subtype of acute myocardial infarction, which is already an original indication. The mechanistic link is therefore direct. In practice, this is largely covered by the existing indication and is not a true repurposing. The prediction is supported by reasoning from the parent condition (ST-elevation MI), not by subtype-specific studies.

Other predictions from the same model, such as posteroinferior and septal myocardial infarction, follow the same logic. Several other high-scoring predictions (chromosomal deletion, red cell enzyme and membrane disorders) have no plausible mechanistic link and appear to be knowledge-graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for posterolateral myocardial infarction.

For context, literature on neighbouring predictions is indirect:
- **Septal MI**: reports cover tenecteplase in pulmonary embolism, a pulmonary embolism that mimicked septal MI, and a ventricular septal rupture complication. None provides controlled efficacy data.
- **Coronary stenosis**: studies include a small randomised feasibility and safety study of low-dose intracoronary tenecteplase during primary PCI (ICE T-TIMI 49, 40 patients, [PMID 31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/)) and a trial of facilitated angioplasty with tenecteplase versus tenecteplase alone (CAPITAL AMI, [PMID 16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/)). The rest are case reports or only loosely related.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12015P | METALYSE FOR INJECTION 10,000 u/vial | Injection, powder, for solution | Not stated in the registration record |

Manufacturer: Boehringer Ingelheim Pharma GmbH & Co KG. The registration is valid and the product is a single-ingredient injectable.

---

## Safety Considerations

**Drug Interactions**: The interaction screening returned 100 entries. Those shown include the following:
- **Major**: abciximab, apixaban, betrixaban, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetan, tositumomab. Most of these affect bleeding risk, which is expected when combined with a clot-dissolving drug.
- **Moderate**: acetylsalicylic acid, ibuprofen, ketorolac, celecoxib, diclofenac (topical), aminocaproic acid, omega-3 fatty acids, fenfluramine, dexfenfluramine, sibutramine.

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predicted indication is a subtype of an indication tenecteplase already covers, so the model prediction adds little new information. No subtype-specific trials or publications exist, and the safety review cannot proceed because package insert data is missing. Evidence stays at L4.

**To proceed, the following is needed:**
- The HSA package insert, to confirm the approved indication wording and obtain warnings and contraindications
- Mechanism of action data from DrugBank
- Confirmation of whether posterolateral MI falls within the existing STEMI indication, which would make a separate repurposing case unnecessary
- A review of bleeding-related interactions (anticoagulants, antiplatelets, NSAIDs) for any proposed use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

