---
layout: default
title: Atovaquone
parent: Low Evidence (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
---

# Atovaquone
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

# Atovaquone: From Antiparasitic Use (MALARONE) to Leprosy

## One-Sentence Summary

Atovaquone is registered in Singapore as MALARONE tablets. The supplied record lists no original indication, but the product is an antimalarial atovaquone-proguanil combination.
The TxGNN model predicts it may be effective for **leprosy** (score 94.2%), but there are **0 clinical trials** and **1 publication**, and that publication is not about atovaquone in leprosy.
The prediction is therefore best treated as a likely artefact. The best-supported candidate for this drug is toxoplasmosis (see the conclusion).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the supplied data (the HSA license text is empty) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 94.24% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for this drug record is not available. Atovaquone is known to inhibit the cytochrome bc1 complex in apicomplexan parasites such as *Toxoplasma gondii*. That is a protozoal target, and no link to *Mycobacterium leprae* is documented in the supplied data.

The only paper linked to the leprosy prediction (PMID 32310272) studies clofazimine, a leprosy drug, against *Babesia microti*. It does not study atovaquone against leprosy. The prediction most likely comes from a shared knowledge-graph neighbourhood (antiparasitic or antimicrobial drugs, Babesia) rather than a validated mechanism.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32310272](https://pubmed.ncbi.nlm.nih.gov/32310272/) | 2020 | Case report/series (as classified) | The Journal of Infectious Diseases | Tests clofazimine, a leprosy and tuberculosis antibiotic, against *Babesia microti* in immunocompromised hosts, where atovaquone resistance has been reported. It does not evaluate atovaquone for leprosy. |

---

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09761P | MALARONE TABLET | Tablet, film coated (oral) | Not provided in the supplied data |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leprosy prediction has no trials, no relevant literature and no plausible mechanism, so it stays at L5. The drug's other predicted indications are much better supported and are worth reviewing instead:

| Predicted Indication | Evidence Level | Pack Recommendation | Basis |
|------|------|------|------|
| Toxoplasmosis | L2 | Proceed with Guardrails | Phase 2 randomized trial NCT00000794 (n=100), salvage pilot NCT00001994, and a plausible cytochrome bc1 mechanism |
| Ocular toxoplasmosis | L3 | Research Question | Small case series and case reports only; no randomized ocular data |
| Nocardiosis | L4 | Hold | Literature suggests a possible signal against benefit, with more nocardial infections in the atovaquone prophylaxis era (PMID 29555315) |

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (blocking gap DG001)
- Mechanism of action data from DrugBank (gap DG002)
- The original approved indication, to confirm whether toxoplasmosis use is already on-label or guideline-recommended in Singapore before treating it as repurposing
- For leprosy specifically, any *M. leprae* in vitro or in vivo data for atovaquone; without it, no further work is justified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

