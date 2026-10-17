---
layout: default
title: Agalsidase Beta
parent: Low Evidence (L5)
nav_order: 44
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Agalsidase Beta: predicted new indication Cervical neuroblastoma (evidence level L5). Approved use: Fabry disease"
monitor_inn: "Agalsidase beta"
predicted_indications: ["cervical neuroblastoma", "schwannoma of jugular foramen", "epiglottis neoplasm", "benign neoplasm of tongue", "benign neoplasm of floor of mouth", "benign neoplasm of buccal mucosa", "benign neoplasm of hypopharynx", "nasal cavity inverting papilloma", "vestibulocochlear nerve neoplasm", "jugular foramen meningioma"]
---

# Agalsidase Beta
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

# Agalsidase beta: From Fabry Disease to Cervical Neuroblastoma

## One-Sentence Summary

Agalsidase beta is a recombinant human alpha-galactosidase A enzyme replacement therapy, marketed in Singapore as Fabrazyme and used for Fabry disease.
The TxGNN model predicts it may be effective for **cervical neuroblastoma**, but **no clinical trials and no publications** currently support this direction.
The prediction is purely computational and has no biological or clinical backing in the data compiled for this report.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Fabry disease (based on the drug's known use; the Singapore licence records contain no indication text) |
| Predicted New Indication | Cervical neuroblastoma |
| TxGNN Prediction Score | 98.37% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, agalsidase beta replaces the deficient lysosomal enzyme alpha-galactosidase A in Fabry disease, helping to clear globotriaosylceramide (Gb3) that builds up in tissues.

No plausible mechanistic link between this enzyme replacement and neuroblastoma was identified. Gangliosides and Gb3 metabolism have only a tenuous, speculative connection to neural crest tumours. The high score (98.37%) most likely reflects the structure of the knowledge graph rather than biological evidence.

The other top predictions show the same pattern. They are mostly head and neck or nerve-related neoplasms:

- Schwannoma of jugular foramen (98.35%)
- Epiglottis neoplasm (98.32%)
- Benign neoplasm of tongue (98.31%)
- Benign neoplasm of floor of mouth (98.31%)
- Benign neoplasm of buccal mucosa (98.31%)
- Benign neoplasm of hypopharynx (98.30%)
- Nasal cavity inverting papilloma (98.29%)
- Vestibulocochlear nerve neoplasm (98.28%)
- Jugular foramen meningioma (98.28%)

For each of these, no mechanistic link was found. The scores likely reflect clustering of neighbouring tumour nodes in the graph, or Fabry disease features such as neuropathy and hearing loss, which are not tumour biology.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13609P | Fabrazyme 35mg (agalsidase beta) | Injection, powder, for solution | Not recorded in the licence data |
| SIN13610P | Fabrazyme 5mg (agalsidase beta) | Injection, powder, for solution | Not recorded in the licence data |

## Safety Considerations

- **Drug Interactions** (4 recorded):
  - **Major**: Amiodarone, Chloroquine, Gentamicin
  - **Moderate**: Migalastat

Please refer to the package insert for other safety information, including warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no registered clinical trials or publications, and no plausible mechanism links enzyme replacement for Fabry disease to neuroblastoma. The same holds for the other top-ranked predictions.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) for agalsidase beta
- Package insert warnings and contraindications from the Singapore regulator
- Evidence of a biological link between Gb3/alpha-galactosidase A and neuroblastoma, such as preclinical studies
- Review of the high-scoring predictions as a group, to judge whether graph proximity explains the scores
- Confirmation that an injectable enzyme therapy is feasible for the target tumour site
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

