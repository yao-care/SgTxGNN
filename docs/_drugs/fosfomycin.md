---
layout: default
title: Fosfomycin
parent: Low Evidence (L5)
nav_order: 454
evidence_level: L5
indication_count: 10
---

# Fosfomycin
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

# Fosfomycin: From Urinary Tract Infection to Ureaplasma Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic originally used to treat urinary tract infections (UTIs). The TxGNN model predicts it may be effective for **Ureaplasma urethritis**, but **no clinical trials and no publications** currently support this direction. The prediction also conflicts with the drug's mechanism, so it rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Fosfomycin inhibits MurA (UDP-N-acetylglucosamine enolpyruvyl transferase). This blocks the first step of bacterial peptidoglycan (cell wall) synthesis. It reaches high concentrations in urine, which is why it is used for UTIs. Detailed mechanism data was not available from the drug database, so this description comes from the mechanistic analysis in the data compiled for this report.

The original and predicted indications are both urogenital infections, which is probably why the model linked them. Mechanistically, however, the prediction is weak. *Ureaplasma* species have no cell wall, so a cell-wall-synthesis inhibitor is unlikely to work against them. The high score most likely reflects the shared urogenital infection context in the knowledge graph, not a real pharmacological link.

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
| SIN11013P | MONUROL SACHET 3 g/sachet (Zambon Switzerland Ltd) | Granule, for suspension | Not listed in the registration data |

---

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for authoritative safety information.

- **Contraindication signals from the knowledge graph** (not label text): kidney disease, pyoureter, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis.
- **Drug Interactions** (3 found):
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or literature (L5). *Ureaplasma* lacks a cell wall, so fosfomycin's mechanism makes efficacy unlikely.

**Other predictions for fosfomycin:**
- **Pyelitis (pyelonephritis):** this is the strongest candidate (L1). It is supported by a Phase 2/3 RCT of IV fosfomycin versus piperacillin-tazobactam (ZEUS) and by recent reviews. It is largely a route and formulation extension of the existing UTI indication, not a true repurposing.
- **Gonococcal urethritis:** this has limited direct evidence (L2), consisting of a 2016 RCT and 1977 studies. Established first-line agents such as ceftriaxone remain preferred.

**To proceed with Ureaplasma urethritis, the following is needed:**
- In vitro susceptibility data against *Ureaplasma* species that would offset the mechanistic concern
- Any clinical or observational evidence in Ureaplasma urethritis
- Package insert safety information, since the warnings and contraindications were not available
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

