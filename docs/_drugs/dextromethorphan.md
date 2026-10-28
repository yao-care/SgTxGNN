---
layout: default
title: Dextromethorphan
parent: Low Evidence (L5)
nav_order: 324
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Dextromethorphan"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
description: "Dextromethorphan: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Dextromethorphan: Nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Dextromethorphan is a widely used cough suppressant, with original indications covering allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
This is a model-only prediction with a very high score and no direct evidence behind it.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 18 of 18) |
| Number of Registrations | 18 (valid: 18) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, dextromethorphan is an antitussive that acts as an NMDA receptor antagonist and sigma-1 receptor agonist, with central effects on the cough reflex. It has no established mechanism for nasal pathology.

The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as the approved rhinitis and common cold indications, not biological evidence. Any benefit would at most be symptomatic, and the prediction should be treated as a hypothesis only.

Other top-ranked predictions show the same pattern:

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 3 | Faucial diphtheria | 0.9936 | L5 | No antibacterial or antitoxin activity; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence |
| 4 | Trigeminal autonomic cephalalgia | 0.9932 | L5 | Plausible but unverified link via NMDA antagonism and headache |
| 5 | Cervical disc degenerative disorder | 0.9930 | L5 | Speculative effect on neuropathic pain only |
| 6 | Allergic urticaria | 0.9925 | L5 | No antihistaminic activity; likely driven by allergic rhinitis proximity |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for nasal cavity disease.


| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [2255670](https://pubmed.ncbi.nlm.nih.gov/2255670/) | 1990 | In vitro | Pharmacology & Toxicology | Effects of dextromethorphan, vadocaine, diphenhydramine and hydroxyzine on ciliary beat frequency in rat tracheal explants; relevant to mucociliary function but does not show therapeutic benefit |
| [952583](https://pubmed.ncbi.nlm.nih.gov/952583/) | 1976 | Preclinical | Arch Int Pharmacodyn Ther | Antitussive properties of butorphanol (a different drug) compared with codeine and dextromethorphan in guinea pigs and dogs |

---

## Singapore Market Information

All 18 licences are valid single-ingredient registrations with no cancellations. Approved indication text is not available in the licence records. Five main authorisations are listed below.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN02810P | Beathorphan Elixir 15 mg/5 ml | Elixir | Not available |
| SIN06770P | Tussidex Forte Linctus 15 mg/5 ml | Elixir | Not available |
| SIN08825P | Strepsils Cough for Dry Cough Lozenges 5 mg | Lozenge | Not available |
| SIN02653P | Beathorphan Tablets 15 mg | Tablet, film coated | Not available |
| SIN13992P | Sunthorphan Syrup 15 mg/5 ml | Syrup | Not available |

Available forms include elixir, syrup, lozenge, tablet (plain, sugar-coated and film-coated) and gelatin-coated capsule.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension, long QT syndrome and torsades de pointes, liver failure and liver disease, epilepsy, COPD, kidney disease, peptic and gastric ulcer, pancreatitis, thrombocytopenia, diabetes and diabetic ketoacidosis, adrenocortical insufficiency, hypothyroidism, benign prostatic hyperplasia, bronchitis, and hypotensive disorder, among others. These should be verified against the package insert.
- **Drug Interactions:** 100 interactions were identified. Major interactions include:
  - Serotonergic agents: dexfenfluramine, fenfluramine, lorcaserin, sibutramine
  - 5-HT3 antagonists (QT-related): dolasetron, granisetron, ondansetron, palonosetron
  - Moderate interactions include bupropion, cimetidine, morphine, opium, metoclopramide, dronabinol, nabilone, eliglustat, mazindol, phentermine and glycerol phenylbutyrate.

Please refer to the package insert for warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a high model score, probably driven by proximity to existing rhinitis and common cold indications. There are no trials or literature for nasal cavity disease, and no established mechanism links dextromethorphan to nasal pathology. The evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and a clear rationale for nasal disease
- Package insert warnings and contraindications from the Singapore regulator (HSA), and the approved indication text for each licence
- A literature and trial search specific to nasal cavity disease, to look for any clinical signal
- Safety review of the knowledge-graph contraindication signals and major interactions (serotonergic and QT-prolonging drugs)
- Consideration of whether a more plausible candidate merits evaluation first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

