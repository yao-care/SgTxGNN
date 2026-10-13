---
layout: default
title: Orlistat
parent: Low Evidence (L5)
nav_order: 743
evidence_level: L5
indication_count: 10
---

# Orlistat
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

# Orlistat: From Obesity to Hypervitaminosis

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor, originally used to treat obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Obesity (including monogenic obesity); the Singapore registry entries contain no indication text, so this comes from the knowledge graph |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 99.42% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Orlistat is, however, a well-known inhibitor of gastrointestinal lipases. By blocking the breakdown of dietary fat, it reduces fat absorption, and with it the absorption of fat-soluble vitamins (A, D, E and K).

This gives a purely theoretical rationale: if less vitamin is absorbed, vitamin excess could in principle be lowered. But this is the opposite of orlistat's known adverse effect, vitamin deficiency, and vitamin deficiency disorder is even listed among its knowledge-graph contraindications. Most hypervitaminosis cases come from over-supplementation and are managed by stopping the supplement. No clinical data support using a lipase inhibitor as a treatment. The high TxGNN score should therefore be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15312P | OBELIT 120 CAPSULE 120MG (Intas Pharmaceuticals Limited) | Capsule, gelatin coated | Not specified in registry data |
| SIN13046P | XENICAL CAPSULE 120MG (F. Hoffmann-La Roche Ltd / Delpharm Milano S.R.L.) | Capsule | Not specified in registry data |

Both products are single-ingredient, valid, oral formulations.

## Safety Considerations

- **Contraindications flagged in the knowledge graph** (these are graph relationships, not package insert text): liver failure, primary hyperoxaluria, anorexia nervosa, bulimia nervosa, vitamin deficiency disorder, cholestasis, benign recurrent intrahepatic cholestasis, familial intrahepatic cholestasis, and drug-induced liver injury.
- **Drug Interactions**: 100 interactions were identified. The main ones, based on the first 20 entries retrieved, are:
  - **Moderate**: abacavir, lamivudine, emtricitabine, atazanavir, acarbose, metformin, albiglutide, alogliptin, canagliflozin, chlorpropamide, amiodarone, cannabidiol, asparaginase (E. coli and Erwinia forms), calaspargase pegol, brentuximab vedotin, clofarabine.
  - **Minor**: cholecalciferol, calcifediol, calcitriol. These are vitamin D agents, which is relevant because orlistat reduces fat-soluble vitamin absorption.
- Package insert warnings were not available in the data compiled for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it (L5). Its only mechanistic rationale conflicts with orlistat's known effect of causing vitamin deficiency, so the benefit-risk balance is unfavourable. Hypervitaminosis is also better managed by stopping the excess vitamin intake.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA website (a blocking data gap for safety screening)
- Mechanism of action data from DrugBank
- Any preclinical or clinical signal that orlistat can lower vitamin levels in a therapeutic setting, together with a plan for managing vitamin depletion

**Note on other predictions:** Among the other predicted indications, **fatty liver disease** (TxGNN score 85.3%, rank 8) has the strongest support. It has two small completed Phase 4 trials (NCT00160407, n=50; NCT00207311, n=30), a 2023 randomized trial of diet versus orlistat in obesity with MAFLD (PMID 36781126), and a 2024 meta-analysis of randomized trials (PMID 38910819). This is graded L3 and flagged as a research question. Any follow-up effort would be better directed there. The benefit appears to be largely weight-mediated, so larger trials with histology endpoints are needed.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

