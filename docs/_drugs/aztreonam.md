---
layout: default
title: Aztreonam
parent: Low Evidence (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
monitor_inn: "Aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-11-20
description: "Aztreonam: predicted new indication hyperamylasemia (evidence level L5). In Singapore: 2 HSA registrations (2 valid)"
---

# Aztreonam
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

## Aztreonam: monobactam antibiotic (inhibits bacterial cell wall synthesis) → hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Aztreonam is a monobactam antibiotic that acts on aerobic Gram-negative bacteria.
The TxGNN model predicts it may be associated with **hyperamylasemia**, but **no clinical trials and no publications** support this prediction, and no plausible mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | hyperamylasemia |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Singapore Market Status | Marketed (valid licences: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for aztreonam: "Aztreonam is a bactericidal agent that acts by inhibition of bacterial cell wall synthesis. Aztreonam has activity in the presence of some beta-lactamases, both penicillinases and cephalosporinases, of Gram-negative and Gram-positive bacteria." ([DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6), label version 2024-06-03; accessed 2026-11-19.) From general pharmacology, aztreonam inhibits bacterial cell wall synthesis by binding to penicillin-binding protein 3 (PBP3) in aerobic Gram-negative bacteria.

Hyperamylasemia is a biochemical finding (elevated blood amylase), not a bacterial infection, and it has no antibacterial target. No plausible mechanistic link between aztreonam and this condition was identified. The high TxGNN score (0.9973) appears to reflect network proximity in the model rather than pharmacological or clinical support, so this prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

<!-- licenses:begin -->

| Licence | Product | Dosage form | Status |
|------|------|------|------|
| SIN00556P | AZACTAM FOR INJECTION 1 g/vial | INJECTION, POWDER, FOR SOLUTION | Valid |
| SIN17438P | EMBLAVEO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1.5G/0.5G | INJECTION, POWDER, FOR SOLUTION | Valid |

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 27 interactions were recorded. The ones graded Moderate are picosulfuric acid, dicoumarol and warfarin (the latter two suggest closer monitoring of coagulation when co-administered). Others are listed without a severity grade, including vancomycin, amikacin, amphotericin B, tacrolimus, heparin, acetylsalicylic acid, metronidazole, fluconazole, acyclovir, morphine, dexamethasone, hydrocortisone, ondansetron, salbutamol, and the proton pump inhibitors omeprazole, pantoprazole and lansoprazole.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications, no plausible mechanism, and the score appears to be a model artifact. There is no basis to advance it.

**To proceed, the following is needed:**
- A credible mechanistic hypothesis linking aztreonam to hyperamylasemia
- Any clinical or preclinical study that directly addresses this condition
- Package insert warnings and contraindications from the HSA record, to enable safety screening
- Mechanism of action data from DrugBank

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the compiled data" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: aztreonam prescribing information, Hospira, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d4500795-3b07-4a7d-b432-73cafbb3dbc6) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

