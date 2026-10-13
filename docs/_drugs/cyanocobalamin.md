---
layout: default
title: Cyanocobalamin
parent: Low Evidence (L5)
nav_order: 283
evidence_level: L5
indication_count: 10
---

# Cyanocobalamin
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

# Cyanocobalamin: From Vitamin B12 Deficiency to Biotin Metabolic Disease

## One-Sentence Summary

Cyanocobalamin (vitamin B12) was originally used to treat vitamin B12 deficiency and related anaemias, including pernicious anaemia.
The TxGNN model predicts it may be effective for **biotin metabolic disease**, but there are **0 clinical trials** and only **1 publication** (an industrial vitamin-production review with no clinical relevance), so the prediction rests almost entirely on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin B12 deficiency, pernicious anaemia, folic acid deficiency anaemia, iron deficiency anaemia and other deficiency anaemias (the Singapore licence records contain no approved-indication text, so these come from the drug's knowledge-graph indications) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 14 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, cyanocobalamin is a water-soluble B vitamin. Its efficacy in B12 deficiency and pernicious anaemia is well established, and mechanistically it may overlap with biotin-related pathways.

Both cyanocobalamin and biotin act as cofactors in enzyme reactions linked to propionyl-CoA and methylmalonyl-CoA metabolism. This pathway-level overlap makes the prediction plausible on paper.

However, the link is weak in practice. Biotin metabolic disorders (for example biotinidase or holocarboxylase synthetase deficiency) are treated with biotin itself, and no data show that cobalamin corrects the underlying defect. The high score most likely reflects network proximity among vitamin-related nodes in the knowledge graph rather than a true therapeutic signal.

Other top-ranked predictions (inborn error of biotin metabolism, esophageal malformation, several inflammatory myopathies, CD59 deficiency) have no clinical evidence and mostly no plausible mechanism. They appear to be graph artifacts.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1368195](https://pubmed.ncbi.nlm.nih.gov/1368195/) | 1992 | Review | J Chem Technol Biotechnol | Biotechnological production of vitamins and coenzymes; not clinical and not about treating biotin disorders |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07876P | Vitamin B12 Injection 1000 mcg/ml | Injection | Not stated in the data |
| SIN06258P | Neurobion Tablet | Tablet, sugar coated | Not stated in the data |
| SIN12077P | Daneuron Tablet | Tablet, film coated | Not stated in the data |
| SIN15098P | Neurobion Tablet (OTC) | Tablet, sugar coated | Not stated in the data |
| SIN10891P | Neuro-B Tablet | Tablet, film coated | Not stated in the data |

There are 14 valid single-ingredient registrations in total, covering injectable and oral tablet forms. Only the first five are listed here.

---

## Safety Considerations

- **Drug Interactions**: The interaction screen found 100 interacting drugs. The entries reviewed were mostly minor, including acid-suppressing drugs (famotidine, ranitidine, cimetidine, omeprazole, pantoprazole, esomeprazole, lansoprazole, rabeprazole, dexlansoprazole, nizatidine) and potassium chloride. Several other entries have an unknown severity level, including metformin, doxycycline, mesalazine, acarbose, glimepiride, rosiglitazone, sucralfate and morphine.

Please refer to the package insert for other safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by model scoring (L5). There are no clinical trials, the single publication is unrelated to treatment, and biotin disorders are already treated with biotin itself, so there is no clear rationale for using cyanocobalamin.

**To proceed, the following is needed:**
- Mechanism of action data for cyanocobalamin
- Package insert warnings and contraindications from the HSA
- Any biochemical or clinical evidence that cobalamin affects biotin-dependent enzyme function
- Review of the other predicted indications; only the proteinuria prediction has indirect evidence (as a feature of hereditary B12 malabsorption), and cyanocobalamin there treats the deficiency, not the proteinuria
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

