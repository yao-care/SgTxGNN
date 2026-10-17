---
layout: default
title: Azacitidine
parent: Low Evidence (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Azacitidine: predicted new indication Bulbar polio (evidence level L5). Approved use: Myeloid leukemia / acute myeloid leukemia"
monitor_inn: "Azacitidine"
predicted_indications: ["bulbar polio", "refractory cytopenia of childhood", "partial deletion of the long arm of chromosome 5", "aregenerative anemia", "severe congenital hypochromic anemia with ringed sideroblasts", "5q35 microduplication syndrome", "neuralgic amyotrophy", "amyotrophic neuralgia", "familial thrombocytosis"]
---

# Azacitidine
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

# Azacitidine: From Acute Myeloid Leukemia to Bulbar Polio

## One-Sentence Summary

Azacitidine is a hypomethylating nucleoside analog originally used for myeloid malignancies such as acute myeloid leukemia (AML) and myelodysplastic syndromes.
The TxGNN model predicts it may be effective for **bulbar polio**, but **0 clinical trials** and **0 publications** currently support this direction. The prediction is purely graph-derived and has no known biological rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Myeloid leukemia / acute myeloid leukemia (the registration records list no indication text, so this comes from the knowledge-graph indication data) |
| Predicted New Indication | Bulbar polio |
| TxGNN Prediction Score | 98.59% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 7 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available for this report. Azacitidine is known as a hypomethylating nucleoside analog. Its efficacy in myeloid malignancies is established, and it works by altering DNA methylation and by cytotoxic incorporation into nucleic acids in rapidly dividing cells.

Bulbar polio is a viral infection of motor neurons caused by poliovirus. Azacitidine has no known antiviral activity against poliovirus, and no mechanistic pathway linking it to this disease was identified. The high score (0.986) reflects proximity in the knowledge graph rather than a plausible therapeutic effect. Azacitidine's cytotoxic and myelosuppressive profile would also be a serious concern in an infectious neurological disease. This prediction should be regarded as a model artefact unless independent evidence emerges.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

Azacitidine is marketed in Singapore under 7 valid single-ingredient registrations (injectable and oral forms). The registration records do not include approved indication text, so that column is omitted. The first 5 registrations are shown below.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| SIN13801P | Vidaza powder for suspension for injection 100mg/vial | Injection, powder, for suspension | Baxter Oncology GmbH |
| SIN15875P | Avoxred powder for suspension for injection 100mg/vial | Injection, powder, lyophilized, for suspension | Dr. Reddy's Laboratories Limited |
| SIN16573P | Onureg film-coated tablets 300 mg | Tablet, film coated | Excella GmbH & Co. KG |
| SIN16572P | Onureg film-coated tablets 200 mg | Tablet, film coated | Excella GmbH & Co. KG |
| SIN15118P | Xpreza 100 injection 100 mg/vial | Injection | Natco Pharma Limited / Panacea Biotec Pharma Ltd. |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (hypomethylating nucleoside analog) |
| Myelosuppression Risk | High (neutropenia and thrombocytopenia are expected; the knowledge graph also flags these as contraindication-related conditions) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function, renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: liver failure, kidney disease, pyoureter, thrombocytopenia, neutropenia, agranulocytosis.
- **Drug Interactions**: 85 interactions were recorded. Major-level examples include deferiprone, samarium (153Sm) lexidronam, adalimumab, baricitinib and live BCG vaccine. Moderate-level examples include zidovudine, ganciclovir, azathioprine, alemtuzumab, chloramphenicol and several vaccines.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no clinical trials, no literature and no plausible mechanism, and azacitidine's toxicity profile is unfavourable for this infectious neurological disease. The high model score alone does not justify further investment.

**To proceed, the following is needed:**
- Any independent biological or clinical evidence linking azacitidine to poliovirus infection or motor neuron protection (none was identified)
- Detailed mechanism-of-action data and the HSA package insert warnings and contraindications

**Note on other predictions:** Other candidates for this drug have far better support. Unclassified myelodysplastic syndrome (L2, Proceed with Guardrails) has a Phase 2 final analysis, a registry and supporting reports. Aregenerative anemia (L2, Proceed with Guardrails) has MDS-focused trials and a lower-risk MDS meta-analysis. Both are closer to azacitidine's existing MDS use and are more sensible to evaluate first.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

