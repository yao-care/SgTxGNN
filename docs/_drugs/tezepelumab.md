---
layout: default
title: Tezepelumab
parent: Low Evidence (L5)
nav_order: 968
evidence_level: L5
indication_count: 10
---

# Tezepelumab
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

# Tezepelumab: From Severe Asthma to Diabetic Cataract

## One-Sentence Summary

Tezepelumab is an anti-TSLP monoclonal antibody marketed for severe asthma.
The TxGNN model predicts it may be effective for **diabetic cataract**,
but currently **0 clinical trials** and **0 publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe asthma (the HSA records provided do not list indication text) |
| Predicted New Indication | Diabetic cataract |
| TxGNN Prediction Score | 98.40% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, tezepelumab is an anti-TSLP (thymic stromal lymphopoietin) monoclonal antibody. Its efficacy in severe asthma is established, but the input contains no data on a pathway to diabetic lens opacity.

Diabetic cataract is driven mainly by hyperglycaemia: polyol pathway activation, oxidative stress and protein glycation. Nothing in the provided data connects TSLP blockade to these processes. Any link through inflammatory signalling is speculative.

The ten top predictions are almost all cataract subtypes (diabetic, senile, cortical, nuclear, mature, immature, tetanic, craniostenosis-associated), with scores between 0.981 and 0.984. Such uniformity suggests a knowledge-graph proximity artifact among cataract terms rather than independent biological signals. The prediction should be treated with caution.

The most biologically conceivable of the ten is **diabetic retinopathy** (score 98.1%), because it has a substantial inflammatory component and a TSLP or type 2 alarmin hypothesis is plausible. It is still unverified and is worth a literature review, not a recommendation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form | Manufacturer |
|---------|------|------|-----------|
| SIN16815P | TEZSPIRE Solution for Injection 210 mg in Pre-filled Syringe | Injection, solution | Amgen Manufacturing Limited LLC |
| SIN16817P | TEZSPIRE Solution for Injection 210 mg in Pre-filled Pen | Injection, solution | Amgen Manufacturing Limited LLC |

## Safety Considerations

Please refer to the package insert for safety information.

No drug interaction records were found for this drug.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no trials, no literature and no mechanistic link. The near-identical scores across many cataract subtypes point to a likely model artifact.

**To proceed, the following is needed:**
- HSA package insert (warnings and contraindications), which currently blocks safety screening
- Mechanism of action data, for example from DrugBank
- A literature review of TSLP in lens and retinal disease, prioritising diabetic retinopathy
- Preclinical or observational evidence, such as TSLP levels in ocular fluids or ocular outcomes in treated asthma patients
- Route compatibility assessment: the available route is injectable, and the suitability of systemic injection for lens disease is unassessed
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

