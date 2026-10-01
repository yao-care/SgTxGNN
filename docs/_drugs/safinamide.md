---
layout: default
title: Safinamide
parent: Low Evidence (L5)
nav_order: 883
evidence_level: L5
indication_count: 10
---

# Safinamide
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

# Safinamide: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Safinamide is an oral add-on therapy for Parkinson's disease. It acts through reversible MAO-B inhibition plus non-dopaminergic effects.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**, but **no clinical trials and no publications** were found to support this prediction.
It is a model-only signal (evidence level L5) and should be treated as a hypothesis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson's disease (add-on therapy). This comes from the drug's known use, not from the Singapore license text, which is blank |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the Evidence Pack. Safinamide is known to inhibit MAO-B reversibly. It also blocks voltage-gated sodium channels and modulates glutamate release. In theory, the last two actions could touch the excitotoxic and seizure components of Rasmussen encephalitis.

The link is weak, though. Rasmussen encephalitis is an immune-mediated disease driven by T-cell inflammation, and MAO-B inhibition does not address that process. The high TxGNN score is a knowledge-graph signal, not clinical evidence. At most, safinamide might offer symptomatic or neuroprotective support, not disease modification.

The other nine predictions in the set are also model-only. Two have a clearer mechanistic rationale than the top-ranked disease:
- **Juvenile paralysis agitans (Hunt)** has a parkinsonian phenotype, so the prediction can be seen as an extrapolation from the adult Parkinson's indication.
- **Lewy body dementia** shares alpha-synuclein pathology and dopaminergic deficit with Parkinson's disease. Dopaminergic agents may worsen psychosis in this population, so cognitive and psychiatric effects are uncertain.

Both are flagged as research questions rather than candidates for development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16615P | EQUFINA FILM-COATED TABLET 50MG | Tablet, film coated (oral) |

The approved indication text is not stated in the registration record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no trials or publications, and the proposed mechanism does not fit an immune-mediated encephalitis. The package insert has not been reviewed, so the safety screen cannot start.

**To proceed, the following is needed:**
- The HSA package insert (warnings and contraindications), downloaded and parsed
- The approved indication text for SIN16615P, so the original indication is confirmed from the Singapore label
- Mechanism-of-action data from DrugBank
- A targeted literature and trial-registry search for safinamide in Rasmussen encephalitis
- A separate evidence search for juvenile parkinsonism and Lewy body dementia, the two mechanistically closer predictions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

