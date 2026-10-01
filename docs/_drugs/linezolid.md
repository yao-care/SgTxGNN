---
layout: default
title: Linezolid
parent: Low Evidence (L5)
nav_order: 597
evidence_level: L5
indication_count: 10
---

# Linezolid
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

# Linezolid: From Gram-Positive Bacterial Infections to Polyclonal Hyperviscosity Syndrome

## One-Sentence Summary

Linezolid is an oxazolidinone antibiotic, used against resistant Gram-positive bacterial infections.
The TxGNN model predicts it may be effective for **polyclonal hyperviscosity syndrome**, but **no clinical trials and no publications** currently support this prediction.
It is a graph-based prediction only, and the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gram-positive bacterial infections (the registered indication text is not available in the Singapore records) |
| Predicted New Indication | Polyclonal hyperviscosity syndrome |
| TxGNN Prediction Score | 92.45% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Linezolid is known as an oxazolidinone that inhibits bacterial protein synthesis by binding the 23S rRNA of the 50S ribosomal subunit.

We could not identify a plausible mechanistic link to the predicted indication. Polyclonal hyperviscosity syndrome involves raised serum viscosity from excess immunoglobulins. Linezolid has no known effect on serum viscosity or immunoglobulin levels, and an antibacterial has no obvious target in this condition. The high score therefore reflects patterns in the knowledge graph, not biological or clinical support.

A safety concern also applies. Linezolid can cause myelosuppression, which is a particular worry in patients with haematologic disease.

For context, the evidence pack also lists other haematologic and related predictions, all with limited or no support. The only candidate that reached S1 (Research Question) is **pyelonephritis**, where a niche role against resistant Gram-positive pathogens such as VRE and MRSA is conceivable. That is outside the scope of this report.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

Seven authorizations are registered; five main ones are listed below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16950P | LINEZAN Solution for Infusion 2 mg/mL | Infusion, solution | Anfarm Hellas S.A. |
| SIN11405P | ZYVOX Tablet 600 mg | Tablet, film coated | Viatris Pharmaceuticals LLC (Vega Baja) |
| SIN15849P | LINEZOLID KABI Solution for Infusion 2 mg/mL | Infusion, solution | Fresenius Kabi Norge AS |
| SIN11408P | ZYVOX Granules for Oral Suspension 20 mg/mL | Granule, for suspension | Neolpharma, Inc. / Viatris Pharmaceuticals LLC (Vega Baja) |
| SIN14946P | LINEZOLID SANDOZ Film Coated Tablet 600 mg | Tablet, film coated | S.C. Sandoz S.R.L. |

## Safety Considerations

- **Myelosuppression**: Linezolid causes dose- and duration-dependent myelosuppression through inhibition of mitochondrial protein synthesis. This matters in patients with marrow or haematologic disorders, the population of the predicted indication.

Please refer to the package insert for the full warnings, contraindications and drug interactions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score alone (L5), with no trials, no literature and no plausible mechanistic link. Known myelosuppression makes use in haematologic disease a safety concern rather than a benefit.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), which is currently missing and blocks safety screening
- Mechanism of action data from DrugBank
- A credible biological rationale linking linezolid to serum viscosity or immunoglobulin-driven disease
- Any clinical or preclinical evidence, since none is currently registered or published
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

