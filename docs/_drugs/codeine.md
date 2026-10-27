---
layout: default
title: Codeine
parent: Medium Evidence (L3-L4)
nav_order: 276
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Codeine: predicted new indication Nasal cavity disease (evidence level L4). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Codeine"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "trigeminal autonomic cephalalgia", "allergic urticaria", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis", "tracheal disease", "cold urticaria", "bronchial disease"]
---

# Codeine
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

## Codeine: From Cough, Cold and Headache to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid used in cough linctuses and combination analgesics, originally for allergic rhinitis, the common cold, pharyngitis and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but only **1 case report** and **no clinical trials** support this, and the report describes codeine as the cause of the problem rather than a treatment.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (the Singapore licence records contain no approved-indication text) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 20 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, codeine is an opioid analgesic and antitussive. It is widely used in single-ingredient and combination products for cough, cold and pain, and these uses are the basis for its original indications of rhinitis, pharyngitis, common cold and headache.

The predicted indication, nasal cavity disease, is anatomically close to these upper-airway conditions. The high TxGNN score most likely reflects this closeness in the knowledge graph rather than a therapeutic mechanism.

The only publication found is a case report of rhinolithiasis (a nasal stone) formed around a hardened mixture of codeine and opium, in which codeine was the cause of the pathology. No credible therapeutic mechanism for nasal cavity disease was identified, so the prediction is not supported.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose & Throat Journal | A 21-year-old man had a rhinolith formed around an impacted foreign body, a hardened codeine and opium mixture wrapped in nylon (an "opioma"). The stone was removed under local anaesthesia. |

## Singapore Market Information

There are 20 valid single-ingredient registrations. The five main ones are listed below. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN03413P | COLINCTUS 10 MIXTURE 10 mg/5 ml | Elixir | Not stated in the records |
| SIN03699P | L.T.R. COUGH LINCTUS 10 mg/5 ml | Elixir | Not stated in the records |
| SIN07044P | CODEINE TABLETS 30 mg | Tablet | Not stated in the records |
| SIN06330P | PARACETAMOL CODEINE TABLETS | Tablet | Not stated in the records |
| SIN13319P | Codipront Capsule | Capsule, extended release | Not stated in the records |

## Safety Considerations

- **Contraindication signals (from the knowledge graph, not label text):** The graph links codeine to contraindications in hypertensive disorder, liver failure and liver disease, kidney disease, epilepsy, chronic obstructive pulmonary disease, pancreatitis, gallbladder disease, porphyria, hypothyroidism, thrombocytopenia, peptic ulcer disease, inflammatory bowel disease, gastritis, insomnia, anxiety and other mental disorders (including psychotic disorders), and dermatitis herpetiformis.
- **Drug interactions:** The interaction query returned 100 records. Major interactions include **alvimopan** and **bupropion**. Moderate interactions include anticholinergics (atropine, clidinium, dicyclomine, glycopyrronium, hyoscyamine), antidiarrhoeals (loperamide, kaolin, attapulgite), 5-HT3 antagonists (dolasetron, granisetron), cimetidine, dexamethasone, dronabinol, eliglustat, eluxadoline, fenfluramine and dexfenfluramine, and glycerol phenylbutyrate.
- **Literature-based concerns:**
  - Codeine directly triggers mast cell histamine release. It is used as a skin-test stimulus and can cause urticaria.
  - It can cause bronchoconstriction in asthmatic patients.
  - There is a mortality signal for misuse of paracetamol/codeine preparations.

Please also refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a single case report in which codeine caused the nasal pathology. There are no trials and no therapeutic mechanism, so this is a model artefact based on graph proximity to rhinitis and the common cold. The other predicted indications do not offer a better opportunity. Most are prediction-only or overlap with existing cough and cold use. Allergic urticaria and cold urticaria are safety concerns, since codeine triggers rather than treats them.

**To proceed, the following is needed:**
- Mechanism of action data for codeine, to support any mechanistic-link analysis
- The package insert warnings and contraindications from the Singapore regulator (HSA), which are required before safety screening can proceed
- Clinical evidence of benefit in nasal cavity disease, which is currently absent
- A risk-benefit review covering the contraindication signals and interactions above, before any further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

