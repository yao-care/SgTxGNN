---
layout: default
title: Ceftolozane
parent: Low Evidence (L5)
nav_order: 224
evidence_level: L5
indication_count: 10
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ceftolozane: From Bacterial Infection Treatment to Gonococcal Urethritis

## One-Sentence Summary

Ceftolozane is a cephalosporin antibacterial, marketed in Singapore as an injectable (Zerbaxa, combined with tazobactam).
The TxGNN model predicts it may be effective for **gonococcal urethritis**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Gonococcal urethritis |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the source record. Ceftolozane belongs to the cephalosporin class, which inhibits bacterial penicillin-binding proteins and blocks cell wall synthesis. Ceftolozane covers Enterobacterales and *Pseudomonas aeruginosa*.

Other cephalosporins, such as ceftriaxone, are standard therapy for *Neisseria gonorrhoeae*, so the mechanism is plausible. However, no ceftolozane-specific gonococcal data were found, and the drug is not positioned for this use. The high score most likely reflects class-level antibacterial similarity rather than drug-specific evidence.

The other top predictions are weaker or less plausible:
- **Xanthogranulomatous pyelonephritis** (99.88%) has the strongest biological link, because ceftolozane/tazobactam is already used for complicated urinary tract infections. It is a chronic, obstructive condition managed mainly by surgery, and the only literature is a general review of febrile UTI (PMID 26658652). Evidence level is L4.
- **Uterine inflammatory disease** (99.88%) is plausible for Gram-negative coverage, but ceftolozane alone lacks anaerobic and atypical pathogen coverage.
- **Ureaplasma urethritis** is mechanistically implausible, because *Ureaplasma* has no cell wall and beta-lactams are expected to be inactive.
- **Urogenital tuberculosis** is implausible, because *M. tuberculosis* produces a beta-lactamase and is generally not susceptible to standard cephalosporins.
- The remaining candidates (polyclonal hyperviscosity syndrome, hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease) have no plausible mechanism and are likely knowledge-graph artifacts.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN15317P | ZERBAXA POWDER FOR SOLUTION FOR INJECTION 1G/0.5G | Injection, powder, for solution | Steri-Pharma, LLC; ACS Dobfar, S.p.A (ceftolozane drug product intermediate) |

The only available route is injectable.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score (L5), with no trials or literature and no ceftolozane-specific gonococcal data. Gonorrhoea already has established cephalosporin therapy, and safety information from the package insert has not been reviewed.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the HSA record (required before any safety screening)
- Mechanism of action data (e.g., from DrugBank)
- In vitro susceptibility data for *N. gonorrhoeae* against ceftolozane, including resistance patterns
- A comparison against current standard gonorrhoea therapy to establish whether there is any added value
- If a urinary tract direction is preferred, a targeted literature review for xanthogranulomatous pyelonephritis, which has the most plausible link

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

