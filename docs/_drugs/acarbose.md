---
layout: default
title: Acarbose
parent: Low Evidence (L5)
nav_order: 26
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Acarbose: predicted new indication Focal stiff limb syndrome (evidence level L5). Approved use: Type 2 diabetes mellitus"
monitor_inn: "Acarbose"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
---

# Acarbose
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

# Acarbose: From Type 2 Diabetes Mellitus to Focal Stiff Limb Syndrome

## One-Sentence Summary

Acarbose is an oral intestinal alpha-glucosidase inhibitor, originally used to control blood sugar in type 2 diabetes mellitus.
The TxGNN model's top-ranked prediction is **focal stiff limb syndrome**, but this is a graph-based prediction only, with **0 clinical trials** and **0 publications** supporting it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus |
| Predicted New Indication | Focal stiff limb syndrome |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Acarbose inhibits alpha-glucosidases in the small intestine, which slows carbohydrate digestion and reduces the rise in blood glucose after meals. Detailed mechanism-of-action data was not available in the compiled data, but this is its well-known pharmacology.

Focal stiff limb syndrome is a neurological, likely autoimmune, disorder involving impaired GABAergic and glycine signalling in the central nervous system. Acarbose acts only in the gut and has no known effect on this pathway. The high score probably reflects links in the knowledge graph (for example, the association of stiff-person-spectrum disorders with diabetes) rather than a real pharmacological connection. There is no plausible mechanistic reason for this prediction at present.

The same pattern holds for the other top-ranked predictions, including classic stiff person syndrome, thiamine-responsive dysfunction syndrome, opsismodysplasia and several localized lipodystrophies. None has any supporting trial or publication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN07861P | GLUCOBAY 50 TABLET 50 mg (Bayer AG) | Tablet |
| SIN15816P | GARBOSE TABLET 50MG (Y.S.P. Industries) | Tablet |
| SIN15815P | GARBOSE TABLET 100MG (Y.S.P. Industries) | Tablet |

All three are valid single-ingredient oral tablet licences. Approved indication text was not available in the data compiled for this report.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** kidney disease, pyoureter, liver disease, gallbladder disease, cirrhosis of liver, inflammatory bowel disease, hypoglycemia, injury.
- **Drug Interactions:** 100 interactions were recorded. The first 20 retrieved are Minor or Moderate, and no Major interactions appear among them. Moderate-level examples include:
  - acetazolamide
  - salbutamol
  - alpelisib
  - amprenavir
  - atazanavir
  - aripiprazole
  - asenapine
  - bedaquiline
  - bendroflumethiazide
  - betamethasone
  - asparaginase products
  - aloe vera leaf

For label-based warnings and precautions, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. There are no registered trials or publications for focal stiff limb syndrome, and acarbose has no plausible effect on its underlying neurological pathology.

**To proceed, the following is needed:**
- Any clinical or preclinical evidence linking acarbose to stiff limb or stiff-person-spectrum disorders. Without it, this candidate should not advance.
- The Singapore package insert, to confirm label warnings, contraindications and approved indications.
- Confirmation of the mechanism of action from DrugBank.

**Side note on a more credible prediction:** Among the lower-ranked predictions, **type 1 diabetes mellitus** (TxGNN score 98.39%) has a plausible mechanism, as adjunct therapy to insulin that blunts post-meal glucose spikes. It also has controlled-study literature, including a double-blind placebo-controlled study ([PMID 10227568](https://pubmed.ncbi.nlm.nih.gov/10227568/)), a multicentre study ([PMID 9051366](https://pubmed.ncbi.nlm.nih.gov/9051366/)) and a network meta-analysis ([PMID 33300282](https://pubmed.ncbi.nlm.nih.gov/33300282/)). Reported benefits appear modest and gastrointestinal side effects are a concern. If a diabetes-related repurposing direction is of interest, this indication should be evaluated as a separate candidate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

