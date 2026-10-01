---
layout: default
title: Baloxavir Marboxil
parent: Low Evidence (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
---

# Baloxavir Marboxil
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

# Baloxavir marboxil: From Influenza to Hemophagocytic Syndrome Associated with an Infection

## One-Sentence Summary

Baloxavir marboxil is an oral antiviral used to treat influenza.
The TxGNN model predicts it may be effective for **hemophagocytic syndrome associated with an infection**, but **no clinical trials or publications** currently support this prediction. It rests on a model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Influenza (the HSA licence records contain no indication text) |
| Predicted New Indication | Hemophagocytic syndrome associated with an infection |
| TxGNN Prediction Score | 98.85% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the input. Based on known information, baloxavir inhibits the influenza PA cap-dependent endonuclease, an enzyme the virus needs to start replicating. It has no known immunomodulatory effect on the cytokine-storm pathways that drive hemophagocytic lymphohistiocytosis (HLH).

The link between influenza and this predicted indication is weak and indirect. Influenza can trigger infection-associated HLH, so baloxavir could in principle treat the triggering infection. That would not treat the HLH itself, which is a hyperinflammatory syndrome. The high TxGNN score (98.85%) is a graph-based prediction and should not be read as clinical support.

The other top-ranked predictions are also unsupported:
- **Other HLH forms and Singleton-Merten syndrome:** no plausible mechanism.
- **Hepatitis C, E and A, and Omsk hemorrhagic fever:** these viruses lack the influenza-style cap-snatching target.
- **Hepatitis C:** the only literature is a general pediatric antiviral review and unrelated articles, which do not show baloxavir activity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN15679P | XOFLUZA FILM COATED TABLETS 20MG | Tablet, film coated |
| SIN15680P | XOFLUZA FILM COATED TABLETS 40MG | Tablet, film coated |

Both products are oral tablets manufactured by Shionogi Pharma (Settsu Plant). The approved indication text is not recorded in the evidence pack.

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for this drug in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (evidence level L5), and there is no plausible mechanism linking baloxavir to HLH beyond treating a triggering influenza infection. The high model score alone does not justify moving forward.

**To proceed, the following is needed:**
- The HSA package insert (warnings, contraindications and approved indications), which is a blocking gap for safety screening
- Mechanism of action data confirmed from DrugBank
- Preclinical or in vitro data showing baloxavir activity relevant to HLH or cytokine-storm pathways
- Any clinical or case-level evidence for baloxavir in infection-associated HLH
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

