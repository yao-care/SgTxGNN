---
layout: default
title: Valproic Acid
parent: Low Evidence (L5)
nav_order: 1043
evidence_level: L5
indication_count: 10
---

# Valproic Acid
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

# Valproic Acid: From Antiepileptic Therapy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Valproic acid is a long-established antiseizure medicine, and 11 Singapore registrations cover injectable, oral tablet and syrup forms.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, with a very high model score.
In practice, **0 clinical trials** and only **1 publication** (on a different disease) support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 11 |
| Recommended Decision | Hold |

The HSA records provided contain no approved-indication text, so the original indication is not listed here. The "antiseizure" label in this report comes from the retrieved literature, not from the registration data.

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the HSA/DrugBank inputs. Valproic acid is known as a histone deacetylase inhibitor with some preclinical antineoplastic interest. It is also an antiseizure drug that enhances GABAergic inhibition and blocks sodium channels.

The data does not link these properties to trigeminal nerve tumours. The only retrieved paper is a 1997 case series on Sturge-Weber syndrome, which is a different disease. The high score therefore appears to come from knowledge-graph proximity rather than a supported biological rationale. Treat the prediction as a model signal, not a mechanistic argument.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years (clinical features, evolution, treatment response). It does not address trigeminal nerve tumours. |

## Singapore Market Information

Showing 5 of 11 registrations. The records contain no approved-indication text.

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|------|
| SIN16642P | VALPROATE-AFT Solution for Infusion/Injection 100 mg/ml | Injection, solution | LABIANA Pharmaceuticals |
| SIN15525P | Sodium Valproate Aguettant Solution for Injection 400 mg/4 ml | Injection, solution | Laboratoire Aguettant |
| SIN05215P | Epilim 400 mg Powder for Injection/Infusion | Injection, powder, for solution | sanofi S.R.L / Chinoin Pharmaceutical and Chemical Works (solvent) |
| SIN05690P | Epilim 200 Tablet 200 mg | Enteric coated tablet | Sanofi-Aventis S.A |
| SIN15343P | Sodium Valproate Wockhardt Solution for Injection or Infusion 100 mg/ml | Injection, solution | CP Pharmaceuticals Limited |

Other dosage forms across the 11 registrations include syrup and film-coated tablet.

## Safety Considerations

Please refer to the package insert for safety information.

The retrieved literature for related seizure indications points to teratogenicity and fetal neurodevelopmental risk, hepatotoxicity, and an interaction with carbapenem antibiotics.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The 99.97% model score is not backed by any clinical trial, mechanism or relevant publication for trigeminal nerve neoplasm. Evidence is L5 (model prediction only). The only retrieved paper concerns a different disease.

**To proceed, the following is needed:**
- HSA package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank, to assess any biological link to tumours of the trigeminal nerve
- Targeted literature searches for valproate in cranial nerve or nerve-sheath tumours
- A decision on whether the other predictions for this drug should be pursued instead. These are visual epilepsy (L3, Proceed with Guardrails), and trigeminal neuralgia, startle epilepsy and reading seizures (Research Question).

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

