---
layout: default
title: Tetanus Immune Globulin
parent: Low Evidence (L5)
nav_order: 965
evidence_level: L5
indication_count: 10
---

# Tetanus Immune Globulin
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

# Tetanus Immune Globulin: From Tetanus Prophylaxis to Diabetic Cataract

## One-Sentence Summary

Tetanus Immune Globulin is a human antibody product that neutralizes tetanus toxin, used for passive protection against tetanus.
The TxGNN model predicts it may be effective for **diabetic cataract**, but **no clinical trials and no publications** currently support this prediction.
The model scored the top 10 predictions between 98.3% and 98.6%, and they are almost all cataract or diabetic eye conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tetanus prophylaxis and treatment (general pharmacological use; the registration record does not list an indication) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.61% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the database. Tetanus Immune Globulin is a human polyclonal IgG preparation that gives passive immunity by binding and neutralizing tetanus toxin.

The predicted condition has no pharmacological connection to this mechanism. Diabetic cataract comes from high blood sugar, polyol pathway activity and oxidative stress in the eye lens. An anti-toxin antibody does not act on any of these.

The high score is most likely an artifact of the knowledge graph:
- The drug has no recorded original indications or mechanism, so the model had little to anchor on.
- The score appears to come from graph proximity to cataract-related nodes.
- Seven of the top 10 predictions share almost identical scores (98.54%). They look like one shared signal, not independent findings.
- "Tetanic cataract" is linked to low blood calcium (hypocalcaemic tetany), not to *Clostridium tetani*. Its inclusion is probably a name-similarity artifact.

The other predictions are also without mechanistic support. They include:
- Mature, immature, cortical, senile and nuclear senile cataract
- Craniostenosis cataract
- Type 2 diabetes-associated cataract
- Diabetic retinopathy, where anti-VEGF therapy, laser treatment and glycaemic control are already established

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09656P | HyperTET S/D Injection 250 units (Grifols Therapeutics LLC) | Injection | Not listed in the available record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is computational only (L5), with no trials, no literature and no plausible mechanism linking a passive anti-toxin antibody to lens opacity. The near-identical scores across many cataract terms point to a graph artifact, not a real signal.

**To proceed, the following is needed:**
- Package insert warnings and contraindications for the Singapore-registered product
- Mechanism of action data and original indication records for the drug
- A credible mechanistic hypothesis, plus any preclinical or clinical evidence, linking the drug to lens or retinal disease
- A route and formulation compatibility assessment, only if such evidence emerges
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

