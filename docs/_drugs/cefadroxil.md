---
layout: default
title: Cefadroxil
parent: Low Evidence (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Cefadroxil
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

# Cefadroxil: From Antibacterial Therapy to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Cefadroxil is a first-generation oral cephalosporin antibiotic that works by inhibiting bacterial cell wall synthesis.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but this is a model prediction only, with **0 clinical trials** and **0 publications** supporting it.
The high score is most likely a knowledge-graph artifact rather than a real biological signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 98.60% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known information, cefadroxil is a first-generation cephalosporin that inhibits bacterial cell wall synthesis, and its use is in bacterial infections.

**The prediction is not mechanistically supported.** Polyclonal hyperviscosity syndrome is caused by excess immunoglobulins raising blood viscosity. It is not an infection, and cefadroxil has no target in this process. The score of 98.60% most likely reflects proximity to other hematologic terms in the knowledge graph rather than biology.

The other top-ranked predictions share the same problem:

- **Non-infectious conditions, with no plausible link:** hyperamylasemia, congenital analbuminemia, blood group incompatibility, premalignant hematological system disease, monoclonal gammopathy, and hematological disease associated with an acquired peripheral neuropathy.
- **Ureaplasma urethritis:** contradicted by mechanism. Ureaplasma lacks a cell wall, so beta-lactams are intrinsically ineffective.
- **Septicemic plague:** cephalosporins are not recommended, and an oral first-generation agent is unsuitable for severe systemic infection.
- **Gonococcal urethritis:** the mechanism is plausible, but the only literature studies a different cephalosporin (cefetamet pivoxil). First-generation agents are not standard therapy because of limited gonococcal activity and resistance concerns.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN11665P | SOFIDROX CAPSULE 500 mg | Capsule | XEPA-SOUL PATTINSON (MALAYSIA) SDN BHD |

Route of administration: oral only.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials or literature behind it and no plausible mechanistic link. Cefadroxil is an antibacterial, and the condition is a non-infectious immunoglobulin disorder. The high TxGNN score alone is not enough to justify further investment.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications, approved indications), which is currently a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A mechanism-based reason, supported by any preclinical or clinical study, why an antibacterial would affect hyperviscosity
- If an infection-related direction is wanted, cefadroxil-specific data for a more plausible indication, since the current gonococcal urethritis evidence covers a different drug
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

