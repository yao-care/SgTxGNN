---
layout: default
title: Cinacalcet
parent: Low Evidence (L5)
nav_order: 251
evidence_level: L5
indication_count: 10
---

# Cinacalcet
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

# Cinacalcet: From Hyperparathyroidism to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Cinacalcet is a calcimimetic that acts on the calcium-sensing receptor (CaSR). It is used to treat secondary hyperparathyroidism and hypercalcemia in parathyroid carcinoma.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**.
This prediction currently rests on the model score alone, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. The compiled literature describes use in secondary hyperparathyroidism and in hypercalcemia from parathyroid carcinoma. |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Cinacalcet is a positive allosteric modulator of the CaSR. It makes the receptor more sensitive to extracellular calcium, which lowers parathyroid hormone (PTH) secretion and serum calcium. Detailed mechanism data were not available in the compiled data, but this mode of action is well described in the literature.

CaSR is also expressed in the kidney's renal collecting duct. There, its activation can oppose vasopressin-driven water reabsorption. NSIAD is a disorder caused by a gain-of-function change in the vasopressin V2 receptor, which leads to excess water retention. A drug that dampens vasopressin's effect in the collecting duct is therefore biologically conceivable as a treatment.

This link is theoretical and has not been tested. No trials or publications were retrieved for cinacalcet in NSIAD, so the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13993P | REGPARA TABLETS 25 MG | Tablet, film coated (oral) | Not stated in the registration record |

The manufacturer is Ohara Pharmaceutical Co., Ltd (Kami Factory). The registration is valid and covers a single-ingredient product.

## Safety Considerations

- **Disease associations flagged by the knowledge graph (not label text):** epilepsy, liver disease, gallbladder disease, hypotensive disorder, hypercalcemia disease, nephrocalcinosis, phosphorus metabolism disease and hypophosphatemia.
- **Drug Interactions:** 100 interactions were recorded. The main ones with a rated severity are:
  - **Major:** eliglustat
  - **Moderate:** clarithromycin, dexfenfluramine, eluxadoline, glycerol phenylbutyrate, metoclopramide, miconazole
  - Others, such as calcitriol, omeprazole, pantoprazole and simvastatin, have no severity rating.

Please refer to the package insert for key warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score (98.48%) and a plausible CaSR-based mechanism. However, no clinical trials or publications support it (Evidence Level L5). It cannot be advanced on this basis.

**To proceed, the following is needed:**
- Preclinical or case-level evidence of cinacalcet's effect on V2 receptor gain-of-function water retention
- The package insert warnings and contraindications from the HSA, which were missing from the data compiled for this report
- Detailed mechanism of action data from DrugBank
- A dedicated safety plan, since cinacalcet lowers serum calcium and the interactions above (especially eliglustat) need review

**Note on other predictions for this drug:** Among the other predicted indications, **multiple endocrine neoplasia (MEN)** has the strongest support. It has Evidence Level L3 and a "Proceed with Guardrails" recommendation. The support is 1 Phase 4 trial (NCT03123406, completed, n=750, in dialysis patients with secondary hyperparathyroidism, so only indirect evidence) and 19 publications. Several of these are observational reports of calcium control in MEN1-related primary hyperparathyroidism. The use there is symptomatic control of hypercalcemia, not disease modification, and surgery remains the standard of care. Monitoring for hypocalcemia, QT prolongation and gastrointestinal adverse events would be needed. It may be worth evaluating this indication first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

