---
layout: default
title: Gadobutrol
parent: Low Evidence (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Gadobutrol
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

# Gadobutrol: From MRI Contrast Imaging to Benign Prostatic Hyperplasia

## One-Sentence Summary

Gadobutrol is a gadolinium-based contrast agent used in MRI. It is a diagnostic agent, not a treatment.
The TxGNN model predicts it may be effective for **benign prostatic hyperplasia (BPH)**,
but **no clinical trials and no publications** support this prediction, so it is a model-only signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Singapore registration records. Gadobutrol is an extracellular gadolinium-based MRI contrast agent. |
| Predicted New Indication | Benign prostatic hyperplasia |
| TxGNN Prediction Score | 83.24% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the record. Gadobutrol is an extracellular gadolinium-based MRI contrast agent. Its gadolinium chelate shortens T1 relaxation time and so brightens vessels and tissues on scans. It has no known pharmacological action on prostate tissue.

The 0.83 graph score is most likely a knowledge-graph artifact rather than a real biological link. The dataset contains no trial or publication that connects gadobutrol to BPH. This prediction is not considered mechanistically plausible.

For context, the model's next-ranked predictions show a similar pattern:
- **Peripheral arterial disease** (score 76.7%) and **peripheral vascular disease** (score 74.4%) have diagnostic evidence only. This includes Phase 4 MR angiography comparisons in which gadobutrol was the comparator, and several prospective studies against digital subtraction angiography. These show gadobutrol works well as an imaging agent for these diseases. They do not show any therapeutic effect, so this is not drug repurposing.
- **Disease of orbital region** has only indirect MRI diagnostic trials in which the contrast agent is not specified.
- The remaining predictions (cauda equina syndrome, strongyloidiasis, prostate calculus, neurogenic bladder, iritis, hypertrichosis) have no supporting trials or literature.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN12399P | GADOVIST INJECTION 1.0 mmol/ml | Injection |
| SIN13807P | GADOVIST 1MMOL/ML PREFILLED SYRINGE 5.0 ML | Injection |

Both products are made by Bayer AG. The approved indication text was not provided in the records.

## Safety Considerations

Please refer to the package insert for safety information. No drug interactions were found in the queried database.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The BPH prediction rests only on a model score, with no trials, no literature and no plausible mechanism. Gadobutrol is a diagnostic imaging agent. The peripheral vascular disease findings are established diagnostic use, not therapeutic repurposing.

**To proceed, the following is needed:**
- The HSA package insert, to confirm approved indications and complete safety screening (currently blocking)
- Formal mechanism of action data from DrugBank
- Any preclinical or clinical evidence linking gadobutrol to BPH. Without it, this candidate should not advance beyond model prediction.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

