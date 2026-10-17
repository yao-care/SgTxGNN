---
layout: default
title: Allopurinol
parent: Medium Evidence (L3-L4)
nav_order: 66
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L4). Approved use: Gout, hyperuricemia, acute urate nephropathy"
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatoportal sclerosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
---

# Allopurinol
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

# Allopurinol: From Gout to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor, originally used to treat gout, hyperuricemia and acute urate nephropathy.
The TxGNN model predicts it may be effective for **hepatic porphyria**, but **no clinical trials** and only **2 indirect publications** (a hypothesis paper and a rat study) currently exist, so this prediction rests almost entirely on the model.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout, hyperuricemia, acute urate nephropathy (from the knowledge graph; the Singapore registrations list no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 8 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Allopurinol is a well-known xanthine oxidase inhibitor that lowers uric acid production, and its efficacy in gout is well established. Older animal work suggests it can influence hepatic heme synthesis and degradation, which is the only plausible link to porphyria.

The two retrieved papers are indirect. One is a hypothesis paper on targeting 5-aminolevulinate synthase (ALAS1) in acute hepatic porphyrias. The other is a rat study of carbamazepine's effects on heme metabolism. Neither shows a therapeutic benefit of allopurinol in porphyria patients.

There is also a safety concern. Allopurinol has been reported in some contexts to be porphyrinogenic, meaning it may induce ALAS1 or deplete heme. The direction of effect is therefore uncertain and could be harmful in acute porphyrias. The high TxGNN score alone should not be read as evidence of benefit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes targeting liver 5-ALAS, via tryptophan or inhibition of heme use by tryptophan 2,3-dioxygenase, as therapy for acute hepatic porphyrias. Does not test allopurinol directly. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal study (rat) | Biochemical Pharmacology | Very low-dose carbamazepine altered liver heme metabolism and exacerbated hepatic porphyria. Not about allopurinol. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05804P | Allopurinol Tablet 100 mg (Beacons Pharmaceuticals) | Tablet | Not stated |
| SIN07051P | YSP Allopurinol Tablet 100 mg | Tablet | Not stated |
| SIN06060P | Zyloric Tablet 100 mg | Tablet | Not stated |
| SIN06247P | Apo-Allopurinol Tablet 300 mg | Tablet | Not stated |
| SIN06248P | Apo-Allopurinol Tablet 100 mg | Tablet | Not stated |

Three more valid single-ingredient oral tablet registrations exist (SIN17004P, SIN06219P, SIN06061P), for 8 in total. All are oral tablets.

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (these come from drug-disease graph edges, not package insert text): liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis, and anti-glomerular basement membrane disease.
  - Liver disease is directly relevant to a hepatic indication.
- **Drug Interactions**: 100 interactions were found. Those rated Moderate involve antacids and adsorbents: aluminum hydroxide, attapulgite, kaolin, magaldrate and sucralfate. Minor interactions include amoxicillin and chlorpropamide. Many other pairs, such as metformin, omeprazole, pantoprazole, glimepiride, doxycycline and morphine, have an unrated severity.
- Allopurinol is a recognised cause of hypersensitivity reactions, and the porphyrinogenic concern above also applies.

For full warnings, please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials and only indirect, non-allopurinol literature (L4). Allopurinol may worsen acute porphyrias, and liver disease appears among its graph-derived contraindication signals. The high model score is not enough to justify progression.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, which are currently missing and block safety screening
- Mechanism of action data (for example from DrugBank)
- Direct preclinical or clinical evidence on allopurinol's effect on heme synthesis in porphyria, including whether it is porphyrinogenic
- A risk assessment for patients with acute hepatic porphyria before any trial is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

