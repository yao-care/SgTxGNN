---
layout: default
title: Riluzole
parent: Low Evidence (L5)
nav_order: 860
evidence_level: L5
indication_count: 10
---

# Riluzole
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

# Riluzole: From Amyotrophic Lateral Sclerosis (ALS) to Bilateral Parasagittal Parieto-Occipital Polymicrogyria

## One-Sentence Summary

Riluzole is a glutamate-modulating neuroprotective drug, best known as the first-line disease-modifying treatment for ALS. The TxGNN model's top-ranked prediction for it is **bilateral parasagittal parieto-occipital polymicrogyria**, a cortical malformation. **No clinical trials and no publications** support this prediction, and the high score appears to be a model artifact rather than a clinical signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | ALS (inferred from the supplied literature; the Singapore registration record does not state an indication) |
| Predicted New Indication | Bilateral parasagittal parieto-occipital polymicrogyria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 (model prediction only) |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the source record. Based on the supplied literature, riluzole inhibits glutamate release, blocks voltage-gated sodium channels and modulates postsynaptic glutamate signaling. This counters excitotoxicity in motor neurons, and its benefit in ALS is modest (survival extended by roughly 2–3 months, per the supplied reviews).

The predicted indication is a structural cortical malformation caused by defects in neuronal migration or organization during development. Riluzole's anti-excitotoxic and sodium-channel effects do not address a structural developmental defect. We found no credible mechanistic link. The very high TxGNN score (0.9999; model rank 236) most likely reflects graph-propagation noise.

The model's other top-10 predictions are also mostly weak (skeletal dysplasias, ultra-rare syndromes, mitochondrial myopathy). The plausible ones are all in the motor neuron disease family: lower motor neuron syndrome with late-adult onset, monomelic amyotrophy, Mills syndrome and ALS type 22. These are hypotheses only, with no supporting trials or literature. The ALS-susceptibility entity (rank 8) reflects an already-established use, not repurposing.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| SIN09426P | RILUTEK TABLET 50 mg (Opella Healthcare International SAS) | Film-coated tablet (oral) | Not stated in the registration record |

## Safety Considerations

Please refer to the package insert for safety information. No drug interaction records were found for riluzole in the queried source.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone, with no trials, no literature and no plausible mechanism. Riluzole's mechanism does not fit a structural neurodevelopmental malformation, so this candidate should not advance.

**To proceed, the following is needed:**
- Singapore HSA package insert (warnings, contraindications and approved indication), which is a blocking gap for safety screening
- Mechanism of action data from DrugBank
- A mechanistic or preclinical rationale for polymicrogyria, if the candidate is to be reconsidered
- Consider redirecting review effort to the motor neuron disease candidates (lower motor neuron syndrome, Mills syndrome, ALS type 22), which are flagged as research questions. Their evidence is indirect and should be verified against primary RCT sources.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

