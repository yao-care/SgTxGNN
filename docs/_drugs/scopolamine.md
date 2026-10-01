---
layout: default
title: Scopolamine
parent: Low Evidence (L5)
nav_order: 888
evidence_level: L5
indication_count: 10
---

# Scopolamine
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

# Scopolamine: From an Unrecorded Original Indication to Cauda Equina Syndrome

## One-Sentence Summary

Scopolamine is a non-selective muscarinic (anticholinergic) drug, and the Singapore registration records do not state its approved indication.
The TxGNN model predicts it may be effective for **Cauda Equina Syndrome**, but **0 clinical trials** and **0 supporting publications** were found.
The prediction is model-only (L5), so the recommendation is **Hold**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration records |
| Predicted New Indication | Cauda equina syndrome |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 6 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available. Scopolamine is a non-selective muscarinic antagonist, and antimuscarinics reduce detrusor (bladder muscle) overactivity. This is general pharmacology, not drug-specific data.

The link to cauda equina syndrome is plausible only for the bladder-dysfunction component. Scopolamine would not treat the underlying nerve-root compression, which needs surgical decompression. Its effects on the central nervous system are also a concern.

The model's other top-ranked predictions are also weak:

- **Obsolete neurogenic bladder (score 99.98%):** The mechanism is sound, since antimuscarinics are established for neurogenic detrusor overactivity. However, better-studied agents (oxybutynin, solifenacin, trospium) already exist. Scopolamine's CNS penetration and cognitive side effects make it a poor candidate. The disease term is obsolete in the ontology and should be remapped to a current term.
- **Conjunctivitis variants (papillary, atopic, rosacea, vernal; 99.08–99.98%):** There is no credible mechanistic rationale. These conditions are driven by mechanical irritation, allergy or gland dysfunction. Anticholinergic drying may worsen dry eye.
- **Nasal cavity disease and acute laryngopharyngitis (98.87–98.99%):** Reduced secretions are conceivable, but the terms are nonspecific or the disease is mostly self-limiting, and mucosal drying may worsen symptoms.
- **Idiopathic uveal effusion syndrome and idiopathic panuveitis (98.14–98.30%):** Topical cycloplegics are already used as symptomatic support in uveitis. This is supportive care, not a repurposing signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Only one publication was retrieved, and it does not support the predicted indications. It is listed under "nasal cavity disease" (score 98.99%, rank 7).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31183806](https://pubmed.ncbi.nlm.nih.gov/31183806/) | 2019 | Preclinical (animal model) | Molecular Neurobiology | Intranasal melanin-concentrating hormone improved memory in scopolamine-induced memory-impaired and Alzheimer's disease mouse models. Scopolamine appears as the amnesia-inducing agent, not as a treatment. |

## Singapore Market Information

Six registrations are on record. The records for the five listed below carry no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN07796P | FUCON INJECTION 20 mg/ml | Injection | Not recorded |
| SIN09563P | VACOPAN INJECTION 20 mg/ml | Injection | Not recorded |
| SIN02854P | HYOMIDE TABLET 10 mg | Tablet, sugar coated | Not recorded |
| SIN07177P | FUCON CAPSULE 10 mg | Capsule | Not recorded |
| SIN16636P | YSP HYOSCINE INJECTION 20MG/ML | Injection, solution | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All ten predictions are model-only (L5), with no clinical trials. The only retrieved paper is a preclinical study that uses scopolamine as an amnesia-inducing agent, not as a therapy. Mechanistic plausibility is limited to bladder symptoms (and, indirectly, ocular cycloplegia), and CNS adverse effects and better alternatives weigh against it.

**To proceed, the following is needed:**
- The HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- The approved indications for the Singapore registrations
- A remapped current term for "obsolete neurogenic bladder"
- A targeted search for studies on antimuscarinic use in neurogenic bladder or cauda equina bladder dysfunction, with comparison against existing agents
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

