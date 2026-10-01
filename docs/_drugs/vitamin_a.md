---
layout: default
title: Vitamin A
parent: Low Evidence (L5)
nav_order: 1062
evidence_level: L5
indication_count: 10
---

# Vitamin A
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

# Vitamin A: From Parenteral Vitamin Supplementation to Congenital Prothrombin Deficiency

## One-Sentence Summary

Vitamin A is registered in Singapore as a component of multivitamin injection products. The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but this is a graph-based prediction only. The 5 retrieved clinical trials are all unrelated to vitamin A (graded C), and **no publications** were found.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.97% (model rank 709) |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, vitamin A is a fat-soluble vitamin supplied in multivitamin injections (VITALIPID N and CERNEVIT), and its role in nutritional supplementation is established. Mechanistically, however, there is no clear path to congenital prothrombin deficiency.

Prothrombin (coagulation factor II) synthesis depends on **vitamin K**, not vitamin A. No established link connects vitamin A to prothrombin production or function. The very high TxGNN score most likely reflects proximity in the knowledge graph, since vitamins share many neighbouring nodes. It is not evidence of therapeutic benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00562783](https://clinicaltrials.gov/study/NCT00562783) | Phase 2 | Completed | 90 | Randomized trial of Vitalliver in decompensated cirrhosis. No vitamin A or coagulation-factor deficiency link; likely keyword-matching noise |
| [NCT04384341](https://clinicaltrials.gov/study/NCT04384341) | N/A | Recruiting | 480 | Observational study of bone loss in haemophilia (factor VIII/IX deficiency). Disease and intervention are unrelated |
| [NCT02392767](https://clinicaltrials.gov/study/NCT02392767) | N/A | Completed | 25 | Dietary supplement combination and endothelial function in mild-to-moderate hypertension. Unrelated population |
| [NCT00168077](https://clinicaltrials.gov/study/NCT00168077) | Phase 3 | Completed | 40 | Beriplex P/N (prothrombin complex concentrate) in acquired factor II, VII, IX and X deficiency from oral anticoagulation. No vitamin A, and the condition is acquired, not congenital |
| [NCT03534752](https://clinicaltrials.gov/study/NCT03534752) | N/A | Completed | 220 | Retrospective database of adult inborn errors of metabolism in French-speaking Switzerland. No vitamin A intervention |

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN05207P | VITALIPID N INFANT INJECTION | Injection | Fresenius Kabi AB |
| SIN05208P | VITALIPID N ADULT INJECTION | Injection | Fresenius Kabi AB |
| SIN11975P | CERNEVIT FOR INJECTION | Injection, powder, for solution | Fareva Pau 1 (sub-contractor) / Baxter S.A. |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph-based score. The mechanism points to vitamin K rather than vitamin A, and none of the retrieved trials tests vitamin A in this disease. There is no supporting literature.

**To proceed, the following is needed:**
- A plausible mechanistic rationale linking vitamin A to prothrombin deficiency
- The HSA package insert, to complete the warnings and contraindications review
- Mechanism of action data from DrugBank

**Note on other predictions for this drug:** Other candidates in the same Evidence Pack have stronger support than this one. The best is **perinatal disease**, rated L2 / Proceed with Guardrails. Cochrane reviews of vitamin A supplementation in very low birth weight infants report modest benefit for bronchopulmonary dysplasia. That is already a studied use rather than a new finding. **Injury**, **cell proliferation disorder** and **radiation or chemically induced disorder** are rated L3 to L4 as research questions. Several of these carry vitamin A safety issues (such as fracture risk at high intake) that need review first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

