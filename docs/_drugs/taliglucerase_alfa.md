---
layout: default
title: Taliglucerase Alfa
parent: Low Evidence (L5)
nav_order: 943
evidence_level: L5
indication_count: 10
---

# Taliglucerase Alfa
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

# Taliglucerase alfa: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Taliglucerase alfa is a recombinant enzyme replacement therapy that is marketed in Singapore as ELELYSO and appears to be used for Gaucher disease. The TxGNN model predicts it may be effective for **Hurler syndrome** (MPS I), but there are **0 clinical trials** and **0 publications** supporting this prediction. The prediction rests on model output alone, and the mechanism does not support it.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gaucher disease (inferred from the literature; the Singapore registration record gives no indication text) |
| Predicted New Indication | Hurler syndrome |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L5 |
| Singapore Market Status | ✓ Marketed |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the input. Taliglucerase alfa is a recombinant glucocerebrosidase that breaks down glucosylceramide. Its on-label use is replacing this deficient enzyme in Gaucher disease.

Hurler syndrome is caused by a different deficiency, alpha-L-iduronidase, which leads to accumulation of glycosaminoglycans. Glucocerebrosidase does not act on these substances, so there is no direct mechanistic link. The high score most likely reflects the two diseases sitting close together in the knowledge graph as lysosomal storage diseases, not a shared pathway. This should be read as a model artifact, not a repurposing signal.

The other top-ranked predictions show the same pattern. These include Scheie syndrome, Wolman disease and cholesteryl ester storage disease, none of which has a plausible mechanistic link. The one exception is rank 6, "lysosomal storage disease with skeletal involvement". Its supporting papers concern Gaucher disease, the drug's known use, so they are not repurposing evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Singapore Market Information

| Authorization Number | Product Name | Dosage Form |
|---------|------|------|
| SIN16770P | ELELYSO Powder for Concentrate for Solution for Infusion 200 units/vial (Pharmacia and Upjohn Company LLC) | Lyophilized powder for injection |

The registration record does not include approved indication text.

## Safety Considerations

Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Hurler syndrome prediction has no trials, no literature and no mechanistic link, so it stays at evidence level L5. The enzyme and substrate differ from the disease defect, and a dedicated therapy (iduronidase replacement) already exists for this condition.

**To proceed, the following is needed:**
- Singapore package insert warnings and contraindications (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- A documented original indication for the drug record
- Any preclinical or clinical evidence linking glucocerebrosidase replacement to MPS I, without which the prediction should not advance

*This report is for research reference only and does not constitute medical advice. Repurposing candidates require clinical validation before any use.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

