---
layout: default
title: Cinacalcet
parent: Low Evidence (L5)
nav_order: 249
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

# Cinacalcet: From Secondary Hyperparathyroidism to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Cinacalcet is a calcimimetic, originally used to treat secondary hyperparathyroidism in dialysis patients.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Secondary hyperparathyroidism (per published literature; the Singapore registration record does not state an indication) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 98.48% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the record. Based on known information, cinacalcet activates the calcium-sensing receptor (CaSR) and is established for lowering parathyroid hormone and calcium. Mechanistically, it is not clear that it can be applied to NSIAD.

NSIAD is caused by activating mutations in the vasopressin V2 receptor (AVPR2), which leads to water retention and low blood sodium. Cinacalcet acts on CaSR in the thick ascending limb and collecting duct, where CaSR activation tends to reduce urinary concentrating ability. A downstream aquaretic (water-excreting) effect is conceivable, but it is speculative. It would not correct the underlying receptor defect.

The high score is therefore best read as a hypothesis from the knowledge graph, not as a mechanism-backed finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN13993P | REGPARA TABLETS 25 MG (Ohara Pharmaceutical Co., Ltd) | Film-coated tablet (oral) | Not listed in the record |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no trials or publications behind it (L5). The proposed mechanism is speculative, and CaSR activation may even work against urinary concentration. The Singapore package insert warnings and contraindications are also not yet available.

**To proceed, the following is needed:**
- Singapore (HSA) package insert warnings, contraindications and approved indication text
- Mechanism of action data from DrugBank
- Preclinical or case-level evidence that a calcimimetic can affect water handling in AVPR2-activating disease

**Note on other predictions for this drug:**
The best-supported candidate in this Evidence Pack is **multiple endocrine neoplasia (MEN)**, specifically MEN1-associated primary hyperparathyroidism. It is rated L2 with a suggested decision of Proceed with Guardrails. Its evidence includes one completed Phase 3 trial (NCT00325104, n=25) and 19 publications, several of them MEN1-specific cohorts. Its evidence tier is limited because randomization is not confirmed. Surgery remains the standard of care, and calcium and QT interval monitoring would be required. It would be worth evaluating as its own report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

