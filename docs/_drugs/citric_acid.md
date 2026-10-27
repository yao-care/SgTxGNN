---
layout: default
title: Citric Acid
parent: Medium Evidence (L3-L4)
nav_order: 257
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Citric Acid: predicted new indication Stomach disease (evidence level L4). Approved use: Dyspepsia"
monitor_inn: "Citric acid"
predicted_indications: ["stomach disease", "pharyngitis", "acute laryngopharyngitis", "postgastrectomy syndrome", "nasal cavity disease", "papillary conjunctivitis", "blepharoconjunctivitis", "rhinitis", "thrombotic disease", "ulcerative blepharitis"]
---

# Citric Acid
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

## Citric Acid: From Dyspepsia to Stomach Disease
{: .text-alpha }

## One-Sentence Summary

Citric acid is already used for dyspepsia and headache disorder in the knowledge base, and in Singapore it is marketed in oral solution, powder and granule products.
The TxGNN model predicts it may be useful for **stomach disease** (score 99.74%), but **no clinical trials** are registered and the 20 publications retrieved are mostly indirect (reviews, diagnostic or metabolomics studies), so this remains a computational prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dyspepsia; headache disorder (from the knowledge graph; no approved indication text in the Singapore registrations) |
| Predicted New Indication | Stomach disease |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, citric acid is an organic acid that is already associated with dyspepsia, a gastric condition. A link to stomach disease is therefore plausible through its effects on gastric acidity and mucosal physiology.

The relationship between the original and new indication is close: both involve the stomach. However, the literature found is indirect. The most relevant item is a diagnostic study using a citric acid test meal to improve the accuracy of the 13C-urea breath test for *H. pylori*. That is a diagnostic aid, not a treatment. The very high TxGNN score reflects network similarity, not demonstrated therapeutic benefit.

Other predicted indications were also screened. Rhinitis (L4) and thrombotic disease (L4) have only indirect evidence. Pharyngitis, acute laryngopharyngitis, postgastrectomy syndrome, nasal cavity disease, papillary conjunctivitis, blepharoconjunctivitis and ulcerative blepharitis have no meaningful support (L5).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The table lists the most relevant items for stomach disease. None is a randomised trial of citric acid as a treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | Clinical diagnostic study | Gut and Liver | Editorial-type discussion of whether a citric acid meal improves 13C-urea breath test accuracy in Asian populations |
| [30970440](https://pubmed.ncbi.nlm.nih.gov/30970440/) | 2019 | Clinical diagnostic study | Gut and Liver | Effect of citric acid on 13C-urea breath test accuracy after *H. pylori* eradication, in a region with frequent atrophic gastritis |
| [15854177](https://pubmed.ncbi.nlm.nih.gov/15854177/) | 2005 | Clinical physiology | Aliment Pharmacol Ther | Compares citric, malic and ascorbic acid effects on intragastric urease activity |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | Diet in peptic ulcer disease; restrictive diets are not supported in the H2-inhibitor era |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | Physiology and metabolism of *Helicobacter pylori* |
| [7106518](https://pubmed.ncbi.nlm.nih.gov/7106518/) | 1982 | Clinical physiology | Gastroenterology | Salivary secretion in reflux oesophagitis patients versus controls |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | Metabolomics | Metabolomics | Higher serum citric acid and L-carnitine detected in Koreans before gastric cancer onset (a biomarker finding) |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05148P | POTCIT MIXTURE | Solution | Not stated in the data |
| SIN06732P | POTASSIUM CITRATE MIXTURE BP | Solution | Not stated in the data |
| SIN17163P | PICO-SWIFT POWDER FOR ORAL SOLUTION | Powder, for solution | Not stated in the data |
| SIN06442P | E-Z-GAS II GRANULES | Granule | Not stated in the data |
| SIN14374P | Ural Effervescent Granules | Granule, effervescent | Not stated in the data |

All five registrations are valid single-ingredient products.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph (not label text):** hypertension, kidney disease and impaired renal function, anuria, liver disease, congestive heart failure, adrenal insufficiency (including Addison disease and congenital adrenal hyperplasia), peptic ulcer disease, gout, hypercalcaemia, nephrocalcinosis, thrombocytopenia, anaemia, hemophilia, chronic diarrhoeal disease, and substance abuse/dependence. These should be verified against official labelling. The peptic ulcer disease signal deserves attention given the stomach-related prediction.
- **Drug Interactions:** 15 interactions were identified.
  - **Major:** aluminium hydroxide.
  - **Moderate:** fluoroquinolone and quinolone antibiotics (ciprofloxacin, levofloxacin, moxifloxacin, norfloxacin, ofloxacin, enoxacin, gatifloxacin, gemifloxacin, lomefloxacin, sparfloxacin, trovafloxacin, grepafloxacin, cinoxacin, nalidixic acid).
- For thrombotic disease, systemic use would raise safety concerns such as hypocalcaemia.

Please refer to the package insert for full warnings and contraindications, as label data were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for stomach disease is plausible given the existing dyspepsia link, but the evidence is indirect: there are no registered trials, and the only citric-acid-specific clinical work concerns a diagnostic breath-test meal. The Singapore registrations carry no approved indication text, and the knowledge graph lists many contraindication signals, including peptic ulcer disease.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA (a blocking gap for safety screening)
- Mechanism of action data (for example from DrugBank)
- Clinical evidence of therapeutic benefit in a gastric condition, such as a pilot or randomised trial with a defined formulation and dose
- Clarification of the approved indications of the local products
- Review of the contraindication signals (especially peptic ulcer disease) and the aluminium hydroxide interaction for the intended use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

