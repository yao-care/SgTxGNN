---
layout: default
title: Allopurinol
parent: Low Evidence (L5)
nav_order: 66
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "idiopathic copper-associated cirrhosis", "hepatopulmonary syndrome", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-28
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
| Singapore Market Status | Marketed (valid licences: 8 of 8) |
| Number of Registrations | 8 (valid: 8) |
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

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05804P | Allopurinol Tablet 100 mg (Beacons Pharmaceuticals) | Tablet | Not stated in the records |
| SIN07051P | YSP Allopurinol Tablet 100 mg | Tablet | Not stated in the records |
| SIN06060P | Zyloric Tablet 100 mg | Tablet | Not stated in the records |
| SIN06247P | Apo-Allopurinol Tablet 300 mg | Tablet | Not stated in the records |
| SIN06248P | Apo-Allopurinol Tablet 100 mg | Tablet | Not stated in the records |

Eight valid single-ingredient registrations exist in total, all oral tablets. The five above are shown.

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
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

