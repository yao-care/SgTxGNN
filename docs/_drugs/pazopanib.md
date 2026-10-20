---
layout: default
title: Pazopanib
parent: Low Evidence (L5)
nav_order: 767
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pazopanib: predicted new indication Renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene… (evidence level L5). Approved use: Renal cell carcinoma and soft tissue sarcoma"
monitor_inn: "Pazopanib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "heart fibrosarcoma", "fibroblastic neoplasm", "kidney fibrosarcoma", "dermatofibrosarcoma protuberans"]
---

# Pazopanib
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

# Pazopanib: From Renal Cell Carcinoma and Soft Tissue Sarcoma to Renal Cell Carcinoma (Xp11.2/TFE3 Translocation Subtype)

The prompt says to use predicted_indications[0] as the primary prediction. That entry (Xp11.2/TFE3 RCC) has no trials or literature. The data compiled for this report also contain better-supported candidates, namely liposarcoma, fibroblastic neoplasm, dermatofibrosarcoma protuberans (DFSP) and unclassified RCC. These are summarised after the main sections so the primary entry is not misrepresented.

## One-Sentence Summary

Pazopanib is an oral multi-target tyrosine kinase inhibitor, originally used for renal cell carcinoma and soft tissue sarcoma.
The TxGNN model predicts it may be effective for **renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions**, but **no clinical trials and no publications** currently support this specific prediction (model prediction only).
Other predicted indications have more support, particularly liposarcoma (6 trials, 20 publications), fibroblastic neoplasm (2 trials, 20 publications) and DFSP (4 trials, 12 publications).

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Renal cell carcinoma and soft tissue sarcoma (the Singapore licence records contain no indication text) |
| Predicted New Indication | Renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, pazopanib inhibits VEGFR-1/2/3, PDGFR and c-Kit. It is already used for renal cell carcinoma and non-adipocytic soft tissue sarcoma.

Xp11.2/TFE3 translocation RCC is a rare RCC subtype in which the VEGF pathway is involved. A biological link to the original indication therefore exists. However, the high TxGNN score is a model output only. No trial or publication addresses this subtype in the compiled data.

## Clinical Trial Evidence

Currently no related clinical trials registered for the Xp11.2/TFE3 RCC prediction.

## Literature Evidence

Currently no related literature available for the Xp11.2/TFE3 RCC prediction.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN17000P | PAZOPANIB-TEVA FC TABLETS 200 MG | Film-coated tablet | Not recorded |
| SIN14023P | Votrient Tablet 400 mg | Film-coated tablet | Not recorded |
| SIN14022P | Votrient Tablet 200 mg | Film-coated tablet | Not recorded |

All three authorizations are valid single-ingredient products for oral use.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Targeted therapy (multi-target tyrosine kinase inhibitor), not a conventional cytotoxic |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Liver function, blood pressure, ECG/QT and electrolytes, thyroid function, urine protein, and blood counts. These follow the contraindication-linked conditions below. |
| Handling Protection | Please refer to the package insert warnings and precautions |

## Safety Considerations

- **Contraindication-linked conditions (from the TxGNN knowledge graph, not label text)**:
  - Cardiovascular: hypertension, long QT syndrome (including familial), torsades de pointes, myocardial infarction, coronary thrombosis
  - Liver: liver failure, drug-induced liver injury, hyperbilirubinaemia (including Gilbert syndrome)
  - Endocrine and metabolic: hypothyroidism, potassium deficiency, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease
  - Other: intracerebral haemorrhage, active peptic ulcer disease, pancreatitis, proteinuria, diarrhoeal disease, hemoglobinopathy
- **Drug Interactions**: 100 interactions were found in total. The main ones shown:
  - **Major**: acid-reducing agents (famotidine, ranitidine, cimetidine, omeprazole, esomeprazole, rabeprazole, dexlansoprazole), clarithromycin, dolasetron
  - **Moderate**: dexamethasone, budesonide, aprepitant, loperamide, bisacodyl, pioglitazone, saxagliptin, eliglustat, magnesium oxide, polyethylene glycol

Please also refer to the package insert for full warnings and contraindications.

## Other Predicted Indications with Stronger Evidence

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Key Support | Recommendation |
|---|---|---|---|---|---|
| 2 | Unclassified renal cell carcinoma | 99.63% | L3 | Single-arm Phase 2 in non-clear-cell RCC ([PMID 28546525](https://pubmed.ncbi.nlm.nih.gov/28546525/)); retrospective series including PANORAMA ([28108284](https://pubmed.ncbi.nlm.nih.gov/28108284/)) | Research Question |
| 4 | Liposarcoma | 99.59% | L2 | Phase 2 trials [NCT01506596](https://clinicaltrials.gov/study/NCT01506596) (n=42) and [NCT01692496](https://clinicaltrials.gov/study/NCT01692496) (n=52); [PMID 31010343](https://pubmed.ncbi.nlm.nih.gov/31010343/) | Research Question |
| 8 | Fibroblastic neoplasm | 99.35% | L2 | [NCT02066285](https://clinicaltrials.gov/study/NCT02066285) (n=96, solitary fibrous tumour/extraskeletal myxoid chondrosarcoma); [PMID 25269954](https://pubmed.ncbi.nlm.nih.gov/25269954/) | Research Question |
| 10 | Dermatofibrosarcoma protuberans | 99.29% | L2 | Phase 2 in unresectable DFSP ([PMID 32956651](https://pubmed.ncbi.nlm.nih.gov/32956651/)); terminated [NCT01059656](https://clinicaltrials.gov/study/NCT01059656) (n=23) | Research Question |

Ranks 3, 5, 6, 7 and 9 (RCC with neuroblastoma, childhood kidney cell carcinoma, ovarian myxoid liposarcoma, heart fibrosarcoma and kidney fibrosarcoma) are L5 with no supporting studies, and are all on Hold.

Caveats on the stronger candidates:
- **Liposarcoma**: pazopanib's soft tissue sarcoma approval excludes the adipocytic subtype, and the evidence is mixed.
- **Unclassified RCC**: the data are retrospective or single-arm and do not isolate this subtype. No randomized evidence is available.
- **DFSP**: imatinib remains the standard targeted therapy, and most listed trials are mixed sarcoma populations.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The primary prediction (Xp11.2/TFE3 RCC) has no clinical trials or literature and rests on a model score and mechanistic plausibility alone, so it is L5. Pazopanib is already marketed in Singapore with three valid authorizations, which makes follow-up feasible. The stronger signals lie in other predicted indications, and those are better treated as separate research questions.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from HSA, which are currently missing and block safety screening
- Detailed mechanism of action data from DrugBank
- The approved indication text for the Singapore licences, which is empty in the current records
- For Xp11.2/TFE3 RCC: a targeted literature search for case series or subgroup analyses within non-clear-cell RCC studies
- Consideration of re-prioritising evaluation toward unclassified RCC, DFSP or fibroblastic tumours, each of which has a Phase 2 evidence base
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

