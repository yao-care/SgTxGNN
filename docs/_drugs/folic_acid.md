---
layout: default
title: Folic Acid
parent: Medium Evidence (L3-L4)
nav_order: 449
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L4). Approved use: Vitamin deficiency disorder"
monitor_inn: "Folic acid"
predicted_indications: ["biotin metabolic disease", "non-syndromic esophageal malformation", "esophageal disease", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "Plummer-Vinson syndrome", "inborn error of biotin metabolism", "Ureaplasma urethritis", "gonococcal urethritis", "esophageal ulcer", "urinary tract infection (disease)"]
---

# Folic Acid
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

# Folic Acid: From Folate-Deficiency Anaemia to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid is a B-vitamin used to treat vitamin deficiency and deficiency-related anaemias, including folic acid deficiency anaemia and iron deficiency anaemia.
The TxGNN model predicts it may be effective for **biotin metabolic disease**, but there are **no clinical trials** and only general vitamin reviews (**20 publications retrieved, none directly testing folic acid for this condition**).
This prediction rests on model output alone and is not supported by direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; folic acid deficiency anaemia; iron deficiency anaemia; hypochromic, microcytic and other deficiency anaemias (from the knowledge graph; the Singapore licence records contain no indication text) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, folic acid is a B-vitamin cofactor in one-carbon metabolism. Its efficacy in folate-deficiency anaemia is established, and it may be mechanistically related to other vitamin-responsive disorders.

Folate and biotin are both B-vitamin cofactors, and vitamin-responsive disorders are often reviewed together. This is probably why the model links them. However, the link is indirect. Folic acid does not replace biotin, and biotinidase or holocarboxylase synthetase deficiencies are treated with biotin itself. The retrieved literature consists of general vitamin reviews with no direct evidence for folic acid in this condition.

Other predictions for this drug were also examined. Most are weaker than the top-ranked one: they have no supporting evidence (for example Ureaplasma and gonococcal urethritis, where folic acid has no antimicrobial role) or are too broad to support a specific indication (for example "esophageal disease"). Plummer-Vinson syndrome (dysphagia, oesophageal webs and iron-deficiency anaemia) is the most clinically plausible, as folate may be supportive, but evidence is limited to a case report and a single-centre prospective study.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for biotin metabolic disease.

---

## Literature Evidence

The most relevant publications are listed below. All are reviews or general papers, and none test folic acid for biotin metabolic disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Vitamin-responsive disorders (cobalamin, folate, biotin, B1, E); inborn errors of vitamin absorption, transport and metabolism |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | International Journal of Molecular Sciences | Vitamin B12 deficiency and the nervous system; B12, biotin and folate act in linked metabolic reactions |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases: malabsorption, metabolic errors and vitamin-dependent syndromes |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | B vitamins in cellular metabolism and erythrocyte synthesis |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; thiamine, pyridoxine and biotin levels lower in diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | Vitamins (including biotin) and type 2 diabetes |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Combined vitamin H (biotin) and folic acid deficiency induced in rats on a purified diet |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN12633P | EUROFER CHEW TABLETS | Tablet | Not stated in the available records |
| SIN05209P | SOLUVIT N FOR INFUSION | Powder for solution for injection | Not stated in the available records |
| SIN11975P | CERNEVIT FOR INJECTION | Powder for solution for injection | Not stated in the available records |

All three licences are valid single-ingredient registrations. Routes available are oral and injectable.

---

## Safety Considerations

- **Contraindication signals (knowledge-graph associations, not label text)**: The knowledge graph links folic acid to many conditions, including kidney disease, nephrolithiasis, sickle cell anaemia, haemolytic anaemia, hereditary haemochromatosis, Wilson disease, diabetes mellitus, diabetic ketoacidosis, hyperparathyroidism, hypercalcaemia, inflammatory bowel disease, ulcerative colitis, peptic ulcer disease, bipolar disorder and sarcoidosis. These need clinical verification against the package insert.
- **Drug Interactions**: 100 interactions were found. The only graded ones in the list reviewed are **Pancrelipase (Moderate)** and **Sulfasalazine (Minor)**. Others, such as metformin, omeprazole, pantoprazole, lansoprazole, mesalazine and prednisone, are of unknown severity.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (99.49%), but the evidence level is L4: no trials exist, and the literature is general vitamin reviews. The mechanistic link to biotin metabolic disease is indirect, since biotin itself is the standard treatment. Other predicted indications are no stronger, apart from Plummer-Vinson syndrome, which may be worth a separate look as a research question.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (currently a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Direct evidence, such as case series or controlled studies, of folic acid in biotin-related disorders
- Evaluation of Plummer-Vinson syndrome as an alternative, clinically more plausible candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

