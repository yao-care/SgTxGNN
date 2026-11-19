---
layout: default
title: Orlistat
parent: Low Evidence (L5)
nav_order: 743
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-20
monitor_inn: "Orlistat"
predicted_indications: ["hypervitaminosis"]
description: "Orlistat: predicted new indication Hypervitaminosis (evidence level L5). In Singapore: 2 HSA registrations (2 valid)"
---

# Orlistat
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Orlistat: Hypervitaminosis
{: .text-alpha }

## One-Sentence Summary

Orlistat is a gastrointestinal lipase inhibitor, originally used to treat obesity.
The TxGNN model predicts it may be effective for **hypervitaminosis**, but there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypervitaminosis |
| TxGNN Prediction Score | 0.9942 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for orlistat: "Orlistat is a reversible inhibitor of gastrointestinal lipases. It exerts its therapeutic activity in the lumen of the stomach and small intestine by forming a covalent bond with the active serine residue site of gastric and pancreatic lipases." ([DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e), label version 2026-09-30; accessed 2026-11-19.) Orlistat is, however, a well-known inhibitor of gastrointestinal lipases. By blocking the breakdown of dietary fat, it reduces fat absorption, and with it the absorption of fat-soluble vitamins (A, D, E and K).

This gives a purely theoretical rationale: if less vitamin is absorbed, vitamin excess could in principle be lowered. But this is the opposite of orlistat's known adverse effect, vitamin deficiency, and vitamin deficiency disorder is even listed among its knowledge-graph contraindications. Most hypervitaminosis cases come from over-supplementation and are managed by stopping the supplement. No clinical data support using a lipase inhibitor as a treatment. The high TxGNN score should therefore be treated as a computational signal only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN13046P | XENICAL CAPSULE 120MG | CAPSULE | Valid |
| SIN15312P | OBELIT 120 CAPSULE 120MG | CAPSULE, GELATIN COATED | Valid |

<!-- licenses:end -->

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

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Xenical (orlistat) prescribing information, H2-Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6240792b-9224-2d10-e053-2a91aa0a2c3e) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

