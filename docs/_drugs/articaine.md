---
layout: default
title: Articaine
parent: Low Evidence (L5)
nav_order: 111
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Articaine: predicted new indication Gout (evidence level L5). Approved use: Not available"
monitor_inn: "Articaine"
predicted_indications: ["gout", "exostosis", "allergic asthma", "intrinsic asthma", "exostoses, multiple,", "hypotrichosis simplex of the scalp", "alopecia", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "congenital hypotrichosis milia"]
---

# Articaine
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

## Articaine: From Local Anaesthesia to Gout
{: .text-alpha }

## One-Sentence Summary

Articaine is an amide-type local anaesthetic, marketed in Singapore as an injectable (the product names point to dental use, but no approved indication text is on file).
The TxGNN model predicts it may be effective for **gout**, but **no clinical trials and no supporting publications** exist for this prediction.
The high score appears to be a graph-based artefact rather than a biologically grounded signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (no approved indication text in the registrations; drug class is local anaesthetic) |
| Predicted New Indication | Gout |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 5 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Articaine is known to be an amide local anaesthetic that blocks voltage-gated sodium channels, producing reversible loss of nerve conduction.

Gout, in contrast, is driven by monosodium urate crystal deposition and NLRP3 inflammasome-mediated inflammation. No clear mechanistic link between sodium channel blockade and urate-driven inflammation was identified. The high TxGNN score is best read as a pattern from the knowledge graph, not as evidence of therapeutic benefit.

Other top-ranked predictions (exostosis, asthma subtypes, alopecia and rare COL4A1-related disorders) likewise lack plausible mechanisms or supporting data. The only publications found for any of them concern local anaesthetic allergy (under allergic asthma), which describes an adverse-reaction context rather than a treatment.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for gout.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN05504P | UBISTESIN INJECTION | Injection | Not stated |
| SIN12648P | CITOCARTIN 100 INJECTION 1.7 ml/cartridge | Injection | Not stated |
| SIN05505P | UBISTESIN FORTE INJECTION | Injection | Not stated |
| SIN15913P | ARTINIBSA 4% WITH EPINEPHRINE SOLUTION FOR INJECTION 1:100000 | Injection, solution | Not stated |
| SIN14537P | Posicaine-100 Injection | Injection, solution | Not stated |

All five registrations are valid single-ingredient products.

## Safety Considerations

- **Drug Interactions**: 10 interactions were identified. The most significant is **Major** with nitrous acid. Hyaluronidase is **Minor**. The remainder are **Moderate**: liposomal morphine and other local anaesthetics (topical benzocaine, lidocaine, cinchocaine and tetracaine; ophthalmic lidocaine, oxybuprocaine and tetracaine).
- **Knowledge-graph contraindication signals** (from drug-disease links, not label text): hypertension and other cardiovascular disease (including coronary artery disease, myocardial infarction, heart conduction disease, sudden cardiac arrest and dilated cardiomyopathy), kidney disease, liver disease, gallbladder disease, diabetes mellitus and diabetic ketoacidosis, angle-closure glaucoma, myasthenia gravis and other neuromuscular junction disease, butyrylcholinesterase deficiency, hyperthyroidism (Graves disease, thyrotoxicosis), Parkinson disease and hemoglobinopathy. These should be verified against the official label.

Please refer to the package insert for the approved warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials or supportive publications, and no plausible biological link between sodium channel blockade and gout. Route compatibility and similarity to the original indication have not been assessed.

**To proceed, the following is needed:**
- Mechanism of action data and a credible mechanistic rationale linking articaine to gout pathophysiology
- Preclinical or clinical evidence in gout or urate-crystal inflammation
- Approved indication text and package insert warnings and contraindications from the Singapore regulator
- Route-of-administration compatibility assessment, since all registered products are injectables for local anaesthesia
- Review of the knowledge-graph contraindication signals, particularly cardiovascular, renal and hepatic conditions, which are common in gout patients
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

