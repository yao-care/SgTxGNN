---
layout: default
title: Biotin
parent: Low Evidence (L5)
nav_order: 163
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Biotin: predicted new indication Dyspepsia (evidence level L5). Approved use: Nutritional biotin deficiency"
monitor_inn: "Biotin"
predicted_indications: ["dyspepsia", "gastroparesis (disease)", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "familial visceral myopathy", "anemia of prematurity", "congenital prothrombin deficiency", "cystinosis", "obsolete contact dermatitis caused by poison oak"]
---

# Biotin
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

# Biotin: From Nutritional Biotin Deficiency to Dyspepsia

## One-Sentence Summary

Biotin (vitamin B7) is a water-soluble vitamin originally used to treat nutritional biotin deficiency.
The TxGNN model predicts it may be effective for **dyspepsia** (score 99.4%), but **no clinical trials** are registered for this use, and the 6 publications retrieved do not show that biotin treats dyspepsia.
The evidence is currently prediction only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Nutritional biotin deficiency (the approved indication text on the Singapore licences is blank) |
| Predicted New Indication | Dyspepsia |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, biotin is a cofactor for carboxylases involved in fatty acid, amino acid and glucose metabolism. Its efficacy in correcting biotin deficiency is established, but no mechanistic route to dyspepsia is evident.

The literature retrieved for dyspepsia does not support the prediction. It covers:
- A case of biotin deficiency in an infant who had been diagnosed with dyspepsia and fed only an amino acid formula. Here dyspepsia was background, not a condition treated by biotin.
- Studies of stomach endocrine cells in irritable bowel syndrome.
- A study of gut microbiota in patients with lung disease taking a multi-ingredient supplement.
- Studies of H. pylori gastritis and of IgA nephropathy.

None of these shows that biotin improves dyspepsia. The high TxGNN score is a computational prediction without clinical support.

For context, other predictions with limited or indirect evidence:
- **Biotin metabolic disease** (score 92.1%) has the strongest supporting material: 6 trials and many reviews. These are mainly high-dose biotin studies in other diseases, so the support is indirect.
- **Vitamin deficiency disorder** overlaps with the existing label and is not a true repurposing signal.
- **Gastroparesis** (score 99.4%) has no trials or literature.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for dyspepsia.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [15863846](https://pubmed.ncbi.nlm.nih.gov/15863846/) | 2005 | Case report | The Journal of Dermatology | Biotin deficiency in an infant on amino acid formula who had been diagnosed with dyspepsia as a neonate |
| [25110039](https://pubmed.ncbi.nlm.nih.gov/25110039/) | 2014 | Cohort | International Journal of Molecular Medicine | Stomach antral endocrine cells in IBS patients; no biotin treatment |
| [24891930](https://pubmed.ncbi.nlm.nih.gov/24891930/) | 2014 | Cohort | World Journal of Gastrointestinal Endoscopy | Endocrine cells in oxyntic mucosa in IBS; no biotin treatment |
| [21695955](https://pubmed.ncbi.nlm.nih.gov/21695955/) | 2011 | Review | Eksperimental'naia i Klinicheskaia Gastroenterologiia | Prebiotic and vitamin supplement (including biotin) for gut microbiota in bronchopulmonary disease patients on antibiotics |
| [11304845](https://pubmed.ncbi.nlm.nih.gov/11304845/) | 2001 | Cohort | Journal of Clinical Pathology | Interleukin 10 in H. pylori gastritis; no biotin treatment |
| [10354275](https://pubmed.ncbi.nlm.nih.gov/10354275/) | 1999 | Cohort | Kidney International | Small bowel T cells and stress protein in IgA nephropathy; no biotin treatment |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05209P | SOLUVIT N FOR INFUSION | Injection, powder, for solution | Not stated in the data compiled |
| SIN11975P | CERNEVIT FOR INJECTION | Injection, powder, for solution | Not stated in the data compiled |

Both products are injectable, multi-vitamin preparations. Neither is an oral form, which would matter for any dyspepsia use.

---

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

**Contraindications suggested by the knowledge graph** (not taken from label text, so they need confirmation): kidney disease, nephrolithiasis, nephrocalcinosis, hypercalcemia, hyperparathyroidism, sarcoidosis, phosphorus metabolism disease, acute urate nephropathy, constipation disorder and lytic metastatic bone lesion.

**Drug interactions**: no interaction records were found.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The dyspepsia prediction has a high model score but no clinical trials and no literature showing a therapeutic effect (Evidence Level L5). The only link in the retrieved papers is a case where dyspepsia preceded biotin deficiency.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between biotin and dyspepsia
- Any clinical or observational study of biotin in dyspepsia
- Package insert warnings and contraindications from the Singapore regulator (HSA), confirming the knowledge-graph contraindications
- Oral product availability in Singapore, since both current registrations are injectables
- Consideration of **biotin metabolic disease** as a better-supported research question. It is currently the only prediction at Evidence Level L2, based on indirect high-dose biotin trials in other diseases.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

