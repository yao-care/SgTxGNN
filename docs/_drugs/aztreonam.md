---
layout: default
title: Aztreonam
parent: Low Evidence (L5)
nav_order: 132
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Aztreonam: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Urinary tract infection and other Gram-negative infections"
monitor_inn: "Aztreonam"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
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

# Aztreonam: From Urinary Tract Infection to Hyperamylasemia

## One-Sentence Summary

Aztreonam is a monobactam antibiotic, originally used to treat Gram-negative bacterial infections such as urinary tract infection, Pseudomonas aeruginosa infection and peritonitis.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection and other Gram-negative infections (the Singapore licence text does not state an indication, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug is not available in the compiled data. Aztreonam is a monobactam antibiotic. It is understood to inhibit bacterial cell wall synthesis by targeting penicillin-binding protein 3 (PBP3) in aerobic Gram-negative bacteria.

**The prediction is not mechanistically reasonable.** Hyperamylasemia is a biochemical finding, an elevated blood amylase level. It has no bacterial target, and aztreonam has no known effect on amylase production or clearance. The high TxGNN score most likely reflects proximity in the knowledge graph rather than real pharmacology.

The same pattern appears in several other top-ranked predictions, such as polyclonal hyperviscosity syndrome and congenital analbuminemia. These are not infections, and they have identical or near-identical scores.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN00556P | AZACTAM FOR INJECTION 1 g/vial | Injection, powder, for solution | Not listed in the licence record |

The product is a single-ingredient injectable made by Catalent Anagni S.R.L. Its status is valid, and there are no cancelled registrations.

---

## Safety Considerations

- **Disease associations flagged in the knowledge graph (not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, and bronchial disease. These should be confirmed against the official package insert.
- **Drug Interactions:** The interaction screen identified 27 interacting drugs, and the details cover 20 of them. Three are rated **Moderate**: warfarin, dicoumarol and picosulfuric acid. The anticoagulant interactions suggest monitoring of coagulation parameters. The remaining listed interactions have no severity rating. They include vancomycin, amikacin, amphotericin B, tacrolimus, heparin, acetylsalicylic acid, metronidazole, fluconazole, acyclovir, morphine, ondansetron, salbutamol, hydrocortisone, dexamethasone, pantoprazole, omeprazole and lansoprazole.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials, no literature and no plausible mechanism. Hyperamylasemia is a laboratory finding that an antibacterial would not be expected to treat.

**To proceed, the following is needed:**
- A credible biological rationale linking aztreonam to amylase elevation. Without this, further work on this indication is not justified.
- Package insert warnings and contraindications from the HSA, which are needed before any safety screening.
- Mechanism of action data confirmed from DrugBank.

**Alternative direction:** Among the other predictions for aztreonam, **gonococcal urethritis** has the most support (evidence level L3). It has six publications, including a 2020 single-arm open-label trial of 2 g intramuscular aztreonam and several 1980s single-dose studies. Its use would be limited by reports of aztreonam- and cephem-resistant gonococcal strains. It is better framed as a research question, for example as a niche option in cephalosporin-resistant or beta-lactam-allergic patients, than as a ready candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

