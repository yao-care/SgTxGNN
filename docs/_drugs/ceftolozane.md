---
layout: default
title: Ceftolozane
parent: Low Evidence (L5)
nav_order: 225
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftolozane: predicted new indication Gonococcal urethritis (evidence level L5). Approved use: Urinary tract infection"
monitor_inn: "Ceftolozane"
predicted_indications: ["gonococcal urethritis", "Ureaplasma urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
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

## Ceftolozane: From Urinary Tract Infection to Gonococcal Urethritis
{: .text-alpha }

## One-Sentence Summary

Ceftolozane is a cephalosporin antibiotic originally used to treat urinary tract infection.
The TxGNN model predicts it may be effective for **gonococcal urethritis**,
but **no clinical trials and no publications** currently support this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (the Singapore licence record contains no approved indication text) |
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, ceftolozane is a cephalosporin that inhibits bacterial cell wall synthesis by binding penicillin-binding proteins. Its activity is mainly against *Pseudomonas aeruginosa* and Enterobacterales.

Urinary tract infection and gonococcal urethritis are both infections of the urogenital tract, and other beta-lactams (for example ceftriaxone) are used for gonorrhoea. The high TxGNN score probably reflects this class-level similarity rather than drug-specific evidence. Ceftolozane has limited activity against *Neisseria gonorrhoeae*, so the rationale is weak and unproven.

The other top-ranked predictions are also not well supported:
- **Ureaplasma urethritis**: *Ureaplasma* has no cell wall, so beta-lactams are mechanistically unlikely to work.
- **Uterine inflammatory disease**: Plausible for polymicrobial pelvic infection, but unproven.
- **Xanthogranulomatous pyelonephritis**: The most plausible candidate, since the drug (usually with tazobactam) is used for complicated UTI and pyelonephritis. This chronic destructive condition is usually linked to obstruction and stones and often needs surgery, so antibiotics alone are unlikely to be enough. One general review is available (indirect support only; evidence level L4).
- **Urogenital tuberculosis**: Mycobacteria are intrinsically resistant to most beta-lactams.
- **Non-infectious conditions** (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant haematological disease): No plausible antibacterial mechanism; these are likely model artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (gonococcal urethritis), currently no related literature is available.

The only publication retrieved across the top-ten predictions relates to the rank 4 prediction (xanthogranulomatous pyelonephritis):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26658652](https://pubmed.ncbi.nlm.nih.gov/26658652/) | 2016 | Review | Current Opinion in Infectious Diseases | General review of febrile urinary tract infections, including pyelonephritis and urosepsis; indirect support only |

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15317P | ZERBAXA POWDER FOR SOLUTION FOR INJECTION 1G/0.5G | Injection, powder, for solution | Not recorded in the compiled data |

## Safety Considerations

- **Drug Interactions**: 11 interactions were identified, all rated Moderate:
  - Aminoglycosides: kanamycin, neomycin, streptomycin, amikacin (including liposomal), gentamicin
  - Anticoagulants: warfarin, dicoumarol
  - Others: chloramphenicol, ethinylestradiol, mycophenolic acid

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for gonococcal urethritis is supported only by the model score, with no clinical trials or literature. Ceftolozane has limited activity against *N. gonorrhoeae*, and established alternatives already exist. Several other top predictions are biologically implausible.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA, and the approved indication text for the Singapore licence
- Detailed mechanism of action data
- In vitro susceptibility data for *N. gonorrhoeae* and relevant clinical isolates
- If any indication is pursued, xanthogranulomatous pyelonephritis is the most plausible lead, but it needs targeted literature review and clinical input on the role of surgery
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

