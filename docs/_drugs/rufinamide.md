---
layout: default
title: Rufinamide
parent: Low Evidence (L5)
nav_order: 878
evidence_level: L5
indication_count: 10
---

# Rufinamide
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

# Rufinamide: From Lennox-Gastaut Syndrome to Febrile Infection-Related Epilepsy Syndrome

## One-Sentence Summary

Rufinamide is an oral antiseizure drug. The Singapore registration record does not state its indication, but the published literature describes it as add-on treatment for seizures in Lennox-Gastaut syndrome. The TxGNN model predicts it may help **febrile infection-related epilepsy syndrome (FIRES)**. **No clinical trials and no publications** specific to this prediction were found, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration record. Literature describes add-on treatment of Lennox-Gastaut syndrome seizures |
| Predicted New Indication | Febrile infection-related epilepsy syndrome |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the Evidence Pack. The literature retrieved for this drug describes rufinamide as a triazole derivative that limits sodium-dependent neuronal action potentials by prolonging the inactive state of sodium channels. This is a generic antiseizure mechanism, and the drug is widely used in refractory epilepsy.

FIRES is a highly refractory epileptic encephalopathy that follows a febrile illness, and it is thought to be inflammation-driven. That gives a generic antiseizure rationale for rufinamide. However, no retrieved trial or publication addresses FIRES, and nothing shows that sodium-channel blockade helps with its inflammatory component. The high score probably reflects the model's closeness between FIRES and other refractory epilepsies that rufinamide is used for. It does not show a specific effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Other Predicted Indications

Nine other indications were predicted. Only one has meaningful supporting evidence.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Perioral myoclonia with absences | 99.51% | L5 | No evidence. Sodium-channel blockers can aggravate some generalized seizure types |
| 3 | Cryptogenic late-onset epileptic spasms | 99.44% | L5 | No direct evidence |
| 4 | Photosensitive occipital lobe epilepsy | 99.44% | L5 | Focal epilepsy, so a generic rationale only |
| 5 | Atypical childhood epilepsy with centrotemporal spikes | 99.44% | L5 | Sodium-channel blockers can worsen spike-wave activation in some atypical syndromes |
| 6 | Trigeminal nerve neoplasm | 97.91% | L5 | Probable false positive. No link to tumour biology |
| 7 | Benign occipital epilepsy | 97.75% | L4 | Indirect only, via focal-epilepsy data. The syndrome is often self-limited |
| 8 | Childhood onset epileptic encephalopathy | 97.71% | L3 | See below |
| 9 | Early-onset epileptic encephalopathy with intellectual disability due to GRIN2A mutation | 96.37% | L5 | NMDA-receptor channelopathy, which differs from rufinamide's mechanism |
| 10 | Renal-hepatic-pancreatic dysplasia | 96.26% | L5 | Probable false positive. No plausible mechanism |

**Rank 8 has the strongest support.** Rufinamide is already used for Lennox-Gastaut syndrome, a childhood-onset epileptic encephalopathy, and Phase 3 data exist for it. For other childhood epileptic encephalopathies, the evidence is a multicentre Italian observational study ([20666837](https://pubmed.ncbi.nlm.nih.gov/20666837/)) and reviews. It is capped at L3 because the Phase 3 RCT evidence covers Lennox-Gastaut syndrome only. Its recommendation is "Research Question". Only 10 of 20 literature records were provided for it.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN15146P | INOVELON FILM-COATED TABLET 200 MG | Tablet, film coated (oral) | Not stated in the record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found in the query.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The FIRES prediction is supported by the model score alone (L5), with no trials or publications. The Singapore package insert, which is needed for safety screening, has not been retrieved, so the candidate cannot move past the first screening stage.

**To proceed, the following is needed:**
- Download and parse the HSA package insert to obtain warnings, contraindications and the approved indication
- Retrieve detailed mechanism of action data from DrugBank
- Targeted search for FIRES-specific evidence, such as case series or registry data on antiseizure drugs
- Consider prioritising the "childhood onset epileptic encephalopathy" prediction (rank 8, L3) for expert review, as it has the strongest evidence

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

