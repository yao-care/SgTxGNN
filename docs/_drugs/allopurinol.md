---
layout: default
title: Allopurinol
parent: Low Evidence (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-11-12
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L5). Approved use: Gout"
---

# Allopurinol
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

## Allopurinol: From Gout to Hepatic Porphyria
{: .text-alpha }

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor. The TxGNN model (deep learning) predicts it may be effective for **hepatic porphyria**, but there are **0 clinical trials** and only **2 loosely related publications** (one hypothesis paper and one rat study not specific to allopurinol), so the evidence is model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout (relation recorded in the knowledge graph; the local licence records supplied contain no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 9 of 9) |
| Number of Registrations | 9 (valid: 9) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Allopurinol is generally known as a xanthine oxidase inhibitor that lowers uric acid production, but that is background knowledge and not drawn from the supplied records.

The link to hepatic porphyria is indirect and speculative. One 2019 hypothesis paper proposes targeting 5-aminolevulinate synthase (the rate-limiting enzyme of heme biosynthesis) through tryptophan or inhibitors of heme utilisation. The second paper is a 1992 rat study of carbamazepine and haem metabolism. Neither paper studies allopurinol in porphyria, and no direct mechanism connecting xanthine oxidase inhibition to porphyria control is established in the supplied data. Neither paper directly studies allopurinol for this disease, so the prediction rests on the model score alone and is therefore rated L5.

Several other top-ranked predictions (portal vein thrombosis, noncirrhotic portal hypertension, hepatoportal sclerosis and others) share identical scores (0.9994), which comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Review (hypothesis) | Medical Hypotheses | Proposes metabolic targeting of liver 5-ALAS, via tryptophan or inhibition of heme use by tryptophan 2,3-dioxygenase, as a therapy for acute hepatic porphyrias. Does not test allopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Preclinical (animal) | Biochemical Pharmacology | Acute carbamazepine exacerbated porphyria-related haem loss in rat liver. Concerns a different drug. |

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN05804P | ALLOPURINOL TABLET 100 mg | TABLET | Valid |
| SIN06060P | ZYLORIC TABLET 100 mg | TABLET | Valid |
| SIN06061P | ZYLORIC TABLET 300MG | TABLET | Valid |
| SIN06219P | ALLOPURINOL TABLET BP 100 mg | TABLET | Valid |
| SIN06247P | APO-ALLOPURINOL TABLET 300 mg | TABLET | Valid |

Showing 5 of 9 HSA registrations.

<!-- licenses:end -->

The five above are shown.

<!-- review:begin sg-lic-20261106-allopurinol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Eight valid single-ingredient registrations exist in total, all oral tablets. The five above are shown." Removed: the number or status of product registrations stated here did not match the HSA register data (the HSA register of therapeutic products as of 2026-11-06). The HSA register lists 9 registrations for this drug, 9 current; the Quick Overview and the table under Singapore Market Information show the current figures. Source: [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/).

<!-- review:end sg-lic-20261106-allopurinol-1 -->

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** contraindication links to liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis and anti-glomerular basement membrane disease. Liver disease is especially relevant given the predicted hepatic indication.
- **Drug Interactions:** 100 interactions were found in the interaction database. Those listed include moderate interactions with aluminium hydroxide, attapulgite, kaolin, magaldrate and sucralfate (antacids and adsorbents that may affect absorption). Minor interactions include amoxicillin and chlorpropamide. Many others (e.g. metformin, omeprazole, doxycycline, morphine) have an unclassified severity level.

Please refer to the package insert for authoritative warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, no allopurinol-specific studies in hepatic porphyria and no established mechanism. The knowledge graph also records liver disease as a contraindication, which conflicts with a hepatic target population.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link between xanthine oxidase inhibition and heme biosynthesis
- Preclinical studies of allopurinol directly in porphyria models
- Package insert warnings and contraindications from the HSA, particularly regarding hepatic safety
- Review of the approved indication wording for the Singapore licences

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Health Sciences Authority data (the register of therapeutic products). Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "Eight valid single-ingredient registrations exist in total, all oral tablets" | Corrected | [HSA – Listing of registered therapeutic products (data.gov.sg)](https://data.gov.sg/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

