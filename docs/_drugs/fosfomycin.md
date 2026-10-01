---
layout: default
title: Fosfomycin
parent: Low Evidence (L5)
nav_order: 450
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

# Fosfomycin: From Uncomplicated Cystitis to Ureaplasma Urethritis

## One-Sentence Summary

Fosfomycin is an antibiotic used for urinary tract infections. The TxGNN model predicts it may be effective for **Ureaplasma urethritis** with a very high score. However, there are **0 clinical trials** and **0 publications** for this indication, and the biology argues against it, so this is a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Uncomplicated cystitis (HSA indication text was not supplied) |
| Predicted New Indication | Ureaplasma urethritis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fosfomycin inhibits MurA, an early enzyme in bacterial cell wall (peptidoglycan) synthesis. It reaches high concentrations in urine, which is why it is used for urinary tract infections. Urethritis is also an infection of the lower genitourinary tract, so a generic "antibacterial for urethritis" link is easy for a knowledge graph to draw.

The mechanism, however, does not fit this specific pathogen. *Ureaplasma* species have no cell wall, so a drug that blocks cell wall synthesis is not expected to work. The near-perfect score is most likely a graph artefact rather than a real efficacy signal. No trials or publications support it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN11013P | MONUROL SACHET 3 g/sachet (ZAMBON SWITZERLAND LTD) | Granule, for suspension |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model score alone. No trials or publications exist, and fosfomycin's cell wall mechanism is not expected to act on cell-wall-deficient *Ureaplasma*.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA
- In vitro susceptibility data for fosfomycin against *Ureaplasma* species
- A clear clinical rationale, given that established alternatives already exist for this infection

**Note on other predictions for this drug:** Two other candidates in the same evidence pack have much stronger support than the top-ranked one:
- **Pyelitis (pyelonephritis)**: L2, with a randomized Phase 2/3 trial of IV fosfomycin (ZTI-01) versus piperacillin-tazobactam (PMID 30861061). It is a suitable candidate for "Proceed with Guardrails". It is not a novel repurposing target, because fosfomycin is already an established UTI antibiotic.
- **Gonococcal urethritis**: L2, with a randomized trial of fosfomycin trometamol (PMID 27064136). Its efficacy result has not been verified from the provided data, so the full text should be checked first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

