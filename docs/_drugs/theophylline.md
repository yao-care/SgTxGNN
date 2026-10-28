---
layout: default
title: Theophylline
parent: Low Evidence (L5)
nav_order: 979
evidence_level: L5
indication_count: 6
monitor_inn: "Theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-28
description: "Theophylline: predicted new indication Thrombotic disease (evidence level L5). Approved use: Asthma, bronchitis, pulmonary emphysema and related airway diseases"
---

# Theophylline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Theophylline: From Asthma to Thrombotic Disease
{: .text-alpha }

## One-Sentence Summary

Theophylline is a bronchodilator originally used for asthma, bronchitis and emphysema.
The TxGNN model predicts it may be effective for **thrombotic disease**, but **no clinical trials** and **no publications that directly study this question** were found.
The prediction is therefore supported by the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Asthma, bronchitis, pulmonary emphysema and related airway diseases (relations recorded in the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 0.9962 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Theophylline is generally known as a non-selective phosphodiesterase inhibitor and adenosine receptor antagonist. In theory, raising cAMP in platelets could reduce platelet aggregation, which is the only link to thrombosis.

This link is hypothetical. The retrieved papers do not test theophylline as an antithrombotic. They cover ticlopidine pharmacokinetics, blood-sample processing, platelet biomarker assays and a theophylline sensor, and theophylline appears only as an analyte or incidental reagent. The high model score is not backed by clinical data.

Thrombosis is also a different therapeutic area from the airway diseases theophylline is used for, so this would be a true new-area extension rather than a modest broadening.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No retrieved paper directly studies theophylline for thrombotic disease. The closest items are listed below, and all are indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Pharmacokinetics of the antiplatelet drug ticlopidine; not about theophylline |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Prostaglandins, platelet aggregation and atherosclerosis; background on cAMP and platelets |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratory study | General Pharmacology | Milrinone and adenosine inhibit platelet aggregation through cAMP; theophylline not the subject |
| [749930](https://pubmed.ncbi.nlm.nih.gov/749930/) | 1978 | Methods | British Journal of Haematology | Platelet factor 4 assay; theophylline used only as an anticoagulant additive |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Methods | Platelets | Soluble CLEC-2 measurement as a platelet activation marker |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Sensor development | Analytica Chimica Acta | Electrochemical detection of theophylline; no therapeutic data |

## Singapore Market Information

The licence records contain no approved indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN11399P | NUELIN-SR 125 TABLET | Tablet | Not stated in the records |
| SIN10679P | NUELIN-SR 250 TABLET | Tablet | Not stated in the records |
| SIN03139P | THEOPHYLLINE TABLETS 100 mg | Tablet | Not stated in the records |
| SIN09668P | APO-THEO LA TABLET 200 mg | Tablet | Not stated in the records |
| SIN10158P | APO-THEO LA TABLET 100 mg | Tablet | Not stated in the records |

Three further licences are held: APO-THEO LA 300 mg, THEOLIN SR 250 mg (film-coated tablet) and NUELIN syrup 80 mg/15 ml.

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications** (not label text): hypertension, liver failure and liver disease, kidney disease, epilepsy, anxiety and other mental disorders, porphyria, hypothyroidism, peptic ulcer disease, open-angle glaucoma, diabetes and diabetic ketoacidosis, benign prostatic hyperplasia, thrombocytopenia, neutropenia and agranulocytosis. Thrombocytopenia and neutropenia are particularly relevant when a drug is considered for a thrombosis setting.
- **Drug Interactions**: 100 interactions were found. The one shown at Major level is **bupropion**. Moderate-level interactions include famotidine, ranitidine, cimetidine, omeprazole, rabeprazole, clarithromycin, doxycycline, tetracycline, minocycline and systemic corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide).
- Theophylline has a narrow therapeutic window, so any new use would need blood-level monitoring.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No trials or directly relevant publications exist for thrombotic disease. The mechanistic link is only hypothetical, and the high TxGNN score is unsupported by clinical data. Evidence level is L5.

**To proceed, the following is needed:**
- Mechanism of action data and the package insert warnings and contraindications
- Preclinical platelet aggregation and thrombosis studies of theophylline itself
- A comparison against existing antiplatelet and anticoagulant options
- A safety review given the narrow therapeutic index and listed interactions

**Other predictions reviewed (for context):**
Among the other predictions, **nasal cavity disease** (allergic rhinitis) and **tracheal disease** have the most support, both at L3 and rated as research questions. For nasal cavity disease, a small controlled study of slow-release theophylline in allergic rhinitis (PMID 9648963) gives direct but limited human evidence. For tracheal disease, the support is preclinical, veterinary or indirect. Laryngotracheitis, pharyngitis and acute laryngopharyngitis have no supporting clinical evidence and are all on Hold.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

